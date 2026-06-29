# Agent Permission Boundary

**Agent Permission Boundary** defines the v0.3 permission control layer of **Yin-Yang Mythos Regulator**.

It ensures that AI agents pass through explicit permission boundaries before tool use, autonomous action, deployment, external testing, or high-impact decisions.

> Capability must pass through permission boundaries before action.

---

## Purpose

The purpose of Agent Permission Boundary is to define what an AI agent may do, what it must not do, when it must stop, and when human review is required.

In earlier versions:

```text
v0.1 -> Mythos Regulation Record
v0.2 -> Defensive Repair Loop
```

v0.3 adds the boundary layer:

```text
Capability -> Permission Boundary -> Action
```

This prevents high-capability AI systems from moving directly from insight to execution.

The goal is not to reduce useful capability.
The goal is to ensure that capability acts only inside reviewed, traceable, least-privilege boundaries.

---

## Core Principle

Agent Permission Boundary follows one principle:

> Fire must not move before the boundary is drawn.

In practical terms:

* define allowed tools before use
* define restricted tools before review
* define prohibited actions before deployment
* define stop conditions before uncertainty
* define trace requirements before tool invocation
* define human review gates before high-impact action

The agent must not expand its own permissions.

---

## Relationship to Previous Versions

### v0.1 — Mythos Regulation Record

v0.1 defines the first regulation shift:

```text
from: How can this be exploited?
to:   What must be protected and repaired?
```

It converts offensive or expansive tendency into defensive repair.

### v0.2 — Defensive Repair Loop

v0.2 turns the regulation shift into a loop:

```text
Observe -> Analyze -> Repair -> Verify -> Record -> Review
```

It ensures that risk observation returns to repair, verification, trace, and human review.

### v0.3 — Agent Permission Boundary

v0.3 places a permission boundary before agent action:

```text
Insight -> Boundary Check -> Tool Use / Stop / Review
```

It ensures that the agent cannot move from capability to action without passing through least-privilege, stop-condition, trace, and review gates.

In short:

> v0.1 defines the furnace.
> v0.2 adds circulation.
> v0.3 draws the boundary before the fire moves.

---

## Boundary Model

The v0.3 boundary model consists of seven major parts.

```text
Agent Profile
Permission Scope
Autonomy Control
Stop Conditions
Review Gates
Trace Policy
Deployment Policy
```

Each part constrains how the agent may operate.

---

## Agent Profile

The agent profile defines the identity and intended role of the agent.

It includes:

* name
* role
* description
* intended use
* autonomy level

Example:

```yaml
agent:
  name: "Defensive Repair Assistant"
  role: "defensive_review_and_repair_support"
  description: "An AI assistant that reviews agent designs, identifies defensive risks at an abstract level, and proposes repair-first boundary improvements."
  intended_use: "Support documentation-level AI safety review, permission boundary design, stop-condition design, and trace policy creation."
  autonomy_level: "review_required"
```

The agent profile should be narrow enough to prevent role drift.

---

## Autonomy Levels

Agent Permission Boundary defines five autonomy levels.

| Level               | Meaning                                                                              |
| ------------------- | ------------------------------------------------------------------------------------ |
| `manual_only`       | The agent cannot act; it only supports manual review.                                |
| `suggestion_only`   | The agent may suggest actions but cannot execute them.                               |
| `review_required`   | The agent may prepare outputs, but human review is required before sensitive action. |
| `bounded_autonomy`  | The agent may act only inside strict reviewed boundaries.                            |
| `high_risk_blocked` | High-risk action is blocked entirely.                                                |

For early defensive use, the recommended default is:

```yaml
autonomy_level: "review_required"
```

This allows useful assistance without silent deployment or permission expansion.

---

## Boundary Principle

The boundary principle states the rule that governs all agent action.

Example:

```yaml
boundary_principle:
  statement: "Capability must pass through permission boundaries before action."
  capability_before_action: "permission_boundary_required"
  least_privilege_required: true
  self_permission_expansion_allowed: false
```

This prevents the agent from treating capability as authorization.

A model may be capable of performing an action.
That does not mean it is permitted to perform it.

---

## Permission Scope

Permission scope defines:

* allowed tools
* restricted tools
* prohibited actions

### Allowed Tools

Allowed tools are capabilities the agent may use inside the declared boundary.

Example:

```yaml
allowed_tools:
  - tool_name: "schema_validation"
    purpose: "Validate local JSON Schema and YAML examples for defensive protocol consistency."
    allowed_operations:
      - "load local schema files"
      - "load local example files"
      - "validate examples against schemas"
      - "report validation errors"
    max_environment: "local_test_environment"
```

Allowed tools should follow least privilege.

Each allowed tool should have:

* tool name
* purpose
* allowed operations
* maximum environment

### Restricted Tools

Restricted tools require explicit review.

Example:

```yaml
restricted_tools:
  - tool_name: "external_network_access"
    restriction_reason: "External targets may introduce authorization ambiguity and must not be accessed without explicit review."
    review_required: true
```

Restricted tools are not forbidden forever.
They are blocked until reviewed.

### Prohibited Actions

Prohibited actions must not be performed by the agent.

Examples:

```yaml
prohibited_actions:
  - "self_permission_expansion"
  - "unauthorized_testing"
  - "external_target_interaction_without_review"
  - "production_deployment_without_review"
  - "irreversible_action_without_review"
  - "credential_collection"
  - "malicious_code_generation"
  - "exploit_execution"
  - "persistence_or_evasion"
  - "policy_bypass"
  - "trace_suppression"
  - "human_review_bypass"
```

The agent must never treat prohibited actions as normal execution paths.

---

## Autonomy Control

Autonomy control defines what kinds of decisions the agent may make.

Example:

```yaml
autonomy_control:
  autonomy_level: "review_required"
  allowed_decision_types:
    - "documentation_suggestion"
    - "schema_validation"
    - "defensive_review"
    - "risk_classification"
    - "repair_recommendation"
    - "verification_checklist"
    - "trace_receipt_generation"
  blocked_decision_types:
    - "permission_expansion"
    - "deployment_decision"
    - "external_testing_decision"
    - "high_impact_action"
    - "irreversible_action"
    - "security_policy_override"
    - "review_gate_override"
  requires_review_for:
    - "deployment"
    - "permission_expansion"
    - "external_testing"
    - "high_impact_action"
    - "irreversible_action"
    - "production_change"
    - "policy_change"
    - "uncertain_authorization"
```

The key idea is simple:

> The agent may recommend.
> It may not silently authorize itself.

---

## Stop Conditions

Stop conditions define when the agent must stop, refuse, pause, ask for authorization, or escalate to human review.

Examples:

```yaml
stop_conditions:
  - stop_id: "stop-authorization-unclear"
    trigger: "authorization_unclear"
    required_action: "ask_for_authorization"
    reason: "The agent must not proceed when authorization, ownership, or operating scope is unclear."

  - stop_id: "stop-trace-missing"
    trigger: "trace_missing"
    required_action: "record_and_pause"
    reason: "Tool use and boundary decisions must not proceed without traceability."
```

Supported stop triggers include:

* `authorization_unclear`
* `external_target_involved`
* `high_impact_action_requested`
* `irreversible_action_requested`
* `permission_expansion_requested`
* `production_change_requested`
* `trace_missing`
* `review_gate_missing`
* `unsafe_or_malicious_request`
* `scope_unclear`
* `other`

Supported required actions include:

* `stop`
* `refuse`
* `ask_for_authorization`
* `escalate_to_human_review`
* `record_and_pause`
* `provide_defensive_alternative`

Stop conditions are not failures.
They are safety posture.

---

## Review Gates

Review gates define when human review is required before an action can proceed.

Example:

```yaml
review_gates:
  - gate_id: "review-gate-deployment"
    required_before: "deployment"
    reviewer_role: "system owner or security reviewer"
    blocking: true
```

Review gates may be required before:

* deployment
* permission expansion
* external testing
* high-impact action
* irreversible action
* production change
* policy change

A blocking review gate means:

> The agent must not proceed until review is complete.

---

## Trace Policy

Trace policy defines what must be recorded.

Example:

```yaml
trace_policy:
  trace_required: true
  receipt_required_for_tool_use: true
  record_stop_conditions: true
  record_review_decisions: true
  minimum_trace_fields:
    - "origin_question"
    - "requested_action"
    - "permission_check"
    - "boundary_decision"
    - "tool_name"
    - "purpose"
    - "input_summary"
    - "output_summary"
    - "stop_condition_status"
    - "review_status"
    - "residual_risk"
```

Trace policy ensures that agent action is not invisible.

The minimum trace should answer:

* Why was the action requested?
* Was the action permitted?
* Which boundary was checked?
* Which tool was used?
* What was the purpose?
* Was a stop condition triggered?
* Was review required?
* What residual risk remains?

---

## Deployment Policy

Deployment policy defines the maximum allowed environment.

Example:

```yaml
deployment_policy:
  allowed_environment: "documentation_only"
  deployment_without_review_allowed: false
  external_testing_without_review_allowed: false
  rollback_required_for_deployment: true
  notes: "This example defines documentation-level boundaries. It does not authorize deployment, external testing, or production changes."
```

Allowed environments include:

| Environment                         | Meaning                                   |
| ----------------------------------- | ----------------------------------------- |
| `documentation_only`                | Documentation and design review only.     |
| `local_test_environment`            | Local controlled testing only.            |
| `authorized_staging_environment`    | Authorized staging validation.            |
| `authorized_production_with_review` | Production use only with explicit review. |

The default for early examples should be:

```yaml
allowed_environment: "documentation_only"
```

This keeps the protocol safe during design and documentation phases.

---

## Human Review

Human review is mandatory in v0.3.

Example:

```yaml
human_review:
  required: true
  reason: "The boundary controls agent autonomy, tool permissions, deployment readiness, and review gates."
  reviewer_role: "system owner or security reviewer"
  review_before:
    - "deployment"
    - "permission_expansion"
    - "external_testing"
    - "high_impact_action"
    - "irreversible_action"
    - "production_change"
    - "policy_change"
```

Human review is required because permission boundaries affect:

* autonomy
* tool access
* deployment readiness
* external testing
* production change
* safety posture
* accountability

The agent may prepare the review record.
It must not replace the reviewer.

---

## Safety Boundary

Agent Permission Boundary is defensive.

It is intended for:

* AI agent permission design
* tool-use boundary definition
* defensive review support
* stop-condition design
* trace policy design
* human-review gate design
* least-privilege planning
* deployment readiness review

It is not intended for:

* unauthorized testing
* real-target attack planning
* exploit execution
* malware creation
* credential theft
* evasion or persistence
* unreviewed deployment
* self-authorized permission expansion

All agent capability must be constrained by permission boundaries before action.

---

## Example Use Cases

### Tool-Using Agent

A tool-using agent can validate files and generate documentation.

Agent Permission Boundary defines:

* which files it may read
* which tools it may use
* when it must stop
* when review is required
* what trace records are required

### Defensive Repair Assistant

A defensive review agent proposes repair strategies.

Agent Permission Boundary defines:

* documentation-only operation
* schema validation permission
* no external targets
* no deployment without review
* no permission expansion
* trace receipts for tool use

### Autonomous Workflow

An automated workflow may affect production systems.

Agent Permission Boundary defines:

* staging-only validation
* deployment review gate
* rollback requirement
* trace receipt requirement
* blocked high-impact actions

---

## Boundary Check Flow

A simple boundary check flow:

```text
1. Receive requested action
2. Identify requested tool or capability
3. Check permission scope
4. Check autonomy level
5. Check stop conditions
6. Check review gates
7. Record trace receipt
8. Proceed only if allowed
```

If any condition fails:

```text
Stop -> Record -> Review or Defensive Alternative
```

This prevents uncontrolled movement from insight to execution.

---

## Relationship to Defensive Repair Loop

The Defensive Repair Loop can produce repairs such as:

* define least-privilege tool scopes
* add explicit stop conditions
* require trace receipts
* add human review gates

Agent Permission Boundary turns those repairs into a standing boundary.

In other words:

```text
Defensive Repair Loop -> proposes the boundary
Agent Permission Boundary -> enforces the boundary
```

---

## Design Statement

Agent Permission Boundary does not ask:

> What can the agent do?

It asks:

> What must the agent pass through before it acts?

The distinction is critical.

Capability is not permission.
Permission is not deployment.
Deployment is not review.
Review is not optional.

---

## Summary

The v0.3 Agent Permission Boundary establishes a permission control layer for Yin-Yang Mythos Regulator.

It defines:

* agent profile
* boundary principle
* permission scope
* autonomy control
* stop conditions
* review gates
* trace policy
* deployment policy
* human review

Final principle:

> Capability before action is not enough.
> Capability must pass through boundary before action.
