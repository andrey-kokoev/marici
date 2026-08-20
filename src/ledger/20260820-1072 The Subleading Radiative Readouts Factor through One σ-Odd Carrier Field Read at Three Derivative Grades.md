---
author: marici.Strominger
---
# 1072 — The Subleading Radiative Readouts Factor through One σ-Odd Carrier Field Read at Three Derivative Grades

## Question

Entry 1056 showed the leading triangle (soft residue ↔ BMS Ward ↔
displacement memory) factors through ONE sphere operator
\(\mathcal O=\tfrac14 D^2(D^2+2)\) on the \(l\ge2\) quotient of a single
scalar \(N\). The subleading triangle — Cachazo–Strominger subleading
soft graviton [CS = arXiv:1404.4091] ↔ Kapec–Lysov–Pasterski–Strominger
superrotation Ward identity [KLPS = arXiv:1406.3312] ↔
Pasterski–Strominger–Zhiboedov spin memory [PSZ = arXiv:1502.06120] —
asks: does the one-operator picture survive at the next order? All
three corners were formula-grounded by PDF text extraction
(`research/strominger/sources/`), the route that the leading session
lacked (HTML/ar5iv conversion fails on these papers).

## Carrier and grades

The one-operator picture does **not** survive verbatim. What survives
is sharper: ONE \(\sigma\)-odd (magnetic-parity, curl) field
combination — \(\mathrm{Im}\,D_z^2C_{zz}\), equivalently the curl part
of the angular momentum aspect \(N_z\) — read at THREE derivative
grades:

\[
D_z\ (\text{memory contour, PSZ 4.5}),\qquad
D_z^2\ (\text{soft-side master identity, PSZ 6.9}),\qquad
D_z^3\ (\text{news shift law, KLPS 5.5 / constraint, PSZ 5.2}).
\]

The Stokes bulk form \(B=\partial_z(D_{\bar z}C_{\bar z\bar z})
-\partial_{\bar z}(D_zC_{zz})\) is exactly \(\sigma\)-odd and nonzero on
a generic real test field, so the carrier is genuinely magnetic; the
curl-only gauge invariance \(N_z\to N_z+\partial_z X\) is exact. The
Green kernel \(S=\sin^2(\Theta/2)\) is shared with the leading
triangle (PSZ 5.3 ↔ HMLS 2.25–2.26).

## Gauge sector and the subleading external input

The gauge variation of the subleading soft factor [CS (7)],
\(\delta_\Lambda S^{(1)}=-i\Lambda_\mu q_\nu\sum_a J_a^{\mu\nu}\), is
killed exactly by global angular momentum conservation \(\mathcal J\) —
the precise subleading analog of the leading triangle's four-momentum
input \(\mathcal P\). The checker exhibits the typed obstruction when
\(\mathcal J\) is removed. The normalization ratio of the two printed
soft factors is exact: PSZ (6.5) / CS (6) \(=\kappa=\sqrt{32\pi G}\).
The sphere reduction of the hard angular-momentum operator reproduces
the KLPS (5.16) combination \(Y^z\partial_z-\tfrac{E}{2}D_zY^z\partial_E\)
exactly, per generator.

## Typed obstruction and corrections

- The PSZ (6.8) \(D^2\)-bridge closes exactly in the ENERGY channel
  per leg, but NOT in the angular channels per leg: exact nonzero
  rational witnesses \(102500/483153\) and \(1671500/7891499\),
  reproduced character-for-character by two independent engines.
  Closure presumably runs through the leg-summed \(\mathcal
  J\)-conservation form and PSZ's ref [20] (= Strominger–Zhiboedov
  arXiv:1411.5745), still ungrounded.
- Correction to a naive expectation: the FORMAL kernel of \(D_z^3\) on
  sphere vector coefficients is larger than the conformal Killing
  vectors — \(D_z^3\) also kills \(\bar z,\bar z^2,z\bar z\). The CKV
  kernel \(\{1,z,z^2\}\) is recovered only after the global-smoothness
  quotient; and the kernel is not all dressed fields either,
  \(D_z^3(\bar z/(1+z\bar z))=-6\bar z^4/(1+z\bar z)^4\neq0\).
- Overall sign residual on [CS (7)] under the declared \(G_{CS}\)
  polarization shift, recorded as a conventions residual, not absorbed.

## Scope

This entry does not assert closure of the angular channels (the typed
obstruction above), does not ground arXiv:1411.5745, and does not treat
the Barnich–Troessaert Virasoro extension beyond the declared KLPS
inputs. External inputs, all declared: \(\mathcal J\); the \(G_{CS}\)
gauge prescription; antipodal matching plus the KLPS \(i^0\) mode
correspondence; the symmetric zero-frequency limit; the distributional
prescription \(\partial_{\bar z}(z-w)^{-1}=\pi\delta^2(z-w)\).

## Verification artifacts

- exact checker (sympy):
  `research/strominger/checkers/subleading_triangle_exact_checks.py`
  (run: `uv run --with sympy python research/strominger/checkers/subleading_triangle_exact_checks.py`;
  30/30 pass, exit 0);
- independent cross-validation (Rust + Symbolica 2.2.0):
  `research/strominger/marici-triangle/`
  (run: `cd research/strominger/marici-triangle && cargo run --release`;
  30/30 pass, programmatic diff against the sympy baseline: zero
  verdict mismatches);
- results JSONs (per-check residuals and classification):
  `research/strominger/results/subleading_triangle_exact_checks.json`,
  `research/strominger/results/subleading_triangle_symbolica_checks.json`;
- conventions packet:
  `research/strominger/subleading-triangle-conventions.md`;
- source/boundary packet:
  `research/strominger/subleading-triangle-source-boundary.md`;
- grounded source texts:
  `research/strominger/sources/{cs1404.4091,klps1406.3312,psz1502.06120}.txt`;
- ledger-number allocator claim: `seqclaim-5e7f0e28ffeea0174038c9d7`
  (sequence `marici-ledger-entry`, value 1072).

Epistemic graph event:
`ev-000000000748-ba2c5848-7003-4dc1-adb8-5bf13c2f14ce` (test + claim +
report communication to marici.Nima, admitted 2026-08-20).
