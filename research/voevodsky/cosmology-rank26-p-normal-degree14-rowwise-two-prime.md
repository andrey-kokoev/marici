# Degree-14 rowwise p-normal reduction certificate

## Result

At ambient degree 14, every original p-normal derivative row reduces to zero against a fixed normalized basis for `S+T`, over both \(\mathbb F_{32003}\) and \(\mathbb F_{32009}\).

The fixed basis is built only from:

- `S`: special exact relation rows;
- `T`: p-tangent derivative rows.

No `nx` or `ny` derivative row is adjoined while testing containment.

| prime | rank(S) | rank(S+T) | nx zero remainders | ny zero remainders | nonzero remainders |
|---:|---:|---:|---:|---:|---:|
| 32003 | 11490 | 11603 | 29904 | 29904 | 0 |
| 32009 | 11490 | 11603 | 29904 | 29904 | 0 |

Thus 59,808 normal derivative rows per prime were reduced against the fixed `S+T` basis, with no nonzero remainder.

Normalized basis digests:

- \(\mathbb F_{32003}\): `e3a422e83cde7aafe1b5c041d5ac7b52cad0955615c7142fb86b3d96abe1007a`
- \(\mathbb F_{32009}\): `ddc25863c33ec34b3dd68c36a703e2f63264eb988b60e2389c788df481573e2a`

## Meaning

This is stronger than comparing final ranks: it checks containment row-by-row without allowing the tested normal rows to enlarge the reducer. It supplies a finite algorithmic reduction certificate for the canonical stored source-word ambient degree 14.

It still does not retain reduction coefficients, construct a uniform chain homotopy, prove ambient-degree induction, construct a horn map, or construct a Bockstein or period.

## Reproducibility

- Row checker: `research/voevodsky/check_cosmology_rank26_p_normal_rowwise_reduction_certificate.py`
- Aggregate checker: `research/voevodsky/check_cosmology_rank26_p_normal_degree14_rowwise_two_prime.py`
- Aggregate result: `research/voevodsky/results/cosmology_rank26_p_normal_degree14_rowwise_two_prime.json`
