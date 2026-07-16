#!/usr/bin/env python3
"""Validate the FP&A knowledge base.

Checks:
  1. Every kpis/*.md (except underscore-prefixed) has valid YAML frontmatter
     with all required keys and allowed enum values.
  2. last_reviewed is a real ISO date; warns (does not fail) if older than
     STALE_DAYS.
  3. Internal markdown links resolve to files that exist in the repo.

Exit code is non-zero if any error is found. Warnings do not fail the build.
"""
from __future__ import annotations

import datetime as dt
import pathlib
import re
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
REQUIRED_KEYS = [
    "id", "name", "domain", "formula", "grain", "source",
    "owner", "favorable_direction", "status", "last_reviewed",
]
ALLOWED_STATUS = {"draft", "approved", "deprecated"}
ALLOWED_DIRECTION = {"up", "down", "neutral"}
STALE_DAYS = 180

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")

errors: list[str] = []
warnings: list[str] = []


def parse_frontmatter(text: str, path: pathlib.Path):
    match = FRONTMATTER_RE.match(text)
    if not match:
        errors.append(f"{path}: missing YAML frontmatter block")
        return None
    try:
        return yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError as exc:
        errors.append(f"{path}: invalid YAML frontmatter ({exc})")
        return None


def validate_kpi(path: pathlib.Path) -> None:
    fm = parse_frontmatter(path.read_text(encoding="utf-8"), path)
    if fm is None:
        return
    for key in REQUIRED_KEYS:
        if key not in fm or fm[key] in (None, ""):
            errors.append(f"{path}: missing required key '{key}'")
    if "status" in fm and fm["status"] not in ALLOWED_STATUS:
        errors.append(f"{path}: status '{fm['status']}' not in {sorted(ALLOWED_STATUS)}")
    if "favorable_direction" in fm and fm["favorable_direction"] not in ALLOWED_DIRECTION:
        errors.append(
            f"{path}: favorable_direction '{fm['favorable_direction']}' "
            f"not in {sorted(ALLOWED_DIRECTION)}"
        )
    reviewed = fm.get("last_reviewed")
    if reviewed is not None:
        try:
            reviewed_date = reviewed if isinstance(reviewed, dt.date) \
                else dt.date.fromisoformat(str(reviewed))
            age = (dt.date.today() - reviewed_date).days
            if age > STALE_DAYS:
                warnings.append(f"{path}: last_reviewed is {age} days old (> {STALE_DAYS})")
        except ValueError:
            errors.append(f"{path}: last_reviewed '{reviewed}' is not an ISO date (YYYY-MM-DD)")


def validate_links(path: pathlib.Path) -> None:
    for link in LINK_RE.findall(path.read_text(encoding="utf-8")):
        if link.startswith(("http://", "https://", "#", "mailto:")):
            continue
        target = link.split("#", 1)[0]
        if not target:
            continue
        if not (path.parent / target).resolve().exists():
            errors.append(f"{path}: dead internal link -> {link}")


def main() -> None:
    kpi_files = [p for p in (ROOT / "kpis").glob("*.md") if not p.name.startswith("_")]
    for path in kpi_files:
        validate_kpi(path)
    for path in ROOT.rglob("*.md"):
        validate_links(path)

    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")

    if errors:
        print(f"\nValidation failed with {len(errors)} error(s).")
        sys.exit(1)
    print(f"Validation passed. {len(kpi_files)} KPI file(s) checked, {len(warnings)} warning(s).")


if __name__ == "__main__":
    main()
