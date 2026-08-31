# Two-prime rational reconstruction of canonical seeds

## Test

Canonical coefficients were paired by typed source descriptor across \(\mathbb F_{32003}\) and \(\mathbb F_{32009}\). Rational candidates were searched under the declared symmetric bounds

\[
|n|\le 22000,
\qquad
1\le d\le 22000,
\]

and validated by reduction at both primes.

## Result

| K pole | coefficients | uniquely reconstructed | unresolved |
|---:|---:|---:|---:|
| 0 | 7 | 6 | 1 |
| 1 | 11 | 6 | 5 |

The reconstructed subset includes small fractions, but six coefficients have no candidate inside the declared uniqueness range. Expanding bounds would lose the simple two-prime uniqueness guarantee rather than supply evidence.

## Disposition

N5a is falsified as a complete two-prime bounded reconstruction. Characteristic-zero promotion is withheld.

Tree rescoring keeps N5 active through N5a2: add a third independently chosen admissible prime, extract the canonical seeds at ambient degree 14, and perform three-modulus rational reconstruction. The prime must be verified before execution; a third residue can distinguish large rational lifts from field-dependent pivot coefficients.

## Reproducibility

- Checker: `research/voevodsky/check_cosmology_rank26_p_normal_K_q_canonical_rational_reconstruction.py`
- Result: `research/voevodsky/results/cosmology_rank26_p_normal_K_q_canonical_rational_reconstruction.json`
