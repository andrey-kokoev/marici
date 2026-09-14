# v185: local qg2 conductor connecting cell is source-derived

The target-derived node factor from v184 is not produced by either the original
or exceptional normal Jacobian; both are -1, and the displayed exceptional
wall equations have conormal rank one. That direct normalization route is
falsified generically.

A different source-derived grade-minus-one cell is nevertheless available from
the qg2 subleading wall form. Its endpoint and conductor residues are both
`1/(64 p^4 (kappa-1))`. The residue at infinity is their negative sum. Dividing
by the collision Euler class `kappa-1`, as forced by localized
self-intersection, gives

`-1/(32 p^4 (kappa-1)^2)`.

The normalized wall kernel is `16 p^4 s^2`, so its multiplicity-two pullback
has trivial Kummer character; the opposite character would make the connecting
coefficient vanish. This constructs the local conductor connecting cell with
its sign and inverse-Euler orientation.

It is not the fitted coefficient needed to cancel qg1 directly. The remaining
physical object is the relative cut chain/nearby-cycle comparison transporting
this local conductor cell into the ambient physical wall complex and then to
the selected L2 class v.

`rzk/213-qg2-conductor-connecting-cell.rzk.md` passes all eight declarations
without assumptions.
