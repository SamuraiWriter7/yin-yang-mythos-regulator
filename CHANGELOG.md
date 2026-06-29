# Changelog

All notable changes to this project will be documented in this file.

This project follows a lightweight pre-release structure during early protocol formation.

---

## [Unreleased]

### Planned

* Add external receipt mapping profiles.
* Add signed trace receipt examples.
* Add cross-protocol synchronization examples.
* Add defensive governance templates.
* Add multi-agent review flow examples.
* Consider a separate continuation repository after the v0.5 first arc.

---

## [0.5.0-candidate] - 2026-06-29

### Added

* Added `schemas/multi-wing-defensive-orchestration.schema.json`.
* Added `examples/multi-wing-defensive-orchestration.example.yaml`.
* Added `docs/multi-wing-defensive-orchestration.md`.
* Updated `scripts/validate_examples.py` to validate v0.1, v0.2, v0.3, v0.4, and v0.5 examples.
* Updated `README.md` with v0.5 Multi-Wing Defensive Orchestration documentation.
* Updated `CHANGELOG.md` with v0.5 candidate notes.

### Defined

* Defined the **Multi-Wing Defensive Orchestration** layer.

* Defined the core orchestration sequence:

  ```text
  Finder -> Analyst -> Repair -> Verifier -> Boundary -> Bridge -> Human Gate -> Trace Core
  ```

* Defined the main orchestration principle:

  > No wing may complete the loop alone.

* Defined orchestration policy:

  * no single wing completion
  * human review required
  * trace required
  * execution requires Human Gate
  * least privilege required
  * external export requires review
  * unsafe detail expansion not allowed

* Defined specialized wings:

  * Finder Wing
  * Analyst Wing
  * Repair Wing
  * Verifier Wing
  * Boundary Wing
  * Bridge Wing
  * Human Gate
  * Trace Core

* Defined wing-level controls:

  * wing ID
  * wing type
  * role
  * responsibility
  * input sources
  * output targets
  * allowed outputs
  * prohibited outputs
  * execution allowance
  * review requirement
  * trace requirement

* Defined handoff rules:

  * Finder Wing to Analyst Wing
  * Analyst Wing to Repair Wing
  * Repair Wing to Verifier Wing
  * Verifier Wing to Boundary Wing
  * Boundary Wing to Bridge Wing
  * Bridge Wing to Human Gate
  * Human Gate to Trace Core

* Defined handoff conditions:

  * after trace recorded
  * after review gate
  * after boundary check
  * after verification checklist
  * after safe export check
  * after human review

* Defined blocking conditions:

  * unsafe detail detected
  * unclear authorization
  * missing trace
  * missing review gate
  * boundary failure
  * human review required
  * external export requested
  * deployment requested
  * permission expansion requested
  * single wing completion attempted
  * residual risk unrecorded

* Defined required actions:

  * stop
  * pause
  * block
  * escalate to human review
  * record and pause
  * remove unsafe detail
  * return to previous wing
  * provide defensive alternative

* Defined orchestration receipt:

  * origin question
  * orchestration summary
  * wing outputs
  * handoff chain
  * blocked conditions
  * review decision
  * residual risks
  * final status

* Defined review decision states:

  * not reviewed
  * review required
  * approved for documentation
  * approved for staging
  * approved for export
  * blocked

* Defined final orchestration statuses:

  * drafted
  * ready for review
  * review required
  * approved for documentation
  * export ready
  * blocked

### Philosophy

* Extended the v0.1 principle:

  > Offensive insight is not executed; it is regulated into defensive repair.

* Extended the v0.2 principle:

  > Defensive repair is not a one-time answer; it is a traceable loop.

* Extended the v0.3 principle:

  > Capability must pass through permission boundaries before action.

* Extended the v0.4 principle:

  > Defensive regulation must be exportable as traceable receipt.

* Added the v0.5 principle:

  > No wing may complete the loop alone.

### Notes

* v0.1 defines the furnace.
* v0.2 adds circulation.
* v0.3 draws the boundary before the fire moves.
* v0.4 exports the regulated fire as traceable receipt.
* v0.5 prevents any single wing from completing the loop alone.
* The protocol now covers regulation records, defensive repair loops, agent permission boundaries, trace receipt bridges, and multi-wing defensive orchestration.
* v0.5 can serve as the closing point of the first arc.

---

## [0.4.0-candidate] - 2026-06-29

### Added

* Added `schemas/trace-receipt-bridge.schema.json`.
* Added `examples/trace-receipt-bridge.example.yaml`.
* Added `docs/trace-receipt-bridge.md`.
* Updated `scripts/validate_examples.py` to validate v0.1, v0.2, v0.3, and v0.4 examples.
* Updated `README.md` with v0.4 Trace Receipt Bridge documentation.
* Updated `CHANGELOG.md` with v0.4 candidate notes.

### Defined

* Defined the **Trace Receipt Bridge** as the v0.4 external trace export layer.

* Defined the core bridge sequence:

  ```text
  Internal Regulation -> Trace Receipt Bridge -> External Receipt
  ```

* Defined the main bridge principle:

  > Defensive regulation must be exportable as traceable receipt.

* Defined source record support:

  * `mythos_regulation_record`
  * `defensive_repair_loop`
  * `agent_permission_boundary`
  * `trace_receipt_bridge`
  * `other`

* Defined bridge target support:

  * `external_trace_receipt`
  * `audit_record`
  * `provenance_record`
  * `royalty_record`
  * `memory_record`
  * `other`

* Defined external compatibility options:

  * `ai_search_trace_receipt`
  * `kazene_trace_receipt`
  * `synchronization_audit_protocol`
  * `origin_structure_market`
  * `royalty_hook`
  * `memory_breathing_protocol`
  * `other`

* Defined exported field support:

  * origin question
  * target summary
  * regulation shift
  * repair loop summary
  * permission boundary summary
  * stop conditions
  * review gates
  * trace policy
  * human review
  * residual risks
  * final status
  * source chain
  * safety boundary

* Defined normalized export payload:

  * origin question
  * target summary
  * regulation summary
  * source chain
  * repair summary
  * permission boundary summary
  * review summary
  * residual risks
  * final status

* Defined integrity policy:

  * trace required
  * review required
  * tamper evidence required
  * source chain required
  * hash recommended
  * hash method declaration

* Defined safety boundary requirements:

  * exported records must not include offensive execution details
  * exported records must not include unauthorized intrusion guidance
  * exported records must not include malicious code
  * exported records must not include credential theft
  * exported records must not include sensitive secret values
  * exported records must include defensive context
  * exported records must include source chain
  * exported records must include review status
  * exported records must include residual risk
  * exported records must include human review requirements

* Defined human review gates before:

  * external export
  * publication
  * cross-protocol synchronization
  * deployment
  * always

### Philosophy

* Extended the v0.1 principle:

  > Offensive insight is not executed; it is regulated into defensive repair.

* Extended the v0.2 principle:

  > Defensive repair is not a one-time answer; it is a traceable loop.

* Extended the v0.3 principle:

  > Capability must pass through permission boundaries before action.

* Added the v0.4 principle:

  > Defensive regulation must be exportable as traceable receipt.

### Notes

* v0.1 defines the furnace.
* v0.2 adds circulation.
* v0.3 draws the boundary before the fire moves.
* v0.4 exports the regulated fire as traceable receipt.
* The protocol now covers regulation records, defensive repair loops, agent permission boundaries, and external trace receipt bridges.

---

## [0.3.0-candidate] - 2026-06-29

### Added

* Added `schemas/agent-permission-boundary.schema.json`.
* Added `examples/agent-permission-boundary.example.yaml`.
* Added `docs/agent-permission-boundary.md`.
* Updated `scripts/validate_examples.py` to validate v0.1, v0.2, and v0.3 examples.
* Updated `README.md` with v0.3 Agent Permission Boundary documentation.
* Updated `CHANGELOG.md` with v0.3 candidate notes.

### Defined

* Defined the **Agent Permission Boundary** as the v0.3 permission control layer.

* Defined the core boundary sequence:

  ```text
  Capability -> Permission Boundary -> Action
  ```

* Defined the main boundary principle:

  > Capability must pass through permission boundaries before action.

* Defined the agent profile structure:

  * name
  * role
  * description
  * intended use
  * autonomy level

* Defined autonomy levels:

  * `manual_only`
  * `suggestion_only`
  * `review_required`
  * `bounded_autonomy`
  * `high_risk_blocked`

* Defined permission scope:

  * allowed tools
  * restricted tools
  * prohibited actions

* Defined prohibited actions:

  * self-permission expansion
  * unauthorized testing
  * external target interaction without review
  * production deployment without review
  * irreversible action without review
  * credential collection
  * malicious code generation
  * exploit execution
  * persistence or evasion
  * policy bypass
  * trace suppression
  * human review bypass

* Defined autonomy control:

  * allowed decision types
  * blocked decision types
  * actions requiring review

* Defined stop conditions:

  * unclear authorization
  * external target involvement
  * high-impact action request
  * irreversible action request
  * permission expansion request
  * production change request
  * missing trace
  * missing review gate
  * unsafe or malicious request
  * unclear scope

* Defined review gates:

  * before deployment
  * before permission expansion
  * before external testing
  * before high-impact action
  * before irreversible action
  * before production change
  * before policy change

* Defined trace policy:

  * trace required
  * receipt required for tool use
  * stop condition recording
  * review decision recording
  * minimum trace fields

* Defined deployment policy:

  * allowed environment
  * deployment without review blocked
  * external testing without review blocked
  * rollback required for deployment

### Philosophy

* Extended the v0.1 principle:

  > Offensive insight is not executed; it is regulated into defensive repair.

* Extended the v0.2 principle:

  > Defensive repair is not a one-time answer; it is a traceable loop.

* Added the v0.3 principle:

  > Capability must pass through permission boundaries before action.

### Notes

* v0.1 defines the furnace.
* v0.2 adds circulation.
* v0.3 draws the boundary before the fire moves.
* The protocol now covers regulation records, defensive repair loops, and agent permission boundaries.

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
* Use v0.2 as the baseline for the Defensive Repair Loop layer.

---

## [0.3.0] - Pending

### Expected

* Promote `0.3.0-candidate` to `0.3.0` after validation and review.
* Use v0.3 as the baseline for the Agent Permission Boundary layer.

---

## [0.4.0] - Pending

### Expected

* Promote `0.4.0-candidate` to `0.4.0` after validation and review.
* Use v0.4 as the baseline for the Trace Receipt Bridge layer.

---

## [0.5.0] - Pending

### Expected

* Promote `0.5.0-candidate` to `0.5.0` after validation and review.
* Use v0.5 as the baseline for the Multi-Wing Defensive Orchestration layer.
* Treat v0.5 as the closing point of the first protocol arc.

