# Generated comparisons survive faithful dependent normalization

## Checked result

`GeneratedNormalizationBridge.agda` now consumes the existing
`WholeHistoryComparisons.Structural.Generated` datatype directly. It does not
introduce a semantic-witness import constructor or replace generated syntax
with an unrelated comparison language.

For an interpretation A, supply a code for each carrier A(q) and an equivalence
from that carrier to the code's interpretation. The arbitrary-dependent
normalizer then supplies faithful coordinates k(q).

The bridge proves:

1. The whole rule algebra transports along k, including arbitrary dependent
   rule arities. Evaluation before/after transport agrees by the checked
   universal-property fusion theorem.
2. Each existing generated derivation c has normalized witness
   `cong k (sound c)`. The dependent-congruence equation is checked against
   the actual `Generated.congruence` constructor.
3. The identity-witness map is an equivalence. The original witness can be
   reconstructed, not merely replaced by some path between the endpoints.
4. Original generated witness completeness implies normalized generated
   witness completeness, and conversely. These are implications between
   obligations; no equivalence of completeness proof spaces is asserted.
5. The retained package stores the endpoint, both raw histories, the actual
   generated derivation, both witnesses, their agreements and reconstruction.
   The entire record can become a subsequent Complete input.

Here normalized semantics means `k(evaluate A d) = k(evaluate A e)`.
Agreement with evaluation in the transported algebra is a proved path, not
an assumed definitional equality.

## Concrete positive and hostile checks

`GeneratedNormalizationBridgeRegression.agda` freezes the existing
`WholeHistoryComparisonInstance` endpoint observer and its explicit
identity-as-general law. The existing derivation passes directly to the bridge;
its witness reconstructs and both histories and derivation remain in the
reified record. A law derivation and its double inversion remain provably
unequal as raw derivations.

With the law removed, a normalized endpoint witness still exists, but no
Generated representative exists. Normalized completeness would imply the
already refuted original completeness. Thus normalization cannot repair the
missing equation.

This concrete observer reads endpoint values, not all raw history data. Its
carrier is encoded atomically in this regression. It tests the actual API
connection and failure preservation, not a completed interpretation of all
intended resolution-order laws.

## Remaining branch

The generic normalization/Generated adapter is checked. The remaining
instantiation must choose a resolution interpretation and explicit dependent
reordering laws that meet the intended full-package semantics. In particular,
the complete inner-first/outer-first traces from
`DependentArbitraryIndexRoutes.agda` still need their law-level connection to
resolution histories in that interpretation. The full finite comparison basis
is not yet complete.

## Verification

Fresh safe Cubical Agda verification passed:

```
pwsh -NoProfile -File research/nima/checkers/check_cubical_agda.ps1 -Module GeneratedNormalizationBridgeRegression -Fresh
```

Artifacts:

* `research/nima/agda/GeneratedNormalizationBridge.agda`
* `research/nima/agda/GeneratedNormalizationBridgeRegression.agda`
* `research/nima/results/agda-GeneratedNormalizationBridgeRegression.json`
* `research/nima/results/agda-GeneratedNormalizationBridgeRegression.log`

Programme tree: `issue-tree:ec9d8dc9a050db37f5f82cd0`.
