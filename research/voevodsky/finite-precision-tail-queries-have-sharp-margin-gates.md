# Finite-precision tail queries have sharp margin gates

## Contract

Pin all source coordinates except p=m-2,q=m-1 exactly. Subtract their moment contributions. The supplied residual measurement is a certified box

    |U-Uhat|<=epsilon_U, |V-Vhat|<=epsilon_V.

This is a coordinatewise error box, not the L1 error ball used in the earlier conditioning theorem. Pin values have no error in this experiment. Write r=128^-p, s=128^-q and d=r-s>0.

The admitted residual sources are the intersection of their source-cap rectangle with the four measurement inequalities. No single member of this intersection is declared the actual source.

## Sharp reconstruction interval away from cap clipping

The unconstrained inverse is

    x=(V-s U)/d, y=(r U-V)/d.

Thus x has center xhat=(Vhat-s Uhat)/d and radius

    rho=(epsilon_V+s epsilon_U)/d.

These extrema occur at opposite measurement-box corners. The formula is sharp if the inverse box fits inside the source caps (or the relevant extremizing corners remain admitted). Near cap boundaries, intersect with the source constraints before taking extrema; clipping x alone is not generally enough because y constraints also matter.

A convenient sufficient condition for the entire inverse box to be admitted is that rho fits both x margins and (epsilon_V+r epsilon_U)/d fits both y margins. The checker uses interior controls satisfying these conditions and an exact polygon calculation that enforces caps in all cases.

## Three-valued audit answers, plus inconsistency

For the audit x<=h, let [lo,hi] be the exact feasible x interval:

- empty feasible set: INCONSISTENT;
- hi<=h: FORCED_TRUE;
- lo>h: FORCED_FALSE;
- otherwise: UNRESOLVED.

In the last case there are admitted witnesses with opposite truth values. This is not optimizer failure: no sound answer about the actual source can choose a truth value from the supplied data alone. The feasible set and its two extremal witnesses provide a useful answer even when point reconstruction is poorly conditioned.

The weak inequality matters: hi=h still forces truth, while lo=h does not force falsehood.

## Precision threshold

At an interior measurement center, take h=xhat+gamma with gamma>0. The audit is forced true exactly when

    epsilon_V+s epsilon_U <= d gamma.

For the final two slopes, multiplying by 128^(m-1) gives

    128^(m-1) epsilon_V + epsilon_U <= 127 gamma.

Thus weighted-moment error and total-mass error have very different amplification in these fixed coordinates. With exact U, a fixed positive audit margin requires epsilon_V<=127 gamma /128^(m-1): exponentially small absolute error. Under a binary absolute-precision convention epsilon_V=2^-b, this means b>=7(m-1)-log2(127 gamma), rounded up with b>=0. Exponential conditioning therefore corresponds to linear growth of required fractional precision bits at fixed margin, not exponential bit count.

This is a worst-case interior margin requirement under the frozen norm and measurement normalization. Source caps or additional evidence can improve particular cases. It is not a bit-complexity estimate for computing the answer, and it does not cover noisy pins.

## Exact controls

For m=3,4,8,16,64 the checker tests exact moments, errors below/at/above the margin, simultaneous U/V errors, a forced-false query, and inconsistent measurements. It verifies sharp extrema and constructs opposite-truth witnesses in the unresolved case. The continuum law follows from the explicit affine inverse, not the finite tests.

    python research/voevodsky/checkers/check_tail_precision_queries.py

Artifact: `results/tail-precision-queries.json`. This is an exact analytical checker, not a separate independent certificate verifier or a fresh replay of upstream source admission.

## Synthesis

A query interface need not turn every approximate observation into a single supposedly reliable witness. It can retain the uncertainty set and return a forced answer, a certified ambiguity, or inconsistency. This separates sensitivity of representative reconstruction from correctness of set-valued query answering. Audit tolerances and noisy audit values remain separate extensions; this experiment varies moment precision only.
