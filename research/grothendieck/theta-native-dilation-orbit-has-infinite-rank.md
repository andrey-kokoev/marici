# The Native Theta Dilation Orbit Has Infinite Rank

## Source generator

For one positive-chart theta label, put

\[
X=\pi n^2e^{2u}.
\]

Up to a nonzero label-dependent constant, the atom is

\[
\phi_n(u)
=X^{1/4}e^{-X}(4X^2-6X).
\]

The native translation in (u) acts by the dilation generator

\[
\partial_u=2X\partial_X.
\]

After removing the fixed factor (X^{1/4}e^{-X}), its action on a polynomial (P) is

\[
\mathcal DP
=2XP'(X)+(1/2-2X)P(X).
\]

## Triangular degree growth

If (P) has degree (d) and leading coefficient (a), then (\mathcal DP) has degree (d+1) and leading coefficient (-2a). Starting from (4X^2-6X), the reduced polynomial after (k) dilations therefore has degree (k+2) and leading coefficient

\[
4(-2)^k.
\]

Distinct degrees make every finite initial packet linearly independent. Hence

\[
\operatorname{span}
\{\phi_n,\partial_u\phi_n,\partial_u^2\phi_n,\ldots\}
\]

is infinite-dimensional for every label (n).

## Completed-source consequence

The primitive label already prevents finite-dimensional closure. Moreover, at large positive (u), the (n=1) atom dominates every higher label exponentially. Any constant-coefficient differential recurrence for the completed sum would induce a polynomial cancellation in the dominant (n=1) reduced orbit. The triangular leading degrees force every coefficient to vanish.

Therefore neither a single theta label nor the completed source satisfies a nontrivial finite constant-coefficient recurrence under the native dilation generator.

## Meaning for the odd comparison port

The finite escape hatch left by the moment hostile is closed in its natural linear form. Theta transport does not collapse the complete odd/tangent tower to a finite-dimensional dilation module. Each further derivative contains a genuinely new polynomial direction before scalar aggregation.

The faithful choices narrow to:

1. retain the primitive reciprocal tails themselves;
2. retain the complete function-valued odd port;
3. use an infinite tower with its completion topology;
4. derive a nonlinear or variable-coefficient modular law carrying additional source data.

The fourth possibility is not ruled out, but it is no longer a finite linear closure. Any such law must name its additional coefficient fields and prove that they are source-derived rather than fitted from (\Xi).

## Scope

This is an exact infinite-rank theorem for the native dilation representation and a no-go for constant-coefficient finite differential closure. It does not rule out nonlinear identities, modular correspondences involving transformed arguments, or variable-coefficient equations with independently derived coefficients.

## Verification

The exact symbolic checker `research/grothendieck/checkers/theta_dilation_orbit_has_infinite_rank.py` verifies degree growth, the leading-coefficient formula, full Krylov rank, and absence of constant-coefficient relations through order twelve. It writes `research/grothendieck/results/theta_dilation_orbit_has_infinite_rank.json`.
