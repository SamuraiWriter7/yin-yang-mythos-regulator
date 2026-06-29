#!/usr/bin/env python3
"""
Validate Yin-Yang Mythos Regulator examples against JSON Schemas.

Validated targets:

* schemas/mythos-regulation-record.schema.json
* examples/mythos-regulation-record.example.yaml

* schemas/defensive-repair-loop.schema.json
* examples/defensive-repair-loop.example.yaml
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]

VALIDATION_TARGETS = [
    {
        "name": "Mythos Regulation Record",
        "schema": ROOT / "schemas" / "mythos-regulation-record.schema.json",
        "example": ROOT / "examples" / "mythos-regulation-record.example.yaml",
    },
    {
        "name": "Defensive Repair Loop",
        "schema": ROOT / "schemas" / "defensive-repair-loop.schema.json",
        "example": ROOT / "examples" / "defensive-repair-loop.example.yaml",
    },
]


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def load_yaml(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def validate_target(name: str, schema_path: Path, example_path: Path) -> bool:
    print(f"[validate] {name}")
    print(f"  schema : {schema_path.relative_to(ROOT)}")
    print(f"  example: {example_path.relative_to(ROOT)}")

    if not schema_path.exists():
        print(f"[error] schema file not found: {schema_path}")
        return False

    if not example_path.exists():
        print(f"[error] example file not found: {example_path}")
        return False

    try:
        schema = load_json(schema_path)
        example = load_yaml(example_path)
    except Exception as error:
        print(f"[error] failed to load files: {error}")
        return False

    try:
        Draft202012Validator.check_schema(schema)
    except Exception as error:
        print(f"[error] invalid JSON Schema: {error}")
        return False

    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(example), key=lambda error: error.path)

    if errors:
        print("[error] validation failed")
        for error in errors:
            path = ".".join(str(part) for part in error.absolute_path)
            location = path if path else "<root>"
            print(f"  - {location}: {error.message}")
        return False

    print(f"[ok] {example_path.name} is valid")
    return True


def main() -> int:
    all_valid = True

    for target in VALIDATION_TARGETS:
        is_valid = validate_target(
            name=target["name"],
            schema_path=target["schema"],
            example_path=target["example"],
        )
        all_valid = all_valid and is_valid

    return 0 if all_valid else 1


if __name__ == "__main__":
    sys.exit(main())


