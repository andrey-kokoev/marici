# Two-factor weighted chain transport

## Source class metric

The full two-factor incidence complex has1152 rectangle2-cells. Each primitive
sphere generator pulls back to a signed vector supported on504 of them. After
normalizing its period, every nonzero coefficient is +/-1/84.

The84 comes directly from the other factor's local labels. A projected rectangle
has two labelled source positions and two labelled target positions; all four
cross-edges must exist, while repetition within either side is allowed. There
are36 assignments with equal sources and48 with distinct sources, totalling84.
There are six primitive rectangles, giving support6*84=504.

The normalized vectors Z1,Z2 are closed, orthogonal to every3-boundary, and
mutually orthogonal. Consequently they minimize cell cost in their classes:

    Z^T Z = (1/14)*I2.

This is induced by unit source rectangle costs. The analogous fresh unit-triangle
class metric is(1/16)*I2.

## Explicit product-anchor chain map

Use a target-to-source anchor in each primitive coordinate, a(t)=t+1 mod4.
The product anchor defines the same edge/rectangle-to-triangle formula as in the
primitive calculation. Both chain-map squares hold on every cell.

The two source harmonic representatives map to closed target chains Y1,Y2.
Their periods form -I2 under the chosen orientations, so both independent
classes are retained. These target chains need not be the minimum representatives
for the target's freshly assigned unit costs.

## Exact quotient and retained residual budget

For the prescribed target chain Yi, find its minimum-norm unconstrained source
lift Li. Retain Ri=Zi-Li. The normal equations certify Li belongs to image(T2^T),
T2*Li=Yi, and T2*Ri=0. Thus Li and Rj are orthogonal for either class index.

The exact Gram matrices are

    source:      (1/14)*I2,
    quotient:    (2029/35280)*I2,
    residual:    (491/35280)*I2.

The latter two sum to the source metric. Unconstrained lifts have nonzero source
boundary. Restoring the residuals closes them. Every tested linear combination
of the two classes reconstructs with its exact source cost.

Since Zi is already minimum among all closed representatives of its class, it
is also minimum among closed source lifts of its particular target chain Yi.
This verifies closed-class metric transport, including both factor directions.
The computation checks these two harmonic columns and their combinations;
it does not claim a lossless implementation for every source cell vector.

## Metric conversion depends on comparison multiplicity

The closed-class conversion from fresh unit-triangle cost to source rectangle
cost is8/7 in the two-factor example. The primitive conversion was3/2. Applying
the primitive ratio unchanged at the next level would assign the wrong budget.

The product-count pattern gives

    rectangle scale at n factors: 6/84^(n-1),
    triangle scale at n factors:  4/64^(n-1),
    ratio: (3/2)*(16/21)^(n-1).

For rectangles, pulling back a primitive cycle adds84 admissible labelled
assignments per extra factor. Closure follows from the two opposite primitive
face contributions at each edge having equal lift multiplicity; orthogonality
to3-boundaries follows from pullback of the primitive cocycle. Projection periods
normalize by84^(n-1). These are the same counting/closure arguments used for the
triangle formula, with different local presentation multiplicities.

At rank4 this predicts rectangle scale1/98784 and conversion2048/3087 to the
triangle scale1/65536. The full rank4 chain map has not been enumerated. Ranks1
and2 have explicit exact matrix verification.

A constant additive rectangle-class budget of scale6 would weight its cells by
84^(n-1). Matching triangle-class budgets would use(3/2)*64^(n-1). Those weights
implement an additional additive budget law; fresh unit weights implement the
different scales computed here. Matching class metrics alone does not replace
retention of source closure constraints or complementary cell information.

## Structural consequence

Weighted comparison transport extends to both independent orientation classes.
The representation-dependent cost is accounted for by local multiplicities and
retained closure data. The remaining architectural choice is which cross-rank
budget the system uses, followed by its implementation in costed higher-cell
records. The direct-reference/root adapter and recursive slot masks are separate
unresolved parts of the full physical model.

## Verification

    OPENBLAS_NUM_THREADS=1 uv run research/nima/checkers/check_two_factor_weighted_chain_transport.py

The checker constructs harmonic source representatives, the chain map, periods,
and closure checks using exact Fraction arithmetic. NumPy proposes normal-equation
multipliers; rationalized multipliers must solve every equation EXACTLY. Exact
orthogonality and Gram identities certify the resulting minimum-norm lifts.
It also checks mixed class returns, the84-assignment count and the rank4
product-count prediction.
