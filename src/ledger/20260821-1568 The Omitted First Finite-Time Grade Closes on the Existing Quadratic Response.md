# 1568 — The Omitted First Finite-Time Grade Closes on the Existing Quadratic Response

## Question

Does the source-derived cubic \(\eta_0^1\) grade require a new boundary
coefficient direction, or does it lie in the rank-three quadratic response
space frozen in Entry 1528?

## Frozen acceptance test

After Entry 1566 cancels the observation-endpoint primitive column, the
surviving frequency support is \(\{\pm2p\}\). Write the positive-frequency
coefficient as

\[
A(\eta)e^{-2ip\eta},
\qquad
A(\eta)=a_0+a_1\eta+a_2\eta^2.
\]

The polynomial was reconstructed from three independent observation times and
verified at a fourth. The resulting real trigonometric coefficient vector was
then tested against all five exact annihilators of Entry 1528. No response
coefficient was fitted to enforce closure.

## Result

The fourth-point interpolation defect is

\[
8.44\times10^{-15}.
\]

All five boundary-response obstructions vanish. The largest numerical
residual is

\[
3.16\times10^{-13}.
\]

At the frozen generic sample, the response coordinates are

\[
(\operatorname{Re}A_p,\operatorname{Im}A_p,B_p)
=
(4.553605033810049,0,0)
\]

in the Entry 1528 normalization.

Therefore

\[
\boxed{
\mathcal C^{(1)}_{\rm cubic}
\in
\operatorname{span}
\{r_{\operatorname{Re}A},r_{\operatorname{Im}A},r_B\}.
}
\]

## Consequence

The first omitted finite-time grade requires neither a new Carrier stratum nor
a new quadratic boundary coefficient operator. It renormalizes the existing
\(\operatorname{Re}A_p\) direction.

This is the first positive closure result for a grade omitted from the source's
explicit matching calculation. It is restricted to the frozen cubic-loop
sector and does not yet include a complete bulk-counterterm matching packet.
The next independent falsifier is the \(\eta_0^0\) grade, where the
nonoscillatory component can also test the \(B_p\) direction.

## Artifacts

- `research/benincasa/checkers/finite_time_grade1_boundary_closure.rs`
- `research/benincasa/results/finite-time-grade1-boundary-closure.json`

Ledger sequence claim: `seqclaim-f7c35602df86d9c3e79c7c0d`.
