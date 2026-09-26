# Witness production for a finite Boolean comparison fragment

`agda/ObserverRRCWitnessSynthesis.agda` implements a total constructive decision procedure, not merely a checker taking an equality witness.

## Exact source and query language

The source generators are the two exhibited packets `pack (atom Bool) b`. Source membership retains a Boolean label and an actual identity from that packet to the requested package; it is not a claim of unique source evidence or globally decidable Complete equality. The procedure uses the exhibited reflexive memberships.

A query consists of x,y:Bool and a mode: identity or swap. Each mode denotes an explicitly constructed equivalence of Bool (identity or Boolean negation). No arbitrary equivalence, boundary path or source-solver callback is an input.

A Solution contains BOTH:

- the actual boundary path `equivFun (equivalence mode) x = y`;
- an RRC Resolve history for the comparison package containing that path, with actual histories for both source premises.

## Soundness, completeness and failure

`synthesize` computes Boolean equality at the interpreted endpoint. A positive result constructs the boundary witness and an actual compare-rule derivation, including both seed histories. A negative result refutes every Solution of that fixed query by projecting its required boundary path.

Its return type is Dec(Solution mode x y). `synthesis-complete` additionally proves that existence of any Solution forces the procedure to return some positive Solution. This is existence/decision completeness, not enumeration or equality of all possible histories.

An unspecified mode can always be selected constructively for these Boolean endpoints: identity for equal values, swap for unequal values. `synthesize-any` returns the chosen mode and full solution.

Two computation regressions check definitionally that swap(true,false) succeeds and identity(true,false) fails. Failure for the latter does NOT mean that no comparison under a different equivalence exists: the former is the explicit counterexample to that overstatement.

## Admission and limits

Generated histories invoke only the declared compare-rule with its now COMPUTED equivalence and boundary witness, plus the two exhibited source seeds. Executing this fragment requires admitting those sources and that rule; the procedure grants no external authority. The earlier substitution-admission theorem still requires independently admitted replacement histories.

This establishes genuine witness construction in a finite, specified fragment. It does not solve arbitrary source equivalence, comparison synthesis for every RRC package, higher filler synthesis, infinite-arity evaluation or a complete DSC operational language. The chosen equivalences are constructed from the finite mode code, not discovered in arbitrary ambient types.

## Fresh verification and continuation

Strict fresh safe Cubical Agda passes for this module. The canonical aggregate passes50 entries with191 source/checker files unchanged and both false-theorem controls rejected in113.298 seconds. Evidence: results/agda-rrc-witness-synthesis.log and results/operational-checkpoint.json.

Next use the existing comparison-coverage branch to transfer these computed witnesses through the recursive RRC–DSC representation and distinguish generated comparison routes from equality of retained raw histories. Broader source-dependent synthesis remains open; the finite result must not discharge that universal obligation.
