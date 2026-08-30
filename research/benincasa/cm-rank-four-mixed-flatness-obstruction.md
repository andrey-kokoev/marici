# Fiberwise rank-four closure fails the mixed-flatness gate

## Frozen frame

The four source roles are fixed before solving coefficients:

\[
(\mathsf n_1,\mathsf n_2,\mathsf n_3,\mathsf A_{\rm cyc}^{(2)}).
\]

For each base direction, every derivative class has a unique coordinate
column in this fiberwise frame. The resulting three \(4\times4\) matrices are
exported without choosing a quotient projector.

## Mixed-flatness calculation

Each matrix entry was reconstructed on 25-point coordinate slices. The
minimal total slice degrees are at most eleven, below the frozen bound of
sixteen, leaving at least eleven held-out values on every slice.

At \((s_1,s_2,s_3)=(5,7,11)\), all sixteen entries of each of

\[
F_{12},\qquad F_{13},\qquad F_{23}
\]

are nonzero modulo 32003. The same result holds modulo 65521. Reversing the
commutator sign does not repair any matrix: all sixteen entries remain nonzero
for all three pairs at both primes.

This result uses the repaired pole-order convention: labelled normal columns
contain bare \(L_i\), which the reducer localizes once, while derivative and
cyclic classes are supplied directly at their final pole order.

## Typing conclusion

Constant fiberwise rank and first-derivative closure do not define a flat
connection. The current matrix extractor reduces each fiber correctly, but it
does not provide the common exact-lift coherence needed to compare those
reductions under two base derivatives.

Therefore:

- the source-derived cyclic residue remains valid as a fiberwise
  second-fundamental-form direction;
- the sixteen-class rank-four closure remains a valid finite rank statement;
- a global rank-four subconnection is unproved;
- the extracted matrices must not be used for monodromy, support, or physical
  readout.

The missing constructor is a source-normalized primitive/exact-lift convention
shared by all four generators and all three base directions. Mixed flatness is
its acceptance gate.

## Artifacts

- `research/benincasa/checkers/check_cm_rank_four_connection_matrices.py`
- `research/benincasa/results/cm-rank-four-connection-matrices.json`
- `research/benincasa/checkers/check_cm_rank_four_mixed_flatness.py`
- `research/benincasa/results/cm-rank-four-mixed-flatness-p32003.json`
- `research/benincasa/results/cm-rank-four-mixed-flatness-p65521.json`
