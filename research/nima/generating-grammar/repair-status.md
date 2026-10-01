# Repair status after iteration 10 (registry 25)

## Checked scope

- `OperandPairInterpretation`: genuine supplied-operand Pi pairing, both value
  projections, assemble/unpack round trips and actual premise recovery.
- `DGHistoryTransport` / `DGFrameUpdates`: conditional common-carrier DG
  active updates and exact edits preserving unit and triangle equations.
- `DGCertificateTransport`: certificate boundary composition and inversion.
- `DGActionComposition` / `DGActionInverse`: admitted composite/inverse requests
  and componentwise agreement/recovery of C,d,r,u,v,W. No equality of proof
  fields is asserted.
- `DGHistoryEditPolicy`: explicit permission/readout gate, retained original
  Resolve derivation, generator, cost, evidence and computed result. Fixed-field
  readouts C,d,r,u are invariant; arbitrary readouts need a supplied witness.
- `InterpretationRegression`: fresh aggregate safe/cubical closure check.
- Dependency audit: 13 roots, 40 local sources, matching receipts; aggregate
  before/after-stable compiler and 1091-file Cubical source inventory. Missing,
  stale, failed or non-fresh receipts fail the audit. An import warning remains
  in FibrationSigmaPiBridge; passing is not warning-free.

## Still executable, not complete

1. Instantiate the graded algebra interfaces with an endpoint-typed, nontrivial
   DG model. The current common-carrier model is NOT automatically the A/B
   corner model: separate identities and composition domains must be tracked.
2. Prove the policy-approved computed result has a native Resolve derivation,
   without silently seeding it. Retaining a result is not deriving it.
3. Connect the supplied permission/readout policy to the concrete DG fixture;
   prove the exact-edit certificate update K -> K + [g,Z] in that scope.
4. Audit semantic dependencies against a corrected typed source signature.
   Hash inventories do not prove derivability from S4. The source signature
   remains unresolved and is not frozen. Compiler built-in data is also outside
   the inventory audit.
5. Retain the existing distinction between independent preparation (not proved)
   and pairing explicitly supplied operands (proved).

## Reproduce

```text
pwsh -NoProfile -File research/nima/checkers/check_cubical_agda.ps1 -Module InterpretationRegression -Fresh
python research/nima/checkers/check_interpretation_dependencies.py --write --self-test
python research/nima/checkers/check_generating_grammar.py --write --self-test
```

Changing local source dependencies can invalidate individual root receipts even
if the aggregate is refreshed. Rerun the listed stale root checks before claiming
that the dependency audit passes.
