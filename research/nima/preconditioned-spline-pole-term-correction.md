# Pole-term correction to the coefficient and contradiction audits

## Question

Does the Fourier-nonnegative negative rival define a contradiction to the Weil criterion under the checker’s omitted-pole form?

## First mismatched term

The five-shift Laurent multiplier is

\[
P(z)=z^2-5z+\frac{33}{4}-5z^{-1}+z^{-2}
=\left(z+z^{-1}-\frac52\right)^2.
\]

Hence `P(2)=P'(2)=0`, and by reciprocity the same double zero occurs at `z=1/2`. These are exactly the exponential modes associated with the pole evaluations in the completed zeta explicit formula. The checker does not include separate pole terms because the baseline preconditioner annihilates them.

The perturbation `epsilon(1,0,-2,0,1)` preserves symmetry, coefficient sum, and Fourier nonnegativity, but

\[
P_{\epsilon}(2)=\frac94\epsilon.
\]

For `epsilon=3e-6`, this equals `27/4000000`, not zero. Therefore the checker’s pole-deleted functional is not the completed Weil functional on this rival. Its negative interval cannot be transported into a contradiction with RH or all-test Weil positivity.

## Correction to the coefficient-space claim

If pole annihilation is imposed in addition to symmetry, write coefficients as `(u,v,w,v,u)`. The equations `P(2)=0` and `P'(2)=0` give

\[
v=-5u,\qquad w=\frac{33}{4}u.
\]

Thus admissible coefficients form a one-dimensional ray, and fixing the outer normalization `u=1` uniquely recovers the baseline vector. The prior two-dimensional space described only symmetry plus a provisional coefficient sum; it was not the admissible space for the pole-deleted checker. Its optimization and sign-reversal conclusions are retracted at criterion level but remain valid sensitivity calculations for the incomplete functional.

## Evidence

- Exact checker/result: `research/nima/checkers/preconditioned_spline_admissibility.py`, `research/nima/results/preconditioned_spline_admissibility.json`
- Execution: `structured_command_execution:e_4616_1788289840867552000_44`

## Disposition

No conditional Weil-criterion contradiction survives. The complete symmetric double-pole-annihilating family is `u(1,-5,33/4,-5,1)`. By linearity and the certified baseline interval, its pole-deleted Gram form is strictly positive for `u>0`, zero for `u=0`, and strictly negative for `u<0`; requiring Fourier nonnegativity selects `u>=0`. Execution `structured_command_execution:e_4616_1788290017787153600_45` checks the exact solve. A source convention map for the remaining archimedean and arithmetic terms is still absent.
