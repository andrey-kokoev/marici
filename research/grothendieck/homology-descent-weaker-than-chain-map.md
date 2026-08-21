# Homology descent is strictly weaker than a physical chain map

Epistemic-graph event: 1331.

## Exact criterion

Let `S_n:C_n(G)->C_n(H)` be the pairing-forced graded map and

`Omega_n=D_H,n S_n-S_(n-1)D_G,n`.

Although `Omega=0` is equivalent to a strict chain map, `S` induces a
well-defined map on homology in degree `n` exactly when

1. `Omega_n(Z_n(G))=0`, and
2. `Omega_(n+1)(C_(n+1)(G))` is contained in `B_n(H)`.

The first condition says cycles map to cycles, since for `x` with `D_G x=0`,
`D_H Sx=Omega x`.  For a boundary `D_G y`, the identity

`S D_G y=D_H S y-Omega y`

shows that its image is a boundary exactly when the second condition holds.

## Strict separation

Take two-term integral complexes with

`D_G=D_H=diag(1,0)`,

and graded maps

`S_1=diag(0,1)`, `S_0=diag(1,1)`.

Then `Omega_1=diag(-1,0)` is nonzero, so `S` is not a chain map.  Nevertheless
the defect lies entirely in the contractible first summand.  The second
summand represents both homology groups, and `S` induces the identity on it.
Thus a homological readout can survive a genuine chain-level obstruction.

## Physical consequence

The five-certificate physical Mackey object still requires strict boundary
compatibility: a homology map alone does not supply a relative-chain
trace/Gysin operation, its endpoint normalization, or chain-level
composition.  But if the intended observable depends only on a specified
homology class, the smaller two-part criterion is the correct survival test.

Accordingly a future five-site boundary packet should report both verdicts:

- strict physical correspondence: every `Omega_n=0`;
- class-level readout: the two cycle/boundary containment conditions in the
  relevant degree.

Passing the second must not be promoted to the first.
