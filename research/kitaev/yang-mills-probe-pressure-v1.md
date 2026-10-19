# Small-probe spectral branch and source logarithmic rate

## Question, source and stratum

Does the actual source gap construct a finite-amplitude logarithmic probe rate, uniformly enough to compare finite and thermodynamic sources, rather than merely a zero-amplitude susceptibility?

SCC obligation: based isolated-spectral realization, large-source-parameter readout completion and changing-state scalar transport. Retain kappa>0, 0<=r<27/262144, R=4096r/3, c=1/2-3R, m=kappa*c, a=4/3 and the prior rational comparison coefficient C_R=max(2R/c,44 eta_R/7)<=18/5. The coordinate T remains the Euclidean source semigroup parameter, without physical calibration.

Work separately in H=L2(nu) and H_Lambda=L2(nu_Lambda). Each actual unperturbed generator A has normalized vacuum vector1, simple eigenvalue0 and remaining spectrum in[m,infinity). The same statements hold for A_Lambda with this common m. No isometry between these Hilbert spaces is assumed.

Let U be a smooth real gauge-invariant local multiplication probe supported in fixed finite K, with ||U||_infinity<=delta<=m/8. Signed probes are allowed by a constant shift. Its units are inverse to the source parameter. Set B_U=A+M_U on Dom(A), and use the corresponding finite-source operator separately.

## Issue-boundary DPC

- **Problem:** fixed-parameter absolute readout convergence does not control logarithms as the readouts become small; the prior local Dyson logarithm neighborhood shrinks with T.
- **Conjecture:** a uniform isolated spectral projection and its original-vacuum overlap control supply a common logarithmic-rate completion. Spatial transport must be performed through positive readouts with these bases retained.
- **Named rivals:** lowest eigenvalue without reader overlap; absolute scalar comparison alone; unproved exchange of parameter and volume limits; importing unitary coordinates between original states; identifying eigenstates from identical scalar rates.
- **Risky consequences:** projection distance<=1/3, original-vacuum weight>=8/9, relative gap>=3m/4, a uniform1/T logarithmic-rate error, and a quantitative finite-source energy comparison.
- **Strongest falsification:** two-atom spectral readouts converge uniformly absolutely while their two logarithmic-rate limits differ by1 when ground weight vanishes. A norm-small two-state multiplication example has equal energies and overlaps but local ground-state readout difference32/257.
- **Disposition:** the written spectral and scalar arguments below construct the auxiliary probe rate and its transport. Finite controls do not independently verify source analysis. Tilted-state transport, physical calibration and continuum/root gates remain separate.

## Full spectral packet before readout

On the contour |zeta|=m/2 the original resolvent norm is at most2/m. For bounded complex multiplication U with delta=||U||<m/4, its Neumann resolvent and Riesz projection obey

\[
\Pi_U=\frac1{2\pi i}\oint_{|\zeta|=m/2}(\zeta-B_U)^{-1}\,d\zeta,
\qquad
\|\Pi_U-\Pi_0\|\le\rho:=\frac{2\delta}{m-2\delta}<1.
\]

The projection therefore has rank1 and is analytic in U on this norm ball. Its image lies in Dom(A). The eigenvalue branch is canonical because

\[
E(U)=\frac{\langle1,M_U\Pi_U1\rangle}{\langle1,\Pi_U1\rangle},
\qquad |\langle1,\Pi_U1\rangle-1|\le\rho<1.
\]

The A term vanishes in this quotient since A1=0. The spectral-inclusion Neumann argument puts the branch within distance delta of0, so |E(U)|<=delta even for the complex analytic extension. Gauge invariance of U makes the projection commute with the source gauge action; Pi_U1 is invariant. This is a projection in the existing vacuum Hilbert space, not an infinite Haar wavefunctional or a replacement original magnetic vacuum.

For real U in the working closed ball delta<=m/8, B_U is self-adjoint and Pi_U is orthogonal. The remaining spectrum is at least m-delta; E(U) is the unique lowest eigenvalue, with relative gap at least m-2delta>=3m/4. Its weight in the ORIGINAL preparation is

\[
\alpha_U=\langle1,\Pi_U1\rangle=\|\Pi_U1\|^2
\ge1-\rho^2\ge8/9.
\]

All estimates hold separately, with the same constants, for every finite source containing K. The spectral projection, eigenvalue, weight and complement are retained together.

## Finite falsifiers

A two-atom spectral readout with energies0,1 and weights epsilon_n=4^(-n),1-epsilon_n has Z_n(T)=epsilon_n+(1-epsilon_n)exp(-T). It differs from exp(-T) by at most epsilon_n for every T>=0. Each finite n nevertheless has logarithmic rate0; taking n to infinity first gives rate1. This gap1 example violates the uniform overlap bound. It rejects absolute scalar convergence as a substitute for that bound; it is not a source model in the admitted small-probe class.

For a norm-small multiplication control use the uniform two-state source A=[[1,-1],[-1,1]]/2. Put q=1/16, d=2q/(1-q^2), and U_plus=diag(d/2,-d/2), U_minus=-U_plus. Both have norm<1/8, equal lowest energy and equal original-state overlap1/(1+q^2). Their normalized ground-state expectations of diag(1,0) differ by2q/(1+q^2)=32/257. Scalar rates and overlaps alone do not transport local eigenstate readouts.

## Complete the real logarithmic rate

Define Z_U(T)=nu(exp(-T B_U)1)=<1,exp(-T B_U)1>. The positive spectral measure gives

\[
Z_U(T)=\alpha_Ue^{-TE(U)}+r_U(T),\qquad
0\le r_U(T)\le(1-\alpha_U)e^{-(m-\delta)T}.
\]

Consequently alpha_U<=exp(TE(U))Z_U(T)<=1. With L=log(9/8)<=1/8,

\[
p_T(U):=-T^{-1}\log Z_U(T),\qquad
0\le p_T(U)-E(U)\le L/T.
\]

Thus the real logarithmic rate exists and equals E(U), uniformly over the declared norm ball and over finite source sizes. The relative complement is suppressed at least by exp(-3mT/4), but the rate estimator generally has a1/T term from log alpha_U. No division of the original state by Z_U is performed.

For signed U, put V=U+delta>=0. The prior positive probe construction gives Q_U=e^(delta T)Q_V and exp(-delta T)<=Z_U(T)<=exp(delta T). This supplies a controlled positive interval for comparing logarithms, rather than assuming that absolute errors are relative errors.

## Transport to the thermodynamic branch

For b=d(K,Lambda complement), the preceding actual probe comparison applied to V yields

\[
|Z_{\Lambda,U}(T)-Z_U(T)|
\le C_R T M(U)e^{\delta T}a^{-b},
\qquad
|p_{\Lambda,T}(U)-p_T(U)|
\le C_R M(U)e^{2\delta T}a^{-b}.
\]

The factor exp(2delta T) records both the shift and the inverse lower readout bound. It cannot be silently discarded. Both one-sided rate-estimator errors belong to[0,L/T], so their difference costs only L/T. Therefore

\[
|E_\Lambda(U)-E(U)|
\le L/T+C_R M(U)e^{2\delta T}a^{-b}.
\]

Choosing a fixed T, passing the actual state/semigroup comparison, and then sending T to infinity proves E_Lambda->E along every spatial exhaustion. This argument never identifies nu_Lambda with a marginal of nu.

There is also a fraction-only diagonal budget. For delta>0 choose integer n>=1, b>=3n and T=n/(8delta). Since exp(1/4)<=4/3,

\[
|E_\Lambda(U)-E(U)|\le\delta/n+C_R M(U)(3/4)^{2n}.
\]

If delta=0 or C_R M(U)=0 the spatial energy discrepancy is exactly0 by the all-T comparison. Otherwise the least n meeting a chosen tolerance is a sufficient-budget planner. With kappa=1, delta=1/128, M(U)<=1 and tolerance1/1000, the whole-window rule gives buffer48; R=9/128 gives39. These are minima of this diagonal sufficient rule, not optimal volume errors.

## Analytic sewing and the previous susceptibility

For any fixed finite amplitude family U(z)=sum_j z_j V_j on a fixed finite union of supports, the branches are holomorphic on sum_j |z_j| ||V_j||<m/4 and uniformly bounded there by the perturbation norm. On the smaller domain with this sum<m/8, real-parameter energy convergence follows from the preceding estimate. Montel compactness and uniqueness of a holomorphic function on a real open set imply locally uniform complex convergence of the finite-source branches; Cauchy then transports every fixed finite-order derivative. The uniform complex spectral bound, not a real absolute-error inequality alone, licenses this step. No dimension-uniform claim for an infinite amplitude family is made.

Normalize the analytic eigenvector by <1,psi_U>=1. At zero, psi'_V=-A_c^(-1)V_c. Differentiating the eigenvalue equation gives

\[
E'_V(0)=\nu(V),\qquad
E''_{V,W}(0)=-2\langle V_c,A_c^{-1}W_c\rangle
=-\mathcal S(V,W).
\]

This identifies the prior response density by a separate spectral calculation. It does not presume an exchange of amplitude differentiation with the large-T logarithm. No global complex logarithm of the finite-T generating function is asserted.

## Checks and remaining constructor

The fraction-only checker freshly replays the susceptibility receipt; tests12 contour/overlap budgets,36 exact norm-small two-state spectral packets,12 mixed eigenvalue-equation jets,96 spatial-pressure budgets and the two falsifiers. The finite packets are not SU2 spectral evaluations. Their role is to reject missing overlap, sign, normalization or scalar-identification steps; the source proof uses the full-domain gap and the written analytic comparison.

Next executable issue: construct a base-preserving finite-source comparison of the normalized small-probe eigenstate and its local observable readouts, using positive semigroup filtering and the uniform relative gap. The projections here live in different original Hilbert spaces; pressure convergence alone does not compare their vectors or tilted local states. Keep any auxiliary tilted state distinct from the original magnetic vacuum. Independent analytic review, physical calibration and continuum/root gates remain open.

Contract: `research/kitaev/contracts/yang-mills-probe-pressure.v1.json`.
Checker: `research/kitaev/checkers/check_yang_mills_probe_pressure.py`.
Receipt: `research/kitaev/results/yang-mills-probe-pressure-v1.json`.
