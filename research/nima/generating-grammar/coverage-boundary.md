# Coverage boundary for the Marici generating grammar

## Revision 1 (2026-10-01)

This document states what the generating grammar covers and what it explicitly
does not. It is authoritative for the grammar audit; extension requires schema
review.

## What is covered

The generating grammar covers **three named manifest scopes** with source-bound
formal verification:

### 1. Native core (8 headers, 12 rules, 2 derivations)

| Component | Count | Verification | Source |
|---|---|---|---|
| Headers (atom, E, Pi, paths, maps, equivalences, retain, comparison) | 8 | Native table equivalence (all 8 Code forms) | `native-table-equivalence.md` |
| Rule schemas (E-kind, P-kind, compare-kind, identity-kind, inverse-kind, compose-kind, higher-kind, reflexivity-kind, path-lift-kind, distribution-kind, E-congruence-kind, P-congruence-kind) | 12 | Native table equivalence (all 12 rules, inverse laws, commuting endpoint) | `NativeTableResolution.agda`, `NativeTableRules.agda` |
| Derivation constructors (seed, apply) | 2 | Closure equivalence for arbitrary original seeds | `NativeTableResolution.agda` |
| Amplitude expression interpretation (zero, one, factor, binary) | 4 forms, 2 modes | native-run | `NativeAmplitudeResolution.agda` |

### 2. Semantic extensions (33 path operations + 25 word/component operations)

| Domain | Definitions | Source |
|---|---|---|
| Retained-path ledger | 33 functions/methods (split, reassemble, compose, decode, encode, etc.) | `retained_path_successor.py`, `semantic-extensions.json` |
| Natural component arithmetic | 25 named definitions (Word semiring, bilinear composition, native bridge) | `ComponentArithmetic.agda`, `NativeComponentArithmetic.agda`, `semantic-extensions.json` |

### 3. Completions and policies (123 definitions + 9 policy assessments)

| Domain | Definitions | Source |
|---|---|---|
| Signed component arithmetic | 47 definitions | `SignedComponentArithmetic.agda` |
| Rational component arithmetic | 43 definitions | `RationalComponentArithmetic.agda` |
| Faithful component ring | 7 definitions | `FaithfulComponentRing.agda` |
| Native coefficient transport | 5 definitions | `NativeCoefficientTransport.agda` |
| Native rational bridge | 12 definitions, 1 datatype | `NativeRationalComponentArithmetic.agda` |
| Native family/pair macros | 9 definitions | `GeneratingGrammarMacros.agda` |
| Policy assessments (all 9 contract rows) | 9 rows | `completions-and-policies.json` |

### 4. Previously registered checked rule applications (5 contract rows)

These entries identify checked terms; full contract preservation obligations
still require an audit. The other four rows in `RemainingInterpretations.agda`
are partial: identity-only history, tagged-sum operand selection, absorbed
reference correction, and a single active-frame composition. Revision 16 replaces
that operand entry with `OperandPairInterpretation.Pairing.run`: genuine Pi
pairing with both values, round trips and premise recovery freshly checked.
This covers supplied operands, not independent preparation. The other partial
entries do not close `gap.operational_interpretations`.

Revision 17 replaces the history registry entry with `HistoryPathEdits.Edits`:
readout and dependent-invariant preservation for a supplied path, with parent,
permission and cost retention. DG exact-edit preservation is still open; no
unit/triangle predicate has yet been instantiated in that generic module.

Revisions 18–19 add separate conditional DG proofs in `DGHistoryTransport.agda`
and `DGFrameUpdates.agda`. Active updates preserve both unit equations and the
triangle while keeping u,v fixed; exact edits preserve full frame validity.
The common-carrier algebra still needs a concrete DG instance, typed endpoint
corners, certificate composition/inversion and a native Resolve bridge. This
is not a claim that the protected-request contract is fully interpreted.

Revision 20 checks the certificate boundary formulas for composition and
inversion in `DGCertificateTransport.agda`, conditional on explicit algebra
laws. Equality of sequential versus direct full frame actions remains open,
so this does not close the full protected-request interpretation.

Revisions 22–23 now check componentwise sequential/direct action agreement
and forward/inverse recovery in `DGActionComposition.agda` and
`DGActionInverse.agda`. Both include W and construct admitted requests. They
remain conditional common-carrier results; proof-field equality, a concrete
endpoint-typed DG instance and policy/native integration are not claimed.

`PathLedgerInterpretations.agda` checks readout agreement and pointwise
naturality only; it does not interpret Python split/reassemble or composition.

| Contract operation | Native rule | Agda source |
|---|---|---|
| filler-as-compare-rule-apply (all Filler-based transport) | compare-rule | `BoundaryGeneratedQuestions.Application.perform` |
| frame.passive (passive frame change) | compare-rule | `PassiveFrameTransport.Interpretation.Passive.change` |
| reference.substitute (witnessed reference substitution) | compose-rule + identity-rule | `ContractInterpretations.Interpret.substitute` |
| record.reindex (re-present retained records) | Pi-congruence-rule | `ContractInterpretations.Interpret.reindex` |
| family.admit (uniform family admission) | Pi-congruence-rule | `ContractInterpretations.Interpret.admit` |

## What is NOT covered (explicitly out of scope)

These categories are not mathematical operations of the generating grammar:

| Category | Examples | Reason for exclusion |
|---|---|---|
| Physical application models | cosmology-* models, nima-mass-* models, nima-optical-* models | They use the grammar; they do not extend it |
| Exchange/infrastructure protocols | nima-exchange-* models, nima-source-exchange-* models | Protocol configuration, not mathematical operations |
| Computational test fixtures | nima-*-regression models, nima-*-fixture models | Test instances, not generative operations |
| External mathematical results | evans-* models, wolfram-converse | Independent external theorems, not grammar operations |

## What remains (registered candidates, bridges unverified)

These six sources are registered as candidates, not established native-rule
interpretations. Existing Agda constructions and module compilation do not prove
operational coverage. The suggested rule families below require typed bridges
and fresh verification before coverage can be claimed.

| Model | Suggested rule family (unverified) | Agda source | Notes |
|---|---|---|---|
| nima-e-tree-templates | E-kind | `ECurriedTemplates.agda` | Template system with E-tree substitution; partial application consumes one slot |
| nima-fibration-constructor-bridge | E-kind / P-kind + congruence | `FibrationCodeInterpretation.agda` | Fiber/section interpretation via annotated constructors |
| nima-fibration-route-generator | compose-kind | `FibrationRouteInterchange.agda` | Route interchange along fibration boundaries |
| nima-index-identity-coherence | identity-kind + reflexivity-kind | `IndexIdentityCoherence.agda` | Index evidence decodes to paths; Family/Index/Fibre/Total/Sections defined |
| nima-nand-constructions | seed (Bool) + apply | `NandConstructions.agda` | NAND via Pi over E-pair; curryIso/emptySumIso isomorphisms checked |
| nima-universal-substitution | compare-kind + distribution-kind | `UniversalSubstitution.agda` | Universal characterization of equivalence via pre/post composition; Sigma/Pi adjunctions |

## Principle

An operation is **covered** when it appears in a grammar manifest with a source
reference and (where applicable) a checked Agda interpretation. It is **out of scope**
when it is a physical application, infrastructure protocol, or external theorem
that does not extend the grammar's generative rules.

This boundary does not assert that the grammar generates every possible value
(atom, type, function, equivalence, witness). Those remain supplied parameters,
exactly as in the baseline. The grammar generates **retained derivations**, not
arbitrary mathematical objects.