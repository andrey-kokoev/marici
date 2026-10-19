# Quasilocal ground vector and Feller realization of the small-probe transform

## Question, source and stratum

Does the actual nonlinear log-filter equation supply the missing uniform regularity, rather than promoting an L2 eigenvector directly to a continuous Feller multiplier?

SCC obligation: nonlinear forward realization, uniform-topology completion and Feller attachment transport. Retain the original source on X=SU(2)^E, radius-two link metric, locally finite plaquette-sharing distance d, kappa>0, 0<=R<9/64, a=4/3, c=1/2-3R and m=kappa*c. Source semigroup parameters are not calibrated physical time. Fix real smooth gauge-invariant U with norm<=delta<=m/8 and a finite nonempty K containing its support. Write M_U=sum_i ||gradient_i U||_infinity. Constants are included by taking M_U=0.

The prior packets give the finite and infinite bounded-probe semigroups Q_U, normalized filters h_T=Q_U(T)1/||Q_U(T)1|| in their own original vacuum measures, normalized eigenvectors psi, weak transport of psi_Lambda^2 nu_Lambda to psi^2 nu, and the canonical conservative L2 ground-state transform. The ORIGINAL vacuum measures remain distinct. Finite measures/functions on X use the prescribed exterior-Haar extension.

## Issue-boundary DPC

- **Problem:** L2 convergence and a spectral gap supply neither a uniform continuous representative nor a bounded continuous inverse for Feller conjugation.
- **Conjecture:** covariant differentiation puts the Hamilton-Jacobi nonlinearity into common advection. The old cooperative gradient matrix then bounds log-filter gradients uniformly over boxes and source parameter. Compactness plus based state identification completes the construction in C(X).
- **Named rivals:** treat mixed Hessian terms as a new uncontrolled zeroth-order coupling; infer uniform convergence from an L2 gap; identify continuous versions without full support; copy finite/infinite Hilbert coordinates.
- **Risky consequences:** weighted log-gradient bound M_U/m, uniform two-sided normalized-filter bounds, coupling-sensitive spatial tails vanishing at R=0, common-C(X) eigenvector/inverse transport and a conservative Feller semigroup.
- **Strongest falsifiers:** dropping mixed-block advection loses2 in an exact covariant jet; normalized triangular spikes have L2 convergence but sup-distance at least1/2; a non-full-support state leaves continuous versions with sup-distance1 indistinguishable in L2.
- **Disposition:** the written PDE/compactness argument below supplies the continuous quasilocal version and Feller transport. Smooth logarithmic drift and cylinder form/operator-core identification are separate. Finite controls do not independently verify the source analysis.

## The nonlinear source equation before norm estimates

Work FIRST on a finite box Lambda containing K. Put L_Lambda=-A_Lambda= kappa*Delta+b_Lambda dot gradient with the actual source drift, q(T)=Q_(Lambda,U)(T)1 and F(T)=log q(T). Bounded-potential order gives exp(-delta T)<=q(T)<=exp(delta T). The calculation below is first made for finite smooth retained-label truncations. If the original potential is only C2, its certified absolute C2 tail gives uniform C1 convergence of the finite-source drifts; compact finite-dimensional diffusion stability and bounded-potential Duhamel stability give uniform q convergence on each bounded parameter interval. The same majorant controls every truncation, and coordinate-Lipschitz bounds pass by lower semicontinuity. No unproved smoothness of the completed potential is needed. At the smooth stages the logarithm satisfies

\[
\partial_T F=L_\Lambda F+\kappa\sum_j|\nabla_jF|^2-U,\qquad F(0)=0.
\]

All Hessians below are Levi-Civita covariant Hessians on the product, not unsymmetrized invariant-frame derivatives. Symmetry of the scalar Hessian gives the exact block identity

\[
\left\langle\nabla_i F,\nabla_i\sum_j|\nabla_jF|^2\right\rangle
=2\sum_j\left\langle\nabla_jF,\nabla_j\frac{|\nabla_iF|^2}{2}\right\rangle.
\]

Thus the nonlinear term changes the COMMON advective drift to b_Lambda+2kappa*gradient F; it does not add an uncontrolled Hess(F) coupling after this identity. The old one-form/Kato comparison retains Ricci1/2 and its actual symmetric nonnegative Hessian majorant h^Lambda with weighted rows/columns<=3R. For gamma_i=|gradient_i F| the resulting inequality is

\[
(\partial_T-L_\Lambda-2\kappa\nabla F\cdot\nabla)\gamma_i
\le-\kappa\gamma_i/2+\kappa\sum_jh^\Lambda_{ij}\gamma_j+u_i,
\qquad u_i=\|\nabla_iU\|_\infty.
\]

Regularize a vanishing block norm, use Kato's inequality, and remove the regularization on each finite compact product. The spatially constant cooperative barrier is unaffected by the advective drift. That drift only needs bounded smooth coefficients on each finite source/finite parameter interval; no volume-uniform Hess(F) bound is assumed. The maximum principle yields

\[
\|\nabla_iF(T)\|_\infty
\le\int_0^T[B_s^\Lambda u]_i\,ds,
\qquad B_s^\Lambda=e^{-\kappa s/2}e^{\kappa s h^\Lambda}.
\]

Define G_K(v)=sum_i a^(d(i,K))||gradient_i v||_infinity. The retained weighted column bound and support of u imply

\[
G_K(F(T))\le\frac{1-e^{-mT}}m M_U\le M_U/m.
\]

This estimate uses M_U, not merely the small sup norm of U. Norm-smallness is needed by the previous spectral branch; the finite log-gradient estimate itself does not require it.

## Noncollapse and coupling-sensitive locality

One link has geodesic diameter2pi. Consequently osc(log q)<=O:=2pi M_U/m. With H=exp(O), normalization in EACH actual probability measure gives

\[
H^{-1}\le h_{\Lambda,T}\le H,\qquad
G_K(\log h_{\Lambda,T})\le M_U/m,
\qquad G_K(h_{\Lambda,T})\le H M_U/m.
\]

No global vacuum max/min ratio is used. For the spatial tail remove the identity INSIDE the positive matrix: B_s-e^(-kappa s/2)I is entrywise nonnegative, and u is supported in K. Therefore

\[
\sum_{i\notin K}a^{d(i,K)}\|\nabla_i\log h_{\Lambda,T}\|_\infty
\le M_U\int_0^\infty(e^{-ms}-e^{-\kappa s/2})\,ds
=\frac{M_U}{\kappa}(c^{-1}-2).
\]

For b>=1 let K_b={i:d(i,K)<b}, a FINITE set by local finiteness of the source metric. Configurations agreeing on K_b consequently satisfy

\[
|\log h_{\Lambda,T}(x)-\log h_{\Lambda,T}(y)|
\le\frac{2\pi M_U}{\kappa}(c^{-1}-2)a^{-b}.
\]

The corresponding h bound has one extra factor H. The gain vanishes at R=0, where the filters depend only on K. It is not subtraction of unrelated scalar upper bounds.

## Finite falsifiers before changing completion topology

For a covariant two-block jet with gradient entries v_0=v_3=1 and symmetric Hessian entries H_(0,3)=H_(3,0)=1, all others zero, the block0 nonlinear derivative is2. Keeping only same-block advection gives0. The mixed-block residual is2.

On[0,1] with Lebesgue probability let b_n(x)=max(1-nx,0) and r_n=1+b_n. Its squared norm is1+4/(3n) and mean is1+1/(2n). The positive normalized psi_n=r_n/||r_n|| has squared L2 distance to1 at most4/(3n), but psi_n(0)>=3/2 for every n>=2. The rank-one operators I-|psi_n><psi_n| even have gap1. These are not local SU2 source models: their growing Lipschitz constants violate the new estimate. They reject the L2-only promotion.

On the discrete compact space{0,1} with probability concentrated at0, functions(1,1) and(1,2) agree in L2 but differ in sup norm by1. Compactness alone does not identify the continuous version; full support is indispensable.

## Source-derived compactness and based sewing

For a continuous function define Lip_i by changes in link i measured in its SU2 geodesic metric. This agrees with the gradient sup norm for a smooth cylinder. Weighted sums of Lip_i are lower semicontinuous under uniform convergence. Thus the finite bounds above pass to uniform limits without claiming classical differentiability in infinitely many variables.

The family {h_(Lambda,T):Lambda contains K,T>=0} is uniformly bounded and equicontinuous on compact X. To verify the latter, first choose b so the weighted tail outside finite K_b is small, then control the finitely many coordinates in K_b by their uniform Lipschitz constants. The quantifier is: for each fixed U and tolerance there is a finite coordinate neighborhood, uniformly over this family. No globally finite source or universal cutoff for unbounded M_U is inferred. Arzela-Ascoli gives precompactness in C(X).

The ORIGINAL nu has full support. Indeed each finite coordinate set S has an actual conditional potential with a finite uniform oscillation bound C_S, from the retained absolutely summable interaction. Its conditional density relative to probability Haar is at least exp(-C_S)>0. Every nonempty basic open cylinder therefore has positive nu measure. The finite source measures with their prescribed exterior extension have the same support property.

For fixed T the existing strong C(X) probe comparison gives q_(Lambda,T)->q_T uniformly. Weak ORIGINAL-state convergence gives nu_Lambda(q_(Lambda,T)^2)->nu(q_T^2), so the correctly normalized h_(Lambda,T)->h_T uniformly. All preceding bounds pass to h_T using the coordinate-Lipschitz definition.

The infinite filters already converge to the spectral psi in their OWN L2(nu) norm. Any uniformly convergent subsequence with T tending to infinity has this same L2 version. Full support makes its continuous representative unique. Precompactness then proves h_T->psi uniformly, with a continuous everywhere-positive representative satisfying H^-1<=psi<=H and the stated log-Lipschitz/tail bounds. The same argument gives continuous representatives for each finite psi_Lambda with the same bounds.

To compare those representatives, take any uniformly convergent subsequence psi_Lambda->chi along an exhaustion. Based weak tilted-state convergence gives nu_Lambda(psi_Lambda^2 f)->nu(psi^2 f) for every continuous f. Uniform convergence and weak ORIGINAL-state convergence also give the limit nu(chi^2 f). Thus chi^2 nu=psi^2 nu. Positive continuous representatives and full support imply chi=psi everywhere. Hence the full exhaustion has

\[
\|\psi_\Lambda-\psi\|_\infty\longrightarrow0,
\qquad
\|\psi_\Lambda^{-1}-\psi^{-1}\|_\infty\longrightarrow0.
\]

This is a newly proved common-C(X) comparison, not an assumed isometry of the original Hilbert spaces. It gives no uniform operator-norm comparison over the C(X) unit ball.

## Feller realization and fixed-input transport

The actual Q_U(s) is already a strongly continuous bounded-perturbation semigroup on C(X). Bounded continuous multiplication and its inverse now realize

\[
\widetilde P_U(s)f=e^{sE}\psi^{-1}Q_U(s)(\psi f)
\]

on C(X). This agrees with the previous L2 construction; continuous functions equal almost everywhere agree everywhere by full support. Positivity, the semigroup law and constant preservation therefore hold on X. It is a strongly continuous conservative positive contraction semigroup on C(X), the claimed Feller realization. Its C(X) generator domain is {f:psi f belongs to Dom(L_U^C)}, with generator psi^(-1)(L_U^C+E)(psi f); no cylinder core or smooth drift is asserted.

Finite-source inverse/eigenvector convergence, E_Lambda->E, and the existing fixed-input Q_(Lambda,U) comparison yield, for each f in C(X) and finite S,

\[
\sup_{0\le s\le S}\|\widetilde P_{\Lambda,U}(s)f-\widetilde P_U(s)f\|_\infty\longrightarrow0.
\]

The varying input psi_Lambda*f is controlled by its uniform convergence and ||Q_(Lambda,U)(s)||<=exp(delta S), before applying the fixed-input theorem to psi*f. Gauge equivariance and the L2 relative gap>=3m/4 are preserved. The original magnetic vacuum and physical clock/continuum gates are unchanged.

## Rational locality budgets, checks and next constructor

Using2pi<44/7, the logarithmic tail is at most C_log M_U(3/4)^b with C_log=44(c^-1-2)/(7kappa). The whole-window coefficient is2376/(35kappa). The least b>=1 meeting a tolerance is a sufficient locality rule: kappa=M_U=1 and tolerance1/1000 give39 universally and32 at R=9/128. H can be bounded without floating point by2^k with k=ceil(88 M_U/(7m)). These are conservative envelopes, not physical measured amplitudes.

The checker replays the Doob receipt and preregisters24 covariant jet packets,12 positive gradient-resolvent packets,24 dyadic norm envelopes,90 rational logarithmic-tail planners and the three falsifiers. Finite controls are not SU2 eigenfunction evaluations; independent analytic review remains open.

Next executable issue: identify the transformed closed gradient form and its cylinder form/operator core in its ACTUAL tilted state. Use the bounded positive multiplier and retained weak gradient bounds to compare form domains and derive the source weak logarithmic drift. Do not infer a C(X) generator core or a classical smooth drift from Lipschitz continuity alone. This is a domain-identification problem with existing source material, not an authority-waiting leaf.

Contract: `research/kitaev/contracts/yang-mills-probe-quasilocal.v1.json`.
Checker: `research/kitaev/checkers/check_yang_mills_probe_quasilocal.py`.
Receipt: `research/kitaev/results/yang-mills-probe-quasilocal-v1.json`.
