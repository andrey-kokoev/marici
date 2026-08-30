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

## Finite-bandwidth completion gates

The finite-bandwidth packet is now represented by five deliberately separate
interfaces. Integer frequency sampling factors through `ZMod N`; shifting by
one sample rate leaves the sampled class unchanged. The four-sample fixture
proves that the distinct integer frequencies one and five alias, so sampling
is not faithful on unrestricted frequencies. This is a finite quotient and
not a continuum Fourier or reconstruction theorem.

A three-bin spectrum projected onto its first two detector bins has an
explicit nonzero out-of-band kernel vector. The spectra `(1,2,3)` and
`(1,2,-3)` are distinct and have identical retained records. Injectivity is
recovered only on a witness-carrying subtype whose third bin is declared zero.
Thus bandlimiting is source-side data rather than a conclusion inferred from
a zero detector record.

Discrete causality uses signed time with nonpositive indices declared present
or past. The three-tap response
`u(0) + (1/2)u(-1) + (1/4)u(-2)` respects equality of complete past histories.
An advanced tap reading `u(1)` fails the same property: the zero stream and a
unit future pulse agree at every nonpositive time but give different present
outputs. A fitted response row therefore carries no causality authority until
its time order is supplied.

For the stable impulse response with squared energy `(1/4)^n`, Lean proves the
infinite energy sum `4/3`, the first-three-sample energy `21/16`, and the
strictly positive omitted tail `1/48`. Summability is proved by the geometric
series theorem. Stability therefore does not make a finite window complete.

The pointwise/uniform distinction is represented by singular values
`1/(n+1)` and inverse gains `n+1`. Every finite sample has an exact inverse,
but the inverse gains exceed every real bound. This is the operational dual of
the existing `DirectLimitReflection` lower-metric-bound hostile, not a new
universal completion abstraction.

Finally, `SameFinitePrefix` and `FinitePrefixDetermines` isolate the logical
descent condition for any supplied asymptotic readout. A zero stream and a
stream that becomes one at the cutoff agree throughout the observed prefix.
Any readout separating them cannot factor through that prefix. The theorem is
kept abstract because an eventual value is not silently interchangeable with
a Cesàro mean.

The positive-impedance/dark-reflection overlap between Nima and Aspect is
represented first on the real axis and then on the complex right half-plane.
For fixed positive scale `a`, the normalized impedance `Z(s)=s/a` has strictly
positive real part whenever `Re(s)>0`. After the unit-reference Cayley
constructor, the matched probe lies in that half-plane and has reflection
zero; the reduced reflection denominator vanishes at the opposite probe
`s=-a`. This refutes transport of nonvanishing from impedance to reflection
while keeping the two port quantities distinct. It does not certify seam
unitarity, identify an off-seam exponential probe with a physical-frequency
measurement, or construct a complementary energy port.

The reciprocal denominator-sewing packet contributes one further shared
finite law. For a scalar retained block `a`, static couplings `b,c`, and
boundary block `e`, Lean proves
`det([[a,b],[c,e]]) = a (e-c a^-1 b)`. At first-jet level it proves that the
full-minus-retained logarithmic determinant increment equals the logarithmic
first jet of the Schur factor. The Schur derivative retains the mixed term
`c a^-1 a' a^-1 b`. In the hostile fixture `a=2`, `a'=b=c=1`, and `e'=0`,
that mixed contribution is `1/4`; using only the diagonal derivative gives
zero and is wrong. This is exact one-mode boundary elimination, not a
continuum determinant line, locally uniform mode limit, or physical bath-port
dilation.

Determinant first jets are also packaged as basepoint value/derivative pairs.
Their logarithmic increments telescope through every intermediate retained
block. Two mode-addition orders with common endpoints therefore have equal
total increments even when their local increments differ. The explicit
hostile produces local pairs `(1,3)` and `(2,2)`: both sum to four, but the
first increments are unequal. Global determinant-line coherence thus does not
erase constructor order at intermediate stages.

The reciprocal sector double is certified at first-jet level. Reflection of
the spectral coordinate preserves the determinant value and negates its first
derivative. Multiplying the direct and reflected jets gives squared basepoint
value and zero first derivative. The hostile starts from value two and first
derivative three: both unsown sector derivatives are nonzero, while the sewn
odd jet vanishes. Cancellation after sewing therefore cannot be descended to
a vanishing claim in either individual sector. This is a basepoint jet
identity, not a global analytic functional equation.

The packet's three-mode determinant channels are represented directly in the
source eigenbasis with eigenvalues `1/2`, `1/4`, and `1/5`. The denominator
product is strictly positive at every positive rational probe. At probe
`1/2`, the selected Cayley numerator product vanishes while the denominator
remains strictly positive and nonzero. The reciprocal product of the positive
and reflected denominator polynomials is globally even. These are determinant
channels; the formalization does not infer their laboratory reconstruction
from one analyzer scalar.

The Hurwitz completion gate has an explicit hostile. At stage `n`, the
determinant channel is the constant nonzero function `(1/2)^n`. The same
geometric number is a probe-independent uniform error bound against the zero
function, and it tends to zero. Thus every finite stage is zero-free while the
uniform limit is identically zero. Local uniform convergence alone therefore
does not preserve nonvanishing; a source-fixed normalization, nonzero
basepoint, or explicit exclusion of the zero limit is indispensable.

The complementary positive gate is local and strictly weaker than a global
uniform lower bound. If the approximation error at a source-normalized
basepoint is smaller than the magnitude of the limiting value there, the
finite-stage value is nonzero. The normalized fixture
`1 + (1/2)^(n+1)` has exact error `(1/2)^(n+1)` from the fixed limit value one;
the error is always smaller than one and tends to zero. This blocks the
identically-zero collapse at the named basepoint. Propagating nonvanishing
from that point across a complex domain still requires analytic structure and
a Hurwitz-style theorem.

Logarithmic determinant jets now carry nonvanishing as part of their type.
Reflection preserves this subtype and negates its logarithmic slope;
multiplication preserves it and adds slopes; reciprocal sewing consequently
has slope zero. The hostile raw jet `(value,first)=(0,1)` demonstrates why the
witness matters: Lean's totalized rational division assigns the untyped
formula `first/value` the number zero, but no nonvanishing logarithmic jet can
have that underlying record. A computed quotient is therefore not authority
for a logarithmic derivative when its denominator gate is absent.

Ordered determinant paths now have a parallel typed increment API. Typed
increments telescope and two typed constructor orders with common endpoints
have equal totals. The raw API is retained as algebraic history and supplies a
hostile: a zero-valued intermediate with derivative seven receives totalized
logarithmic slope zero, producing raw increments `-1` and `5` that telescope
numerically to four. No nonvanishing typed jet can represent that intermediate.
Numerical telescoping is therefore weaker than an admissible determinant-line
path and cannot by itself certify effective descent.

The schematic typed path is now instantiated by Aspect's actual source-fixed
three-mode matrix. Exact determinant values and derivatives at `z=0` were
derived read-only from the packet checker, not replaced by normalized
value-one coordinates. All four base/intermediate/full stages have explicit
nonzero witnesses. Order `(1,2)` has increments
`497817076/679033509` and `98569/122430`; order `(2,1)` has increments
`3076504369/3821955330` and `5053/6891`. The first increments differ, while
both typed totals equal `853149/554630`, exactly matching the checker export.

The first actual boundary addition is replayed from the matrix entries rather
than only from exported increments. Lean recovers Schur value
`306075/221852`, nonzero mixed inverse-block derivative
`35212356/3076144369`, and full Schur derivative
`3111356725/3076144369`. Its logarithmic Schur jet equals the first typed path
increment exactly. Dividing the diagonal derivative one by the Schur value
does not equal that increment, certifying the checker’s deliberate
diagonal-only failure inside Lean.

Grothendieck's boundary-bearing cut and Aspect's retained-plus-tail energy law
share a finite discrete core. For rational sample streams, Lean proves exact
prefix-energy splitting at an arbitrary cut and exact three-piece energy
splitting under two staged cuts. A seam-only unit source has prefix energy one
while its translated two-sample tail has energy zero. Vanishing of the visible
tail therefore does not erase energy retained by the seam component. This is
labeled a finite-cut theorem; it does not establish Sobolev trace continuity,
closed image, or infinite-cutoff completion.

## Missing convention-fixed inputs

A common structure named `Instrument` remains withheld. The current packets
do not jointly fix:

- a post-measurement state-update or back-action map;
- positivity and normalization laws on a shared ordered state space;
- completely positive maps for quantum outcomes;
- detector memory, dead-time, or afterpulse state;
- a continuum temporal-mode or point-process completion;
- convergence from finite readout effects to a quantum stochastic model.

The finite-bandwidth promotion additionally still requires:

- named finite and continuum function spaces, measures, and a convergence map;
- a sampling normalization, anti-alias filter, and source-derived bandlimit;
- a continuum causal transfer prescription and radiation boundary condition;
- cutoff-independent operator and tail estimates;
- an infinite-time averaging functional, its index/denominator convention,
  and its convergence topology;
- noise spectral density normalized per unit bandwidth.

Amplitude readouts are complex-linear before intensity formation, whereas
probability effects are affine or linear on states. Treating both as the same
linear map would erase a known optics distinction.

## Verification status

The operator narrowly lifted the no-build direction for the targeted Lean
file and `lake build MariciFormal`, while continuing to prohibit the Marici
site build. The active operator prohibition still forbids Git inspection. The
new file contains no `sorry`, `admit`, or active conjecture assumption.

The verified snapshot is 131 theorem declarations and 118 definitions across
1836 lines. The module is imported by
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

The latest targeted elaboration took approximately 140 seconds despite a
small final finite-cut proof, compared with the earlier roughly 20--30 second
runs. This performance discontinuity is preserved as a module-scalability
warning. Further substantive optics increments should use a bounded successor
Lean module once targeted-build authority for that new file is explicit.

## Successor module boundary

The operator subsequently authorized continuation. New finite sewing work now
lives in `MariciFormal/FiniteCompletionSewing.lean`, which imports the stable
finite-instrument module. Existing declarations were not moved. The successor
defines energy over an ordered finite list of adjacent cut lengths and proves
that it equals the energy of the single prefix whose length is their sum. Its
hostile fixture proves that a zero translated tail does not determine the sewn
whole when a nonzero seam-bearing prefix remains.

This increment generalizes the common finite discrete law independently used
by Grothendieck's boundary-bearing cuts and Aspect's retained-plus-tail energy
accounting. It does not promote that law to an infinite cover, a completed
space, a continuous trace, or effective analytic descent.

Verification from `research/buzzard/marici_formal` succeeded with:

```powershell
lake env lean MariciFormal/FiniteCompletionSewing.lean
lake build MariciFormal
```

The targeted command exited zero without output. The project build completed
successfully with 8791 jobs. No Marici site build or Git command was run.

The successor also distinguishes the ordered local segment record from its
summed sewn total. Lean proves that summing `segmentEnergyRecord` recovers
`segmentedPrefixEnergy`, and that splitting one leading cut into two adjacent
cuts preserves the total. A second-sample unit fixture gives local records
`[0, 1]` and `[1, 0]` for cuts `[1, 2]` and `[2, 1]`, respectively, while the
sewn totals agree. Thus finite refinement coherence does not identify local
allocations; moving-seam invariance would require an additional transport or
comparison interface.

That smallest comparison interface is now formalized. `mergeLeadingRecord`
coarsens a refined record by adding its first two adjacent contributions.
Lean proves that splitting a leading cut and then applying this map recovers
the unsplit local record exactly. The map is not injective: `[0, 1]` and
`[1, 0]` have the same coarse image. Thus refinement supplies a commuting
coarsening cell but no inverse reconstruction and no equality between the
fine and coarse presentations.

Three-piece refinement now carries its own coherence boundary. Lean proves
that merging the first pair and then merging again agrees with merging the
second pair and then merging, using rational addition's associativity. The
reusable `CoherentBinarySewing` structure stores a binary sewing operation and
its associator rather than inferring triple coherence from pairwise
availability. Integer subtraction is the hostile model: it is a total binary
operation, but the two three-piece parenthesizations at `(1, 1, 1)` disagree.
This is the finite algebraic content of the folded square, not an assertion of
analytic or completion-level descent.

Finite refinement is additionally packaged as
`RecordCoarseningCertificate`: the fine and coarse records, actual comparison
map, record equation, and sum-preservation law are separate fields. The
leading-cut split constructs this certificate from `mergeLeadingRecord`.
Equal totals are derived from the certificate. The converse is rejected by a
Boolean-labelled fixture whose two records have equal aggregate sums but are
not compatible with the declared identity label transport. Aggregate
agreement therefore cannot manufacture source-indexed transport data.

The refinement certificates now form a typed partial composition system.
Identity is available on every finite record. Two certificates compose only
with an explicit equality between the first coarse record and the second fine
record; the resulting comparison map is their function composite and still
preserves total energy. The records `[0, 1]` and `[1, 0]` have equal sums but
are unequal, providing the hostile intermediate that aggregate equality does
not type. This is a partial-category boundary, not an assertion that every
equal-total presentation admits transport.

The finite partial category laws are now checked at certificate level, not
only at the level of comparison functions. Certificate extensionality follows
from equality of the fine endpoint, coarse endpoint, and coarsening map; the
remaining fields are propositions. Lean then proves left identity, right
identity, and associativity for every pair of explicitly supplied intermediate
record equalities. This completes the finite categorical increment while
retaining partiality at the source-indexed boundary.
