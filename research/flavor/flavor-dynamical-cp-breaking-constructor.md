# A coherent dynamical CP-breaking flavor constructor (WP87)

Agent: `marici.Figueiredo`. Date: 2026-08-24.

## Authority and source

Following explicit operator authorization after WP86, introduce the bounded
extended source `FDM-1`. It promotes one CP-odd flavor orientation coordinate
`s` to a dynamical modulus. This is a proposed theory package, not a claim that
the declared Standard Model already contains the field.

The source action in dimensionless field/time units is

\[
V(s)=\frac14(s^2-1)^2,\qquad
\dot s=-V'(s)=s(1-s^2).
\]

The coefficients and normalization are part of `FDM-1` before the ensemble
test. The action is CP symmetric under `s -> -s`; it does not insert the
observed sign of the Jarlskog invariant.

## Quotient map and proper attribute

Let `q` denote the remaining flavor moduli, including a positive CP scale
`j(q)>0`. Declare the covariant physical map

\[
f(s,q)=(q,J=s\,j(q)).
\]

CP conjugation sends `(s,J)->(-s,-J)`. The vacuum attribute

\[
\mathcal A=\{s=-1,+1\}
\]

maps to the proper CP-broken physical attribute `J != 0`. It excludes the
CP-conserving locus without choosing either sign. The admitted preparation
domain is `s != 0`; `s=0` is the exact unstable separatrix and is an explicit
falsifier/domain boundary.

## Task and exact repeatability

The task is dissipative annealing

\[
T_\tau:(s,q;b_0)\mapsto(s(\tau),q;b_\tau),
\]

implemented by a cooled flavon bath whose force is `-V'(s)`. For
`y=s^2`,

\[
y(t)=\frac1{1+(y_0^{-1}-1)e^{-2t}}.
\]

Every admitted input converges to `A`; points in `A` are exact fixed points.
For the certified working domain `1/4 <= y0 <= 4` and `e^-2t <= 1/4`,

\[
|y(t)-1|\le \frac{3e^{-2t}}{1-3e^{-2t}/4}.
\]

The ideal bath is catalytic. A finite bath has declared per-cycle degradation
`delta_b`; after `N` cycles it is bounded by `N delta_b`, and a reset pump
restores its reference state. These are task-specific certificates, not
borrowed measurement evidence.

## Instrument

The instrument is a zero-temperature overdamped annealing stage coupled to the
CP-odd modulus, with four typed ports: modulus input, cooled dissipative bath,
elapsed-time control, and bath reset. Its readout is the signed CP-odd invariant
already available in the physical16 probe algebra. Readout verifies the task;
it does not generate the force.

## Predeclared ensemble prediction

Before loading WP20, `FDM-1` predicts only

\[
J\ne0,
\]

not its sign or magnitude. The checker evaluates this on every stored viable
sheet. All 1,210 have nonzero `J`; both signs remain allowed by the source.
This is a weak but genuine selector prediction that does not fit a scalar
normalization to the ensemble.

## Scope and falsifiers

This package is internally coherent at the proposed-model level. It is
falsified by an admitted CP-conserving flavor point, loss of covariance of
`f`, a source coefficient chosen after the ensemble test, nonconvergence for
`s != 0`, failure of the degradation bound, or absence of a realizable flavon
bath in any UV completion. Empirical existence of `FDM-1` remains open.

Verification: `uv run --with sympy python
research/flavor/checkers/wp87_dynamical_cp_breaking_constructor.py`.
