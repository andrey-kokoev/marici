# Spectral-cutoff radicals form an inverse, not direct, quotient system

## Correction

The proposed requirement that a cutoff transition map carry the rank-two radical into the next radical has the wrong variance for positive spectral truncations.

Let `V` be a fixed finite test space and let

`G_N=sum_(j<=N) w_j F_j^* F_j`,

with positive weights. Adding one spectral pair gives

`G_(N+1)=G_N+w_(N+1) F_(N+1)^*F_(N+1)`.

Therefore

`rad(G_(N+1)) = rad(G_N) intersect ker(F_(N+1))`,

so

`rad(G_(N+1)) subset rad(G_N)`.

The radicals shrink as the cutoff increases.

## Quotient variance

The identity on `V` induces a canonical map

`V/rad(G_(N+1)) -> V/rad(G_N)`,

because the finer radical is contained in the coarser one. This map is surjective. In the opposite direction, a class modulo `rad(G_N)` has no canonical lift modulo the smaller radical: a vector previously identified with zero may become detectable at the next cutoff.

Hence the finite quotient spaces form an inverse system under canonical projections, not a direct system under inclusions.

## Four-cell rectangle

For one generic conjugate spectral pair, the `1,2,3,6` Gram has rank two and a two-dimensional radical. Adding a second noncollinear pair generically makes the Gram rank four and removes the radical. No identity-induced map can send the first quotient into the second while preserving representatives: the second pair distinguishes classes collapsed at the first stage.

This is not a pathology. It is exactly how additional spectral probes increase resolution.

## Completion consequences

A cutoff-compatible construction has three admissible forms:

1. retain the common pre-quotient core `V` and quotient only by the radical of the completed form;
2. use the inverse system of finite quotients and prove an appropriate projective-limit statement;
3. supply noncanonical splittings with independent source authority and coherence proofs.

The third option cannot be inferred from positivity or dimensions. The first is analytically simplest but requires closability and exact identification of the completed radical. The second retains finite quotient data but requires proving that the projective limit agrees with the completed form quotient and introduces no phantom compatible families.

## Relation to Voevodsky's audit

This corrects the earlier proposed acceptance test. Radical stability cannot mean that every finite radical persists. The correct invariant is that the completed quotient is derived from one common core and that finite inverse projections agree with the completed restriction maps. Voevodsky's warnings about new limiting radicals remain active, but the present phenomenon is the opposite: finite radicals disappear when additional spectral components are admitted.

## Cheapest falsifier

Given any proposed direct cutoff map induced by the identity, choose a vector in

`rad(G_N) setminus rad(G_(N+1))`.

It is zero in the source quotient and nonzero in the target quotient, so the proposed map is not well defined. For the rectangle, a symbolic two-frequency example supplies this witness generically.

## Disposition

The direct quotient-transition target is rejected. Future `R_zeta` constructions must act on the common Mellin-Schwartz core before quotienting, or use the correctly oriented inverse quotient system.
