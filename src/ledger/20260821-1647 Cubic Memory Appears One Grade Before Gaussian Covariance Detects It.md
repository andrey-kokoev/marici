# 1647 — Cubic Memory Appears One Grade Before Gaussian Covariance Detects It

## Falsifier

Entry 1646 characterizes Markov descent exactly inside the Gaussian category.  Apply a cubic interaction and test whether covariance remains a sufficient detector after the state leaves that category.

## Cubic kick

For independent centered unit-variance Gaussian quadratures (X,Y,Z), the generator (XYZ) gives

\[
P_X'=P_X-gYZ,
\qquad
P_Y'=P_Y-gXZ.
\]

Parity kills all first-order corrections to the linear covariance blocks.  A covariance-only audit therefore reports no first-order observed--internal cross block.

## First non-Gaussian memory grade

The supported quadratic observable (YZ) gives

\[
\operatorname{Cov}(P_X',YZ)
=
-g\,\mathbb E[Y^2Z^2]
=-g.
\]

Hence the full state is already nonfactorized at first order.

The internal linear covariance detects the failure only at second order:

\[
\operatorname{Var}(P_Y')-operatorname{Var}(P_Y)
=g^2\mathbb E[X^2Z^2]
=g^2.
\]

Meanwhile the displayed linear observed--internal covariance remains zero through this order by odd Gaussian parity.

## Narrow result

\[
\boxed{
\text{full process memory begins at }g,
\qquad
\text{Gaussian-covariance memory begins at }g^2.
}
\]

Thus Entry 1646 remains correct but is insufficient after cubic evolution: covariance sees only a quotient of the process object.  The first memory class lives in the mixed linear--quadratic moment layer.

This supplies a concrete cosmological reason for higher moment/Rees grades.  It does not require a new carrier stratum; the extra datum is a higher coefficient layer on the same labelled occurrences.

## Durable artifacts

- `research/benincasa/checkers/cubic_memory_normal_order.rs`
- `research/benincasa/results/cubic-memory-normal-order.json`
- `research/benincasa/cubic-memory-normal-order.md`

## Next falsifier

Construct the minimal degree-two observable extension containing (YZ) and derive its two-step process-tensor closure under the cubic generator.  Test whether this finite extension closes or generates an unbounded moment hierarchy.  Closure would yield a finite coefficient object; degree growth would force a filtered infinite process module.
