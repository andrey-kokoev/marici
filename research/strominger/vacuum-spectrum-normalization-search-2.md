# Search 2: photon successors, common vacuum, and signed-record spectra

## Strongest recovered construction

`research/voevodsky/prior-coupling-clues-recovery.md` points to `finite-record-mediator-constructor.md`. This already constructs two source-controlled signed record gates:

    R_plus=(I-S) tensor I+S tensor X,
    R_minus=-(I-S) tensor I+S tensor X.

With the prior uniform rule Q_R=(I-R)/2,

    Q_plus+Q_minus=I-S tensor X.

Keeping the scalar term is essential. With one record, occupation n=(I-Z)/2 and the prior supplied lambda=1/2, the law is H=n+lambda(I-SX).

Fresh exact verification gives:

| Control branch | Spectrum | Transition gap |
|---|---|---|
| Inactive / empty S=0 | 1/2, 3/2 | 1 |
| Matched S=1 | 1-sqrt(2)/2, 1+sqrt(2)/2 | sqrt(2) |

Its occupied-minus-common-vacuum ground shift is **(1-sqrt(2))/2 < 0**. These are explicit constructed spectra, but a neutral dressing law rather than the positive charging spectrum sought for the neutron.

The existing 21 transported satisfied-seam controls S_e=I-P_e pass the projector condition needed by the constructor. This is a compatibility test, not selection of those signed extensions by the original neutron process. The occupation gap, signed-gate admission and normalized-pool strength remain declared inputs in the original construction.

The negative shift is the already known dressing mechanism, now traced to its explicit signed-gate diagonal and conditional spectra; it is not presented as a new explanation of vacuum instability.

Fresh checker:

    python research/strominger/checkers/check_recovered_signed_register_spectra.py

Seven checks passed. Receipt: `results/recovered-signed-register-spectra.json` in this research directory.

## Followed physical-normalization successor, not only the first attempt

The finite-record note tests identifying its elementary gap with the electron rest energy and obtains about 71.36 keV rather than the retained 1293.33 keV neutron-proton splitting.

Its completed successor `interacting-elementary-reference.md` uses the actual full rank-two electron spinor and the SAME field law. The elementary gap is then 3/4 in the chosen unit; the comparison becomes about 95.15 keV, still excluded. Changing positive dark-spinor defect weights cannot repair that particular ground-energy comparison.

These are held-out calibration failures, not evidence that no field constructor exists. The current search does not reuse the empirical mass reference to fit a missing factor.

## Photon construction and its actual successors

Read the chain:

1. `research/nima/photon-creation-state.md`: normalized Fock state, added vacuum and CCR; no source gap selection.
2. `photon-momentum-wavepacket.md`: explicit normalizable light-cone packet and exact moments. Doubling supplied radial support doubles energy at unchanged norm and seed. Its mean energy is not a sharp source gap.
3. `photon-source-emission.md`: an exact driven transfer with supplied Omega and form factor. Work is retained. At Omega equal to mean photon energy, the nonzero continuum variance still prevents autonomous free-energy conservation.
4. `photon-local-quantum-dynamics.md`: conserved local transition current with the source gap differentiated correctly; full coupling conserves parity, not exact excitation number. The positive-gap continuum dynamics are not closed by the next control.
5. `photon-coherent-herald.md`: an all-orders solvable driven control with a deliberately degenerate source. Radiation energy comes from external switching; profile, gain and physical units remain inputs.

Thus the photon branch supplies emission and work accounting, but does not deliver the missing inactive/matched register gaps or a selected physical energy scale. In particular its soluble zero-gap control cannot silently replace the unresolved positive-gap source.

## Common-vacuum matter/link branch

`research/voevodsky/open-flux-common-vacuum.md` supplies one common zero-background graph with explicit exterior charge and energy. Its constrained sector minima are exact within the declared classical norm-charge model.

The physical boundary rule is decisive: cross-face leads put belt energy above proton, while all-mode leads reverse the ordering. Beta and eta are supplied. The construction is not a quantized vacuum/register spectrum and cannot calibrate our two-level registers merely because it has an empty reference.

## Current delivery and remaining gate

Delivered: an explicit prior source-addressed **conditional** vacuum/register spectrum, exact compatibility tests with the transported controls, and the completed outcomes of its two physical-normalization trials.

Not delivered: physical admission selecting those gates, a positive source-selected charging gap, or an experimentally/operationally grounded energy conversion. The inspected prior constructions state these as additional inputs.

Next targeted search: follow the native signed-record admission/uniform-core chain and the retained action/phase calibration implementations. The question is whether either supplies more than an existential constructor—specifically the actual occupied/inactive operation and its action/reference calibration. Do not repeat the failed electron-gap rescaling or construct another oscillator fixture.

Only the new signed-spectrum checker was freshly run. The historical photon, field and held-out comparison results were read from their notes, not freshly rerun here.
