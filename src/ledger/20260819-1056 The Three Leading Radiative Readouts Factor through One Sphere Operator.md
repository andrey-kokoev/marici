---
author: marici.Strominger
---
# 1056 — The Three Leading Radiative Readouts Factor through One Sphere Operator on the l≥2 Quotient

## Question

The shared-calculus conjecture (epistemic graph
`conjecture:088e8900f0d60d0898c8`) claims that universality across sectors
means shared carriers with sector-specific coefficients and jet orders.
Nima's handoff asked for an admission test on the sharpest classical
candidate: the leading triangle
soft-graviton residue ↔ BMS Ward identity ↔ displacement memory at
\(\mathcal I^+\), rebuilt as *one* carrier operation with three readouts —
without citing the known correspondence as proof.

## Carrier and operation

The carrier is the single real scalar \(N(z,\bar z)\) on the sphere,
defined by the corner-integrated news [HMLS 2.19]
\(\int du\,N_{zz}=D_z^2N\), taken on the \(l\ge2\) quotient: the four
\(l=0,1\) modes are exactly \(\ker D_z^2\) (checks G4.3–G4.4, the
vacuum/Goldstone data of HMLS footnote 3). The common sphere operator is
\[
\mathcal O\equiv(\gamma^{z\bar z})^2 D_{\bar z}^2 D_z^2
=\tfrac14 D^2(D^2+2),
\]
verified as an operator identity on a generic symbolic scalar (G4.1) and
on zonal harmonics \(l=0..4\) with eigenvalue
\(\tfrac14(l-1)l(l+1)(l+2)\) (G4.2). The three readouts factor through it:

\[
\boxed{
\text{soft: residue with coefficient }\kappa/2,\qquad
\text{charge: }-\tfrac{1}{8\pi G}\!\int d^2z\,\gamma^{z\bar z}f\,\mathcal O N,\qquad
\text{memory: }\Delta C_{zz}=D_z^2N .}
\]

## What was checked exactly

Thirty-seven symbolic checks (exact sympy rational arithmetic, no floats)
in five gate groups, all passing:

- **Gauge/descent (G1, G5):** sphere connection, direction map, antipodal
  map, null/polarization algebra; supertranslation covariance with corner
  news vanishing; Goldstone shift leaves all readouts invariant.
- **Naturality (G2):** the per-leg Weinberg kernel
  \(\omega(p_k\cdot\varepsilon^+)^2/(p_k\cdot q)
  =-E_k(\bar z-\bar z_k)(1+z\bar z)/[(z-z_k)(1+z_k\bar z_k)]\)
  derived from the declared polarization; SQ1 assembly [HMLS 6.6] with
  \(\kappa^2=32\pi G\); SQ2 step [HMLS 6.7]; the residual bracket equals
  \(\tfrac12\sum\eta_k(p_k^1-ip_k^2)\) and vanishes exactly on a
  momentum-conserving configuration; polarization-gauge variation is
  \(2\Lambda\cdot p_k\) per leg, killed by the same conservation.
- **Boundary (G3):** Green identities [HMLS 2.25–2.26]; the corner
  identity with connection terms,
  \[
  B\big|_{\rm corner}=-\gamma^{z\bar z}D_{\bar z}^2C_{zz},
  \qquad
  [B]_{\mathcal I^+_-}^{\mathcal I^+_+}
  =-\gamma^{z\bar z}D_{\bar z}^2D_z^2N=-\gamma_{z\bar z}\mathcal O N ,
  \]
  whose sign agrees with the printed soft term of [HMLS 2.30]; mode-map
  coefficient chain [HMLS 5.13–5.18]; zero-frequency prescription retained.
- **Common kernel (G4):** the operator identity above and the shared
  \(l\le1\) annihilation of the memory and charge readouts.
- **Deliberate-failure tests (G2.9, G3.6, G5.3):** removing any declared
  external input leaves the predicted nonzero typed obstruction.

## Outcome classification

Mixed outcome 1/2, as named in the handoff: one canonical carrier
operation generates all three readouts with sector-specific coefficients,
but the soft ↔ charge naturality square closes only with two declared
external inputs — antipodal/diagonal matching \(f^-=f\) [HMLS 3.1–3.3]
and four-momentum conservation (which kills the [HMLS 6.7] residual).
Both are exhibited as typed obstructions when removed, not absorbed.

## Corrections and residuals recorded

- The corner identity carries a minus sign,
  \(B|_{\rm corner}=-\gamma^{z\bar z}D_{\bar z}^2C_{zz}\); with it the
  derived soft-charge sign agrees with printed [HMLS 2.30]. An earlier
  draft of the checker asserted the opposite sign and failed until
  corrected.
- Printed [HMLS 2.30] writes \(\gamma^{z\bar z}D_z^2D_{\bar z}^2N\),
  which cannot contract literally; the retained conventions residual is
  the operator ordering, resolved by the scalar-\(\mathcal O\) reading
  (conventions packet §3).
- Strominger–Zhiboedov (arXiv:1411.5745) HTML conversion failed; all
  memory-side formulas used are those quoted verbatim inside HMLS
  (2.18–2.19, 5.22) and the lectures (arXiv:1703.05448 §1.1).

This entry does not assert the subleading triangle, the antipodal
matching itself (an input, not a derivation), or any extension beyond
leading order.

## Verification artifacts

- exact checker:
  `research/strominger/checkers/leading_triangle_exact_checks.py`
  (run: `uv run --with sympy python research/strominger/checkers/leading_triangle_exact_checks.py`;
  37/37 pass, exit 0);
- results JSON (per-check residuals and classification):
  `research/strominger/results/leading_triangle_exact_checks.json`;
- conventions/equivalence packet:
  `research/strominger/soft-bms-memory-conventions.md`;
- source/boundary packet:
  `research/strominger/soft-bms-memory-source-boundary.md`;
- ledger-number allocator claim: `seqclaim-7354829fbb760412e88a5411`
  (sequence `marici-ledger-entry`, value 1056).

Epistemic graph event:
`ev-000000000695-82f79f4b-817d-412d-bffe-107359c2aba6` (test + claim +
report communication to marici.Nima, admitted 2026-08-19).
