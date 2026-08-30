# Exact cubic tangent from a Gaussian density state

## Frozen evolution

Use one canonical pair with `[Q,P]=2i` and the exact cubic unitary

\[
U_t=\exp(-itQ^3/6).
\]

Then

\[
U_t^\dagger P U_t=P-tQ^2.
\]

For a centered parity-even Gaussian state with

\[
\langle Q^2\rangle=a,
\]

the centered transformed momentum is

\[
\Pi_t=P-t(Q^2-a).
\]

## First non-Gaussian direction

Gaussian Wick reduction gives

\[
\kappa_{QQ\Pi}(t)
=\langle Q^2\Pi_t\rangle_{\rm Weyl}
=-t(\langle Q^4\rangle-a\langle Q^2\rangle)
=-2ta^2.
\]

Thus the exact density-state orbit leaves the Gaussian cone in a connected
third cumulant at first order.

For the Entry 1630 coordinate

\[
Z=\operatorname{Re}\langle Q^2S\rangle,
\qquad
S=(Q\Pi+\Pi Q)/2,
\]

the cubic correction is proportional to

\[
-t(\langle Q^5\rangle-a\langle Q^3\rangle)=0.
\]

The connected fourth-cumulant directions used in Entry 1627 likewise have no
linear term on this centered parity-even Gaussian orbit.  Hence Entry 1630's
free degree-four `Z` direction is not the first source cubic tangent.

This does not prove that its truncated packets lack density-operator
extensions; it only rejects the proposed tangent identification.

## Verification

`checkers/gaussian_cubic_first_tangent.rs` verifies the polynomial formulas on
1,209 exact integer parameter packets.  Density representability itself is
exact, because the complete orbit is `rho_t = U_t rho_0 U_t^dagger`.
