# Fixed gamma multiplier cannot uniformly semibound prime cutoffs

## Question

Can the archimedean gamma multiplier, added pointwise to each finite prime multiplier, provide a cutoff-independent lower bound on the full heat-observer Hilbert space?

## Claim boundary

No, provided the gamma multiplier is fixed and locally bounded near frequency zero. The joint multiplier still tends to minus infinity there as the prime cutoff grows. This rejects a full-space pointwise multiplier completion, not a source-regularized distributional limit or a lower bound restricted to the analytic heat-polynomial core.

## Joint cutoff multiplier

Let

\[
W_N(u)
=
W_\Gamma(u)+W_{P,N}(u),
\]

where

\[
W_{P,N}(u)
=-
\sum_{2\leq n\leq N}
\frac{\Lambda(n)}{\sqrt n}
\cos(u\log n).
\]

The archimedean digamma multiplier is finite at \(u=0\). Hence

\[
W_N(0)
=
W_\Gamma(0)
-
\sum_{2\leq n\leq N}
\frac{\Lambda(n)}{\sqrt n}
\longrightarrow
-\infty.
\]

Continuity of each finite cutoff gives a positive-measure neighborhood on which \(W_N\) is arbitrarily negative. Therefore

\[
\operatorname*{ess\,inf}_{u}W_N(u)
\longrightarrow
-\infty.
\]

No constant \(C\), independent of \(N\), can satisfy

\[
\langle f,M_{W_N}f\rangle
\geq
-C\lVert f\rVert^2
\]

for every vector in the full ambient \(L^2(\rho_{t,h})\).

## Why logarithmic ellipticity does not repair this

The gamma multiplier grows like \(\log|u|\) at high frequency. That can dominate a fixed finite-prime order-zero perturbation in a high-frequency tail. It does not dominate the conductor-cutoff divergence concentrated near \(u=0\). These are distinct limits.

Thus the fixed-support ellipticity argument and the unbounded-conductor completion problem cannot be interchanged.

## Remaining analytic-core possibility

The observation vectors have restricted form

\[
f(u)=p(e^{-hu^2}).
\]

A cutoff-dependent negative neighborhood may shrink too rapidly to be captured efficiently by a polynomial of bounded degree. Consequently the present no-go does not establish failure on a graph-norm-controlled analytic core where degree, mesh, and conductor cutoff are coupled.

Any surviving theorem must state that coupling explicitly and prove a uniform inequality there. Passing from that core to a closed form also requires density in the resulting graph norm.

## Higher-coherence interpretation

The pointwise sum of finite gamma and prime multipliers is not the higher coherencer. Its lower-bound residual diverges with conductor. A viable higher coherencer must alter the completion operation itself by one of:

1. combining gamma and prime through the exact explicit-formula distribution before operator realization;
2. imposing a source-derived analytic graph domain that forbids uncontrolled concentration;
3. adding an authorized counterterm whose change to the form is tracked exactly.

## Disposition

`joint_full_L2_multiplier_semiboundedness` fails. The surviving gate is `joint_analytic_core_semiboundedness`, followed by closability and graph-norm density. RH is not advanced.

## Verification

- `research/voevodsky/checkers/check_fixed_gamma_prime_lower_bound.py`
- `research/voevodsky/results/fixed_gamma_prime_lower_bound.json`
