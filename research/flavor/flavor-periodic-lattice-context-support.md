# Periodic-lattice context support

## Question

Can WP539's six abstract Euclidean contexts be realized as distinct supported
momenta on a concrete periodic lattice without fitting their values to the
flavor poles or target ratio?

## Frozen support witness

Use WP524's nearest-neighbor lattice momentum in one periodic direction,

\[
\widehat q_n^2={4\over a^2}\sin^2{\pi n\over N}.
\]

Freeze \(N=24\), \(a=1\,\mathrm{GeV}^{-1}\), and the six even modes

\[
n\in\{0,2,4,6,8,10\}.
\]

The lattice spacing is a predeclared support witness. A physical calculation
must replace it with ordinary QCD scale setting that is independent of the
flavor target.

The exact supported momentum squares are

\[
0,\quad 2-\sqrt3,\quad 1,\quad 2,\quad 3,\quad 2+\sqrt3
\]

in \(\mathrm{GeV}^2\). They are distinct and nonnegative, and none intersects
the timelike pole set.

## Rank certificate

Applying the WP538 companion resolvent at these six nodes gives an exact
context determinant proportional to \(\sqrt3\), with a nonzero rational
coefficient. Therefore the context rank is six. Every five-context deletion
has rank five.

Tensoring with WP525's four Ward channels gives complex rank 24 and the same
48-real estimator dimension required by WP535.

## Periodic alias falsifier

Distinct Fourier labels need not give distinct \(\widehat q^2\). Replace mode
10 with mode 16. Modes 8 and 16 then both have

\[
\widehat q^2=3\,\mathrm{GeV}^2,
\]

and the context rank falls exactly to five. Momentum support must therefore be
checked after the lattice dispersion relation, not inferred from distinct
integer labels.

## Authority boundary

WP540 supplies a concrete kinematic grammar and an exact alias-control test.
It is not a continuum-extrapolated physical measurement. Instrument authority
still requires:

- a preregistered QCD scale-setting observable;
- multiple lattice spacings and volumes;
- supported four-dimensional momentum tuples;
- the four renormalized Ward-channel bilocal correlators;
- coincident-point subtraction and threshold matching;
- continuum, finite-volume, and heavy-quark systematics;
- the full common 48-real covariance.

No source coefficient or value of \(t\) is inferred from the momentum design.

## Reproduction

Run:

    uv run --offline --with sympy python research/flavor/checkers/wp540_periodic_lattice_context_support.py

The generated result is
research/flavor/results/wp540_periodic_lattice_context_support.json.

The reviewed claim and report to marici.Nima were admitted at graph event
ev-000000004872-e2c1b937-c795-4b0b-ab90-060bbccbc3db. Admission records
reviewed provenance and does not certify truth.
