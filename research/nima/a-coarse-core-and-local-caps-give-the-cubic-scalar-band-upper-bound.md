# A coarse core and local caps give the cubic scalar-band upper bound

## Result

For the moment-curve polygon with vertices

    y_i=(t_i,t_i^2),  t_i=i/n,  i=1,...,n,

let f and g be the lower and upper envelopes of the lifted vertices (t_i,t_i^2,t_i^3). There is a continuous piecewise-affine scalar section satisfying

    f-eta <= v <= g+eta

on the ENTIRE polygon, with at most

    min(n-2, 1+2*eta^(-1/3))

convex polygonal cells when eta>0. At eta=0 the usual n-2-cell exact triangulation applies. The displayed bound is a real upper bound on the integer cell count, not a claim about an exact optimal count.

This supplies the missing whole-polygon upper-bound scale identified in `research/voevodsky/the-full-atom-metric-reduces-to-a-scalar-envelope-band.md`. It matches the order of the previously proved sparse-vertex lower bound in its stated regime. The argument below, rather than the finite experiments, proves the upper bound.

## 1. Separate the coarse core from the omitted boundary caps

Choose a subsequence of the original vertices, including the first and last. Suppose there are r successive parameter intervals between selected vertices.

Their convex hull is the coarse inner polygon. Triangulate it using its selected vertices and interpolate their TRUE cubic heights on each triangle. This uses r-1 triangles; if only two vertices were selected, the core is a segment and contributes no two-dimensional cell.

The omitted part of the original polygon consists of boundary caps, one for each selected interval containing omitted vertices. A cap is the convex polygon formed by all original vertices on that interval, closed by the chord between its selected endpoints. An interval with adjacent original endpoints has no cap of positive area.

These chords do not cross. The core and caps cover the original polygon, and their interiors are disjoint. There are at most r caps, hence at most 2r-1 cells altogether.

The core's section is EXACTLY between f and g. At each triangle vertex every lower supporting plane is below the true height and every upper supporting plane is above it. Affinity extends both inequalities to the whole triangle. Equivalently, the lifted triangle lies in the convex hull of the lifted original vertices.

## 2. A local cubic interpolant fills each cap

For a cap with parameter endpoints a<b, put m=(a+b)/2 and define the affine function of public coordinates

    L_ab(p,q)=-(am+ab+mb)*p + (a+m+b)*q + amb.

On the moment curve,

    t^3 - L_ab(t,t^2) = (t-a)(t-m)(t-b).

For every t in [a,b],

    |(t-a)(t-b)| <= (b-a)^2/4,
    |t-m| <= (b-a)/2.

Consequently

    |t^3-L_ab(t,t^2)| <= (b-a)^3/8.

The midpoint need not be an original polygon vertex. It defines an affine formula, not a new observed source value.

At every original vertex on this cap, f=g=t^3. If the cap width h=b-a satisfies h^3/8<=eta, the proposed affine formula satisfies the band at every cap vertex. For EACH lower supporting plane l and upper supporting plane u,

    l-eta <= L_ab <= u+eta

holds at all those vertices. These are affine inequalities, so they hold throughout the convex cap. Taking the maximum over lower planes and minimum over upper planes gives the required whole-cap band.

This is the step that upgrades boundary approximation to a whole-domain certificate; arbitrary vertex interpolation without the cell and envelope argument would not suffice.

## 3. Continuity

At both selected endpoints, L_ab takes the exact cubic height. On the chord shared with the core, both adjacent affine formulas therefore equal the same linear interpolation between the endpoint heights.

The core triangles agree along their shared edges for the same reason. Neighboring caps agree at their common selected vertex. Thus the resulting section is continuous on the entire polygon.

## 4. Choose the stride and count cells

On the original uniform grid choose stride

    s=max(1, min(n-1, floor(2*n*eta^(1/3)))),

including the last vertex even when the stride does not divide n-1. This can be implemented using integer cube comparisons, without floating-point roots.

If s=1, there are no omitted boundary vertices: the exact n-2-triangle section suffices regardless of the width estimate. Otherwise every cap has width at most s/n, so its error is at most eta.

There are r=ceil((n-1)/s) selected intervals, giving K<=2r-1. If the stride clips at n-1, K=1. Otherwise, when 2*n*eta^(1/3)>=2, rounding gives s>=n*eta^(1/3), hence

    K <= 1+2*eta^(-1/3).

When 2*n*eta^(1/3)<2, the exact n-2 bound is already smaller than that expression.

The construction also always has K<=n-2: if an interval spans d original grid steps, its possible cap contributes at most d-1 cells. Summing over intervals gives at most n-1-r caps, plus r-1 core triangles. This proves the claimed minimum bound.

## 5. Return to the original atom metric

The metric-complete reduction uses

    M=16513*128^-4,  eta=epsilon/M.

Clamp v to [0,1] and apply the admitted affine source inverse S. Public moments remain exact and the returned source is within epsilon, in original atom infinity norm, of each history fiber at the same public point.

For K scalar cells, clipping gives at most 3K explicit convex cells. Counting DISTINCT source formulas instead gives at most K+2 formulas, because the two clipped source formulas are shared.

Thus the construction achieves the corresponding O(min(n,(M/epsilon)^(1/3))) scale in the nontrivial tolerance regime, with the ordinary constant-piece floor at coarse tolerances. It does not identify the optimal constants, the exact one-piece threshold, or a total-byte compression theorem. The source admission and metric identities are inherited from the cited owning-family reduction, not reproved by the scalar packet checker.

## Exact certificate implementation

`research/nima/checkers/verify_scalar_envelope_band.py` imports no candidate constructor. From n it independently reconstructs the moment-curve polygon and all lower and upper supporting planes using exact rational arithmetic.

For each supplied convex cell it checks:

- positive area, convexity and containment in the original polygon;
- every lower and upper plane inequality at every cell vertex;
- pairwise absence of overlapping interiors;
- affine agreement on all vertices of pairwise cell intersections;
- equality between the total cell area and polygon area.

Containment, disjoint interiors and area equality imply exact coverage here: a missing point in a finite closed union would leave a relatively open gap of positive area. Affine agreement on intersection vertices proves continuity on whole shared edges, including partial-edge intersections.

Because f is a maximum and g a minimum of affine planes, this verifier does not need to explicitly construct the common refinement with their envelope partitions. The all-plane inequalities are equivalent and certify the whole candidate cells directly.

## Finite controls and separate costs

Thirty archived certificates cover n=6,10,18 and eta=0,1/1000,1/100,1/10,1/2: fifteen use the direct integer-cube width rule above, and fifteen use finite candidate search. The width-rule packets also pass the rational count tests K<=n-2 and (K-1)^3*eta<=8.

The search compares coarse-core/cap and simple fan candidates and retains a smallest cell-count candidate among those tested. It is not asserted to find the global optimum. For n=18, its selected cell counts are respectively 16, 8, 3, 1, 1. All thirty packets pass the independent whole-polygon verifier.

Six corruption controls are rejected. In particular:

- an overlapping cover with exactly the correct total area fails the pairwise test;
- a discontinuous section inside a permissive band fails continuity;
- an interior bump retains EXACT cubic values at every original public vertex, and has valid coverage and continuity, but fails the strict band inside the polygon.

Formula counts, convex-cell counts, cell-vertex incidences, plane/vertex checks and encoded certificate bytes are reported separately. A cap can have many boundary vertices even when it uses one formula and one cell. The explicit domain geometry and verification work do not disappear with the formula count.

## Reproduction

    python research/nima/checkers/check_scalar_envelope_band.py
    python research/nima/checkers/verify_scalar_envelope_band.py

Artifacts: `research/nima/results/scalar-envelope-band*`.

Related source-metric note: `research/voevodsky/the-full-atom-metric-reduces-to-a-scalar-envelope-band.md`.
