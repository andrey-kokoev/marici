# Declared neutral-state extension

**12x12 fibration, state 50** adds an explicit candidate state-space extension after collective-cell materialization. It is not a derivation of neutron particles from the native replay.

## Construction and assumptions

`../realization-tower/neutral-state-extension.mjs` defines

    V_N = C^56_positive ⊕ C^56_negative ⊕ ker(Q),   dim ker(Q) = 14.

The site banks are attached to the 56 actual octahedral IDs, not to the two neutral-labelled corner tetrahedra. Both banks share geometric sites but their coefficient fields are independent in this NEW extension. The original native probe and its linked sheets remain unchanged. The fourteen residual coordinates use the explicit free-slot basis of `four-by-four-filler-model.mjs`; they are not copies of native residuals that already depended on five inputs.

A sparse embedding maps the 126 channels to 128 ambient coordinates: 112 site-channel coordinates plus sixteen filler slots. Charge readout is zero on the site-channel summands by declaration, and uses the existing candidate boundary rows on the sixteen slots. Each channel carries five complex coefficients, hence 630 complex coefficients in the extension. The embedded basis has rank 126 per coefficient. Independence follows from this declared direct-sum construction, not from physical/native dynamics.

No physical geometry is added. An inspected site channel is labelled N+ or N− at its existing octahedron. An inspected residual is labelled N* at the collective boundary port, as a port-fiber inspection marker, not a newly placed spatial cell. All original cells, histories, filler confirmation, and collective P/E counts remain retained.

## Viewer

Refresh and advance to state 50. The bottom-right **Added N channels** row shows 126 separately from raw cell counts and external P/E readings. In the neutral extension panel, select any channel and any of its five coefficients, then edit real/imaginary parts independently. The panel reports nonzero channels and the computed P/E boundary change. All values initially vanish: available dimensions are not occupied particles. Inputs are bounded to ±1,000,000 in the UI. Clear extension amplitudes explicitly resets them.

Values and channel selection persist across reload and process switches. Stepping backward disables the extension's presentation but retains its editable bank for later reuse. It does not silently overwrite either native sheet or its coefficients.

## Verification and remaining gap

`tests/neutral-state-extension.test.mjs` checks rank 126, all 1,260 real/imaginary basis perturbations across the five coefficients, fixed P/E boundary readouts, distinct banks at shared sites, preservation of geometry and charged carriers, invalid records, and settings round trips. `scripts/test-fibration12-process.mjs` edits both banks and a residual independently, verifies persistence and boundary neutrality, and checks backward removal and reset. Screenshot: `results/fibration12-viewer/neutral-extension.png`.

This supplies 126 independently adjustable **candidate neutral channels**, not 126 established neutrons. Boundary neutrality alone establishes neither neutron dynamics, particle occupancy, stability, nor a Pb-208 realization. Those remain open requirements; neither the native rank-five replay nor its two linked N sheets has acquired an unproved higher rank.
