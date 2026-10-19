# Continuous ground-vector gradients and the actual Feller cylinder core

## Source and issue-boundary DPC

Iteration14/100 addresses `small-probe-pointwise-generator-core:v1`. Retain X=SU(2)^E with radius-two link geometry, kappa>0,0<=R<9/64,m=kappa*(1/2-3R), and real smooth local gauge-invariant U with ||U||<=delta<=m/8. Put g=m-2delta>0. Existing packets give the actual original/tilted Feller semigroups, uniform psi_j->psi,E_j->E, H^-1<=psi_j,psi<=H, and weighted block log-Lipschitz sum<=L=M_U/m, with a=4/3 and H=exp(2pi L). The completed interaction is C2 in the certified summable sense; higher derivatives are NOT assumed.

Use the common continuous one-form space B=C(X;ell2(E;C3)) in fixed invariant link frames, with norm sup_x |v(x)|_ell2. Frames identify comparison carriers, not Hilbert measures. The following construction is on this Banach space before using changed-state L2 arguments.

- **Problem:** based L2 gradients, continuous eigenvectors and full support do not supply pointwise drift or a C(X) cylinder generator core.
- **Conjecture:** continuous connection transport plus the bounded Hessian multiplier realize the one-form semigroup directly. Its coercive resolvent transports actual ground-vector derivatives uniformly. Reverse Poincare then gives a Banach resolvent-range argument.
- **Rivals:** assume global operator-norm convergence of the infinite Hessian matrices; infer C1 from uniform values and bounded Lipschitz constants; drop Ricci from the differentiated eigen-equation; reuse Hilbert resolvent constants on C(X); call a finite C2-coefficient elliptic resolvent smooth without approximation.
- **Risky consequences:** uniform one-form gradient recovery, continuous logarithmic drift, Dom(T_C)=Dom(A_C), a smooth cylinder C(X) operator core, and cylinder martingale drift for every deterministic initial configuration.
- **Strongest falsifiers:** an actual free-SU2 plaquette loses coefficient128/65537 if Ricci is omitted; a C1 Huber family has value error1/(2n) but gradient Cauchy defect1/2; finite-coordinate projections converge strongly but retain operator-norm defect1.
- **Disposition:** the direct continuous-field and full-range arguments below fill this cell at written-proof scope. Finite regressions do not mechanically certify the stochastic transport, infinite-dimensional limits or analytic imports. Independent analytic review remains open.

## 1. Original paths and connection transport, without third derivatives

Let beta_j=gradient V_j for the actual retained finite interaction. The previous positive symmetric majorant h has weighted rows AND columns<=3R and dominates covariant Hess(V_j). Also ||beta_(Gamma,i)-beta_(Lambda,i)||<=2R*a^-d(i,Lambda^c) in Lambda, and the same global estimate holds with distance0 outside Lambda after exterior Brownian extension.

Couple all finite original diffusions with the same link Brownian motions. Brownian motion can be realized by independent invariant Killing fields on each bi-invariant SU2 factor. Factoring out their stochastic isometries leaves random time-dependent ordinary equations. First variation of product geodesic distance, using the covariant Hessian block bound, gives the positive comparison system for equal initial configurations

D_i(t)<=kappa*integral_0^t[sum_j h_ij D_j(s)+epsilon_i]ds.

Here epsilon_i is the preceding drift discrepancy. The weighted row bound gives, for i in a fixed finite K and t<=T,

\[
\sup_x d_i(X_t^{\Gamma,x},X_t^{\Lambda,x})
\le\tfrac23(e^{3\kappa RT}-1)a^{-d(K,\Lambda^c)}.
\]

This is a synchronous path bound; at cut loci use upper Dini derivatives/minimizing geodesics. The isometry factorization eliminates extra noise-distance terms. It proves local path convergence uniformly in the initial configuration, also for nonnested exhaustions by a common larger box. It constructs the actual original paths, since their finite-word semigroups are the already identified uniform limits.

Levi-Civita stochastic parallel transport on any FIXED link also converges in L2 on bounded intervals, uniformly in initial configuration. To see this, write it in the global smooth link frame: its noise coefficients are fixed smooth geometric matrices and its drift coefficients use beta_(j,i)(X^j), which converge locally by the distance comparison. The finite-dimensional BDG/Gronwall stability estimate applies. For a fixed link only its own geometric transport equation occurs; no dimension-dependent sum of connection coefficients is introduced. No derivative of Hess(V) is used here.

Define the connection semigroup S_t^j on B by expectation of inverse parallel transport of v(X_t^j), multiplied by exp(-kappa*t/2). Ricci=1/2 on every radius-two factor. It has norm<=exp(-kappa*t/2). On finite-component cylinder fields, the preceding convergence proves strong convergence in B uniformly on bounded intervals; component support does not spread under S^j. Such fields are dense in B (compactness of a continuous ell2-valued image gives uniform component tails). Contraction extends the limit to every v in B. The resulting S_t is strongly continuous; verify at0 first on the dense localized fields and then use contraction.

## 2. Hessian multiplication and the genuine one-form limit

Set M_j(x)=kappa*Hess V_j(x), interpreted in the covariant frame identification. Schur's row/column bound gives ||M_j(x)||_(ell2->ell2)<=3kappa R. Every fixed matrix entry converges uniformly by the certified absolute C2 tails. For a field supported on finitely many components, weighted COLUMN tails make M_j v Cauchy in B. Hence M_j->M strongly on B, with uniform operator bound3kappa R. M is a bounded multiplier on B.

This is NOT global operator-norm convergence of M_j to M, nor operator-norm continuity of x->M(x). Far-away coordinates can retain a nonzero Hessian. Strong continuity on localized vectors and uniform bounds are exactly what is needed.

Bounded perturbation/Dyson series now constructs

\[
H_t^j=\exp[t(\operatorname{gen}S^j+M_j)],\qquad
H_{U,t}^j=\exp[t(\operatorname{gen}S^j+M_j-U)].
\]

They converge strongly in B, uniformly on bounded intervals, to H_t,H_(U,t), with

\[
\|H_t^j\|,\|H_t\|\le e^{-mt},\qquad
\|H_{U,t}^j\|,\|H_{U,t}\|\le e^{-(m-\delta)t}.
\]

Termwise convergence of the Dyson series uses strong convergence on each fixed vector plus uniform bounds; moving vectors range over compact continuous-time images and are approximated by finite nets. Thus no varying-input or operator-norm convergence is silently assumed. Finite-dimensional differentiation gives D P_t^j f=H_t^j Df. Smooth retained harmonic truncations prove the identity first; C2 convergence and the same uniform bounds remove those truncations. Closure of fiber differentiation gives D P_t f=H_t Df for smooth cylinders.

## 3. Ground-vector derivatives by the one-form resolvent

The finite differentiated eigen-equation is

\[
(A_j^{(1)}+U-E_j)D\psi_j=-\psi_j DU,
\quad A_j^{(1)}=-\operatorname{gen}H^j.
\]

Because m-2delta=g>0, its continuous-field solution has the convergent representation

\[
D\psi_j=-\int_0^\infty e^{tE_j}H_{U,t}^j(\psi_j DU)dt.
\]

This also follows by differentiated finite-source filters. For C2 rather than smooth completed coefficients, pass smooth retained truncations through the bounded-interval identity and exponential integral tail. The forcing is bounded by H*M_U and the integrand by H*M_U*exp(-g*t), uniformly in j. Strong one-form transport, uniform psi_j and E_j convergence, and dominated Bochner integration therefore give

\[
D\psi_j\longrightarrow v=-\int_0^\infty e^{tE}H_{U,t}(\psi DU)dt
\quad\hbox{in }B.
\]

Uniform convergence of a function and its fiber derivatives identifies v=Dpsi by integration along one-link curves. Thus psi is coordinate C1 and Dpsi belongs to B. In particular

\[
r_j=D\log\psi_j\longrightarrow r=D\log\psi\quad\hbox{in }B,
\qquad r\in C(X;\ell^2),\quad\|r\|_B\le L.
\]

The old weighted block bounds still hold pointwise. Splitting into a finite neighborhood of K and its weighted tail also gives sum_i||r_(j,i)-r_i||_infinity->0 in the UNWEIGHTED block sum. Convergence in the full a-weighted norm is not claimed. This is a direct common continuous-field derivative construction, not evaluation of a merely measurable limiting gradient in another source state. The actual tilted drift beta+2r now has continuous link components at every configuration.

## 4. Original C(X) core and reverse Poincare smoothing

Write A_C for the nonnegative original Feller generator. The old propagator comparison's uniform resolvent-range sequence proves a C(X) core as well as an L2 core: for smooth cylinder f and lambda>3kappa R its finite resolvents u_j converge uniformly to (lambda+A_C)^-1 f and (lambda+A_C)u_j->f uniformly.

There is a regularity clarification: with only C2 completed V_j, u_j need not be C-infinity. Finite-dimensional elliptic regularity with C1 drift gives C2 regularity (indeed C^(2,alpha),alpha<1). Approximate u_j on its finite compact product in C2 by smooth functions. Since only finitely many bounded beta_i occur in A_C u_j, choose the smoothing error to make the additional uniform graph residual tend to0. The resulting SMOOTH CYLINDERS are graph-dense. This repairs any unnecessary finite smoothness shorthand without strengthening the source envelope.

For each finite extended system, Ric-Hess V_j>=c=1/2-3R gives the Bakry-Emery reverse Poincare estimate, with Gamma=kappa*|D|^2,

\[
\|D P_t^j f\|_B^2
\le\frac{m}{\kappa(e^{2mt}-1)}\|f\|_\infty^2
\le\frac1{2\kappa t}\|f\|_\infty^2.
\]

Pass it to P_t on cylinders using Section2, then to arbitrary f in C(X) by uniform approximation and closed fiber differentiation. This regularizes CONTINUOUS inputs into the continuous ell2 one-form topology; no strong-Feller assertion on arbitrary bounded Borel functions, or infinite-product smooth-manifold assertion, is made. Integrating the bound gives

\[
\|D(\alpha+A_C)^{-1}\|_{C\to B}
\le\sqrt{\pi/(2\kappa\alpha)}.
\]

## 5. Full Banach range identifies the tilted cylinder closure

On Dom(A_C) define Kf=-2kappa*r dot Df. The resolvent bound shows that Df is in B and Kf is continuous, with

\[
\|K(\alpha+A_C)^{-1}\|_{C\to C}
\le\sqrt{2\pi\kappa/\alpha}\,L.
\]

This tends to0 with alpha, so K is infinitesimally A_C-bounded. Hence S_C=A_C+K on Dom(A_C) is closed with equivalent graph norm, and smooth cylinders are its operator core. For alpha=8kappa*(1+4L^2), using pi<4, the squared Neumann bound is less than or equal to L^2/(1+4L^2)<1/4. Consequently alpha+S_C has full range C(X).

The actual tilted Feller generator T_C already agrees in L2 with T. For a cylinder f, the L2 identity Tf=A f-2kappa*r dot Df now has a continuous right-hand side. Resolvent consistency puts f in Dom(T_C): apply the Feller resolvent to (alpha+T)f, identify its L2 value with f, and use full support only to identify these TWO continuous representatives. Thus T_C extends S_C by closedness and its cylinder core. Full range of alpha+S_C and injectivity of alpha+T_C exclude a hidden extension, exactly as in the Hilbert argument but now with the BANACH estimate just proved. Therefore

\[
\operatorname{Dom}(T_C)=\operatorname{Dom}(A_C),\qquad
T_Cf=A_Cf-2\kappa r\cdot Df,
\]

and smooth cylinders are the actual C(X) generator core. The pre-existing Feller similarity also gives Dom(T_C)=psi^-1 Dom(A_C); therefore multiplication by psi and its inverse preserves this Feller domain. No wrong-measure symmetry or Hilbert resolvent norm is used. Gauge averaging gives the invariant core without orbit-space differentiability.

## 6. Every-start-point weak drift, not a strong tilted SDE theorem

The finite tilted link drifts beta_(j,i)+2r_(j,i) converge uniformly for each fixed i. They are uniformly bounded per link. Smooth coordinate embeddings SU2->R4 and finite-dimensional Ito/BDG estimates give fourth increment moments<=C_T*|t-s|^2, uniformly in the box and initial configuration. The uniform Feller semigroup convergence identifies finite words for any initial x; coordinate tightness and the summable product metric give their continuous-path limits P_U^x on every fixed horizon.

Cylinder generator values now converge uniformly. Hence their martingale identities, including cross brackets2kappa*Df dot Dg, pass to these paths for EVERY deterministic initial x, not just stationary-a.e. The C(X) operator core extends the identities to the full Feller domain and gives the usual martingale-problem uniqueness by resolvent/time-dependent semigroup tests. This establishes a canonical all-start-point weak drift realization. It does not prove pathwise uniqueness driven by the same Brownian motions or a strong tilted solution map. Continuous r alone is not silently promoted to Lipschitz r or classically smooth drift.

The iteration13 nonconstant infinite-horizon density obstruction remains closed and unchanged. No global change of probability measure was used in this construction.

## Actual controls and next missing constructor

For the actual R=0 four-link plaquette character x, A x=3kappa*x and |Dx|^2=4-x^2. Take raw psi=1+epsilon*x and U=-3kappa*epsilon*x/(1+epsilon*x). The pointwise differentiated identity reads

(3kappa+U)*epsilon=-(1+epsilon*x)*U'(x).

The normalized eigenvector has the same identity after multiplication by its constant normalizer. Removing kappa*Ricci changes the left coefficient by -kappa*epsilon/2. At kappa=1,t=1/256,epsilon=t/(1+t^2), its magnitude is128/65537; at x=0 the actual covector Dx is nonzero. This is a genuine SU2 source falsifier, not a circle replacement.

The checker freshly replays iteration13 and preregisters90 actual free-SU2 pointwise one-form packets,36 cooperative resolvent envelopes,18 Banach Neumann envelopes,6 Huber value/gradient topology controls and4 strong-versus-operator-norm projection controls. None mechanically verifies the infinite-dimensional transport or martingale-problem theorem.

Next executable cell: construct a common-noise STRONG tilted stochastic realization, or locate its exact regularity obstruction. The newly continuous all-configuration force and one-form semigroup now permit testing whether second-derivative/leafwise Lipschitz estimates follow from the existing C2 interaction control and bounded-multiplier regularization, without assuming third derivatives. A sufficient ell2-leaf Lipschitz bound on r, combined with the original majorant and localized ell2 forcing, would close synchronous pathwise uniqueness. Otherwise prove the precise missing estimate rather than infer strong well-posedness from weak martingale uniqueness. Physical calibration, independent analytic review and continuum/root gates remain separate.

Contract: `research/kitaev/contracts/yang-mills-probe-pointwise-core.v1.json`.
Checker: `research/kitaev/checkers/check_yang_mills_probe_pointwise_core.py`.
Receipt: `research/kitaev/results/yang-mills-probe-pointwise-core-v1.json`.
