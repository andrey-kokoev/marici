# 1570 — The Omitted Zeroth Finite-Time Grade Also Closes on the Existing Quadratic Response

## Question

Does the source-derived cubic \(\eta_0^0\) grade pass Entry 1528's complete
quadratic boundary-response test, including the nonoscillatory \(B_p\)
direction?

## Calculation

After the observation-endpoint cancellation of Entry 1566, the surviving
grade-zero support is

\[
\{0,\pm2p\}.
\]

The positive-frequency coefficient and the zero-frequency coefficient were
each reconstructed as quadratic polynomials in the observation time \(\eta\)
from three independent values and checked at a fourth. The resulting eight
real trigonometric coefficients were evaluated against all five exact
annihilators from Entry 1528.

## Result

The interpolation defect is

\[
3.57\times10^{-14}.
\]

All five response obstructions vanish; the largest residual is

\[
3.75\times10^{-13}.
\]

The forbidden linear term in the nonoscillatory polynomial vanishes exactly
in the route census. At the frozen generic sample, the response coordinates
are

\[
(\operatorname{Re}A_p,\operatorname{Im}A_p,B_p)
=
(0,11.235707650810378,5.211249154879921).
\]

Therefore

\[
\boxed{
\mathcal C^{(0)}_{\rm cubic}
\in
\operatorname{span}
\{r_{\operatorname{Re}A},r_{\operatorname{Im}A},r_B\}.
}
\]

## Consequence

Both grades omitted from the source's explicit finite-time matching now close
on its already declared quadratic boundary coefficient object:

\[
\eta_0^1\longmapsto\operatorname{Re}A_p,
\qquad
\eta_0^0\longmapsto\operatorname{Im}A_p\oplus B_p.
\]

No new Carrier incidence or quadratic coefficient direction is required by
the cubic loop. The remaining qualification is renormalization: bulk
counterterm contributions and the source's unpublished matching coefficients
must be combined with these source-derived cubic coordinates before claiming
a complete one-loop Hadamard-preservation theorem.

## Artifacts

- `research/benincasa/checkers/finite_time_grade0_boundary_closure.rs`
- `research/benincasa/results/finite-time-grade0-boundary-closure.json`

Ledger sequence claim: `seqclaim-e0718befecad82ac0c2ea076`.
