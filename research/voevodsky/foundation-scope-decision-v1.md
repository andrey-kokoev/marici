# Parent scope decision: a foundation-indexed family does not erase validity choice

Target: `parent:formulation-and-quantifiers`, remains open.
Checker: `research/voevodsky/checkers/check_foundation_scope_decision.py`.
Receipt: `research/voevodsky/results/foundation-scope-decision-v1.json`.

## Reviewed alternatives

1. **Fixed foundation.** Independently select F, its universes and derivability/model-validity mode, K and E; then ask Root(F,K,E). This gives a determinate conditional target once those parameters are fixed. Our bounded native profile supplies one restricted test instance, not a justified selection of the parent's universal scope.
2. **Per-foundation family.** For each admissible F there exists a P_F and a coherent realization family. This leaves physical/process selection dependent on foundation. It is strictly weaker than a claim requiring one P across every F in the chosen class, and still requires that class and admissible interpretation data to be fixed.
3. **One process across foundations.** There exists one P and physical binding, then for every admissible F and every valid M in its independently defined K_F there is coherent realization. This strengthens the fixed-F conjecture; no bounded result here proves it. It also needs a declared size/universe policy for the family and typed comparison obligations between foundations.
4. **Erase foundation tags.** Treat the same displayed formula or scalar truth annotation as having the same validity in all profiles. This candidate is rejected by the exact semantic control below.

Decision: retain the existing parameterized Root(F,K,E) as a research schema. Do NOT claim that changing it to a foundation-indexed family resolves the missing universal selection. Neither the fixed universal F nor an admissible class of F has been selected by the operator or justified by the available evidence. This is a concrete residual decision, not another unfinished toy implementation.

## A real validity discriminator

Consider p OR NOT p. It is true under both classical Boolean valuations. In a two-world intuitionistic Kripke chain 0≤1, let p hold only at world 1. Valuations are persistent. At world 0, p is not forced; NOT p is also not forced because the accessible world 1 forces p. Hence excluded middle is not forced at world 0, though it is forced at world 1.

The checker implements implication using ALL accessible worlds and enumerates all three persistent valuations of this chain. It also checks p→p as a positive control. Thus identity-on-formulas validity erasure fails on an actual semantic example, rather than merely on policy strings.

This is not a theorem that classical mathematics cannot be interpreted in constructive mathematics. Negative translations, changed semantics or restricted domains are different maps requiring their own preservation/reflection statements. Nor is this a claim about every Cubical model. It demonstrates why an unqualified phrase 'valid mathematics' cannot be replaced by silently interchanging the two validity policies.

## Common-P quantifier order

The checker exhausts all sixteen relations between two foundation labels and two candidate process labels. In every relation, one common process serving both foundations implies a process exists for each foundation. The converse fails, including the diagonal relation where each foundation has only its own candidate. This is a finite logic countermodel to the inference, not an impossibility theorem about every physical process.

A tagged union of per-foundation simulations records the difference; it does not by itself construct one independently specified native physical account or coherent cross-foundation interpretation. A universal interpreter can be a candidate, but its supplied laws, runtime/resources and physical binding remain separate obligations.

## Physical admissibility criterion versus physical existence

A precise formulation need not already exhibit a physical source. It must say what counts as one, which contexts/resources and observations matter, and what evidence establishes the binding. The current common-witness interface names these fields and physical-premise obligations. It does not select a lowest-level criterion. A bounded cavity/detector target charter is a concrete test regime, not a definition of all fundamental physical processes.

Likewise consistency or soundness of an admissible foundation class cannot simply be inferred from a finite successful run. If the class uses those properties, they are metatheoretic hypotheses requiring an explicit policy, not an effective admission test supplied by this turn.

## Consequence for the live frontier

No parent node is resolved by this review. The remaining formulation decision is genuinely about scope: fixed F/K/E or a specified class with interpretation maps and one common P. Further positive examples of the already checked finite grammar will not decide it.

Nonredundant continuation remains available: (a) specify a versioned proposed admissible foundation/physical-criterion class and review its fidelity to the original universal target, or (b) continue an independently ready RH/compatibility test while leaving this selection open. The current workbench has both. Do not mark the objective complete or infer that no executable continuation exists.
