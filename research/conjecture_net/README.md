# Signed conjecture interaction net

This executable model treats a conjecture diagram as a finite signed port graph. It contains no clock, signal propagation, causal order, or sequential meta-verdict.

## Complete sign semantics

Let \(S=\{+,-\}\). An exploration agent is one of the four elements of

\[
S\times S=\{++,+-,-+,--\}.
\]

The agent \(E_{ab}\) is the local typed relation

\[
a\longrightarrow b.
\]

Its principal port has polarity \(a\), and its auxiliary port has polarity \(b\). Thus:

- \(E_{++}\) preserves confirmation polarity;
- \(E_{+-}\) changes confirmation to rejection polarity;
- \(E_{-+}\) changes rejection to confirmation polarity;
- \(E_{--}\) preserves rejection polarity.

These are static input/output polarities, not earlier and later events.

A wire is admissible exactly when its endpoint polarities agree. Consequently adjacent exploration agents compose by ordinary relation composition:

\[
E_{ab};E_{cd}\text{ is defined iff }b=c,
\qquad
E_{ab};E_{bd}=E_{ad}.
\]

The path word `+-,-+`, for example, is a well-typed \(+\to+\) path. The word `+-,++` is ill-typed.

## Structural agents

A signed `fork` has traversal `p -> a0 | a1`; a signed `join` has `a0 | a1 -> p`. All three ports have the structural agent's polarity. Explicit forks and joins express alternatives while every port remains incident to at most one wire.

`origin` and `terminal` each have one signed port. A path is an alternating sequence of wires and directed local traversals. Its composite type is fixed by the endpoint signs.

## Enumeration

For a finite net, `Net.paths()` exhaustively enumerates simple origin-to-terminal paths. `Net.path_words()` projects each structural path to its word over `{++, +-, -+, --}` while preserving multiplicity of distinct routes.

The implementation validates before enumeration:

1. all agents and ports exist;
2. every port has at most one wire;
3. every wire preserves polarity;
4. origin and terminal designate agents of the corresponding kinds.

## Interaction-net boundary

This completes the static compatibility and path semantics. A reduction system is orthogonal: it would consist of local rules replacing principal-port active pairs by polarity-equivalent finite subnets. Such rules must preserve the free-port interface. Reduction is a relation among static nets, without an inherent temporal or causal reading.

## Next-rung refinement

`refinement.py` decomposes a costly parent action into typed child gates. Each gate declares required interfaces, typed outputs, estimated cost, branch elimination, interface tightening, and falsification power. Hard type/incidence gates receive scheduling priority. Dependency order is checked for cycles, duplicate interface names are rejected, and the parent aggregation rule is frozen before execution. A parent outcome remains undefined until every child resolves.

`RefinementEvent` records this operation immutably in `event_log.py`. Continue an existing ledger with `EventLog.resume(projection)`; constructing a new log from graph/state alone intentionally starts a segment-local projection and must not be used for cumulative metrics. `project(through=n)` treats `n` as an event count in the closed range `0..len(events)`. Metric reporting can use `metric_percent_delta`; a zero previous base is returned as `None` rather than an invented percentage.

## Composite arrow tests

`composite_arrow_tests.py` compares alternative typed paths with common endpoints. It composes four-valued arrows, rejects port mismatches, reports the complete suspect edge set on path disagreement, and scores shared-computation bundles by prospective entropy touched per joint cost. A composite pass establishes path coherence only; it does not resolve every constituent arrow unless a separately frozen identifying contract permits that inference.

`path_polarity_constraints.py` adds wildcard constraints (`*+`, `*-`, `+*`, `-*`, or exact signs) over unresolved paths. Bounded exact propagation classifies a target as forced, possible, impossible, or typing-impossible and reports witnesses or a minimal constrained-arrow unsatisfiable core. Alternative-path coherence can be imposed simultaneously.

`coherence_pyramid.py` applies typed coherence layers successively, records marginal pruning at each rung, and ranks the next constituent-arrow observation by survivor entropy per declared cost. Object-level domain/codomain checking is separate from sign composition, preventing equal sign vectors in unrelated interfaces from being identified.

## Authoritative metrics

`graph_metrics.py` derives frontier width, interface deficit, coherence burden, formal outcome entropy, active action count, and declared terminal depth from an explicit typed graph snapshot. Percentage changes are valid only when computed by `percent_change(before.metrics(), after.metrics())`; zero bases return `None`. Hand-authored `before`/`after` dictionaries are not authoritative projections.

Run:

```text
python research/conjecture_net/test_conjecture_net.py
python research/conjecture_net/test_refinement.py
python research/conjecture_net/test_refinement_event.py
python research/conjecture_net/test_composite_arrow_tests.py
python research/conjecture_net/test_path_polarity_constraints.py
python research/conjecture_net/test_coherence_pyramid.py
```
