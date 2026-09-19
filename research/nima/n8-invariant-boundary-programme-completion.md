# Exact completion of the invariant n=8 boundary programme

## Disposition

The finite source-side boundary problem is complete at n=8.  The result is an exact oriented boundary-chain theorem, not merely an associahedral incidence analogy:

- all 20 sourced eight-point NNMHV history cells are represented by positive colored single-column BCFW bridge charts;
- their 166 coordinate-facet incidences are covered;
- the 40 shared rank-seven positroid facets cancel pairwise as oriented logarithmic residues;
- the remaining 86 external incidences split into 80 rank-seven physical facets and 6 contracted loci which do not define target divisors;
- all 16 nonphysical target images cancel;
- the physical boundary canonical form is complete and has an independent second-positive-Z facetwise check.

## Exact orientation theorem

Orient each shared rank-seven facet by its incidence from the lower-index history.  For a coordinate residue, include deletion parity

\[
(-1)^{\alpha-1}
\]

and the exact logarithmic transition Jacobian.  Every shared facet then has relative sign `-1`.  Thus the complete internal source boundary vanishes coefficientwise.

The 40 witnesses divide into:

- 23 exact overlapping-seed dlog transitions;
- 17 exact cyclic colored-BCFW bridge transitions with independently checked seed-orientation anchors.

This is stronger than inferring cancellation from an unweighted cellular identity: each logarithmic residue and transition sign is explicitly computed.

## Physical and nonphysical pushforward

The complete oriented source chain leaves 86 external incidences.  Exact pushforward gives:

- 80 rank-seven physical facets;
- 6 contracted facets with no target divisor;
- cancellation of all 16 nonphysical images;
- exact physical inverse-fiber representatives for 11 orbit representatives;
- agreement between BCFW and polygon residue representatives;
- a second-positive-Z facetwise cross-check;
- saturation of the exceptional history-2 open inverse fiber.

## Reproducible entry point

Run:

```bash
python research/nima/checkers/check_n8_boundary_programme_manifest.py
```

The authoritative summary is:

- `research/nima/results/n8-boundary-programme-manifest.json`
- `research/nima/results/n8-complete-oriented-boundary-chain.json`
- `research/nima/results/n8-complete-cyclic-bcfw-bridge-atlas.json`
- `research/nima/results/n8-complete-external-pushforward.json`
- `research/nima/results/n8-physical-boundary-canonical-form-completion.json`

The manifest checks all pass, including `positive_atlas_covers_166`, `all_40_shared_cancel_directly`, `all_16_nonphysical_images_cancel`, `external_80_plus_6`, and `physical_boundary_completion`.

## Claim boundary

This proves the exact finite n=8 source boundary cancellation and physical pushforward for the declared sourced charts and deterministic lexicographic bridge convention.  It does not by itself prove an arbitrary-m theorem, a radiative/Bondi interpretation, or equivalence to unstated tie-breaking details in prose descriptions of BCFW bridge construction.
