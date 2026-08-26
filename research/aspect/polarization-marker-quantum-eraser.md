# Polarization marker and quantum eraser

Owner: `marici.Aspect`

## Bounded question and tensor typing

Consider a predeclared two-path apparatus on

`H_route tensor H_pol tensor H_marker tensor H_environment tensor H_detector`.

The source prepares route amplitudes before any detector projection.
Polarization may act as an accessible marker; leakage may carry additional
which-route information into an inaccessible environment. Detector outcomes
are records downstream of these factors. Conditioning those records never
changes the earlier source state.

## Global state and reduced route state

After marking and before recombination, suppressing a common polarization
factor, the normalized pure state is

`|Psi> = (|0>|mu0> + exp(i phi)|1>|mu1>)/sqrt(2)`,

where each `|muj>` belongs to polarization, marker, and environment jointly.
Write `gamma=<mu0|mu1>`. Tracing every non-route factor gives

`rho_route = (1/2) [[1, gamma* exp(-i phi)],
                     [gamma exp(i phi), 1]]`

for real `gamma`; the complex case replaces the lower entry by the conjugate
of the upper. A balanced recombiner gives unconditional intensities

`I_plus = (1 + Re(gamma exp(i phi)))/2`,

`I_minus = (1 - Re(gamma exp(i phi)))/2`.

Thus orthogonal total marker states (`gamma=0`) erase marginal fringes while
the global state remains a coherent pure superposition. The off-diagonal term
has moved into cross-factor correlations; it has not been destroyed globally.

For normalized pure markers with equal priors, visibility and optimal
which-route distinguishability are

`V=|gamma|`, `D=sqrt(1-|gamma|^2)`, hence `V^2+D^2=1`.

The checker uses the exact 3-4-5 witness `gamma=3/5`, `D=4/5`.

## Conditional eraser outputs and event order

For orthogonal polarization markers `|H>` and `|V>`, predeclare the
complementary analyzer basis `|+>=(|H>+|V>)/sqrt(2)` and
`|->=(|H>-|V>)/sqrt(2)`. Conditional route states are proportional to

`|0> + exp(i phi)|1>` and `|0> - exp(i phi)|1>`.

Their detector fringes and antifringes cancel in the unconditional mixture.
At zero phase the only nonzero joint records are `(bright,+)` and `(dark,-)`,
each with probability `1/2`. Choosing or reading the analyzer after the route
detection merely partitions already-recorded joint events. It cannot rewrite
the source preparation, marking interaction, or past marginal distribution.
The analyzer basis must be frozen before inspecting outcomes; otherwise the
exercise is model selection on the same records, not a prospective test.

## Environment port and recoverability boundary

Accessible marking and environmental leakage are not interchangeable. The
states

`(|0>|H>|e> + |1>|V>|e>)/sqrt(2)` and

`(|0>|+>|e0> + |1>|+>|e1>)/sqrt(2)`

have identical flat route marginals when `<e0|e1>=0`, but the first stores the
distinction in the accessible marker while the second stores it in the
environment. An analyzer on polarization can erase the first marker. It
cannot recover coherence lost by tracing an orthogonal inaccessible
environment. Equal marginal intensities do not identify global entanglement.

## Local oscillator and phase authority

A homodyne port mixes the signal with a nonzero local oscillator of declared
phase `theta_LO`. Its quadrature row measures phase relative to that reference.
Without the local oscillator, the transformations

`signal -> exp(i alpha) signal`

act freely on the unreferenced phase convention. The possible phase origins
form a `U(1)` torsor: there is no distinguished zero and hence no absolute
phase observable. Intensity and `|gamma|` remain invariant. Fitting an
unreferenced phase is gauge choice, not measurement.

## Smallest faithful detector family on a declared class

Declare the reduced-state class to be equal-population route qubits

`rho(c)=[[1/2,c],[conj(c),1/2]]`, with `|c|<=1/2`.

Two balanced detector contrasts with predeclared reference phases `0` and
`pi/2` recover `Re(c)` and `Im(c)` and are minimal on this two-real-parameter
class. One row leaves a one-real-dimensional kernel. This detector family is
not faithful on global purifications: marker basis, entanglement locus,
environment allocation, inaccessible phases, and distinct purifications with
the same reduced `rho(c)` remain invisible.

## Hostile falsifiers

1. Equal marginal intensities are used to identify different global
   entanglement patterns.
2. The eraser basis is fitted after outcome inspection and reported as
   predeclared.
3. Postselection is promoted from record sorting to source-state authority.
4. Absolute phase is claimed without a nonzero local oscillator or equivalent
   phase reference.
5. Orthogonal environmental leakage is called recoverable by acting only on
   the accessible marker.

Each is rejected by an exact checker gate.

## Conceptual bridge and claim boundary

Marginal scalar cancellation can coexist with a nonzero oriented route state
and with coherence stored in correlations. This is the same typed warning as
the dark-port interferometer: a vanished scalar projection is not annihilation
of its source object. This packet makes no Riemann-hypothesis claim or analogy
of evidential force.

## Completion gate

Promotion beyond the finite tensor fixture requires a declared temporal-mode
space, detector instrument, environment accessibility algebra, causal ordering
of time-tag records, convergence from finite marker bases, and a calibrated
local-oscillator field over the admitted bandwidth. Finite visibility and
conditional-count identities do not establish that completion.

Run `python research/aspect/checkers/polarization_marker_quantum_eraser.py`.
The result is
`research/aspect/results/polarization_marker_quantum_eraser.json`.
