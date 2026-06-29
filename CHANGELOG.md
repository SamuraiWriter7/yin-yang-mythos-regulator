# Changelog

All notable changes to this project will be documented in this file.

This project follows a lightweight pre-release structure during early protocol formation.

---

## [Unreleased]

### Planned

* Add Agent Permission Boundary schema.
* Add Trace Receipt Bridge documentation.
* Add Multi-Wing Defensive Orchestration model.
* Add more examples for agent design, workflow review, system prompt regulation, and tool permission review.

---

## [0.2.0-candidate] - 2026-06-29

### Added

* Added `schemas/defensive-repair-loop.schema.json`.
* Added `examples/defensive-repair-loop.example.yaml`.
* Added `docs/defensive-repair-loop.md`.
* Updated `scripts/validate_examples.py` to validate both v0.1 and v0.2 examples.
* Updated `README.md` with v0.2 Defensive Repair Loop documentation.

### Defined

* Defined the **Defensive Repair Loop** as the v0.2 circulation model.

* Defined the core loop sequence:

  ```text
  Observe -> Analyze -> Repair -> Verify -> Record -> Review
  ```

* Defined the loop policy structure:

  * offensive detail expansion control
  * repair-first requirement
  * trace requirement
  * human review requirement
  * allowed environment

* Defined stage records for:

  * observe
  * analyze
  * repair
  * verify
  * record
  * review

* Defined repair output types:

  * policy change
  * permission boundary
  * stop condition
  * logging requirement
  * trace requirement
  * configuration change
  * documentation update
  * test case
  * human review gate

* Defined allowed environments:

  * documentation only
  * local test environment
  * authorized staging environment
  * authorized production with review

* Defined residual risk recording inside the trace receipt.

* Defined mandatory human review gates before deployment or other high-impact changes.

### Philosophy

* Extended the v0.1 principle:

  > Offensive insight is not executed; it is regulated into defensive repair.

* Added the v0.2 principle:

  > Defensive repair is not a one-time answer; it is a traceable loop.

### Notes

* v0.2 turns the initial Mythos Regulation Record into a repair circulation model.
* v0.1 defines the furnace.
* v0.2 adds circulation.

---

## [0.1.0-candidate] - 2026-06-29

### Added

* Created initial repository structure for **Yin-Yang Mythos Regulator**.
* Added `schemas/mythos-regulation-record.schema.json`.
* Added `examples/mythos-regulation-record.example.yaml`.
* Added `scripts/validate_examples.py`.
* Added GitHub Actions workflow for schema/example validation.
* Added `requirements.txt` with validation dependencies.
* Added initial `README.md`.
* Added initial `CHANGELOG.md`.

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

* Promote `0.1.0-candidate` to `0.1.0` after early review if needed.
* Keep `0.1.0-candidate` available as the first candidate release.

---

## [0.2.0] - Pending

### Expected

* Promote `0.2.0-candidate` to `0.2.0` after validation and review.
* Use v0.2 as the baseline for the next Agent Permission Boundary layer.

