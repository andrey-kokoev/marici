# Weighted joint reference faults are augmented minimum cuts

## Bounded question

What replaces the simple-graph identity

\[
d_{\mathrm{mix}}=1+\min_{v\notin A}\deg(v)
\]

when comparison edges may be parallel or carry unequal fault costs?

## Frozen model

Let \(G=(V,E)\) be a finite loopless multigraph, let \(A\subset V\) be a
nonempty anchored set, and attach positive costs \(\alpha_v\) to command
flips at unanchored vertices and \(\beta_e\) to comparison-record flips.
A nonzero command flip set is a nonempty \(S\subseteq V\setminus A\).  Its
undetectable joint representative flips the command vertices in \(S\) and
exactly the comparison records in the multiset cut \(\delta_G(S)\).  Hence

\[
d_{\alpha,\beta}
=
\min_{\varnothing\ne S\subseteq V\setminus A}
\left(
\sum_{v\in S}\alpha_v+
\sum_{e\in\delta_G(S)}\beta_e
\right).
\]

This is a classical pre-actuation controller model. It does not model quantum
actuator faults, correlated faults, or the physical cost of the comparison
interface.

## Augmented-cut theorem

Construct \(G^+\) by contracting all anchors to a root \(r\), retaining every
comparison edge with capacity \(\beta_e\), and adding an edge \((r,v)\) of
capacity \(\alpha_v\) for each unanchored vertex \(v\). Then

\[
d_{\alpha,\beta}
=
\min_{v\in V\setminus A}\lambda_{G^+}(r,v),
\]

where \(\lambda_{G^+}(r,v)\) is the minimum capacity of a cut separating
\(r\) from \(v\).

Indeed, every root-side complement \(S\subseteq V\setminus A\) has augmented
cut capacity

\[
\operatorname{cap}_{G^+}(\delta(S))
=\alpha(S)+\beta(\delta_G(S)).
\]

Minimizing over nonempty \(S\) is equivalent to first choosing any
\(v\in S\), then minimizing over cuts separating \(v\) from \(r\).

Consequently the controller detects every joint fault of cost below
\(d_{\alpha,\beta}\). For integral unit fault costs it corrects every set of
at most \(t\) joint faults exactly when

\[
\min_{v\notin A}\lambda_{G^+}(r,v)\ge 2t+1.
\]

## Why degree ceases to suffice

Take an anchor \(a\), unanchored vertices \(u,v\), one edge from each of
\(u,v\) to \(a\), and five parallel edges between \(u,v\), all with unit
cost. Both unanchored weighted degrees are six. A singleton cut has joint
cost seven, but \(S=\{u,v\}\) has cost four. Thus

\[
d_{\mathrm{mix}}=4<7=1+\min\deg.
\]

The earlier simple-graph theorem is not contradicted: its lower bound uses
the fact that a set of \(s\) vertices contains at most \(s(s-1)/2\) internal
edges. Parallel edges destroy that step.

## Carrier geometry versus coefficient lens

The cut incidence \(S\mapsto\delta_G(S)\), anchor contraction, and augmented
root construction belong to shared Carrier geometry. The positive costs,
the choice of which command and comparison faults are admitted, and the
Hamming decoding interpretation belong to the classical coefficient lens.
Nothing here supplies quantum Pauli commutation, a syndrome Hamiltonian, or a
physical fault-rate model.

## Exact audit and falsifiers

The checker compares the defining subset minimum with independently enumerated
root-separating cuts for exhaustive small weighted multigraphs. It also checks
the unit simple-graph specialization and requires the parallel-edge degree
formula to fail on the explicit three-vertex witness.

The theorem is falsified by any positive-cost finite fixture for which the two
minima differ. The decoding corollary is falsified by a pair of distinct error
patterns of cost at most \(t\) with the same readout when the augmented cut is
at least \(2t+1\).

## Claim boundary

This is a finite classical coding theorem. It does not establish efficient
decoding under arbitrary real costs, stochastic thresholds, temporal fault
tolerance, hypergraph comparisons, correlated noise, quantum actuator repair,
or source authority for a particular controller architecture.

## Process calibration

Pre-objective: excitement 9/10, confidence 9/10, expected information gain
8/10. The frozen branches were an augmented-mincut invariant and a degree-like
closed formula. The obvious confound was hindsight from the simple-graph
identity.

Post-objective: excitement 9/10, confidence 10/10, realized information gain
9/10. The degree branch was eliminated by one exact witness; the augmented-cut
branch became an exact weighted-multigraph theorem. One canonical construction
and two equivalences were established. Weighted efficiency, correlated noise,
and physical implementation remain unresolved.
