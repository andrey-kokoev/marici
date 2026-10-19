# Cavity/detector observation and resource interface

## Disposition

Constructed a source-specific model interface for both frozen targets. Contract: `contracts/physics-observation-resource-interface.v1.json`. The model interface is accepted by `contracts/physics-interface-geometry-admission.v1.json`; physical-source slots remain explicit.

The contract separates physical state, retained records, predictive state and observations. Every occurrence retains source/trial identity, step and predecessor, preparation/input/outcome, clock and calibration version. Equal outcomes do not identify histories. Physical execution is blocked in the executable model API.

## Cavity

Retain the complete incident ports `(u,v2,w)` and returning state x. At the charter's nominal coefficients,

`x_next = (36/125)x + (48/125)u + (9/25)v2 + (4/5)w`.

The full resource law is

`|x_next|²-|x|² = |u|²+|v2|²+|w|²-|y_r|²-|y_t|²-|y_e|²`.

All amplitudes use the same declared energy normalization. Their conversion to physical units, phase reference and clock requires independent calibration. Returning state is not automatically a measured port. With known input and calibrated coefficients, however, the scalar state reconstructs exactly as `x=(y_r+r1*u)/t1`. A dark reflected port does not erase storage; it also does not refute the scalar source's one-sample observability. Polarization and continuum-delay state are different domains.

## Detector

The physical memory is ready/dead. Its predictive belief r is a conditional probability, not a third physical memory state. The unnormalized outcome maps for a zero/one input n are

```
C(R,D) = (0, eta*n*R)
N(R,D) = ((1-eta*n)*R + gamma*D, (1-gamma)*D).
```

Their masses are outcome likelihoods. Normalize only positive-likelihood branches. Complete history probabilities equal products of conditional likelihoods; impossible records produce no posterior.

For no-click,

`f(r)=((1-eta*n)*r+gamma*(1-r))/(1-eta*n*r)`.

Its derivative is `(1-eta*n)*(1-gamma)/(1-eta*n*r)^2 >= 0`. Thus endpoints transport a readiness interval exactly on the domain of everywhere-positive likelihood. For the nominal probabilities and initial readiness interval `[1/4,3/4]`, a photon/no-click event gives `[43/91,57/73]`; the half-ready point gives `25/41`. Intervals containing impossible conditioning states require a support restriction and cannot receive an unconditional posterior certificate.

Photon number and readiness have different resource types. Each supplied photon is destroyed into counted or uncounted absorption. During empty-bin recovery, dead probability multiplies by `1-gamma`. Readiness recovery supplies no detector energy budget. Photon frequency, bias power, heat, clock and reset costs remain physical inputs.

## Physical and comparison gates

The interface lists six unresolved physical slots for each target: apparatus/preparation/control authority, calibration and clock, readout/resource evidence and frozen complete-record protocol. There are no admitted apparatus certificates or acquired records.

The two instruments retain distinct source IDs. Amplitude-to-photon preparation, quantization/Born pairing, routing and the common-source map remain separate constructions. The coherent-Gamma/Poisson controller does not replace the ready/dead instrument.

## Verification

The independent checker passes:

- 81 complete-port cavity energy/state-reconstruction cases;
- 252 detector history cases through three bins;
- 909 exact readiness-interval enclosure cases;
- eight rejected hostiles: reset, deleted no-click, mixed source, physical execution, impossible click, zero-likelihood no-click, unsupported interval conditioning and mixed resource units.

These are model tests. Record-shape validation and probabilistic replay are distinct checks. Source notes are hash-pinned; producer suites and receipts are untouched.

```
python research/nima/checkers/check_physics_observation_resource_interface.py
python research/aspect/scc/scc.py check physics-observation-resource-interface-v1
```

## Next iterations

Use this contract to choose and test an explicit common-source geometric candidate, then its operation law. Required preserved objects are the complex optical energy metric, classical memory simplex, ordered source histories and instrument/resource maps. An encoding of the imported laws remains conditional until the dynamics-selection task supplies independent source justification or a precise candidate obstruction.
