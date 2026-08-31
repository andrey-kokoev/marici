# Ambient transport of marked-q K absorption

## Result

At ambient degrees 12 and 16 over \(\mathbb F_{32003}\), every `nx` K-derivative row is absorbed by `T + S_K + S_q`.

The canonical lifts retain the same sizes as at degree 14:

- 7 special `g1` q rows at K pole 0;
- 11 special `g1` q rows at K pole 1.

Their monomial-shift domains follow one exact cutoff law:

| ambient degree \(A\) | interior shifts per pole | interior maximum degree | boundary shifts per pole | boundary degrees |
|---:|---:|---:|---:|---|
| 12 | 21 | 5 | 24 | 6, 7, 8 |
| 14 | 36 | 7 | 30 | 8, 9, 10 |
| 16 | 55 | 9 | 36 | 10, 11, 12 |

Thus canonical shift closure holds exactly through degree \(A-7\). The only unavailable direct shifts occupy the top three retained K-monomial degrees \(A-6,A-5,A-4\). Every defined shifted identity reconstructs modulo `T + S_K`.

## Disposition

N3b4b and N3b4 are completed at the tested finite-degree level. The special marked-q mechanism, residual stratum, canonical lift sizes, and three-degree boundary law all transport across ambient degrees 12, 14, and 16.

This is not an unbounded theorem. The next active branch N3b5 is to formulate and test a source-natural ambient induction: interior multiplication transports the 7/11-row lifts, while a separately typed boundary operator supplies the top three degrees. Such an induction must avoid pivot-order coefficients and must state its cutoff transition maps explicitly.

## Reproducibility

- Checker: `research/voevodsky/check_cosmology_rank26_p_normal_K_q_ambient_transport.py`
- Results:
  - `research/voevodsky/results/cosmology_rank26_p_normal_K_q_ambient_a12.json`
  - `research/voevodsky/results/cosmology_rank26_p_normal_K_q_ambient_a16.json`
