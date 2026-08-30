# Common-Gain Identifiability Requires an Absolute-Rate Port

## Question

Can the smallest WP880 hostile, the common rescaling (G=gH), be removed by
the presently authorized flavor observations?

## Exact observation model

Let channel amplitudes factor as

\[
A_i(g)=g a_i,
\]

with nonnegative channel weights (q_i=|a_i|^2). The ideal signal yields are

\[
s_i(g)=\mathcal L\,\epsilon_i g^2q_i,
\]

where \(\mathcal L\) is integrated luminosity and \(\epsilon_i\) is the
channel efficiency. Every normalized flavor fraction is

\[
p_i(g)=\frac{s_i(g)}{\sum_j s_j(g)}
      =\frac{\epsilon_iq_i}{\sum_j\epsilon_jq_j}.
\]

Hence \(\partial p_i/\partial g=0\): branching fractions, normalized angular
shapes, and the current texture or `physical16` coordinates cannot identify
the common gain.

An absolute count channel has expectation

\[
\mu_i(g)=b_i+\mathcal L\,\epsilon_i g^2q_i.
\]

Its gain derivative is

\[
\frac{\partial\mu_i}{\partial g}
=2\mathcal L\,\epsilon_i gq_i.
\]

It separates positive gains when \(\mathcal L\), \(\epsilon_i\), \(b_i\),
and \(q_i\) are independently fixed and some accepted channel has \(q_i>0\).
The sign of \(g\) remains invisible to a pure rate and requires an admitted
interference reference.

## Nuisance symmetry

Without independent luminosity or source-current normalization, the
transformation

\[
(g,\mathcal L)\longmapsto(cg,\mathcal L/c^2)
\]

leaves every absolute expectation invariant. Thus merely writing a count row
does not remove the common-gain kernel. The calibrated normalization is part
of the instrument, not a presentation convention.

With one count and unknown luminosity, the Jacobian with respect to
\((\log g,\log\mathcal L)\) is proportional to \((2,1)\) and has rank one.
Adding an independently calibrated luminosity monitor gives the two rows
\((2,1)\) and \((0,1)\), whose determinant is (2). This is the smallest
formal rank repair. It is physical only when the monitor has an acquisition
contract and its calibration does not use the portal signal being tested.

## Aspect classification

- Realization: the rate law is a conditional collider-style realization, not
  yet a selected Spin(5) production and decay process.
- Exact tester: normalized observations are proven gain-blind.
- Falsifier: (g=1) and (g=2) remain identical in normalized records and
  differ by four in calibrated signal yield.
- Ontology: nonlinear widths, interference, acceptance dependence, and
  detector adaptation remain fresh hostile terms.
- Governance: the absolute-rate row is deferred pending completion-specific
  production, decay, background, and calibration constructors.
- Experiment portfolio: no acquisition-authoritative flavor rate cell is
  presently available.

The result removes a false escape from WP880. Common gain is not recoverable
from more precise normalized flavor data. It requires a new source-calibrated
absolute-rate experiment. Such an experiment would select a magnitude on the
physical quotient, while a separate relational interference port would be
needed to read its sign.

## Smallest exact falsifiers

1. Gain blindness: (g=1) and (g=2) give the same normalized fractions.
2. Calibration laundering: ((g,\mathcal L)=(1,4)) and ((2,1)) give the
   same uncalibrated absolute signal.
3. Sign blindness: (g) and (-g) give the same pure rate.

## Claim boundary

This is an identifiability theorem for the declared factorized counting
model. It does not assert that a suitable Spin(5) process, luminosity monitor,
background model, detector efficiency, or interference reference has been
constructed. Those are precisely the remaining physical-instrument gates.

## Verification

Run:

~~~text
uv run --with sympy python research/flavor/checkers/wp881_common_gain_absolute_rate_gate.py
~~~
