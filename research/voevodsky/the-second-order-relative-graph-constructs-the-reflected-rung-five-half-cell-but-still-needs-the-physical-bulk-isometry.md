# The second-order relative graph constructs the reflected rung-five half-cell but still needs the physical-bulk isometry

## Source-derived half-cell

On the weighted second-order relative graph, define

\[
X_a f=
\left(
 f(-\infty),f(+\infty),
 w_a^{1/2}f',w_a^{1/2}f''
\right).
\]

Its norm is exactly the declared graph energy:

\[
\|X_af\|^2
=
|f(-\infty)|^2+|f(+\infty)|^2
+
\int w_a(|f'|^2+|f''|^2).
\]

Let \(P_{end}\) be the orthogonal projection onto the first two coordinates and
let \(P_{bulk}=I-P_{end}\). Then

\[
\beta_af=P_{end}X_af,
\qquad
Y_af=P_{bulk}X_af,
\]

and the noncircular identity is exact:

\[
\boxed{
\|X_af\|^2
=
\|\beta_af\|^2+
\|Y_af\|^2.}
\]

Thus endpoint observation is an actual orthogonal projection of a
source-reached positive feature and is automatically contractive.

## Reflection

Reflection about the seam exchanges the two endpoint coordinates, preserves the
weighted derivative energy, and reverses flux. Hence the reflected half-cell is
the adjoint/orientation mate of the original one. Translation of the seam is
isometric when the weight is translated simultaneously.

Therefore the second-order graph supplies a genuine dagger/reflection-compatible
rung-five cell on the endpoint-history subsystem, naturally under seam motion.

## Source provenance

For the Volterra source map

\[
(H_ag)(u)=\int_{-\infty}^u g(v)\,dv,
\]

one has

\[
(H_ag)'=g,
\qquad
(H_ag)''=g'.
\]

Thus both the endpoint coordinates and the positive remainder \(Y_aH_ag\) are
constructed from the same source density. The remainder is not defined as the
square root of a desired Schur margin.

## Missing comparison

The graph identity proves contraction relative to the graph Gram

\[
X_a^*X_a.
\]

The physical pyramid requires contraction relative to the common prolate/Widom
bulk \(\mathsf B_{\alpha,k}\). Hence the remaining equation is the isometric
comparison

\[
\boxed{
X_a^*X_a
=
\mathsf B_{\alpha,k}}
\]

on the source-generated domain, or at minimum the domination

\[
X_a^*X_a\preceq\mathsf B_{\alpha,k}.
\]

If this comparison holds, then

\[
\beta_a^*\beta_a
\preceq X_a^*X_a
\preceq\mathsf B_{\alpha,k},
\]

which proves the required Schur--Douglas inequality without circularity.

## Result

The reflected rung-five mechanism is already present on the completed endpoint
graph. What remains is no longer construction of its norm-square half-cell; it
is identification of that source graph energy with the physical common bulk.
