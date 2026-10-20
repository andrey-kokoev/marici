# Actual forward/forward two-comparison, two-attachment Body binding

## Closed claim

The named two-exchange, two-attachment diagram now uses the **actual forward-lifted initial native proofs**, rather than the earlier inverse-facing return to the original operand. Its four interchange cells compose at checked interfaces. Sequential and fused complete fillers agree, the actual native derivations are compared dependently, and their higher path has faithful native envelope admission.

The theorem is parameterized by **every** `d : Resolve Seeds (pointQ A)`. The original attachments are AB then BC. A generic two-attachment row helper is proved, but the assembled two-row theorem is this named A/AB/BC diagram, not an all-vertices/all-edge-pairs or global Body-action theorem.

## Actual proof and operand lineage

`agda/ForwardForwardBodyBinding.agda`, module `Diagram d`, defines:

    d1 = moveInitial A d
    d2 = moveInitial B d1
    a0 = start A d
    a1 = start B d1
    a2 = start A d2

The comparison compiler derives the first complete filler from `exchange a0 a1`, producing q1. It derives the second from `exchange q1 a2`, producing q2. The latter retains both q1 and the actual d2. It does not substitute `root A`, the original d, or a new backwards lift for that input.

The existing `forward-square-initial A d` is explicitly bound to an equality `a2 ≡ a0`, then to Body, both attachments, and a dependent path of their native derivations. This is a **propositional comparison**, not a definitional reset. No proof-irrelevance assumption on Resolve is used.

Here “forward/forward” names this actual initial-proof tower inside the specified Body diagram. It does not assert that a globally defined forward functor has been applied twice to every arbitrary Body, including its comparison constructors.

## Four cells and exact interfaces

| Row | Base comparison | Attachment pair | Actual cells |
|---|---|---|---|
| First | q1: a0 compared with a1 | AB, BC, transported to BA, AD | FirstRow.First, FirstRow.Second |
| Second | q2: q1 compared with a2 | BA, AD, transported back to AB, BC | SecondRow.First, SecondRow.Second |

All four are instances of the existing `InternalComparisonInterchange.Interchange`, not newly invented laws. Each row retains the comparison-after-attachment and attachment-after-comparison terms. Its second cell is composed with the first cell lifted through the next attachment.

`rows-meet : FirstRow.target ≡ SecondRow.leftFinal` is reflexivity on the actual Fragment terms. That is the interface which previously could not be assumed from separate Chain and Body results.

## Sequential and fused routes

The common outer source compares the first row's actual source with the second row's right operand at depth two. Its comparison filler composes the first row's sequential map with the second row's twice-attached base comparison. The outer source therefore retains the first row's comparison and witnesses.

- **Sequential:** rebase the outer comparison graph to the second row's source using their actual common right operand and graph equivalences; then apply the second row's two-cell pasting.
- **Fused:** project the same fixed outer comparison to its right operand; lift the inverse second **base comparison graph** through both dependent attachments in one route. This does not paste the second row's interchange cells.

The fused route uses inversion of a carrier equivalence as a comparison operation. It does **not** replace the second initial proof by the earlier inverse-facing proof or reset a native premise.

Both routes are complete fillers between the exact same source and target: equivalence, selected-point witness and whole-carrier reader law. Both agree with the independently computed final canonical filler. Their equality includes all these witnesses, not only point observations or carrier functions. A dependent path then compares their actual native derivations.

The 16-term raw Body diagram retains the original a0/a1/a2, q1/q2, four main cells, intermediate row interfaces and final terms. Full-filler coherence does not delete that retained diagram.

## Higher admission and recovery

`agda/ForwardForwardHigherAdmission.agda`, module `Admit d`, reuses the existing construction pattern from `TwoComparisonHigherAdmission`:

1. Build a reflexivity branch over every complete final filler, from that filler's actual native comparison derivation.
2. Admit the E envelope using the unchanged native rules and original Seeds.
3. Prove its projection is an equivalence, using the generated fragment's proved carrier sethood to contract the branch loop fibers.
4. Lift the derived sequential/direct filler equality into the envelope and recover that exact equality by projection.
5. Admit the resulting higher path with the existing `HigherWitnessAdmission.PathAdmission` theorem.

The bare atomic path package remains **not admitted**, by the existing atomic-spine invariant. The successful envelope does not reverse that earlier rejection. The raw diagram and its native closures are also retained in a recoverable certificate; reifying that certificate as an atom at the next universe is not claimed as a native admission of that atom.

## Verification

    python research/strominger/checkers/check_forward_forward_body_binding.py

Fresh safe Cubical/guarded Agda closure passed with ignored interfaces, implicit libraries disabled, stable inputs and a conservative 2,304-file include-root/primitive manifest. Three negative controls reject:

- using reflexivity instead of the actual forward-square witness;
- leaving an AB edge untransported at a B source;
- treating the admitted envelope higher path as admission of the bare atomic package.

The first is a judgmental-equality control: the required propositional equality is positively proved, not refuted. Cubical indexed-match warnings are recorded; no repository-source warnings were reported. The earlier inverse-facing modules and other-owner implementations remain unchanged.

- Binding: `agda/ForwardForwardBodyBinding.agda`
- Higher admission: `agda/ForwardForwardHigherAdmission.agda`
- Contract: `contracts/forward-forward-body-binding.v1.json`
- Receipt: `results/forward-forward-body-binding/verification.json`
- Lock: `results/forward-forward-body-binding/dependency-manifest.json`
- Connected net: `wg-source-determination-conjecture-net-v1.md`

## Remaining obligations

The scoped `two-comparisons-two-attachments` node is closed. The chosen triple-exchange overlap, general coherence induction and non-set witness cases are not inferred from this finite diagram. New comparison parameters here are derived; arbitrary inherited parameter origins elsewhere remain uncertified.

The next recommended gate is the existing **parameter-origin discipline** task: turn these bounded producers and their ledgers into an explicit certified program fragment, and audit the remaining higher-family inputs. The chosen higher source-action overlap remains a separate actionable frontier, not silently discharged by this result.
