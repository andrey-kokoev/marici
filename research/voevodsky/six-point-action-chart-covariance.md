# Complete single-field tree six-point chart covariance

Fresh resume selected `six-point-action-chart-readout:v1`.

## Result

For Nima's supplied parity-even, two-derivative scalar model, the complete tree
six-point Feynman amplitude is identical in the angle, ratio and sine charts:

    amplitude = -i [ g6_can + lambda_can^2 sum_I 1/(P_I^2-m2) ].

I ranges over the TEN unordered 3|3 partitions of six labeled external legs.
All momenta are incoming, signature is +---, and the expression is evaluated
away from exchange poles. Here m2 denotes mass squared, not mass.

For the logarithmic model,

    m2=2U/F^2, lambda_can=16U/F^4, g6_can=512U/F^6.

For the same canonically quartic-truncated model transported into every chart,
m2 and lambda_can are unchanged but g6_can=0. All exchange terms therefore cancel
in their difference:

    amplitude_log - amplitude_quartic = -i 512U/F^6.

The sixth-order refinement is thus visible in the COMPLETE amplitude, not merely
in a coordinate-dependent potential derivative. This is conditional on the
supplied scalar action and conventional tree prescription, not a derivation of
physical scales or spacetime from the source carrier.

## Calculation

Write the chart action through the required order as

    L = 1/2(dv)^2 + a v^2(dv)^2 + b v^4(dv)^2
        - m2 v^2/2 - l v^4/24 - g v^6/720.

The differentiated-leg assignment counts give 4 per unordered pair for the
quartic derivative vertex and 48 per pair for the sextic derivative vertex.
The checker enumerates all 4! and 6! assignments to obtain these factors.

For a four-point vertex with three on-shell external legs and one internal leg,
put D=P^2-m2. Its coefficient, after removing -i, is

    l-2a(3m2+P^2) = lambda_can-2aD,
    lambda_can=l-8a m2.

The six-point contact coefficient is g-144b m2. Each exchange channel contributes

    (lambda_can-2aD)^2/D
      = lambda_can^2/D - 4a lambda_can + 4a^2 D.

The checker constructs all ten partitions, verifies complementary triples have
the same P^2 using the six momentum-conservation dot-product equations, and
obtains

    sum_I D_I = 8m2.

Consequently contact plus the non-pole part of all exchanges is

    g-144b m2 -40a lambda_can +32a^2 m2
      = g-40a l+352a^2 m2-144b m2
      = g6_can.

This is the canonical sixth derivative found in the preceding chart test, now
recovered from the actual contact-plus-exchange diagram calculation.

Parity forbids odd vertices. At tree level six external legs allow only one
six-point vertex or two four-point vertices; higher vertices cannot contribute.
The quadratic terms are already included in the free propagator. Thus these are
all trees for this single-field action, not a selected subset of diagrams.

## Controls and evidence

`check_six_point_action_charts.py` checks the symbolic kinematic identities,
vertex multiplicities, ten-channel sum and all three general-positive-F,U chart
coefficients. Potential-only substitutions fail; using just the canonical sixth
derivative also fails to include the exchange part.

An additional exact REAL 3->3 on-shell example, embedded in 3+1 dimensions from
1+1, conserves energy and momentum and has no zero exchange denominator. It
checks the complete cancellation at actual logarithmic scales F=1,U=1/2.
The general symbolic identity does not rely on that example or on assuming that
arbitrary unconstrained dot products are realizable spacetime momenta.

Verification:

    uv run --with sympy python research/voevodsky/check_action_chart_comparison.py
    uv run --with sympy python research/voevodsky/check_six_point_action_charts.py

The preceding 55 checks and the new 45 checks pass. Current upstream formal and
owner dependency hashes are checked. This turn adds an exact symbolic tree
calculation, NOT a new Agda six-point theorem or a fresh Agda compilation.
Receipt: `six-point-action-charts.json`.

## Boundary and next question

The conditional SINGLE-FIELD comparison now succeeds at a complete observable
amplitude level. It does not establish a quantum equivalence of the full source
target: Nima's full unit-probe target has two additional massless directions.
No loop, quantum-decoupling, global-overlap or analytic-completion theorem follows.

The next physical refinement should test those omitted modes directly: derive a
mixed scalar/massless-mode tree channel from the full counting-metric target and
ask whether the scalar-only profile loses an allowed physical process. Classical
consistency of setting the other fields to zero is not a claim that all mixed
scattering channels vanish. General constructor propagation remains deferred.
