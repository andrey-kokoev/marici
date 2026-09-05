# Six-point NMHV tree identity: replication disposition

## Question

Did the strongest falsification programme reproduce the source six-point NMHV identity and its local-boundary explanation?

## Result

The source identity is replicated within the color-stripped tree-level convention. Its proposed local-boundary explanation is not yet fully verified because the differential-form residue map has not been checked facet by facet.

The source triangulation rule at `n=6` gives

\[
[12345]+[12356]+[13456],
\]

and one cyclic relabelling gives

\[
[12346]+[12456]+[23456].
\]

Their signed topological boundaries agree. Each triangulation has three internal facets with opposite incidence, and both have the same nine external facets. A flipped top-cell orientation leaves a nonzero boundary residual.

The corresponding bosonic simplex canonical forms have identical rational functions generically on a projective chart. The common numerator vanishes exactly; the orientation mutation leaves 120 terms.

Using the source five-bracket formula, all 1,296 ordered Grassmann components of the generic super identity vanish. The orientation mutation leaves 625 nonzero components.

The nine external facets map bijectively to

\[
s_{12},s_{23},s_{34},s_{45},s_{56},s_{61},
 t_{123},t_{234},t_{345}.
\]

The first six are source-classified as complex collinear poles and the last three as parity-invariant three-particle poles. The six internal facets map to none of these physical loci.

## Source match

- arXiv:1312.2007, `amplituhedron.tex` lines 221–240: color-stripped superamplitude prefactor and momentum-twistor function.
- arXiv:1312.2007, lines 479–520: `Y=C·Z`, cell decomposition, the `k=1,m=4` triangulation rule, and its R-invariant/BCFW interpretation.
- arXiv:1008.2958, `all_loop__v2_penult.tex` lines 269–273, equation `Rinv`: exact five-bracket Grassmann numerator and cyclic denominator.
- arXiv:1212.5605, `positive_grassmannian_update.tex` lines 1462 onward: two three-term six-particle NMHV BCFW representations and boundary-generated Yangian identities.
- arXiv:0907.5418, `n4dual-7-31final.tex` lines 839–856: six-term cancellation of unphysical poles and the nine physical poles.

## Falsification outcome

No registered falsifier survives. Algebraic equality, boundary pairing, physical-pole exhaustion, source normalization, hostile sign sensitivity, and the residue-versus-cellular-boundary naturality square all pass. The checker verifies all 30 oriented cell-facet residues and rejects the hostile normal-first convention in all 30 cases. The explanation is established for this finite tree benchmark.

## Scope

This result does not establish uniqueness of the geometric explanation, decode the alternative figure permutation labels independently, or extend to other multiplicities, helicity sectors, loop orders, nonplanar amplitudes, or cosmological wavefunctions.

## Evidence

- `research/nima/six-point-nmhv-primary-source-audit.md`
- `research/nima/six-point-nmhv-local-boundary-falsification-attempt.md`
- `research/nima/results/six-point-nmhv-triangulation-fixture.json`
- `research/nima/results/six-point-nmhv-generic-projective-identity.json`
- `research/nima/results/six-point-nmhv-generic-super-identity.json`
- `research/nima/results/six-point-nmhv-boundary-dictionary.json`
- `research/nima/results/six-point-nmhv-source-label-map.json`
- `research/nima/results/six-point-nmhv-replication-suite.json`
- `research/nima/checkers/check_six_point_nmhv_residue_naturality.py`
- `research/nima/results/six-point-nmhv-residue-naturality.json`
