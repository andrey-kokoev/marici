# The Half-Density Conjugates the Scale Differential to the Critical-Centered Operator

## Canonical mate

In logarithmic scale `q`, let the additive-to-multiplicative Haar
half-density be

\[
(Wf)(q)=e^{q/2}f(q).
\]

Direct differentiation gives the operator identity

\[
W\partial_qW^{-1}=\partial_q-\frac12.
\]

Therefore

\[
W(\partial_q+s)W^{-1}
=\partial_q+s-\frac12.
\]

Writing `z=s-1/2`, the source tail equation is transported to a differential
system whose spectral coefficient is exactly `z`. The critical offset is not
inserted into the Green identity; it is produced by conjugating the scale
derivative through the relative Haar half-density.

## Seam-period covariance

For logarithmic translation

\[
(T_af)(q)=f(q-a),
\qquad p=e^a,
\]

the half-density satisfies

\[
WT_a=e^{a/2}T_aW.
\]

Hence the lifted period obeys

\[
\lVert WT_af\rVert_{L^2(dq)}^2
=p\lVert Wf\rVert_{L^2(dq)}^2.
\]

This is precisely the relative-Haar modular cocycle. Thus the same
half-density operation simultaneously:

- transports the seam-period metric with factor `p`;
- centers the differential operator at `s=1/2`;
- intertwines raw scale translation between the two Haar sectors.

These were not three coincidences. They are three faces of one conjugation
identity.

## Multi-tower consequence

This constructs the missing mate between the endpoint-homotopy towers and the
relative-Haar comparison tower. The final `1` tower now has an explicit
operator-level coherence cell rather than only a scalar norm ratio.

The remaining RH gate is narrower but still substantial. One must show that:

1. the complete pair-label tail–seam current lies in the domain of `W` and its
   conjugated differential;
2. primitive, square, and archimedean boundary channels transform with the
   same mate;
3. the completed endpoint flux vanishes for a scalar-zero state;
4. the lifted relationship period is finite and nonzero.

Only then does the centered Green coefficient force the real part of `z` to
vanish. The present theorem derives the coefficient and its metric from one
source operation; it does not establish the endpoint statement.

