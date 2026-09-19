# The rapid-label rigging makes all polynomial-logarithmic Euler rows entire dual sections

## General coefficient theorem

Let

\[
\mathcal S_{\mathrm{lab}}
=
\bigcap_{a>0}\ell^2(\mathbb N,n^{2a}).
\]

Suppose a labelled coefficient row satisfies

\[
|b_n|\le C n^m(1+\log n)^r
\]

for fixed `m,r`. Define

\[
B_s(c)=\sum_{n\ge1}b_n c_n n^{-s}.
\]

For every compact `K` in the `s`-plane, choose `a` so large that

\[
a+\inf_{s\in K}\operatorname{Re}s-m>\frac12.
\]

Then Cauchy--Schwarz gives

\[
|B_s(c)|
\le
C p_a(c)
\left(
\sum_{n\ge1}
(1+\log n)^{2r}
 n^{-2(a+\operatorname{Re}s-m)}
\right)^{1/2}.
\]

The series converges uniformly for `s` in `K`. Differentiating in `s` only
adds powers of `log n`, so every parameter jet obeys the same kind of bound.
Thus `s -> B_s` is a weakly entire, compact-locally equicontinuous section of
`S_lab'`.

## Euler rows

The von Mangoldt row satisfies

\[
0\le\Lambda(n)\le\log n.
\]

Therefore

\[
\Psi_s(c)=\sum_{n\ge1}\Lambda(n)c_n n^{-s}
\]

and all its `s`-jets are continuous entire dual sections. Restriction to
primitive prime labels or to any fixed prime-power grade remains continuous,
as does the valuation-excess decomposition whose combined coefficient is
`log n`.

The reciprocal rows with `n^{s-1}` are obtained by `s -> 1-s` and have the
same property. Hence primitive, repeated-valuation, and full logarithmic
interval currents all coexist with the two exterior Mellin channels on one
explicit projective label rigging.

## Topological meaning

This is distributional continuity, not boundedness on the source-normalized
Green Hilbert space. The latter generally fails because normalization cancels
the Euler half-density label by label. The projective rigging is precisely
what permits the exterior observer and arithmetic currents to remain typed
without manufacturing a bounded rank-one loading.

## Remaining comparison

The label-side continuity gate is closed for every Euler row of
polynomial-logarithmic growth. What remains is a mixed-carrier theorem:
combine this discrete rigging with the exponential radial test space and
prove that the Hardy ordered port, endpoint traces, and polarized Green
current define one path-independent five-wall boundary morphism. Scalar
entireness alone does not supply that comparison cell.
