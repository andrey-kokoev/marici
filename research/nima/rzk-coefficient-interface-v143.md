# v143: L2 integral denominator lattice

A fresh exact-rational reconstruction of the actual labelled soft-axis formulas
was run through D28 (6,960 columns). Unlike the earlier Cartier Smith checker,
this uses `L2-=a-u/2`, `L2+=a+u/2`, the p/q formulas, and the square-zero u
relation directly.

Every coefficient denominator is 1 or 2. All u0 coefficients are integral; all
half-integrality is confined to the u1 sector. The counts are 16,374 integral
u0 terms, 50,688 integral u1 terms, and 3,390 half-integral u1 terms.

Therefore an explicit candidate integral lattice is available: retain the
original u0 lattice and use `u/2` as the square-zero u-sector generator. Every
tested labelled column is integral in this lattice. This repairs the
presentation provenance enough to formulate the true integral L2 matrix.

The Bockstein relation/kernel Smith computation in that lattice remains open,
and the cutoff audit is not yet an all-degree denominator theorem.

Evidence is `results/L2-integral-denominator-lattice.json` from
`checkers/check_L2_integral_denominator_lattice.py`.
`rzk/171-l2-integral-denominator-lattice.rzk.md` passes all six declarations
without assumptions.
