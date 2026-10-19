# Mixed bounded-probe response and coupling-sensitive spatial susceptibility

## Question, source and stratum

Can the completed probe construction supply a connected mixed amplitude response with a bilinear spatial bound, including its zero-coupling limit, rather than a derivative inferred from a coarse finite-amplitude inequality?

SCC obligation: bounded-amplitude analytic realization, ordered-insertion sewing and state-based covariance readout. Keep the actual source state nu, semigroup P_s and nonnegative self-adjoint generator A from the prior packets. The source parameter s is not a calibrated physical clock. Retain kappa>0, 0<=r<27/262144, R=4096r/3, c=1/2-3R, m=kappa*c and a=4/3.

Let V,W be bounded smooth real gauge-invariant local probes on disjoint finite supports K,L, ell=d(K,L)>=1. Nonnegative probes belong to the preceding construction; bounded complex amplitude extension below supplies the local derivatives without changing the base state. Write M(V)=sum_i ||gradient_i V||_infinity and V_c=V-nu(V).

## Issue-boundary DPC

- **Problem:** the prior finite-amplitude bound is linear in the sum of gradient budgets and does not control mixed derivatives or connected subtraction.
- **Conjecture:** bounded operator insertion gives a canonical local logarithm at zero amplitude. Its two ordered insertions reduce to a centered source covariance integral; subtracting the identity inside the positive gradient matrix retains a coupling-sensitive off-diagonal bound.
- **Named rivals:** differentiate a real absolute bound; omit one insertion order; use the uncentered second derivative; subtract two unrelated upper estimates; infer an entire logarithm from an entire generating function.
- **Risky consequences:** constant-shift invariant bilinear response, full-distance spatial decay, exact zero at R=0 on disjoint supports, and a controlled large-source-parameter response density.
- **Strongest falsifiers:** constant probes give uncentered mixed derivative2 but connected response0; a reversible weak-pair control loses1/136 in its quadratic coefficient if one ordering is omitted; positive real normalized functions can be within1/16 of1 yet have mixed log derivative4096.
- **Disposition:** written local analytic, covariance and spatial comparison arguments follow. Finite controls do not verify the imported SU2 analysis. No sign or nonzero interacting cross-response, global complex logarithm, finite-amplitude pressure or continuum theorem is inferred.

## Bounded amplitude construction before scalar derivatives

For complex z,w define Q_T(z,w) by the bounded-perturbation Dyson series with generator G-z M_V-w M_W on the existing C(X) carrier. Its time-ordered strong integrals define bounded coefficient operators; their norms have the majorant T^k q^k/k!, where q=|z| ||V||+|w| ||W||. Thus the amplitude series converges in operator norm, locally uniformly in z,w, for each fixed T. This amplitude analyticity is not an operator-norm assertion about partition convergence or source-parameter continuity.

The same series agrees on continuous vectors in the original vacuum Hilbert space. For real amplitudes the operator there is exp[-T(A+z M_V+w M_W)]; complex amplitudes use its bounded-perturbation semigroup, not self-adjoint functional calculus. Gauge equivariance passes coefficientwise.

Set Z_T(z,w)=nu(Q_T(z,w)1). The original nu is held fixed. Since Z_T(0,0)=1 and

\[
Tq\le1/4\quad\Longrightarrow\quad
|Z_T(z,w)-1|\le e^{Tq}-1\le1/3,
\]

the convergent power series for log(1+(Z-1)) defines the unique local logarithm with value0 at the origin. At T=0 the germ is identically0. No nonvanishing claim is made outside this neighborhood.

Both ordered insertions are retained. Stationarity of the unperturbed state removes endpoint propagators, and differentiation gives

\[
Z_z(0,0)=-T\nu(V),\qquad Z_w(0,0)=-T\nu(W),
\]
\[
Z_{zw}(0,0)=\int_{0<s<t<T}
\nu\big(VP_{t-s}W+WP_{t-s}V\big)\,ds\,dt.
\]

Reversibility identifies the two pairings, not the operators inside the integrand. Therefore the mixed connected response is

\[
\chi_T(V,W):=\partial_z\partial_w\log Z_T(0,0)
=2\int_0^T(T-u)\operatorname{Cov}_\nu(V,P_uW)\,du.
\]

Adding a constant to either probe multiplies Z by an exponential linear in amplitudes, so it leaves chi unchanged. In particular a constant probe has zero mixed response.

## Finite falsifiers

For V=1,W=2,T=1, Z=exp(-z-2w). Its raw mixed derivative is2; log Z has mixed derivative0. Centering is indispensable.

The reversible binary heat-bath control has stationary law [[9,8],[8,9]]/34 and updates each coordinate at rate1 to its conditional law. For V=x and W=y, eta=1/17 and Cov(V,W)=eta/4=1/68. The coefficient of T^2 in chi is1/68. One insertion order gives1/136 instead, leaving defect1/136. Exact bivariate matrix jets below retain the noncommuting generator between the two multiplication operators.

A separate logical hostile is Z_N(z,w)=1+sin(N^2 z)sin(N^2 w)/N for N>=2. It is positive on real amplitudes, normalized at zero and within1/N of1 on the real plane, but its mixed log derivative at zero is N^3. At N=16 these are1/16 and4096. This is not a source generating function: it rejects derivative control from a real absolute bound alone. The source Dyson construction supplies the missing uniform complex-amplitude control.

## Off-diagonal gradient transport, not subtraction of upper bounds

Use a finite source box Gamma containing K and L. The existing symmetric nonnegative Hessian majorant h^Gamma has weighted row and column bounds3R, and the gradient propagator majorant is B_u=exp(-kappa*u/2)exp(kappa*u*h^Gamma).

Let F_i=||gradient_i V|| and H_i=||gradient_i W||. Disjoint supports give F^T I H=0. Consequently

\[
F^TB_uH=e^{-\kappa u/2}F^T(e^{\kappa u h^\Gamma}-I)H
\le a^{-\ell}M(V)M(W)
\big(e^{-mu}-e^{-\kappa u/2}\big).
\]

The bound uses the nonnegative power series after removing its identity term; its weighted row sum is at most exp(3kappa R u)-1. It is not obtained by subtracting two separate scalar inequalities.

Insert this in the source packet's exact finite-box covariance identity and integrate its auxiliary gradient parameter. The result, passed to the actual thermodynamic scalar pairing by the established propagator/state comparison, is

\[
|\operatorname{Cov}_\nu(V,P_uW)|
\le a^{-\ell}M(V)M(W)g_R(u),\qquad
 g_R(u)=c^{-1}e^{-mu}-2e^{-\kappa u/2}.
\]

Here g_R is nonnegative and nonincreasing: its derivative is kappa(exp(-kappa*u/2)-exp(-m*u))<=0. At R=0 it vanishes identically. Passing uniform finite-box scalar bounds avoids postulating an infinite sum of limiting gradients.

## Completion of the response integral and rational budgets

Define J_b(T)=T/b-(1-exp(-bT))/b^2 for b>0. The covariance integral gives

\[
|\chi_T(V,W)|\le2a^{-\ell}M(V)M(W)
\big[c^{-1}J_m(T)-2J_{\kappa/2}(T)\big].
\]

The bracket is nonnegative because it is the integral of (T-u)g_R(u). Its elementary upper bounds give the fraction-only envelope

\[
|\chi_T(V,W)|\le a^{-\ell}M(V)M(W)H_R(\kappa,T),
\quad H_R=\min\left\{T^2(c^{-1}-2),\frac{2T}{\kappa}(c^{-2}-4)\right\}.
\]

These bounds are bilinear in the gradient budgets and exactly zero at R=0. Throughout the source window, replace the two coefficients by54/5 and7992/25 respectively to obtain a coupling-independent sufficient rule. For kappa=T=M(V)M(W)=1 and epsilon=1/1000, this rule requires separation33; R=9/128 requires26. These are minima of this sufficient estimate, not actual correlation lengths.

The source gap m also completes the response density on the centered Hilbert space:

\[
\mathcal S(V,W):=\lim_{T\to\infty}\frac{\chi_T(V,W)}T
=2\langle V_c,A_c^{-1}W_c\rangle.
\]

Here A_c is A restricted to the orthogonal complement of constants, where its inverse is bounded. The Bochner integral of P_u on that subspace equals A_c^(-1). Dominated integration using g_R proves, for disjoint supports,

\[
|\mathcal S(V,W)|\le\frac2\kappa(c^{-2}-4)a^{-\ell}M(V)M(W),
\]
\[
\left|\frac{\chi_T(V,W)}T-\mathcal S(V,W)\right|
\le\frac{2}{\kappa^2T}(c^{-3}-8)a^{-\ell}M(V)M(W),\quad T>0.
\]

For the remainder, bound its covariance integral by(2/T) integral_0^infinity u*g_R(u) du. Thus this is an explicit large-source-parameter completion at zero amplitude, not an exchange of amplitude differentiation with an unproved finite-amplitude asymptotic limit. The response matrix is positive semidefinite by spectral calculus of the nonnegative function integral_0^T (T-u)exp(-uA_c)du, but a cross entry has no asserted sign.

## Controls, scope and next constructor

The checker replays the probe-clustering receipt, compares16 bivariate heat-bath jets through source-parameter degree8 against the connected covariance formula, checks four exact centered resolvent responses, tests12 weighted matrix-resolvent gain packets and powers through degree12, and runs48 rational susceptibility planners. The weak-pair response density is17/288. These are finite analogues, not SU2 evaluations; the source promotion is the ordered Dyson/covariance/gradient argument above. Independent analytic review remains open.

Next executable issue: construct the isolated small-probe spectral branch and large-parameter logarithmic readout rate for norm-small real probes using the full source gap; prove finite-source/thermodynamic stability with the original state carriers. The zero-amplitude density here does not prove that finite-amplitude limit or justify exchanging its derivatives and limits. This remains an auxiliary source probe, not a new original magnetic vacuum, physical calibration or continuum/root discharge.

Contract: `research/kitaev/contracts/yang-mills-probe-susceptibility.v1.json`.
Checker: `research/kitaev/checkers/check_yang_mills_probe_susceptibility.py`.
Receipt: `research/kitaev/results/yang-mills-probe-susceptibility-v1.json`.
