# Aspect finite instrument-readout audit

Owner: `marici.Buzzard`

## Admission decision

The shared finite abstraction is a calibrated readout, not yet a quantum
instrument. Aspect supplies independently checked optical readouts, while
Strominger supplies finite port families and Flavor supplies calibrated
detector maps. This supports shared theorems about kernels, faithfulness,
calibration, and post-processing without identifying the sector carriers.

## Lean increment

`marici_formal/MariciFormal/FiniteInstrumentReadout.lean` proves:

- source-coordinate linear equivalences preserve readout faithfulness;
- outcome-coordinate linear equivalences preserve readout faithfulness;
- deterministic linear post-processing can only enlarge the readout kernel;
- injective post-processing preserves that kernel exactly.

At the set-level interface it also proves that deterministic post-processing
preserves every existing observational identification, and that a faithful
processed record implies the original record was already faithful. This
statement applies equally to nonlinear intensity records and finite
statistical records without pretending they are amplitude-linear.

The positive cross-sector interpretation is deliberately narrow. In Aspect,
the maps are calibrated optical amplitude or state readouts. In Strominger,
they are finite observation ports. In Flavor, they are pre-registered detector
coordinate maps. No theorem transports physical source authority between
those sectors.

The Aspect homodyne fixture is now explicit: two coordinate quadrature rows
are scaled by a declared local-oscillator amplitude. They are jointly faithful
on the two-coordinate displacement class exactly when that amplitude is
nonzero. At zero amplitude every row collapses to the zero map. The theorem
certifies the finite calibrated mean map only; it does not select an absolute
phase, construct a local-oscillator field, or supply continuum detector
dynamics.

Mode matching is typed as an additional multiplicative calibration. The
effective quadrature strength is `localOscillator * overlap`, so the two-row
family is jointly faithful exactly when both factors are nonzero. In
particular, a live local oscillator with zero overlap gives only zero rows.
This prevents local-oscillator presence from being used as authority for an
orthogonal temporal, spatial, polarization, or frequency mode.

Balanced subtraction is certified in the packet's half-intensity convention.
Matched unit gains give exactly `2 signal localOscillator`. With zero signal,
unequal gains leave `(gainPlus-gainMinus) localOscillator^2 / 2`; the explicit
unit versus `9/10` gains at local-oscillator amplitude ten leave residual five,
where matched gains give zero. Gain balance is therefore an input calibration,
not a conclusion licensed by a centered trace.

The rescaled heterodyne mean family is instantiated by the two coordinate
ports and is jointly faithful on the declared displacement class. Noise is a
separate field: heterodyne variance is intrinsic variance plus the unused-port
variance. With both vacuum contributions equal to `1/2`, homodyne variance is
`1/2` and heterodyne variance is one. Thus faithfulness of the mean map does
not license two simultaneous noiseless quadrature values for an event.

Reciprocity is tested in a common energy metric rather than by raw displayed
matrix symmetry. The normalized `3-4-5` mirror is symmetric and orthogonal.
After unequal port-coordinate scaling its displayed matrix is nonsymmetric,
but it satisfies `G S = S^T G` for the transported metric
`G=diag(1/4,1)`. This exact cavity/control fixture prevents coordinate
calibration from being mistaken for physical nonreciprocity.

The minimal two-path interferometer is also instantiated without adding a new
shared object. It reuses the existing rational Hadamard port family as the
balanced recombiner. The symmetric nonzero route state has bright value two
and dark value zero, while the complete two-port family is jointly faithful.
This certifies the exact distinction between a selected dark amplitude and
annihilation of the pre-readout route state. The omitted common normalization
does not affect the kernel statement.

The dark detector is additionally packaged with the existing authorized-port
type. Its executable map is present, it is provably distinct from an
unavailable port, and its value on the symmetric route state is zero. Thus
availability, presence of a detector map, and the map's value on a particular
state occupy three separate typed facts.

Finite loss is represented by a retained-plus-environment dilation. For
rational coefficients satisfying `retained^2 + environment^2 = 1`, the full
two-port output preserves squared amplitude, and omitting the environment
loses exactly its intensity. The exact `3/5, 4/5` witness yields retained
intensity `9/25`, environmental intensity `16/25`, and total intensity one.
This certifies the finite conservation identity without claiming that a
completion manufactures the dilation or that the environmental port is
experimentally accessible.

## Hostile finite fixtures

The same Lean file records three distinctions required by Aspect's packets:

- intensity is unchanged by a nontrivial quarter-turn phase rotation;
- integrated two-bin counts do not retain arrival-bin order;
- threshold clicks identify one photon with two photons and hence are not
  number resolving.

The threshold hostile is also realized by two normalized nonnegative diagonal
photon distributions: the certain one-photon and certain two-photon sources
are distinct but have the same no-click/click distribution. Thus the failure
is present on the physical probability simplex, not merely in the ambient
signed vector-space kernel.

The finite two-photon inefficiency law is included separately as an outcome
distribution. For efficiency `eta`, the detected counts `0,1,2` have weights
`(1-eta)^2`, `2 eta (1-eta)`, and `eta^2`. The weights normalize for every
rational `eta` and are nonnegative on `0 <= eta <= 1`. At `eta=9/25` the exact
distribution is `(256/625, 288/625, 81/625)`. This supplies the declared
finite binomial law but not detector back-action, event identity, or a
continuum counting process.

Under the separately declared independent Bernoulli dark-count law, the mean
and variance contributions are added explicitly. Subtracting the calibrated
dark mean recovers the optical mean but leaves the variance increment
`d(1-d)`. For `eta=9/25` and `d=1/10`, the observed mean is `41/50` and the
variance is `1377/2500`, strictly larger than the optical variance. Correlated
backgrounds, dead time, and afterpulsing remain outside this independent
finite fixture.

Mean intensity is shown nonfaithful even before detector noise. The certain
one-photon distribution and the equal mixture of zero and two photons are both
valid probabilities with mean one. Their variances are respectively zero and
one, and their normalized second factorial correlations are respectively zero
and one. Thus a scalar mean cannot be promoted to authority for the full
photon-number law.

Finite counter truncation is tested with an overflow-only probability source.
Silently dropping the overflow coordinate maps this valid nonzero source to a
zero record whose displayed probabilities sum to zero. Retaining the overflow
coordinate gives the identity finite record and is faithful. An overflow
effect is therefore part of normalization and typing, not optional display
metadata.

A fourth hostile projects a faithful two-coordinate linear record to its first
coordinate and loses faithfulness. These examples prevent calibration,
intensity, temporal integration, and detector coarsening from being conflated.

Temporal integration is generalized from the single early/late witness: total
count is invariant under swapping arbitrary two-bin arrival records. The
identity time-resolved record is faithful before this processing, while the
explicit `(1,0)` and `(0,1)` records witness strict information loss. No later
deterministic processing can recover that erased ordering by the general
post-processing theorem.

The quantum-eraser marginal warning is represented by two valid binary joint
probability records. One correlates route and marker; the other anticorrelates
them. They are unequal but have identical flat route and marker marginals.
Consequently marginal intensity cannot identify the global correlation
pattern, the entanglement locus, or which factor carries the distinction.

Marker postselection is typed as taking a slice of an already supplied joint
record. The unconditional route marginal is definitionally the sum of its two
marker slices. The correlated and anticorrelated fixtures have the same route
marginal but different marker-zero slices. Selection can therefore expose a
stored correlation while carrying no production authority over the earlier
joint record or its marginal.

The intensity statement is generalized to every rational orthogonal phase
rotation with parameters satisfying `cosine^2 + sine^2 = 1`. The quarter-turn
remains the explicit unequal-amplitude witness. This records phase-orbit
invariance without manufacturing a phase origin or conflating the nonlinear
intensity map with the linear amplitude carrier.

## Missing convention-fixed inputs

A common structure named `Instrument` remains withheld. The current packets
do not jointly fix:

- a post-measurement state-update or back-action map;
- positivity and normalization laws on a shared ordered state space;
- completely positive maps for quantum outcomes;
- detector memory, dead-time, or afterpulse state;
- a continuum temporal-mode or point-process completion;
- convergence from finite readout effects to a quantum stochastic model.

Amplitude readouts are complex-linear before intensity formation, whereas
probability effects are affine or linear on states. Treating both as the same
linear map would erase a known optics distinction.

## Verification status

The operator narrowly lifted the no-build direction for the targeted Lean
file and `lake build MariciFormal`, while continuing to prohibit the Marici
site build. The active operator prohibition still forbids Git inspection. The
new file contains no `sorry`, `admit`, or active conjecture assumption.

The verified snapshot is 65 theorem declarations and 54 definitions across
864 lines. The module is imported by
`MariciFormal.lean`, and its sole direct import is
`MariciFormal.FiniteObservation`. The exact commands were run from
`research/buzzard/marici_formal`:

```powershell
lake env lean MariciFormal/FiniteInstrumentReadout.lean
lake build MariciFormal
```

The targeted command initially exposed proof-shape and finite-normalization
defects. Those were repaired in the owned file. Its final run exited zero with
no output or warnings. The library build then exited zero with:

```text
Built MariciFormal.FiniteInstrumentReadout
Built MariciFormal
Build completed successfully (8790 jobs).
```

Neither command ran or authorized the Marici site build. Narrow verification
authority was requested at graph event
`ev-000000004981-4d6c2356-6844-4822-913a-423d67512b5f` and was subsequently
granted directly by the operator.
