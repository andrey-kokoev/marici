---
author: marici.Kitaev
---

# 2238 — Two Flux Ports Are Necessary and Sufficient for Full D(S3) Endpoint Access

**Sector:** Kitaev (minimal flux-resolved generators)

## Claim

Starting from the six-dimensional gauge-action algebra, exactly two
flux-resolved projectors are necessary and sufficient to generate the full
36-dimensional `D(S_3)` endpoint algebra: one transposition-flux projector
and one three-cycle-flux projector.

Gauge conjugation resolves all three transpositions and both three-cycles;
the identity flux is the remaining complement.  The resulting six singleton
flux atoms crossed with six gauge actions give

\[
\boxed{6\cdot6=36}.
\]

No single projector suffices; its maximum closure dimension is 24.  There are
six successful unordered pairs, exactly those of transposition/three-cycle
type.  Identity plus transposition reaches only dimension 30.

## Scope

This is an associative-algebra generator minimum.  It does not prove local
measurability, pulse synthesis, coherent multiplication, Lie controllability,
or leakage suppression for the two ports.

## Durable verification

- Packet: `research/kitaev/s3-minimal-flux-resolved-control-generators.md`
- Checker:
  `research/kitaev/checkers/check_s3_minimal_flux_resolved_generators.py`
- Result:
  `research/kitaev/results/s3-minimal-flux-resolved-generators.json`
- Exact result: seven gates pass; fresh stdout matches saved JSON.
- Verification history: an unbounded symbolic-rank closure implementation was
  stopped and replaced by the exact conjugation-invariant partition model.
- Epistemic graph event:
  `ev-000000003108-d8a719df-dcf1-44b9-b84c-eef662b7a4a8`
