# Positive reciprocal Pauli return region

## Question

What are the exact positivity and strict-return boundaries for a reciprocity-even Hermitian operator on the primitive-square Pauli plane?

## Reciprocal form

Conjugation reciprocity removes the \(Y\) coefficient, so the general reciprocal Hermitian return is

\[
K=aI+xX+zZ
=
\begin{pmatrix}
a+z&x\\
x&a-z
\end{pmatrix},
\qquad
a,x,z\in\mathbb R.
\]

Set

\[
r=\sqrt{x^2+z^2}.
\]

The eigenvalues are

\[
\lambda_-=a-r,
\qquad
\lambda_+=a+r.
\]

## Exact region

Positivity is equivalent to

\[
a\ge r.
\]

For a positive return, strict contraction is equivalent to

\[
a+r<1.
\]

Hence the reciprocal positive strict-return region is

\[
0\le r\le a,
\qquad
a+r<1.
\]

The terminal boundary is the upper cone surface

\[
a+r=1
\]

inside the positive cone. Positivity alone does not separate this boundary.

## Cross-grade mixing

The \(Z\) term is diagonal in the primitive-square basis, while \(X\) is the cross-grade route. Grade preservation holds exactly when

\[
x=0.
\]

Reciprocity permits every nonzero \(x\) satisfying

\[
x^2+z^2\le a^2,
\qquad
a+\sqrt{x^2+z^2}<1.
\]

Thus strict confinement is compatible with reciprocal cross-grade mixing. It requires a quantitative radial bound, not elimination of the \(X\) channel.

## Exact cases

A strict mixed return is

\[
a=\frac12,
\qquad x=\frac3{10},
\qquad z=0,
\]

with eigenvalues \(1/5,4/5\).

A terminal mixed return is

\[
a=\frac12,
\qquad x=\frac3{10},
\qquad z=\frac25,
\]

with \(r=1/2\) and eigenvalues \(0,1\).

A positive but superunit return is

\[
a=\frac34,
\qquad x=\frac35,
\qquad z=0,
\]

with largest eigenvalue \(27/20\).

## Physical boundary

The parameters \((a,x,z)\) are an exact coordinate classification once a physical return is mapped into this Pauli plane. Reciprocity determines the absence of \(Y\); it does not source the remaining coefficients. No current local arithmetic frame supplies their physical values.

## Verification

`research/aspect/checkers/check_positive_reciprocal_pauli_region.py` verifies exact rational strict, terminal, positive-superunit, and nonpositive cases.

## Disposition

The reciprocal two-port region is fully classified. The next executable optics question is which additional source symmetry, if any, constrains the radial coordinate \(r\) rather than merely deleting one Pauli direction.
