# Preconditioned-spline coefficient robustness

Correction: these perturbations test the pole-deleted executable functional. They generally break the baseline’s double zeros at exponential modes `2` and `1/2`, so they are not criterion-admissible without restoring the omitted pole terms. See `preconditioned-spline-pole-term-correction.md`.

## Question

How large a perturbation of the five shift coefficients is certified to preserve the narrowly positive Gram interval?

## Claim boundary

The executable form is linear in the coefficient vector. The checker was parameterized by a global five-component vector, and each coordinate basis was evaluated with the same exact moment, prime, and tail machinery.

The component intervals, ordered by shifts `2a,a,0,-a,-2a`, are approximately

\[
(-0.00113853,-0.20490932,-2.17343226,-5.22867389,-9.23594955).
\]

Every component is negative. A conservative bound for their absolute values is `M=9.235949548136842`. If `delta c` is a coefficient perturbation, interval linearity gives

\[
|L(\delta c)|\le M\|\delta c\|_1.
\]

Using the certified baseline lower endpoint, every perturbation satisfying

\[
\|\delta c\|_1<1.2765824107972949\times10^{-6}
\]

preserves strict positivity. This is a certified sufficient radius, not a claim that the full positive region is an l1 ball or that this bound is optimal in another norm.

A deliberate crossing changes the final coefficient from `1` to `1.000002`. Linear interval transport gives

\[
[-6.6814483561\times10^{-6},-6.5658854606\times10^{-6}],
\]

strictly negative.

## Evidence

- Component executions: `structured_command_execution:e_4616_1788288609855677200_30`, `e_4616_1788288650049226700_31`, `e_4616_1788288816722942800_35`, `e_4616_1788288873527871300_36`, `e_4616_1788288928277899100_37`
- Radius and crossing arithmetic: `structured_command_execution:e_4616_1788288951290705200_38`
- Full baseline regression: `structured_command_execution:e_4616_1788289063184945900_39`

## Disposition

The baseline sign is mathematically strict but coefficient-fragile. Perturbations at the scale of two parts per million in the most sensitive coordinate reverse it.
