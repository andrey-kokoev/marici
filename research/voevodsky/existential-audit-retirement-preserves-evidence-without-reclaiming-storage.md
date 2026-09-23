# Existential audit retirement preserves evidence without reclaiming storage

## Representation and theorem

Retain a private/internal schema B, source carrier C and full evidence history. Choose a public subschema A with O_A=p O_B. Public possibility space is O_A(C). Retired coordinates remain internal existential variables, not deleted evidence.

A public linear objective a pulls back to a composed with p. Optimizing that pullback over C gives exactly the optimum over O_A(C); emptiness is also preserved. A source witness plus the original dual certificate certifies the public optimum after checking the schema translation. This construction avoids materializing projected facets. It does not reduce internal storage.

An exact public point-membership implementation would constrain only the public coordinates and leave retired coordinates free. It must not fill retired coordinates with zeros or selected values. That branch is a consequence of the source-space formulation but is not implemented by this small retirement wrapper, which currently supports maximization only.

## Owning source control

In the tail box, retain internal audit h=x_0 and frames U=h, h<=1. Since all source coordinates are nonnegative, U=h forces all remaining atoms to zero. The exact public U maximum is one.

Retire h from the public schema while keeping all three inequality rows (the equality uses two). The source-space optimizer still certifies maximum U=1. A retired-coordinate objective is rejected by the public query shape check.

Deliberately deleting only the h<=1 frame changes the optimum to 100. The discarded evidence was not irrelevant merely because its coordinate ceased to be public. These are controls on the admitted analytical tail box, not a new source model.

## Binding and tests

The wrapper's envelope binds internal state, public schema, public query and the translated internal certificate. The independent verifier receives the expected state/schema/query externally, reconstructs the objective translation, and uses the arithmetic checker without importing the producer or solver.

Four cases through m=16 yield eight checked arithmetic certificates (correct projection and deliberate deletion controls). Twelve mutations changing history, public schema or requested query are rejected. The tests also compare pre-retirement and post-retirement optimum values and reject direct retired-coordinate queries.

No confidentiality is claimed. Full internal state and source witnesses appear in certificates; in this example h is also mathematically determined by public U. 'Public' describes the admitted query language, not a cryptographic access-control boundary. The wrapper is a research prototype, not a validated general API, and source admission was not freshly replayed.

## Next boundary

The executable distinction is now: hide a coordinate from the query language while retaining its evidence internally, versus actually compress the representation. Storage reclamation would require a certified alternative presentation of O_A(C), not just a changed list of exposed coordinates. In this control U<=1 summarizes the retired audit's relevant restriction, but finding and proving such summaries generally is a separate projection/compression task.

## Reproduction

    uv run --with sympy python research/voevodsky/checkers/check_projected_tail_interface.py
    python research/voevodsky/checkers/verify_projected_tail_interface.py

Artifacts:

- `results/projected-tail-interface.json`
- `results/projected-tail-interface-verification.json`
