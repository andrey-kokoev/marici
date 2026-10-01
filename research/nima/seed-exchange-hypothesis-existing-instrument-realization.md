# Operational hypothesis v1 already has a conditional instrument realization

## Recovered prior chain

The prior programme already contains:

- `exchange-oscillator-preparation-and-measurement.md`: controlled difference-mode Hamiltonian implementing the exact exchange;
- `labelled-exchange-experiment-compiler.md`: source-labelled witness/event adapter with separately attached memory;
- `exchange-detector-calibration-and-identifiability.md`: coherent homodyne predictions and calibration failure controls;
- `source-exchange-end-to-end-audit.md`: actual shared-leg matrix values through the conditional experiment;
- `exchange-shared-leg-composition-gate.md`: obstruction to treating addressed composite-label events as shared-leg factorizations.

Thus the candidate is not missing an abstract physical implementation. It is missing source selection and a binding of THIS six-seed-port task to that implementation.

## Reuse for the six-port candidate

The six-port probe calculation used q on 24 carrier coordinates and six distinct records. Convert its rational coordinates to Euclidean normalized amplitudes Q=q/sqrt(N), u_e=f_e/sqrt(N), where N=2 for endpoint-fixing probes or N=6 for transition probes. Record amplitudes w_e are unchanged.

In the prior oscillator framework, introduce carrier annihilation modes a_k and one record mode r_e per seed role. For the supplied unit vector u_e define

    c_e=sum_k u_e,k a_k,
    b_e=(c_e-r_e)/sqrt(2),
    H_e(t)=hbar*kappa_e(t)*b_e^dagger b_e.

The existing pulse formula S_e(theta)=I+(exp(-i theta)-1)d_e d_e^T, d_e=(u_e,-record_e)/sqrt(2), gives the exact real exchange at theta=pi. This algebra is independent of the original 16+137 mode census. Applying it to 24+6 modes is a conditional specialization, not a claim that the old source-labelled compiler has already been instantiated for these seed paths.

Both probe hypotheses can be implemented by selecting different carrier supermodes while retaining the same six record ports. Their hardware selection is a physical input. Equal endpoint-fixing supermodes for AB and BA do not merge the two record modes.

## One discriminating ideal protocol

1. Prepare carrier vacuum and record AB in a coherent state of real amplitude A, with the other records in vacuum.
2. Apply an AB pulse of area pi, then a BA pulse of area pi. Do not reset or measure between them.
3. Homodyne-read the final BA record with a retained phase reference.
4. Compare with a separate reference trial preparing BA directly with the same amplitude A and the same detector calibration.

The previously computed amplitude ratio is 1 for endpoint-fixing probes and 1/3 for transition probes. In the ideal coherent model the BA quadrature mean is respectively sqrt(2)A and sqrt(2)A/3; its variance remains 1/2. With stable common loss/gain/phase conditions and nonzero reference mean, offset-subtracted population mean ratios retain 1 versus 1/3. This imports the existing detector assumptions; it is not a finite-sample inference or observed experiment.

This is a TWO-DIFFERENT-PORT transfer test, not the prior two-identical-pulse echo discriminator. Its controls must not be conflated with the old exchange-versus-quarter-turn test.

## Costs and authority not supplied by the calculation

The oscillator construction assumes standard bosonic mechanics, coherent preparation, phase-locked detection and controllable supermode coupling. The Hamiltonian requires the stated diagonal frequency shifts as well as coupling; a bare beam-splitter coupling has different phases unless compensated. Pulse area does not determine duration or frequency. A preserved excitation budget is not automatically laboratory energy conservation when pumps or unequal frequencies are involved.

No native source rule selects this instrument, feature realization or detector. The existing compiler validates supplied witness boundaries but explicitly treats instrument attachment as an assumption. The actual primitive seed rows have not acquired those witnesses by this proposed experiment.

## Composition warning and its scope

The old 137-port model assigns one independently addressed exchange to each COMPOSITE comparison label. Its exact rectangle test rejects factorization of those events into invertible shared primitive legs on one state space.

Our six-port proposal instead assigns events to primitive occurrences and defines composite path action by their ordered product. It must not import the old 137-composite-label map or claim the old obstruction has vanished. These are different instrument-addressing contracts. Neither establishes physical equivalence of distinct seed paths, and both must retain actual temporal histories.

## Fresh verification

    OPENBLAS_NUM_THREADS=1 uv run research/nima/checkers/check_exchange_oscillator_instrument.py
    python research/nima/checkers/check_exchange_shared_leg_composition.py

Both original checkers freshly pass. Their reports are refreshed. The six-port rational predictions were checked in the preceding `check_seed_probe_exchange_bridge.py` run; no new six-port native witness compiler, hardware execution or detector experiment was performed here.

## Decision point

Operational hypothesis v1 now has an explicit conditional preparation/control/readout interpretation using existing work. The next substantive step is NOT another recovery or pulse checker: either identify a source construction selecting this task, or choose to investigate it as an externally specified experimental model. Do not describe conditional implementability as a derivation of the physical seed cycle.
