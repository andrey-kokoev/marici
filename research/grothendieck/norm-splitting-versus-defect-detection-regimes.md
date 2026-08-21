# Norm splitting and invariant-defect detection have three arithmetic regimes

Epistemic-graph event: 1337.

## Regime theorem

Let `S T=d id` on a coefficient module `M`, where `S` is quotient
pushforward and `T` is fiber trace.

There are three distinct arithmetic regimes.

1. **Unit regime.** If `d` is invertible on `M`, then `(1/d)T` splits `S`,
   and `S` detects every vector in `im(T)`.
2. **Regular nonunit regime.** If multiplication by `d` is injective but `d`
   is not invertible, then `S` still detects `im(T)`, but the norm provides no
   scalar splitting inside the coefficient ring.
3. **Torsion regime.** If `M` has nonzero `d`-torsion, invariant vectors can
   be annihilated and norm-based detection may fail.

The second regime is genuinely intermediate.  Over `Z`, every positive
fiber degree is regular, so invariant integral boundary defects are detected,
even though no nontrivial degree is a unit.  Over `Z[1/d]` one enters the
unit regime.  Over `F_p` with `p|d`, one enters the torsion regime.

## Five-site specialization

Every nontrivial five-site branch kernel has order `2^k`.

- Over `Z`, fiber-invariant defects are detectable but norm splitting is
  unavailable.
- Over any ring in which `2` is invertible, both detection and splitting are
  available.
- In characteristic `2`, the norm can annihilate the entire invariant trace
  direction at every one-bit stage.

Thus integral failure to divide by the deck degree must not be confused with
failure to detect an invariant obstruction.  Conversely, the mod-2 branch
collapse is dangerous for both purposes.

## Scope

These are algebraic consequences of a supplied equation `S T=d id`.  They do
not assert that the frozen five-site source has physical chain-level maps
`S,T`; that admission remains open.
