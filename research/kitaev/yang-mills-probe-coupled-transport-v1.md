# Native finite-source strong maps converge on the same marked Wiener input

## Source, target and issue-boundary DPC

Iteration16/100 addresses `small-probe-coupled-source-transport:v1`. Retain the fixed spatial lattice, X=SU(2)^E, radius-two source geometry, kappa>0,0<=R<9/64,m=kappa*(1/2-3R), and a fixed real smooth local gauge-invariant ||U||<=delta<=m/8. No spacing trajectory or physical clock is introduced. The actual finite sources use the prescribed exterior-Haar/Brownian extension; their restrictions inside the box remain the native finite dynamics.

Throughout, j follows an arbitrary cofinal exhaustion; no almost-sure simultaneity across all exhaustions is asserted. The predecessor constructs adapted marked-noise strong maps F_j(x,W),F(x,W) and pathwise uniqueness, with fixed orthonormal invariant frames and countably independent Brownian components. Write b_j=kappa*(beta_j+2r_j),b=kappa*(beta+2r). Every fixed link component converges uniformly on X, and ||b_(j,i)||<=2kappa*(R+L). These are local continuous coefficient comparisons, NOT a globally ell2-small original drift difference.

Enumerate the links and use the bounded product metric rho(x,y)=sum_(n>=1)2^-n*|q_n(x)-q_n(y)|/2, where q_n is the unit-quaternion coordinate. Put d_T= sup_(t<=T) rho on continuous paths. Let W_T be the countable product of three-dimensional Wiener path spaces, not ell2-valued Brownian motion.

**Claim:** on one specified initial probability space take Xi_j->Xi in probability in X, with the ENTIRE initial family independent of W. Then, for every fixed T<infinity,

\[
F_j(\Xi_j,W)\longrightarrow F(\Xi,W)
\quad\hbox{in probability in }C([0,T],X).
\]

The source-state marginals of Xi_j,Xi are not changed or identified as Hilbert spaces. Fixed deterministic x_j->x is included.

- **Problem:** separate path-law convergence and strong realizations do not identify their joint comparison with a common marked noise or initial coupling.
- **Conjecture:** joint solution/noise characteristics survive native coefficient transport. The already constructed target solution and pathwise uniqueness force every paired limit to be diagonal.
- **Rivals:** omit mixed brackets; forget that W must be Brownian in the JOINT filtration; silently replace a given initial coupling; use a global ell2 beta_j-beta bound; interchange sup_x and expectation to claim a perfect flow.
- **Risky consequences:** same-noise convergence in probability, joint path/noise readers, uniform-in-initial mean convergence and native stationary initial-state couplings, without a numerical convergence rate or universal all-x Wiener null set.
- **Strongest falsifiers:** at R=0, a gauge-invariant plaquette with character0 has a mixed-generator defect2 for opposite noise markings at kappa=1/8. Antipodal Haar initial states have identical marginals but path distance at least1/2 under the same noise. A finite scope fixture has E sup minus sup E equal7/8.
- **Disposition:** the native marked-noise comparison is constructed below at written-proof scope. Finite controls do not mechanically certify tightness, martingale-limit closure or pathwise uniqueness. Independent analytic review remains open. This closes the remaining declared fixed-lattice construction arrow; no new executable successor is needed in the retained source envelope.

## 1. Uniform tightness with the initial coupling retained

Set Y_j=F_j(Xi_j,W) and Y=F(Xi,W), all on the stated product probability space. For smooth single-link quaternion coordinate functions, bounded drifts and the fixed smooth diffusion fields give by Ito/BDG

E|q_i(Y_j(t))-q_i(Y_j(s))|^4<=C_(kappa,R,L,T)*|t-s|^2.

The constant is independent of box, link and initial configuration; the same bound holds for Y. Minkowski and the summable metric weights imply E rho(Y_j(t),Y_j(s))^4<=C*|t-s|^2. Compactness of X and the metric Kolmogorov tightness criterion therefore give tightness in C([0,T],X). The fixed Wiener law is tight in W_T. Thus (Y_j,Y,W,Xi_j,Xi) is jointly tight. No ell2 norm of W or global drift difference is used.

Since Xi_j->Xi in probability, every weak joint subsequential limit has its two initial states equal. Future noise increments are independent of the whole initial family. This property must not be replaced by merely specifying each initial marginal.

## 2. The full joint martingale contract

For a real smooth cylinder f define L_j f=kappa*sum(Delta_i f+(beta_(j,i)+2r_(j,i))*D_i f), and M_j^f=f(Y_j(t))-f(Xi_j)-integral_0^t L_j f(Y_j(s))ds. Use L and M^f for the limiting-source solution Y. Uniform fixed-component coefficient recovery gives L_j f->L f uniformly on X.

For the common marked components a=(i,c), sigma=sqrt(2kappa), the finite-source identities include

\[
d\langle M_j^f,M_j^h\rangle
=2\kappa\sum_a(X_a f)(Y_j)(X_a h)(Y_j)dt,
\qquad
d\langle M_j^f,W_a\rangle=\sigma(X_a f)(Y_j)dt,
\]

\[
d\langle M_j^f,M^h\rangle
=2\kappa\sum_a(X_a f)(Y_j)(X_a h)(Y)dt,
\qquad d\langle W_a,W_c\rangle=\delta_{ac}dt.
\]

All sums tested here are finite. The corresponding first martingales and product-minus-bracket martingales are tested against bounded continuous histories of BOTH state paths, the noise and initial states. In particular W is Brownian relative to this JOINT history, not only its own natural filtration.

Equivalently the joint cylinder generator on (x,y,w) has the marginal generators L_j^x,L^y,(1/2)Delta_w AND the mixed terms

\[
2\kappa\sum_a X_a^xX_a^y
+\sqrt{2\kappa}\sum_a(X_a^x\partial_{w_a}+X_a^y\partial_{w_a}).
\]

Dropping these terms changes the marked coupled object even when every marginal generator is correct.

## 3. Pass characteristics, not stochastic integrals, through weak limits

For any convergent joint subsequence, uniform L_j f convergence and continuity of Lf on compact X transport the drift integrals. All bracket integrands are continuous finite-coordinate readers. The unbounded noise factors in product martingales cause no hidden integrability problem: M_j^f is uniformly bounded on a fixed horizon by2||f||+T*sup_j||L_j f||, and the finitely many Wiener coordinates have uniform moments of every finite order. These bounds give uniform integrability for the required products. Bounded continuous past tests then pass every joint martingale identity; a monotone-class argument extends to the joint canonical history.

Call a limit (Z^1,Z^2,W). Levy's characterization in each finite noise projection makes W Brownian in their joint filtration, including the common initial state. For either state path, form the finite sum

I^f=sigma*sum_a integral (X_a f)(Z) dW_a.

The retained self and mixed-with-W brackets give <M^f-I^f>=0. Thus M^f=I^f. Each Z is therefore a solution of the SAME marked limiting SDE with the SAME W and SAME initial state. This is not an assertion that stochastic integration is a continuous function of uniform paths. The mixed characteristics are what recover the correct integral after the limit.

Pathwise uniqueness from iteration15 now forces Z^1=Z^2. All joint limit laws are supported on the diagonal.

## 4. Diagonal limits imply convergence on the original Wiener space

The target Y=F(Xi,W) already exists; no additional Gyongy-Krylov theorem is needed. If d_T(Y_j,Y) failed to tend to0 in probability, a subsequence would have P(d_T>epsilon)>=eta>0. Take a weakly convergent paired/noise subsequence. The bounded continuous function min(1,d_T/epsilon) has limiting expectation0 by the diagonal property, whereas it dominates the indicator of d_T>epsilon. Contradiction.

Hence the claimed convergence holds on the ORIGINAL probability space with its ORIGINAL common W and chosen initial coupling. Because d_T<=1 it also holds in every finite Lp metric, p>=1. Joint bounded continuous readers of (Y_j,W,Xi_j) transport in expectation. A common marked noise has not been manufactured by independently re-realizing each marginal path law.

## 5. Uniform-in-initial mean comparison, not a perfect flow

First apply the same paired-limit proof with unchanged coefficients and deterministic x_j->x. It proves F(x_j,W)->F(x,W) in probability. Thus x->F(x,W) is continuous into the Lp metric of random paths. Compactness of X makes this continuity uniform in mean.

Now suppose a_j(T,p):=sup_x E_W d_T(F_j(x,W),F(x,W))^p failed to tend to0. Choose deterministic near-maximizers x_j and a compact subsequence x_j->x. The main theorem gives F_j(x_j,W)->F(x,W); the preceding initial continuity gives F(x_j,W)->F(x,W). Boundedness and the triangle inequality contradict the nonvanishing mean. Therefore a_j(T,p)->0.

Let omega_(T,p)(epsilon)=sup_(rho(x,y)<=epsilon) E_W d_T(F(x,W),F(y,W))^p. Then omega_(T,p)(epsilon)->0. For any specified good initial coupling independent of W,

\[
E d_T(F_j(\Xi_j,W),F(\Xi,W))^p
\le2^{p-1}\left[a_j(T,p)+\omega_{T,p}(\epsilon)
+P(\rho(\Xi_j,\Xi)>\epsilon)\right].
\]

This is a structural error decomposition, NOT an explicit boundary-distance or numerical rate. Uniform sup_x E is not E sup_x. No universal exceptional Wiener set, perfect stochastic flow or almost-sure convergence of the entire exhaustion is inferred. Subsequences with summable error probabilities may of course be coupled almost surely on each stated fixed horizon.

## 6. Native changing states and attached readers

The original extended states nu_j->nu and tilted states rho_j=psi_j^2 nu_j->rho are weakly convergent on compact metrizable X. For either family the Skorokhod representation theorem supplies an auxiliary initial coupling with its EXACT native marginals and Xi_j->Xi almost surely. Take its product with the marked Wiener law. The main theorem then transports the native initialized strong paths. This is a probability coupling, not a pointwise Hilbert isometry, a global density ratio or a claim that every initial coupling works.

For stationary tilted sources use rho_j,rho; for U=0 use nu_j,nu. Arbitrary explicitly specified convergent initial couplings are also covered. Native stationarity remains a marginal statement and is not replaced by a common initial measure.

Uniform convergence of the fixed-horizon endpoint/action likelihood functions, and of continuous r_j,|r_j|^2 and their source occupation readers, combines with the coupled path convergence to transport them jointly with W. A likelihood reader evaluated under a tilted law is not thereby called an original-law martingale. Infinite-horizon densities are not constructed: iteration13's nonconstant-probe obstruction remains closed.

## 7. Actual SU2 controls and scope guards

For the R=0 four-link gauge-invariant character z, Delta z=-3z and |Dz|^2=4-z^2. At an equal pair of configurations, shared, independent and globally opposite noise markings give mixed-generator readers respectively

2kappa*(4-z^2), 0, -2kappa*(4-z^2).

All have the same marginal generator. At z=0,kappa=1/8 the correct reader is1, the opposite reader is-1 and the defect is2. The independent-reader defect is1. A bracket with the common projected noise similarly distinguishes the residual martingale from zero. This is a genuine SU2 source coupling test, not a two-state replacement.

For the initial-coupling rival take product Haar at R=0,U=0. Keep all links equal except the first, where Xi_j=-Xi. Central antipodal multiplication preserves Haar; both native marginal states are IDENTICAL. With the same right Killing noise, the first paths remain antipodal for all times, since (-q)b=-(qb). Their bounded quaternion distance is1 and the first product-metric weight is1/2. Thus d_T>=1/2 even at time0. Good initial convergence is indispensable.

For the sup/expectation guard, take uniform omega in{1,...,N} and disjoint initial-parameter spikes D_N(i,omega)=1_(i=omega). Then sup_i E D_N=1/N but E sup_i D_N=1; at N=8 the gap is7/8. This finite scope fixture is not a source-SDE counterexample; it prevents an unjustified upgrade of the proved quantifiers.

The checker freshly replays iteration15 and preregisters45 actual free-SU2 mixed-generator packets,9 joint covariance/residual packets,25 exact quaternion initial-coupling packets,18 product-tail envelopes,6 sup/expectation guards and48 Lp triangle envelopes. These do not mechanically certify tightness, Levy/martingale-limit arguments, native measure coupling or the source theorem.

## Bounded closure and reopening policy

The written fixed-lattice construction now has all its declared arrows: retained equal-time state and gradient form; identified actual source semigroup and correlation packets; bounded-probe pressure/ground-vector and form/core comparisons; stationary and every-start-point paths; finite-horizon likelihood/entropy and the negative infinite-horizon domain classification; canonical continuous force and strong marked-noise maps; and the native common-noise thermodynamic comparison just constructed.

No nonredundant executable construction cell remains for THIS frozen objective/envelope. Independent source/analytic review is still open, and none of the finite controls substitutes for it. Physical clock/energy conversion, refinement/continuum construction and reviewed Yang-Mills root assembly remain open OUTSIDE this completion; the parent gap-net outcome is not discharged. Optional perfect-flow or higher-smoothness strengthenings are not silently made new completion criteria. Do not create a leaf merely to wait for review or an unprovided physical bridge.

Reopen executable work only for a concrete analytic falsifier/gap in an input or constructor, a newly supplied source-compatible calibration/refinement bridge with authority, or an explicitly revised bounded objective requiring an additional typed object. Preserve the nonconstant infinite-horizon density obstruction unless its source envelope changes. This is completion at written-proof scope, not independent certification of the source theorem or the classical Yang-Mills problem.

Contract: `research/kitaev/contracts/yang-mills-probe-coupled-transport.v1.json`.
Checker: `research/kitaev/checkers/check_yang_mills_probe_coupled_transport.py`.
Receipt: `research/kitaev/results/yang-mills-probe-coupled-transport-v1.json`.
