# v50: genuine union recollement

**Framing update:** [`rzk-coefficient-interface-v51.md`](rzk-coefficient-interface-v51.md)
distinguishes weight-zero coherent primary rigidity from first-conductor
endpoint/Q-zero deformations.

`rzk/65-union-recollement-obstruction-persistence.rzk.md` separates three
coefficient constructions that must not be identified: the finite union-dual
layer, the colimit over all support thickenings, and the genuine open
complement. Their closed-fibre and orthogonality properties have distinct
constructors.

The six irreducible branch-normal components of the primary Q obstruction are
represented individually. Each carries an explicit type-level witness that it
has support outside the union of the three pair intersections. The open
primary and secondary obstruction families reuse, rather than weaken, the
seven generators from modules 45 and 48. Their statuses record that the generic
unit still has no lift, admissible lift spaces remain the original discrete
torsors, and the coefficient-naturality extension remains nonsplit.

The module also distinguishes first-pole residues from higher normal poles:
normal multiplication kills a first-pole layer but lowers a higher pole to a
still-retained layer. This blocks replacement of genuine local cohomology by
the finite first-normal fibre.

A fresh 76-file transitive closure passed in 37.93 seconds. Evidence:
`results/65-union-recollement-obstruction-persistence.typecheck.json`.

Scope: the arbitrary-thickness 28-column transition maps, localization
incidence complex, exact ideal saturations, open hypercohomology comparison,
and Ext restriction injectivity remain certificate-backed. No physical
identification of this open with deformation time or construction of the
normalization-sheet source is asserted.
