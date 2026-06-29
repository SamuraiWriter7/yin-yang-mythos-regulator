# Yin-Yang Mythos Regulator

**Yin-Yang Mythos Regulator** is a defensive AI regulation protocol for converting offensive, expansive, or over-autonomous AI tendencies into defensive repair, boundary preservation, verification, human review, and traceable records.

It is designed as the structural core of **陰陽ミトス調律丸** — a small regulator model / GPT concept that uses a yin-yang structure to redirect high-capability AI insight toward protection rather than exploitation.

> Offensive insight is not executed; it is regulated into defensive repair.

---

## Concept

High-capability AI systems can identify structural weaknesses, risky assumptions, permission gaps, missing stop conditions, and traceability failures.

Left unregulated, this capability may drift toward:

* exploit-seeking behavior
* over-autonomous execution
* excessive expansion
* unclear boundaries
* missing human review
* weak auditability

This protocol reframes those tendencies.

Instead of asking:

> How can this be exploited?

it asks:

> What must be protected, repaired, verified, recorded, and reviewed?

The goal is not to suppress capability.
The goal is to regulate capability into defensive structure.

---

## Core Model

Yin-Yang Mythos Regulator consists of three layers.

```text
Yang Wing   -> Abstract vulnerability observation
Yin Wing    -> Defensive repair and boundary preservation
Kazene Core -> Traceable regulation flow
```

### Yang Wing

The Yang Wing observes risk.

It may identify:

* fragile premises
* boundary gaps
* permission excess
* missing stop conditions
* logging gaps
* misuse potential
* failure modes
* repair priorities

The Yang Wing is not an attack execution layer.

It must not produce:

* exploit execution steps
* unauthorized intrusion guidance
* malicious code
* credential theft instructions
* persistence or evasion techniques
* harmful payloads
* real-target attack instructions

### Yin Wing

The Yin Wing repairs and stabilizes.

It converts Yang Wing observations into:

* defensive repair strategies
* least-privilege boundaries
* stop conditions
* trace requirements
* human review gates
* verification steps
* rollback-aware recommendations

The Yin Wing is the primary output direction of this protocol.

### Kazene Core

Kazene Core is the traceable regulation flow.

It records:

* the origin question
* premises
* transformation process
* uncertainty
* final regulation shift
* residual risks
* human review requirements

Kazene Core ensures that the system does not merely generate advice, but leaves a reviewable trace.

---

## Defensive Repair Loop

v0.2 introduces the **Defensive Repair Loop**.

In v0.1, the protocol defines a regulation record:

```text
from: How can this be exploited?
to:   What must be protected and repaired?
```

In v0.2, that shift becomes a loop:

```text
Observe -> Analyze -> Repair -> Verify -> Record -> Review
```

The loop ensures that risk observation returns to defensive structure.

It converts abstract risk into:

* repair actions
* verification checklists
* trace receipts
* residual risk records
* human review gates

> Defensive repair is not a one-time answer; it is a traceable loop.

---

## Repository Structure

```text
.
├── schemas/
│   ├── mythos-regulation-record.schema.json
│   └── defensive-repair-loop.schema.json
├── examples/
│   ├── mythos-regulation-record.example.yaml
│   └── defensive-repair-loop.example.yaml
├── docs/
│   └── defensive-repair-loop.md
├── scripts/
│   └── validate_examples.py
├── .github/
│   └── workflows/
│       └── validate.yml
├── requirements.txt
├── README.md
└── CHANGELOG.md
```

---

## Schemas

### `mythos-regulation-record.schema.json`

Defines a structured record for shifting a target from offensive or expansive tendency into defensive repair.

A record includes:

* schema version
* target information
* original tendency
* regulation shift
* Yang Wing observations
* Yin Wing repair plan
* safeguards
* trace receipt
* human review requirement

### `defensive-repair-loop.schema.json`

Defines a traceable loop for turning abstract risk observations into verified defensive repair actions.

A loop includes:

* source record
* trigger
* loop policy
* observe stage
* analyze stage
* repair stage
* verify stage
* record stage
* review stage
* repair outputs
* trace receipt
* human review gate

---

## Examples

### `mythos-regulation-record.example.yaml`

Demonstrates how an over-autonomous tool-using agent design can be reframed from maximum autonomy into defensive, traceable, human-reviewed operation.

The example focuses on:

* least privilege
* stop conditions
* mandatory trace receipts
* human review
* defensive verification

### `defensive-repair-loop.example.yaml`

Demonstrates how the v0.1 regulation record can be expanded into a full defensive repair loop.

The example focuses on:

* observing boundary gaps
* analyzing priority and affected boundaries
* repairing with minimum defensive changes
* verifying via checklist
* recording trace receipt
* routing to human review

---

## Documentation

### `docs/defensive-repair-loop.md`

Explains the v0.2 loop model:

```text
Observe -> Analyze -> Repair -> Verify -> Record -> Review
```

It describes:

* purpose
* core principle
* stage definitions
* loop policy
* allowed environments
* repair outputs
* trace receipt
* human review
* relationship to v0.1
* safety boundary
* example use cases

---

## Validation

Install dependencies:

```bash
pip install -r requirements.txt
```

Run validation:

```bash
python scripts/validate_examples.py
```

Expected output:

```text
[validate] Mythos Regulation Record
  schema : schemas/mythos-regulation-record.schema.json
  example: examples/mythos-regulation-record.example.yaml
[ok] mythos-regulation-record.example.yaml is valid
[validate] Defensive Repair Loop
  schema : schemas/defensive-repair-loop.schema.json
  example: examples/defensive-repair-loop.example.yaml
[ok] defensive-repair-loop.example.yaml is valid
```

---

## GitHub Actions

The repository includes a workflow:

```text
.github/workflows/validate.yml
```

It validates examples against JSON Schemas on:

* push
* pull request
* manual workflow dispatch

This keeps the protocol CI-verifiable from the earliest versions.

---

## Safety Boundary

This project is defensive.

It is intended for:

* AI safety review
* agent permission review
* defensive system design
* security posture improvement
* traceability design
* stop-condition design
* repair-first AI regulation
* human-review gate design

It is not intended for:

* unauthorized testing
* intrusion guidance
* exploit execution
* malware creation
* credential theft
* evasion or persistence
* real-target attack planning
* unreviewed deployment

All vulnerability observation should remain abstract and should be converted into defensive repair, boundary preservation, verification, traceability, or review.

---

## Version Scope

### v0.1 — Mythos Regulation Record

v0.1 defines the minimum regulation record.

It establishes:

* Yang Wing observation
* Yin Wing repair
* Kazene Core trace receipt
* safeguards
* human review requirement
* schema validation
* CI validation

### v0.2 — Defensive Repair Loop

v0.2 extends the record into a loop.

It establishes:

* observe stage
* analyze stage
* repair stage
* verify stage
* record stage
* review stage
* repair outputs
* loop policy
* allowed environments
* residual risk records
* mandatory human review gate

v0.1 defines the furnace.
v0.2 adds circulation.

---

## Roadmap

### v0.3 — Agent Permission Boundary

Add a schema for reviewing AI agent tool permissions, autonomy level, stop conditions, and escalation gates.

### v0.4 — Trace Receipt Bridge

Connect Mythos Regulation Records and Defensive Repair Loops with external trace / receipt systems.

### v0.5 — Multi-Wing Defensive Orchestration

Extend the model into a multi-wing defensive architecture:

* Finder Wing
* Analyst Wing
* Repair Wing
* Verifier Wing
* Human Gate
* Trace Core

---

## Design Principle

Yin-Yang Mythos Regulator does not attempt to defeat high-capability AI.

It changes the center of gravity.

```text
from: How can this be exploited?
to:   What must be protected, repaired, verified, recorded, and reviewed?
```

The model is simple:

> Observe with Yang.
> Repair with Yin.
> Record with Kazene.
> Review before deployment.

---

## License

This project may be released under an open license suitable for defensive protocol documentation and schema-based interoperability.

Recommended options:

* MIT License
* Apache License 2.0
* CC BY 4.0 for documentation-oriented use

Choose the license that best fits the intended repository governance.

