# Approximate common lifting has a positive but scale-sensitive complexity obstruction

**Follow-up:** `the-full-atom-metric-reduces-to-a-scalar-envelope-band.md` strengthens the sufficient lower-bound tolerance by a factor of 16513 and removes the metric-conditioning gap below. The bounds here remain valid but are conservative.

## Contract

Retain the two-history moment-curve family of `merging-two-histories-forces-linear-common-section-complexity.md`. A returned source vector must satisfy original atom caps and public moments exactly. At every public point y it must be within epsilon in the ORIGINAL atom-coordinate infinity norm of each history's fiber AT THAT SAME y. It need not belong to either fiber exactly. Sections are continuous finite piecewise-affine source-vector functions.

Distance is to each history separately, not to their intersection. The argument below respects that weaker approximate contract. Fine t1=51 need not hold exactly for the returned vector; the lower bound only uses its t0 readout. Exact witnesses used to measure distance still satisfy each history's full evidence.

## Positive-tolerance lower bound

At the public vertex (t,t^2), history A forces h>=t^3 and history B forces h<=t^3, with source t0=50+delta*h and delta=128^-4. Being epsilon-close to both fibers therefore forces

    |h_returned-t^3|<=eta, eta=epsilon/delta.

An affine source formula induces an affine h formula in (p,q); restricted to the moment curve this is a quadratic polynomial in t. For four distinct parameters t_i, define divided-difference weights

    w_i=1/product_(j!=i)(t_i-t_j).

These annihilate quadratics and satisfy sum_i w_i*t_i^3=1. If one affine formula meets all four vertex tolerances, necessarily

    1<=eta*sum_i |w_i|.

If consecutive parameters have gaps at least s, then

    sum_i |w_i| <= (1/6+1/2+1/2+1/6)/s^3 = 4/(3s^3).

Thus eta<3s^3/4 rules out any one formula serving all four. With the original grid s=1/n, every continuous piecewise-affine common section requires at least ceil(n/3) formulas whenever

    epsilon < 3*delta/(4*n^3).

As in the exact proof, continuity and finitely many formulas assign at least one limiting formula to every boundary vertex; open cells do not evade the count. The exact n-2-piece construction remains a valid upper bound. Hence matching-order Theta(n) complexity persists at these positive tolerances, whereas separate histories still have exact one-piece sections.

For four equally spaced vertices the divided-difference threshold is sharp as a scalar interpolation obstruction: choose errors eta*sign(w_i) at eta=3s^3/4. The corrected heights have zero third divided difference, hence fit a quadratic. This does NOT prove feasibility of a one-piece approximate source section over the whole public domain at that threshold.

## Sparsified bound at larger tolerances

Select grid vertices with stride k. Their minimum separation is k/n and their number is floor((n-1)/k)+1. If eta<3(k/n)^3/4, no formula covers four selected vertices. This gives the corresponding one-third vertex-count lower bound, even when adjacent original vertices no longer produce an obstruction.

Up to constants and finite-domain cutoffs, the resulting lower-bound scale is min(n,(delta/epsilon)^(1/3)). This is only a LOWER-bound scale. No matching epsilon-dependent upper bound has been established.

## A coarse regime where one piece suffices

For the fixed-t1 source inverse, changing h at fixed public moments changes the actual atoms by

    delta*(1, 0, -16513, 16512)*dh.

Thus its infinity-norm Lipschitz constant is M=16513*delta. The global affine source section h=1/2, t1=51 is source-admitted over the entire parameter cube and preserves both public moments. Each history has a nonempty h interval in [0,1]; choose the nearest point of that interval to 1/2. Its source distance from the returned section is at most M/2.

Consequently one common affine piece suffices for epsilon>=16513/536870912 (about 3.08e-5 atom units), for every n in this family.

The lower bound used only the t0 coordinate and delta, while this upper bound uses the full inverse direction and M. The conditioning gap is real and is NOT silently normalized away. Neither threshold is asserted to be the optimal operational transition.

## What was learned

The exact separation is not solely a zero-error artifact: it survives an explicit positive original-coordinate tolerance. But the present full linear lower bound requires epsilon shrinking as n^-3, multiplied by the very small embedding scale delta. For n=18 its sufficient tolerance is below roughly 4.8e-13 atom units. This is not evidence of practically robust linear growth at a fixed tolerance.

At sufficiently coarse fixed tolerance the separation disappears completely. The intermediate optimal complexity, especially with the full source metric rather than the single-coordinate necessary condition, remains open in this lane. We have not earned a matching tolerance-dependent compression theorem.

## Reproduction

    python research/voevodsky/checkers/check_robust_lifting_tradeoff.py

Artifact: `results/robust-lifting-tradeoff.json`.

The direct exact checker verifies divided-difference identities and norm bounds for every quartet through n=18, positive-tolerance controls, the scalar sharpness construction, sparsified lower bounds at n=60, and original source inverse/cube admission. This is not an independent packet verifier or a total-storage lower bound.
