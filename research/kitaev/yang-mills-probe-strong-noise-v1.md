# Strong marked-noise realization from a vector-valued Banach range argument

## Source and issue-boundary DPC

Iteration15/100 addresses `small-probe-strong-noise-realization:v1`. Retain the fixed-lattice source, radius-two SU2 geometry, kappa>0,0<=R<9/64,m=kappa*(1/2-3R), real smooth local gauge-invariant ||U||<=delta<=m/8, g=m-2delta, M_U=sum_i||D_i U||_infinity,L=M_U/m,H=exp(2pi L). The completed interaction has the certified absolute C2 tails; no third derivative is assumed. Iteration14 supplies the actual continuous field v=Dpsi,r=D log psi, psi in[H^-1,H],||r||<=L, its continuous one-form semigroup and the unique all-start-point weak martingale problem.

Fix orthonormal invariant Killing frames X_(ia),a=1,2,3, with [X_a,X_b]=epsilon_(abc)X_c. The MARKED SDE uses these frames and countably independent Brownian components:

\[
dX_i=\sqrt{2\kappa}\sum_a X_{ia}(X_i)\circ dW_{ia}
+\kappa[\beta_i(X)+2r_i(X)]dt.
\]

- **Problem:** a weak path law and continuous drift do not specify an adapted path map for given marked Brownian noise.
- **Conjecture:** the scalar reverse-Poincare estimate traces over vector output components without a volume factor. In invariant frames, the connection term is a relatively small FIRST-ORDER perturbation. A vector-valued full-range argument gives a continuous Hilbert-Schmidt derivative of r, and hence leafwise Lipschitz control and pathwise uniqueness.
- **Rivals:** hide the first-order connection in a bounded multiplier; introduce a sqrt(volume) factor in the traced estimate; differentiate the C2 Hessian multiplier and assume D3; apply an ell2 Gronwall estimate before proving solutions lie in the same ell2 leaf; infer common-noise transport from marginal laws.
- **Risky consequences:** uniform continuous second ground-vector derivatives, a source-independent-of-volume force Lipschitz bound, same-noise pathwise uniqueness, and strong solutions for every initial configuration. Actual finite-box common-noise map convergence remains a distinct comparison arrow.
- **Strongest falsifiers:** omission of the frame-curl term changes an actual free-SU2 gradient coefficient by256/65537; covariance-equivalent opposite noise markings change a source cross-bracket reader by2 at kappa=1/2. Neither finite control proves the strong solution theorem.
- **Disposition:** the vector-valued range and compatible conditional-law arguments below construct the strong marked-noise realization at written-proof scope. Independent analytic review remains open; no physical-clock, continuum or global-density extension is asserted.

## 1. Trace the scalar estimate, not the spatial volume

Let B=C(X;ell2(E;C3)) in the fixed frames, and let P_t^B act componentwise by the original scalar Feller semigroup. Its generator is -A_B. Finite-component smooth cylinder fields are an operator core: output projections commute with P_t^B, approximate both a domain element and its generator uniformly, and the scalar C(X) core handles each of the finitely many remaining components.

Write partial F for the FLAT matrix (X_(jb)F_(ia)) and use the Hilbert-Schmidt norm over BOTH index pairs. Summing the scalar reverse-Poincare inequality over finitely many output components gives

\[
\|\partial P_t^B F\|_{C(HS)}^2
\le\frac1{2\kappa t}\|F\|_B^2.
\]

Indeed the sum of variances is P_t|F|^2-|P_t F|^2, bounded by ||F||_B^2. There is no number-of-output-components factor. Output truncation, uniform cylinder approximation and closed fiber differentiation extend this to every F in B, with a continuous HS-valued derivative. Therefore

\[
\|\partial(\alpha+A_B)^{-1}\|_{B\to C(HS)}
\le d_\alpha:=\sqrt{\pi/(2\kappa\alpha)}.
\]

Continuity here is in the product configuration topology and HS norm. No bounded-Borel strong-Feller assertion or infinite-product manifold structure is needed.

## 2. Keep the first-order connection term

In these frames C_a z=(1/2)e_a cross z, sum_a C_a^2=-(1/2)I, and Ric=(1/2)I. The connection one-form generator of iteration14 is consequently

\[
\operatorname{gen}S=-A_B+J+Z_0,
\quad (JF)_i=2\kappa\sum_a C_aX_{ia}F_i,
\quad (Z_0F)_i=\kappa C(\beta_i)F_i-\kappa F_i.
\]

The -kappa term includes BOTH the connection-square and Ricci terms. Pointwise Cauchy-Schwarz gives ||JF||_B<=sqrt(3)*kappa*||partial F||_(C(HS)). The source bound ||beta_i||<=2R gives ||Z_0||<=kappa*(1+R). With M=kappa*Hess V interpreted as the strong multiplier already constructed, define

\[
G=\operatorname{gen}(e^{tE}H_{U,t})=-A_B+J+Z,
\quad Z=Z_0+M-U+E,
\quad \|Z\|\le b:=\kappa(1+4R)+2\delta.
\]

All finite sources have the same bounds. M is used only as a bounded multiplier on B; it is NEVER differentiated. In particular no third interaction derivative or global Hessian operator-norm convergence enters.

## 3. A second genuine Banach full-range identification

Put x=b/kappa, alpha=64kappa*(1+x)^2. The resolvent estimates give

\[
\|(J+Z)(\alpha+A_B)^{-1}\|
\le\sqrt{3\pi\kappa/(2\alpha)}+b/\alpha
\le\frac5{16(1+x)}+\frac{x}{64(1+x)^2}
\le\frac{81}{256}<\frac12.
\]

We used pi<4,sqrt(6)<5/2 and x/(1+x)^2<=1/4. Also J is infinitesimally A_B-bounded. Thus -A_B+J+Z on Dom(A_B) is closed, has the finite-component smooth cylinder core and has full alpha-resolvent range.

The actual semigroup e^(tE)H_(U,t), of norm<=exp(-g*t), extends this core operator: pass the finite-source generator integral identity on each localized smooth field through the strong one-form convergence. Full range and injectivity of alpha minus the actual generator exclude any larger extension. Hence the ACTUAL G has domain Dom(A_B). This is another range argument, not a formal differentiation of a rough matrix potential.

## 4. Continuous second derivatives and an explicit uniform force bound

The previous differentiated eigen-equation says Gv=psi DU, with v=Dpsi and ||v||_B<=HL. Thus v belongs to Dom(A_B), and partial v belongs to C(X;HS). The large-resolvent identity

v=(alpha-G)^-1*(alpha*v-psi*DU)

and the Neumann bound show

\[
\|\partial v\|\le D_*:=
\frac{H(\alpha L+M_U)}{2\kappa(1+x)}.
\]

This deliberately coarse rational-coefficient envelope follows from d_alpha/(1-q)<2sqrt(2/(kappa*alpha))<=1/[2kappa(1+x)]. Derivatives are obtained by the closed flat-gradient operator, not assumed in writing the eigen-equation.

Since r=v/psi,

partial r=psi^-1*partial v-r tensor r.

The conversion to covariant differentiation adds the block connection map C(r), whose HS norm is ||r||/sqrt(2). Therefore

\[
\nabla r\in C(X;HS),\qquad
\|\nabla r\|\le B_*:=H D_*+L^2+L.
\]

This proves coordinate C1 drift (and coordinate C2 psi), not arbitrary higher smoothness. For configurations at finite product geodesic ell2 distance, integrate along finite-coordinate geodesics and then use r in C(X;ell2) to obtain

\[
\|r(y)-\operatorname{PT}r(z)\|_{\ell^2}
\le B_* d_2(y,z).
\]

The estimate holds with any chosen minimizing coordinate geodesics. No ell2 distance is assigned to arbitrary pairs in different leaves.

The same argument is uniform in the actual finite sources. In fact partial v_j->partial v in C(HS): the traced scalar resolvents and their derivatives converge strongly, first on finite-output cylinder fields using iteration14 and then on B by their uniform bounds. Z_j converges strongly and J times the scalar resolvents does as well. The uniformly convergent Neumann inverses then act on alpha*v_j-psi_j DU, which converges in B. Thus covariant derivatives of r_j also recover in C(HS). This is common continuous-field recovery, not copying coordinates between vacuum Hilbert measures.

## 5. Prove same-leaf membership before Gronwall

Consider two solutions with the SAME marked Brownian motions and the SAME initial configuration. Factor out the common link stochastic isometries as in iteration14. Let D_i(t) be coordinate geodesic distances between the resulting random ordinary trajectories. Each D_i<=2pi. Positive first variation gives, initially without any ell2 claim,

D_i(t)<=kappa*integral_0^t sum_j h_ij D_j(s)ds
+2kappa*integral_0^t (|r_i(Y_s)|+|r_i(Z_s)|)ds.

Iterate this Volterra inequality. The remaining unknown-distance term is bounded by2pi*(3kappa*R*t)^n/n!, which tends to0 on every finite interval by the ROW bound. The forcing is ell2 with norm<=2L, and the row/COLUMN bounds make h bounded on ell2. Hence

\[
D(t)\in\ell^2,\qquad
\|D(t)\|_2\le4\kappa L\int_0^t e^{3\kappa R(t-s)}ds.
\]

The continuous ell2-valued forcing also gives uniform ell2 tails on bounded intervals; this justifies summing the distance-energy inequalities. Now, and only now, use the leaf Lipschitz estimate:

\[
\tfrac12\frac{d^+}{dt}\|D(t)\|_2^2
\le\kappa(3R+2B_*)\|D(t)\|_2^2.
\]

Gronwall gives D=0. The same argument for finite initial d2 gives same-noise stability d2(X_t^y,X_t^z)<=exp[kappa*(3R+2B_*)t]*d2(y,z). Ricci does NOT give synchronous exponential contraction: the Killing noise is isometric and the original positive drift majorant is3R, not -m.

This proves pathwise uniqueness for every initial configuration on every finite horizon. The argument uses bounded coordinate distances and the factorial remainder to rule out an unobserved entrance from infinity.

## 6. Compatible weak solutions yield an adapted strong path map

Iteration14 supplies weak solutions for every initial law. Smooth invariant coframes recover their driving martingales; the prescribed brackets give countably independent normalized Brownian components by the finite-dimensional Levy characterization, and the drift and covariance identify the marked Stratonovich SDE above.

For completeness the weak-to-strong implication is a COMPATIBLE conditional-law argument on Polish spaces, not uniqueness in law alone. Disintegrate a weak joint law given its initial state and Brownian path. Adaptedness and independent future Brownian increments imply that conditional laws of past solution segments depend only on past noise. Two conditionally independent copies given the same noise are consequently still solutions with that noise Brownian in their common filtration. Pathwise uniqueness makes them equal; the conditional law is Dirac. Its atom is an adapted measurable path map F(x,W).

The measurable weak-solution kernel permits jointly measurable representatives in (x,W). The theorem is for every initial distribution, including each deterministic x. Null sets may depend on x: no single exceptional Wiener set valid simultaneously for every uncountably indexed initial configuration, perfect stochastic flow, or full-product pathwise continuity is claimed. The map's law is the actual tilted Feller/path law by the established weak uniqueness. Constants have L=B_*=0 and recover the original strong dynamics.

## 7. Actual controls and remaining coupled comparison

For the free four-link character z, |Dz|^2=4-z^2 and

|Hess z|_HS^2=6+(3/2)z^2,
Hess z(Dz,Dz)=-z*(4-z^2).

The latter identities follow directly from Bochner, Ric=1/2 and Delta z=-3z. For raw psi=1+epsilon*z, c=epsilon/(1+epsilon*z),

\[
|\operatorname{Hess}\log\psi|_{HS}^2
=c^2(6+3z^2/2)+2c^3z(4-z^2)+c^4(4-z^2)^2.
\]

Its square root is bounded by4epsilon/(1-2epsilon)+4epsilon^2/(1-2epsilon)^2. This is an actual admissible gauge-invariant SU2 probe family, with epsilon=t/(1+t^2),t=1/(256n), not a Euclidean substitute.

For an exact gradient, X_aX_b f=Hess_(ab)f+(1/2)epsilon_(abd)X_d f, so J(Df)=kappa*Df. At R=0 this cancels Z_0=-kappa. Omitting J changes the actual differentiated plaquette coefficient by kappa*epsilon, equal to256/65537 at kappa=1,n=1.

The checker replays iteration14 and preregisters90 actual free-SU2 Hessian packets,72 vector Banach envelopes,81 frame-jet packets,54 factorial-tail certificates and3 marked-noise orientation controls. For the last control, at the group identity f=2q_1 has X_1 f=1. Noise markings +sigma and -sigma have the same generator (kappa=sigma^2/2) but opposite instantaneous cross bracket with W_1. At kappa=1/2 the defect is2. This refutes inference of the marked joint arrow from marginal path laws. Finite packets do not certify the infinite-source range theorem, pathwise uniqueness or conditional-law construction.

NEXT: transport actual finite-box STRONG MAPS jointly with the SAME marked Wiener input to the infinite-source map on fixed horizons, rather than asserting that marginal weak convergence supplies it. The newly proved pathwise uniqueness licenses a joint-noise/paired-solution limit and diagonal argument. Verify the cross-bracket readers and any use of a Gyongy-Krylov/conditional argument. A global ell2 norm of beta_j-beta is generally unavailable, since the original drift changes outside every box; local product-path comparison must respect this. Quantitative bounds may be added only where supported. This is the remaining source-compatible coupled-map arrow, now executable, not a request to wait for review.

The nonconstant infinite-horizon density extension remains a closed obstruction. Strong solutions driven by a common noise do not require equivalence of their infinite observation laws. Independent analytic review, physical calibration and continuum/root gates remain separate.

Contract: `research/kitaev/contracts/yang-mills-probe-strong-noise.v1.json`.
Checker: `research/kitaev/checkers/check_yang_mills_probe_strong_noise.py`.
Receipt: `research/kitaev/results/yang-mills-probe-strong-noise-v1.json`.
