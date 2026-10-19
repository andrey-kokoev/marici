# Search 1: source-selected vacuum/register spectra and physical normalization

## Freshly recovered clues

### 1. A specific calibration protocol already exists

`research/nima/retained-clock-calibration-identifiability.md` distinguishes three operations:

- Angular source evolution, which leaves an external rate omega free.
- A timed first arrival at a specified source angle, which would identify omega; endpoint recurrence without winding information does not suffice.
- Horizontal connection transport around a calibrated canonical-area loop, giving unwrapped phase -area/kappa. This can identify an action scale, unlike common-endpoint rotor-phase comparisons where kappa cancels.

This is a constructive calibration lead, not a general impossibility result. The note explicitly leaves a native horizontal-transport implementation, physical area calibration and external clock admission open. Its ordinary unit-rescaling argument is separate from its restricted phase-observation nonidentifiability theorem.

The existing source-pulse and Clifford phase normalizations must be transported consistently before using a common kappa*omega energy conversion. Merely identifying two angular variables is not that transport.

### 2. Source-backed charging alternatives were already searched and tested

`research/voevodsky/prior-charging-law-search.md` recovers an existing matter/link kinetic-current action and warns that its older missing-adapter statement was superseded by `weighted-matter-link-adapter.md` and `open-flux-common-vacuum.md`.

`source-gauss-operator-charging.v1.md` gives an actual source-response spectrum with a shared vacuum, but its reduced one-occupation positive-coefficient family is excluded as a joint mass explanation: proton/elementary stays below one. Its beta, eta, boundary and quantization choices are supplied. This is a completed branch, not a new calibration proposal.

### 3. Concrete clocks do not automatically supply physical units

`radar-clock-admission-is-checked-without-inventing-physical-evidence.md` has concrete finite clock certificates and a separate physical-realization premise. Its proper-clock/c=1 convention and tick denominator are declared protocol data; the certificate does not manufacture a seconds calibration.

This prevents borrowing a large integer tick count from that branch and presenting it as the energy normalization of the neutron pulse model.

### 4. Other recovered constructions are useful but not a selected spectrum

- `native-square-controlled-hamiltonian.md` constructs source-derived projector generators after a declared linearization; its stated successor proves stronger state-image nonuniqueness. Endpoint operations and positivity do not select their continuous logarithm or physical rate.
- `bank-mixing-normal-form.md` derives an exact hidden-readout recurrence and tests coordinate equivalence, but retains mixer/adapter/metric/scale inputs. Its six-step return is not a physical clock.
- `interface-record-native-completion.md` supplies a genuine retained native comparison, but its numeric exponent is representation metadata rather than elapsed time.
- The coupling-recovery sections of `phase-occupation-persistence-frontier.md` point to conditional Maxwell/Fock photon constructions, signed-record vertices and source-compressed spinor/orbital spectra. Their physical interaction and energy-scale identification remain open in the inspected sections. Follow these sources rather than treating them as absent constructions.

No retrieved result so far selects the two conditioned register spectra for the new neutron/source-bank binding and gives their physical energy unit.

## Delivered executable inverse spectral contract

Rather than choose another epsilon/J/g fixture, invert the existing register law. Let r_v,r_b be the inactive and matched transition gaps, and n_v,n_b their ground occupations. Then

    epsilon=[r_v(1-2n_v)-r_b(2n_b-1)]/2,
    J=[r_v(1-2n_v)+r_b(2n_b-1)]/2,
    g²=r_v² n_v(1-n_v)=r_b² n_b(1-n_b).

The equality of the two g² readings is a nontrivial consistency gate. The conditional rest gap is 21(r_v-r_b)/2. Occupations are not necessary if only that gap is sought; they are necessary here to reconstruct and test the proposed common register law. The sign/phase of g needs an additional convention or coherent readout; the gap only needs g².

Fresh exact regression checks reconstruct both previous admissible parameter sets and reject an inconsistent pairing of a vacuum gap with another fixture's occupation. These are regression fixtures, not fabricated source observations.

```sh
python research/strominger/checkers/check_register_spectral_calibration_contract.py
```

Results: `research/strominger/results/register-spectral-calibration-contract.json`.

## Physical-calibration input contract

Under the separately implemented protocols:

    omega=theta_first/t_first,
    kappa=-calibrated_area/unwrapped_horizontal_phase,
    E_physical=kappa*omega*E_angular.

The last equation requires the pulse/phase-action normalization comparison and a common reference baseline; no numerical physical conversion is delivered by these symbolic formulas alone.

## Next search

Follow the recovered conditional photon/Fock energy construction, the signed-record coupling chain and the existing common-vacuum matter/link action. Look specifically for an admitted inactive-versus-matched spectral readout or a calibrated action/clock comparison, not another spectrum with supplied couplings.

Only the new inverse-contract checker was run this turn. The retrieved prior clock, Gauss, radar and formal checkers were read through their notes or source, not freshly rerun.
