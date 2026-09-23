# Exact slope-face fibres rule out two positive first-order B-to-D matches

The previous normal-quotient calculation required a **finite** shift along the collapsed source-weight direction to match B's slope-gap target jet using cell D. Here that fibre is solved **exactly**, rather than by truncating a Taylor series. At each of two positive `t=u` controls, the rank-seven kernel vector `r` has entries only in the five source weights `(w₄,w₅,w₆,w₇,w₈)`. Because the target plane's face dependence on those weights is linear, **the entire line** `p+λr` has exactly the **same target plane**, for every λ for which the chosen chart exists. Thus finite-λ normal-jet comparisons are meaningful at one fixed target-face point.

Projecting the **exact** D normal jet along this face fibre to the shared two-dimensional target normal quotient, parallelism with B's normal jet at `p` has one rational candidate at each control:

* First positive control: `λ=−7098/4169`; D weights become `w₄=−2156/379`, `w₆=−16072/4169`, `w₈=−2929/4169` (negative).
* Second positive control: `λ=−57011/13291`; D weights become `w₄=−51072/13291`, `w₆=−22204/13291`, `w₈=−3847/13291` (negative).

The required slope-gap rescaling is positive in both cases, but **neither unique first-order matching point lies in the positive D cell**. This is a stronger obstruction than the earlier infinitesimal jet mismatch for these two exact targets and their explicitly parametrized face-fibre branches. It is **not** an exclusion theorem for other face preimages, other cells, other positive data or nonlinear image coverage; it does not compute a pushed image-form residue.

Checker: `research/nima/checkers/check_nine_point_slope_face_exact_fibre_normal_match.py`; certificate: `research/nima/results/nine-point-slope-face-exact-fibre-normal-match.json`.
