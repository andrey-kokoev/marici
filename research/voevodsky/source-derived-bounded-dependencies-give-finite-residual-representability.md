# Source-derived bounded dependencies give finite residual representability

## Frozen premise

Read the owning inspectable operational rule language, not its reference quotient. Its state fields are end (a six-event subset mask), origin (binary), and pending/received/issued (absent or binary). Guards and output reads seed dependency closure; retained update expressions recursively add their dependencies. All five fields are needed by this syntactic closure.

The product of declared source-domain cardinalities is

    64 * 2 * 3 * 3 * 3 = 3456.

The contract freezes these domains before exploration. Exhausting 62,208 state/label cases verifies that this finite carrier is inductive under all eighteen operations, including observable rejected self-loops. Initial values lie in it. There are no opaque callbacks or undeclared variable reads.

## Independent tightening

A Cartesian range analysis starts from the declared initial values, propagates all rule updates, and stabilizes in five iterations. It permits nine endpoint masks and the same other value domains, giving the smaller upper bound

    9 * 2 * 3 * 3 * 3 = 486.

This range analysis does not inspect a reference graph or minimal classes. Subsequent source-rule reachability yields 70 compatible states; minimization yields 70 states with both origin audits and 62 for the original language.

The owning causal-interface verifier is also freshly replayed. A control adding a guard on an undeclared historical counter is rejected by dependency validation before state exploration.

## Conditional theorem

Suppose independently admitted field values range over finite domains, initialize inside their product, and remain inside it under every rule. Suppose every admission guard, observable output and update of a retained dependency is a function of those values and the declared action parameters. Then equal retained valuations have equal present outputs, equal admission and equal next retained valuations. Induction supplies equality for every finite continuation.

The finite valuation carrier is therefore a sufficient residual observer, of size at most the product of the domain sizes. Its minimal continuation quotient is finite. With k fields of at most d values, d^k is a coarser bound.

The substantive gate is an independently established, inductive dependency carrier. A bound on simultaneous field count alone is insufficient when fields have unbounded values. A promise that history factors through some values is likewise insufficient for implementation unless their initialization and updates are constructively given.

## Structural synthesis

Finite representability here comes from a closed finite space of influences across a cut. Reachability removes jointly impossible combinations; continuation equivalence then removes distinctions irrelevant to the frozen language.

Thus three reductions have distinct meanings:

    3456 syntactically typed valuations
      -> 486 range-admissible valuations
      -> 70 source-reachable valuations
      -> 62 current-language behavior classes.

The audit language retains all 70 source-reachable distinctions. This theorem concerns finite state cardinality. The piecewise analytical interface can be finite-dimensional while containing infinitely many distinguishable real-valued states; it satisfies a different representation contract.

## Reproduction

    python research/voevodsky/checkers/check_bounded_dependency_finite_residual.py

Artifacts:

- `results/bounded-dependency-finite-residual-contract.json`
- `results/bounded-dependency-finite-residual.json`
