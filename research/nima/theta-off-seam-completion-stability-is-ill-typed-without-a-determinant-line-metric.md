# Off-seam completion stability is ill-typed without a determinant-line metric

## Defect in the previous criterion

The previous completion gate asked for uniform bounds on finite determinant-line trivializations and their inverses. That statement depends on the chosen frame.

Let \(L_X\) be a one-dimensional line and let \(s_X\in L_X\) be a nonzero section. In a frame \(e_X\),

\[
s_X=t_Xe_X.
\]

Changing frame by a nonzero scalar \(g_X\),

\[
e'_X=g_Xe_X,
\]

changes the coordinate to

\[
t'_X=g_X^{-1}t_X.
\]

By choosing \(g_X\), the same geometric section can have bounded, vanishing, or diverging coordinates. The inverse coordinate changes oppositely. Therefore coordinate bounds on \(t_X\) and \(t_X^{-1}\) are not properties of the section or line system.

## Finite gauge falsifier

Take the constant line \(L_N=\mathbb C\) with the constant geometric section \(s_N=1\).

Three frames give:

\[
t_N=1,
\qquad
t_N'=N,
\qquad
t_N''=N^{-1}.
\]

Nothing geometric changed. One coordinate is stable, one diverges, and one tends to zero with inverse escape.

Thus a criterion based only on coordinate norms can both accept and reject the same source object.

## What would make a bound meaningful

A norm statement becomes invariant only after one of the following is source-derived:

1. a Hermitian metric on each determinant line, transported compatibly through cutoff transitions;
2. a dual line and a nondegenerate evaluation pairing;
3. a normalized connection plus an independently fixed base frame;
4. a graph topology on the entire line system whose transition maps are part of the object.

On the critical seam, local Tate transitions are unitary, so a Hilbert direct-limit metric is available. Off the seam, the same transitions are nonunitary. The seam metric does not automatically extend to either open sector.

This is exactly where reciprocal doubling is insufficient: it supplies an exchange pairing, but that pairing is indefinite and does not orient a positive norm.

## Gauge-invariant data already available

Several statements survive frame changes:

- whether a section vanishes at a fixed cutoff;
- the divisor of a completed section;
- periods of a logarithmic connection around closed loops;
- the isomorphism class of the relative line system;
- transition cocycle coherence;
- pairing with a source-derived dual observer.

Local logarithmic coordinates change by exact terms under a nonvanishing gauge. Their closed-loop periods remain unchanged. Hence the completion anomaly should be expressed as a connection or index class, not as the size of a chosen scalar trivialization.

## Raw Euler convergence is not the right substitute

Ordinary finite Euler products do not converge throughout the open strip \(1/2<\operatorname{Re}s\le1\). Requiring their scalar trivializations to converge would therefore reject the actual source before reaching RH.

The relative determinant construction avoids this by retaining primitive and square anomalies as transition coordinates and only completing the connected tail ordinarily. Any later scalar frame must be produced by the full endpoint–gamma–prime coherence law, not by assuming convergence of raw Euler frames.

## Corrected completion gate

The next constructor must provide a gauge-invariant off-seam comparison object. The strongest viable candidates are:

- a source-derived Hermitian or Krein-to-Hilbert metric on the relative determinant line;
- a source-derived dual section whose evaluation detects nonvanishing;
- a Fredholm index pairing whose open-sector value is forced to zero;
- a connection whose completion anomaly is proved to have no open-sector integer periods.

Each candidate must be constructed before reading the completed scalar section. Hostile symmetric multipliers remain the immediate falsifier because they preserve reciprocal transition metadata while changing the divisor.

## DPC

A proposed completion-stability theorem passes only if:

1. its boundedness statement is invariant under admitted frame changes;
2. the metric, dual pairing, connection, or index is source-derived;
3. raw Euler convergence is not assumed in the critical strip;
4. primitive and square coordinates remain relative transition data;
5. the theorem controls the completed section rather than a freely rescaled coordinate;
6. reciprocal sewing does not masquerade as a positive metric;
7. hostile divisor-bearing gauges are rejected by the source structure itself.

## Outcome

Finite lifted augmentation is constructed, but the earlier norm formulation of completion stability was not well typed. The missing RH-bearing object is now more precise: a source-derived, gauge-invariant off-seam detector on the relative determinant line. Without it, “bounded trivialization” is a coordinate choice, not an explanation.
