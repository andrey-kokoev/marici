# Residue incidence versus amplitude normalization

## Problem

The selected research-tree root asks for the first typed descent from cosmological wavefunction data to scattering amplitudes. Existing work constructs a labelled divisor/residue incidence category but not a normalized amplitude map.

## Bold conjecture

Labelled residue incidence and coherent sequential residues determine the normalized lower-graph scattering amplitude.

## Named rivals

1. incidence alone fixes the amplitude;
2. incidence is invariant under common coefficient rescaling, so an independent source normalization is required;
3. the sewn physical contour fixes normalization without a total-energy residue declaration.

## Risky consequences

Any two realizations with identical labelled divisors, compatibility, and residue-order coherence must have identical lower-graph coefficients.

## Strongest falsification attempt and residual

Execution `structured_command_execution:e_21672_1788307988643428900_1` keeps the labelled divisor incidence and ordered codimension-two relation fixed while applying distinct nonzero common rescalings to all residue coefficients. Incidence is unchanged and the proposed amplitude coefficients differ. Therefore the incidence category cannot determine numerical normalization. The bold conjecture is falsified.

This matches the source boundary in `amplitude-cosmology-factorization-first-interface.md`: the first common architecture is labelled residue incidence, while the source normalization relating the site-energy integral to the flat-space wavefunction is additional data.

## Disposition and residual conjecture

The minimal next arrow is a source-normalized total-energy residue map

\[
\operatorname{Res}_{E_{\rm tot}=0}^{\rm src}:\Psi_G\longrightarrow A_G,
\]

with declared domain, codomain, pole order, coefficient, sign/orientation convention, and one low-point evaluation. The residual conjecture is that the frozen three-site source supplies this map before any Carrier realization. Equal pole patterns or sewn contour existence do not substitute for it.

The next test is to locate and freeze the exact three-site total-energy-pole formula and compare its coefficient against the independently normalized lower-graph amplitude.

## Evidence

- `research/nima/checkers/check_residue_incidence_normalization_no_go.py`
- `research/nima/amplitude-cosmology-factorization-first-interface.md`
- `research/nima/source-sewn-contour-factorization-revision.md`
