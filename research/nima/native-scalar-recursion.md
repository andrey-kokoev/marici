# Arbitrary-even-n native scalar amplitude recursion

## Status

Formal follow-up: [native-amplitude-resolution.md](native-amplitude-resolution.md)
constructs actual native Resolve executions for all finite marked expressions,
proves their amplitude readout and semiring diagram expansion, and instantiates
the six-point fixture. The general DAG compiler is now checked against that
expression grammar through twelve points; its universal correctness remains open.

`amplitudes/native_scalar_recursion.py` implements the massless real phi-four tree algorithm for every even multiplicity `n >= 4`. It constructs and evaluates native three-column tables directly from rational external momenta and the supplied coupling. It does not import or call the old current builder or amplitude evaluator.

The earlier [four/six-point table calculation](native-scalar-fiber-amplitude.md) remains a separate checked reference. The new general implementation is computationally tested through twelve legs; it is not an arbitrary-n Agda correctness theorem.

## Recursive table construction

Each declared boundary retains its coupling, external momenta and amputated external root. A current is addressed by `(boundary, current, external-label-subset)`.

| label | from | to |
| --- | --- | --- |
| current declaration: labels, momentum, denominator, amputation flag | current address | declaration |
| three child-current addresses | current address | canonical partition port |

Every partition is an unordered split into three nonempty odd blocks. Ordering blocks by their smallest external label removes permutations without a factorial correction. All partitions and child attachments are retained. Identical labelled subcurrents are shared in a directed acyclic graph; they are not merged merely because their numerical values agree.

The independent validator checks exact coverage of partition ports, disjoint canonical child attachments, source momenta and denominators, and the external-root amputation. Child subsets strictly decrease, so cycles are rejected. Orphan currents, duplicate endpoints, missing partitions and inconsistent metadata are rejected. Boundary namespaces prevent a child from silently using another process's coupling or data.

The memoized readout is

\[
J(\{i\})=1,
\qquad
J(S)=\frac{\lambda}{P_S^2}
\sum_{S=A\sqcup B\sqcup C}J(A)J(B)J(C),
\]

\[
\mathcal M_n=-\lambda
\sum_{\{1,\ldots,n\}\setminus\{r\}=A\sqcup B\sqcup C}
J(A)J(B)J(C).
\]

The external root is amputated: its vanishing on-shell squared momentum is never used as a propagator denominator. Leaf currents likewise have no propagator.

## Relation to the weighted fiber sum

A complete diagram chooses one partition at each nonleaf current and recursively chooses a diagram in each child. For a fixed partition the children are independent and have disjoint external labels. Finite distributivity therefore turns the product of their sums into the sum of products over those choices. Induction on subset size identifies the memoized result with the expanded weighted diagram fiber sum.

The canonical partition decomposition is unique for a rooted labelled quartic tree. The stored DAG therefore preserves the individual diagram choices and their multiplicity while avoiding eager expansion. `Evaluation.diagrams(limit=...)` can explicitly expand them into internal split sets and weights. It refuses an exceeded budget rather than truncating the amplitude or deleting contributions.

The same induction explains agreement with the original recurrence when both partition enumerators enumerate exactly that family. Tests compare the actual enumerators on odd subset sizes through eleven and compare full diagram topology/weight data at eight points. This argument is not a machine-checked proof of Python semantics.

## Checks passed

- Four and six points: every external root; agreement with both the old recurrence and the earlier native evaluator.
- Eight points: two rational fixtures, every external root; all **280 distinct labelled diagram topologies and individual weights** agree with the independent three-vertex-path enumeration.
- Ten points: roots 0, 4 and 9; agreement with the old recurrence and **15,400** diagram choices.
- Twelve points: root 0; agreement with the old recurrence and **1,401,400** diagram choices.
- Exact scaling, changed coupling including zero, ten eight-point leg permutations, shuffled rows and separate boundary fibers.
- Rejection of incorrect propagators, missing/duplicate partitions, cyclic/wrong child attachments, root propagators, orphan currents, off-shell inputs, invalid roots, odd multiplicities and internal poles. A zero coupling does not bypass pole checks.

At twelve points the checked instance stores 1,024 shared currents in 88,334 rows instead of expanding 1,401,400 diagrams. This is still an exponential algorithm, not a promise that arbitrarily large multiplicities are practical. Optional diagram expansion has a separate explicit budget.

## Use and reproduction

With `research/nima/amplitudes` on the Python import path:

```python
from fractions import Fraction
from native_scalar_recursion import construct, Evaluation

rows = construct(momenta, Fraction(3, 5), root=0)
result = Evaluation(rows)
print(result.amplitude)
print(result.diagram_count)
```

Run:

```text
python research/nima/amplitudes/native_scalar_recursion_check.py
python research/aspect/scc/scc.py check nima-native-scalar-recursion
```

The source-bound receipt is `results/native-scalar-recursion.json`. It records the tested external momenta, roots, exact amplitudes, diagram counts, table sizes and implementation/reference hashes.

## Scope

The physical input remains the massless phi-four theory, `+---` metric, all-incoming momenta, vertex `-i lambda`, propagator `i/q^2`, and delta-stripped `i M`. Exact rational inputs must conserve momentum, be massless, and avoid internal poles. The API rejects odd multiplicities; it does not implement an odd-n zero-return interface.

The new algorithm does not derive these physical weights from fibration. It does not implement loops, a continuum measure, other interactions, an arbitrary-n Agda proof, or an amplitude readout on the full `NativeTableResolution.Resolve` datatype. The existing general finite-fold theorem and fixed six-point Agda calculation retain their previous scope. Independent review remains pending.
