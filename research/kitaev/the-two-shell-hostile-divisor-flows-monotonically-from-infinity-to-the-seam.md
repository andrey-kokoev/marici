# The Two-Shell Hostile Divisor Flows Monotonically from Infinity to the Seam

Consider the source-labelled family

\[
F_c(z)=\cosh z+c\cosh 2z,
\qquad 0<c<1.
\]

Its hostile zero pair is

\[
z_\pm(c)=\pm\alpha(c)+i\pi \pmod{2\pi i},
\]

where

\[
\alpha(c)=\operatorname{arcosh}a(c),
\qquad
a(c)=\frac{1+\sqrt{1+8c^2}}{4c}.
\]

Put \(s(c)=\sqrt{1+8c^2}\). Exact differentiation gives

\[
a'(c)
=-\frac{1+s(c)^{-1}}{4c^2}<0
\]

and therefore

\[
\alpha'(c)
=-\frac{1+s(c)^{-1}}
{4c^2\sqrt{a(c)^2-1}}<0.
\]

As \(c\downarrow0\), \(a(c)\to\infty\) and \(\alpha(c)\to\infty\). As
\(c\uparrow1\), \(a(c)\to1\) and \(\alpha(c)\to0\). Thus each hostile
branch flows strictly from infinity to the seam as the second-shell
coefficient increases from zero to its sharp threshold.

## Oriented divisor-flow observable

For either branch,

\[
\operatorname{Re}z_\pm(c)\,
\frac{d}{dc}\operatorname{Re}z_\pm(c)
=\alpha(c)\alpha'(c)<0.
\]

The sign is branch-independent: the negative branch has both its position and
velocity reversed. Equivalently,

\[
\frac{d}{dc}\frac12\bigl(\operatorname{Re}z_\pm(c)\bigr)^2<0.
\]

This is a Lyapunov law for off-seam distance along the specified coefficient
path. A positive sign is an exact finite falsifier of monotone inward divisor
transport.

The typing is essential. The derivative is meaningful only after the source
supplies:

- an oriented completion parameter;
- a differentiable family of operators or sections;
- continuation of a simple zero branch;
- a fixed seam and common coordinate frame.

Reversing the parameter reverses the velocity sign without changing the zero
set. A scalar completed section does not reconstruct its ancestral trajectory.
Hence this observable certifies a typed homotopy, not a static endpoint.

## Implicit constructor form

For a simple zero \(z(c)\) of a differentiable holomorphic family,

\[
F_c(z(c))=0,
\]

implicit differentiation yields

\[
z'(c)
=-\frac{\partial_cF_c(z(c))}{\partial_zF_c(z(c))}.
\]

For the two-shell family this becomes

\[
z'(c)
=-\frac{\cosh 2z(c)}{\sinh z(c)+2c\sinh 2z(c)}.
\]

This ratio is admissible only along a source-given simple-zero branch. Using
it to find zeros would be circular; using it after a divisor branch has been
independently constructed transports that divisor.

## Completion trichotomy

Suppose holomorphic approximants converge locally uniformly and hostile zeros
are followed along source-authorized branches. Any subsequence has only three
possible outcomes:

1. a bounded limit on the seam;
2. a bounded off-seam limit, which remains a zero of the limiting section;
3. escape from every compact set.

The present family realizes one continuous trajectory joining outcome 3 at
\(c=0\) to outcome 1 at \(c=1\). The RH-bearing task is not finite-shell
positivity. It is exclusion of outcome 2 for the actual completion, together
with control of whether outcome 3 is compatible with the chosen
normalization.

## Falsifiers

- A source-authorized simple branch with
  \(\operatorname{Re}z\,\operatorname{Re}z'>0\).
- Counting a reversed parameterization as an intrinsic failure.
- Inferring a divisor trajectory from the scalar endpoint alone.
- Applying the implicit quotient at a multiple zero where
  \(\partial_zF=0\).
- Claiming locally uniform convergence can erase a bounded off-seam limiting
  zero.
- Importing this monotone coefficient path into theta/Tate completion without
  deriving its source orientation.

## Process calibration

Pre-objective: excitement 10/10, confidence 9/10, expected information gain
10/10. The aim was to upgrade the square-root endpoint law into a complete
oriented divisor-flow theorem.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. The exact velocity is negative on both branches, and the observable is
now correctly typed as a homotopy certificate rather than endpoint data.
