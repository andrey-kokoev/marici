# There need not be a unique smallest explanatory enlargement

## The phrase “the smallest enlarged state object” is too strong

Take four histories labelled by two hidden bits: `00`, `01`, `10`, and `11`.
The reduced record is constant. Two physically admissible auxiliary ports exist:

- port `A` reports the first bit;
- port `B` reports the second bit.

For the target pair `00` versus `11`, either port restores perfect
distinguishability. Each is minimal relative to the admitted port family. But
neither is sufficient for everything the other can answer:

- `A` distinguishes `00` from `10` but not `00` from `01`;
- `B` distinguishes `00` from `01` but not `00` from `10`.

Thus `A` and `B` are incomparable minimal sufficient enlargements. The combined
port `AB` is sufficient but not minimal. There is no unique least explanatory
extension in the admitted physical port poset.

## Replace smallest object with a sufficiency frontier

The right question is not:

> What is the smallest enlarged object on which the histories differ?

It is:

> What are the minimal admissible extensions sufficient for the declared
> downstream counterfactual family?

Changing the future question changes the frontier. Choosing among incomparable
minimal extensions requires another criterion: cost, locality, causal
availability, robustness, explanatory integration, or compatibility with other
questions.

This also blocks a subtle explanatory shortcut. Recovering one distinction does
not establish that the chosen extension contains the mechanism. Different ports
may correlate with the same target pair while predicting different interventions
on neighboring histories. Those neighboring counterfactuals discriminate rival
explanations.

## Optical reading

One environment port may carry path information while another carries
polarization phase. For a selected pair of preparations, either may distinguish
the outputs. Spanning neighboring probe pairs reveals that the ports are not
interchangeable. The explanatory object should therefore be selected against a
declared probe module, not a single successful recovery demonstration.

## Deeper correction to constructor realism

Operational equivalence must be indexed at least four ways:

- record equivalence under the data already stored;
- resource equivalence under an agent’s accessible constructors;
- nomological equivalence under all transformations allowed by the theory;
- ontic identity in the theory’s state space.

The optical experiments directly test the first two. Moving from them to the
last two requires an independently stated dynamical theory. Constructor analysis
disciplines that move but does not derive the theory from records alone.

## Claim boundary

The checker uses a finite admitted port poset and deterministic bit-valued
records. It proves nonuniqueness in this model, not in every physical theory.

## Verification

```text
python research/aspect/checkers/check_no_unique_smallest_explanatory_enlargement.py
```
