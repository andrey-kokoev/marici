# Baryonic-matter bridge — old identification withdrawn

## Current disposition — 7 October 2026

The natural four-point S4 representation is 1+3, not 1+sign+2. This was already
settled in `weak-doublet-singlet-weight-and-s4-representation-audit.md`, which
also constructs the valid witness-S3 doublet and explicit conditional gauge
operators. Its symmetry-only charge/kinetic underdetermination remains a closure.

The new missing comparison is now constructed in `s4-gram-action-comparison.md`:

- The ACTUAL old 24-by-24 permutation-operator Gram has eigenvalues 24, 8 and 0
  with multiplicities 1, 9 and 14. It is not a nondegenerate regular Gram.
- Its rank-ten operator image carries 1+3+3+3 under left translation, but
  1+1+2+3+3' under conjugation. The latter doublet is an OPERATOR sector.
- The completed witness weak/charge operators lift explicitly through that
  full Gram. Its orthogonal operator projection also recovers the earlier
  pinched witness charge.

These are compatible finite constructions, not a derivation of physical matter,
SU(3)xSU(2)xU(1), generations, masses or CKM mixing. Neither equality of dimensions
nor switching group actions supplies the missing matter map. No blanket
absence-of-doublets conclusion follows.

The old particle-content and “all layers confirmed” tables are withdrawn.
Original text and code are preserved in `quarantine/20261007-s4-evidence/`.
The live `checkers/check_baryonic_matter.py` now reports only checked finite
representation content. Verification of the comparison uses
`checkers/check_s4_gram_action_comparison.py` and its result JSON.
