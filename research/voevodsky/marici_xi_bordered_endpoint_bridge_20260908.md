# Source-bordered Xi family and the strict marked endpoints

Date: 2026-09-08

## Result

The source-derived bordered family

\[
\mathcal M_s=
\begin{pmatrix}
s&0&1\\
0&s-1&1\\
1&-1&H(s)
\end{pmatrix}
\]

admits a non-tautological typing by the strict marked endpoint data. Regard it as the differential of a two-term rank-three analytic complex. Its determinant is

\[
\det\mathcal M_s=s(s-1)H(s)+1=2\xi(s).
\]

Identify its endpoint basis by

\[
e_0\longmapsto u_{35},
\qquad e_1\longmapsto u_{04}.
\]

The strict conormal quotients give

\[
\pi_{35}(u_{35})=1,
\qquad\pi_{04}(u_{04})=1,
\]

so the outgoing bulk-to-endpoint incidence is the symmetric column

\[
u=(1,1)^T.
\]

Independently, dual normalization descent produced the conductor-to-sheet row

\[
\alpha=(1,-1).
\]

This is exactly the oriented return row of `M_s`. In particular

\[
\alpha u=0.
\]

Thus the endpoint incidence in the Xi matrix is not being fitted from its determinant: both its symmetric outgoing line and antisymmetric return line are supplied by the strict conormal quotient and the independently computed normalization-dual conductor comparison.

## Reflection

If `P` exchanges the two endpoint basis vectors, then

\[
\mathcal M_{1-s}
=\operatorname{diag}(-P,-1)\,
 \mathcal M_s\,
 \operatorname{diag}(P,-1).
\]

This matches the established rule that reflection exchanges the marked `D35` and `D04` targets through different left and right comparison maps, rather than by conjugation inside one fixed target.

## Consequence

This repairs the failed map from the Xi Koszul complex to a parameter-independent closed conductor line. The Marici target now receives a genuinely parameter-dependent, source-bordered endpoint complex whose determinant is `2xi` and whose endpoint rows are independently typed.

At a nontrivial zero `rho`, the explicit kernel vector of the bordered family therefore defines a state in this typed parameterized endpoint complex. This establishes the zero-to-typed-endpoint realization step.

## Remaining gate

The scalar bulk entry `H(s)` has not yet been promoted to a chain map between the complete additive theta and multiplicative valuation observer complexes. Nor has joint conservativity on the off-critical locus been proved. The remaining RH-bearing statement is:

> every off-critical kernel state of the typed bordered family is detected by the completed additive-multiplicative comparison system.

## Verification

```sh
python research/voevodsky/check_marici_xi_bordered_endpoint_bridge_20260908.py \
  --root . \
  --output research/voevodsky/marici_xi_bordered_endpoint_bridge_certificate_20260908.json
```

The checker verifies the determinant, both endpoint rows, their annihilation pairing, reflection covariance, and all eight framed endpoint normalizations in 28 assertions.
