# Mesh-uniform comparison of actual source insertion words

## Question, stratum and claim

Can actual finite-box insertion moments approximate the thermodynamic moments uniformly over the number and spacing of insertions, rather than only for each fixed word?

The SCC obligation is forward realization and state-based readout comparison. The source is unchanged: SU2 spatial links, actual vacuum measures nu and nu_Lambda, and their actual Markov semigroups P and P^Lambda. Set a=4/3, R=4096r/3<9/64, alpha=8R/9, c=1/2-3R and m=kappa*c. These parameters retain their declared lattice-source, not physical-clock, interpretation.

Take any FINITE ordered list t1<=...<=tn and real smooth gauge-invariant cylinders f_j supported in one finite K inside Lambda. Require ||f_j||_infinity<=1 and sum_j M(f_j)<=B, where M sums link-gradient sup norms in the radius-two metric. Put b=d(K,Lambda complement). Let S and S_Lambda be their actual nested propagation/multiplication moments, integrated against nu and nu_Lambda respectively.

**Written comparison theorem:** simultaneously for all such finite lists, with no mesh, count or horizon factor,

\[
|S-S_\Lambda|\le (3/4)^b B
\max\left\{\frac{2R}{c},\frac{44}{7}\eta_R\right\}
\le\frac{18}{5}B(3/4)^b,
\qquad \eta_R=\frac R2+\frac\alpha{1-\alpha}.
\]

The coefficient vanishes at R=0. All quantifiers concern finite words with a fixed total gradient budget, not a single limiting infinite product. The analytic proof depends on the existing interaction, gradient and Dobrushin comparison arguments, still independently unreviewed. Exact controls below test algebraic consequences, not those analytic inputs.

## Issue-boundary DPC

- **Problem:** repeated insertion changes intermediate supports; fixed-input semigroup convergence neither budgets those changes nor compares the two vacuum measures.
- **Conjecture:** weighted gradients remain localized under bounded multiplication and damped propagation. Each insertion's gradient contribution telescopes through the partition, while the initial-state discrepancy is bounded by the complementary damped contribution.
- **Rivals:** pay an uncontrolled factor n; keep only propagation error and identify vacuum measures; infer an infinite insertion limit from a uniform finite-word comparison; transfer the claim to iterated conditional projections without derivative control.
- **Risky consequences:** an exact discounted-gradient telescope, an R-sensitive state comparison, and a common finite-word error coefficient independent of mesh and n at fixed B.
- **Strongest falsifiers:** a one-insertion finite-law mean discrepancy1/3 when propagation error is zero; alternating constant insertions with B=0 and consecutive-word difference2 despite zero approximation error. They reject measure identification and an unsupported infinite-word completion, not the scoped theorem.
- **Disposition:** actual finite-word moment comparison is supplied by the argument below. No arbitrary infinite-word or iterated projected-reader theorem is asserted.

## Preserve spatial gradient locality through the word

For a smooth finite-box function u, including functions supported on all of Lambda, define

\[
G_K(u)=\sum_{i\in\Lambda}a^{d(i,K)}\|\nabla_i u\|_\infty.
\]

The positive weighted gradient matrix from the clustering packet and the metric triangle inequality give G_K(P_s^Lambda u)<=exp(-ms)G_K(u), without requiring u to be supported in K. Multiplication by f_j gives G_K(f_j u)<=M(f_j)||u||_infinity+G_K(u), since f_j is supported in K and has sup norm at most1.

Write tau_j=t_(j+1)-t_j, x_j=exp(-m*tau_j), and define u_n^Lambda=f_n and u_j^Lambda=f_j P_(tau_j)^Lambda u_(j+1)^Lambda. Positivity and constant preservation imply ||u_j^Lambda||_infinity<=1. The gradient recursion yields

\[
G_K(u_j^\Lambda)\le
\sum_{\ell\ge j} M(f_\ell)e^{-m(t_\ell-t_j)}.
\]

This is the needed control on varying intermediate inputs; their supports need not remain in K.

The finite-source Duhamel argument in the buffered-memory packet also applies with G_K(u) in place of M(f): the input may fill Lambda but has this weighted localization. It gives

\[
\|(P_s-P_s^\Lambda)u\|_\infty
\le (3/4)^b\frac{2R}{c}(1-e^{-ms})G_K(u).
\]

Prove this first with the larger source box Gamma and pass the already established propagator limit for fixed Lambda,u. No convergence assertion is applied directly to an uncontrolled varying input.

Telescoping the actual and finite nested words uses only sup-norm contractions of both semigroups and multiplication by f_j. Reordering the resulting finite sum uses the exact identity

\[
\sum_{j<\ell}(1-x_j)\prod_{k=j+1}^{\ell-1}x_k
=1-\prod_{k<\ell}x_k.
\]

Therefore, with Delta_ell=t_ell-t1,

\[
\|u_1-u_1^\Lambda\|_\infty
\le (3/4)^b\frac{2R}{c}
\sum_\ell M(f_\ell)(1-e^{-m\Delta_\ell}).
\]

Zero gaps cause no defect and need no minimum spacing.

## Compare the actual vacuum measures separately

Use the thermodynamic packet's influence majorant C and resolvent D=(I-C)^(-1). Let h_i=d(i,Lambda complement) and xi_i be the single-link specification discrepancy. Its existing bounds are xi_i<=R*2^(-h_i-1) inside Lambda and xi_i<=1 outside; globally (D xi)_i<=a^(-h_i)/(1-alpha).

For i INSIDE Lambda, the identity D xi=xi+C D xi improves this to

\[
(D\xi)_i\le a^{-h_i}
\left(\frac R2+\frac\alpha{1-\alpha}\right)
=\eta_R a^{-h_i}.
\]

Indeed the direct term costs at most R/2 after weighting, while the weighted C row costs alpha/(1-alpha). This removes the nonvanishing R=0 error of the earlier coarse bound.

One link's geodesic diameter is2pi in the declared radius-two metric, so its oscillation is at most2pi times its gradient sup norm. Applying the EXISTING real-cylinder Dobrushin comparison to u_1^Lambda, not identifying nu_Lambda with a marginal of nu, gives

\[
|\nu(u_1^\Lambda)-\nu_\Lambda(u_1^\Lambda)|
\le (3/4)^b 2\pi\eta_R G_K(u_1^\Lambda)
\le (3/4)^b 2\pi\eta_R
\sum_\ell M(f_\ell)e^{-m\Delta_\ell}.
\]

The finite function is smooth even when it depends on all box links. Its weighted gradient, not its unweighted support size, controls this scalarization.

Adding the propagation and state errors yields, for each insertion gradient, a convex combination of2R/c and2pi eta_R. The rational bound pi<22/7 gives the claimed coefficient. At the source-window endpoint, eta_R<191/896, hence44 eta_R/7<2101/1568<18/5; also2R/c<18/5. This proves the universal coefficient, without replacing either actual measure or source propagator.

## Executable budgets and exact controls

A fraction-only word planner uses C_R=max(2R/c,44 eta_R/7) and chooses the smallest nonnegative integer b with C_R B(3/4)^b<=epsilon. A universal version uses18B/5. For B=1 and epsilon=1/1000, the full-window rule needs buffer29; at R=9/128 the rational coefficient is4301/6720 and needs buffer23. These are sufficient-budget minima, not optimal-error claims.

The checker freshly replays the buffered-memory receipt. Fifty-four abstract damping grids test the discounted-gradient recursion and telescope with1,2,3,8,31 and128 insertions, including zero-gap factors. Fraction-only planner tests cover zero and near-cutoff couplings. A reversible finite-law pair with distinct stationary measures tests actual nested words and the separate state term; these are controls, not SU2 truncations.

For those controls the reset kernels qI+(1-q)J_pi and qI+(1-q)J_rho have pi=(1,1,1)/3 and rho=(1,4,1)/6, contraction of oscillation by q, and comparison coefficient1/3. Positive bounded insertion functions satisfy the same product inequality. Exact propagation and state budgets sum to B/3 independently of count. At one insertion f=(1,0,1), the mean discrepancy is1/3 although there is no propagation interval. Omitting the state term fails on that fixture.

Finally f_j=-1 is a legitimate constant gauge-invariant insertion with gradient budget0. Both source moments agree exactly, but their values alternate with n. Thus mesh-uniform finite-word error alone does not construct a refinement-compatible infinite insertion or a path-functional limit.

## Surviving scope and next constructor

The result compares actual free-boundary source words and thermodynamic source words, including the vacuum-state discrepancy, for all finite words under the declared sup/total-gradient budget. It does not directly compare arbitrarily iterated compressed K_t strings: conditional projections may not preserve the required weighted derivative class. No physical clock, continuum Yang–Mills or parent/root discharge follows.

**Next executable issue:** impose source-derived sewing for a bounded nonnegative local probe V using factors exp(-delta V), and construct the associated bounded-perturbation product limit with a declared strong-operator topology. The refinement law and finite-word budget must be used; an arbitrary infinite product is excluded by the constant-sign counterexample. Treat the added multiplication as a probe, not a replacement magnetic vacuum or a continuum interaction theorem.

Contract: `research/kitaev/contracts/yang-mills-mesh-word.v1.json`.
Reproduce: `python research/kitaev/checkers/check_yang_mills_mesh_word.py`.
Receipt: `research/kitaev/results/yang-mills-mesh-word-v1.json`.
