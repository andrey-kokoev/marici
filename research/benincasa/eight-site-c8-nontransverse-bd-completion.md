# C8 nontransverse Bunch--Davies specialization: final corrected audit

## Objective disposition

The requested source-derived chain has been constructed through its canonical algebraic sewing.  The final affine Betti-selection gate is reopened by primary-source Eq. (4.19):

\[
\text{canonical form}
\to
\text{labelled transverse Leray current}
\to
\text{rank-three excess specialization}
\to
\text{OS degree-four sewing}
\to
\text{projective fold line}.
\]

Primary-source Eq. (4.19) supplies a negative-imaginary external energy tube, correcting the earlier packet-only audit.  Its exact fold-normal image gives the final physical split: eight labelled B8 occurrences are selected, 168 A-family occurrences are unselected because the positive cone crosses both chambers, and 112 occurrences are dormant because their source coefficient vanishes.

## Requirement-by-requirement evidence

| Requirement | Evidence | Disposition |
|---|---|---|
| Complete C8 numerator and ordered contour without fitting | `eight_site_canonical_contour_packet.py`, `eight_site_canonical_regular_triangulation.py`, `eight_site_canonical_numerator_certificate.py`; Entry 1926 | Exact 65-facet denominator and degree-49 numerator as a certified 255-simplex arithmetic circuit; 1016 internal residues cancel and 2048 boundary ridges cover all facets. |
| Nontransverse relative current over 288 occurrences | `eight_site_rank4_excess_leray_complex.py`; Entry 1928 | Exact derived pullback of a transverse seven-torus with rank-three Koszul excess, chain ranks \((1,3,3,1)\). |
| Regulator, elimination, coordinate, and resolution independence | `eight_site_rank4_excess_independence.py`, `eight_site_canonical_triangulation_independence.py` | 4176 circuit bases, 4704 elimination charts, 288 routing charts, the full positive regulator cone, and two disjoint certified triangulations give the same typed object/projective form. |
| Betti/de Rham comparison compatible with Entry 1924 | `eight_site_rank4_betti_derham_comparison.py` | Normalized torus periods are identity chain maps; regulator and private-circuit coboundaries vanish in the complete OS quotient. |
| Two cyclic components and orientation/deck data | `eight_site_canonical_cyclic_orientation.py`, `eight_site_rank4_os_fold_sewing.py`, `eight_site_rank4_fold_betti_selection.py` | Components remain \(144+144\), transverse signs are \((-8,+8)\), every cyclic projective transport scalar is \(+1\), and the fold deck character on the odd line is \(-1\). |
| Sewn fold pairing and cyclic assembly | `eight_site_rank4_face_fold_pairing.py`, `eight_site_rank4_os_fold_sewing.py`; Entry 1930 | Generic source coefficients split \(22+14\) over 36 orbits; OS sewing gives \(176+112\) over 288 labels, balanced \(88+88\) nonzero across components. |
| Physical classification | `eight_site_rank4_source_regulator_fold_chambers.py`; Entries 1932--1933 | The A cone crosses opposite chambers (168 unselected); the B8 cone stays in one open quadrant (8 selected); 112 are dormant by routing invisibility. |
| Narrow theorem, artifacts, graph relations, next falsifier | Entry 1930; graph event `ev-000000002347-6bd8aa40-2d6b-4e97-91ef-b3115af5eecd` | Recorded with allocator claim `seqclaim-1d49bf235de87c808ee48dac`; next falsifier is a primary-source derivation of an external continuation intertwining deck and cyclic data. |

## Prohibited-shortcut audit

- No spurious-boundary theorem was imported.
- No regulator chamber or hierarchy was selected; the three base-normal labels remain symbolic.
- No residue weights were fitted.
- Betti activation was not inferred from OS closure.
- No carrier cells or support summands were added.
- The absence of an affine scalar is recorded as lift dependence, not repaired by choosing a vanishing path.

The regulator image is complete because \((a,b,c,d,z)\) are the retained Eq. (4.19) edge-energy variables, while \((k,l)\) are fixed routing-Gram shape parameters.  No additional regulator Jacobian is required at this fixed-shape fold test.

## Fresh verification

On 2026-08-22/23 all nine principal checkers were rerun from the current worktree with exact arithmetic.  All assertions passed.  The only environmental correction was supplying the declared NumPy/SciPy dependencies for the regular-triangulation checkers.
