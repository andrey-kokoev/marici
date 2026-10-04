# Smallest native Yoneda gate: application versus retained specialization

## Question and frozen contract

Can the actual twelve-rule native closure specialize a supplied function without
admitting the evaluated answer? This is forward realization, upstream of Yoneda
witness composition. The source is `NativeTableRules` / `NativeTableResolution`,
not a newly invented evaluator.

The concrete inputs are a maps-node package for f:Unit→Bool with f(tt)=true,
and an atomic Unit package containing tt. The admission family has exactly two
seed constructors for those inputs; as a type family it also respects equality.
The required endpoint is the atomic Bool result, either bare or with BOTH input
packages retained through `remember`. No evaluated result is admitted.

## Disposition

**The canonical evaluated-endpoint gate fails; certified-family specialization
passes.** Fresh safe Cubical Agda proves both results. No core file was changed.

`NativeApplicationGate.agda` proves an invariant over every universe level and
all twelve actual rule schemas: after recursively stripping retention wrappers,
no rule output has an atom as its principal constructor. Consequently any native
derivation of such a package must obtain its admission certificate.

For the chosen seeds, every admitted principal-atomic carrier is propositional:
only the Unit argument qualifies, whereas the function has a maps principal node.
Bool is not propositional, so neither the bare Bool answer nor the answer retaining
both operands has an admission certificate or a native derivation. This is a
formal unbounded derivation obstruction, not failure of bounded proof search.

The proof uses the proposition/nonproposition distinction rather than attempting
to distinguish true and false across univalent package-carrier paths. Package
equality can transport the carrier and value together; raw value comparison would
not have been a sound admission discriminator.

## What already works

`GeneratingGrammarMacros.Retained.family-run` assembles a P-kind derivation from
its component derivations. Its existing `family-premise` recovers the exact
selected component and derivation. The new `CertifiedFamily.specialize` exposes
this operation and checks its beta equality by refl. This is genuine reuse of
an existing native subderivation; it does not produce missing components from
an opaque supplied function seed.

A separate positive fixture forms an actual P-kind package retaining f and tt.
Its external readout applies f to tt and computes true. The negative module
`NativeApplicationBadReadout.agda` is rejected when that pairing derivation is
misrepresented as a derivation ending at the retained evaluated Bool package.
Host-language evaluation and native endpoint generation are different claims.

## Governing falsification

- Problem: Yoneda's identity evaluation requires specialization, not just storage.
- Conjecture tested: the unchanged native closure derives the canonical retained
  codomain package from function and argument seeds alone.
- Rivals: only certified P-family selection is supported; computation occurs in
  an external readout; rejecting bare outputs merely reflects history retention.
- Risky consequence: even constant Unit→Bool application must reach the stated
  Bool endpoint without a new answer seed.
- Strongest test: an exhaustive rule-output invariant rules out every derivation,
  including endpoints retaining both operands. Existing P-family specialization
  and external evaluation remain positive controls.
- Surviving scope: the stated generative claim is refuted. This does NOT rule out
  every alternative result encoding, interpreted application, or a separately
  justified native elimination extension.

## Yoneda consequence

The next missing operation is an application/elimination bridge from the chosen
input representation to a certified native result endpoint. Changing to a
certified family representation requires its component derivations; adding an
application generator is a core extension, not a macro already proved here.
Neither change is silently made. Yoneda's mathematical proof remains checked;
its complete execution as a native rule derivation is not established.

## Verification

```text
pwsh -NoProfile -File research/nima/checkers/check_native_application_kernel.ps1
python research/nima/checkers/check_native_application_gate.py
python research/aspect/scc/scc.py check nima-native-application-gate
```

Fresh kernel execution: `structured_command_execution:e_16084_1791129445149633800_15`.
Audit: `structured_command_execution:e_16084_1791129536926562000_16`.
Receipts: `research/nima/results/native-application-kernel.json` and
`research/nima/results/native-application-audit.json`. Source/compiler/driver
hashes are checked, together with the six-file Stone core freeze.
