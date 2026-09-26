# First explicit dependent reduction fragment

`agda/ResolutionNetDependentMachine.agda` freshly passes safe Cubical Agda with --ignore-interfaces; log: results/agda-dependent-machine.log. This is a small constructed fragment, not an independently bootstrapped foundation or a complete dependent type theory.

Unlike the preceding function models, it contains first-order object syntax and directed reduction rules. Index expressions have variables, Bool literals and flip. An Output is indexed by its actual index EXPRESSION. Its mathematical result family is Unit at true and Nat at false. The choose expression supplies tt or a stored numeral according to that index.

Object substitution traverses syntax explicitly. A substitution of variables can expose new redexes. The output substitution's type checks that substituting the input also substitutes the output's type index.

Checked results:

* identity and composition of index substitution;
* substitution preserves indexed output typing by construction;
* index and configuration reductions remain valid under substitution;
* every closed configuration is a value or has a computed next step;
* each reduction preserves the dependent pair of mathematical index AND result;
* interpretation commutes with object-level substitution.

The stepper is defined before the mathematical interpreter and never calls it. It executes syntax by local rules. Thus the operational machine and the model are separate definitions here, with their connection proved rather than assumed by defining execution as host function application.

Concrete checked execution:

    open input: choose (flip x) 1
    supply x := true
    choose (flip true) 1
      → choose false 1
      → number 1
      [halt]

The machine-first, machine-second and machine-halts equations check that the actual stepper produces exactly this trace. The open program uses one variable; substitution closes it into the empty variable context.

Scope: this fragment has real dependency (the result type varies with the input) but deliberately limited expressivity. It has no binders, general Pi/Sigma syntax, general recursion, effects, linear contexts, object-level equality/transport syntax, or universal normalization theorem. Its soundness proof is not a derivation of these missing features. The prior nontrivial circle transport test is NOT yet represented by this machine.

Foundational lesson: aligned mathematical composition can be exposed as explicit syntax substitution, and a separate directed machine can preserve it. However, direction of execution is additional chosen structure: substitution laws alone did not select these rules. The next discriminating extension is witnessed transport at unchanged endpoints, where an endpoint-only machine would erase observable mathematical action.
