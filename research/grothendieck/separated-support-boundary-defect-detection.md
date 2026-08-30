# Separated boundary support prevents cancellation but not annihilation

Epistemic-graph event: 1333.

## Detection theorem

For composable forced maps, Ledger 1317 gives

`Omega_(r q)=Omega_r S_q+S_r Omega_q`.

Let

`A=im(Omega_r S_q)` and `B=im(S_r Omega_q)`

inside the terminal boundary-chain group.  If `A intersect B=0`, then

`Omega_(r q)=0`

implies both transported defects vanish separately:

`Omega_r S_q=0` and `S_r Omega_q=0`.

This is immediate pointwise: a vector in `A` cannot cancel a vector in `B`
unless both are zero.

To recover the untransported stage defects, two additional faithfulness
conditions are needed.  If `S_q` is surjective, then `Omega_r S_q=0` implies
`Omega_r=0`.  If `S_r` is injective on `im(Omega_q)`, then
`S_r Omega_q=0` implies `Omega_q=0`.  Under all three hypotheses, a passing
composite certifies both stages.

## Quotient warning

The formal deck-basis pushforward for a nontrivial quotient is surjective but
not injective.  Hence separated boundary-stratum support can prevent
cancellation and can expose the later-stage defect, yet an earlier defect may
still land in `ker(S_r)` and disappear.  Support separation alone is not a
terminal certification theorem.

## Small hostile annihilation

Let `S_q` be the identity, let `S_r=[1 0]`, take `Omega_r=0`, and let
`Omega_q` have image spanned by `(0,1)`.  Then `A=0`, `B=0`, so supports are
trivially separated and the composite defect vanishes, while `Omega_q` is
nonzero.  The later quotient annihilates the entire earlier obstruction.

## Five-site acquisition rule

Source-labelled boundary strata should be retained because disjoint supports
rule out cancellation.  But every one-bit commutator must still be tested
unless the next forced map is proven injective on its defect image.  For the
rank-decreasing branch quotients, that extra proof cannot be inferred from
the formal deck map.
