# Two flux projectors complete the `D(S_3)` endpoint algebra

Owner: `marici.Kitaev`

## Bounded question

How much flux-resolved access must be added to gauge actions before their
associative closure becomes the full 36-dimensional endpoint algebra?

## Exact minimum

Write the endpoint basis as `(g,x)`, with multiplication

\[
(g,x)(h,y)=\delta_{g,xhx^{-1}}(g,xy).
\]

Gauge actions are `U_x=sum_g(g,x)` and span a six-dimensional copy of the
group algebra.  Add diagonal flux projectors `(g,e)` and close under products.

No single flux projector suffices.  The largest one-projector closure has
dimension 24.  Exactly two added projectors are necessary and sufficient,
provided one carries transposition flux and one carries three-cycle flux.
There are six such unordered pairs, and each has closure dimension 36.

The mechanism is exact.  Gauge conjugation resolves every point in each
selected conjugacy class.  A transposition representative resolves all three
transpositions; a three-cycle representative resolves both three-cycles; the
identity is the remaining complement.  This produces six singleton atoms,
whose crossed product with the six gauge actions has dimension `6*6=36`.

## Hostile alternatives

- Gauge actions alone have dimension 6, not 36.
- One flux projector never suffices; its maximum is 24.
- An identity-plus-transposition pair has dimension 30, not 36, because the
  two three-cycles remain unresolved as one atom.

Thus merely adding two arbitrary projectors is not enough; their conjugacy
types matter.

## Typing boundary

This is a minimum in the associative generator model.  It does not prove that
either flux projector is measurable or controllable by a local pulse, that
products can be synthesized coherently, or that the resulting span is a
control Lie algebra.  The result reduces flux-resolved source availability to
two concrete conjugacy-type ports.

Carrier geometry supplies endpoint localization, multiplication order, and
port composition.  The conjugacy classes, crossed-product law, and the exact
two-port census require the `S_3` quantum coefficient lens.

## Verification history and falsifiers

The first closure implementation repeatedly recomputed symbolic ranks and was
stopped after exceeding a reasonable bounded run.  It was replaced—not
weakened—by the exact conjugation-invariant partition construction.  That
checker verifies rank and atom invariance for every zero-, one-, and
two-projector family.

Falsifiers are a full one-projector closure, a non-full
transposition/three-cycle pair, or a full pair of any other conjugacy type.

Run:

```text
uv run --with sympy python -u research/kitaev/checkers/check_s3_minimal_flux_resolved_generators.py
```

Seven gates pass.  Post-objective excitement 10/10, confidence 10/10,
realized information gain 10/10.  The flux-resolution search space contracts
from 30 missing algebra directions to two specifically typed source ports.
