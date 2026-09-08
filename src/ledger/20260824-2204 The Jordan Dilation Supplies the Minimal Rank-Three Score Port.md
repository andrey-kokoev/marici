---
authors:
  - marici.Benincasa
date: 2026-08-24
---
# 2204 — The Jordan Dilation Supplies the Minimal Rank-Three Score Port

## Edge-score space

Under Entry 2203's product law, write \(X_e\in\{0,1\}\) for the deletion bit
of edge \(e\). The centered scores are

\[
s_e=X_e-\frac23.
\]

Independence gives

\[
\operatorname{Cov}(s_e,s_f)
=\frac29\delta_{ef}.
\]

Hence the score space has rank three and transforms as the regular cyclic
permutation representation. It is exactly the minimal representation type
required by Entry 2200.

Tilting the three Bernoulli odds independently differentiates the signed
augmentation in the three labelled deletion-count directions. Consequently
the score port recovers Entry 2197's conormal response after restoring the
normalization derivative.

## Interpretation

The required preaggregation detector now has a canonical finite model:

\[
\boxed{
\text{three deletion bits}
+\text{ parity readout}
+\text{ three edge scores}.
}
\]

This confirms algebraic realizability and minimal rank. It does not prove
physical realization: no such sampler, ancilla, or parity observable has
been derived from the frozen Bunch–Davies/correlator source.

The next falsifier is therefore source provenance, not another linear-
algebra search: determine whether the signed weighted-polytope construction
is itself obtained from a coherent two-branch or auxiliary-system dilation
whose measured parity is \(\chi\).

## Evidence

- Entries 2197 and 2200–2203
- `research/benincasa/checkers/deletion_edge_score_port.rs`
