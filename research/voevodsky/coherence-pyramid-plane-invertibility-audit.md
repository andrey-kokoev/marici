# Coherence-pyramid plane invertibility audit

## Question

Are the coherence-pyramid planes invertible, so that they may be modeled as homotopies in an \((\infty,1)\)-category?

## Claim boundary

This audit uses the registered computad signature and cell-law packet. It does not identify conversational geometry with a registered cell class without a source-derived map.

## Registered cells

The cell-law packet declares six classes:

- associator;
- left unitor;
- right unitor;
- interchange;
- Beck--Chevalley;
- completion comparison.

Only Beck--Chevalley and completion comparison have explicit invertibility gates.

A Beck--Chevalley cell is invertible only when its comparison map is an isomorphism and the inverse preserves transported certificates.

A completion-comparison cell is invertible only when there is a closed-domain equivalence and positive reduced minimum modulus in both directions.

The packet explicitly refuses a Beck--Chevalley invertibility claim when inverse certificate preservation is absent.

## Missing identification

Neither `meaning_plane` nor `transport_plane` occurs in the registered cell schema. Therefore no current source arrow identifies those conversational planes with one of the audited classes.

Without that identification, constructing formal reverse planes would test an invented model rather than the coherence pyramid.

## Disposition

Uniform plane invertibility is not established. Promotion of the current structure to an \((\infty,1)\)-category is therefore inadmissible.

The first missing typed object is a source-derived identification of the meaning and transport planes with registered cell classes. Once supplied, the acceptance test is:

1. construct a reverse cell;
2. verify both composites are identity cells;
3. verify the reverse preserves all certificates required by composition.

If either plane lacks such a reverse, the structure requires directed 2-cells and belongs in an \((\infty,2)\)-categorical model.

## Verification

```text
python research/voevodsky/checkers/check_coherence_pyramid_plane_invertibility_gate.py
```

Artifacts:

- `research/voevodsky/checkers/check_coherence_pyramid_plane_invertibility_gate.py`
- `research/voevodsky/results/coherence_pyramid_plane_invertibility_gate.json`
