# Geometric KMS Horizon-Parallelization Audit

## Question

Can horizon geometry co-generate the temperature and signed splitting left
independent in WP812, thereby fixing a dimensionless portal bias without an
arbitrary reservoir scale?

## Admitted geometry and physical-time map

The source is a stationary horizon with nonzero surface gravity \(\kappa\).
Its Killing or modular flow supplies a genuine physical-time map for a
stationary detector. Hawking--Unruh thermality fixes

\[
\beta=\frac{2\pi}{\kappa}.
\]

The favorable portal hypothesis is that the same source fixes a detector or
flavor splitting

\[
\Delta=n\kappa,
\]

where \(n\) is an admitted integer representation weight. The flavor readout
is still required to descend to a weak-basis-invariant `physical16`
coordinate; no horizon chart variable is granted that authority.

## Exact scale parallelization

The thermal product becomes

\[
\beta\Delta=2\pi n,
\]

so the Gibbs orientation and transition ratio are

\[
B_n=\tanh(\pi n),
\qquad
\frac{\gamma_\uparrow}{\gamma_\downarrow}=e^{-2\pi n}.
\]

Both are independent of \(\kappa\). This removes WP812's continuous
temperature--splitting fiber. A common geometric renormalization
\(\kappa\mapsto c\kappa\) rescales temperature and splitting together and
preserves the prediction exactly. Conditional on \(n=1\), the bias is the
fixed nonzero number \(\tanh\pi\).

This is genuine progress: geometry can parallelize the source and detector
clocks so that an arbitrary dimensional scale cancels from a dimensionless
readout.

## Aspect germ-tester audit

Aspect's tester requires constancy on complete quotient fibers, evaluation at
the target's native arity, and independent source authority for the comparison
and realization cells. The endpoint-only horizon proposal fails all three.

The marked endpoint germs are:

```text
HorizonThermalGerm
  horizon_identity
  metric_and_state_provenance
  surface_gravity
  horizon_generator_orientation
  horizon_state_choice
  retained_frequency_port

FlavorSplittingGerm
  physical16_identity
  chiral_representation_provenance
  representation_weight
  portal_eigenvalue_scale
  retained_frequency_port

DetectorRealizationGerm
  detector_identity
  coupling_provenance
  physical_time_root
  bandwidth
  gain
  retained_frequency_port
```

These endpoints do not determine their attachments. Introduce a comparison
coefficient \(a\) by

\[
\Delta=a n\kappa.
\]

The same three endpoint germs with \(a=1\) and \(a=2\) give
\(\tanh(\pi n)\) and \(\tanh(2\pi n)\). Hence the target is not constant on
the quotient that forgets the comparison attachment. This is Aspect's fiber
failure.

The selector target has native arity three:

```text
horizon thermal germ
flavor representation germ
primitive frequency-comparison cell
```

The physical record has native arity four because the detector realization
germ is an additional argument. Calculating \(\beta\) from the horizon and
\(\Delta\) from a flavor ansatz separately does not authorize their common
frequency carrier or the detector attachment.

The smallest adequate object is therefore:

```text
GeometricKMSFlavorComparisonGerm
  horizon_thermal_germ
  flavor_splitting_germ
  detector_realization_germ
  common_physical_frequency_carrier
  horizon_frequency_attachment
  flavor_frequency_attachment
  detector_frequency_attachment
  horizon_orientation
  comparison_variance
  thermal_bias_target
  physical16_record_target
  source_authority
```

No current source supplies the flavor frequency attachment
\(\Delta=n\kappa\), the detector attachment, or a selector for the horizon
orientation. The calculation has therefore not yet produced a failed or
successful physical horizon selector. It has produced a deterministic
conditional result on a comparison germ whose decisive cell is not yet
source-authorized.

## Remaining orientation pair

The sign is relative to the horizon generator. Reversing that generator sends

\[
n\longmapsto-n,
\qquad
B_n\longmapsto-B_n.
\]

A future-oriented black-hole exterior and the reversed past/white-hole
construction supply the hostile pair at the level relevant to this audit.
Selecting the future horizon by collapse invokes a low-entropy boundary
condition. It is physical preparation data, not a consequence of the local
KMS relation.

Accordingly, the horizon does not reveal an absolute sign. It creates a
relational observable with respect to its selected modular or Killing flow.
Fixing that flow restricts the experiment to its stabilizer groupoid.

## Weight, rate, and threshold gates

Geometry alone does not select \(n\). The exact predictions \(\tanh\pi\) and
\(\tanh2\pi\) differ, so the representation weight must come from the same
flavor source rather than be chosen to match the answer.

KMS fixes a transition-rate ratio, not the absolute system--field coupling.
Multiplying both rates changes the physical relaxation clock without changing
the stationary state. The actual detector duration and bandwidth therefore
remain part of the instrument packet.

Common geometric threshold scaling preserves \(\beta\Delta\). An asymmetric
finite correction

\[
\Delta\longmapsto n\kappa+\delta

\]

changes it by \(2\pi\delta/\kappa\). Threshold protection requires a symmetry
or index theorem forcing every correction to retain \(\Delta=n\kappa\); shared
dimensional analysis is insufficient.

## Physical instrument and contextual partition

An Unruh--DeWitt-type transition counter is an executable instrument for the
rate ratio. It separates the two horizon-relative signs after a detector time
orientation and level ordering have been declared. It does not by itself map
the result to flavor `physical16`.

For a signed portal eigenvalue \(g_0\) and detector gain \(s\),

\[
R=s g_0\tanh(\pi n).
\]

The exact hostile pair \((g_0,s)=(1,2),(2,1)\) remains. Thus:

- fixed oriented horizon and fixed \(n\): unique thermal attractor and
  scale-independent bias;
- full horizon groupoid: future/past orientation pair;
- fixed geometry without flavor representation: discrete \(n\)-fiber;
- common geometric thresholds: protected dimensionless bias;
- asymmetric flavor thresholds: unprotected bias;
- transition counter: executable thermal instrument but no calibrated
  `physical16` portal map.

## Selector classification and smallest falsifiers

The geometric KMS operation is a conditional selector, scale parallelizer,
and executable relative probe only on the complete marked comparison germ. It
fixes a dimensionless thermal magnitude once the horizon orientation, integer
weight, and primitive frequency attachment are admitted. It does not select
those inputs, the portal eigenvalue normalization, the absolute rate, or
detector gain.

The smallest sign falsifier is the future/past generator pair. The smallest
magnitude falsifier is \(n=1\) versus \(n=2\). The smallest instrument
falsifier is the gain--portal pair above. A single horizon response therefore
does not establish the complete source.

## Deutschian appraisal

This is the closest algebraic architecture yet for magnitude: a common
geometric frequency carrier makes temperature and splitting inversely covary,
so their arbitrary scale cancels. Aspect's tester prevents treating that
written compatibility as source authority. The relationship becomes
explanatory only if the source constructs the primitive comparison cell. At
present the integer representation, horizon orientation, flavor attachment,
and detector realization are independent objects.

The precise successor is a chiral horizon-bound representation in which an
index fixes \(n=1\), anomaly inflow fixes the coupling to the faithful flavor
orientation, and the same localized detector interaction sets \(g_0\) and
gain. It must be tested on a formation geometry rather than an eternal horizon,
because formation is where the future orientation and low-entropy preparation
claim either gains or loses source authority.

## Assumptions and falsifiers

The positive result assumes stationary Hawking--Unruh KMS thermality and the
strong source relation \(\Delta=n\kappa\). That relation is a candidate, not a
flavor theorem. A full solution requires its derivation from the chiral matter
action, protection under finite thresholds, and a calibrated map to
`physical16`. A past-oriented solution within the same admitted formation
domain, a free representation weight, or an asymmetric threshold correction
falsifies absolute selection.

Primary sources: Hawking, [Particle Creation by Black
Holes](https://doi.org/10.1007/BF02345020), Sewell, [Quantum Fields on
Manifolds: PCT and Gravitationally Induced Thermal
States](https://doi.org/10.1016/0003-4916(82)90285-8), and Conroy,
[Unruh--DeWitt Detectors in Cosmological
Spacetimes](https://arxiv.org/abs/2204.00359).

## Disposition

Progressive algebraically but source-incomplete. Horizon geometry removes the
continuous thermal scale fiber only after a marked comparison attachment is
supplied. The endpoint-only proposal fails Aspect's fiber, native-arity, and
authority gates. The unresolved constructor must join chiral index, formation
orientation, flavor coupling, threshold protection, and detector calibration
to the geometry before the physical target is defined.
