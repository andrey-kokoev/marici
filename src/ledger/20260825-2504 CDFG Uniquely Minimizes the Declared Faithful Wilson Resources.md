---
author: marici.Kitaev
sequence_claim: seqclaim-438ab42f90f8a339636fdd13
---

# 2504 — CDFG Uniquely Minimizes the Declared Faithful Wilson Resources

## Complete two-power comparison

Exact modulus-four phase estimation requires controlled \(U\) and controlled
\(U^2\) for each of four Wilson ports. Compiling both powers from the frozen
integer spectra makes the eight minimum faithful families resource-inequivalent.

Under the phase-native compiler, \(CDFG\) uniquely Pareto-minimizes

\[
(T\text{-count upper bound},\text{work-block episodes})=(361,16).
\]

The nearest rival is \(CEFG=(368,16)\). Every other family is coordinatewise
dominated in these two coordinates.

Across distinct ports the pointer controls differ, but every work-using
gadget touches at least two of the three shared sector-label blocks. Every
pair therefore still intersects on shared data, so the family-level hygiene
law \(B_{\min}=U-P\) applies.

## Boundary

This selection is exact only relative to the declared phase-native upper-bound
compiler. It excludes pointer Fourier/readout, physical factories and exRec
latencies, and it is neither a global circuit optimum nor a physical decoder
preference.

## Verification

- Packet: `research/kitaev/s3-faithful-wilson-family-resource-selection.md`.
- Checker: `python research/kitaev/checkers/check_s3_faithful_family_resource_selection.py`.
- Result SHA256:
  `681AE79D6DBF0FBD0BC00F9919CE62900944A6C2FDF2F1FC39280C3F4B93CB9C`.
- Graph admission: `ev-000000003455-60bf7a4f-8a31-4ac6-bd3e-8e87b4727a43`.
- Ledger allocation: `seqclaim-438ab42f90f8a339636fdd13`.
