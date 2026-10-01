# Marici generating grammar

## Governing source and current result

The implemented native grammar is **[NATIVE-CORE.md](NATIVE-CORE.md)**, generated
from **[native-core.json](native-core.json)**. Its authoritative definitions are
`IndexedConstructorTables.agda`, `NativeTableRules.agda` and
`IndexedResolutionTransport.agda`; this register transcribes and checks them.

The source contains one typed node constructor with eight header forms, twelve
rule schemas, and two retained-derivation constructors (`seed`, `apply`). The
existing `NativeTableResolution` equivalence covers every legacy constructor,
rule and retained derivation for arbitrary original admission policies. This is
an actual generating grammar with a structural exhaustion criterion, not a list
of representative examples. Potentially infinite premise domains are permitted.

The first registry revision missed this already implemented core. Its
[operation table](TABLE.md) is now explicitly a supplementary experimental/policy
catalogue, not the governing grammar. In particular PP/SP/PS is not promoted to
an exhaustive account of native operations.

## What is complete, and what is not

| Boundary | Evidence / remaining work |
|---|---|
| Native Header, Node, Kind, Resolve declarations | Exhaustive source census: 8 headers, 1 node constructor, 12 rule schemas, 2 derivation constructors |
| Legacy syntax/rules/retained closure to native core | Existing equivalence and inverse laws; fresh safe/cubical NativeTableRegression compilation and six intended compiler rejections |
| Amplitude Expr to native Resolve | All four expression forms mapped; `native-run` recurses on expressions; binary uses P-kind with operator/left/right ports |
| Natural component arithmetic | All 25 named definitions classified; recursive equations and native expression bridge recorded; fresh safe/cubical bridge compilation and two compiler rejections pass |
| Retained-path ledger | All 33 defined functions/methods classified, including guards and private support; computational rules and finite exact tests pass; native Resolve operational interpretation remains open |
| Signed/rational arithmetic | 114 public definitions across five completion/bridge files censused; source-bound formal receipts and four intended compiler rejections checked |
| Native family/pair macros | Nine public definitions; fresh compilation and intended missing-operand rejection pass; supplied packages AND premise derivations recovered |
| Nine-row comparison-successor policy contract | Every row assessed in `COMPLETIONS-AND-POLICIES.md`; retention/pairing macros implemented, full operational interpretations remain open |
| All sector operations in Marici | No authoritative global admission/coverage theorem established |
| Generation from the intended structured S4 object | Source signature and derivations remain open; supplying arbitrary atoms or witnesses is not counted as deriving them |

The global objective remains **in progress**. Core exhaustion does not establish
repository-wide exhaustion. Equality is the source type theory's equality of
full packages and derivations, not equality of scalar outputs. No decidable
normal-form algorithm for arbitrary supplied functions or higher witnesses is
claimed.

## Maintenance

- `native-core.json`: source locators, exhaustive native forms, dependent premise
  conditions, literal/application rules, coverage witnesses and established
  expression interpretation. Edit this to update the core transcription.
- `semantic-extensions.json`: exhaustive definition classification and source
  equations for retained-path computation and natural component arithmetic;
  generated view `SEMANTIC-EXTENSIONS.md` and receipt
  `semantic-extensions-verification.json`.
- `completions-and-policies.json`: exhaustive arithmetic/macro public-definition
  census and nine policy assessments; generated view `COMPLETIONS-AND-POLICIES.md`
  and receipt `completion-verification.json`. Assessments are not derivations.
- `registry.json`: stable supplementary operation IDs, assumptions, dependencies,
  coverage of the policy ledger, and unsupported families. Its `native_core`
  field fixes the governing manifest.
- `NATIVE-CORE.md` and `TABLE.md`: generated human-readable views; do not edit.
- `native-core-verification.json` and `verification.json`: source hashes,
  validation boundaries and rejection-test receipts.

For changes, retain stable IDs, increment the owning manifest revision, cite the
source declaration and record assumptions rather than inserting them silently.
Schema changes require corresponding checker changes. A newly discovered family
must be interpreted into the grammar or retained as an explicit coverage gap.
Never admit an arbitrary desired output as a seed to manufacture a derivation.

Run through the repository structured-command surface:

```text
python research/nima/checkers/check_generating_grammar.py --write --self-test --require-formal
python research/nima/checkers/check_generating_grammar.py --self-test --require-formal
python research/nima/checkers/check_grammar_completion.py --write --self-test --require-formal
```

The integrated command checks all four manifests/views and writes the aggregate
`verification.json` with `--write`. Without `--write` it rejects stale views;
formal evidence checks may refresh their underlying arithmetic receipts but do
not recompile Agda. The completion checker requires formal receipts by default
(use `--metadata-only` for isolated census work). Native census checks all
source datatype alternatives, legacy/native tag correspondence, and the
Parameters/Arity/input/output clause domains. These checks do not typecheck the
manifest's explanatory prose. Agda checks the actual source definitions.

Fresh formal reproduction:

```text
pwsh -NoProfile -File research/nima/checkers/check_native_grammar_formal.ps1
pwsh -NoProfile -File research/nima/checkers/check_native_component_arithmetic.ps1 -Fresh
pwsh -NoProfile -File research/nima/checkers/check_completed_component_arithmetic.ps1
pwsh -NoProfile -File research/nima/checkers/check_generating_grammar_macros.ps1
```

This wrapper uses the existing native-table formal checker. It repairs executable
discovery in a child process only and avoids reporting the final *expected*
negative-test exit code as an overall failure. The existing receipts identify the
compiled root, source hashes and six rejected modules. Underlying admission,
functions and witnesses remain explicit parameters.

## Related exploratory proposal

[Reversible trivalent coherence calculus](../reversible-trivalent-coherence-calculus-proposal.md)
records the operator-supplied structural proposal, its non-assumptions, open
graph conventions and a small-diagram enumeration plan. It is not the frozen
source signature or a checked replacement for this grammar. No interpretation
from that calculus to the current grammar or conditional DG model is proved.

## Next executable work

1. Construct a generation-preserving typed interpretation of the DG comparison
   computation, including its weak-return correction, under a frozen admission
   policy. The checked pairing macro retains supplied operands; it does not
   compute that comparison or provide missing operands.
2. Interpret retained-path computation operationally in the native grammar,
   preserving the distinction between reversible retained packages and their
   noninvertible readouts. The existing obstruction concerns the ambient decoder,
   not the reversible parent/detail interface.
3. Establish the admitted source boundary for repository-wide coverage without
   declaring arbitrary supplied results to be generated literals. The source
   censuses are complete only for their explicitly named files.

These are implementation-backed continuations, not requests to invent another
abstract completion criterion.

## Retracted iterations 5–6

Material added in iterations 5–6 was found on examination to contain
substantive errors:

- The S₄ source signature was promoted from `unresolved` to `frozen` without
  an authorised typed signature or a substantial checker. The promotion has
  been retracted; the registry status is again `unresolved`.
- The operational interpretation sketches for split/reassemble and composition
  erroneously used P-kind (dependent product) in roles that required
  dependent sums, tensor products or other constructions. The sketches have
  been removed.
- The repository coverage survey classified models from names alone and
  referenced a nonexistent native `reference-kind`. It has been removed.

These items were deleted or reverted, not retained as drafts. The previously
checked native core, arithmetic and macro receipts remain valid at their
stated boundaries.

## Change record

- Revision 25 (repair iteration 10): fresh `InterpretationRegression.agda`
  aggregate check passes (known dependency import warning remains). Checker
  receipts now bind before/after-stable local and full Cubical source inventories
  and compiler hash. The dependency audit rejects stale/failed/non-fresh receipts
  and checks the aggregate external inventory; rejection self-tests added.
  Audit passes for 13 roots, 40 local sources and 1091 Cubical source files.
  Compiler built-in data and semantic derivability remain outside this audit.
  Concrete endpoint-typed DG instantiation, native output derivations and source
  signature freeze are still open; ten iterations do not establish completion.
- Revision 24 (repair iteration 9): `DGHistoryEditPolicy.agda` freshly checks
  retained permission/cost certificates around the DG exact edit. Unit and
  triangle equations come from the derived edit, not fresh policy assumptions.
  Readouts of C,d,r,u are proved invariant; arbitrary readouts require an
  explicit witness. Parent Resolve derivation and computed result are retained,
  without manufacturing a Resolve derivation for the output. Dependency audit
  includes the twelfth root. Concrete endpoint typing and native bridge remain.
- Revision 23 (repair iteration 8): `DGActionInverse.agda` freshly checks an
  admitted inverse request and recovery of all six stored frame components,
  including W, after forward/inverse execution. Proof-field equality is not
  asserted. The dependency audit now has 11 roots and explicitly records
  InverseAlgebra's unit-action, negation-action and additive cancellation laws.
  Concrete typed-endpoint DG instantiation and policy/native integration remain.
- Revision 22 (repair iteration 7): `DGActionComposition.agda` freshly checks
  construction of a composite admitted request and equality of sequential and
  direct C,d,r,u,v,W components, including triangle-witness data W. Equality
  of Frame proof fields is not assumed. The local dependency audit now includes
  this tenth root and records the additional ActionAlgebra assumptions. Concrete
  typed-endpoint instantiation, inverse full-action recovery, policy integration
  and native bridge remain open.
- Revision 21 (repair iteration 6): reproducible local dependency audit added
  in `check_interpretation_dependencies.py`; 9 roots, 36 local sources and 25
  external import boundaries. All 9 root receipts match their local source
  closure and record fresh checking. `S4Aut` now checks with --safe; both it
  and `RelationalCarrier` were freshly checked. The latter has a dependency
  import warning. Corrected S4 draft arrows and unsupported cardinality/proof
  multiplicity claims. External library closure and semantic signature audit
  are explicitly not certified; source signature remains unresolved.
- Revision 20 (repair iteration 5): `DGCertificateTransport.agda` freshly
  checks the certificate boundary laws for K_hg=h*K_g+K_h*g and
  K_inverse=-g_inverse*K_g*g_inverse. Additional assumptions are explicit
  differential-negation, negated-subtraction and identity-action laws.
  This does not yet prove sequential/direct full-frame equality, provide
  a concrete DG instance, or close the native Resolve/policy/audit gaps.
- Revision 19 (repair iteration 4): `DGFrameUpdates.agda` freshly checks full
  common-carrier frame updates C'=gC, d'=gd, r'=r g^-1, W'=gW+Kd, with u,v
  fixed. Both unit equations are derived using inverse and admission laws;
  triangle preservation uses revision 18. Exact edits now construct valid full
  frames too. This is conditional algebra, not a concrete typed-endpoint DG
  instance or a native Resolve bridge. Certificate composition/inversion,
  execution permissions/readouts and dependency audit remain open.
- Revision 18 (repair iteration 3): `DGHistoryTransport.agda` freshly checks
  noncommutative active-triangle transport W'=gW+Kd and exact history-edit
  preservation v'=v+delta(Z), W'=W-Zd. The latter preserves delta(v) and the
  triangle boundary. Proofs are conditional on an explicit homogeneous DG
  fragment, not on the desired updated boundary. Concrete DG instantiation,
  endpoint typing, full frame unit updates, certificate composition/inversion,
  native Resolve bridge and dependency audit remain open.
- Revision 17 (repair iteration 2): `HistoryPathEdits.agda` freshly checks a
  supplied-path edit policy. Readouts are preserved by congruence; dependent
  invariants are transported with a PathP coherence witness. A compare-rule
  derivation and a next-universe certificate retain both endpoint derivations,
  permission and cost. This is not yet an instantiation of DG exact edits or
  unit/triangle equations; the registry remains partial for history.edit.
- Revision 16 (repair iteration 1): `OperandPairInterpretation.agda` freshly
  checks supplied-operand pairing in the original Resolve layer via Pi-rule,
  both value projections, assemble/unpack round trips, and recovery of both
  actual premise derivations. This matches the existing native Pi pairing in
  `GeneratingGrammarMacros.agda`; independent preparation is not claimed.
  Full DG frame updates, history-edit preservation and dependency audit remain.
- Revision 15: retract full-contract coverage claims from revision 12. The four
  additions are partial checked rule applications, not complete interpretations.
  Six additional registered sources have unverified native-rule bridges.
  `PathLedgerInterpretations.agda` now checks only readout agreement and
  pointwise naturality; unsupported payload composition and dummy split spaces
  were removed. All three gaps remain open. Operator approval to continue the
  signature audit has been received; freezing still requires technical evidence.
- 2026-10-01, revision 12: added four compiling rule applications in
  `RemainingInterpretations.agda`. The original claim of complete coverage of
  all nine contracts was incorrect (see revision 15).
- 2026-10-01, revision 11: coverage boundary documented
  (`coverage-boundary.md`): three manifest scopes + 5 checked Agda contract
  interpretations.  Gap `gap.global_coverage` narrowed: what is covered, what is
  out of scope, and what remains uncovered are now stated with an authoritative
  principle.
- 2026-10-01, revision 10: three more contract interpretations checked:
  reference.substitute (compose-rule + identity-rule), record.reindex
  (Pi-congruence-rule), family.admit (Pi-congruence-rule).
  `research/nima/agda/ContractInterpretations.agda` compiles.
- 2026-10-01, revision 9: checked Agda interpretation of passive frame change
  (frame.passive) as a native compare-rule application
  (`research/nima/agda/PassiveFrameTransport.agda`).
- 2026-10-01, revision 4: 123 public completion/macro definitions and nine policy
  assessments checked; family/pair native macros freshly compiled with intended
  missing-operand rejection. Integrated validator checks all four views and
  source-bound formal receipts. Retired the optional PP/SP/PS identification and
  equality-decision requirements: neither is required for a generating grammar.
- 2026-10-01, revision 3: exhaustive path (33 definitions) and natural arithmetic
  (25 definitions) census; exact path execution controls; fresh native natural
  arithmetic bridge compilation; noninjective averaging witness. Existing
  signed/rational completion located and recorded as the next census boundary.
- 2026-10-01, revision 2: recovered the existing complete native 8/12/2 grammar;
  added exhaustive declaration/implementation-clause census, eight hostile census
  controls, source-bound formal evidence and the expression interpretation.
  Downgraded the original flat table to a supplementary catalogue.
- 2026-10-01, revision 1: operator-requested maintenance locus and partial policy
  inventory. Graph proposal `ep_cc841b35-7404-4b23-8612-e8ca2ddabae2` records that
  initial instruction and report. The initial inventory was not a completed grammar.

## Iteration 7 verification record

Iterations 5–6 added unverified drafts and incorrectly promoted the S₄ source
signature to `frozen`. Retraction: the S₄ working draft at
`research/nima/s4-working-draft.md` now accurately documents the three layers
of S4 formalization (S4Aut.Iso Point Point, BoundaryGeneratedQuestions.Filler,
RelationalCarrier.Aut) as a draft for discussion, not a frozen interface.
`source_basis.status` remains `unresolved`. The validator again enforces that
no promotion to any other value is accepted.

A verified existing operational interpretation was recorded:
`BoundaryGeneratedQuestions.Application.perform` interprets a `Filler a b` as
a native `compare-rule` application. This is checked Agda code, not a new sketch.

All three gaps remain open; no unsupported claims have been added.

## Iteration 1 verification record

The first SCC rerun reported missing formal receipts. The direct legacy
PowerShell runner then failed executable discovery. The child-local wrapper
allowed fresh compilation and all six negative controls to complete; its first
version propagated the final expected Agda exit code 42. The wrapper now checks
the successful audit and returns 0. These were execution defects, not mathematical
counterexamples. The corrected wrapper rerun exited 0. Both grammar validators
pass their eight rejection tests and read-only freshness checks; the existing
finite audit passes 335 code and 1,804 package controls; SCC
`nima-native-table-equivalence` now passes. The amplitude/component bridge was
source-inspected, not separately recompiled in this iteration.

Graph report proposal `ep_1a376ecb-db9f-4c7a-b645-037c7c821897` is admitted.
The source edits and both grammar-report proposals remain uncommitted; there are
no active background runs at that boundary. Native-core closure is verified at
its stated source boundary.

## Iteration 2 verification record

`check_semantic_grammar.py` discovers Python functions/methods with AST and
arithmetic declarations with a source-layout census, and requires each definition
to appear exactly once. Six malformed-census controls reject omitted/new
operations, duplicate classification and replacing multiplication by addition.
The path execution tests use the existing implementation, not a parallel model:
all exact child basis vectors split/reassemble, ancestry transitions invert on
their declared image, stored operand identities survive composition, associative
outputs keep distinct assembly trees, spectral projectors sum to the image
projector, and ownership/domain violations are rejected.

A nonzero sibling contrast has zero average. Therefore the ambient decoder is
not a candidate for `compare-kind`'s equivalence datum. The corrected reversible
interface is either the lift image or the joint parent/detail record. Generally,
A L=I gives A(x-L A x)=0; substitution shows split/reassemble are mutual inverses.
These identities hold for every finite nonempty sibling partition, not merely
the test fixtures.

Fresh `NativeComponentArithmetic` compilation and its two intended compiler
rejections pass. The existing receipt checker verifies its local import closure
and sources. `--require-formal` on the semantic checker reuses that checker and
refreshes its receipt; without that flag the semantic check is read-only unless
`--write` is supplied. No path-to-native Resolve equivalence is asserted.
The 23 invalid path requests, six census hostiles, both generated-table freshness
checks and SCC `nima-native-component-arithmetic` pass.

Graph proposal `ep_075bde69-47ff-4f9c-81a1-481db57f4881` records this milestone.
All grammar changes/reports remain uncommitted; no background computation is
active. Iteration 3 starts from signed/rational arithmetic and the nine-row policy
interpretation, not from re-enumerating the now-covered path/Word definitions.
