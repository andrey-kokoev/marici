# C13 moves from the conductor to its elliptic square-root cover

The conductor is

\[
\mathcal C\cong\mathbb P^1,
\]

and

\[
g(m)=\frac{m(m+1)(x-my)}{(m^2y+x)^2}.
\]

Its divisor has four simple zeros,

\[
0,-1,x/y,\infty,
\]

and two double poles at the roots of \(m^2y+x\). Thus

\[
\deg\operatorname{div}(g)=4-4=0.
\]

After clearing poles, the zero divisor defines \(\mathcal O(4)\).

An ordinary theta characteristic on \(\mathbb P^1\) satisfies

\[
L^2=K_{\mathbb P^1}=\mathcal O(-2),
\]

so \(L=\mathcal O(-1)\). For the four-mark logarithmic canonical bundle,

\[
K_{\mathbb P^1}(D)=\mathcal O(2),
\]

a logarithmic theta line has degree one. The degree-four zero line of \(g\) matches neither theta axiom.

Therefore C13 is rejected in its direct form: \(g\) itself does not define a theta characteristic on the conductor.

A stronger replacement emerges. Consider

\[
\Sigma_g:\quad \xi^2=g(m).
\]

The four simple zeros are branch points, while the double poles are unbranched. Riemann--Hurwitz gives

\[
g(\Sigma_g)=1.
\]

Hence \(\Sigma_g\) is an elliptic double cover of the conductor. Its three nonzero two-torsion classes correspond naturally to the three pairings of the four branch points. This is the appropriate home for the triality data and a prospective quadratic refinement.

The refined conjecture is:

> The Bunch--Davies orientation selects a two-torsion class on \(\Sigma_g\), and its image under the component-difference comparison equals the universal Picard parity \(-K_S\bmod2\).

Certificate:

- `research/voevodsky/checkers/reject_C13_theta_characteristic_axioms.py`;
- `research/voevodsky/results/C13_theta_characteristic_axiom_test.json`.
