# UV flavor-ensemble microprogramme index

Owner: `marici.Figueiredo`.

## Frozen predecessor

WP116 is authoritative. Texture charts are presentation rigidifiers;
`physical16` probes are faithful separator/readouts; the mixed Gram word
`I_11` separates the measured-ten hostile pair; the FDM-2 thermal arrow is a
conditional algebraic selector; no source-authorized physical selector is
currently established. This programme cannot reopen downstream selector
fitting.

## Objective

The only admitted direction is

`UV source and normalization -> physical flavor ensemble -> frozen readouts`.

Numerical flavor constants may test a frozen ensemble, but may not define the
UV source, its coefficients, its normalization, or its equivalence weights.

## Work packages

1. **UV source class.** Declare fields, representations, local action,
   coefficient domain, UV scale, scheme, and boundary data without flavor
   targets.
2. **Parameter typing.** Partition source inputs, gauge/presentation choices,
   renormalization data, and derived observables.
3. **Normalization.** Supply a normalized positive state or probability
   measure on UV quotient configurations.
4. **UV-to-`physical16`.** Derive the measurable covariant map before reading
   phenomenological outputs.
5. **Descent.** Prove invariance under UV gauge, weak-basis, and chart arrows.
6. **Ensemble fiber.** Classify the pushforward as unique, finite, continuous,
   or undefined from missing source data.
7. **RG transport.** Fix input/output scales and scheme, then push the ensemble
   through an equivariant RG map.
8. **Phenomenology.** Test only the already frozen pushforward ensemble.
9. **Readout reuse.** Apply canonicalization, thermal, detector, repeatability,
   and route weights without selector authority.
10. **Hostile controls.** Reject output-fitted parameters, post-readout
    normalization, chart-weight dependence, measured-ten injectivity, and
    selector authority silently assigned to RG/detectors.
11. **Missing datum.** If the ensemble is undefined, state the minimal missing
    source datum rather than fitting it.
12. **Data-descent v2.** Compile conditional capability, reliability contract,
    and bounded evidence replay.

## First bounded release: WP117

- `flavor-uv-source-equivalence-conventions.md`
- `flavor-uv-to-physical16-contract.md`
- `flavor-uv-ensemble-hostile-controls.md`
- `contracts/flavor-uv-ensemble-data-descent.v2.json`
- `checkers/wp117_uv_ensemble_contract.py`
- `results/wp117_uv_ensemble_contract.json`

WP117 types all twelve packages and proves the decisive finite descent
falsifier. It does not invent the missing UV action or measure. Its current
classification is **undefined without additional source data**.

## Admission gate

A successor may become a physical ensemble only if it provides, before flavor
readout, a concrete UV action and coefficient domain, an independently
normalized positive measure, an equivariant vacuum/matching map, and an
explicit RG scale/scheme contract. The decisive falsifier is two
source-equivalent UV presentations inducing different pushforward measures on
`physical16`.
