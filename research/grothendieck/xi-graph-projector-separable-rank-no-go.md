# No fixed finite family of one-variable traces can realize the graph projector

Let `D={rho_1,...,rho_N}` be a finite conjugation-stable divisor truncation.
The conjugation-graph matching kernel is

```
G_ij = 1  if rho_j=conj(rho_i),
       0  otherwise.                                  (1)
```

It is a permutation matrix, hence

```
rank G = N.                                            (2)
```

Suppose one attempts to construct it from `m` independent one-variable
channels,

```
G_ij = sum_(k=1)^m f_k(rho_i) g_k(rho_j).              (3)
```

Each summand is rank one, so

```
rank G <= m.                                           (4)
```

Therefore exact graph matching requires

```
m >= N.                                                (5)
```

As the divisor window grows, no fixed finite collection of scalar explicit
formulas can implement the conjugation graph. The missing object must be
operator-valued, infinite-channel, or supplied as a genuine correspondence
rather than reconstructed from finitely many separable traces.

## Weighted defect kernel

Multiplying the graph permutation by nonzero diagonal reflection weights
preserves rank on the off-line sector. Thus an off-line truncation with `M`
nonzero defect weights still needs at least `M` separable channels. On-line
weights vanish, as they should; this does not reduce the rank obstruction
for a hostile branch containing arbitrarily many off-line orbits.

## Small C2 test

For one free conjugate pair the graph matrix is

```
[0 1]
[1 0],                                                 (6)
```

of rank two. A single product trace cannot reproduce it. For the smallest
off-line quartet the graph projector has rank four. This is the linear
algebraic reason the independent doubled trace failed numerically.

## Scope

This is a representation-rank no-go, not a claim that source realization is
impossible. Countably many channels, a reproducing kernel, a Hilbert-module
correspondence, or a normal operator with real structure can carry the full
rank. The theorem rules out only a fixed finite scalar reduction.

