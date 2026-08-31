# No currently materialized candidate is a sourced surviving p-normal line

## Candidate audit

- Abstract tau_p: no source object or chain map; importing it would be circular.
- Retained c-kernel: sourced, but not p-normal; its covector and dp have rank 2.
- Rank-26 nx/ny common normal image: sourced and p-normal, but absorbed modulo `S+T`; the marked K residual now has an unbounded exact absorption class.
- Total-energy Rees class: belongs to a different normal sector; total energy is nonzero at the p-normal test point.
- Gamma-normal Bockstein vector: belongs to a different normal sector; only its relation-derivative algorithm transfers.

No candidate is both source-admissible, p-normal, and surviving.

## Disposition

P6a1 is completed and the present candidate domain is exhausted. P6a remains blocked rather than globally falsified: a new relative-face source object could still produce a line outside the absorbed domain.

The missing datum is a resolved/Rees exceptional object, logarithmic Cech-de Rham cone cell, or Cayley-Menger/relative-face cone with a chain map whose primitive integral differential column is `(1,1)` in the required rows. No such object is currently materialized.

Consequently P6b remains blocked. The unbounded marked-K theorem strengthens the obstruction: it supplies canonical absorption classes, not the surviving class required for a horn or relative Bockstein.

## Reproducibility

- Checker: `research/voevodsky/check_cosmology_rank26_p_normal_surviving_line_candidate_gate.py`
- Result: `research/voevodsky/results/cosmology_rank26_p_normal_surviving_line_candidate_gate.json`
