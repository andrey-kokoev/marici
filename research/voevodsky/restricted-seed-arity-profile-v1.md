# Restricted seed/arity profile: actual Resolve compilation

Target: `parent:formulation-and-quantifiers`, still open.
Formal source: `research/voevodsky/agda/RestrictedSeedArityProfile.agda`.
Checker: `research/voevodsky/checkers/check_restricted_seed_arity_profile.py`.
Receipt: `research/voevodsky/results/restricted-seed-arity-profile-v1.json`.

## Fixed bounded profile

This profile fixes ℓ=0 in the existing `WholePackageSigmaPi.Universe` and `WholePackageResolution.Generators`. Code and Complete are at successor level. It introduces a syntactic `Term : Type` with exactly:

- `literal false-seed`, the only admitted literal command;
- `identity t`, applying the existing identity-comparison rule;
- `pair t u`, applying the existing Pi rule indexed by Bool;
- `select b t u`, applying the existing E rule indexed by Bool with explicit selected index b.

There is no arbitrary Complete, function, equivalence, family, proof or expected answer parameter in this syntax. Inputs are finite terms built from the fixed constructors. Boolean selection is an explicit rule parameter, not an additional literal seed. The profile is noncircular: grammar membership does not depend on observed outputs or whether a desired theorem was proved.

## Constructed native-source bridge

`eval` uses the actual imported rule outputs, not a parallel toy arithmetic evaluator. `compile` constructs an actual `G.Resolve Seed (eval t)` by structural recursion. It uses the original `seed` constructor on the one literal and `apply` for the three selected rules. The Bool-indexed applications retain both input derivations, including the unselected E branch.

`run` retains the original source term alongside this typed derivation. `source-recovered` is reflexive. It guarantees source recovery from the retained record, not recovery from an endpoint-only value or an injectivity theorem about eval.

This instantiates three of the twelve existing rule schemas. The parent native-table equivalence can apply to the original source relation, but no new independently executed native-table compilation or full twelve-schema effective fragment is claimed here.

## Finiteness and resources

Every Term constructor has at most two recursive arguments. `cost` computes the number of syntax nodes, counting both E branches; it is a structural finite-work measure, not measured physical time, bit complexity of every target expression, or a claim about all terms of the unrestricted Resolve type.

The selected example keeps a literal on the chosen branch and an identity-wrapped literal on the unselected branch. Its cost is four, not two. A deliberately ill-typed equality attempting cost two must fail compilation. Another negative module attempts `literal true`; true is a Boolean value, not the sole syntactic SeedName, so it is rejected.

A stronger future complexity claim would need a target representation and evaluator cost model, including copying/sharing and proof normalization. The present structural recursion is not that theorem.

## Syntactic admission versus semantic closure

The seed relation used as the target of compile is an indexed Agda family. It lives inside a type theory with equality/transport; this work does NOT characterize all its inhabitants or its entire semantic closure. In particular, absence of a literal command named true is not a proof that no semantically related package can ever arise under type paths or other rules.

The exact restriction proved is on the explicit source language and its compilation. This avoids using an equality of complete packages as a surrogate for source provenance. Supplying a target package or a path to a seed does not manufacture a source command in this profile.

The full existing resolution signature admits arbitrary index types and supplied evidence. Its infinitely branching cases and externally supplied atoms/functions remain outside this finite source grammar. They have not been declared invalid mathematics.

## Verification and next gate

Fresh headless safe Cubical compilation of the new module and its imported closure passes, with interfaces ignored. Both negative modules are checked separately. No postulates, holes or owner-source changes were added.

The profile provides a concrete bounded F/K test of the candidate formulation. It does not select a universal foundation, interpret analytic completion, construct a physical account or close the formulation gate.

Next: compare the actual three primitive rule meanings with a candidate common process/resource interface, and decide explicitly whether to extend this effective grammar or retain the unrestricted semantic source policy as a separate scope. Do not extrapolate this finite profile to universal coverage.
