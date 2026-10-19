# The accepted finite witness cannot be promoted unchanged to an all-tolerance compiler

## Question

The latest conjecture extends one certified encoder witness to a total WG compiler
for every positive rational accuracy. Test the direct implementation candidate:
retain the existing 312-gate word and acceptance machinery, and expose tolerance
as a request parameter. This candidate has two independent obstructions.

The test does not refute the existence of a different compiler which genuinely
changes the word and refines evaluation precision. No such universal implementation
was supplied to this test.

## Exact lower bound on the existing word

The acceptance checker previously computed only an upper bound. It now also
computes a downward dyadic enclosure L of the exact weighted Hilbert-Schmidt
norm of the rounded-word output minus the certified polynomial target on the
five-dimensional bright domain.

For that map D,

    ||D||op >= ||D||HS/sqrt(5) >= (4/9) L.

The factor is valid because sqrt(5)<9/4. Subtract the charged word-evaluation
rounding bound r and polar-target evaluation bound eta. Reverse triangle
inequality gives a lower bound for the EXACT unitary word A versus the IDEAL
polar ready embedding J:

    ||A-J||op >= max(0,(4/9)L-r-eta).

All quantities are rational; the square-root enclosure is checked by exact
squaring. This is not the optimizer's numerical score and not merely failure
of an upper-bound acceptance test.

The resulting certified interval, with endpoints displayed in decimal, is

    0.03796922410420683 <= ||A-J||op <= 0.08543395404933576.

Thus the word remains accepted at encoding tolerance 1/10 but is mathematically
refuted at 1e-8 (indeed at any smaller tolerance than the lower bound). Increasing
arithmetic precision cannot make this SAME exact word meet those requests.
A new control word is required.

## Fixed evaluator budget blocks completeness of the current checker

The current evaluator receipt was generated for 1e-6 and contributes the exact
positive upper budget eta, approximately 9.84558e-7. The verifier accepts only
when

    measured_upper + rounding_upper + eta < requested_epsilon.

Therefore for requested epsilon<=eta it cannot accept ANY candidate word while
that evaluator receipt remains fixed, even if the candidate were much better.
This is an incompleteness of that frozen acceptance configuration, not a physical
or mathematical lower bound on attainable encoding error.

At epsilon=1e-8 both defects are present: the current word itself is too inaccurate,
and the frozen target-evaluation budget already exceeds the request. They must
not be conflated. A terminating all-tolerance implementation must change both
candidate words and certificate precision as needed.

## Executed tests and three-way disposition

The checker now takes --epsilon and --output. Its scientific result distinguishes:

- accepted: certified upper bound below tolerance;
- refuted: certified lower bound above tolerance;
- unresolved_by_bounds: neither inequality holds.

A checker exit of zero means the calculation completed consistently, not that
its candidate was accepted. The original accepted result is preserved by rerunning
it at the original tolerance; the negative request has its own output file.

    python research/strominger/checkers/check_encoder_control_word_acceptance.py
    python research/strominger/checkers/check_encoder_control_word_acceptance.py --epsilon 1/100000000 --output encoder-control-word-refutation-1e-8.json

Both fresh executions exit 0. The first says accepted; the second says refuted
and `evaluation_budget_alone_exhausts_tolerance: true`. Both independently replay
the source controls and certified evaluator polynomial before computing bounds.

## Disposition

Falsified: merely wrapping the existing finite word and frozen verifier as a
request/answer WG yields a total all-tolerance compiler. Retaining and certifying
that package adds no missing accuracy refinement.

Not falsified: the broader existential compiler conjecture with genuine word
search, precision dovetailing and source-preserving WG composition. The earlier
reachability/density arguments remain intact. This packet supplies no complexity
lower bound or proof that every 312-gate word fails; its word-level lower bound
is for the exact accepted candidate only.

Artifacts:
- `results/encoder-control-word-acceptance.json`
- `results/encoder-control-word-refutation-1e-8.json`
- `checkers/check_encoder_control_word_acceptance.py`

No new formal WG term, all-tolerance run, formal-kernel check, graph publication,
commit or push.
