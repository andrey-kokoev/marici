# Singular nearby-boundary Bockstein gate

## Question

Does allowing the degeneration coefficient `1/t` produce the missing horn?

## Claim boundary

In a regular `Q[t]` complex, an identity `d(h)=t z` has two distinct consequences. After inverting `t`, `d(h/t)=z`; in the regular lattice, `h/t` is absent. Modulo `t`, `h` is closed and the connecting morphism sends its class to `[z]`. The simple pole therefore records a `t`-Bockstein or vanishing class, not a regular nullhomotopy.

The arrangement circuit has coefficient residual `tZ`, which supplies the required first-order determinant pattern. It does not yet supply a typed degree-one precycle `h` or an equality

`d(h)=t (Xi_log,-sigma123)`

in a motivic or logarithmic total complex. Every additional differential component would also have to vanish.

## Disposition

The `1/t` route neither fills nor disproves the horn. It isolates the exact constructor still missing: a regular sourced arrangement-circuit precycle with the stated differential. The next leaf must construct or falsify that identity and audit all residual components; determinant divisibility alone is insufficient.

## Verification

- `research/voevodsky/check_cosmology_singular_nearby_boundary_Bockstein_gate.py`
- `research/voevodsky/results/cosmology_singular_nearby_boundary_Bockstein_gate.json`
