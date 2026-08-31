# Rank-26 p-normal absorption is not tautological quotienting

## Question

Is the observed disappearance of the p-normal derivative image merely an artifact of quotienting the two normal choices against each other?

## Claim boundary

This packet proves a finite linear-algebra typing statement for the tested degrees and primes. It does not construct a uniform chain homotopy or induction in ambient degree, a horn map, a relative Bockstein, or a physical period.

## Formal distinction

For every raw labelled relation row, the checked derivative identity is

\[
D_{n_x}(r)-D_{n_y}(r)=D_t(r),
\qquad t=n_x-n_y.
\]

Let `S` be the special exact image and `T` the span of the p-tangent derivatives \(D_t(r)\).

Quotienting by `T` has only the formal consequence

\[
[D_{n_x}(r)]=[D_{n_y}(r)].
\]

It does **not** formally imply that this common class is zero. The forbidden inference is

\[
D_{n_x}-D_{n_y}\in T
\quad\not\Rightarrow\quad
D_{n_x}\in S+T.
\]

The zero common image is therefore an additional rank fact, not a tautology.

## Computed evidence

At every tested degree \(8,10,12,14,16,18\), over both \(\mathbb F_{32003}\) and \(\mathbb F_{32009}\):

1. `T/S` is nonzero;
2. quotienting by `T` identifies the two normal choices;
3. separate extension-rank calculations show both normal derivative spans add zero over `S+T`.

| degree | rank(T/S) | nx over S+T | ny over S+T |
|---:|---:|---:|---:|
| 8 | 97 | 0 | 0 |
| 10 | 101 | 0 | 0 |
| 12 | 107 | 0 | 0 |
| 14 | 113 | 0 | 0 |
| 16 | 119 | 0 | 0 |
| 18 | 125 | 0 | 0 |

Thus `T` enforces normal-choice independence, while vanishing of the common normal image is a distinct two-prime computation.

## Consequence

The finite absorption result is not manufactured by a circular quotient. Nonetheless, it remains finite evidence: no uniform reduction certificate or ambient-degree induction has yet been constructed.

No surviving sourced line exists in these tests, so no comparison with the formal \(\tau_p\) horn is available.

## Reproducibility

- Checker: `research/voevodsky/check_cosmology_rank26_p_normal_absorption_not_tautological.py`
- Result: `research/voevodsky/results/cosmology_rank26_p_normal_absorption_not_tautological.json`
- Command: `python research/voevodsky/check_cosmology_rank26_p_normal_absorption_not_tautological.py`
