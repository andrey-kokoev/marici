# Source-certified producers for a bounded native fragment

## Closed claim

`agda/SourceCertifiedPrograms.agda` supplies an explicit producer grammar and typed certificates for its native outputs, including a uniform higher family, its path and its higher alpha. This closes `parameter-origin-discipline` **for this named grammar**, not for every old native derivation.

The closed grammar removes the earlier compiler's arbitrary inherited operand inputs. It begins only at the declared original `root v` seeds, attaches actual source edges, and compares recursively generated operands using the existing canonical compiler. There is no constructor importing an arbitrary Resolve proof, Fragment, Body, type, function, equivalence, family, path or alpha.

Vertex, edge, mode and program-tree choices remain declared control inputs. The unpointed graph does not uniquely select a program.

## Grammar and certificates

`Program` has three constructors:

- `seedP v` uses the original `root v`;
- `attachP p edge` uses the actual `Out(v)` and the preceding generated package;
- `compareP mode p q guard` uses the canonical comparison compiler on the recursively decoded operands.

The guard is a checked Boolean equality. Its type is proved proposition-valued; changing its proof gives an equal program. It cannot carry an independent comparison or value payload. `Pair.build` computes either a certified comparison program or the compiler's actual separating-fiber refusal.

`Command` has three constructors:

- `bodyP p` emits the program's native package;
- `coherenceP mode p q guard` emits the computed comparison-coherence path in a faithful envelope;
- `unitHigherP mode p q guard` emits the next higher-rule package using the derived right-unit alpha.

Every command evaluates to both a `Complete` and an actual `Resolve Seeds` proof using the unchanged native rules. `Produced q d` retains the command, an equality of its output with q, and a **dependent equality of its computed derivation with d**. This is stronger than a receipt saying that q is admitted. It is a constructive producer witness up to the stated equality, not proof of a unique historical producer of an unrelated old proof.

## Higher-parameter audit

The inspected `HigherWitnessAdmission` mechanism has two different boundaries:

1. `PathAdmission.from-derived-point` accepts a path as an argument. Admission alone therefore does not establish that path's origin.
2. Its concrete branch family and coherence witnesses are separately constructed. Those producer programs, rather than the admission wrapper alone, are the relevant evidence.

The new grammar makes a bounded version of that distinction executable:

| Parameter | Producer |
|---|---|
| Attachment index | Actual source `Out(v)` |
| Attachment family | Existing reflexivity family over the preceding generated package |
| Comparison equivalence, selected-point and port witnesses | Canonical compiler on generated operands |
| Higher index | Complete Filler type computed from those operands and mode |
| Higher family | For each **internally bound** filler, the reflexivity package of its actual native comparison |
| Uniform family derivation | Native comparison followed by reflexivity, for every bound filler |
| Left endpoint | Computed canonical filler |
| Right endpoint | Explicit right-unit normalization of its selected-point witness |
| Coherence | Existing complete-filler uniqueness on those computed endpoints |
| Envelope path | That coherence paired with reflexivity |
| Higher alpha | Foundation `rUnit` applied to that computed envelope path |

The filler variable is bound inside the derived uniform family; a caller does not supply an arbitrary family or its witness function. The envelope projection is proved an equivalence, the exact filler path is recovered, and the final alpha is used by the actual unchanged higher rule.

These are concrete producer constructors, not a general reflection theorem for every possible Agda function or native parameter program.

## Reused predecessor boundaries

- `GeneratedContinuationContexts` already shows how to distinguish explicit program syntax from importing arbitrary maps. Its general ground types, inverse-law inputs and `Extended.generated-map` constructor are not silently promoted to source-derived inputs or old native rules here. The new evaluator targets the original `Resolve Seeds`, not that extension.
- `ResolutionMapIntroductionGap` already proves that the original rules do not introduce an unseeded bare `maps` root. That exact-presentation result remains intact, and is freshly reused alongside the continuation extension's boundary theorem.
- The new grammar does not need bare map admission: it uses the existing comparison and envelope presentations.

## Arbitrary-function injection replay

For arbitrary types X,Y and supplied function f:X→Y, the new control uses the **original graph seeds**:

    family x = E-package Y (constant (pointQ A)) (f x)
    encoded = Pi-package X family.

Every branch and the resulting package are natively derived under original Seeds. Projection recovers f(x) exactly. No Unit seed is added or substituted.

Nevertheless `Produced encoded admitted` is empty for this grammar. All command outputs have a non-Pi root; the injected package has a Pi root. A Boolean Code observation proves the incompatibility even across a proposed equality of Complete packages.

This is deliberately an **exact-presentation exclusion**. It neither proves semantic nonexpressivity of f nor forbids every alternative representation of a function. It establishes that native admission and recovery of a supplied parameter do not by themselves provide this producer certificate.

## Verification

    python research/strominger/checkers/check_source_certified_programs.py

Fresh safe Cubical/guarded Agda closure passed with ignored interfaces, implicit libraries disabled, stable sources and a conservative 2,308-file include-root/primitive manifest. Three negative controls reject certifying the injected function with a seed program, importing an arbitrary old Fragment history, and bypassing the failed same-point comparison guard. The positive proof also constructs a genuine higher-rule output and its producer certificate.

Cubical indexed-match warnings are recorded; no repository-source warnings were reported. No original native rule, Seeds declaration or other-owner source was modified.

- Proof: `agda/SourceCertifiedPrograms.agda`
- Grammar and parameter ledger: `contracts/source-certified-programs.v1.json`
- Receipt: `results/source-certified-programs/verification.json`
- Lock: `results/source-certified-programs/dependency-manifest.json`
- Connected net: `wg-source-determination-conjecture-net-v1.md`

## Remaining common-witness boundary

This grammar does not accept arbitrary initial Resolve inputs or automatically certify every raw term in the older forward/forward diagram. In particular its current source constructor starts at `root v`, not an arbitrary transported initial proof. Binding the exact chosen forward histories into a certified producer/context interface remains part of assembling the overall common-witness theorem; it is not erased by this local closure.

The chosen triple-exchange overlap is still open and is the next executable net frontier. General coherence induction, continuation/task policy, non-set fibers and the overall source-certified objective remain open. None is inferred from the existence of this bounded grammar.
