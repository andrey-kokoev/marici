# RH G1.1 relative-extension reconciliation

## Closed linear data

Later source packets close more than the earlier wall/history audits record:

1. theta completion kills the wall in the ordinary bulk image;
2. the maximal relative domain retains both half-density wall solutions;
3. the Wronskian--Lagrange concomitant is the canonical connecting morphism;
4. its even wall and odd reciprocal-jump coordinates have exact normalization;
5. reflection gives the required parity decomposition;
6. the source-level wall-to-completed-history incidence is therefore closed in the relative completion complex.

The earliest residual is not existence of a relative carrier or connecting map.

## Missing quadratic theorem

The first unresolved implication is transport of the complete Green form by block congruence and Schur elimination. Schematically, if \(J_{\mathrm{rel}}\) is the source incidence and \(G_{\mathrm{rel}}\) the relative Green block, one needs an identity of quadratic forms of the type

\[
J_{\mathrm{rel}}^*G_{\mathrm{rel}}J_{\mathrm{rel}}
=
G_{\mathrm{Adams}}
\]

on the declared common form domain, with all wall, jump, history, and fourth Gaussian-grade entries retained. Its relevant Schur return must then equal

\[
D_\pm
=
\frac12(I\pm iH)^*(I\pm iH).
\]

Equality of the four-front vector, endpoint traces, or the two normalized incidence columns does not imply this quadratic identity. Cross terms and action on unobserved directions remain unconstrained.

## Exact finite hostile

`research/nima/checkers/check_rh_adams_quadratic_functoriality.py` constructs two exact rational incidence matrices that agree on the audited boundary vector but induce different pulled-back Green forms. Comparing all four matrix units detects the discrepancy.

The checker proves only the logical necessity of the quadratic test. It does not construct the source congruence.

## Revised G1.1 frontier

The remaining order is:

1. freeze the full relative Green block and common form domain;
2. write the source incidence matrix/operator including every retained grade;
3. verify block congruence on a generating polarized core;
4. prove closure and radical compatibility;
5. compute the Schur return and identify it with the shifted-history square;
6. invoke the existing theta-mass estimate for the uniform lower bound;
7. identify the finite odd compression with \(\tau\) and its Euler/Wronskian orientation.

G1.1 remains open. No RH conclusion is promoted.

## Evidence

- `research/nima/the-completion-differential-annihilates-the-wall-so-the-common-carrier-must-be-relative.md`
- `research/nima/the-killed-wall-survives-as-the-wronskian-boundary-class-of-completion.md`
- `research/nima/the-wronskian-lagrange-boundary-map-is-the-relative-connecting-morphism-for-the-killed-wall.md`
- `research/nima/all-local-linear-adams-data-are-fixed-the-remaining-gate-is-quadratic-functoriality.md`
- `research/nima/the-graph-energy-reciprocal-blocks-are-exact-shifted-history-squares.md`
