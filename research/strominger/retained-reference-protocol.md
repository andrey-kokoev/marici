# Executable source-typed memory reference protocol

## Fresh construction

Implemented prepare/couple/preserve/interrogate/recover using the EXISTING conservative memory dynamics, with explicit source resource and empty-bank initialization.

A useful source adapter was recovered directly from `check_four_packet_cycle.py`: its actual real Cl(2,0) matrix representation

    matrix(s,q,p,z)=((s+q,p+z),(p-z,s-q)).

This is not an arbitrary coordinate reshape. It maps the Clifford unit to I, preserves the actual source multiplication, and has linear rank4. It types a memory value as a real2x2 OPERATOR in End(R^2).

The previous reference-resource audit's value/operator gap is therefore partially closed by an existing algebraic interpretation. The identification with comparison boundaries A->B and physical port attachments is still an additional typed input.

## Executable protocol

`checkers/retained_reference_protocol.py` exposes:

- `prepare(carrier,bank,provenance)`: both resource and bank are explicit;
- `advance()`: calls the unchanged conservative exchange and retains its parent/event;
- `interrogate('stored'|'delayed')`: returns value, source-represented operator, mode, depth, preparation and history;
- `recover_initial()`: verifies inverse steps through the actual retained parents;
- `inverse_operator()`: only available for nonsingular represented records.

The caller's provenance is an explicit mathematical declaration, not authentication, physical admission or experimental evidence. No automatic normalization to2I occurs.

## Exactly how2I can be prepared conditionally

Choose the supplied initial carrier resource

    x=2*Clifford unit,
    bank=0.

After one exchange, the stored memory value represents2I. After two exchanges, the same operator is available at the delayed record port. Its strict inverse is I/2, matching the numeric fixed reference/return in the software fixture.

After three exchanges, that scalar carrier resource returns and the active bank is empty. The retained history is NOT identified with the empty history.

The source coefficient budget is4, while the represented matrix Frobenius norm squared is8. Their conversion follows the representation; neither is declared laboratory energy.

This preparation is conditional on choosing the explicit two-unit input. It does not derive that amplitude, select units or explain the physical reference scale. Inputs of0,1 and3 units yield0,I and3I respectively.

## Reference lifecycle matters

The protocol creates an accessible record from an input resource and returns that resource. It does NOT keep an active bank reference permanently available after the third exchange.

The software parent history still retains earlier record states. That is mathematical lineage, not a demonstration that copying/interrogating physical records is free or that a permanent reference catalyst exists. Clock, detector back-action, storage/reset resources and reuse/degradation remain outside this calculation.

The original retained depth policy is enforced; another advance after three source steps is rejected. No history is silently discarded to claim unlimited repeatability.

## Invertibility and typing controls

Some source values represent singular matrices. The checker supplies an actual such control and verifies that no inverse reference return is fabricated.

The operator representation lives in End(R^2). The pinned T9 reference lives in Hom(A,B). Even when their numerical coordinates agree, interpreting them as the same reference requires boundary identifications and the existing supplied port attachments. Common matrices do not identify those typed objects automatically.

The represented lineage is exact:

    stored_operator = M(rotate(x)) = M(J) M(x) M(J)^-1.

It is source-represented dynamics, not passive port transport or a physical connection selected from endpoint incidence.

## Verification

    python research/strominger/checkers/check_retained_reference_protocol.py

53 exact checks pass. They cover all basis products in the source representation, its rank/unit, full-basis lineage and resource recovery, explicit2I preparation/inverse, budget conversion, reference lifecycle, scale controls, singularity rejection, required preparation/port declarations and the retained depth limit.

Source functions are exercised directly. No source-owner receipts are overwritten and no new Agda or physical instrument verification is claimed.

Artifacts:

- `research/strominger/checkers/retained_reference_protocol.py`
- `research/strominger/checkers/check_retained_reference_protocol.py`
- `research/strominger/results/retained-reference-protocol.json`

## Status

**Complete conditionally:** executable source memory protocol and existing algebraic value-to-operator adapter; explicit two-unit preparation reproduces the numeric2I reference.

**Still supplied:** preparation/units of that resource, boundary and carrier-port identifications, source mixer realization, clock, detector and physical reuse/degradation. Physical T9 remains unestablished.

No fixed matrix target was used to alter the source law or representation. The chosen input resource is exposed as a choice rather than reported as a source-derived calibration.
