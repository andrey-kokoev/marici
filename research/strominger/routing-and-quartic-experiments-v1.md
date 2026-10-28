# Two distinct experiments: task-relative routing and quartic interaction

Status: research proposals. These are separate experimental questions, not two interpretations of one measurement.

## A. Routing/access experiment: task-relative sufficiency

### Scientific target

Determine whether a reduced description remains sufficient under a restricted physical access task and fails at a predicted enlargement of that task.

### Object and model

The object is a persistent network configuration g in A4. In an ideal four-input/four-output routing network,

    y = P_g x; P_g e_s = e_g(s).

Fixing the source input s exposes only one column of the transfer matrix. Twelve configurations become four observational classes, each containing three configurations. All output-side A4 permutations preserve that quotient. Access to a second input distinguishes all twelve configurations. An input-side permutation preserves the quotient exactly when it fixes s.

These are exact finite-model results, checked in `checkers/check_port_access_sufficiency.py`. Adding a separately implemented Boolean pointer changes the corresponding predictive-state counts from 4/12 to 8/24; passive routing alone does not implement that pointer.

### Decisive measurement

Compare networks ABCD and ACDB (image-list notation). Both send input A to output A under the same initial conditions, and remain equal under common output-side permutations. Input B exits at B versus C. Test the restricted-task equivalence across held-out output-side compositions and then the predicted separation after enlarging input access.

Compare a full calibrated predictor with one retaining only the first-column class. A stronger variant uses an actual reduced device with explicitly limited retained state. Do not confuse hiding data with physically erasing a network configuration.

### Observables and controls

Complex transfer amplitude, phase, loss, and frequency/time dependence. Independently calibrate components and transports. Test for first-input leakage through unequal cable delay, phase, attenuation, mismatch, crosstalk, unused-port loading, and controller labels. No per-setting correction may force equivalence after seeing evaluation records.

### Interpretation

This is linear network identification and a test of task-relative reduction. The original signal probes a retained network configuration. It does NOT measure quartic interactions of the signal. Its scientific value must come from predictive reduction and the exact intervention boundary, not from unexpected linear RF behavior.

### Present disposition

Ideal-network bridge verified; physical architecture, inventory, tolerances and acquisition remain unspecified. Full analysis: `research/strominger/port-access-sufficiency-experiment-v1.md`.

## B. Quartic-interaction experiment: nonlinear response of the original signal

### Scientific target

Determine whether a source/probe and mode configuration selects a particular quartic interaction of the original field, with independently predicted coupling support, amplitude scaling, phase dependence, and endpoint dependence.

The object is now the interacting signal or physical field, not a hidden routing configuration. This addresses the operator's intended nonlinear target. It is NOT simply a measurement of fourth-order correlations in a linearly propagated signal.

### First theoretical obligation: identify what is quartic

A quartic potential or Hamiltonian, for real mode coordinates, may take the candidate form

    V4(x) = sum_ijkl lambda_ijkl x_i x_j x_k x_l.

Its generalized force contribution is -dV4/dx_m, which is cubic in field coordinates. For complex amplitudes, a candidate resonant interaction term has the form

    H4 contains lambda_ijkl a_i a_j a_k* a_l* + complex conjugate.

Differentiation can yield a cubic drive proportional to a_i a_j a_k*. Under suitable mode and frequency conditions, this is four-wave mixing. These are conventional candidate forms, not terms derived from Marici in this document.

A quartic energy, a cubic field response, a quartic measured transfer term, and a fourth-order correlation are different claims. Select the actual governing term and measurement map before specifying a scaling test. With three equally scaled undepleted inputs and otherwise fixed response, an isolated cubic generated field can scale as A^3 and its power as A^6. Pump fixing, interference with a seed, saturation and depletion change the measured scaling. A measured fourth power alone does not identify a quartic interaction energy.

### Candidate medium-level design

1. Derive the physical mode encoding and the interaction term from the intended Marici formulation. Specify the source/probe labels, tensor symmetries, units, frequency conditions and mapping to detector observables.
2. Choose a characterized nonlinear medium or circuit capable of the derived interaction. The current KrakenSDR receiver plan supplies no such nonlinear element by itself.
3. Prepare coherent input modes with separately controlled amplitudes and phases. Scan them independently, rather than fitting one common power sweep only.
4. Measure complex generated responses at predicted mixing frequencies and/or nonlinear phase shifts. A possible channel is omega_l = omega_i + omega_j - omega_k, with predicted phase combination phi_i + phi_j - phi_k plus the calibrated coupling/transfer phase.
5. Estimate a shared coupling model from calibration data. Predict held-out amplitude/phase settings, mode combinations and source/probe choices without fitting each response separately.
6. Test the proposed coupling-support rule: which coefficients vanish, which survive, and which relations hold between them. Compare with a conventional nonlinear circuit/material model under the same data access.

### Possible tetrahedral connection

A tetrahedral structure could constrain the support or relations of lambda_ijkl. Four indices do not establish that geometry. A compelling result needs a pre-derived relation between the native labels and physical modes that predicts coupling zeros, phase relations, or endpoint changes beyond a diagram attached after measurement.

### Decisive result

A single independently constrained interaction model predicts held-out nonlinear response amplitudes and phases, including selected null channels and source/probe-dependent changes. To establish a distinctive contribution from Marici, derive the structural constraints before evaluation and show their explanatory or predictive benefit against conventional identification. Ordinary four-wave mixing alone is not that contribution.

### Rival mechanisms and controls

- Source-generated harmonics and intermodulation: characterize the incident spectrum at the nonlinear element, not just the generator settings.
- Receiver, amplifier, mixer or ADC nonlinearity: distinguish an upstream-generated product from a detector artifact through calibrated attenuation/location controls and an independent measurement path where available.
- Linear leakage at a nominally generated frequency: no-interaction/bypass and pump-off controls, with matched loading and documented changes.
- Lower/higher-order nonlinearities, cascaded quadratic processes, thermal drift and saturation: compare phase signatures, independent amplitude exponents, frequency dependence and an explicit alternative model.
- Apparatus asymmetries mistaken for coupling selection: repeated calibrated mode/port changes and held-out permutations.

Scaling is necessary evidence for some models but is not by itself a unique identification of a quartic Hamiltonian. Distinct mechanisms can yield the same effective cubic response.

### Present disposition

Concept proposal only. No Marici-specific quartic term, physical interaction element, quantitative prediction, tolerance, or acquisition protocol has yet been selected. The next step is source inspection and derivation, not wiring.

## Comparison and priority

| | A: routing/access | B: quartic interaction |
| --- | --- | --- |
| Physical object | Persistent network configuration | Interacting signal/field |
| Leading model | Linear transfer matrix | Nonlinear interaction and response |
| Main prediction | Boundary of a sufficient quotient | Coupling support, scaling and phase |
| Role of source/probe | Restricts accessible network columns | Prepares/drives and reads interaction channels |
| Established mathematics here | Exact A4 port-access quotient | Generic candidate interaction forms only |
| Next work | Assess realistic quotient-preserving hardware | Locate and derive the intended quartic term |

Retain A as an independent research proposal and possible calibration/composition methodology. B is the experiment aligned with the clarified interest in nonlinear effects of the original signal. A is not evidence for B and should not be described as its implementation.
