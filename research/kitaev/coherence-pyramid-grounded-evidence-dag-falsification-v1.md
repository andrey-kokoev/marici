# Falsification attempt on grounded acyclic evidence

## Question

Must every admissible certificate dependency graph be acyclic and rooted in source evidence, with cycles rejected as unsupported?

## Claim boundary

This packet tests acyclicity as a universal admission condition. It does not rehabilitate unguarded circular proof.

## Bold conjecture under test

A non-unknown registry status is admissible only if its evidence dependencies reach source roots without an ungrounded strongly connected component, alongside frozen execution and semantic review.

## Guarded-cycle counterexample

Consider the complete metric space of real numbers and the equation

\[
x=1+\frac{x}{2}.
\]

Its evidence dependency is syntactically cyclic: the value of `x` is used to construct the value of `x`. Rejecting the strongly connected component as ungrounded would refuse it.

But the constructor

\[
T(x)=1+\frac{x}{2}
\]

is a contraction with constant `1/2`. Banach's fixed-point theorem supplies a unique fixed point, and iteration from any source value converges to `x=2`. The cycle is sound because every traversal decreases a certified metric residual by a factor of `1/2`.

The same pattern occurs in guarded recursion, coinductive bisimulation, recursive domain equations, feedback systems with a contraction certificate, and convergent completion constructors. Evidence acyclicity is therefore not necessary for grounded admission.

## Opposite hostile: grounded roots are not sufficient

An acyclic evidence graph may terminate at a source assertion that is mislabeled, convention-mismatched, fabricated, or simply false. Reachability of a root is provenance, not truth. Freezing the checker and environment reproduces the same error. Deliberate-failure controls test selected branches but cannot establish checker completeness.

## Strongest residual

The acyclic-grounding conjecture fails in both directions:

- it rejects valid guarded cycles;
- it admits no truth merely by reaching a root.

## Surviving conjecture

Evidence strongly connected components require a discharge certificate. Admissible discharge modes include:

- well-founded decrease;
- contraction with explicit constant below one on a complete typed space;
- guarded recursion accepted by a declared type system;
- coinductive bisimulation with a sound proof rule;
- independently grounded invariant that uniquely fixes the component.

Ungrounded and undischargeable cycles remain refused. Root records carry provenance, source identity, convention, and independent admissibility status; they are not automatically evidence of truth.

## Strongest next falsifier

Construct a cycle accepted by one listed discharge mode whose conclusion remains nonunique or false because completeness, guardedness, metric compatibility, or invariant faithfulness was misstated. Such a fixture tests the discharge certificate rather than cycle syntax.

## Disposition

Revise. Replace evidence-DAG admission by strongly connected component analysis plus typed discharge certificates. Preserve separate statuses for provenance, mechanical replay, logical discharge, semantic review, and demonstrated transfer strength.
