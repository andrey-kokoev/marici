# Formal binary-effect refinement of the `D(S3)` scalar probes

Owner: `marici.Kitaev`

## Bounded question

Does the three-probe minimum survive when each bounded scalar coordinate is
given the formal Bernoulli completion `p(+|m)=(1+m)/2`?

Yes on the frozen atomic surface

\[
\{\Re\theta,\Im\theta,S_A,\ldots,S_H\}.
\]

All `S` entries are real.  Exhaustive search again gives minimum cardinality
three and exactly four minimum families:

\[
(\Im\theta,S_C,S_D),\ (\Im\theta,S_C,S_E),
(\Im\theta,S_D,S_F),\ (\Im\theta,S_E,S_F).
\]

Thus the real twist quadrature is unnecessary.  The selected family is
`(Im theta,S_D,S_F)`.

## Formal binary effects

For each bounded real coordinate `m`, define the formal binary effect by

\[
p(+|m)={1+m\over2},\qquad p(-|m)={1-m\over2}.
\]

For the selected settings, the exact expectation signatures are

| sector | `Im theta` | `S_D` | `S_F` |
|---|---:|---:|---:|
| A | 0 | 1/2 | 1/3 |
| B | 0 | -1/2 | 1/3 |
| C | 0 | 0 | -1/3 |
| D | 0 | 1/2 | 0 |
| E | 0 | -1/2 | 0 |
| F | 0 | 0 | 2/3 |
| G | `sqrt(3)/2` | 0 | -1/3 |
| H | `-sqrt(3)/2` | 0 | -1/3 |

All eight induced triples of binary plus-probabilities are distinct.  The
minimum expectation separation remains `1/3`, so the minimum probability
separation is `1/6` and empirical plus-frequency error strictly below
`1/12` preserves unique nearest-signature classification.

## Conditional sampling bound

If repetitions are independent, stationary, exactly calibrated Bernoulli
trials, Hoeffding's inequality and a union bound over three settings give

\[
\Pr\left[\max_j|\widehat p_j-p_j|\ge 1/12\right]
\le 6e^{-n/72}.
\]

Therefore

\[
n\ge\left\lceil72\log(6/\alpha)\right\rceil
\]

shots per setting suffice for failure probability at most `alpha`.  This is
a conditional statistical guarantee, not a source-derived noise law.

## Instrument typing correction

The first version of this packet incorrectly described the raw `S_D,S_F`
Bernoulli effects as source-derived Hadamard tests.  A Hadamard test returns a
unitary matrix element or normalized trace.  Charge--flux monodromy gives
`tr M = 6 S_ab`, while normalized trace estimation divides by the internal
dimension; it does not generally return raw `S_ab`.

Therefore `p(+|S_b)=(1+S_b)/2` is a **formal binary-effect completion**.  A
source-derived realization requires an additional block encoding,
interferometric normalization, or other apparatus dilation proved to have
these effects.  None has yet been derived.  The twist imaginary quadrature
can arise from a controlled twist unitary, but that does not realize the two
raw `S` settings.

Carrier geometry supplies the framed or linked process.  The coefficient
lens supplies the scalar table.  The missing datum is the apparatus map from
those scalars to the declared binary effects.

## Verification

`uv run --with sympy python -u research/kitaev/checkers/check_s3_binary_hadamard_probe_surface.py`
passes eight aggregate gates.  It exhausts all subsets of the ten atomic
settings, verifies the four minima, constructs exact binary probabilities,
and checks the expectation, probability, and empirical-frequency margins.
Fresh stdout matches the saved JSON after newline normalization.

## Claim boundary and falsifiers

No source-derived realization of the raw `S` Bernoulli effects, local
controlled-ribbon synthesis, correlated fault model, state-preparation cost,
or calibration uncertainty is supplied.  The Hoeffding
bound fails outside its explicit i.i.d. stationary Bernoulli assumptions.
The theorem is falsified by a faithful one- or two-setting subset, duplicate
selected probability signatures, a probability gap other than `1/6`, or a
valid i.i.d. derivation exceeding the stated union-bound failure probability.
