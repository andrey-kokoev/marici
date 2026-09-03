# Three-site normalized residue-map audit

## Question

Do the frozen three-site artifacts define normalized factorization morphisms for the six compatible pairs of the physical `C6` link?

## Claim boundary

The local artifacts distinguish three residue notions:

1. the physical link records compatible divisor pairs and alternating source-order signs;
2. the flat logarithmic connection records residue matrices and Kohno relations on its arrangement;
3. specialized physical calculations compute residues only after a transverse coordinate, branch, or regulator chamber is chosen.

These objects do not automatically compose. A sign attached to an incidence edge is not a normalized residue map, and connection flatness does not identify its matrix residue with a physical factorization morphism.

One exact nearby-cycle calculation exists for the total-energy `g3` boundary. It uses `E=epsilon^2`; the two branches have opposite leading coefficients, and only `epsilon` times the residue is invariant and regular. This supplies a rank-one Kummer-normalized line for that boundary, not residue maps for the six `C6` pairs.

## Strongest falsification attempt

The iterated-cut regulator audit starts with `Res(q_G12)` and tracks the remaining `q_g31` and `q_g23` denominators. Positive regulator assignments realize four nonzero sign chambers. In units of `i*pi*delta`, their current coefficients are:

- `--`: `2`;
- `-+`: `0`;
- `+-`: `0`;
- `++`: `-2`.

The equal-regulator diagonal gives zero induced side and selects no boundary value. Thus the divisor pair and source-order sign do not determine a unique iterated physical residue. The graph-level contour-cone image is explicitly uncomputed, and interchange of specialization and regulator limits is not authorized.

This falsifies the conjecture that the existing `C6` incidence data alone define normalized sequential residue maps.

## First missing map

The first absent object is a source-derived contour-side map

\[
\sigma_{\Gamma}:\Gamma_{\rm phys}
\longrightarrow
\prod_{g}\{-,+\},
\]

or an equivalent relative-chain prescription assigning compatible boundary values to the physical contour for every divisor sequence. It must determine the induced chamber after the first residue and be coherent under the cyclic action.

Only after `sigma_Gamma` is supplied can one define normalized single and sequential residue morphisms, test the two orders, and compare them with Carrier restrictions. A contour-independent residue map would require a proof that the chamber-dependent currents agree; the frozen audit gives the opposite result.

## Acceptance test

For all six compatible pairs:

1. provide the physical relative chain and its boundary-side image;
2. compute both sequential residues with exact normalization;
3. verify the stated signed order relation;
4. rotate the data around the sourced `C6` action;
5. exhibit one incompatible pair whose iterated residue is undefined or vanishes for the declared reason;
6. show that regulator and specialization limits commute, or retain their exact commutator residual.

## Disposition

The ten divisors and their cyclic incidence are complete. Normalized factorization is blocked before Carrier comparison by missing contour-side authority. The next executable local branch is to test whether any frozen relative-chain artifact supplies `sigma_Gamma`; otherwise the owner handoff must request precisely that map.

## Evidence

- `research/benincasa/three-site-physical-residue-link.json`
- `research/benincasa/check_iterated_cut_regulator_chambers.rs`
- `research/benincasa/compute_g3_total_energy_nearby_residue.py`
- `research/benincasa/cm-total-energy-second-period-adapter.md`
