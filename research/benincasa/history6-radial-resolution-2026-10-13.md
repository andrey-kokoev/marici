# History6 endpoint/boundary iteration 7 — positive radial resolution and blowdown obstruction

Freshly read the b3 boundary receipt/checker and current work-net (pins v33). Resolve the indeterminate b2=b3=0 source corner by

    b2=rho*t, b3=t,
    ordered coordinates (b1,t,rho,b4,b5,b6,b7,b8).

The eight-dlog transition determinant is -1. Deleting t at index1 has parity -1, so the transported exceptional residue has coefficient +1 on the remaining order (b1,rho,b4,b5,b6,b7,b8). The actual pulled-back quotient weight is

    c6 = (b4+rho*t+t)/((b4+t)(rho+1)).

At t=0, with rho and remaining parameters positive, the resolved split seven-forms have coefficients

    K0: 1/(rho+1),   B22: rho/(rho+1),   total: 1.

Their source-local exceptional coefficient is regular; the formerly added pole b2+b3 becomes the excluded divisor rho=-1. Its signed six-dlog split residues are +1 and -1, summing to zero. Direction endpoints have weights (1,0) at rho=0 and (0,1) at rho=infinity; the latter changes dlog orientation by dlog rho=-dlog(1/rho), retained explicitly rather than inferred from weights.

## Actual target image and fiber

The exceptional source matrix at t=0 is independent of rho. At both positive external fixtures:

- exceptional target tangent rank is six;
- full radial-chart target germ rank is seven;
- original unblown F6 target germ at the same corner has rank eight;
- the rho target tangent vanishes exactly and is the one-dimensional exceptional boundary kernel.

Two positive rho values give the same target point but different K0/B22 weights. Thus the resolved exceptional scalar coefficient does **not** descend to an ordinary scalar on the blowdown corner. Moreover the source exceptional form has degree seven whereas the image has rank six: its ordinary target seven-form residue/pushforward is unavailable, not zero. No integration or fitted average over the lost rho fiber is introduced. The original quotient denominator still vanishes on the blowdown center; source resolution does not regularize it on the ordinary target automatically.

The b3=0 regular rank-seven square and b2=b4=0 common-corner calculation remain valid on their own localized opens. This exceptional contraction is a distinct disposition, not a retroactive change to those witnesses.

## Continuation and verification

Next executable continuation: use the actual regular unblown F6 inverse to define a target blowup with t=b3(Y), rho=b2(Y)/b3(Y), and six surviving source-inverse coordinates. Verify inverse arcs and the exceptional residue square on that decorated target. Keep the unavailable ordinary blowdown residue and missing physical boundary-supercomponent compatibility separate; a decorated-target result is not a global weighted map.

Evidence: `checkers/check_history6_radial_resolution.py`, `results/history6_radial_resolution.json`. The first run failed a syntactic SymPy equality for the unsimplified weight sum; replacing it with exact rational simplification gave a passing fresh rerun without changing the coefficient or candidate. All scientific verdicts unchanged. Successor pins v34 and structural net/SCC checks are distinct from the rank/fiber computation. A nonredundant executable continuation remains.
