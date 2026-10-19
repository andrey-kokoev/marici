# Existing seed/rung and instrument chains: binding comparison

## Objective and method

Compare the existing confirmed 12--9-->6, 11--8-->5, 10--7-->4 transport with the existing native-matrix-prepared exchange experiment. Do not add a replacement fixture or declare a new physical observer. Freshly run both chains, the actual-path endpoint audit, and the instrument audit's eight supporting checks.

The word "native" in the instrument code refers to the supplied shared-leg DG fixture. It must not be read as evidence that its matrix amplitudes were generated from the six-arrow seed.

## Positive binding: the initial preparation interface agrees exactly

Both implementations use identical matrix values, direct reference d=2I, and the same ordered 121 arrow-pair plus16 state-pair labels. For every original rung leaf C_ij=Y_j X_i, the instrument's exact raw preparation is

    r_ij = tr(C_ij-d).

Both retained horizontal policies give the identical original member-weighted rung reader

    J4 = (sum C_ij)/137 - d
       = [[-1, 629/411], [629/685, 1006/2055]].

Therefore

    tr(J4) = (sum r_ij)/137 = -1049/2055,
    mean(initial prepared X) = gamma tr(J4) = -1049/8220,
    gamma = 1/4.

The matrix and rational identities are exact; their comparison with the instrument's NumPy preparation uses tolerance 1e-10. This is a genuine common interface between two existing implementations, not merely agreement of dimensions. It binds the INITIAL scalar mean, not each addressed record, subsequent detector responses, or physical normalization. Gamma and trace remain declared preparation choices.

## Operation and memory: existing obstructions survive fresh execution

The instrument's existing support checks establish their original scoped results:

- Shared 2-by2 matrix-leg trace preparations need not remain in that preparation class under a selected exchange: a hostile arrow block changes rank four to five.
- At fixed endpoint data, the native additive witness reader factors through the boundary. Changing witnesses by retained fillers cannot supply independently writable record amplitudes.
- The addressed exchange operators fail strict same-state-space invertible shared-leg factorization on all109 tested rectangles. They do implement ordered labelled events with attached memory.

These are not universal impossibility statements for other adapters. In particular the rank hostile uses the previously declared preparation class, not a new claim that every pulse of the baseline fixture raises its rank.

## Readout comparison on the actual prepared fixture

Reuse the existing two-event echo at port120 and the chronological rectangle at ports120,10,0,110. No new pulse word or preparation is introduced.

Both experiments retain the same matrix preparation and preparation identity. The echo restores the entire prepared mean state. The rectangle changes independently retained current record corrections. Their offset-subtracted detector mean ratios are respectively +1 and 0 (within 1e-10).

Project either augmented experiment back to its retained ORIGINAL preparation. The original J4 is identical, while the detector response differs. Thus this detector response cannot factor through J4 of preparation alone.

This projection is explicitly forgetting current memory and event history; it is NOT an asserted native time evolution of matrix legs. The full faithful packet reconstructs the changed records. An authorized new current-state rung realization might behave differently, but none is constructed here.

Separately, the freshly rerun actual-path endpoint audit retains its original collision: the two repeated triangle histories have equal unchanged J4=-I and different exchange mismatches. That adapter remains distinct from the137-row preparation above.

## Gate ledger

| Interface | Result |
|---|---|
| Six-arrow seed to matrix fixture | Still absent: numerical legs, state branch, reference, and DG witness interpretation are supplied |
| Fixture to initial instrument preparation | Exact declared trace/gain interface verified on all137 records |
| Native operation to exchange | Labelled event execution works; strict shared-leg realization fails its existing controls |
| Native witnesses to writable memory | Existing fixed-boundary additive reader cannot provide independent corrections |
| Initial aggregate to preparation mean | Exact agreement |
| Preparation aggregate to current detector | Explicit echo/rectangle collision |
| Physical selection | Intended T9, memory attachment, preparation, pulse and detector remain unselected |

The next required input is not another averaging formula: it is a source-authorized operation on a specified current state, including whether independently writable memory is part of that state. A proposed binding must supply a seed-to-fixture interpretation and an operation comparison before its detector can be identified with a rung observation. Keeping attached memory explicit is a valid conditional experiment, not completion of source-selected descent.

## Verification and artifacts

    OPENBLAS_NUM_THREADS=1 uv run research/nima/checkers/check_seed_instrument_binding_comparison.py

18 comparison checks pass, alongside fresh execution of the existing rung, endpoint, and end-to-end instrument chains. Negative controls passing means their scoped obstructions were reproduced, not that the descent gates passed. Source-selected descent remains false in the machine receipt.

- Checker: `checkers/check_seed_instrument_binding_comparison.py`
- Receipt: `results/seed-instrument-binding-comparison.json`
- Existing chains: `executable-rung4-chain-first-missing-seed-link.md`, `source-exchange-end-to-end-audit.md`, `rung-descent-endpoint-binding.md`

No physical data, new calibration, source map, or replacement reader is introduced.
