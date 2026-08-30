# Flux energy stabilizes the metric but leaves an orientation doublet: WP784

## Question

Does minimizing the physical flux energy select one WP783 pairing-three orbit
and simultaneously stabilize its tensor metric?

## Exact pairing-three family

For \(b=(1,1)\) in \(I_{1,1}\), write

\[
f=(y+3,y).
\]

Then \(b\cdot f=3\). In lightcone coordinates,

\[
u=f_1+f_2=2y+3,
\qquad
v=f_1-f_2=3.
\]

The compatible one-parameter positive metric gives the quadratic energy

\[
V_t(f)=\frac12\left(e^tu^2+e^{-t}v^2\right).
\]

## Discrete minimization leaves two states

Primitivity excludes \(y\) divisible by three. The smallest allowed value of
\(u^2\) is one, attained twice:

\[
f_+=(2,-1),
\qquad
f_-=(1,-2).
\]

Their lattice norms are

\[
f_+^2=3,
\qquad
f_-^2=-3.
\]

Because the energy depends on \(u^2\), the two remain exactly degenerate for
every compatible metric. Quadratic backreaction cannot select their
orientation.

## Metric backreaction is genuinely progressive

On either minimizing branch,

\[
V_t=\frac12\left(e^t+9e^{-t}\right).
\]

Its unique stationary point is

\[
t=\log 3,
\]

with

\[
V_{\min}=3,
\qquad
\frac{d^2V}{dt^2}=3.
\]

Thus the same source operation that narrows the flux orbit also stabilizes the
dimensionless tensor-metric ratio. This is a genuine rigidifier, not a fitted
coordinate convention.

## Remaining kernels

An independent overall energy scale still multiplies \(V\). Moreover, the
potential has no dependence on the separate Green--Schwarz coefficients
\(k,c\). Its derivative along Aspect's exact product-preserving tangent

\[
(\delta k,\delta c)=(k,-c)
\]

vanishes. Hence it cannot fix the Stückelberg threshold.

## Classification

Flux energy is both a partial orbit selector and a metric rigidifier. It
reduces the infinite pairing-three fiber to a two-state orientation doublet
and fixes \(t=\log3\), but it does not select a sign, derive pairing three,
fix the overall scale, or provide a physical instrument.

The next source must be an orientation-odd operation with an explicitly
declared relational reference. It must split \(f_+\) from \(f_-\), be
transverse to the Green--Schwarz product kernel, and derive its sign rather
than fitting it.

Reproduce with:

    uv run --with sympy python research/flavor/checkers/wp784_flux_energy_metric_rigidifier_orientation_doublet.py

Generated result:
research/flavor/results/wp784_flux_energy_metric_rigidifier_orientation_doublet.json
