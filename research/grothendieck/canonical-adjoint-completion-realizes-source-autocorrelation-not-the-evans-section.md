# Canonical adjoint completion realizes source autocorrelation, not the Evans section

## Forward tail realization

Let `D` denote the one-sided tail generator and let

\[
B_f:\mathbb C\longrightarrow E,
\qquad B_f(c)=cf
\]

be the source forcing. The decaying tail state is schematically

\[
G_z=(D-z)^{-1}B_f(1).
\]

The Evans readout producing the one-point transform is endpoint evaluation:

\[
F(z)=E_0G_z.
\]

This is linear in the source `f`.

## Canonical adjoint completion

The rigged transpose found earlier is

\[
B_f^\times(\lambda)=\lambda(f).
\]

Using it as the lower incidence of a symmetric block produces the Schur or
Weyl term

\[
M_f(z)=B_f^\times(D-z)^{-1}B_f.
\]

This is quadratic in `f`. In an `L2` realization it is

\[
M_f(z)=\langle f,G_z\rangle.
\]

Expanding the tail gives a two-point ordered autocorrelation integral, not the
one-point Evans transform.

## Smallest exact separation

Take `f(q)=1` on `[0,1]` and `z=0`. The decaying tail is

\[
G_0(q)=\int_q^1 1\,dv=1-q.
\]

The endpoint readout is

\[
E_0G_0=1,
\]

whereas the adjoint return is

\[
B_f^\times G_0
=\int_0^1(1-q)\,dq
=\frac12.
\]

Thus the canonical transpose does not reproduce the Evans observer even in
the smallest source model.

## Structural consequence

The canonical symmetric completion naturally realizes the source
autocorrelation, logarithmic curvature, or separation-measure object that
appeared repeatedly in the Green, Clark, and Stieltjes lanes. It does not
directly realize the Riemann section.

This explains the earlier compression:

```text
source forcing plus its adjoint
    -> two-point autocorrelation
    -> curvature / separation transform

source forcing plus endpoint evaluation
    -> one-point Evans section
```

The two constructions use different lower arrows.

## No scalar-unit shortcut

For different sources, or as `z` varies, the ratio between `M_f(z)` and
`F(z)` is not a fixed source-independent nowhere-zero unit. Replacing one by
the other would therefore alter the divisor problem rather than merely change
its presentation.

Any operator proof of RH must bridge endpoint evaluation to the adjoint source
return through an additional source-derived correspondence. It may not simply
identify them.

## Next constructor

The missing object must factor both observers through a larger boundary
reservoir:

\[
E_0G
\quad\text{and}\quad
B_f^\times G.
\]

Equivalently, seek a source-derived map `K` on the seam/history space such
that endpoint evaluation and source pairing are two boundary faces of one
Green correspondence. The equality required for zero confinement must then
follow from that correspondence, not from choosing the symmetric observer in
place of the physical Evans observer.

## Scope

This does not invalidate the canonical rigged transpose or its boundary-grade
matching. It shows that adjoint completion and determinant identification are
separate gates. The former is now constructed at boundary level; the latter
fails for the naive symmetric block.
