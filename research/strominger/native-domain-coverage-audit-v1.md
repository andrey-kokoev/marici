# Native admission and coverage: audit and checked composition

## Changed conclusion

The recovery premise of the common representation theorem is **already discharged for every retained derivation of the named native WG grammar**, under an arbitrary original source policy S. It is not an additional open question inside that scope.

A new composition module, `research/nima/agda/NativeResolvedDomainRepresentation.agda`, binds the existing native-table closure equivalence directly to `RetainedDomainRepresentation`. Fresh safe Cubical compilation passes with ignored interfaces.

## Exact theorem

For any universe level and source policy

    S : Complete -> Type,
    Domain = Sigma q. Resolve S q,

and three declared focus maps on the native retained-table representation, the construction gives

    encode : Domain -> TriangleRecord,
    decode : TriangleRecord -> Domain,
    decode(encode(d)) = d.

It recovers the **whole dependent pair**, not merely the final value: the endpoint package, source certificate, retained premise derivations and rule parameters remain part of the recovered object. Endpoint recovery and preservation of arbitrary declared observations follow. Decode/apply/encode operations compose; this does not claim an independent native implementation of each supplied operation.

`reified-history-recovered` also checks that the existing next-universe `reify-history` carries exactly the original domain pair. The universe increase is explicit.

No new universal seed policy is introduced. No target history is supplied merely because the encoder can accept it: the theorem consumes an actual `Resolve S q` derivation.

## Sources audited

| Existing source | What it supplies | What it does not supply |
| --- | --- | --- |
| `WholePackageSigmaPi.Code.atom`, `pack` | A type/value package for supplied data | Admission of that package under a particular S |
| `WholePackageResolution.Resolve` | Actual seed certificates or rule applications with every premise; potentially infinite dependent branching, well-founded histories | Automatic synthesis of arbitrary parameters or fillers |
| `WholePackageResolution.reify-history` | Whole actual retained derivation at the next universe | Assertion that every arbitrary package is generated |
| `NativeTableResolution.ForOldSeeds.closure-equivalence` | Full original/native retained-closure equivalence for every S; endpoint compatibility | Expansion of the original admission policy or arbitrary cyclic graph syntax |
| `NativeTableRules` and `native-table-equivalence.md` | All eight constructor forms and twelve rule schemas of this signature, with actual parameter and boundary compatibility | Exhaustion of every repository sector adapter or every possible WG signature |
| `generating-grammar/NATIVE-CORE.md` | Explicit distinction between syntax, supplied headers, literal admission and rule premises | An implicit fallback admitting arbitrary packages |
| Voevodsky's `stagewise-mathematical-interface-v1.md` | General witnessed-edge payload movement, retained histories and explicit supplied-law interfaces | Derivation of a supplied physical compute law merely by wrapping it |

The last report's open downstream reviews are not treated as a current global frontier. The operative audit conclusion comes from the inspected definitions and the freshly compiled composition.

Empty source admission is not the same as empty closure: a zero-arity Pi rule can still apply. Conversely, arbitrary atom formation is not seed admission. These two distinctions prevent an incorrect yes/no answer based only on whether S has members.

## Coverage remaining outside the theorem

For a physical model presented by an actual native derivation, the table/triangle representation now follows without an extra recovery assumption. The remaining bridge is identification of the desired physical-domain structure with such an admitted derivation, or with another explicitly declared WG signature carrying equivalent recovery machinery.

The native signature is not all WG by definition: the existing family-promotion adapters and sector constructions have their own source contracts. Their successful Python domain examples do not automatically become derivations of these twelve rules. Nor does this audit prove that no broader coverage theorem exists elsewhere; it establishes the exact reusable native theorem rather than treating its coverage as missing.

The governing all-laws conjecture therefore remains open, with the internal native representation portion now formalized. Do not repeat that proof or rename it as a new admission gate.

## Verification

    pwsh -NoProfile -File research/nima/checkers/check_cubical_agda.ps1 -Module NativeResolvedDomainRepresentation -Fresh

Exit zero, execution `structured_command_execution:e_42200_1792522412166996700_48`. Receipt and dependency inventory: `research/nima/results/agda-NativeResolvedDomainRepresentation.json`; log beside it. The command freshly checks the native-table/retained-resolution dependency chain and the cone/triangle chain together. This is formal verification at the declared source scope, not empirical validation or a universal physical-domain theorem.
