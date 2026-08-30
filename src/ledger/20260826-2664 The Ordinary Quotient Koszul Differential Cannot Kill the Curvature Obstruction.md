# 2664 — The Ordinary Quotient Koszul Differential Cannot Kill the Curvature Obstruction

## Frozen complex

For

\[
I=(5K_a,5K_b,5K_c,zK-1)\subset P
\]

and \(R=P/I\), retain the four source-labelled generators and their ordinary Koszul complex. Its differential is

\[
d(e_i)=g_i,
\qquad
d(e_i\wedge e_j)=g_i e_j-g_j e_i.
\]

## Exact quotient audit

At every replicated point and prime, reduction by the same Gröbner basis gives

\[
g_1=g_2=g_3=g_4=0\quad\text{in }R.
\]

Consequently every ordinary quotient Koszul differential vanishes. In exterior degrees \(0\) through \(4\), its ranks are

\[
(0,0,0,0).
\]

## Narrow result

The ordinary quotient Koszul complex cannot supply a boundary for Entry 2662's nonzero rank-four obstruction. The candidate coherence must retain variation of the labelled generators before quotient specialization: a differentiated Koszul, Spencer, Atiyah, or equivalent Gauss–Manin cell.

This does not prove that such a differentiated cell exists. It removes the raw Koszul differential from the candidate list and prevents a zero quotient differential from being reinterpreted as the required homotopy.

## Updated acceptance equation

Any surviving differentiated construction must produce a labelled homotopy \(H_c\) satisfying

\[
D H_c+H_cD
=
c_{12}F_{12}+c_{13}F_{13}+c_{23}F_{23},
\]

where \(D\) retains both the Koszul differential and its base variation before passing to \(R\).

## Artifacts

- `research/benincasa/marici-gm/src/bin/cm_normal_tower_rank.rs`
- `research/benincasa/checkers/check_cm_conormal_kodaira_spencer.py`
- `research/benincasa/results/cm-conormal-kodaira-spencer.json`

## Next falsifier

Construct the first differentiated Koszul differential directly from \(\partial_j g_i\), including the principal generator \(zK-1\), and test its mixed square against the full-rank obstruction. No free homotopy matrix may be introduced.
