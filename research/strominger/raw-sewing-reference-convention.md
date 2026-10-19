# Same unit-resource execution: normalized I versus raw2I

## Fresh result

Tested the strongest recovered clue without altering the conservative exchange.

For the SAME retained unit-resource execution:

- normalized memory readout C produces the represented operator I;
- actual source raw sewing mu produces2I;
- the stored coefficient budget remains ONE in both cases.

The factor2 is derived from the actual sewing rows under the supplied coefficient metric. It is not a fitted gain inserted to match the reference.

This supplies an alternative conditional realization of the fixture's numeric2I, but does NOT select raw-response semantics as the intended physical reference.

## Exact source identities

Construct the rectangular readout matrices directly from the actual source functions on all16 bank basis vectors. Each raw coefficient row has four signed nonzero terms, and

    mu mu^T=4I,
    C=mu/2,
    C C^T=I.

The checker verifies the raw/normalized factor on the full bank basis at both stored and delayed ports, not only on a scalar example.

The conservative dynamics still uses its ORIGINAL normalized readout C. The new raw option changes interrogation only.

## Executable interface change

`ReferenceProtocol.interrogate(mode,readout_policy)` now accepts:

- `normalized` (unchanged default);
- `raw-sewing` (calls the existing source sewing function).

Every observation retains its policy. `BoundReference` also retains that policy, and `bind(...,readout_policy)` checks the represented reference against the pinned fixture without rescaling.

Older normalized callers and their checks still pass. The machine-readable software contract is NOT changed to claim raw preparation or physical calibration.

## Compare two distinct ways to get numeric2I

| Explicit resource | Readout | Bound operator | Coefficient budget |
|---|---|---|---:|
|unit, empty bank|raw sewing|2I|1|
|2*unit, empty bank|normalized|2I|4|

All137 leaf and32 selected final-family attachments agree numerically because both bound operators and inverses agree. The preparation/resource and readout-policy packets do NOT agree and are retained as distinct.

Therefore a2I reference value alone does not identify the implementation or its resource calibration.

Controls reject normalized-unit I instead of2I, raw-two-unit4I instead of2I, unknown readout policies and the depleted bank after the third step. No automatic multiplication/division is allowed to force a fit.

## Why raw2I is not doubled stored resource

At the unit-resource stored stage, the bank has coefficient norm squared1. Its raw readout value has norm squared4. Treating that raw value as a conservatively transferred carrier state would exceed the total input budget before accounting for any nonnegative remainder.

Thus raw sewing cannot be substituted as an isometric output block under the same positive coefficient metric. This is a readout response convention, not energy creation or a stronger prepared bank state.

The matrix representation adds its own norm conversion: Frobenius norm squared is twice the coefficient norm squared. Physical detector gain, units and apparatus resources require their own calibration; none is inferred from these counting-basis identities.

## Lifecycle remains unchanged

The raw reference2I is available in the stored record after one exchange and at the delayed port after two. After three exchanges, the original unit resource returns and the active bank is zero.

Full parent/event history remains retained. Reading a past software snapshot is not a claim that a physical reference stays available forever, or that its interrogation/reset is resource-free.

## What the clue resolves

The earlier two-unit input is NOT the only mathematical explanation of the fixture coefficient2. An existing source readout can produce that coefficient from a unit record.

However the source does not currently say that its raw sewing response is the fixed comparison map d:A->B. That role binding remains explicit. An algebraic unit resource still requires physical preparation and units.

The next deciding question is consequently sharper:

**Is d intended to denote a stored/prepared reference map, or a raw comparison-response standard?**

A raw convention may be sensible for the latter, but must carry its readout metric/detector gain separately from the normalized conservative state dynamics. Selecting it merely because it yields2I would still be backward inference from a target.

## Verification

    uv run research/strominger/checkers/check_raw_sewing_reference_convention.py

254 exact checks pass. The previous2004-check reference/port suite, retained source protocol and pinned software suites are freshly rerun as dependencies and remain passing.

No new physical experiment, Agda closure, fitted gain or change to the pinned reference policy is claimed.

Artifacts:

- `research/strominger/checkers/check_raw_sewing_reference_convention.py`
- `research/strominger/results/raw-sewing-reference-convention.json`
- updated `research/strominger/checkers/retained_reference_protocol.py`
- updated `research/strominger/checkers/reference_port_binding.py`
