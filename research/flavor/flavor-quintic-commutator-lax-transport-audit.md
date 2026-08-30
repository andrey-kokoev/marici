# The First Commutator Covariant Is Lax Transport, Not Shape Selection

Work package: WP928

## Question

Does the lowest-degree commutator-sensitive covariant evade WP927 and select a
nondegenerate physical flavor point?

## Quintic covariant

The first explicit commutator term has tensor degree five:

\[
\beta_{Y_a}=\kappa_a[H_u,H_d]Y_a,
\qquad a\in\{u,d\}.
\]

Since (C=[H_u,H_d]) is anti-Hermitian, the induced Gram flow is

\[
\dot H_a=\kappa_a[C,H_a].
\]

This is Lax form. Every individual spectral power trace is preserved:

\[
\frac{d}{dt}\operatorname{tr}(H_a^k)=0.
\]

Therefore the operation cannot select either sector's two eigenvalue-shape
ratios.

## Common-coefficient branch

When (\kappa_u=\kappa_d), both Grams undergo the same unitary conjugation,

\[
H_a(t)=U(t)H_a(0)U(t)^\dagger.
\]

This is precisely a weak-basis orbit. All joint trace invariants and the
commutator determinant are preserved. The vector field is nonzero on literal
matrices but descends to zero on physical16.

This is the sharpest possible instance of the distinction between algebraic
motion and physical motion.

## Unequal coefficients and fixed points

Unequal (\kappa_u,\kappa_d) can transport relative eigenvectors and hence
mixing data, but each Gram remains on its original spectral leaf. It still
cannot supply the missing discriminant normalization.

For invertible Yukawas, a fixed point with any relevant nonzero (\kappa_a)
requires

\[
[H_u,H_d]=0.
\]

That eliminates CP violation. Setting the coefficient to zero leaves the CP
orientation unconstrained. Thus the fixed-point dichotomy is commuting or
unselected, not an isolated CP-violating point.

## Exact hostile

The checker uses (H_u=\operatorname{diag}(1,2,3)) and a rationally rotated
positive (H_d) with spectrum ((4,5,7)). Their commutator and literal Lax
velocities are nonzero. Nevertheless all six individual power-trace
derivatives and the common-flow derivative of
(\operatorname{tr}(H_uH_d)) vanish exactly. The commutator itself is constant
under the common flow.

## Verdict

The lowest commutator covariant is a transport operator, not a spectral-shape
selector. With common coefficient it is entirely quotient-trivial; with
unequal coefficients it may transport orientation but cannot fix spectra.

The next candidate must be Hermitian and commutator dependent, such as a
double-commutator gradient. Its coefficient and sign must be source-derived,
and its fixed locus must be tested for isolated noncommuting points rather than
assumed from dissipation language.

No physical instrument gate opens before such an operation descends
nontrivially to physical16 and survives thresholds.

## Verification

Run:

~~~text
uv run --with sympy python research/flavor/checkers/wp928_quintic_commutator_lax_transport_audit.py
~~~
