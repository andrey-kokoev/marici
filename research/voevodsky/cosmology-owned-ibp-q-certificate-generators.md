# Owned IBP and q certificate generators

## Question

Can the remaining 976 source certificates be regenerated without mutating the ambiguous untracked generators?

## Result

`check_cosmology_owned_IBP_q_source_certificates.py` independently uses the shared column packet, raw relations, derivative-row adapter, source DAG, exact CRT lift, and rational solver. It emits separate owned outputs and leaves the untracked files unchanged.

Execution produced:

- 16 IBP certificates;
- 960 q certificates;
- zero nonzero reconstruction residuals;
- exact agreement with every corresponding descriptor, dimension, equation count, rank, denominator bound, and reconstruction flag in the immutable prior summaries.

Each certificate replayed against recomputed exact rows and target before serialization. Together with the 248 nonmarked-K certificates, all 1,224 seed absorptions now have durable algebraic source words.

## Claim boundary

The certificates establish exact algebraic contractions and generator-recompute replay. They do not provide geometric supports, a source differential, DNC filtration or specialization, or exceptional transport.

## Verification

- `research/voevodsky/check_cosmology_owned_IBP_q_source_certificates.py` — exit 0
- `research/voevodsky/results/cosmology_IBP_exact_source_certificates_a12.json` — 16
- `research/voevodsky/results/cosmology_q_exact_source_certificates_a12.json` — 960
- `research/voevodsky/results/cosmology_nonmarked_K_exact_seeds_a12.json` — 248
