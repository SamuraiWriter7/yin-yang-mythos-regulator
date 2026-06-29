# Changelog

All notable changes to this project will be documented in this file.

This project follows a lightweight pre-release structure during early protocol formation.

---

## [Unreleased]

### Planned

* Add Defensive Repair Loop schema.
* Add Agent Permission Boundary schema.
* Add Trace Receipt Bridge documentation.
* Add Multi-Wing Defensive Orchestration model.
* Add more examples for agent design, workflow review, and system prompt regulation.

---

## [0.1.0-candidate] - 2026-06-29

### Added

* Created initial repository structure for **Yin-Yang Mythos Regulator**.
* Added `schemas/mythos-regulation-record.schema.json`.
* Added `examples/mythos-regulation-record.example.yaml`.
* Added `scripts/validate_examples.py`.
* Added GitHub Actions workflow for schema/example validation.
* Added `requirements.txt` with validation dependencies.

### Defined

* Defined the initial **Mythos Regulation Record**.
* Defined the core yin-yang regulation model:

  * Yang Wing: abstract vulnerability observation.
  * Yin Wing: defensive repair and boundary preservation.
  * Kazene Core: traceable regulation flow.
* Defined offensive-to-defensive regulation shift:

  * from exploit-seeking or over-autonomous tendency
  * to repair-first, boundary-preserving, human-reviewed operation.
* Defined required safeguards:

  * no exploit execution steps
  * no unauthorized intrusion guidance
  * no malicious code
  * no credential theft
  * no persistence or evasion
  * no harmful payloads
  * no real-target attack instructions
* Defined required constraints:

  * repair-first framing
  * abstract risk only
  * trace required
  * human review required
  * least privilege
  * no unauthorized testing
  * defensive verification only

### Validated

* Confirmed that `mythos-regulation-record.example.yaml` validates against `mythos-regulation-record.schema.json`.
* Confirmed that the GitHub Actions workflow passes successfully.

### Philosophy

* Established the core principle:

  > Offensive insight is not executed; it is regulated into defensive repair.

* Positioned the project as a defensive protocol for converting high-capability AI observation into repair, verification, and traceable review.

---

## [0.1.0] - Pending

### Expected

* Promote `0.1.0-candidate` to `0.1.0` after README, changelog, and release notes are finalized.
* Tag the first stable pre-release.
* Publish initial release notes.
