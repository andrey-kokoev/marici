# Grothendieck quadratic Hermite companion

## Source mapping

Source:
`research/grothendieck/theta-bordered-divisor-has-a-canonical-krein-realization.md`.

For the monic quadratic

\[
p(z)=z^2+a_1z+a_0,
\]

`quadraticCompanion a₀ a₁` is the multiplication-by-`z` companion matrix in
the basis `1,z`. `quadraticHermite s₀ s₁ s₂` is the first Hankel/Hermite block
of the coefficient-derived Newton sums. The only recurrence needed in degree
two is

\[
s_2=-a_0s_0-a_1s_1.
\]

## Lean results

`quadraticHermite_companion_symmetry` proves

\[
\mathcal H C=C^T\mathcal H
\]

over an arbitrary commutative ring from that recurrence alone. It neither
mentions roots nor assumes positivity.

For `p(z)=z²+1`, the Newton data are `(s₀,s₁,s₂)=(2,0,-2)`.
`nonrealPair_companion_symmetric_for_Hermite` proves the same companion
symmetry, while `nonrealPair_Hermite_has_negative_direction` evaluates the
form on the second basis vector to `-2`. Thus coefficient-derived Krein
selfadjointness does not promote the Hermite form to a Hilbert metric.

## Remaining general-degree interface

The arbitrary-degree theorem needs a finite companion definition and the full
Newton recurrence indexed beyond the companion boundary. The classical rank
and signature theorem is separate again; it must not be replaced by an
assumption that the theta polynomial is real-rooted.

## Verification

Per Nima's instruction, no Lean build was run. This module is not imported by
`MariciFormal.lean`; elaboration remains unverified.
