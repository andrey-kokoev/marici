# The eighth axis is regulator/completion

## Coordinate

Add the directed coordinate

\[
R:\text{finite regulated packet}\longrightarrow\text{completed carrier}.
\]

The eight local axes are

\[
(H,V,D,q,L,C,O,R).
\]

They mean:

1. input arity/rooted substitution;
2. output arity/physical cut;
3. polarity;
4. chart successor;
5. convolution degree;
6. realization comparison;
7. observation/readout;
8. regulator completion.

The `R` coordinate is binary only locally: before and after one completion comparison. Globally it is a filtered or pro-direction through cutoffs.

## Why completion enters after observation

At finite cutoff, the analytic operations are concrete but may be lax. Observation produces finite endpoint and trace data. Completion asks whether these operations and readouts converge to one closed object independently of operation order.

The fundamental leakage term is

\[
A_X=P_X\mathcal F(I-P_X).
\]

At finite `X`, chart transport need not preserve the truncated carrier. The completed square becomes strict only after a compatible leakage nullhomotopy or convergence theorem.

Thus completion is the axis that decides whether the previous seven-dimensional finite architecture survives passage to the limit.

## Seven new face types

| Face | Current role |
|---|---|
| `R x H` | completion under product-associahedral/rooted refinement |
| `R x V` | completion of finite cut coactions and their leakage cells |
| `R x D` | dagger compatibility with aperture/projective graph completion |
| `R x q` | chart-transport leakage and completed strictness |
| `R x L` | graph-domain invariance of convolution-degree multipliers |
| `R x C` | completion-level realization comparison |
| `R x O` | trace/endpoint convergence and retained joint-graph completion |

The strongest unresolved face is `R x C`: the completion-level comparison between the canonical and historical realizations. The `R x q` face is naturally lax at finite cutoff. The `R x O` face exists for weighted trace-class and retained joint-graph carriers, while raw positive feature legs can fail strong Hilbert convergence.

## Combinatorics

The local 8-cube has

\[
256\text{ vertices},
\quad1024\text{ edges},
\quad1792\text{ squares},
\]

and one 8-cell. Its Freudenthal triangulation has

\[
8!=40320
\]

maximal ordered 8-simplices.

This equals the repository's recurring count of `40320` schedules, but a direct dictionary fails. Historical schedules permute

\[
(0,A,J,P,C,T,E,F),
\]

where `0` is an initial object rather than an operation. They therefore contain seven transition types, not eight independent axes. The historical transitions also combine several roles: cutoff `C` mixes chart and regulator structure, endpoint completion `E` mixes observation and completion, and the apex filler `F` is a comparison cell. Conversely, the proposed input/output arity axes have no historical schedule symbols.

Thus the equality `8!=40320` is factorial coincidence at the level of cardinality, not an identification of indexed sets. The historical schedules remain distinct from both the proposed operational cube and the 343 geometric tetrahedra.

## Higher law

The unique 8-cell says that every ordering of the eight operations gives the same completed observed realization after inserting all lower comparison cells. Schematically:

\[
\operatorname{Complete}\,
\operatorname{Observe}\,
\operatorname{Realize}\,
LqDVH
\]

is independent of ordering up to the declared hierarchy of homotopies.

This is the first level at which finite operation order, analytic realization, observation, and completion appear in one coherence object.

`check_eight_axis_regulator_completion_frontier.py` verifies the 8-cube face counts, cyclic Gray code, `8!=40320` triangulation count, and classifies all seven regulator pair faces.
