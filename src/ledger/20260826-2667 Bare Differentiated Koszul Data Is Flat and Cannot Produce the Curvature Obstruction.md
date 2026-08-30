# 2667 — Bare Differentiated Koszul Data Is Flat and Cannot Produce the Curvature Obstruction

## Frozen candidate

Differentiate the four exact generators

\[
g=(5K_a,5K_b,5K_c,zK-1)
\]

along the three labelled momentum-square directions. On the Koszul complex, the first variation is contraction by the Kodaira–Spencer section \(\kappa_j=\partial_jg\).

The candidate mixed coherence has two source-defined pieces:

1. the antisymmetrized mixed derivative \(\partial_i\partial_jg-\partial_j\partial_i g\);
2. the graded commutator of the two contraction operators.

## Exact result

Across all replicated points and primes,

\[
\partial_i\partial_jK-\partial_j\partial_iK=0
\]

for every labelled pair. The induced generator derivatives therefore commute. Independently, contractions on an exterior algebra satisfy

\[
\iota_{\kappa_i}\iota_{\kappa_j}
+
\iota_{\kappa_j}\iota_{\kappa_i}=0.
\]

Hence the bare differentiated Koszul mixed curvature vanishes.

## Narrow result

Neither the ordinary quotient Koszul differential nor its bare first base variation can produce Entry 2662's nonzero rank-four obstruction. The obstruction must involve the primitive/reduction connection used to identify varying quotient representatives—an Atiyah, Spencer-with-splitting, or equivalent Gauss–Manin coherence term.

This is a type restriction, not authorization to choose a primitive splitting. Any such connection must be derived from the frozen reduction machinery, and its dependence on primitive lifts must cancel at the level of the obstruction class.

## Artifacts

- `research/benincasa/marici-gm/src/bin/cm_normal_tower_rank.rs`
- `research/benincasa/checkers/check_cm_conormal_kodaira_spencer.py`
- `research/benincasa/results/cm-conormal-kodaira-spencer.json`

## Next falsifier

Extract the connection induced by the tracked Gröbner reduction on the full labelled Koszul presentation. Compute its Atiyah commutator with the Koszul differential and test whether the relation contraction equals Entry 2662's obstruction independently of primitive representatives.
