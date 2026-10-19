# Stationary tilted source diffusion and continuous-path transport

## Source and issue-boundary DPC

Iteration11/100 addresses `small-probe-diffusion-path-transport:v1`. Keep X=SU(2)^E with the radius-two link metric, kappa>0,0<=R<9/64,m=kappa*(1/2-3R), and fixed real smooth local gauge-invariant U with ||U||<=delta<=m/8. Let rho_j=psi_j^2 nu_j and rho=psi^2 nu be the actual tilted source states. Write T_j,T for the positive L2 generators and P_j(t),P(t) for their conservative Feller semigroups. Throughout, t is the source semigroup parameter, not calibrated physical time.

The preceding packets supply the closed forms q_U(f,g)=kappa*rho(D conjugate(f) dot Dg), cylinder form AND operator cores, full-support rho, and based strong drift transport. Put L=M_U/m, r_j=D log psi_j and r=D log psi; ||r_j||_(L-infinity;ell2),||r||_(L-infinity;ell2)<=L. The weak Markov generator is

\[
\mathcal L=-T=\kappa\sum_i[\Delta_i+(\beta_i+2r_i)\cdot\nabla_i],
\]

on the cylinder L2 core; coefficients involving r need only be measurable. The finite sources use the actual exterior-Haar/Brownian extension on the SAME product X.

- **Problem:** finite-time insertion words do not imply tightness on continuous path space, and weak measurable drifts cannot be transported by pointwise evaluation.
- **Conjecture:** regular strongly local forms realize the stationary diffusions; uniform coordinate fourth moments yield path tightness. Stationary L2 approximation then transports the actual drift integrals, martingales and brackets.
- **Rivals:** finite-dimensional distributions alone determine convergence on C-path space; weak L2 fields alone control their stationary additive functionals; drop the source bracket factor2kappa; assert all-start-point drift identities from a stationary L2 version.
- **Risky consequences:** canonical stationary continuous-path laws, weak convergence on C([0,S],X), joint finite-family drift/martingale/bracket transport, reversibility and gauge equivariance, all in actual source units.
- **Strongest falsifiers:** randomly shifted thin periodic pulses have collapsing finite-dimensional distributions but sup norm1 and fourth-moment ratio3n/5; frozen stationary cosine fields are weakly null but retain additive-functional squared error1/2; a half-sized bracket misses1 at kappa=1 in a unit tangent direction.
- **Disposition:** the written form, tightness and stationary approximation arguments below supply the stated laws and transport. Finite controls are not SU2 path simulation or independent analytic verification. No all-start-point martingale, strong SDE uniqueness, physical clock or continuum theorem is inferred.

## Realization: check the diffusion theorem hypotheses

X is a compact metrizable countable product. Smooth cylinders form a uniformly dense, point-separating real algebra in C(X) and are a form core. Closed scalar contraction/chain rules make the weighted gradient closure a Dirichlet form. Its gradient derivation is local; the cylinder preform is strongly local, and its regular closure is strongly local. Thus this is a REGULAR strongly local Dirichlet form on the full-support probability space (X,rho), not merely an arbitrary self-adjoint operator. The same applies in every extended finite source.

Use the standard regular strongly-local Dirichlet-form diffusion theorem and its generator-domain martingale theorem. These analytic imports give a continuous-path Hunt realization outside a properly exceptional set. Conservativeness follows from P(t)1=1. Starting in rho avoids the exceptional set and yields a stationary continuous-path law, denoted mathbb P_U; symmetry gives reversibility. Its finite-dimensional distributions are those of the already identified Feller semigroup, not a newly chosen extension. The same construction gives mathbb P_(j,U). No appeal to a smooth infinite-product density or a singular gauge quotient is made.

For a real smooth cylinder f, the established generator expression gives a bounded L2 representative mathcal L f. In particular, with

\[
C_f=\kappa\sum_i\|\Delta_i f\|_\infty+
\kappa(4R+2L)\sum_i\|\nabla_i f\|_\infty,
\]

we have ||mathcal L_j f||_infinity,||mathcal L f||_infinity<=C_f. The original component bounds |beta_ia|<=2R imply block norm<=2sqrt(3)R<=4R. Stationarity makes time integrals independent of rho-null choices of these representatives. Generator-domain martingales are

\[
M_t^f=f(X_t)-f(X_0)-\int_0^t\mathcal L f(X_s)\,ds.
\]

They are continuous true martingales on every finite interval: their absolute values are at most2||f||_infinity+S*C_f. Apply the martingale theorem also to products fg, which remain in the cylinder operator core. The gradient product rule cancels the entire drift and gives

\[
\langle M^f,M^g\rangle_t
=2\kappa\int_0^t Df\cdot Dg(X_s)\,ds.
\]

These statements hold for the finite sources as well. They are stationary-law assertions; no rho-null derivative representative is declared valid at every deterministic starting point.

## Uniform source geometry and increment bound

Identify one link with the round sphere S3 of radius2 in R4. Its four embedding coordinates y_alpha satisfy

\[
|y_\alpha|\le2,\quad
\Delta y_\alpha=-\tfrac34 y_\alpha,\quad
\nabla y_\alpha\cdot\nabla y_\gamma
=\delta_{\alpha\gamma}-y_\alpha y_\gamma/4.
\]

Thus for each link, each coordinate and every source, the drift is bounded by

\[
B=\kappa(3/2+4R+2L),
\]

and its martingale bracket density is at most Q=2kappa. If h=t-s, Ito's fourth-power identity and localization give E|M_t-M_s|^4<=3Q^2 h^2: the stopped second moments are at most Qh, and the fourth-moment drift is6*M^2*d bracket. No Gaussian-increment independence is assumed. The finite-variation increment has absolute value<=Bh, so for0<=s,t<=S,

\[
\mathbb E|y_\alpha(X_t)-y_\alpha(X_s)|^4
\le 8B^4h^4+24Q^2h^2
\le(8B^4S^2+96\kappa^2)h^2.
\]

Stationarity ensures the a.e. coefficient bounds hold along paths for almost every integration parameter; this is sufficient for the estimate. The sum of four coordinate squares and d_SU2<=pi/2 times chord distance yield the rational link estimate

\[
\mathbb E\,d_{SU2}(X_i(t),X_i(s))^4
\le C_{\rm link}(S)h^2,\quad
C_{\rm link}(S)=16(11/7)^4(8B^4S^2+96\kappa^2).
\]

Here pi/2<11/7; all constants are independent of source volume and link index. This bound controls topology, not a physical energy/time calibration.

## Tightness is separate from finite-time words

The fourth-moment bound and compact link state space give tightness of every link-coordinate path law in C([0,S],SU(2)), by the Kolmogorov tightness criterion (any exponent below1/4 is available for modifications). Enumerate E and use d_X=sum_i2^-i*min(1,d_SU2). The space C([0,S],X) with uniform d_X topology is homeomorphic to the countable product of these coordinate path spaces: finitely many coordinates control the head and the metric tail is uniformly small.

For any tolerance choose a compact coordinate-path set with failure probability at most tolerance*2^-i for each link. Their countable product is compact and has total failure probability at most the tolerance. This proves joint path-space tightness. It does not assert a globally finite carrier or interchange volume and parameter limits without control.

For a fixed finite collection of parameters and continuous readouts, iterated semigroup composition and weak rho_j convergence give convergence of finite-time words. At each step, control the varying intermediate input by contraction BEFORE applying the fixed-input Feller theorem. Products of continuous readouts determine the joint marginal laws on compact X. Every tight subsequential path limit therefore has the canonical limiting finite-dimensional distributions. Rational evaluations generate the Borel sigma-field on continuous path space, so that limit is unique. Consequently

\[
\mathbb P_{j,U}|_{[0,S]}\Longrightarrow
\mathbb P_U|_{[0,S]}
\quad\text{on }C([0,S],X).
\]

The limiting law is stationary, reversible and gauge equivariant; these properties also follow directly from its actual form/kernel. Gauge acts on the prequotient product paths; no quotient smoothness is needed.

## Joint transport of measurable drift integrals

For a finite family of real cylinder functions, the previous packet proves strong based mathcal L_j f->mathcal L f in their actual L2(rho_j) spaces. Choose common continuous cylinder b_n approximating mathcal L f with

\[
\|\mathcal Lf-b_n\|_{\rho}\to0,
\qquad \lim_n\limsup_j\|\mathcal L_jf-b_n\|_{\rho_j}=0.
\]

With I_j^f(t)=integral_0^t mathcal L_j f(X_s)ds, stationarity and Cauchy-Schwarz give the decisive pathwise-reader estimate

\[
\mathbb E_{j,U}\sup_{t\le S}
\left|I_j^f(t)-\int_0^t b_n(X_s)ds\right|^2
\le S^2\|\mathcal L_jf-b_n\|_{\rho_j}^2.
\]

The analogous limiting estimate holds. For fixed n, integrating b_n is a continuous map from the path space to C([0,S],R), since X is compact and b_n is continuous. Path weak convergence followed by the two-stage L2 approximation therefore gives JOINT convergence of paths and every finite family of these additive drift functionals. No limiting measurable drift is evaluated in a different source's measure.

The martingale paths follow by subtraction of f(X_t)-f(X_0). The brackets are continuous path functionals already, because2kappa*Df dot Dg is a fixed continuous cylinder. The uniform bound2||f||_infinity+S*C_f gives uniform integrability for martingale and product tests. Passing bounded continuous past-cylinder tests through the joint limit and then using a monotone-class argument preserves the martingale and bracket identities in the natural stationary filtration. This also identifies the transported drift as the actual weak source drift rather than an unrelated continuous-path realization.

## Falsifiers and finite controls

A randomly shifted period-one triangular pulse of height1, support width2/n and slopes+/-n is stationary. Each fixed observation is nonzero with probability2/n, so every fixed finite-dimensional distribution tends to zero. Yet on[0,1] its supremum is1 almost surely. At h=1/n its fourth increment moment is3/(5n), hence its moment/h^2 ratio is3n/5, unbounded. This refutes finite-time-only path promotion; it is not an actual source diffusion obeying the preceding bounds.

For a frozen stationary uniform-circle path X_t=X_0 and fields b_n=cos(n theta), all fixed low-mode weak tests vanish eventually, but integral_0^1 b_n(X_s)ds has squared L2 norm1/2. Thus stationarity and weak field convergence alone do not prove the generic additive-functional comparison. This fixture is not the nondegenerate source process; the actual proof uses strong based L2 recovery.

The checker freshly replays the gradient-transport receipt and preregisters240 rational radius-two coordinate-jet identities,72 fourth-moment envelopes,18 stationary occupation/recovery packets,6 pulse packets and6 weak-field packets. The bracket factor hostile has defect1 at kappa=1; pulse sup defect1 and weak-field additive defect1/2 remain explicit. No finite packet independently verifies the Dirichlet-form diffusion theorem or source analytic chain.

Next executable issue: construct the finite-horizon path change-of-measure arrow from the ORIGINAL stationary source diffusion to this auxiliary tilted law. Derive the endpoint/action density with the actual original/tilted initial states, its martingale/Girsanov interpretation and source entropy rate, and transport these densities through the thermodynamic comparison. The needed continuous paths, actual bounded positive multiplier and stationary weak-gradient martingales now exist. Do not assume an infinite-horizon density, use the auxiliary law as a replacement original magnetic vacuum, or treat an entropy rate as physical-clock calibration.

Contract: `research/kitaev/contracts/yang-mills-probe-diffusion-path.v1.json`.
Checker: `research/kitaev/checkers/check_yang_mills_probe_diffusion_path.py`.
Receipt: `research/kitaev/results/yang-mills-probe-diffusion-path-v1.json`.
