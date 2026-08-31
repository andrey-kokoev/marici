# Active marked-wall derivatives are primitive singleton columns

## Result

At ambient degree 14, every nonzero p-normal derivative of a marked-\(q\) multiplication relation is a unit singleton row: it has support on exactly one labelled presentation column with coefficient one.

| direction | active rows | distinct singleton columns | multiplicity range |
|---|---:|---:|---:|
| `nx` | 10,080 | 7,560 | 1–2 |
| `ny` | 10,080 | 7,560 | 1–2 |
| `nx-ny` | 20,160 | 9,450 | — |

Column-set relations:

- the `nx` and `ny` singleton sets intersect in 5,670 columns;
- their union contains 9,450 columns;
- the p-tangent singleton set is exactly that union.

## Meaning

The active marked-wall derivative is not a complicated Laurent combination. Differentiating

\[
e-q_i e_i^+=0
\]

along an active unit normal differentiates only the constant parameter term of \(q_i\), producing a primitive labelled basis column.

Combined with the two-prime rowwise certificate, this means the fixed `S+T` span contains each of the 7,560 `nx` columns and each of the 7,560 `ny` columns individually. Their overlap explains why 20,160 tangent rows occupy only 9,450 distinct columns.

This is a partial algebraic explanation of marked-wall absorption. It does not retain explicit `S+T` expansion coefficients and does not explain the IBP or \(K\)-multiplication families.

## Reproducibility

- Checker: `research/voevodsky/check_cosmology_rank26_p_normal_marked_q_singletons.py`
- Result: `research/voevodsky/results/cosmology_rank26_p_normal_marked_q_singletons.json`
