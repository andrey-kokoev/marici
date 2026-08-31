# The relative seam return needs det2 to create an open reciprocal overlap

## Trace class stops at the centered line

For the right reciprocal chart, the primitive seam incidence has singular-size
model

\[
s_p(B(s))
\asymp
\frac{p^{-\sigma}}{\sqrt{\log p}},
\qquad
\sigma=\operatorname{Re}s.
\]

The Hilbert--Schmidt budget is

\[
\sum_p\frac{p^{-2\sigma}}{\log p}.
\]

It converges for \(\sigma\ge1/2\) and diverges for \(\sigma<1/2\).  Therefore
the ordinary trace-class return

\[
R(s)=B(s)^\dagger G(s)B(s)
\]

is available on the right closed half-strip but does not extend by the same
ideal estimate to an open neighborhood across the critical line.

The reflected chart has the symmetric condition \(1-\sigma\ge1/2\).  The two
ordinary Fredholm regions meet only on \(\sigma=1/2\), not on an open complex
overlap.  Equality on one real-codimension-one line is not holomorphic chart
gluing.

## Schatten-three incidence region

For \(q=3\),

\[
\sum_p s_p(B(s))^3
\asymp
\sum_p
\frac{p^{-3\sigma}}{(\log p)^{3/2}}.
\]

This converges for \(\sigma>1/3\); at the boundary, the extra prime-density and
logarithmic factors also give convergence, but the open region is sufficient.
Thus

\[
B(s)\in\mathcal S_3
\qquad(\operatorname{Re}s>1/3).
\]

The ideal product rule gives

\[
R(s)=B(s)^\dagger G(s)B(s)
\in\mathcal S_{3/2}
\subset\mathcal S_2.
\]

Hence the order-two regularized relative determinant

\[
\det_2(I-K_{\rm rel}(s))
\]

is defined holomorphically in the right region, provided the bounded propagator
and inverse loop factor depend holomorphically there.

## Reciprocal overlap

The reflected chart is valid when

\[
\operatorname{Re}(1-s)>1/3,
\]

that is, when \(\operatorname{Re}s<2/3\).  Therefore the two regularized
relative charts have the open overlap

\[
\frac13<\operatorname{Re}s<\frac23.
\]

This is the first operator-ideal overlap wide enough to support a holomorphic
reciprocal transition function.

## Centered relation to the Fredholm determinant

On the centered line the return improves to trace class.  There,

\[
\det_2(I-K)
=
\det(I-K)e^{\operatorname{Tr}K}.
\]

Thus replacing the ordinary determinant by \(\det_2\) introduces a first-trace
anomaly factor.  That factor must be matched with a source boundary current or
included in the reciprocal transition unit; it cannot be discarded.

## Separation from the bare Euler det3

Two regularizations now coexist for distinct reasons:

- the bare Euler loop uses \(\det_3\), with primitive and square cumulants as
  separate boundary data;
- the boundary-mediated relative return uses \(\det_2\) off the centered seam,
  improving to an ordinary Fredholm determinant on the seam.

Their anomaly factors and transition functions must be composed without
counting the primitive current twice.

## G4 consequence

An ordinary relative Fredholm determinant cannot provide reciprocal
holomorphic gluing because its two charts lack an open overlap.  The minimal
relative compiler on the strip is \(\det_2\).

The next exact theorem must construct the right and reflected
\(\mathcal S_2\)-families, prove on \(1/3<\operatorname{Re}s<2/3\) that their
ratio is a source-derived nowhere-zero transition function, and reconcile its
first-trace anomaly with the low-grade Euler boundary factors.

This advances ideal-class typing but does not prove the transition identity or
comparison with \(\Xi\).  G4 remains open, and no RH conclusion is authorized.
