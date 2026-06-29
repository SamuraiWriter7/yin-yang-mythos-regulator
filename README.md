# Yin-Yang Mythos Regulator

**Yin-Yang Mythos Regulator** is a defensive AI regulation protocol for converting offensive, expansive, or over-autonomous AI tendencies into defensive repair, boundary preservation, and traceable review.

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

> What must be protected, repaired, and recorded?

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
* human review requirements

Kazene Core ensures that the system does not merely generate advice, but leaves a reviewable trace.

---

## Repository Structure

```text
.
├── schemas/
│   └── mythos-regulation-record.schema.json
├── examples/
│   └── mythos-regulation-record.example.yaml
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

## Schema

### `mythos-regulation-record.schema.json`

The schema defines a structured record for shifting a target from offensive or expansive tendency into defensive repair.

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

---

## Example

### `mythos-regulation-record.example.yaml`

The example demonstrates how an over-autonomous tool-using agent design can be reframed from maximum autonomy into defensive, traceable, human-reviewed operation.

The example focuses on:

* least privilege
* stop conditions
* mandatory trace receipts
* human review
* defensive verification

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

This keeps the protocol CI-verifiable from v0.1 onward.

---

## Safety Boundary

This project is defensive.

It is intended for:

* AI safety review
* agent permission review
* defensive system design
* security posture improvement
* traceability design
* human-review gate design
* repair-first AI regulation

It is not intended for:

* unauthorized testing
* intrusion guidance
* exploit execution
* malware creation
* credential theft
* evasion or persistence
* real-target attack planning

All vulnerability observation should remain abstract and should be converted into defensive repair, boundary preservation, and traceable review.

---

## v0.1 Scope

Version `0.1.0` defines the minimum regulation record.

It establishes:

* Yang Wing observation
* Yin Wing repair
* Kazene Core trace receipt
* safeguards
* human review requirement
* schema validation
* CI validation

This is the first working furnace: offensive heat is not released outward; it is returned into defensive structure.

---

## Roadmap

### v0.2 — Defensive Repair Loop

Define a structured loop for:

* finding risks
* classifying impact
* generating repair actions
* verifying repairs
* recording review status

### v0.3 — Agent Permission Boundary

Add a schema for reviewing AI agent tool permissions, autonomy level, stop conditions, and escalation gates.

### v0.4 — Trace Receipt Bridge

Connect Mythos Regulation Records with external trace / receipt systems.

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
to:   What must be protected and repaired?
```

The model is simple:

> Observe with Yang.
> Repair with Yin.
> Record with Kazene.

---

## License

This project may be released under an open license suitable for defensive protocol documentation and schema-based interoperability.

Recommended options:

* MIT License
* Apache License 2.0
* CC BY 4.0 for documentation-oriented use

Choose the license that best fits the intended repository governance.
