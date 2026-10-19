# Infinite-horizon domain obstruction and source long-window separation

## Source and issue-boundary DPC

Iteration13/100 addresses `small-probe-long-window-separation:v1`. Retain the fixed-lattice source with kappa>0,0<=R<9/64,m=kappa*(1/2-3R), and a fixed real smooth local gauge-invariant U with ||U||<=delta<=m/8. Let P_0=P_0^nu and P_1=P_U^rho be the original and tilted STATIONARY continuous-path laws. Their gaps are at least m and g=m-2delta>=3m/4. Keep (A+U)psi=Epsi,rho=psi^2 nu,H^-1<=psi<=H and r=D log psi.

Work on C([0,infinity),X) with canonical RAW observation sigma-fields F_S= sigma(X_t:0<=t<=S), F_infinity=sigma(union_S F_S). Cross-law comparisons may be completed separately on a fixed horizon. Completing one law globally must not insert a separating future-null event into F_0 and then falsely claim finite-horizon equivalence on that enlarged field.

The preceding packet proves that the finite-horizon likelihood is

\[
D_S=\psi(X_0)\psi(X_S)
\exp\left(SE-\int_0^S U(X_t)dt\right),
\qquad E_0 D_S=1.
\]

Put a=E-rho(U)=kappa*rho(|r|^2) and b=nu(U)-E=kappa*nu(|r|^2).

- **Problem:** a positive normalized density on every finite horizon does not decide whether its restrictions admit a global density or remain uniformly integrable.
- **Conjecture:** constant probes leave the laws identical; every nonconstant admitted probe yields mutually singular infinite-observation path laws despite bounded-equivalent equal-time measures. Source gap/time-average bounds quantify the separation.
- **Rivals:** extrapolate finite-horizon normalization to global absolute continuity; infer mutual singularity from positive entropy rate alone without ergodicity; infer a uniform positive discrimination rate from the mass gap; conflate dynamic singularity with a new equilibrium phase or physical clock.
- **Risky consequences:** strict signed likelihood rates, density collapse and non-uniform-integrability for nonconstant probes, total variation tending to1 with explicit source horizons, and an identical-law constant exception.
- **Strongest falsifiers:** the actual free-SU2 plaquette family has positive a,b but arbitrarily small rates; finite Bernoulli likelihoods retain mean1 at every prefix; adding an invariant flag leaves positive entropy rates but common path mass1/2. The last rival violates the required one-dimensional kernel.
- **Disposition:** infinite-horizon density extension is obstructed for every nonconstant admitted U. This is a CLOSED domain boundary, not an unavailable authority transition. Finite-horizon arrows survive unchanged. Independent source/analytic review remains open.

## Strict dichotomy before dividing by an entropy rate

If U is constant, psi=1,E=U,rho=nu and D_S=1. The stationary laws are identical on F_infinity, and the densities are uniformly integrable.

Conversely a=0 implies q(psi)=0. The original gap with kernel span{1} forces psi to be constant; positivity/normalization gives psi=1. The eigen-equation then gives U=E nu-a.e., and full support plus continuity gives U=E everywhere. Also b=0 iff r=0 nu-a.e.; bounded equivalence of nu and rho then gives a=0. Hence for a NONCONSTANT U,

\[
a>0,\quad b>0,\qquad \rho(U)=E-a<E<E+b=\nu(U).
\]

No positive lower bound on a or b uniform over the whole norm-small probe ball is asserted. These margins, not just the original mass gap, enter every discrimination budget below.

## Gap control of time averages, with an almost-sure argument

For either stationary law write mu for its state, gamma=m or g for its gap, and Ubar_S=S^-1*integral_0^S U(X_t)dt. Spectral contraction on centered real U gives

\[
|\operatorname{Cov}_\mu(U(X_0),U(X_t))|
\le e^{-\gamma t}\operatorname{Var}_\mu U.
\]

Thus

\[
\operatorname{Var}_\mu(\overline U_S)
=\frac2{S^2}\int_0^S(S-t)\operatorname{Cov}_\mu(U(X_0),U(X_t))dt
\le\frac{2\operatorname{Var}_\mu U}{\gamma S}
\le\frac{2\delta^2}{\gamma S}.
\]

This also proves the needed almost-sure time average without assuming an unverified ergodic component. Chebyshev and Borel-Cantelli at S_n=n^2 in the fixed source units give Ubar_(S_n)->mu(U) almost surely, first for rational error tolerances. For S_n<=S<=S_(n+1), bounded U gives |Ubar_S-Ubar_(S_n)|<=2delta*(S_(n+1)-S_n)/S_n->0. Therefore convergence holds for all S->infinity.

The two measurable events lim Ubar_S=nu(U) and lim Ubar_S=rho(U) have probability1 in their respective laws and are disjoint for nonconstant U. Consequently P_0 and P_1 are mutually singular on F_infinity. This proof uses the actual gap/simple kernel and fixed U; positive expected entropy growth alone would not suffice.

## Likelihood collapse and the exact domain of the arrow

Endpoint logs are bounded in absolute value by2log H. Combining the time averages with log D_S yields

\[
\frac1S\log D_S\longrightarrow-b<0\quad P_0\text{-a.s.},
\qquad
\frac1S\log D_S\longrightarrow a>0\quad P_1\text{-a.s.}
\]

Thus D_S->0 P_0-a.s. and D_S^-1->0 P_1-a.s. Both have expectation1 at every finite S under their corresponding reference law. Neither density family is uniformly integrable, and neither can converge in L1 to a global Radon-Nikodym density. The limiting-density mean is0 whereas the finite-horizon means remain1: mass-loss defect1. The conditional Z_S differs from D_S only by the fixed bounded positive initial factor, so its nonconstant-probe extension fails as well.

This is NOT a failure of the finite-horizon construction, nor a new thermodynamic phase. Equal-time rho and nu remain mutually absolutely continuous with bounded densities. Even an auxiliary perturbation supported on one finite plaquette can separate infinite observation histories. Do not reopen the disproved global-density extension unless the source envelope changes (for example to a constant probe or a finite horizon).

## Quantitative source discrimination and finite-window total variation

Use the event B_S={Ubar_S<E} to identify the tilted law. The source mean margins give

\[
P_0(B_S)\le\frac{2\delta^2}{m S b^2},\qquad
P_1(B_S^c)\le\frac{2\delta^2}{g S a^2}.
\]

With TV defined as sup_B|P_1(B)-P_0(B)| in[0,1],

\[
\operatorname{TV}(P_1|_{F_S},P_0|_{F_S})
\ge\max\left(0,1-\frac{C_U}{S}\right),\qquad
C_U=2\delta^2\left(\frac1{m b^2}+\frac1{g a^2}\right).
\]

For target error sum epsilon in(0,1), S>=C_U/epsilon is sufficient. The checker supplies the least positive INTEGER source horizon satisfying this sufficient rule; the process itself remains continuous-parameter. This is a conservative Chebyshev budget, not an optimal exponent, universal detectability floor or physical-time calibration.

There is also a fixed-source signed-likelihood concentration statement: since |log D_S-S(E-Ubar_S)|<=2log H,

\[
P_0\left(\left|S^{-1}\log D_S+b\right|>
\eta+2\log H/S\right)\le\frac{2\delta^2}{m S\eta^2},
\]

and the tilted version replaces +b,m by -a,g.

## Uniform cofinal source windows, not a blind exchange of limits

The preceding packet proves a_j->a and b_j->b through the ACTUAL changing states. For fixed nonconstant U they are eventually bounded below by a/2,b/2. All finite-source gaps retain the same m,g and endpoint bound H. Thus along ANY exhaustion j and source horizons S_j->infinity, the two error bounds tend to0 and finite-source TV at S_j tends to1. Signed likelihood rates converge in probability to -b and +a in their OWN source laws. No common sample-space almost-sure comparison across distinct original states is claimed.

This cofinal conclusion needs the uniform bounds and limiting positive margins; fixed-horizon weak path convergence by itself does not permit the exchange. It also does not give a lower entropy floor uniform over U tending to a constant.

## Actual free-source control and entropy-only hostile

In the predecessor's R=0 gauge-invariant plaquette family, t=1/(256n),epsilon=t/(1+t^2),J=1+3t^2+t^4 give

\[
a=3\kappa t^2/J,\quad b=3\kappa t^2,\quad
\delta=\frac{6\kappa\epsilon}{1-2\epsilon},\quad
m=\kappa/2,\quad g=m-2\delta.
\]

Every n is a nonconstant admissible probe, but both rates tend to0. The fixed original gap therefore cannot be used as a lower likelihood rate. Exact rational planners retain these actual margins and source scales rather than replacing them by m.

To test the role of ergodicity, adjoin an invariant fair flag. On flag0 both models use P_0; on flag1 one uses P_0 and the other P_1. Conditional flags are observed and have the same weights. The finite-horizon entropies have HALF the actual positive rates, yet the laws share common path mass1/2 and their infinite-horizon TV is1/2, not1. The flag supplies an extra zero mode, so this is outside the source's simple-kernel hypothesis. It refutes an entropy-only shortcut, not the source theorem.

The checker freshly replays the path-density receipt, verifies36 actual free-SU2 source-budget packets,18 constant exceptions,12 normalized Bernoulli prefix/flag packets and9 variance-kernel envelopes. The finite word regressions use fair versus3/4-biased Bernoulli words: their mean-one prefix likelihoods and the shared-flag TV factor are exact. They are not SU2 path simulations or mechanical verification of the almost-sure theorem. The shared-mass hostile residual is1/2; actual free-plaquette rate decay retains b_n/b_1=1/n^2.

Next executable issue: the remaining CONFIGURATION-WISE generator cell is still open. Infinite-horizon reweighting cannot fill it. Attempt volume-uniform one-link derivative smoothing/comparison for the original finite-source diffusions and bounded-probe filters, using the retained C2 interaction tails and positive Jacobi/Hessian majorant. Establish continuous ground-vector gradients and the Feller cylinder generator core by a genuine C(X) resolvent-range argument if those estimates suffice; otherwise isolate the exact regularity obstruction. Do not promote based L2 gradients or full support alone to pointwise drift, and do not assume unproved higher derivatives. This is a distinct remaining source realization problem, not renewed pursuit of the closed infinite-horizon density branch.

Contract: `research/kitaev/contracts/yang-mills-probe-long-window.v1.json`.
Checker: `research/kitaev/checkers/check_yang_mills_probe_long_window.py`.
Receipt: `research/kitaev/results/yang-mills-probe-long-window-v1.json`.
