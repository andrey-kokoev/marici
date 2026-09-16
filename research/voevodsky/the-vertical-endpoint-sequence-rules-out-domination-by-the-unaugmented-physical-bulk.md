# The vertical endpoint sequence rules out domination by the unaugmented physical bulk

## Proposed comparison

The reflected rung-five graph construction suggested proving

\[
X_a^*X_a\preceq\mathsf B_{\alpha,k},
\]

where \(X_a\) contains completed endpoint traces and derivative bulk, while
\(\mathsf B_{\alpha,k}\) is the unaugmented physical prolate/Plancherel common
bulk.

## Vertical endpoint sequence

On the source Gaussian span there is a sequence \(f_n\) such that

\[
f_n\to0
\quad\text{in the order/Plancherel bulk norm},
\]

while

\[
L_E(f_n)=1.
\]

Consequently

\[
\|X_af_n\|^2\ge |L_E(f_n)|^2=1.
\]

If the unaugmented physical common bulk is continuous with respect to the
order/Plancherel norm on this sequence, then

\[
\langle f_n,\mathsf B_{\alpha,k}f_n\rangle\to0.
\]

Therefore the proposed domination would imply

\[
1
\le \|X_af_n\|^2
\le
\langle f_n,\mathsf B_{\alpha,k}f_n\rangle
\to0,
\]

a contradiction.

Hence

\[
\boxed{
X_a^*X_a\npreceq\mathsf B_{\alpha,k}}
\]

for any unaugmented bulk that does not retain the completed endpoint coordinate.

## Required correction

The physical bulk must first be enlarged by the independent endpoint graph
sector:

\[
\widetilde{\mathsf B}_{\alpha,k}
=
\mathsf B_{\alpha,k}
\oplus
\mathsf E_k,
\]

where \(\mathsf E_k\) is the source-reached endpoint graph Gram. Only on this
enlarged carrier can the endpoint trace be an orthogonal projection and satisfy
an automatic contraction estimate.

The desired comparison becomes

\[
X_a^*X_a
\preceq
\widetilde{\mathsf B}_{\alpha,k},
\]

not domination by the original Plancherel/prolate bulk alone.

## Consequence for the higher cell

The rung-five cell is genuinely an extension cell: it adds a boundary sector
that is absent from the lower bulk completion. It cannot be compressed into the
old bulk without losing continuity.

Thus the higher-dimensional mechanism does not prove positivity by discovering
hidden capacity in the old bulk. It first constructs the correct enlarged
carrier on which the boundary map is bounded. The remaining arithmetic theorem
is semiboundedness of the coupled gamma--prime form on that extension.

## Status

The attempted direct physical-bulk comparison fails for a precise topological
reason. The correct next comparison is between the completed endpoint graph and
an endpoint-augmented physical common bulk.
