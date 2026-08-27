# The Two Endpoint Homotopies Differ by a Seam Period

## Minimal decision problem

The reciprocal normalization anomaly requires an inverse of the scale
derivative. On the half-line there are two source-natural inverses, selected by
the two endpoint orientations:

\[
(H_0g)(q)=\int_0^q g(v)\,dv,
\qquad
(H_\infty g)(q)=-\int_q^\infty g(v)\,dv.
\]

Both satisfy

\[
\partial_qH_0g=g,
\qquad
\partial_qH_\infty g=g.
\]

But they are not the same homotopy. Their difference is the constant seam
period

\[
(H_0-H_\infty)g
=\int_0^\infty g(v)\,dv.
\]

For the positive anomaly mode `g(q)=exp(-2 lambda q)`, this period is
`1/(2 lambda)`, hence nonzero.

## Exact obstruction

No single primitive can obey both endpoint normalizations

\[
H g(0)=0,
\qquad
H g(\infty)=0
\]

unless the seam period of `g` vanishes. The anomaly density has positive
period, so its forward and backward contractions cannot be identified.

This forces a refinement of the multi-tower architecture. The global homotopy
layer splits into two directed towers:

- the input-oriented homotopy normalized at `q=0`;
- the output-oriented homotopy normalized at `q=infinity`.

Their difference is not an error. It is a new comparison datum carried by the
seam-period tower.

The resulting minimal shape is

\[
3+2+2+1.
\]

Here the first `3` are the input, output, and control state towers; the first
`2` are forward and backward construction/defect witnesses; the second `2`
are the endpoint-oriented homotopy towers; and the final `1` compares them by
the seam period.

## RH consequence

The hoped-for zero-confinement identity cannot set this period to zero merely
because the scalar readout vanishes. For the augmentation bivector, scalar
nullity deliberately leaves a nonzero relationship state, and its positive
anomaly density has a nonzero period.

The next source theorem must therefore identify the arithmetic seam current
with this period and show how the completed reciprocal object accounts for it.
If it merely discards the period, it erases precisely the state recovered by
the bivector channel.

