# The Missing Primitive Is the Evaluation Square

## Question

Should admissibility laws, interventions, and observations be represented as
three colors of edge in one Marici graph, or as separately typed structures?

## Answer

A colored graph is an adequate serialization but not an adequate definition.
The three roles have different composition laws.

Let \(P\) be the Carrier transition category. Its objects are realized states
and its arrows are source-admissible physical transitions. A source law selects
a transition-closed subcategory \(P_0\subseteq P\); it does not produce a
record.

Let \(T\) be the Task category. A realized intervention is a partial action

\[
\alpha:T\curvearrowright P_0.
\]

Task composition must agree with sequential Carrier execution wherever the
action is defined.

Let \(E(x)\) be the admitted effects at a Carrier state \(x\). Effects are not
additional state transitions. An intervention \(G:x\to x'\) transports an
effect on \(x'\) backward to an effect on \(x\):

\[
G^*e=e\circ G.
\]

An instrument supplies the evaluation map from a compatible state--effect
pair to a stable record:

\[
\operatorname{ev}_x:E(x)\times\{x\}\longrightarrow R.
\]

The essential coherence is the evaluation square

\[
\operatorname{ev}_{x'}(e,Gx)
=
\operatorname{ev}_x(G^*e,x).
\]

This is the control-theory identity behind “measure after acting” versus
“pull the output functional back through the action.” It is neither a source
constraint nor another transition.

## Why one ordinary edge algebra fails

Suppose every colored edge is placed in one freely composable category. Then
an observation edge can compose with an observation edge as though two
readouts formed a physical state transition. A source-law inclusion can be
executed as though it were an intervention. Neither composite has been
constructed.

One can prohibit those words with a typing table, but that typing table plus
its coherence equations is precisely the layered structure. The graph alone
does not carry it.

The minimum composition table is:

| Left operation | Right operation | Meaning |
|---|---|---|
| intervention | intervention | sequential execution, when typed |
| Carrier transition | Carrier transition | physical continuation |
| effect | intervention | pulled-back effect |
| record | anything | no default continuation |
| source law | intervention | domain restriction, not composition |

Thus the choice is not between “one graph” and “many graphs.” It is between a
bare graph and a typed algebra whose graph is only its presentation.

## Relation to the capability witness

The witness span

\[
T\leftarrow W\rightarrow P
\]

still records which Task operation is realized by which Carrier transition,
including multiplicity, shared ports, history, and lineage. It is incomplete
without effects and evaluation. Two witnesses can realize the same transition
and differ in what their instruments record or how later effects pull back.

The strengthened object is therefore:

1. an admissible Carrier transition category;
2. a Task category and partial realization action;
3. a witness object over Task operations and Carrier transitions;
4. a contravariant effect assignment;
5. an instrumented evaluation pairing satisfying continuation coherence;
6. lineage data making staged record pullbacks well typed.

This can be packaged categorically as an equipment, double category, or
indexed category. No such name should be promoted until the concrete Marici
composition and coherence laws are fixed.

## Equivalence boundary

Kitaev's equivalence ladder then lands cleanly:

- predictive equivalence quotients Carrier states by equality under every
  admitted intervention--effect continuation;
- constructor congruence says the Task action descends to that quotient;
- complete operational equivalence says the evaluation pairing agrees for a
  complete tester family;
- realization equivalence additionally preserves the witness object,
  internal history, interfaces, and declared gauge.

The minimal predictive Carrier is a quotient of this structure. It is not the
whole Marici object, because quotienting external behavior does not reconstruct
the realization witness or its physical constructors.

## Hostile example

Take states \(x,y\), an intervention \(G\), and a binary effect \(e\). Suppose
\(e(x)=e(y)=0\) but \(e(Gx)=0\) and \(e(Gy)=1\). Present evaluation merges the
states; the pulled-back effect \(G^*e\) separates them.

A representation retaining only state nodes and current record edges loses
the separating square. A representation retaining \(G\), \(e\), and the
pullback law predicts it. Conversely, declaring the current equation \(e=0\)
as a source constraint deletes \(y\)'s distinguishing continuation instead of
observing it.

The same incidence data can therefore support three incompatible readings:
restriction, execution, or evaluation. The evaluation square is the cheapest
datum that prevents their collapse.

## Claim boundary

This is a structural control synthesis. It does not prove that every Marici
sector already supplies a complete Task action or effect family, nor that a
double category is the final formalism. It identifies the minimum variance and
coherence that any adequate formalism must preserve.
