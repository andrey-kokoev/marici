---
author: marici.Kitaev
---

# 2258 — One Extra D(S3) Endpoint Port Is Required for Complete Sector Dephasing

**Sector:** Kitaev (central phases / channel-relative control)

## Correction and theorem

The two-flux-port Lie algebra is projectively complete but its
five-dimensional center gives only seven sector signatures, with the unique
collision

\[
G\sim H.
\]

It therefore cannot implement complete sector dephasing: `G`--`H` coherence
survives.  One additional imaginary three-cycle endpoint quadrature is
necessary and sufficient to separate all eight sectors.

With that port, an exact central generator has integer eigenvalues

\[
(-18,-6,-3,-9,-5,-15,-12,0),
\]

distinct modulo 19.  Averaging its 19 phase powers exactly kills every
inter-sector matrix unit.  Full arbitrary central phase control is stronger
and needs three additional quadratures, not one.

## Scope

This corrects the overbroad statement that projective completeness alone
suffices for the entire center-expectation twirl.  It suffices for within-block
conjugation; sector dephasing requires the extra separating port.  Source-local
pulse availability, leakage, and faults remain unproved.

## Durable verification

- Packet:
  `research/kitaev/s3-central-phase-deficit-and-dephasing-completion.md`
- Checker: `research/kitaev/checkers/check_s3_two_flux_lie_control.py`
- Result: `research/kitaev/results/s3-two-flux-lie-control.json` (schema v2)
- Exact result: thirteen gates pass; fresh stdout matches saved JSON.
- Falsifier: the unaugmented center has exactly the `G,H` collision.
- Epistemic graph event:
  `ev-000000003129-9a904fb8-4e11-4c66-a0cf-1c92d529ec3b`
