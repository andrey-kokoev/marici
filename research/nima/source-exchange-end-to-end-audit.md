# Iteration 8: actual native preparation through the conditional experiment

## What changed

Earlier tests compiled native witness labels but supplied a separate simple
one-port preparation. This audit now evaluates the actual native shared-leg
matrix fixture, seeds all137 records from its responses, executes compiled
exchanges, and computes detector predictions. All eight supporting checkers
are freshly rerun; their file hashes and statuses enter the machine report.

## Explicit state/preparation map

For the freshly read native values X_i,Y_j,d and each actual witness h_ij,

    r_ij = trace(evaluate(boundary(h_ij))) = trace(Y_j X_i-d),
    X_record_ij = gamma*r_ij,
    X_carrier = 0.

Set gamma=1/4 as a DECLARED preparation gain. All record and carrier modes are
prepared coherently, with X covariance I153/2 and supplied independent vacuum
P quadratures. This is a concrete conditional map from native matrix responses
to instrument preparations. It does not assert that trace or gamma is selected
by the native source or that preparation is free.

The source matrices, direct reference, gain and quadrature conventions are
serialized as provenance. Original legs remain preparation data. After execution,
record corrections w_current-w_initial are retained independently; they are not
refactored back into native shared-leg products. The current state is stored by
its faithful16-anchor/137-mismatch packet plus covariance and event history.

## End-to-end controls

The arrow port(10,10) has native trace14/3, hence prepared X=7/6. Its two-pulse
exchange echo restores the ENTIRE prepared mean state. The chronological
rectangle (10,10),(0,10),(0,0),(10,0) empties its first port. Both conserve the
anchors and quadratic mean budget; coherent covariance stays I153/2.

Using the independently declared detector fixture from iteration7, the resulting
offset-subtracted population mean ratios are

    native-seeded exchange echo: +1,
    competing quarter-turn echo: -1,
    native-seeded exchange rectangle: 0.

This calculation uses actual compiled witnesses and source matrix values,
not just a matching census. It remains a prediction of an assumed apparatus,
not a measurement or a derivation of why nature selects that apparatus.

Doubling gamma doubles the detector signal and quadruples the coherent prepared
excitation budget while leaving those ratios unchanged. Thus even this complete
conditional chain does not determine an absolute response normalization.

## Success-criterion ledger

| Criterion | Checked result | Remaining boundary |
|---|---|---|
| State | Actual native matrix responses seed the full instrument record array; provenance and corrections retained | Trace readout, gain, coherent preparation and independent memory are supplied |
| Operation | Native boundary validation, event concatenation and tested reference transport | Strict native shared-leg factorization fails; source selection of the pulse is open |
| Observable | Coherent quadrature means/covariance feed a loss/gain/noise/phase detector model | Physical calibration, phase monitoring and instrument resources are assumed |
| Normalization | Raw signal and energy-scale freedom are exposed;1/137 is not substituted for gain | Absolute current/field coupling is not derived |
| Discriminator | Signed echo and rectangle distinguish specified alternatives | Stable preparation and phase controls are required; no experimental data supplied |

The immediate source-labelled experiment deliverable is now executable under
explicit assumptions. The stronger objective of source-selected physical descent
is NOT marked complete in the machine report.

## Verification

    OPENBLAS_NUM_THREADS=1 uv run research/nima/checkers/check_source_exchange_end_to_end.py
    OPENBLAS_NUM_THREADS=1 uv run --with 'numpy>=2,<3' python research/aspect/scc/scc.py check nima-source-exchange-end-to-end

Native response evaluation is exact rational arithmetic. Packet evolution and
measurement moments use tolerance1e-10. Report:
`research/nima/results/source-exchange-end-to-end.json`.

Next account explicitly for preparation, reset and control resources. Conserved
exchange budget does not make137 mode displacements, vacuum resets, pulse
controls or a phase-reference apparatus free. This is an executable remaining
audit, separate from the unresolved source selection and physical coupling.
