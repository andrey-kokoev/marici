# Finite-symmetry averaging produces a natural repair only after inverting its order

Epistemic-graph event: 1350.

## Averaging theorem

Let a finite group `Gamma` of order `m` act on a nonempty affine torsor of
pairing-preserving radical repairs over a coefficient ring in which `m` is
invertible.  For any repair `C`, the affine average

`C_av=(1/m) sum_(gamma in Gamma) gamma C`

is again a repair and is `Gamma`-fixed.

The repair equation is affine-linear and invariant, so averaging preserves
it.  Radical-valuedness and all coefficient pairings are preserved as well.
Thus Ledger 1331's class in `H^1(Gamma,A)` vanishes after `m` is inverted.

The averaged point need not be the unique natural repair.  All fixed repair
classes still form a torsor under `A^Gamma`; uniqueness additionally requires
`A^Gamma=0`.

## Integral and bad-prime boundary

Without division by `m`, the orbit sum is not an affine point of the original
torsor.  Ledger 1331's action `sigma(x)=1-x` on the integral torsor `Z`
illustrates the failure: its formal average is `1/2`, not integral.  Modulo
two, the corresponding first-cohomology obstruction need not be removable by
averaging.

This is parallel to, but distinct from, finite-deck normalization.  Here the
average changes only a pairing-invisible radical correction, whereas deck
averaging can rescale a frozen visible selector.  Neither operation is
physically authorized solely by algebraic existence.

## Five-site consequence

If a physical five-site pairing has radical repair freedom and the relevant
automorphism group is a two-group, natural repair is automatic only after
inverting two.  Integral or mod-two naturality requires an independent fixed
repair or a direct vanishing proof for the `H^1` class.
