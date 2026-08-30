# Arithmetic reciprocal incidence matches the rigged transpose but is not a core for the seam

## Finite labelled boundary packet

Let a finite arithmetic grade have positive logarithmic supports `a_j` and
real weights `w_j`. At centered parameter `z`, write

\[
\nu_z^+
=
\sum_j w_je^{-za_j}\delta_{a_j}.
\]

Define conjugate-reflected transport by

\[
\mathfrak J\nu_z^+
=
\sum_j w_je^{-\overline z a_j}\delta_{-a_j}.
\]

This is the boundary-distribution form of reciprocal Real transport.

## Exact transpose matching

The completed theta forcing is real and even:

\[
f(-q)=f(q).
\]

Therefore

\[
B_f^\times(\mathfrak J\nu_z^+)
=
\sum_j w_je^{-\overline z a_j}f(-a_j)
=
\overline{
\sum_j w_je^{-za_j}f(a_j)
}
=
\overline{B_f^\times(\nu_z^+)}.
\]

This holds separately for:

- primitive supports `a=log p`;
- square supports `a=2 log p`;
- connected supports `a=k log p`, `k>=3`.

At finite cutoff it is an exact labelled identity, not a scalar continuation.
The previous common-domain theorem allows it to pass absolutely to each
completed arithmetic grade.

## What has been constructed

On the arithmetic boundary subobject, reciprocal Real transport and the
canonical rigged transpose are compatible. Thus the arithmetic adjoint
residual vanishes after evaluation on the fixed theta test vector.

This is weaker than the operator identity

\[
B_-=B_f^\times
\]

on the complete seam--tail dual. The arithmetic packet tests only discrete
boundary distributions.

## Failure of the core argument

Every positive arithmetic support satisfies

\[
a\geq\log2.
\]

Choose a nonzero smooth test function supported in the open interval
`(0,log 2)`. Every primitive, square, and connected-tail distribution
annihilates it. A seam distribution supported in that interval need not.

Consequently the span of arithmetic prime-power atoms is not weak-star dense
in the full positive-chart distribution space and is not a graph core for the
continuum seam incidence. Equality on all arithmetic grades cannot be extended
to the seam by density.

The obstruction is infinite-dimensional: the whole test-function space
supported in `(0,log 2)` lies in the annihilator of the arithmetic packet.

## Categorical meaning

The boundary object has at least two genuinely different subobjects:

```text
arithmetic atoms at prime-power logarithms
continuum seam history between arithmetic walls
```

Reciprocal transpose coherence on the first does not authorize coherence on
the second. The seam incidence must be derived independently and then compared
on overlaps and endpoint traces.

## Revised next gate

Construct the reciprocal transpose on the continuum seam interval itself.
For a cut length `L`, test the reflected restriction correspondence

\[
H^1(0,L)
\longleftrightarrow
H^1(-L,0)
\]

against the theta test--dual pairing, including value and flux traces at zero
and at the moving endpoint. Only after this local interval identity is proved
can arithmetic concatenation assemble a global return arrow.

## Scope

This proves gradewise arithmetic incidence matching and disproves extension by
arithmetic density. It does not construct the continuum seam adjoint, the
archimedean endpoint incidence, or a selfadjoint completed operator.
