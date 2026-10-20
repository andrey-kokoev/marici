# Actual forward source lift: binary composition proved

Owner: `marici.Strominger`. Net node: **`forward-lift-binary-composition`**, constructed at the scope below.

- [Current conjecture net](contracts/wg-source-determination-conjecture-net.v1.json)
- [Formal source](agda/ForwardSourceLiftComposition.agda)
- [Fresh verification](results/forward-source-lift-composition/verification.json)
- [Dependency manifest](results/forward-source-lift-composition/dependency-manifest.json)

## New theorem

For the **existing** `RetainedFeedbackCovariance.moveInitial` and `move`, forward transport agrees propositionally with the previously constructed backward transport. Consequently forward transport twice returns:

1. Every actual `Resolve Seeds (pointQ v)` input, with the dependent endpoint correction `sigma² v`.
2. Every retained finite `Chain`, including its arbitrary initial native derivation and all edge witnesses.
3. The complete native `Closure` interpreted from that chain, including the derivation, not just the selected value.

No seeds, constructor schemas, existing source files or chosen `pointPath` definitions were changed. Cancellation is a proved path, **not judgmental equality**, a fresh seed lookup, or proof irrelevance of native histories.

This discharges the formerly missing **binary forward-square law**. It does not by itself complete a coherent group action or bind the law to every `Body` comparison presentation.

## Why the path comparison exists

The graph provenance in `pointPath` stays fixed while its pointed vertex carrier travels along `ua sigmaEquiv`.

1. `sigma-inverse : sigmaEquiv ≡ invEquiv sigmaEquiv` follows from equality of the actual underlying functions via `equivEq`.
2. `ua-inverse` combines this with Cubical's `uaInvEquiv`, comparing the actual type path with its inverse.
3. `pointed-inverse` fills the dependent selected-point square over that type-path comparison. The fibers are propositional because **Vertex is a set**; `isOfHLevelPathP'` supplies exactly that local fact.
4. Applying the original `remember graphQ (pack (atom _) _)` presentation gives equality of the full pointed package paths.
5. Congruence of `subst (Resolve Seeds)` yields `forward-back-initial` for an arbitrary derivation `d`. No pattern matching on the derivation is required.
6. The existing backward/forward inverse law now yields `forward-square-initial`. Structural recursion gives `forward-back-chain`, and `forward-square` follows on `Total`.

The proof uses ordinary univalence, equivalence extensionality, dependent path uniqueness over a set carrier, and transport congruence. It does **not** assert sethood of `Code`, `Complete`, `Resolve`, or the space of retained histories.

## Exported composition laws

`action stay` is the identity on the chain adapter's `Total`; `action exchange` is precisely the existing `R.move`. With the explicit two-mode product:

```text
composition-law m n c :
  action m (action n c) = action (product m n) c
```

All four binary cases are proved. `native-composition-law` applies the actual `closure` interpreter to this path. `involutiveEquiv` uses forward transport as its own inverse and is proved equal to the previous `wholeEquiv` as an equivalence, without erasing the separately recorded backward implementation.

`two-attachment-forward-square` and `two-attachment-native-square` apply cancellation after two actual dependent attachments. They quantify over the arbitrary preceding chain and both appropriately indexed edge witnesses. These are **Chain/closure** theorems, not yet the forward/forward binding of the separate `Body` interchange implementation.

A single exchange is still provably nonidentity (`exchange-not-identity`). Binary cancellation does not make every comparison trivial.

### Ready normalization boundary

The proved law is

```text
moveReady (moveReady r) = encode (decode r).
```

It recovers the canonical presentation of the decoded retained history. The present proof does not identify all arbitrary Ready admission paths or establish the stronger equality with `r`. The negative control rejects directly substituting this normalization theorem for that stronger statement; it is **not** an impossibility theorem about a future Ready equivalence proof.

## Exact remaining higher boundary

The module declares, but does not inhabit:

```text
TripleExchangeOverlap =
  (c : Total) ->
    forward-square (move c) = cong move (forward-square c).
```

Both sides compare three forward exchanges with one forward exchange. A coherent action must compare these **chosen binary-law witnesses**, not merely check associativity of the two-element mode table. Further unit/overlap coherences and general induction remain their own obligations. A declared boundary or failed `refl` is not a mathematical obstruction to filling it.

## Parameter origins and source boundaries

- Incidence, four endpoint seeds, task policy and native rule signature are unchanged supplied inputs.
- The existing `ua sigmaEquiv`/`ua-gluePath` package path is reused, not replaced by a better-behaved lift.
- The inverse comparison and dependent point square are constructed from the fixed involutive source equivalence and the proved local sethood of Vertex.
- `d` remains an arbitrary actual initial native derivation throughout.
- The newly declared two-mode `Total` action records its interpretation explicitly. It does not identify the syntax of a stay-comparison `Body` with an unchanged history.
- No parameter-program completeness, policy uniqueness, topology-changing attachment or physical interpretation follows.

## Verification

```sh
python research/strominger/checkers/check_forward_source_lift_composition.py
```

Fresh safe Cubical headless closure passes with `--ignore-interfaces` and explicit include roots. The receipt records the compiler/version, command, exits, full logs, source hashes and a conservative **1,823-file** source/library/primitive inventory. The inventory covers the declared include roots; it is not an exact import graph or a claim that every inventoried file compiled. Inputs are checked unchanged over the run.

Three intended negative modules fail with `UnequalTerms`:

- replacing propositional forward-square cancellation by `refl`;
- replacing arbitrary transported input proof data by `root B` using `refl`;
- using the Ready normalization result as equality with the arbitrary original Ready value.

Cubical dependency indexed-match warnings, normally suppressed by library configuration, are recorded explicitly. Repository sources have no warnings. Finite mode/edge checks are only regression controls; the unbounded history statements are the Agda theorems.

## Net update and next work

The net preserves the earlier inverse-facing two-comparison control and adds this binary-lift theorem as a separate constructed node. The larger `source-comparison-composition` node remains open specifically at the chosen higher-overlap boundary. No prior scoped claim is silently broadened.

**Recommended next task: `two-comparisons-two-attachments`.** Bind the actual forward-lifted native histories into the `Body` diagram using the new law. Do not substitute fresh endpoint seeds or infer equality between the `Chain` and `Body` interfaces without an adapter. The previous inverse-facing result is reusable evidence, not that binding itself.
