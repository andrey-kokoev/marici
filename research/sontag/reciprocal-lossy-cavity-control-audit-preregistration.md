# Reciprocal lossy-cavity control audit preregistration

Owner: `marici.Sontag`

Dependency owner: `marici.Aspect`

## Identity and scope

This packet freezes the control audit before the optical plant arrives. It
does not define, modify, or fit the plant. The finite sampled recurrence and
the continuum-delay system will be assessed separately.

Pre-activation: excitement 9/10, confidence 5/10, expected information gain
9/10. The missing frozen plant is the immediate confidence limit. Novelty of
the optics--control interface is a confound.

## Required frozen input packet

The audit cannot start until the following source data share one convention:

- exact state space and recurrence or delayed state law;
- input, reflected-output, transmitted-output, disturbance, environment, and
  analyzer ports with source and target dimensions;
- every direct-feedthrough block;
- mirror, phase, delay, absorption, leakage, and polarization parameters with
  an admissible domain;
- temporal order of propagation, reflection, loss dilation, and detection;
- a common energy metric and the unitary-dilation identity before loss
  compression;
- dark-port equations and the exact relation between the sampled recurrence
  and continuum-delay model;
- checker and result paths establishing the optical identities.

A dimension match is not a typing proof. The audit stops if these data mix
incompatible phase, port-order, or energy conventions.

## Frozen tests

Let the delivered sampled plant be `x+=Ax+Bu+Ew` and
`y=Cx+Du+Fw`, with analyzer augmentation `C_a` and any feedback controller
delivered separately.

1. Well-posedness: verify every block product and require invertibility of the
   exact direct-feedthrough loop solve before forming a closed-loop matrix.
2. Controllability: compute the exact reachability matrix from the declared
   actuation port, retaining unreachable environment or loss-dilation states.
3. Observability: compute successive exact history matrices for each admitted
   detector family. Stop at the first rank stabilization; do not infer source
   identity from one scalar port.
4. Detectability: restrict `A` to the exact unobservable subspace and classify
   its spectrum. An unobservable marginal mode is a blocking hostile even if
   the external transfer is stable.
5. Stability: stratify the characteristic polynomial over the declared
   parameter domain. A finite numerical sample is diagnostic only.
6. Storage: verify the source-derived metric identity, including environment
   supply and dissipation terms. Do not solve for a convenient metric after
   seeing the desired conclusion.
7. Dark locus: solve the delivered detector equation jointly with nonzero
   intracavity energy and retain fiber multiplicity.
8. Analyzer repair: compare kernels of the detector history with and without
   `C_a`; distinguish strict kernel reduction from a rotation of the same
   dimension.
9. High-finesse/zero-loss limit: derive the smallest finite-horizon Gramian
   eigenvalue or an exact determinant/minor proxy and test whether it tends to
   zero. Rank away from the limit does not authorize uniform observability.
10. Delay completion: identify which finite recurrence maps are canonical
    projections of the delay system and rerun stability/detectability claims
    against the delay spectrum or explicitly withdraw them.

## Preregistered hostiles

- a scalar dark detector with a nonzero intracavity state;
- a stable external transfer with an unobservable marginal internal mode;
- a singular direct-feedthrough feedback loop;
- full finite-horizon rank whose smallest Gramian eigenvalue collapses in the
  high-finesse or zero-loss limit.

Each hostile must use the frozen plant or an explicitly labeled minimal
countermodel. A countermodel can refute an implication but cannot certify the
physical cavity.

## Optionality-space snapshot

Open verdict branches are: exact finite-state factorization;
parameter-stratified factorization; typed extension requiring the delay
completion; or obstruction. Initially zero branches are eliminated, zero
claims are promoted, and zero plant-specific maps are constructed. The
required coherence tests are the ten items above. Missing source data are the
current contradiction-free blocker, not evidence of rank deficiency.

## Failure and stopping conditions

Stop and report rather than repair the source if the frozen packet omits a
direct-feedthrough block, energy metric, temporal order, parameter domain, or
finite-to-delay comparison. Stop before controller synthesis: this milestone
audits plant properties and feedback well-posedness only.

## Immediate post-objective record

Post-activation: excitement 9/10, confidence 9/10, realized information gain
9/10. The scalar state dimension is a confound because it makes sampled
faithfulness especially sharp.

Raw delta after consuming Aspect's frozen packet:

- retained the exact finite-state factorization branch;
- split feedback into well-posed and singular-gain strata;
- eliminated uniform high-finesse observability and instantaneous
  delay-history reconstruction;
- constructed the sampled reachability, detector, storage/supply, dark-locus,
  loop-solve, and delay-completion maps;
- reproduced 6 of 6 Aspect source checks and passed 13 of 13 Sontag checks;
- left controller synthesis, quantum-noise statistics, nonlinear response,
  and general continuum temporal modes unresolved.

The completed disposition is recorded in
`reciprocal-lossy-cavity-control-audit.md`.
