# Original-to-tilted path density, weak Girsanov arrow and source entropy

## Source and issue-boundary DPC

Iteration12/100 addresses `small-probe-path-density:v1`. Keep the actual fixed-lattice sources on X=SU(2)^E, kappa>0,0<=R<9/64,m=kappa*(1/2-3R), and real smooth gauge-invariant local U with ||U||<=delta<=m/8. Let (A+U)psi=Epsi, nu(psi^2)=1, rho=psi^2 nu. Previous packets supply H^-1<=psi<=H, L=M_U/m, H=exp(2pi L), r=D log psi with L-infinity ell2 norm<=L, and stationary continuous-path source laws. All parameters/rates below are SOURCE units.

Write P_0^nu for the original stationary diffusion, P_U^rho for the tilted stationary diffusion, and P_0^rho for the ORIGINAL kernel started in rho. The last law is generally not stationary. Its initial-state density relative to P_0^nu is psi(X_0)^2. Distinguishing these three laws is essential.

- **Problem:** a same-source unitary and a tilted stationary law do not yet specify their actual path-space comparison with the original vacuum source.
- **Conjecture:** the ground-state equation gives a normalized endpoint/action density; closed weak chain rules identify its stochastic exponential and actual drift shift. Stationarity gives exact forward/reverse entropy rates and finite-source transport.
- **Rivals:** discard the changed initial state; omit the energy shift or quadratic-variation compensation; read finite-horizon bounded densities as infinite-horizon absolute continuity; call a source entropy rate a physical clock.
- **Risky consequences:** an explicit finite-horizon Radon-Nikodym arrow, conditional density martingale, weak Girsanov interpretation, exact two entropy formulas and thermodynamic transport of likelihood/entropy readers.
- **Strongest falsifiers:** omitting the initial factor preserves total mass but changes a free-source SU2 plaquette readout by512/65537; omitting E loses logarithmic mass1/256 for a constant admissible probe; omitting stochastic compensation gives Gaussian log-mass defect1.
- **Disposition:** the written density, chain-rule and entropy argument supplies the finite-horizon arrow. The checker includes an actual free-source gauge-invariant plaquette family, but does not mechanically verify the general interacting-source theorem or stochastic imports. Independent analytic review remains open.

## Endpoint/action density and its normalization

For0<=t<=S define on the original path law

\[
Z_t=\frac{\psi(X_t)}{\psi(X_0)}
\exp\left(tE-\int_0^tU(X_s)ds\right),\qquad
D_t=\psi(X_0)^2 Z_t.
\]

The original diffusion Feynman-Kac formula realizes the ACTUAL bounded perturbation Q_U(t)=exp[-t(A+U)]. This follows, for bounded continuous U, from bounded-potential product approximations and continuity of paths; it is not a new kernel chosen to match the desired law. The ground-state equation gives e^(tE)Q_U(t)psi=psi. Conditional Markov expectation then proves E_0[Z_t|F_s]=Z_s and E_0[Z_t|F_0]=1. In particular D_t is a mean-one density martingale with D_0=psi(X_0)^2, not1.

Telescoping the ground-state kernel through finite observation words, or conditioning successively using Feynman-Kac, gives

\[
\frac{dP_U^\rho}{dP_0^\rho}\bigg|_{\mathcal F_S}=Z_S,
\qquad
\frac{dP_U^\rho}{dP_0^\nu}\bigg|_{\mathcal F_S}=D_S
=\psi(X_0)\psi(X_S)
\exp\left(SE-\int_0^S U(X_s)ds\right).
\]

Finite words identify the continuous-path law because rational evaluations generate its Borel sigma-field. Thus no martingale-problem uniqueness assumption is hidden in this identification. Both densities are positive and bounded, with

\[
H^{-2}e^{-2\delta S}\le D_S,Z_S\le H^2e^{2\delta S}.
\]

Here |E|<=delta. This gives mutual absolute continuity on EACH fixed horizon, and consistent restrictions, but no bound uniform over S->infinity. It is not a claim of an infinite-horizon density.

## Weak logarithmic chain rule, not assumed classical smoothness

The known eigen-equation puts psi in Dom(A), with Apsi=(E-U)psi bounded. Its weak gradient is bounded, and psi is bounded away from0. The closed form product/chain rules imply that for a smooth scalar phi on the range of psi,

\[
A\phi(\psi)=\phi'(\psi)A\psi-\kappa\phi''(\psi)|D\psi|^2.
\]

To justify the operator-domain statement, test Apsi against phi'(psi)*h for h in the form domain. This multiplier preserves that domain because its weak gradient is bounded. Product expansion identifies the displayed bounded L2 right-hand side; the closed-form representation theorem puts phi(psi) in Dom(A). Bounded smooth extensions off the positive interval justify log without a singularity at0.

In particular ell=log psi is continuous, bounded, in Dom(A), and

\[
A\ell=E-U+\kappa|r|^2.
\]

The original diffusion's generator-domain martingale for ell and the product rule for ell^2 give

\[
N_t=\ell(X_t)-\ell(X_0)-\int_0^t(U-E-\kappa|r|^2)(X_s)ds,
\qquad \langle N\rangle_t=2\kappa\int_0^t|r|^2(X_s)ds.
\]

These are valid under P_0^nu and its bounded INITIAL-state reweighting P_0^rho. The latter preserves martingale identities since its density is F_0-measurable. All weak versions are interpreted through these laws, not arbitrary deterministic initial points.

Consequently

\[
Z_t=\exp(N_t-\tfrac12\langle N\rangle_t),\qquad
E_0\exp(\tfrac12\langle N\rangle_S)\le e^{\kappa L^2S}.
\]

Novikov therefore applies on every fixed horizon. Weak Girsanov subtracts the cross bracket2kappa*integral Df dot r from the original cylinder martingale, giving Markov drift -Af+2kappa*r dot Df=-Tf, exactly the previously identified tilted drift. The source covariance2kappa*Df dot Dg is unchanged. This uses scalar martingale brackets and does not assert a strong infinite-dimensional SDE solution or all-start-point regularity.

## Exact forward and reverse finite-horizon entropies

Let Ent(P|Q)=E_P log(dP/dQ). Stationarity of EACH law under its OWN initial state evaluates both endpoints and the action in log D_S:

\[
\operatorname{Ent}(P_U^\rho|P_0^\nu)_{[0,S]}
=\operatorname{Ent}(\rho|\nu)+S a_U,
\qquad a_U=E-\rho(U)=\kappa\rho(|r|^2),
\]

\[
\operatorname{Ent}(P_0^\nu|P_U^\rho)_{[0,S]}
=\operatorname{Ent}(\nu|\rho)+S b_U,
\qquad b_U=\nu(U)-E=\kappa\nu(|r|^2).
\]

The first rate is the actual eigen-energy identity. For the second integrate Aell=E-U+kappa|r|^2 against1; A1=0 and ell belongs to Dom(A), so its mean is0. Both rates are nonnegative and bounded by min(2delta,kappa L^2). The initial entropies are finite and at most2log H. These are source inverse-parameter rates, not physical energies or a clock calibration. A constant U has psi=1,E=U and zero rates: a vacuum energy shift cancels the action exactly.

## Thermodynamic transport at fixed horizon

Apply the construction separately in every actual source. Uniform psi_j->psi and E_j->E, and fixed bounded continuous U, imply D_(j,S)->D_S uniformly on the common path carrier C([0,S],X). The uniform positive lower bound also gives uniform convergence of log D_(j,S) and D_(j,S)*log D_(j,S). Original path-law convergence is the preceding theorem at U=0. Therefore, for any bounded continuous path reader F,

\[
E_{j,U}F=E_{j,0}(D_{j,S}F)\longrightarrow E_0(D_SF)=E_UF.
\]

The same argument transports both relative entropies; alternatively use weak original/tilted states and the exact formulas above. Initial log psi readers converge uniformly, and E_j-rho_j(U),nu_j(U)-E_j converge. The conditional densities Z_(j,S), initial densities psi_j(X_0)^2 and their joint bounded continuous readers transport as well. The original-state module comparison also gives strong based r_j->r by the uniformly convergent inverse multipliers. Clip common recovery vector fields radially to the radius-L ball. This preserves recovery and bounds their norms pointwise, so the inequality ||r_j|^2-|eta_n|^2|<=2L*|r_j-eta_n| gives strong based scalar recovery of |r_j|^2. The preceding stationary occupation estimate, now under the ORIGINAL path laws, transports their time integrals jointly with paths. Uniform log psi_j and E_j convergence then transports N_j, its bracket, Z_j and D_j jointly as continuous paths on each fixed horizon. Initial rho_j reweighting is bounded and continuous, so the same holds under the original kernel started in rho_j. This is weak transport of measures/readers with explicit density functions, NOT total variation convergence of distinct changing original path measures. No limiting measurable gradient is evaluated in another source measure.

## Actual free-source plaquette and exact controls

At R=0 the original state is product Haar and A=-kappa*sum Delta_i. Let x be the fundamental character of one four-link plaquette holonomy. It is gauge invariant, ||x||<=2, nu(x)=nu(x^3)=0,nu(x^2)=1, and Ax=3kappa*x from four Casimirs3/4. Put psi_raw=1+epsilon*x, normalization N=1+epsilon^2, E=0, and U=-3kappa*epsilon*x/(1+epsilon*x). For epsilon<=1/256 this is a genuine smooth local gauge-invariant probe with norm<=6kappa*epsilon/(1-2epsilon)<kappa/16=m/8. It has the exact normalized positive eigenvector psi_raw/sqrt(N).

For rational t=1/(256n),epsilon=t/(1+t^2), put J=1+3t^2+t^4. Haar character moments (Catalan even moments) and the positive resolvent branch give

\[
a_U=3\kappa t^2/J,\quad b_U=3\kappa t^2,\quad
\operatorname{Ent}(\nu|\rho)=\log J-t^2,
\]

\[
\operatorname{Ent}(\rho|\nu)
=\frac{5t^2+(14/3)t^4+t^6/6}{J}-\log J.
\]

One derivation uses x=z+z^-1 and the Haar class weight1-(z^2+z^-2)/2. The weighted psi_raw^2 coefficients through order4 are N,epsilon,-1/2,-epsilon,-epsilon^2/2. Fourier coefficients of log psi_raw are -log(1+t^2) at0 and (-1)^(k+1)t^k/k at +/-k; only the first four enter. Also nu[1/(1+epsilon*x)]=1+t^2, the small Catalan branch solving F=1+epsilon^2 F^2. This derives the formulas without numerical path simulation. Alternating rational log(1+y) brackets certify the initial entropy intervals.

The checker freshly replays the diffusion-path receipt and preregisters48 weak chain/Girsanov jet packets,36 Gaussian compensation packets through order6,36 constant-probe cancellation packets and18 actual free-plaquette entropy packets. The latter include Haar moment/branch checks and four horizons. Dropping the initial density gives the ORIGINAL initial mean0 of x instead of2epsilon/(1+epsilon^2); at epsilon=1/256 the exact defect is512/65537 although both candidate laws have mass1. Dropping E for U=1/256,kappa=1,S=1 gives log-mass defect1/256. Dropping half-bracket compensation in a unit Gaussian martingale gives log-mass defect1. The analytic stochastic and interacting-source arguments are not mechanically certified by these controls.

Next executable issue: classify whether this actual finite-horizon arrow extends to infinite observation horizons. Use source spectral gaps/ergodicity, endpoint bounds and time averages of fixed U to determine equivalence versus singularity and density uniform integrability; derive source discrimination bounds if available. This is the unresolved global domain of the arrow, not a request to wait for review. Keep any obstruction scoped to path laws, distinct from the already bounded-equivalent equal-time states and from physical/continuum conclusions.

Contract: `research/kitaev/contracts/yang-mills-probe-path-density.v1.json`.
Checker: `research/kitaev/checkers/check_yang_mills_probe_path_density.py`.
Receipt: `research/kitaev/results/yang-mills-probe-path-density-v1.json`.
