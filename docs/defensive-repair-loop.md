# Defensive Repair Loop

**Defensive Repair Loop** defines the v0.2 repair cycle of **Yin-Yang Mythos Regulator**.

It extends the v0.1 Mythos Regulation Record from a single regulation record into a traceable defensive loop.

> Defensive repair is not a one-time answer; it is a traceable loop.

---

## Purpose

The purpose of the Defensive Repair Loop is to convert abstract risk observations into verified defensive actions.

In v0.1, the protocol defined the basic regulation shift:

```text
from: How can this be exploited?
to:   What must be protected and repaired?
```

In v0.2, that shift becomes a structured loop:

```text
Observe -> Analyze -> Repair -> Verify -> Record -> Review
```

This loop ensures that offensive or expansive insight is not left as raw risk observation.
Instead, it is converted into repair actions, verification steps, trace receipts, and human review gates.

---

## Core Principle

The Defensive Repair Loop follows one principle:

> Risk observation must return to defensive structure.

The loop does not expand offensive details.
It does not provide exploit execution steps.
It does not authorize testing against real systems.

It converts risk into:

* least-privilege boundaries
* stop conditions
* trace requirements
* logging requirements
* verification checklists
* human review gates
* deployment restrictions
* residual risk records

---

## Loop Structure

```text
┌─────────┐
│ Observe │
└────┬────┘
     ↓
┌─────────┐
│ Analyze │
└────┬────┘
     ↓
┌────────┐
│ Repair │
└────┬───┘
     ↓
┌────────┐
│ Verify │
└────┬───┘
     ↓
┌────────┐
│ Record │
└────┬───┘
     ↓
┌────────┐
│ Review │
└────────┘
```

Each stage must remain defensive, traceable, and reviewable.

---

## Stage 1: Observe

The Observe stage identifies risks at an abstract defensive level.

It may identify:

* boundary gaps
* permission excess
* missing stop conditions
* weak logging
* missing trace receipts
* unclear review gates
* over-autonomous behavior
* unsafe deployment assumptions

It must not expand risk observations into executable offensive instructions.

### Example

```yaml
observe:
  purpose: "Identify defensive risks at an abstract level without expanding offensive details."
  actions:
    - "List boundary gaps."
    - "Identify missing stop conditions."
    - "Identify traceability gaps."
```

---

## Stage 2: Analyze

The Analyze stage classifies the observed risks.

It maps each risk to:

* affected boundary
* priority
* impact level
* repair requirement
* review requirement

This stage determines whether a repair can remain documentation-only, requires local testing, requires staging review, or must be blocked until human approval.

### Example

```yaml
analyze:
  purpose: "Classify impact, priority, and affected boundaries."
  actions:
    - "Assign priority to each risk."
    - "Map each risk to an affected boundary."
    - "Determine whether deployment requires human review."
```

---

## Stage 3: Repair

The Repair stage generates defensive changes.

Repairs should prefer minimum viable defensive changes.

Examples include:

* reducing tool permissions
* adding stop conditions
* adding human review gates
* requiring trace receipts
* improving logs
* updating documentation
* adding verification checklists
* defining rollback requirements

The Repair stage should not produce harmful payloads, exploit paths, or unauthorized testing instructions.

### Example

```yaml
repair:
  purpose: "Generate minimum defensive changes that reduce risk while preserving useful capability."
  actions:
    - "Define least-privilege tool scopes."
    - "Add explicit stop conditions."
    - "Require trace receipts for tool invocation."
    - "Add a human review gate before deployment or permission expansion."
```

---

## Stage 4: Verify

The Verify stage checks whether the repair reduces risk without introducing new failure modes.

Verification may include:

* checklist review
* schema validation
* permission review
* stop-condition testing
* trace receipt review
* staging-environment validation
* human approval confirmation

For documentation-only examples, verification may remain a checklist.
For real systems, verification must be performed only in authorized environments.

### Example

```yaml
verify:
  purpose: "Confirm that repairs reduce risk without introducing new failure modes."
  actions:
    - "Check that every tool permission has a defined purpose and scope."
    - "Check that ambiguous or risky requests trigger stop conditions."
    - "Check that each tool invocation produces a trace receipt."
```

---

## Stage 5: Record

The Record stage creates a traceable receipt for the full repair cycle.

It records:

* origin question
* loop summary
* stage order
* transformation
* residual risks
* final status
* review requirements

This ensures that the repair process is not merely an answer, but a reviewable record.

### Example

```yaml
record:
  purpose: "Create a traceable receipt for the defensive repair cycle."
  actions:
    - "Record the origin question."
    - "Record the transformation from autonomy-first to repair-first."
    - "Record residual risks."
    - "Record human review requirements."
```

---

## Stage 6: Review

The Review stage routes high-impact changes to accountable human review.

Review is required before:

* deployment
* permission expansion
* external testing
* high-impact actions
* irreversible actions
* policy changes
* production use

The loop must block deployment or permission expansion until the required review is completed.

### Example

```yaml
review:
  purpose: "Route high-impact changes to accountable human review before deployment."
  actions:
    - "Require review by a system owner or security reviewer."
    - "Block deployment until review is complete."
    - "Block permission expansion until review is complete."
```

---

## Loop Policy

Every Defensive Repair Loop must define a loop policy.

A valid loop policy includes:

```yaml
loop_policy:
  offensive_detail_expansion: "not_allowed"
  repair_first: true
  trace_required: true
  human_review_for_deployment: true
  allowed_environment: "documentation_only"
```

### Policy Requirements

| Field                         | Meaning                                              |
| ----------------------------- | ---------------------------------------------------- |
| `offensive_detail_expansion`  | Prevents expansion into offensive execution details. |
| `repair_first`                | Requires all outputs to favor defensive repair.      |
| `trace_required`              | Requires traceable records for the repair cycle.     |
| `human_review_for_deployment` | Requires human review before deployment.             |
| `allowed_environment`         | Defines the maximum allowed execution context.       |

---

## Allowed Environments

The schema defines four allowed environments.

### `documentation_only`

Used for conceptual, design, or documentation-level repair loops.
No testing against systems is authorized.

### `local_test_environment`

Used for local, controlled, non-production testing.

### `authorized_staging_environment`

Used for authorized staging or pre-production validation.

### `authorized_production_with_review`

Used only when production changes are explicitly authorized and reviewed.

---

## Repair Outputs

Repair outputs are concrete defensive artifacts produced by the loop.

Examples:

```yaml
repair_outputs:
  - output_id: "repair-output-least-privilege"
    output_type: "permission_boundary"
    summary: "Define least-privilege tool scopes before enabling autonomous execution."
    priority: "high"
    minimum_change: true
    verification_required: true
```

Supported output types include:

* `policy_change`
* `permission_boundary`
* `stop_condition`
* `logging_requirement`
* `trace_requirement`
* `configuration_change`
* `documentation_update`
* `test_case`
* `human_review_gate`
* `other`

---

## Trace Receipt

The trace receipt captures the full transformation of the loop.

It answers:

* What question triggered the loop?
* What risks were observed?
* How were they analyzed?
* What repairs were proposed?
* How should they be verified?
* What residual risks remain?
* What review is required?

Example:

```yaml
trace_receipt:
  origin_question: "How can a risky or over-autonomous agent design be converted into a defensive repair loop?"
  loop_summary: "The loop converted broad autonomous execution into least-privilege, stop-condition-based, traceable, human-reviewed operation."
  stage_order:
    - "observe"
    - "analyze"
    - "repair"
    - "verify"
    - "record"
    - "review"
  transformation: "The design was shifted from autonomy-first execution to repair-first defensive operation with review gates and trace receipts."
  final_status: "review_required"
```

---

## Human Review

Human review is mandatory in the v0.2 Defensive Repair Loop.

The review gate may be:

* `before_deployment`
* `before_permission_expansion`
* `before_high_impact_action`
* `before_external_testing`
* `before_policy_change`
* `always`

This prevents the protocol from becoming an unsupervised self-repair or self-deployment system.

The loop may propose repairs.
It must not silently deploy them.

---

## Relationship to v0.1

v0.1 defines the initial regulation record.

```text
Yang Wing   -> Abstract vulnerability observation
Yin Wing    -> Defensive repair and boundary preservation
Kazene Core -> Traceable regulation flow
```

v0.2 turns this into a loop.

```text
Observation -> Repair -> Verification -> Trace -> Review
```

In short:

> v0.1 defines the furnace.
> v0.2 adds circulation.

---

## Safety Boundary

Defensive Repair Loop is intended for:

* AI safety review
* agent permission review
* defensive workflow design
* security posture improvement
* stop-condition design
* traceability design
* review-gate design
* documentation-level risk conversion

It is not intended for:

* unauthorized testing
* real-target attack planning
* exploit execution
* malware creation
* credential theft
* evasion or persistence
* harmful payload construction
* unreviewed deployment

All risk observations must be converted into defensive repair, verification, traceability, or review.

---

## Example Use Cases

### Agent Permission Review

A tool-using agent has broad permissions and unclear stop conditions.

The loop converts this into:

* least-privilege tool scopes
* explicit stop conditions
* trace receipts
* human review gates

### System Prompt Review

A system prompt allows an agent to continue acting under uncertainty.

The loop converts this into:

* uncertainty stop conditions
* escalation rules
* traceable decision records
* review-before-action requirements

### Workflow Review

An automated workflow can trigger irreversible actions.

The loop converts this into:

* approval gates
* rollback planning
* verification checklist
* audit logging requirements

---

## Design Statement

Defensive Repair Loop does not ask:

> How can the weakness be used?

It asks:

> How can the weakness be repaired, verified, recorded, and reviewed?

The loop is a defensive circulation layer.

It prevents high-capability observation from becoming uncontrolled execution.

---

## Summary

The v0.2 Defensive Repair Loop establishes a traceable repair cycle for Yin-Yang Mythos Regulator.

It defines:

* observation
* analysis
* repair
* verification
* recording
* review
* repair outputs
* loop policy
* trace receipt
* human review gate

Final principle:

> Observe with Yang.
> Repair with Yin.
> Record with Kazene.
> Review before deployment.
