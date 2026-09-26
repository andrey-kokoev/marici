# RRC–DSC source/signature admission ledger

## Frozen interface and ambient assumptions

Audited sources: `research/nima/agda/WholePackageSigmaPi.agda`, `WholePackageResolution.agda`, and `research/voevodsky/resolution-net-v1/agda/ResolutionNetDependentSubstitution.agda`.

At level ℓ, Code and Complete live in Type(ℓ+1). El interprets Code into Typeℓ. Complete retains both an expression Q and an actual value of El Q. Reifying a whole package/history raises the universe; it does not erase the distinction between a package and its value.

Code admits eight constructors: atom, E, Pi, paths, maps, equivalences, retain, comparison. In particular atom accepts an arbitrary ambient Typeℓ, maps admits host functions, and equivalences/comparison retain supplied equivalence data. This is not a closed enumerable source language or an effective description of every atom. Infinite dependent arities are admitted.

A source is an explicit family S : Complete → Type(ℓ+1). A seed requires an actual s : S q, not merely a declaration that q is permitted. The current signature does not decide which seed witnesses exist or how to construct them. A chosen S is a mathematical source boundary, not an authorization from an external owner.

## Exact generator inventory: twelve constructors

Every application additionally requires a Resolve history for EVERY listed premise. Supplying a Rule value alone is not a derivation.

| Rule | Supplied parameters/evidence | Premise packages | Constructed result |
|---|---|---|---|
| E-rule | I, complete family F, selected i | every F j, not just F i | retained dependent sum and selected value |
| Pi-rule | I, complete family F | every F i | retained dependent product |
| compare-rule | endpoints a,b; equivalence e; boundary path e(a.value)=b.value | a and b | comparison retaining supplied e and path |
| identity-rule | a | a | identity equivalence and refl boundary |
| inverse-rule | a,b,e,p | comparison-package a b e p | inverse comparison, derived from supplied e,p, retaining the original |
| compose-rule | a,b,c,e,f,p,q | the two actual comparison packages | composed equivalence/path, retaining both inputs |
| higher-rule | Q,x,y,p,q and actual alpha:p=q | both path packages | package containing alpha; no synthesis of alpha |
| reflexivity-rule | Q,x | pack Q x | reflexive path package |
| path-lift-rule | Q,R, actual equivalence e, endpoints x,y | equivalence package containing e | derived equivalence of path spaces; no search for e |
| distribution-rule | I,J,F and actual v in Pi-of-E | all F i j AND pack left v | explicit dependent distributivity comparison |
| E-congruence-rule | I,F,G, pointwise equivalences e, boundary paths p, selected i | every pointwise comparison | derived sum comparison retaining all supplied comparisons |
| Pi-congruence-rule | I,F,G, pointwise equivalences e and paths p | every pointwise comparison | derived product comparison retaining all supplied comparisons |

Arity is respectively lifted I, lifted I, Bool, Unit, Unit, Bool, Bool, Unit, Unit, (Σ I J)+Unit, lifted I, lifted I (finite names here abbreviate their lifts).

All twelve are primitive TAGS of Resolve's current syntax. Several output witnesses are constructively derived by their implementations: identity, inverse/composition, reflexivity, path lifting, distributivity and E/Pi congruence. This does not establish that their tags are eliminable while preserving raw histories. Conversely compare and higher explicitly take the sought witnesses as parameters. Neither classification is a universal independence/minimality theorem.

## What is genuinely structural

RRC's mapSeeds and flatten are defined by recursion on retained histories. DSC's compose, extend and execute are host dependent functions with their structural laws. The recursive bridge adds explicit var/call syntax, imports all twelve generator tags, and proves representation and substitution compatibility. It derives no missing generator merely by giving the same tree another name.

`agda/ObserverRRCSourceAdmission.agda` checks a useful policy boundary. Given a mathematical predicate Allowed on actual Rule values, Admitted recursively requires Allowed at every application and all child histories to be admitted. Seed renaming preserves this predicate. Substitution preserves it provided EVERY replacement history satisfies the SAME policy.

The replacement hypothesis cannot be dropped: under a policy allowing no rules, an outer seed containing an identity-rule history is admitted, but flattening exposes a forbidden application. `Regression.no-unchecked-flatten` proves this obstruction. Thus packaging a computation as seed data is not permission to execute or flatten it. This is mathematical policy preservation, not external effect/ownership authorization.

## Next existing obligation

Activate witness construction for a specified constructive fragment. Start with explicitly supplied source witnesses and the derived operations above; separate constructing their output evidence from the unsupported task of synthesizing arbitrary comparison equivalences or higher fillers. Any completeness claim must name its source theory and decision boundary. Source-owner additions remain owner work; this ledger changes no Nima-owned artifact and does not declare a universally sufficient signature.

## Verification

The admission module and aggregate are checked with safe Cubical Agda, fresh interfaces disabled and -Werror. Exact entry coverage, source hashes, stable-source check and two rejected false-theorem controls are recorded in `results/operational-checkpoint.json`. The ledger's semantic classifications are a source audit, not automatically certified by the Agda policy theorem.
