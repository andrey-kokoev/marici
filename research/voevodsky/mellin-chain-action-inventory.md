# Mellin affine-chain action inventory

## Question

Which declared operations actually act on the affine filler chain object, and which are known only at the period or relative-class level?

## Claim boundary

The inventory does not infer a chain action from modular terminology. Each action must name its locus and map.

## Actions

### Reciprocal negation

The map \(v\mapsto -v\) acts directly on the spectral affine chain object. Its strict simplex naturality is verified.

### Complex conjugation

Conjugation is real-linear and therefore affine on the underlying real space. Its chain action is conditional on invariance of the declared spectral domain.

### Stokes basis mutation

The theta source asserts Stokes basis mutation and covariance of Mellin jets. This establishes class/period-level covariance. It does not print an explicit chain map on the affine filler object, so chain-level naturality remains unverified.

### Euler cutoff transition

The source names finite-cutoff fillers \(M_X\) and cutoff refinement, but no transition map between filler chain objects is supplied. Naturality and completion cannot yet be typed.

## Excluded import

No nonlinear spectral inversion is declared on this chain object. Such an action cannot be imported merely because the surrounding construction is called modular.

## Disposition

Four action loci were audited. Reciprocal naturality is closed; conjugation is conditional; Stokes mutation stops at period covariance; cutoff transitions are absent. The first missing map is an explicit Stokes/basis chain action, followed by Euler-cutoff transition maps.

## Verification

- `research/voevodsky/mellin-chain-action-inventory-v1.json`
- `research/voevodsky/checkers/check_mellin_chain_action_inventory.py`
- `research/voevodsky/results/mellin_chain_action_inventory.json`
