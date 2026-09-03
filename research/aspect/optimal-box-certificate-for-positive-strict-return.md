# Optimal box certificate for positive strict return

## Question

How do independent uncertainty bounds on scalar load, reciprocal mixing, and diagonal imbalance combine into a robust strict-return certificate?

## Uncertainty box

For

\[
K=aI+xX+zZ,
\]

assume

\[
a_{\min}\le a\le A,
\qquad |x|\le X,
\qquad |z|\le Z.
\]

Set

\[
\rho=\sqrt{X^2+Z^2}.
\]

Every matrix in the box is positive if and only if

\[
a_{\min}\ge\rho.
\]

Every positive matrix in the box is a strict return if and only if

\[
A+\rho<1.
\]

Thus the full robust certificate is

\[
\sqrt{X^2+Z^2}\le a_{\min}
\quad\text{and}\quad
A+\sqrt{X^2+Z^2}<1.
\]

If positivity is known independently, only the second inequality is needed.

## Optimality for independent bounds

The largest eigenvalue is increasing in \(a\) and in the radial coordinate \(\sqrt{x^2+z^2}\). The uncertainty corner

\[
a=A,
\qquad |x|=X,
\qquad |z|=Z
\]

attains \(A+\rho\). Therefore no smaller universal upper bound is available from the independent box data.

Likewise, the smallest eigenvalue is minimized at \(a=a_{\min}\) and the same radial corner, giving \(a_{\min}-\rho\).

## Exact cases

The box

\[
a_{\min}=\frac25,
\quad A=\frac12,
\quad X=\frac3{10},
\quad Z=0
\]

is robustly positive and has upper norm \(4/5\).

The box

\[
a_{\min}=A=\frac12,
\quad X=\frac3{10},
\quad Z=\frac25
\]

has \(\rho=1/2\) and reaches the terminal eigenvalue \(1\).

Reducing \(a_{\min}\) to \(1/4\) in that box destroys robust positivity while retaining the same upper boundary. This separates the lower and upper certificates.

## Mixing-only hostile

Even exact parity, \(X=0\), supplies no strict-return certificate without scalar and diagonal control. The admissible data

\[
A=1,
\qquad X=Z=0
\]

already reaches the terminal boundary. A parity-defect estimate must therefore be composed with source-derived bounds on \(A\) and \(Z\).

## Verification

`research/aspect/checkers/check_robust_return_certificate.py` verifies strict, terminal, positivity-failure, and zero-mixing hostile boxes with exact rational arithmetic.

## Disposition

The independent-box problem is completely classified. The certificate converts route-level parity control into strict confinement only after diagonal-load bounds are supplied; current local arithmetic data does not supply those physical bounds.
