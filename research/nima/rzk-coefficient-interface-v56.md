# v56: conductor-symbol lifting and symmetry

The standalone Branch A replay passed 315,452 assertions. At regulator-normal
grade three, the complete endpoint/Q frame has a rank-134 lattice of closed
first symbols, a saturated rank-74 quadratic obstruction lattice, and a rank-60
lattice of full lifts. Compatibility is necessary and sufficient: every
compatible symbol has a unique full coefficient-cycle lift because no
higher-conductor degree-three correction exists.

`rzk/74-conductor-symbol-lifting-symmetry.rzk.md` records this dichotomy, the
16 visible plus 9 primary-homotopy equivariant directions, and the index-two
defect for invariant integral preimages. Its fresh headless Rzk check passed;
see `results/74-conductor-symbol-lifting-symmetry.typecheck.json`.

The scalar six-term alternating conormal symbol still does not choose a point in
the 134-dimensional chain-symbol lattice. Consequently these exact lifting and
symmetry tests do not select the physical conductor--Morse class or identify the
index-two equivariance defect with `Delta_J`.
