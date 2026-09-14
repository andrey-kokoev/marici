# v157: L2 derived torsion-cell census

The true relation-lattice Smith factors are now converted into an explicit
finite derived-saturation cell census.

At D12,16,20,24,28 the numbers of nonunit invariant factors are respectively
`17,34,53,76,103`. Their 2-primary lengths are `18,38,61,82,117`; their
3-primary lengths are `9,13,17,25,25`. Every factor is 2/3-primary.

A finite-cutoff integral saturation can therefore be modeled by one two-term
derived cell for each nonunit Smith factor, with differential multiplication by
that factor. The distinguished transition removes one `Z/2` cell at every
cutoff.

This gives concrete cell counts rather than a generic statement that torsion is
present. The remaining global problem is to construct compatibility maps among
these cutoff cell complexes; the nonmonotone invariant-factor distributions
mean that naive inclusion of cell lists is not justified.

Evidence is `results/L2-derived-torsion-cell-census.json` from
`checkers/check_L2_derived_torsion_cell_census.py`.
`rzk/185-l2-derived-torsion-cell-census.rzk.md` passes all eight declarations
without assumptions.
