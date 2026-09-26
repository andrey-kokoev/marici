# Full constructor and retained-resolution equivalence with recursive tables

## Result

The typed recursive table completion now covers **all eight** `WholePackageSigmaPi.Code` forms and **all twelve** `WholePackageResolution.Rule` schemas. Its operations are implemented on native tables. The actual imported retained-resolution closure is equivalent to the native closure, for arbitrary original source policies, with both inverse laws and a commuting endpoint map.

This advances the earlier [E/P-stage result](recursive-constructor-tables.md) and removes the old `Code` annotation used by the [annotated bridge](fibration-constructor-equivalence.md). The independently constructed native NAND also matches the actual old NAND constructor and operation by `refl`; its Wolfram result is double negation generally, and `C` under the existing stable-proposition assumptions.

Fresh safe/cubical compilation, six intended rejection controls, the source-bound finite checker, and the SCC check pass. These are formal/implementation verification controls, not new scientific evidence. Independent review has not yet been established.

## 1. The recursive table construction

[`IndexedConstructorTables.agda`](agda/IndexedConstructorTables.agda) has one generic recursive constructor:

```agda
table-node : (h : Header)
  → ((i : Arity h) → Node (Inputs h i))
  → Node (Result h)
```

A declaration records the constructor kind, active port domain, expected attachment carriers, and required actual witness data. Each child row attaches a recursive table at its declared port. The index enforces compatibility of that child's carrier with the declaration. The eight familiar constructor names are smart constructors for this one table constructor.

The canonical three columns are:

| label | from | to |
| --- | --- | --- |
| declaration, including active domain and typed witness attachments | local root | declaration port |
| recursive child table | local root | argument port |

Declarations survive empty child domains. In particular, an empty product and a product with a declared empty-valued fiber remain different constructions.

`row-data-iso` identifies a native graph with exactly its declaration and typed family of child rows; both inverse laws are `refl`. `kernel-table` instantiates the actual `TableFibrationCycle.Table`. Endpoint uniqueness and four-step table-data recovery are checked. A complete package has a two-row envelope containing its code table and actual typed selected value (`package-table`).

This is an intrinsic, well-typed canonical table format. Arbitrary malformed raw tables are not silently admitted. Types, indices, functions, equivalences and source witnesses remain supplied parameters, exactly as in the baseline. Supplied atoms may themselves be structured data; this construction does not claim to synthesize arbitrary atoms or finitely serialize arbitrary functions.

## 2. All eight code forms, values and witnesses

The covered forms are atom, E, Pi, paths, maps, equivalences, retain and comparison.

No original `Code` is a required field of the native node, declaration or child row. Only the decoder/proof section uses:

```agda
At A = Σ Old.Code (λ c → Old.El c ≡ A)
```

Keeping decoded code and its carrier path together makes dependent path endpoints, retained values and equivalence attachments coherent. `backfill`, `equiv-backfill` and the `quote-*` lemmas supply the corresponding typed compatibility witnesses.

Checked results:

- `fiber-iso : Iso (At A) (Node A)`;
- `syntax-iso : Iso Old.Code Graph`;
- `complete-equivalence : Old.Complete ≃ Package`;
- `selected-unchanged = refl`.

The inverse laws cover every constructor. The forward map keeps the value's type and selected value definitionally unchanged. It preserves code data as well as values; it does not identify maps with atoms of function type or replace witness attachments by truth of existence.

## 3. All twelve native rule operations

[`NativeTableRules.agda`](agda/NativeTableRules.agda) independently defines native E/P packages, retention, comparison, identity, inverse, composition, higher paths, reflexivity, path lifting, distribution and the two congruence operations. These definitions do not decode through the old system to perform their work.

A native rule is a tag with typed native parameters. Those parameters retain full input packages and actual equivalences/compatibility paths, including unselected E inputs. Its `Arity`, `input` and `output` are independently defined.

The proof section compares these implementations with the actual imported rules:

\[
E_R : \mathrm{OldRule} \simeq \mathrm{NativeRule}.
\]

For every rule there is a port equivalence, and both marked boundary equations hold:

\[
E_Q(\mathrm{input}(r,i))
=
\mathrm{nativeInput}(E_R(r),E_{\mathrm{ports}}(i)),
\]

\[
E_Q(\mathrm{output}(r))
=
\mathrm{nativeOutput}(E_R(r)).
\]

`parameters-equivalence` preserves all twelve parameter spaces, not just a chosen output. All input equations and eleven output cases are `refl`. Distribution uses an explicit equality of equivalences with the same underlying function; its `isEquiv` fields agree propositionally. No actual compatibility-path witness is truncated.

## 4. Retained derivations and original source policies

[`IndexedResolutionTransport.agda`](agda/IndexedResolutionTransport.agda) defines a generic indexed derivation datatype with literal and application constructors. Its transfer theorem takes equivalences of states, rules, ports and seed families, together with the actual input/output compatibility witnesses.

Univalence and equivalence induction yield an equivalence of retained closures **and** a commuting endpoint map. They compare independently instantiated signatures; they do not define the target operations by transporting old operations.

[`NativeTableResolution.agda`](agda/NativeTableResolution.agda) instantiates the target datatype using native packages, native rules and their independently implemented operations. Native derivation tables retain the literal source certificate or the complete native application declaration, and every child derivation.

The proof then identifies the generic source datatype with the actual imported `WholePackageResolution.Resolve`, by structural maps and both inverse laws. Combining the results gives:

\[
\sum_q \mathrm{OldResolve}(S,q)
\simeq
\sum_t \mathrm{NativeResolve}(S\circ E_Q^{-1},t).
\]

`ForOldSeeds` covers every original source family `S`. The admission interface is transported along the complete-package equivalence; no new admission authority is invented. The main construction also accepts arbitrary independently supplied native admission families.

The forward derivation map satisfies:

\[
\mathrm{fst}(E_D(q,d))=E_Q(q).
\]

Both inverse laws recover the retained derivations, including supplied witness data, up to the type theory's equality. Equal outputs do not erase distinct source certificates. Empty admission still permits a zero-arity Pi application without any literal seed.

`readout-commutes` exposes the remaining interface precisely: an independently specified native readout must be compared with the original readout on encoded packages. Such a comparison then commutes on translated derivations. The exact finite tidal fixture below instantiates an independent projection; no continuum readout-completion theorem is inferred from the generic equivalence.

## 5. Actual comparison and Boolean interfaces

[`NativeTableRegression.agda`](agda/NativeTableRegression.agda) imports `BoundaryGeneratedQuestions.Filler` itself. At encoded marked boundaries its equivalence with the native filler space is the identity equivalence. Composition compatibility is `refl`. The supplied equivalence and compatibility path remain actual data.

The native NAND table is built independently from native E and P tables. Its decoded constructor matches `NandConstructions.nandCode` by `refl`; its value operation matches `QBooleanity.N` by `refl`. The actual imported Wolfram results apply:

- double negation of `C` for arbitrary `A`, `B`, `C`;
- equivalence with `C` under `isProp C` and `Stable C`.

This is the typed completion of the table construction. E uses total values; Pi uses sections. Opposite-endpoint grouping alone does not supply Pi, and the four-step table-data equality does not erase retained derivations.

## 6. Existing tidal routes: independent finite readout

Voevodsky's interface reply identifies the actual `NewtonianTidalRoutes` packages and comparison, and requires retention of second-derivative data. [`NativeTidalTableReadout.agda`](agda/NativeTidalTableReadout.agda) implements an exact second jet as thirteen labelled integer rows: scalar, three gradient entries and nine Hessian entries. Its constant/add/scale/product operations and inverse-radius polynomial are independently implemented on those rows. The tensor readout directly selects the second-derivative rows; it does not call an old-code decoder or the old jet evaluator.

All nine components agree with the actual `potentialTotal8 a b` route by `refl`. The full tensor also agrees with `geometric8` through the existing `routeAgreement`; an independently written direct geometric numerator agrees by `refl`. Both use the same denominator `8 * denominator`, retaining route and source metadata. Integer scaling is not asserted to be an equivalence of all integer tensors.

The native packages are compared with the actual `adPackage` and `directPackage`; the actual comparison rule commutes. The original full retained `history`, including its source evidence package, instantiates the native closure equivalence and its recovery law.

The hostile first-jet-only control has equal scalar and gradient data but unequal Hessian entries. `no-first-jet-factor` proves that no function of the first jet alone recovers the Hessian of every exact jet. The corresponding attempted equality is an intended compiler rejection.

The owner construction here supplies **finite exact second-jet data**, not a declared continuum topology or limiting completion. Voevodsky's separate [second-jet completion analysis](../voevodsky/tidal-readout-needs-second-jet-completion.md) distinguishes first-order metric convergence from a controlled second-order readout extension. Those analytic completion hypotheses are not consequences of generic encode/decode transport and are not newly proved here.

## Verification and scope

Run:

```powershell
pwsh -NoProfile -File research/nima/checkers/check_native_table_equivalence.ps1
python research/nima/checkers/check_native_table_equivalence.py
python research/aspect/scc/scc.py check nima-native-table-equivalence
```

The fresh compiler root is `NativeTableRegression`. It checks the full code/rule/closure chain. Six negative modules must reject precisely: wrong attachment carrier, constructor erasure, marked filler erasure, source-certificate erasure, retained-input erasure and first-jet-only Hessian recovery.

The finite checker exercises 335 eight-form code roundtrips, 1,804 value-package roundtrips, twelve rule-parameter codecs, empty-domain/wrong-attachment controls, actual distinct filler payloads and 64 Boolean controls. It independently interprets native row schemas without decoding them to old code. General operation and retained-closure correctness are supplied by the source-bound Agda proofs, not inferred from those finite examples.

Receipts:

- [fresh formal closure](results/agda-NativeTableRegression.json);
- [formal rejection audit](results/native-table-formal-audit.json);
- [source-bound result](results/native-table-equivalence.json);
- [SCC model](scc-models/native-table-equivalence.json).

The established equivalence is for the original eight-constructor/twelve-rule system and this typed well-founded recursive table completion, including potentially infinite branching. It does not cover arbitrary malformed tables, arbitrary cyclic graph syntax, or generation of arbitrary supplied types/functions from regrouping alone. The existing finite exact tidal calculation has an independently checked native readout. No continuum topology/completion, new physical realization or empirical claim is added.
