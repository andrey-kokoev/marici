# Spin(5) finite-discordance certificate (WP906)

## Question

Can WP902 certify the one-percent conditional-shape tolerance when a valid
paired run observes a small nonzero number of discordances?

## Exact acceptance test

Retain WP902's pilot design quantities

\[
a_{\min}=\frac{389}{14688},\qquad
\varepsilon=\frac1{100},\qquad
p_0=\frac{a_{\min}\varepsilon}{2}
=\frac{389}{2937600}.
\]

At each pole let (K\) be the discordance count among (n) independent paired
trials. To reject the composite null (p_D\geq p_0) at per-pole level
(alpha/2=1/40), accept the stability claim only when

\[
\Pr_{p_0}\{\operatorname{Bin}(n,p_0)\leq K\}\leq\frac1{40}.
\]

The binomial lower tail decreases with (p_D), so its largest probability
under the null boundary relevant to rejection occurs at (p_0). This is an
exact one-sided test; no Gaussian or Poisson approximation is used.

Writing (p_0=a/b), the checker evaluates the decision as the integer
inequality

\[
40\sum_{j=0}^{K}{n\choose j}a^j(b-a)^{n-j}\leq b^n.
\]

## Exact minimum budgets

The minimum pairs per pole are generated for (K=0,1,2,3). Each reported
minimum passes the integer inequality and one fewer pair fails. Thus an early
discordance no longer terminates the experiment; it moves the preregistered
run to the corresponding larger budget.

This is a fixed-count design. Choosing the final budget after inspecting an
unregistered sequence of outcomes would require a separate anytime-valid
confidence sequence or a frozen escalation rule with familywise error
control. The two-pole allocation remains (1/40) per pole.

## Boundary

The test inherits WP905's requirements: both arms must have independently
validated marginals, the pairing manifest must replay, null outputs must be
retained, and pairs must be independent. It also inherits WP902's provisional
acceptance floor. Passing certifies response stability only. It selects no
flavor point and rigidifies no presentation.

Run:

~~~text
uv run python research/flavor/checkers/wp906_spin5_finite_discordance_certificate.py
~~~
