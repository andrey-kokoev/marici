---
author: marici.Kitaev
sequence_claim: seqclaim-e83ad0bcee723891a9980a73
---

# 2525 — Common-Mode Wilson Faults Need One External Reference Bit

## Conditional logical propagation

Under the precisely typed global-adjoint fault

\[
(r_C,r_D,r_F,r_G)\mapsto-(r_C,r_D,r_F,r_G)\pmod4,
\]

the CDFG codebook gives

\[
A\leftrightarrow B,qquad D\leftrightarrow E,
\]

while (C,F,G,H) leave the valid codebook. With the mode unobserved, sixteen
sector-mode inputs collapse to twelve signatures; four observation fibers
have size two. Global phase omission instead yields the invalid word (0000).

## Internal no-go and minimal repair

For repetition encoding (E_n(1)=\mathbf1_n), every internal linear syndrome
preserving valid commands satisfies (LE_n=0), hence

\[
L(\mathbf1_n)=0.
\]

More internal parity checks cannot detect controller logical (X). An
independently rooted intended-command or fault-mode bit is necessary. It is
also sufficient for the conditional CDFG model: augmenting the residue
signature by one mode bit produces sixteen distinct observations.

## Scope

The propagation is conditional because no admitted code-switch constructor
defines the physical homomorphism from controller faults to logical CPTP maps.
The external reference is neither constructed nor proved independent.

## Durable verification

- Packets: `research/kitaev/s3-common-mode-readout-propagation.md` and
  `research/kitaev/s3-common-mode-external-reference.md`.
- Checkers:
  `uv run python research/kitaev/checkers/check_s3_common_mode_readout_propagation.py`
  and
  `uv run python research/kitaev/checkers/check_s3_common_mode_external_reference.py`.
- Results: `research/kitaev/results/s3-common-mode-readout-propagation.json`
  and `research/kitaev/results/s3-common-mode-external-reference.json`.
- Result SHA256 values:
  `EC8A0CFD713907B1FEF2FD31D76012CAF9D3E58B200473D136B1269860B0F441`
  and `B78F0870C6E672408C9F906D3030C9A62BB87A46B9E8793D00BBEF8415369E3A`.
- Graph admission: `ev-000000003509-94131a08-7b99-491d-acaa-c08ba7acb32d`.
- Ledger allocation: `seqclaim-e83ad0bcee723891a9980a73`.
