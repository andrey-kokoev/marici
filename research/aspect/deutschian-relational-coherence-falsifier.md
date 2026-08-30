# Deutschian relational-coherence falsifier

## Question

Can the `2(3+2+1)+1` architecture make an explanatory optical prediction whose
counterfactual structure can be experimentally falsified?

## Explanation

The joint phase is recoverable because the source creates an odd relational
coordinate and coherent sewing is a possible transformation that couples that
coordinate to a detector port. Neither local wing contains that coordinate as
a marginal observable. Measurement followed by classical comparison cannot
replace the sewing transformation because it has destroyed the phase relation
before the comparison is made.

This answers: why can interference exist in the completed pair when it exists
in neither completed part?

Because interference is carried by a transformable relation, not by an
unobserved local fringe.

## Prediction

Let `gamma` be source coherence, `kappa_A` and `kappa_B` the independently
calibrated coherence survival factors in the two wings, and `s` the coherent
fraction of the sewing analyzer. When the two intervention channels are
independently certified to factorize, the predicted joint visibility is

\[
V_{\rm joint}=\gamma\kappa_A\kappa_B s.
\]

Both local marginal visibilities remain zero throughout the scan.

For the frozen test value `gamma = 3/5`:

- complete coherent sewing gives visibility `3/5`;
- dephasing either wing gives zero;
- measuring and forgetting a local record gives zero;
- coherently retaining and uncomputing that record restores `3/5`;
- classical comparison gives zero unconditional visibility;
- a vacuum-port sewing dilation with incidence amplitudes `3/5` in both
  directions gives round-trip factor `9/25` and visibility `27/125`.

The last line is important: this is a quantitative composition prediction,
not only a binary coherence witness. The attenuation is not an abstract dial.
It is admitted only when a complete unitary vacuum-port dilation produces the
two incidence amplitudes and retains the complementary port outcomes.

## Apparatus sequence

Randomize every heralded pair among six interventions while using the same
source and calibration epoch. Scan the joint phase at four quarter turns.
Retain all single, double, and no-click events.

In the measurement intervention, irreversibly measure one marker before the
joint analyzer. Run a separate coherent-record intervention in which the same
marker information is copied reversibly, retained, and uncomputed before
sewing. Their local recorded distributions agree; their allowed future
transformations do not.

## Direct falsifiers

The architecture fails if any preregistered condition occurs:

1. either local marginal develops the joint phase fringe;
2. verified nonzero source coherence plus complete sewing produces no joint
   fringe;
3. an entanglement-breaking local measurement preserves the unconditional
   joint fringe;
4. post hoc classical record comparison reproduces the unconditional coherent
   sewing fringe;
5. independently inserted coherence attenuators violate the multiplicative
   visibility law after their independence has been certified.

Correlated phase channels are outside that product law. They are tested by the
companion correlated-noise discriminator rather than counted as failures.

The strongest test is the matched pair: irreversible record formation versus
coherent record retention and uncomputation. Equal observed local records but
different recoverability directly test whether explanatory content resides in
possible transformations rather than in a static catalogue of outcomes.

## Disposition

This is a Deutschian explanation with a finite optical falsifier. It explains
the joint fringe by specifying what transformations of the relational phase
are possible and impossible, then predicts the response to interventions that
preserve local statistics while changing those possibilities.

## Scientific placement

The probability law agrees with ordinary quantum mechanics. The new result is
the organized constructor-level prediction and its combined falsification
protocol, not a competing numerical correction to quantum theory.

## Verification

Run:

```text
python research/aspect/checkers/check_deutschian_relational_coherence_falsifier.py
```
