# Witness generation: universal continuation and exact native admission

## Verdict

For the **existing declared source-continuation interface**, one fixed selected comparison has a derived, universally quantified continuation operation. It generates native interchange witnesses, coherent finite extensions, higher comparisons, and a natively admitted retained representation of those higher comparisons that can be used next.

There are two essential qualifications:

1. **The exact `RepeatedInterchangeCoherence.higher-package-formed` has no `Resolve Seeds` derivation.** Its atomic presentation is unreachable under the existing seeds and rules.
2. Universal continuation is a source-relative capability, not a consequence of arbitrary native admission. The domains here are all `Out` edges/histories, all requests of the existing source-indexed adapter, and every presentation of the declared certified policy family. They are not silently identified with all twelve native rule schemas or all conceivable policies.

No geometry, dimensions, executable edge inverses, or generation of all possible witnesses is assumed. The source's `Vertex` type is used as its existing abstract index type.

## 1. First deliverable: exact obstruction

The requested theorem is proved:

```agda
no-higher-package-admission :
  Resolve Seeds Existing.higher-package-formed → ⊥
```

A further dependency, `research/strominger/agda/HigherWitnessAdmission.agda`, already proves this exact result. The final implementation **reuses** `exact-atomic-path-not-admitted`, rather than retaining a duplicate proof developed during the initial inspection.

Its `atomicSpine` invariant removes leading `paths` constructors and tests whether the resulting constructor is `atom`. Every admitted package has `atomicSpine = false`:

| Derivation case | Why the invariant holds |
|---|---|
| Actual source seed | `pointQ v` has outer `retain` |
| E, Pi | Output has outer E or Pi |
| Comparison, identity, distribution | Output has outer comparison |
| Inverse, composition, path lift, E/Pi congruence | Output has outer retain |
| Reflexivity | Inherits the invariant from its admitted pointed-package premise |
| Higher | Inherits it from an admitted input path package |

But the exact requested expression is

```agda
paths (atom CompleteFiller) sequentialFiller directFiller
```

and has `atomicSpine = true`. This rules out **every** native derivation, including attempts using dependent transport. It is not merely failure to find a preferred derivation tree.

### The precise missing premise

Reflexivity plus ordinary path induction would suffice if we had

```agda
Resolve Seeds (pack (atom CompleteFiller) sequentialFiller)
```

That premise is itself formally impossible under the same invariant. `if-carrier-admitted` proves its conditional sufficiency; `missing-reflexivity-premise` proves its absence.

The existing `higher-rule` is not missing. It takes two admitted path packages and a supplied path between their path values. Its output has code `paths (paths Q x y) p q`, not the requested bare-atom path presentation. Its premises do not manufacture atomic admission.

## 2. Positive admission already available in the source

`HigherWitnessAdmission.agda` also supplies an admitted **E-envelope** recovering the original higher witness exactly. The atomic obstruction must not be misreported as an obstruction to all retained representations.

We reuse:

- `admitted-higher-witness`;
- `path-recovery`;
- `next-higher-derived`, an actual application of the unchanged `higher-rule`;
- the original `RepeatedInterchangeCoherence.filler-coherence` and `native-history-coherence`.

### Complete rule-tree specification for that retained admission

Write `D(b)` for the actual native derivation of a Body. Its recursive tree is exactly:

```text
D(prepared q d reader alignment) = d
D(attach b o) = E-rule(outgoing family, o)
                  every branch: reflexivity-rule(package b)
                                  D(b)
D(compare a b e p ports) = compare-rule(a,b,e,p)
                             D(a)
                             D(b)
D(seedBody v) = seed(source v)
```

For the unchanged earlier two-step diagram, let `a=seedBody A`, `b=seedBody B`, `o1=AB`, `o2=BC`, and let the transported edges be `BA`, `AD`. Its source and target are:

```text
source = compare (attach (attach a AB) BC)
                 (attach (attach b BA) AD)
                 (the existing Second.attachment equivalence and witnesses)
target = attach (attach (compare a b sigmaEquiv refl ports) BA) AD
```

Thus the complete envelope tree is recursively specified, with no extra seed:

```text
Dcompare(f) = compare-rule(source,target,f.e,f.point)
                D(source)
                D(target)
Dbranch(f)  = reflexivity-rule(package(asBody f))
                Dcompare(f)
Denvelope(f) = E-rule(CompleteFiller, branch, f)
                 for every g: Dbranch(g)
Dpath(alpha) = dependent transport of
                 reflexivity-rule(EnvelopeCode, section(f))
                   Denvelope(f)
               along the supplied path alpha : f = g
DnextHigher = higher-rule(EnvelopeCode, section(f), section(g),
                         liftedAlpha, liftedAlpha · refl, rUnit liftedAlpha)
                Dpath(alpha)
                Dpath(with the lifted right-unit path)
```

The transport is the source's existing `PathAdmission.from-derived-point`, implemented by path induction. It is not an extra native constructor. Every branch of E has an explicit derivation function; no enumeration or choice of unknown witnesses is used.

The envelope changes the retained Code presentation. Projection recovers the **actual original higher path**, not just its endpoints. No equality of the envelope Code with the atom Code is claimed.

## 3. Quantified continuation theorem

`WitnessContinuationHistories.agda` fixes the source-compatible selected comparison

```agda
chosen : State exchange A
chosen = cell (seedBody A) (seedBody B)
  (sigmaEquiv , refl , (λ x → refl))
```

This is one concrete comparison from the existing source, not an assumption that every witness is an equivalence.

A `History v t` is any finite composable list of actual `Out` edges. It has no reversibility filter, endpoint selection filter, or bound on length. At each step the operation uses the unchanged `InternalComparisonInterchange.Interchange` to construct the transported comparison and the interchange witness. No new comparison filler is an input to a recursive step.

The finite law is:

```agda
finiteSquare h s :
  Filler stay
    (witness (run h s))
    (runBody (mapHistory m h) (witness s))
```

These are the complete compare-after-continuation and continue-after-comparison presentations. `finite-native` admits their comparison under the unchanged native rules. In particular:

```agda
chosen-universal : (h : History A t) →
  Resolve Seeds (package (witness (squareState h chosen)))
```

The constructed native comparison can itself be the next selected input: `recursively-reusable` quantifies over every subsequent history. `pastingTree` retains actual native composition-rule derivations of the intermediate legs, not merely their endpoints.

### Direct/staged and higher coherence

- `run-append` compares complete direct and staged extension states.
- `higher-pasting` compares the two three-stage pastings by induction, without proof irrelevance of State, Code or Resolve.
- `stagedSquare` actually constructs the staged whole interchange filler, transporting its complete endpoint presentations to the common boundary.
- `chosen-direct-staged` equates it with `finiteSquare` at every history split.
- `chosen-direct-staged-native` is a path between the actual native derivations over that filler path.
- `ChosenHigher` also supplies coherence of higher pastings at these fixed complete boundaries.

The stronger whole-filler equality uses the **proved source reader classification** from `GeneratedReaderClassification`, not endpoint agreement alone. Every history of the chosen witness retains the required faithful reader. No continuation was removed to achieve this.

The same closure proof is supplied for **all** source-adapter requests (`SourceHigher`) and **all** presentations of the producer-certified family (`PolicyHigher`). The compiled producer, guard, control and presentation remain explicit inputs; no new continuation policy is substituted.

The unchanged earlier two-step example is bound back to the quantified theorem by `existing-sequential-agrees` and `existing-direct-agrees`. The latter uses the original `filler-coherence`; it does not reconstruct that theorem.

## 4. Higher witnesses become native next inputs

`WitnessNativeEnvelope.agda` generalizes the existing E-envelope mechanism to any specified family with an explicit native derivation function. Applied to the generated direct/staged filler path, it gives:

```agda
Selected.admitted  : Resolve Seeds Selected.higherQ
Selected.recovered : cong fst (value Selected.higherQ) ≡ Selected.alpha
Selected.continue  : (tail : History (act exchange t) z) →
  Resolve Seeds (package (runBody tail (C.body alpha)))
```

The higher package's continuation reader is **explicitly bound to its existing target boundary**, using that target's reader and alignment. This is a constructed adapter via the existing `prepared` constructor, not an inference of a reader from `Resolve` alone. No assertion of reader faithfulness for arbitrary such prepared packages is made.

`NativeFamily.higher-native` also admits supplied higher paths using the actual native `higher-rule`, with both path-package derivations supplied. This is recursive native reuse of a retained presentation, without adding a primitive or seeds.

## 5. Direction and preservation

`opposite-native` applies the existing inverse-**comparison** rule and retains the original comparison in its output. `oppositeState` carries the reverse reader compatibility; `opposite-full-value` proves recovery of complete values.

A reversed history query retains the original forward history as data. It does not return an executable reverse history. The formal `no-DA` control shows that the source edge AD has no reverse edge DA.

Complete Body values, supplied native derivations, intermediate composition trees and original edge histories are retained. No theorem asserts that all histories with equal endpoints coincide, or that arbitrary Resolve proofs are irrelevant.

## 6. Falsification and the exact hypothesis boundary

The original hidden-fiber obstruction is reused at the level of **complete fillers**. Identity and Boolean swap have equal selected values and port readings but unequal full comparison maps. Therefore their complete fillers cannot be equated.

The new control strengthens this without new seeds: native E rules introduce two Boolean fields above a native reflexivity package. Both identity and swap comparisons are actual native constructions. `no-native-hidden-filler-equality` rejects their equality.

The canonical finite-continuation and staging theorems survive: `hidden-continuations` and `hidden-canonical-pasting` instantiate them on that hidden-field witness. They never equate independently chosen initial fillers.

For an arbitrary pair of independent fillers, one needs their actual complete comparison path. For a blanket theorem comparing **all** fillers in a fixed fiber, `isProp Filler` is the exact necessary-and-sufficient hypothesis. Faithful readers with the proved local sethood are a sufficient source condition, not a minimal necessary condition. In our selected and certified source families that condition is derived; for arbitrary Body/Rule inputs it is false.

There is a second independent limit: `NativeExtensionFamilyAudit.tau-derived` is natively admitted but `tau-breaks-incidence` shows that it does not preserve continuation incidence. Native admission alone therefore cannot supply a universal source router.

## 7. Capability boundary

| Capability | Status under unchanged rules/seeds |
|---|---|
| Exact original atom-coded higher package | **Formally impossible** |
| Original higher witness in its existing retained E-envelope | **Admitted; exact recovery** |
| All declared elementary continuations and finite histories of the selected witness | **Derived and native** |
| Direct/staged complete filler and higher coherence in the selected/certified source families | **Proved using derived reader classification** |
| Native reuse of generated comparisons and retained higher witnesses | **Proved** |
| Opposite comparison/query presentation | **Available; not inverse execution** |
| All independent fillers commute because endpoints/ports agree | **Refuted** |
| Arbitrary native admission implies source-compatible routing | **Refuted** |
| Exact bare-atom admission without changing presentation | Requires a new admission bridge or changed seed policy |

Thus there is a **derived composite generative operation** for the declared interface, including recursive retained admission. There is no unrestricted source-independent primitive guaranteeing every requested behavior, and no need for a stronger primitive merely to reuse these higher witnesses in their admitted retained representation.

## Verification and files

Fresh command:

```text
python research/voevodsky/checkers/check_witness_generator_coherence.py
```

The positive entry freshly checks the complete dependency closure with `--safe --cubical --guardedness --ignore-interfaces`. Three hostile fixtures fail at the intended type mismatch: atomic admission relabelling, hidden-filler equality, and reverse execution. Compiler and source hashes are retained and sources are checked stable during verification.

Receipt: `research/voevodsky/results/witness-generator-coherence-v1.json`.

New modules under `research/voevodsky/agda/`:

- `WitnessHigherAdmissionObstruction.agda` — exact source obstruction and prior admission reuse;
- `WitnessContinuationHistories.agda` — quantified continuation, staging, pasting, history retention and opposite presentations;
- `WitnessHigherControls.agda` — complete-filler coherence, source/certified binding and negative controls;
- `WitnessNativeEnvelope.agda` — quantified native higher admission and reuse.

Verification development included a wrapper timeout and a rejected negative-fixture diagnostic whitelist; the final fresh run passes. These were harness issues, not evidence of an accepted false theorem.

No existing owning module, native rule, seed policy, graph verdict, or independent four-simplex pentagon bridge was changed.
