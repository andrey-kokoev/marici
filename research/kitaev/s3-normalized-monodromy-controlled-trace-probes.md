# Normalized-monodromy controlled-trace probes for `D(S3)`

Owner: `marici.Kitaev`

## Bounded question

Can the formal raw-`S` binary effects be replaced by quantities that an
abstract controlled-unitary trace test actually returns?

Yes, conditional on controlled monodromy and a maximally mixed state on the
sector's internal tensor-product space.  The measured expectation is

\[
\mu_{ab}={\operatorname{tr}M_{ab}\over d_a d_b}
={6S_{ab}\over d_a d_b},
\]

which always lies in `[-1,1]`.  This corrects the normalization defect of the
raw-`S` formal completion.

## Minimum setting theorem

On the atomic surface

\[
\{\Re\theta,\Im\theta,\mu_A,\ldots,\mu_H\},
\]

exhaustive enumeration again gives minimum cardinality three and four
minimum families:

\[
(\Im\theta,\mu_C,\mu_D),\quad
(\Im\theta,\mu_C,\mu_E),
\]

\[
(\Im\theta,\mu_D,\mu_F),\quad
(\Im\theta,\mu_E,\mu_F).
\]

Select `(Im theta,mu_D,mu_F)`.  Its expectation signatures are

| sector | `Im theta` | `mu_D` | `mu_F` |
|---|---:|---:|---:|
| A | 0 | 1 | 1 |
| B | 0 | -1 | 1 |
| C | 0 | 0 | -1/2 |
| D | 0 | 1/3 | 0 |
| E | 0 | -1/3 | 0 |
| F | 0 | 0 | 1 |
| G | `sqrt(3)/2` | 0 | -1/2 |
| H | `-sqrt(3)/2` | 0 | -1/2 |

All eight differ.  No one- or two-setting family on the frozen surface is
faithful.

## Binary instrument and margins

A controlled-unitary trace test with ancilla `X` or `Y` measurement gives

\[
p(+|\mu)={1+\mu\over2}.
\]

The selected expectation codebook has minimum distance `1/2`, attained by
`C/D` and `C/E`.  Hence the binary probability gap is `1/4`, and empirical
frequency error strictly below `1/8` preserves unique nearest-signature
classification.

Under independent stationary calibrated Bernoulli repetitions, Hoeffding
plus a union bound gives

\[
\Pr[\max_j|\widehat p_j-p_j|\ge1/8]\le6e^{-n/32},
\]

so `ceil(32 ln(6/alpha))` shots per setting suffice for failure probability
at most `alpha`.

## Apparatus typing

The abstract dilation requires: coherent control of the twist or monodromy
unitary, a maximally mixed state on the relevant internal space, an ancilla
phase selecting real or imaginary trace, and binary ancilla measurement.
Unlike the raw-`S` completion, its normalization follows directly from the
trace circuit.

The quantum-double source supplies the ideal monodromy representation and
sector dimensions.  It does not yet supply a local fault-tolerant controlled-
ribbon circuit or a sector-uniform preparation protocol for the required
maximally mixed internal state.  The result is therefore an abstract typed
dilation conditional on those capabilities, not a hardware theorem.

Carrier geometry supplies the framed/linked process and reference sector.
The coefficient lens supplies internal dimensions, controlled action, mixed
state, trace normalization, and ancilla effects.

## Verification and falsifiers

`uv run --with sympy python -u research/kitaev/checkers/check_s3_normalized_monodromy_probe_surface.py`
passes seven aggregate gates, exhausts the ten-setting surface, and checks all
margins exactly.  Fresh stdout matches the saved JSON.

The packet fails if any normalized expectation leaves `[-1,1]`, a faithful
one- or two-setting family exists, selected signatures collide, the minimum
expectation gap differs from `1/2`, or the trace-test normalization differs
from `6S_ab/(d_a d_b)`.  Its sampling claim fails outside the stated i.i.d.
assumptions.
