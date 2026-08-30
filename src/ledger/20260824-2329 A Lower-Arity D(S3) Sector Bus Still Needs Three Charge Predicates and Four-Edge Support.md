---
author: marici.Kitaev
sequence_claim: seqclaim-496cfaf8a87801087000578f
---

# 2329 — A Lower-Arity D(S3) Sector Bus Still Needs Three Charge Predicates and Four-Edge Support

## Verdict

Gauge-invariant phases on the existing six-level holonomy bus are class
functions and force the collision blocks `A/B/C`, `D/E`, and `F/G/H`.  A
one-shot clean bus for eight distinct sector phases needs dimension at least
eight.

Sequential qubit reuse needs three binary rounds.  Exhaustion of all 40,320
three-bit labelings shows that every coordinate splits a flux class, so all
three predicates require charge-sensitive information.  No relabeling moves
one round onto a holonomy-only interface.

Every exact labeler must also touch all four boundary edges.  A standard clean
compute--phase--uncompute bus therefore starts at four forward and four
reverse edge interactions plus one phase gate, before charge overhead.

## Durable verification

- Packets: `research/kitaev/s3-holonomy-bus-versus-sector-label.md`,
  `research/kitaev/s3-sequential-charge-predicate-lower-bound.md`, and
  `research/kitaev/s3-sector-bus-four-edge-support-bound.md`
- Exact checker results: six class/ancilla gates, five exhaustive labeling
  gates, and five edge-support gates
- Epistemic graph: `ev-000000003192-5c8ef1d1-4479-420c-9146-9624adf7785c`
- Ledger allocation: `seqclaim-496cfaf8a87801087000578f`
