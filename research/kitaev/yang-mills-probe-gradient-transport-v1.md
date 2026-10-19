# Based gradient-norm transport and tilted operator-graph recovery

## Source and issue-boundary DPC

Iteration10/100 addresses `small-probe-gradient-transport:v1`. Retain X=SU(2)^E, kappa>0,0<=R<9/64,m=kappa*(1/2-3R), and fixed real smooth gauge-invariant local U with ||U||<=delta<=m/8. All parameters are source units. Along an exhaustion use the actual exterior-Haar/Brownian extensions, original measures nu_j and operators A_j, and normalized positive eigenvectors psi_j of A_j+U with eigenvalues E_j. Let rho_j=psi_j^2 nu_j, T_j the actual tilted generator, and use no subscript for the infinite source. Previous packets prove weak nu_j->nu and rho_j->rho, uniform psi_j/inverse convergence, E_j->E, fixed-input Feller transport, and the actual cylinder form/operator cores.

- **Problem:** uniform positive eigenvector convergence and bounded gradients do not imply derivative convergence; a graph comparison needs more than cylinder energies.
- **Conjecture:** actual eigen-energy identities prevent gradient norm loss, and original conditional integration by parts identifies all weak components. Based finite-component tests then give strong varying-Hilbert convergence, localized drift transport and operator-graph recovery.
- **Rivals:** uniform functions/inverses imply strong derivatives; compare norms without identifying weak components; silently evaluate a limiting measurable derivative in a different source measure; label core energy convergence an operator limit.
- **Risky consequences:** strong based Dpsi_j transport in original states, strong based 2D log psi_j transport in tilted states, core generator-value transport, full graph recovery and weak graph-limit inclusion, and strong gradients of fixed-input resolvents.
- **Strongest falsifiers:** normalized high-frequency ripples converge uniformly with bounded log-gradient but retain gradient squared norm>=4/9; equal-norm rotated vectors have wrong weak components, defect1. These are outside the actual fixed-probe source sequence, not counterexamples to it.
- **Disposition:** the written based-Hilbert and energy/IBP argument supplies these comparisons. No direct L2(nu) norm of Dpsi_j-Dpsi is asserted. Independent analytic review remains open.

## Declare the comparison before transporting vectors

For original states let H_j^vec=L2(nu_j;ell2(E x {1,2,3})), and define H^vec similarly. Common test sections are finite-component continuous cylinder fields; smooth ones are dense, also uniformly on any fixed finite component set. Scalar spaces use continuous cylinders. Common-section norms and inner products converge by weak measure convergence.

A sequence v_j is **based weakly convergent** to v if its norms are bounded and <eta,v_j>_j-><eta,v> for every common test eta. It is **based strongly convergent** if there are common sections eta_n approaching v in H^vec such that

\[
\lim_{n\to\infty}\limsup_{j\to\infty}\|v_j-\eta_n\|_j=0.
\]

These subtractions occur only WITHIN a declared source. The same definitions apply to rho_j and to scalar or graph-pair spaces. Continuous finite-component fields may replace cylinders by uniform approximation and bounded norms.

Weak convergence plus convergence of full squared norms implies this strong convergence: for every fixed common eta,

\[
\lim_j\|v_j-\eta\|_j^2
=\|v\|^2+\|\eta\|^2-2\operatorname{Re}\langle\eta,v\rangle
=\|v-\eta\|^2.
\]

Density supplies eta_n. Conversely strong convergence gives weak convergence, norm convergence, and strong/weak pairing convergence by common-section approximation. Uniformly convergent bounded continuous scalar multipliers and fixed finite-component continuous row contractions preserve strong convergence. To prove this, approximate the limiting multiplier times each fixed recovery section uniformly by common sections, and bound the remaining error by the uniform operator bound. No inner-product isometry between different original states is needed.

## Original gradients: identify components and then full norm

Put v_j=Dpsi_j in H_j^vec. For a smooth finite-component test eta, actual original-state conditional integration by parts gives

\[
\langle\eta,D\psi_j\rangle_{\nu_j}
=-\sum_{i,a}\nu_j\bigl(\psi_j[
X_{ia}\overline\eta_{ia}+\beta_{j,ia}\overline\eta_{ia}]\bigr).
\]

Only finitely many components occur. For each fixed component beta_(j,ia)->beta_ia uniformly, by the source interaction-tail comparison. Uniform psi_j convergence and weak ORIGINAL-state convergence therefore pass this identity to its infinite-source counterpart. This identifies weak v_j->Dpsi, rather than guessing derivative limits from function values.

The actual normalized eigen-equations give

\[
\kappa\|D\psi_j\|_{\nu_j}^2=E_j-\rho_j(U)
\longrightarrow E-\rho(U)=\kappa\|D\psi\|_\nu^2.
\]

The convergence uses the based tilted-state theorem and fixed continuous U. Nonnegativity comes from the energy identity, not separate scalar bounds. Weak components plus these FULL norms give strong based gradient transport. In particular, no unobserved gradient energy can escape to distant links or high modes.

The retained weighted bounds give additional explicit localization. With L=M_U/m, H=exp(2pi L), a=4/3, K a finite support for U, and L_off=M_U*(c^-1-2)/kappa, for b>=1,

\[
\|1_{d(i,K)\ge b}D\psi_j\|_{\nu_j;\ell^2}
\le H L_{\rm off}a^{-b},\qquad
\|1_{d(i,K)\ge b}D\log\psi_j\|_{\rho_j;\ell^2}
\le L_{\rm off}a^{-b}.
\]

The same inequalities hold in the limit. At R=0 these tails vanish outside K. The original beta need not be globally ell2; only the probe-induced increment is localized this way.

## Change states by the actual source multiplier, not by coordinate copying

Let r_j=D log psi_j=psi_j^-1 Dpsi_j and r=D log psi. The vector-valued J_j, multiplication by psi_j, is unitary from H_(rho_j)^vec to H_(nu_j)^vec WITHIN that source. For any fixed original recovery eta,

\[
\|r_j-\eta/\psi\|_{\rho_j}
=\|D\psi_j-(\psi_j/\psi)\eta\|_{\nu_j}.
\]

Uniform psi_j/psi->1 makes the right side have limit ||Dpsi-eta||_nu. The common continuous finite-component sections eta/psi recover r, since their limiting error in rho is exactly the original error in nu. Hence r_j->r strongly based in the TILTED states, and the same holds for the weak drift increments w_j=2r_j. This proves convergence of norms and pairings without defining a spurious cross-source difference r_j-r.

## Core values and full operator graphs

For every fixed smooth cylinder f, the established L2 generators satisfy

\[
T_jf=A_jf-2\kappa r_j\cdot Df,\qquad
Tf=Af-2\kappa r\cdot Df.
\]

The original term A_jf->Af uniformly. The gradient row Df has finite continuous components, so the module contraction lemma gives strong based T_jf->Tf in L2(rho_j). The functions f themselves are common sections. Thus (f,T_jf) converges strongly to (f,Tf) in the product Hilbert spaces. No continuous representative of Tf is required.

For any u in Dom(T), choose cylinder f_n with (f_n,Tf_n)->(u,Tu) in the limiting graph norm. There is a diagonal sequence u_j=f_(n(j)) in Dom(T_j) whose graph pairs converge strongly based to (u,Tu). Here is the quantifier discipline: fix a countable uniformly dense family of common scalar cylinder tests and a graph-core sequence. For each n choose an exhaustion threshold so the graph norm and pairings of (f_n,T_jf_n) differ from their limits by at most2^-n on the first n tests. Increase thresholds strictly and let n(j) grow only after the corresponding threshold. Norm convergence and all test pairings follow; the weak-plus-norm lemma gives strong graph recovery. This diagonal is not a universal volume rate or operator-unit-ball estimate.

There is also a weak graph-limit inclusion. If u_j and T_j u_j converge based weakly to u,h, then for every cylinder g,

\[
\langle g,h\rangle=\lim_j\langle g,T_ju_j\rangle_j
=\lim_j\langle T_jg,u_j\rangle_j=\langle Tg,u\rangle.
\]

The middle limit uses the PROVED strong core-value convergence and weak/strong pairing lemma. Since cylinders are an operator core and T is self-adjoint, u belongs to Dom(T) and Tu=h. Together with recovery this is a genuine based graph comparison, not just agreement of a finite list of energies or formal differential expressions. It restricts to the gauge-invariant cores by the established compact-group averaging.

## Fixed-input resolvent gradients

For alpha>0 and f in C(X), let z_j=(alpha+T_j)^-1 f. The already proved Feller transport, contraction and the exponentially small Laplace tail give z_j->z uniformly. Also T_jz_j=f-alpha*z_j converges uniformly, so these are graph-recovery sections. Their gradient norms satisfy

\[
\kappa\|Dz_j\|_{\rho_j}^2
=\langle z_j,f-\alpha z_j\rangle_{\rho_j}
\longrightarrow\langle z,f-\alpha z\rangle_\rho
=\kappa\|Dz\|_\rho^2.
\]

To identify weak gradient components, use the tilted integration-by-parts formula against a fixed smooth finite-component test. The beta_j term converges uniformly; the increment2r_j converges strongly based, and z_j is a uniformly convergent continuous multiplier. Thus the adjoint pairings converge to those of Dz. The weak-plus-norm lemma proves strong based Dz_j->Dz. This is for each fixed f,alpha, not operator-norm convergence of a unit ball, nor pointwise derivative convergence.

## Finite controls and executable successor

The checker freshly replays the gradient-core receipt. Six three-atom module packets use t=1/(8n), nu_t=((2-t)/8,(2+t)/8,1/2) and psi_t=(1+t,1-t,1), with EXACT nu_t(psi_t^2)=1. Two-component vectors test common recovery, the actual within-source multiplier identity, and row contraction, with squared recovery errors<=5t^2,8t^2,32t^2. These are module algebra, not gradients of SU2 eigenvectors. Eighteen norm-small continuous-circle packets check the kinetic/eigen-energy normalization. Six normalized ripple packets have uniform function/inverse convergence and bounded log-gradient but squared derivative norm>=4/9; their potentials grow, so they violate the actual fixed-probe energy hypotheses. Equal-norm rotated vector fields give weak-test defect1 and squared distance2. These finite tests do not mechanically prove the changing-state Hilbert/domain theorem.

Next executable issue: construct the STATIONARY continuous-path tilted source diffusion and finite-source weak path-law transport on C([0,S],X). Use the actual closed strongly local form/Feller kernel, uniform coordinate drift/covariance bounds for tightness, and the new strong localized drift transport to identify measurable drift integrals by stationary L2 approximation with common continuous fields. Attach the cylinder martingale and bracket2kappa*D f dot Dg in the actual source units. Finite-time words alone do not imply path-space tightness. Do not claim all-start-point regularity, strong SDE uniqueness, a classical smooth drift, physical-clock calibration or continuum reconstruction without their separate proofs.

Contract: `research/kitaev/contracts/yang-mills-probe-gradient-transport.v1.json`.
Checker: `research/kitaev/checkers/check_yang_mills_probe_gradient_transport.py`.
Receipt: `research/kitaev/results/yang-mills-probe-gradient-transport-v1.json`.
