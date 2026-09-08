# v45: central Rees Gysin, pair orbit, and beta-zero difference

**Spatial gate update:** [`rzk-coefficient-interface-v46.md`](rzk-coefficient-interface-v46.md)
records that the natural endpoint-complete factorized carrier has a null generic
morphism even after the Gysin tensor, and that the smaller generic projection
fails the mixed-triangle chain equation.

Three modules integrate the 2026-09-07 support updates.

`rzk/57-central-rees-gysin-channel.rzk.md` separates the zero central value of
an ordinary return from the primitive degree-three determinant-valued Gysin
channel. It records unit short/generic reverse pairings and a distinct
excess-labelled Gysin unit; none is typed as an ordinary degree-one excess
homology image.

`rzk/58-q-three-pair-supported-section.rzk.md` records the rotated-pair orbit
with remaining Rees counts `6,4,2,0`. At the full three-pair PC support it
constructs an actual direct-sum target, strict Q inclusion and projection, and
checks `projection section = identity`, including the native four-term Q cycle.
This target-side section retains its codimension-six framing externally.

`rzk/59-beta-zero-supported-difference.rzk.md` represents the endpoint-detected
map difference over beta and X35. Separate homotopy states make every positive
beta or X35 multiple a boundary. An origin detector is one on the unmultiplied
class and zero on every boundary, proving its primitive nonboundary status.
The type-level classification keeps apart the beta-torsion primary, X35-only
`Z_beta`, and `(beta,X35)`-torsion map difference.

Fresh transitive checks passed for all three modules (closures of 7, 75, and 73
files respectively). Evidence is in `results/57-*.typecheck.json`,
`results/58-*.typecheck.json`, and `results/59-*.typecheck.json`.

Scope: the all-polynomial ordinary-return annihilator, complete Cech residue
matrix, pair-supported 25-generator presentation, exact full-ring
annihilators, endpoint coefficients, and beta-adic 430-state identities remain
certificate-backed. The physical source still has no admitted comparison into
the triple-supported PC target, and no endpoint-fixed physical Delta_J or
reflection parity follows.
