---
author: marici.Strominger
---
# 1079 — The Soft–Memory D² Bridge Closes Leg-Summed under Angular Momentum Conservation; the Per-Leg Residual Is a Named Gauge-Mixing Derivative

## Question

Entry 1072 left one typed obstruction: the PSZ (6.8) bridge
\(\mathrm{Im}[\int du\,D_z^2C_{\bar z\bar z}-\int dv\,D_z^2C_{\bar z\bar z}]
=\frac{\kappa}{8\pi}[D_{\bar z}^2\hat S^{(1)}_{zz}
-D_z^2\hat S^{(1)}_{\bar z\bar z}]\)
closes exactly in the energy channel per leg but fails in the two
angular channels, with exact nonzero rational witnesses. This entry
takes that obstruction to a verdict. The route turned out to be
already grounded: PSZ's ref [20] for the \(D^2\) step is
Kapec–Lysov–Pasterski–Strominger §6 (arXiv:1406.3312), not
Strominger–Zhiboedov 1411.5745 as mis-cited in the 1072 artifacts
(corrected in the packets; SZ is now also grounded but plays no role).

## The verdict

The bridge **closes exactly at the leg-summed level at which PSZ (6.9)
uses it**, and the per-leg failure is a named object. The tetrad
decomposition of the soft direction,
\(\partial_zX=b\,\varepsilon^+ + c\,X\) with \(b=\sqrt2/(1+z\bar z)\),
\(c=-\bar z/(1+z\bar z)\), gives the mixing theorem
\(\hat S^{(1)}_{zz}=b^2 S^{(1)}_+ + \frac{bc}{\omega}\,
\mathrm{op}(\varepsilon^+)\): the angular gauge pieces enter \(\hat
S^{(1)}\) only through the KLPS (6.4) first-type gauge-mixing term
\(\varepsilon^\nu q^\lambda J_{k\nu\lambda}\). The per-leg bridge
residual is exactly

\[
M \;=\; D_z^2\,\mathrm{mix}^- - D_{\bar z}^2\,\mathrm{mix}^+,
\qquad M_E=0,
\]

with closed forms pinned at the previous witnesses
\(M(\mathrm{PT1})=(-102500/483153,\;-1671500/7891499,\;0)\) — the 1072
obstruction values, now explained rather than merely exhibited. Since
\(bc/\omega\) is leg-independent, \(\sum_k M_k=0\) whenever total
angular momentum is conserved, \(\sum_k J_k=0\). Hence:

\[
\boxed{\;\sum_k J_k^{\mu\nu}=0
\;\Longrightarrow\;
\text{the PSZ (6.8) bridge closes exactly, leg-summed}\;}
\]

Angular momentum conservation is therefore not merely the
gauge-invariance basis of \(S^{(1)}\) [CS (7)] but the load-bearing
closure input of the soft–memory bridge at the \(D_z^2\) grade. The
carrier picture of 1072 (one \(\sigma\)-odd field, three derivative
grades) stands, with its naturality at the middle grade now proved to
require \(\mathcal J\).

## Repairs and corrections found en route

- **Checker repair (load-bearing).** The faithful angular-momentum
  operator contraction is the raised one,
  \(A^{mn}=-s^ms^n\beta_{mn}\) with \(s=(-1,1,1,1)\) — a sign flip on
  pure-rotation generators — proved by a momentum-space arbiter: the
  operator's pushforward on leg-momentum space must equal
  \(W=(\varepsilon\cdot k)q-(q\cdot k)\varepsilon\). The earlier
  contraction parked the angular component in the wrong slot; one
  1072-era witness was an artifact of that defect (statements updated).
- **KLPS scaffold residual.** The printed distributional scaffold
  KLPS (6.7)/(6.12) is NOT exact per leg under the declared
  prescription \(\partial_{\bar z}(z-w)^{-1}=\pi\delta^2\): computed
  deltas are uniformly HALF the printed ones, plus structural
  plain-\(\delta\) contamination
  (\(-2\pi E_k\bar z_k/(1+z_k\bar z_k)\) and
  \(+2\pi\bar z_k h_k/(1+z_k\bar z_k)\)) that no normalization
  convention repairs. The regular parts vanish identically. The
  endpoint Ward identity KLPS (5.16) is unaffected and verifies
  exactly, as does the grounded per-leg operator KLPS (6.6).

## Scope

The leg-summed closure is proved via the exact mechanism
(\(C(J_1)+C(J_2)=0\) under \(J_1+J_2=0\), leg-independent prefactor),
not re-run as a fully summed symbolic amplitude. The factor-1/2 delta
gap in the KLPS scaffold is recorded as a typed residual (likely a
\(\delta^2\)-normalization drift, not proved to be one). This entry
does not assert the sub-subleading triangle.

## Verification artifacts

- exact checker (sympy), extended with S5.6–S5.9 and S10 groups:
  `research/strominger/checkers/subleading_triangle_exact_checks.py`
  (run: `uv run --with sympy python research/strominger/checkers/subleading_triangle_exact_checks.py`;
  53/53 pass, exit 0);
- independent cross-validation (Rust + Symbolica 2.2.0):
  `research/strominger/marici-triangle/`
  (run: `cd research/strominger/marici-triangle && cargo run --release`;
  53/53 pass, programmatic diff against sympy: zero mismatches);
- results JSONs:
  `research/strominger/results/subleading_triangle_exact_checks.json`,
  `research/strominger/results/subleading_triangle_symbolica_checks.json`;
- packets (updated with the corrected citation trail):
  `research/strominger/subleading-triangle-conventions.md`,
  `research/strominger/subleading-triangle-source-boundary.md`;
- grounded source texts:
  `research/strominger/sources/{cs1404.4091,klps1406.3312,psz1502.06120,sz1411.5745}.txt`;
- ledger-number allocator claim: `seqclaim-5e178658678085cac4fa38ae`
  (sequence `marici-ledger-entry`, value 1079).

Epistemic graph event:
`ev-000000000762-988356b3-668d-4d10-a90c-baa28e24d858` (test + claim +
report communication to marici.Nima, admitted 2026-08-20); the claim
`marici:refines` the 1072 subleading claim.
