# Selected Witnessed Steps and Dependent Refinement: A Cubical Agda Tutorial

This tutorial explains a selected-step interface using standard dependent records and displayed constructions. Its value is a worked implementation and comparison, not a new mathematical principle.

## 1. Select a step and retain its witness

Let S:Type ℓ and R:S→S→Type ℓ′. A selected witnessed step is a function

\[
g:\prod_{s:S}\sum_{t:S}R(s,t).
\]

The result contains a successor next(s) and a witness edge(s). The dependent pair lies in Type (ℓ ⊔ ℓ′). The implementation's `Layer1 ℓ` uses the same level ℓ for states and witnesses; we follow that convention below.

The code calls this interface a *Witness Generator* (WG). The name adds no capability to the dependent function: it neither constructs g nor decides whether a witness exists. An arbitrary R need not compose. A history of consecutive selected edges is not automatically a composite witness in R.

Retention is explicit. A result contains earlier evidence only if its type includes that evidence. Dependent records already provide this mechanism.

## 2. Refine states and individual witnesses

A refinement F of a selected-step structure L supplies:

1. an auxiliary source type and a selected source record;
2. an admission family Admit:State→Type ℓ;
3. advancement Admit(s)→Admit(next(s));
4. extra evidence Extra(x,y,r):Type ℓ, indexed by admitted endpoints and an individual base witness r;
5. a certificate of Extra for each selected generated edge.

Compilation forms admitted states (s,p) and witnesses (r,e). The generator advances the state and admission and attaches the extra certificate. A subsequent refinement may inspect e, not just the endpoints.

In the implementation, Source:Type (ℓ+1) is auxiliary retained metadata, not a component of the compiled state or complete-step type. Thus `Refinement L` lives in Type (ℓ+2), while compiled states and witnesses remain in Type ℓ. The Boolean example below uses Source:Type₁ and states/witnesses in Type₀. Pairing source records preserves that separation.

This is a displayed graph with chosen lifts of selected transitions. Compilation is totalization. A chosen lift is not a lift of every base edge: a checked example in the wider library has an alternative edge that cannot be lifted. A general fibration or category interpretation requires additional structure; the category-library bridge explicitly assumes hom-sets.

## 3. Compose refinements and specify what is preserved

Given F:Refinement(L) and G:Refinement(compile(F)), the implementation constructs

\[
F\star G:\operatorname{Refinement}(L).
\]

Admissions are dependent pairs. Over a base edge r, the composite extra evidence is (e,f), where f may depend on r and e. Advancement, certification and source records are paired from the supplied refinements. The leaf refinements are inputs; a finished composite is not.

The comparison between compile(G) and compile(F star G) contains:

- a state isomorphism;
- an isomorphism of complete step types at every source state;
- compatibility with the target projection;
- preservation of the selected generated step.

The complete step type includes both the target and its witness:

\[
\operatorname{Step}_L(x)=\sum_{y:\operatorname{State}_L}\operatorname{Witness}_L(x,y).
\]

Flattening and unflattening dependent tuples give the comparison for every inhabitant of this type, not merely the selected output. Pair projections recover the original source records. `Composite.correct` packages the laws, and `Composer.solve` returns the composite with its certificate. Neither infers compatibility between unrelated specifications.

These are the precise preservation obligations used here. They do not assert semantic naturality beyond the displayed isomorphism fields. The wider artifact also contains units and canonical pentagon/triangle results, but those historical checks were not independently rerun for this tutorial. The comparison below covers two-layer flattening and three-layer reassociation only.

## 4. Work through a proof-dependent example

The base generator flips a Boolean state. The first refinement flips an admitted Boolean p and emits its old value as extra evidence. The second refinement flips another admission and requires the retained first-layer evidence e to equal p. A third refinement checks the same retained value after composition.

This makes proof dependence observable: replacing e=true by false, while retaining the same endpoints and original base witness, leaves an obligation false≡true. Neither implementation may certify it.

The task is to flatten two layers, compare the three-layer groupings, preserve complete steps and selected transitions, and retain the three fixed source records. We compare three implementations:

1. **Hand-written dependent pairs:** explicit state, edge and tuple-reassociation definitions.
2. **WG client:** the same leaf refinements, followed by generic composition, rebasing and associativity.
3. **Library-factored dependent pairs:** Cubical's `Σ-assoc-Iso`, `Σ-cong-iso-snd`, `compIso` and `invIso` replace the hand-written structural maps and inverse proofs.

The third version uses a small additional helper, `totalAssoc`, to lift strict reassociation through an arbitrary dependent result family. It is built from ordinary library isomorphisms and has no WG, source-record or generator premise. It is new glue, not part of the existing Cubical library.

### What the tests establish

| Requirement | Result on the fixed fixture |
| --- | --- |
| State and edge types | Definitionally equal |
| Selected generators | Definitionally equal |
| Forward and inverse full-step comparison maps | Definitionally equal |
| Retained values of the fixed source records | Definitionally equal under the stated pairing |
| Source reassociation | Ordinary pair reassociation |
| Incorrect first-layer payload | Rejected by all three implementations |
| Baseline endpoint and selected-step laws | Explicit reflexivity proofs |

The library comparison's statements and proofs are identical to the hand-written comparison except for module and import names; the checker enforces this equality. All cross-implementation proofs remain `refl`. The maps are quantified over complete edge types, not tested on sampled outputs. Source-value comparisons concern the fixed records, not an arbitrary-source experiment.

### What the interface contributes

WG assembles state/edge families and selected generators from refinement records and packages preservation laws into named certificates. The ordinary library version provides the same reusable structural proof machinery without extra axioms. Thus WG offers an organization and assembly convenience; this example demonstrates neither additional capability nor a nontrivial proof advantage.

That is the lesson of the comparison: retaining witnesses is a dependent-type design choice, while a domain-specific interface can make the choice convenient to reuse. The implementation should not be mistaken for a new construction principle. Detailed source counts and their limitations are in [the comparison report](matched-comparison.md), not used as performance or development-effort evidence.

## 5. Read and run the code

Start with these modules under `research/voevodsky/agda/`:

- `WGRefinementBaseline.agda`: explicit dependent-pair implementation.
- `WGRefinementLibraryBaseline.agda` and `SigmaReassociation.agda`: ordinary library reuse.
- `WGRefinementClient.agda`: the domain-specific client.
- `WGRefinementComparison.agda` and `WGRefinementLibraryComparison.agda`: identical comparison obligations.

Run from the repository root:

```text
python research/voevodsky/checkers/check_wg_refinement_comparison.py
```

The checker uses Agda 2.8.0 and Cubical 0.9 with fresh safe Cubical checking. Set `AGDA` and `CUBICAL_DIR` to override installation paths. Expect two successful compilations and three intended Boolean-mismatch rejections. A failure for another reason does not pass a negative control.

An independent internal review reran these checks in the existing checkout and found the fixed-fixture mathematics correct and useful for tutorial/library documentation. That was not a clean-checkout test or a recheck of the wider coherence library. The existing `TypedGeneratorLayers` import warning about `isPropIsContr` remains. Exact commands, hashes and logs are documented in [the comparison report](matched-comparison.md).

## Foundations

Dependent records and sections are standard type-theoretic constructions [Voe14, pp. 3–4]. Displayed totalization and dependent-sum composition, including second-layer dependence on first-layer morphism witnesses, are explicit in [AL19, Definitions 3.2 and 3.17]. Cubical's dependent-sum isomorphisms supply the structural operations used by the baseline.

- Ahrens, B., and Lumsdaine, P. LeF. *Displayed Categories*. Logical Methods in Computer Science 15(1), article 20 (2019). DOI: 10.23638/LMCS-15(1:20)2019.
- Voevodsky, V. *An experimental library of formalized Mathematics based on the univalent foundations*. arXiv:1401.0053.
- Cubical Agda library, version 0.9: `Cubical/Data/Sigma/Properties.agda` and `Cubical/Categories/Displayed/Constructions/TotalCategory.agda`.
