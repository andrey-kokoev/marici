# Boundary-current cokernel class

Owner: `marici.Buzzard`

Source locator: `The doubled obstruction is a boundary-current cokernel class`
in `research/strominger/distinction-preserving-completion.md`.

## Formal increment

The finite density space is `Fin 3 → Rat`. The authorized boundary derivative
maps a scalar `t` to the line spanned by `(1,-1,0)`. The forcing residual is
`(1,0,-1)`. Scalar aggregation sums the three coordinates.

Lean proves:

- the authorized current direction has scalar aggregate zero;
- the forcing residual also has scalar aggregate zero;
- the forcing residual is not in the range of the authorized derivative;
- its class in the quotient by that range is nonzero.

Therefore vanishing of a scalar projection is strictly weaker than exactness
of the typed forcing residual. Equal endpoint bytes do not construct an
authorized boundary current.

## Hostile proof geometry

If the residual were `t * (1,-1,0)`, its first coordinate would force `t=1`,
while its second coordinate would force `t=0`. Lean records this contradiction
before passing to the quotient. The quotient theorem then uses the standard
criterion that a quotient class is zero exactly when its representative lies
in the submodule.

## Boundary and missing interfaces

This is the exact rational three-coordinate hostile fixture, not the completed
theta current. A sector-level theorem needs:

- the topological vector space of bulk forcing densities;
- the source-authorized domain of boundary currents;
- a continuous boundary derivative with a typed range or closure convention;
- the doubled forcing map and its pre-aggregation residual;
- the archimedean and atomic current attachments;
- a decision whether the cokernel is algebraic, topological, or derived;
- the complete boundary-flux condition used by the conditional seam theorem.

In infinite-dimensional topology, quotient by the algebraic range and quotient
by its closure are different objects. This formalization selects the algebraic
finite-dimensional cokernel only and does not silently answer that convention.

The abstraction generalized the exactness-versus-projection distinction and
specialized the cokernel type to the finite hostile model.

## Verification

From `research/buzzard/marici_formal/`:

```powershell
& "$env:USERPROFILE/.elan/bin/lake.exe" env lean MariciFormal/BoundaryCokernel.lean
& "$env:USERPROFILE/.elan/bin/lake.exe" build
```

The targeted command exited `0` without warnings or diagnostics. No site build
or Git command was run.

Changed owned files:

- `research/buzzard/marici_formal/MariciFormal/BoundaryCokernel.lean`
- `research/buzzard/marici_formal/MariciFormal.lean`
- `research/buzzard/boundary-current-cokernel.md`
