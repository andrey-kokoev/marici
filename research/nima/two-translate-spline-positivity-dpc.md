# Two-translate spline positivity — corrected N=3 disposition

## Correction

The earlier N=1 generalized atomic-tail evaluation failed baseline regression and is retracted. Its negative cross interval and coherent negative vector must not be used. The corrected generalized evaluator uses `N=3`, where the diagonal baseline matches exactly.

## Problem

Does positivity of the centered spline extend to the first two-translate Gram cell at `delta=4 log 2`?

## Bold conjecture

The corrected N=3 two-translate Gram matrix is positive semidefinite.

## Strongest falsification attempt and residual

The corrected intervals are

\[
d\in[1.1790450740\times10^{-5},1.1906013635\times10^{-5}],
\]

and

\[
c\in[0.004366227496,0.004366339865].
\]

The determinant satisfies

\[
\det G\in[-1.90647849\times10^{-5},-1.90638008\times10^{-5}],
\]

so positive semidefiniteness remains falsified. Because `c>0`, the negative eigenvalue is now `d-c`; the explicit negative packet is the disagreement vector

\[
h=g-\tau_{4\log 2}g.
\]

The coherent vector is positive.

## Disposition and residual conjecture

The first translate cell still falsifies positivity, but with the opposite eigendirection from the retracted N=1 result. Independent reproduction must preserve the `N=3` baseline regression. The residual conjecture is that the positive cross term is intrinsic to the corrected declared functional rather than a generalized-tail defect.

This is a theorem about the declared executable form, not an RH conclusion without the outstanding source and contour identifications.

## Evidence

- `research/nima/checkers/check_first_two_translate_spline_gram.py`
- `research/nima/checkers/check_two_translate_negativity_margin.py`
- corrected independent execution remains `structured_command_execution:e_11792_1788310575430008500_3`
