# The full atom metric reduces to a scalar envelope band

## Improvement over the previous bound

The earlier approximate-lifting note used the t0 coordinate alone and obtained a valid but unnecessarily weak tolerance threshold. The full source geometry yields a 16513-fold improvement. It also reduces the entire approximate lifting problem, including possible off-line outputs, to scalar envelope approximation up to constant-factor piece complexity.

Use the same owning m=4 two-history family, source inverse S(y,h) with t1=51, delta=128^-4 and histories h in [f(y),1] and [0,g(y)]. Their public domain is the moment-curve polygon, and 0<=f<=g<=1. Define M=16513*delta.

At fixed public moments the inverse direction is

    dS/dh=delta*(1,0,-16513,16512).

Consequently ||S(y,h)-S(y,h')||_infinity=M*|h-h'| EXACTLY.

## A metric-complete affine readout

For ANY returned source vector x with public moments y, whether or not x has t1=51, define

    H_y(x)=(S(y,0)_2-x_2)/M.

Here atom indices start at zero. On the original fine line H_y(S(y,h))=h. Moreover

    M*|H_y(x)-h|=|x_2-S(y,h)_2|<=||x-S(y,h)||_infinity.

Thus epsilon-closeness to both history fibers necessarily implies

    f(y)-eta <= H_y(x) <= g(y)+eta, eta=epsilon/M.

This necessity remains valid for off-line outputs. It does not presume that their nearest witnesses coincide or that distance to each history equals distance to the intersection.

## Constructive converse

Suppose a scalar function v(y) obeys that band. Clamp it to c(y)=min(1,max(0,v(y))) and return S(y,c(y)).

Clamping cannot increase distance to an interval contained in [0,1]. The distance of c to [f,1] and [0,g] is therefore at most eta. By the exact source-line norm identity the returned source vector is within epsilon of both histories. It also satisfies exact public moments and source admission, since the entire parameter cube was admitted.

The scalar criterion is therefore both necessary and sufficient for the approximate contract. Necessity extracts a scalar from any source section; sufficiency constructs a possibly different section. It is not an equality of distances for every off-line returned vector.

## Representation complexity

The readout is jointly affine in y and x, so a K-formula continuous piecewise-affine source section yields a K-formula scalar band function. Conversely, clipping a scalar section and applying S uses at most K+2 distinct affine formulas: one per original formula, plus the shared source formulas S(y,0) and S(y,1).

If charging explicit convex polyhedral cells rather than distinct formulas, clipping splits each original cell into at most three, giving at most 3K cells. These are different accounting conventions and should not be conflated. Shared domain partitions and proof storage remain separate costs.

## Stronger positive-tolerance obstruction

At each public vertex both envelopes equal t^3. Therefore the extracted scalar must approximate t^3 to eta=epsilon/M, not merely epsilon/delta. The divided-difference proof in the earlier note applies unchanged and yields

    K>=ceil(n/3) whenever epsilon<3M/(4n^3).

At n=18 the threshold improves from about 4.8e-13 to about 7.91e-9 original atom units. The same sparse-vertex proof now gives a lower-bound scale min(n,(M/epsilon)^(1/3)), subject to its stated finite-domain cutoffs.

At epsilon>=M/2 the constant scalar 1/2 still gives a one-piece source section. The conditioning mismatch in the earlier bounds has been removed: both sides now use the same original-metric scale M. The n^-3 dependence remains, and a matching intermediate tolerance-dependent upper bound has NOT been proved.

## What remains

The open problem is now precise and scalar: how many affine pieces are needed for a continuous function lying between f-eta and g+eta on the moment-curve polygon? Source-coordinate conditioning and off-line witness freedom are no longer excuses for the gap. A claimed solution must control the entire polygon, not just approximate cubic heights at its vertices.

## Reproduction

    python research/voevodsky/checkers/check_metric_complete_lifting_reduction.py

Artifact: `results/metric-complete-lifting-reduction.json`.

The direct checker verifies the readout for off-line source coordinates, interval distance inequalities, clamping, exact source-line distance and admitted reconstructed witnesses in 675 rational controls. The universal claims follow from the affine coordinate identities and interval projection argument above, not sampling. It also recomputes the improved rational thresholds. This is not an independent packet verifier or a total-byte bound.
