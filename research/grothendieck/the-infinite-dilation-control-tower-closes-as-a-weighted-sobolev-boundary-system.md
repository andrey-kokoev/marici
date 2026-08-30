# The Infinite Dilation Control Tower Closes as a Weighted Sobolev Boundary System

## Canonical completion

Let

\[
y=e^{2u}-1,
\qquad
(U\psi)(u)=(1+y)^{1/4}\psi(y).
\]

Equip the dilation half-line with

\[
d\nu(y)=\frac12(1+y)^{-1/2}dy.
\]

Then

\[
\|U\psi\|_{L^2(du)}^2
=
\|\psi\|_{L^2(d\nu)}^2.
\]

Thus `U` is unitary. The transported dilation operator

\[
A=2(1+y)\partial_y+\frac12
\]

satisfies

\[
UAU^{-1}=\partial_u.
\]

There is therefore no need to guess a Fock weight. The canonical completion is
the pullback of the ordinary logarithmic Sobolev boundary system:

\[
\operatorname{Dom}(A)
=
U^{-1}H^1(0,\infty).
\]

Since the weak derivative is closed on `H^1`, `A` is closed in this domain.

## Seam trace

The endpoint value is continuous in the graph norm by the one-dimensional
Sobolev trace theorem. In the dilation frame,

\[
(U\psi)(0)=\psi(0).
\]

Hence the Green identity is a closed boundary-system identity:

\[
2\Re\langle A\psi,\psi\rangle_{\nu}
=-\left|\psi(0)\right|^2
\]

for decaying domain states. The seam is not reconstructed from a tail norm and
is not discarded in completion. It is the continuous trace of the graph
domain.

## Meaning of the infinite raising wall

In the monomial-exponential coordinates

\[
e_j=y^je^{-\lambda y},
\]

the operator has an outward arrow at every grade. This proves that finite
polynomial truncations are not invariant. It does not imply that the completed
operator is ill-defined: the full tower is simply a nonorthogonal coordinate
presentation of the closed translation generator.

The distinction is:

- finite algebraic closure fails;
- graph completion succeeds;
- seam evaluation survives continuously;
- arbitrary coefficient norms remain unauthorized.

## Theta labels are analytic vectors

For one theta label,

\[
h_n(u)=e^{u/2}P(\pi n^2e^{2u})
e^{-\pi n^2e^{2u}},
\]

where `P` is quadratic. Its holomorphic continuation in `u` decays uniformly
on every closed substrip

\[
|\Im u|<\frac{\pi}{4}.
\]

Indeed, the exponential has modulus controlled by

\[
e^{-\pi n^2e^{2\Re u}\cos(2\Im u)},
\]

and `cos(2 Im u)` stays positive in such a substrip. Cauchy estimates then
give, for every radius smaller than `pi/4`, constants `C` and `R` such that

\[
\|A^kh_n\|
\leq C R^k k!.
\]

Thus each theta label is an analytic vector for the completed control
generator. Its outward-grade orbit does not escape the graph completion.

## Scope boundary

This resolves the completion problem for the archimedean dilation tower. It
does not prove that finite monomial cutoffs have vanishing top currents under
an arbitrary truncation scheme, nor does it close the arithmetic reciprocal
boundary identity. A convergent cutoff must approximate in the graph norm,
not merely retain the first `N` monomials.

The next RH-bearing gate is consequently no longer closedness. It is whether
the reciprocal pair of these completed boundary systems has a source-derived
comparison whose seam traces cancel while its joint graph norm remains
faithful.

## Result

The infinite control tower has a canonical, completion-stable realization as
a weighted Sobolev boundary system unitarily equivalent to logarithmic
translation. The quarter-density simultaneously fixes the norm, the closed
generator, and the seam trace. Completion does not lose the individual theta
states; the unresolved information lies in reciprocal-sheet comparison.

