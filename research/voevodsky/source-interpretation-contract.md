# Source interpretation contract

## Question

What exact data would promote the checked integer fixture into a source-derived interpretation of the signed-even analytic fixture?

## Claim boundary

The module defines the required interpretation type and verifies that omitted naturality witnesses are rejected. It does not construct an inhabitant for the analytic fixture and therefore does not establish source-global naturality.

## Construction

`SourceInterpretation.agda` requires coordinate maps from each source parameter, object, and residue type into the integer fixture, together with paths showing that coordinates commute with every generator and coherencer. A cycle interpretation additionally requires naturality for all three directed residue transports. A completion interpretation must commute with the source completion injection. A filler interpretation must map each source filler to a generated edge triple and identify its generated second boundary with the source discrepancy.

These fields form `SourceInterpretationContract`. No inhabitant is exported.

## Strongest falsification attempt

`negative/MissingNaturality.agda` supplies three identity coordinate functions but omits generator and coherencer naturality. Agda rejects the record as incomplete and names both missing fields. Thus coordinate functions alone cannot be presented as an interpretation.

## Disposition

The source-global gap is now a precise uninhabited contract rather than prose. The first missing typed object is a source-derived coefficient or coordinate interpretation from the signed-even analytic fixture into `Generatedℤ³`. The existing analytic fixture gives a function-valued discrepancy \(\tau H\), whereas the current native complex uses integer coefficients; no canonical map between those types has been supplied. Further promotion stops at this blocker unless a source packet constructs that map or replaces the coefficient object with a formally defined analytic additive group.

## Verification

- `research/voevodsky/agda/SourceInterpretation.agda`
- `research/voevodsky/agda/negative/MissingNaturality.agda`
- `research/voevodsky/results/cubical_agda_source_interpretation.json`
