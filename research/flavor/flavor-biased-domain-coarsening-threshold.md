# Biased domain-coarsening threshold (WP284)

## Local source dynamics

Replace WP283's external majority vote by a finite periodic domain chain with

\[
E=-J\sum_i s_is_{i+1}-h\sum_i s_i,
\qquad s_i\in\{-1,+1\},
\qquad J,h>0.
\]

At zero temperature, admit only single-spin moves that lower energy. Flipping a
minus spin with two minus neighbors costs

\[
\Delta E=4J-2h.
\]

A positive bias does not automatically coarsen the wrong vacuum. For
\(0<h<2J\), the all-minus configuration is a strict local minimum. At
\(h=2J\), its first flip is neutral.

## Deterministic finite-ring threshold

When \(h>2J\), flipping any minus spin lowers energy, even inside the uniform
wrong vacuum. Flipping any plus spin raises energy. Repeated lowering moves
therefore convert every finite configuration to the unique absorbing all-plus
vacuum in at most one flip per initial minus spin.

The exact five-site audit gives:

- \(J=1,h=1\): the globally disfavored all-minus vacuum remains trapped;
- \(J=1,h=2\): the wrong vacuum has a neutral escape move;
- \(J=1,h=3\): all-plus is the unique local minimum.

## Classification

Biased local domain dynamics is a conditional deterministic finite-ring branch
selector only when \(h>2J\). This replaces formal majority aggregation by an
executable local operation in the declared model, but its physical authority
depends on deriving the bias-to-wall ratio, field dynamics, geometry, thermal
activation, expansion, defects, runtime, and stabilization.

Run `uv run --with sympy python
research/flavor/checkers/wp284_biased_domain_coarsening_threshold.py` for the
exact flip costs, exhaustive five-site minima, threshold, and metastable
hostile packet.
