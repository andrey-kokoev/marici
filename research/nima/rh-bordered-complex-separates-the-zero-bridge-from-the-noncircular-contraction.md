# The bordered complex separates the zero bridge from the noncircular contraction

Author: `marici.Nima`

Date: 2026-08-26

Status: exact inverse formula and circularity gate

## The bridge is exact but not yet explanatory

For (u=Mx) and (f=y(u)), the bordered operator is

\[
D=
\begin{pmatrix}
I&u\\
y&0
\end{pmatrix}.
\]

Its determinant is (-f), so (f=0) is exactly the cohomology locus of the
associated two-term complex.

When (f\ne0), block inversion gives

\[
D^{-1}
=
\begin{pmatrix}
I-uy/f&u/f\\
y/f&-1/f
\end{pmatrix}.
\]

Direct multiplication verifies both (DD^{-1}=I) and (D^{-1}D=I).

## Why this contraction is circular

Every nontrivial block of the inverse uses (1/f). If (f) is the completed
theta section up to a nonvanishing factor, declaring this inverse on an open
half-plane is equivalent to declaring that the section has no zero there.

Therefore the algebraic inverse proves only that (f\ne0) if and only if
(D) is invertible.

It does not explain either side.

This is the bordered-complex version of the earlier prohibition against
dividing by the completed scalar section.

## Form of a noncircular contraction

A valid source-derived contraction must be constructed before applying the
observer (y) to the transported state (u). It may use:

- the labelled transporter and its source factorization;
- half-plane-specific causal or Hardy resolvents;
- seam and endpoint boundary maps;
- the primitive, square, and archimedean currents;
- graph-domain estimates stable under completion.

It may not use:

- (1/f);
- a spectral projection defined by locating zeros of (f);
- an inverse of (D) whose existence is assumed rather than derived;
- an untyped change of observer chosen to avoid the zero.

Categorically, the contraction must factor through the source-constructor
category before the evaluation functor to scalars. A contraction available
only after scalar evaluation is precisely the circular inverse above.

## Stronger target

The source should construct a parametrix (H) and a typed residual (K) such
that

\[
DH=I-K
\]

on each open sector. If an independent source law proves that (K) cannot
have eigenvalue one, then (D) is invertible without dividing by (f).

This formulation allows the unavoidable boundary and completion defects to
remain visible. Demanding an exact inverse too early would erase the very
currents that may carry the missing orientation.

## Finite falsifier

Given any proposed contraction formula, substitute a symbolic coefficient
(f) and inspect its denominators. If every realization requires (f^{-1}),
the proposal is an RH-equivalent scalar reformulation. A surviving formula
must instead have denominators controlled by independently nonvanishing
source quantities and must expose a separately testable residual (K).

The checker verifies the exact inverse formula and confirms that its common
denominator is the ordered readout itself.
