# Loewner rediscovery and meaning audit

## Exact identification with the earlier program

The recent angular-current route defines

\[
H(w)=\left(w-\frac14\right)\frac{C'(w)}{C(w)},
\qquad C(w)=\Xi\!\left(\frac12+\sqrt w\right)
\]

up to the fixed Xi normalization convention.

The earlier reduced gamma--prime program defined a source function
\(\texttt{reduced\_F}(w)\). Direct substitution of
\(s=1/2+\sqrt w\) gives the exact identity

\[
\boxed{\texttt{reduced\_F}(w)=4H(w).}
\]

Therefore the following were already established before the recent thimble
and energy-flow work:

1. the RH-equivalent Herglotz/Pick target for this normalized function;
2. its Loewner divided-difference kernel;
3. the conditional positive rank-one expansion from real squared zero
   coordinates;
4. the reconstruction of a positive resolvent measure and self-adjoint model
   after global kernel positivity; and
5. the quarter-centered angular-modulus reformulation.

The recent finite Pick-matrix checker extends reconnaissance to new tuples,
but it does not introduce a new equivalence.

## What is genuinely new

The return through relative cycles and the undecomposed theta source added a
different layer of meaning:

### 1. Denominator-free current

\[
Q=\Re\!\left[(\beta-i\alpha)B'\overline B\right]
\]

extends smoothly through zeros and satisfies
\(B=0\Rightarrow Q=0\). Strict positivity therefore supplies nonvanishing
rather than requiring it as a premise.

### 2. Relative-cycle invariance

The thimble self and cross terms are coordinates for one Hermitian quadratic
functional of the physical relative class. Integral Picard--Lefschetz basis
mutation leaves it invariant.

### 3. Exact characteristic dynamics

The cone vector field linearizes under \(w=z^2\):

\[
\dot w=-4i(w-1/4).
\]

This derives the centered-circle foliation as the actual energy-flow
characteristics.

### 4. Source-operator origin of the center

For the modular theta profile \(A\),

\[
\Phi=(\partial_u^2-1/4)A.
\]

Thus \(w-1/4\) is the transform symbol of the source operator, not merely a
successful fractional normalization.

### 5. Canonical endpoint subtraction

With \(K=\cosh(u/2)-A(u)\),

\[
\Phi=(1/4-\partial_u^2)K,
\qquad
Z(z)=(1/4-z^2)F(z)
\]

inside the critical strip, with honest vanishing endpoint terms.

### 6. Boundary-zero ingress meaning

A simple critical-line zero is a quadratic zero-energy boundary minimum with
strictly positive inward curvature. It is an admissible generator of flow,
not a singular obstruction.

### 7. Denominator-free Loewner form

\[
L_C(x,y)=
\frac{(x-1/4)C'(x)C(y)-(y-1/4)C'(y)C(x)}{x-y}
\]

is the analytic congruence-cleared form of the earlier Loewner kernel and
extends through allowed real zeros.

## Changed interpretation

The earlier program correctly identified the RH-equivalent positive kernel
and conditional operator completion. Its unresolved instruction was "find a
source Gram factorization."

The new work does not bypass that gate. It changes what a satisfactory
factorization must explain:

- why the center is forced by the theta differential operator;
- how endpoint null modes produce the completed pole cancellation;
- why real-axis zeros are positive atoms rather than exceptions;
- why wall-crossing decompositions cannot affect the invariant current; and
- why the faithful positivity statement should be made before dividing by
  \(C(x)C(y)\).

This is explanatory progress even though the central positivity theorem is
the same theorem.

## Revised constructive target

The target is no longer an unspecified Gram factorization of a discovered
Loewner kernel. It is:

> Construct a Gram factorization of the denominator-free kernel \(L_C\) from
> the Green pair \(K\xrightarrow{1/4-\partial_u^2}\Phi\), with the two
> asymptotic null modes and their endpoint cancellation represented
> explicitly.

Such a construction would connect the source differential operator to the
positive resolvent measure. A factorization reconstructed from zero poles
would remain circular.

The exact pullback has now been written as a two-copy integral of the
renormalized precursor against the transform kernels
\(\phi_w=\cosh(\sqrt w\,u)\) and \(\psi_w=\partial_w\phi_w\). See
`theta-renormalized-precursor-loewner-pullback.md`.

## Falsifier

If the Green identity for the renormalized precursor produces an unavoidable
indefinite boundary form, then the new source interpretation does not close
the old positivity gate. The Loewner equivalence would remain correct, but
the proposed explanation would fail.
