# Boundary rational-interface inventory

## Findings

The boundary artifacts retain three different interfaces:

1. `cosmology_rank26_p_normal_K_q_boundary_signature_census.json` records 60 degree-14 target coordinates, q-row counts, normalized signature hashes, and mark counts. It does not retain q-row indices or coefficients.
2. `cosmology_rank26_p_normal_K_q_boundary_correction_words_A12_to_A14.json` and its A14-to-A16 companion retain original-source `T/S_K` coefficients for selected vertical correction cells at one prime.
3. `cosmology_rank26_p_normal_K_q_boundary_all_composition.json` records 48 strict direct/composite coefficient matches at one prime, but not rational representatives.

Therefore the existing projections cannot reconstruct exact rational boundary q templates directly. Hash equality is not a coefficient interface, and single-prime correction words do not determine rational coefficients.

## Disposition

N5b1 is completed. N5b2 must not infer rational boundary words from the hashes.

The source-available route is to rebuild a full `T+S_K+Q` pivot DAG for every top-three-degree target, retain its active original-source closure, reconstruct those rows over the integers by four-prime CRT, and solve the resulting rectangular system over the rationals. This avoids importing finite-field pivot coefficients as rational data.

The bounded target counts are 54 at ambient degree 12, 60 at degree 14, and 66 at degree 16. A closure census is required before exhaustive exact solving.

## Evidence

- `research/voevodsky/results/cosmology_rank26_p_normal_K_q_boundary_signature_census.json`
- `research/voevodsky/results/cosmology_rank26_p_normal_K_q_boundary_correction_words_A12_to_A14.json`
- `research/voevodsky/results/cosmology_rank26_p_normal_K_q_boundary_correction_words_A14_to_A16.json`
- `research/voevodsky/results/cosmology_rank26_p_normal_K_q_boundary_all_composition.json`
