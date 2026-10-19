# Small-probe ground-state-transformed source dynamics

## Question, source and stratum

Does the completed auxiliary eigenstate carry canonical conservative source dynamics, and do its local paired readouts survive the thermodynamic comparison?

SCC obligation: source Markov realization, same-source attachment transport and based paired-readout comparison. Retain the original spaces H=L2(nu), H_Lambda=L2(nu_Lambda), vacuum vector1, symmetric Markov semigroups P_s=exp(-sA), common full gap m=kappa*(1/2-3R), kappa>0 and0<=R<9/64. The parameter s has only its Euclidean source semigroup meaning, without a physical clock map. The coefficient C_R=max(2R/c,44 eta_R/7)<=18/5, c=1/2-3R, eta_R=R/2+(8R/9)/(1-8R/9), and a=4/3 are inherited from the actual mesh-word comparison.

For real smooth local gauge-invariant U with norm<=delta<=m/8, the existing packet gives B=A+M_U, Q_U(s)=exp(-sB), normalized nonnegative eigenvector psi, lowest eigenvalue E, overlap <1,psi>=sqrt(alpha)>=sqrt(8/9), and relative gap g>=m-2delta>=3m/4. It also constructs dnu_U=psi^2 dnu and its based finite-source weak limit. All finite-source spectral objects remain in their own original spaces, with the prescribed source exterior extension.

## Issue-boundary DPC

- **Problem:** nonnegative eigenvectors need not admit inverse multiplication, and normalizing a positive probe readout does not establish a conservative composition law.
- **Conjecture:** bounded-potential positivity plus original gap mixing forces strict almost-everywhere positivity. A fixed multiplication unitary then transports the shifted Hamiltonian, not a separately normalized readout at each parameter.
- **Named rivals:** invert a weight with zeros; omit the intrinsic eigenvalue shift; normalize each kernel row before checking semigroup sewing; infer pointwise/Feller transport from an L2 construction.
- **Risky consequences:** a canonical onto unitary within each source, a positive conservative symmetric semigroup with relative gap>=3m/4, and local paired-readout convergence uniformly on each bounded source-parameter interval.
- **Strongest falsifiers:** a zero weight loses an original-space direction of squared norm1/2; omitting the eigenvalue shift on a constant small probe loses row mass by1/2; row normalization of a genuine norm-small two-state probe has a nonzero composition residual given below.
- **Disposition:** the source operator construction and based transport below supply the claimed L2 dynamics. Feller regularity, a smooth logarithmic drift, physical calibration and continuum/root gates remain unproved.

## Strict positivity precedes inverse multiplication

The positive bounded Dyson expansion with multiplication delta-U>=0 gives, on the positive cone of H,

\[
Q_U(s)h\ge e^{-\delta s}P_s h,\qquad h\ge0.
\]

This is an order inequality, not operator monotonicity of the exponential for arbitrary self-adjoint operators. Apply it to psi, for which Q_U(s)psi=exp(-sE)psi. On D={psi=0}, P_s psi therefore vanishes almost everywhere for every fixed s. But the ORIGINAL full gap gives

\[
\|P_s\psi-\nu(\psi)1\|_H\le e^{-ms}\|\psi-\nu(\psi)1\|_H,
\qquad \nu(\psi)=\sqrt\alpha>0.
\]

If nu(D)>0 the squared left side is at least nu(D)*nu(psi)^2. Sending s=n/m to infinity contradicts mixing. Thus psi>0 nu-almost everywhere, and nu_U is equivalent to nu. No pointwise everywhere positivity or infinite Haar density is inferred.

Define J_U:L2(nu_U)->H by J_U f=psi f. It is an isometry because its norm identity is based in the declared measures. It is onto: for h in H, h/psi belongs to L2(nu_U) and maps to h. Its inverse need not be bounded multiplication on H with the original measure; it is a unitary between the two specified spaces. This unitary is a source-derived change of state within one source, not an isometry between finite and infinite original vacua.

## Preserve the operator composition law

Set

\[
\widetilde A_U=J_U^{-1}(B-E)J_U,
\quad \operatorname{Dom}(\widetilde A_U)=J_U^{-1}\operatorname{Dom}(B),
\qquad
\widetilde P_U(s)=J_U^{-1}e^{-s(B-E)}J_U.
\]

The generator is self-adjoint and nonnegative; its actual domain is retained rather than guessed from smooth cylinder coordinates. Functional calculus proves strong L2 continuity and the semigroup law. Positivity of Q_U and psi makes the semigroup positive. The eigenvector equation gives tilde P_U(s)1=1. For bounded real f with |f|<=F, order comparison with F*psi gives |tilde P_U(s)f|<=F. Symmetry and constant preservation imply invariance of nu_U. Thus this is a conservative symmetric Markov semigroup on L2(nu_U), also contracting bounded measurable observables.

The unitary sends constants to the true ground vector, so

\[
\|\widetilde P_U(s)f-\nu_U(f)1\|_{L^2(\nu_U)}
\le e^{-(m-2\delta)s}\|f-\nu_U(f)1\|_{L^2(\nu_U)}.
\]

Gauge equivariance is inherited because psi is invariant and J_U intertwines the source gauge actions. Every statement applies separately to finite sources. No Feller kernel, continuous inverse eigenfunction, smooth drift or path-space regularity has been assumed.

## Finite route falsifiers

A nonnegative weight h=(1,0) over the uniform two-state measure defines a tilted probability supported only on coordinate0. The coordinate vector(0,1) has original squared norm1/2 but no preimage under multiplication by the normalized h. Nonnegativity alone does not make J onto.

For a gap1 reset source and constant U=1/16, the ground vector is1 and E=1/16. At s=16 log2 the unshifted Q_U(s) sends1 to1/2. The missing-shift conservation residual is1/2. The correct factor exp(sE) is determined by the eigenvalue equation, not fitted to a desired row sum.

For the uniform two-state source A=[[1,-1],[-1,1]]/2 and q=1/16, put U=diag(16/255,-16/255), so norm(U)<1/8. Its ground projection is Pi=[[225,255],[255,289]]/514. Write S_z=Pi+z(I-Pi) and row-normalize K_z=diag(S_z1)^(-1)S_z. All K_z are positive and conservative for0<z<=1, but

\[
(K_{1/2}K_{1/3}-K_{1/6})_{00}
=\frac{333238023}{586794978}-\frac{1639}{2914}>0.
\]

The parameters correspond to s=log2/g and t=log3/g for the actual relative gap g. Removing the common exp(-sE) factor does not affect row normalization. This counterexample lies in the norm-small reversible multiplication class and rejects readout normalization as a substitute for source composition.

## Based paired-readout transport

For smooth real gauge-invariant local f,g with norms<=F,G, retain multiplication operators and define

\[
\widetilde C_U(s;f,g)
=\langle f,\widetilde P_U(s)g\rangle_{\nu_U}
=\langle\psi f,e^{-s(B-E)}\psi g\rangle_\nu.
\]

The comparison topology here is these paired readouts, uniformly for s in each fixed[0,S]. It is not cross-source operator-norm or pointwise transport. Since exp(-s(B-E)) is an H contraction, replacing BOTH endpoint vectors by the previous normalized filter h_T has error at most FG*exp(-3mT/4), uniformly for all s>=0 in each source separately.

Put V=U+delta>=0. The filtered pairing is

\[
e^{s(E+\delta)}\frac{N_{T,s}(f,g)}{D_T},\qquad
N_{T,s}=\langle1,Q_V(T)M_fQ_V(s)M_gQ_V(T)1\rangle_\nu,
\quad D_T=Z_V(2T).
\]

The full sandwich has D_T>=exp(-4delta T), |N_(T,s)|<=FG D_T, and total insertion-gradient budget (2T+s)M(U)FG+G M(f)+F M(g). The numerator domination follows from H contraction of Q_V(s), not independence of the endpoint factors. Based mesh-word comparison and the positive quotient bound consequently give, with K the union of the three supports and b=d(K,Lambda complement),

\[
|\widetilde C_{\Lambda,U}(s;f,g)-\widetilde C_U(s;f,g)|
\le2FG e^{-3mT/4}
+e^{2\delta S}\left\{C_Re^{4\delta T}
[(4T+S)M(U)FG+G M(f)+F M(g)]a^{-b}
+SFG|E_\Lambda-E|\right\},\quad0\le s\le S.
\]

The final term is necessary: the shifted finite-source eigenvalue cannot simply be replaced by E. Use the previous pressure comparison with an independent parameter tau>0,

\[
|E_\Lambda-E|\le1/(8\tau)+C_RM(U)e^{2\delta\tau}a^{-b}.
\]

For fixed T,tau the based spatial comparisons tend to zero; then sending both completion parameters to infinity proves the stated local paired-readout convergence. Uniform approximation extends it to continuous gauge-invariant cylinder observables and their uniform closure. No independent gauge averaging of two noninvariant factors is used.

For a rational joint budget with delta>0 choose T=n/m, tau=n/(8delta), b>=4n, and k=ceil(4delta S). Using exp(2delta S)<=2^k gives the sufficient envelope

\[
2FG(4/7)^n+2^k\left\{
C_R[(4n/m+S)M(U)FG+G M(f)+F M(g)](81/128)^n
+SFG[\delta/n+C_RM(U)(27/64)^n]\right\}.
\]

It tends to0 for each fixed horizon and budgets. Whole-window planning uses m_lower=5kappa/64 with delta<=m_lower/8. At R=0 paired local readouts agree exactly after including all supports. For constant U the construction is the original P_s and the original mesh-word bound C_R[G M(f)+F M(g)]a^(-b) applies, without a filter or phase cost. Constant f,g and zero-norm factors are exact cases.

## Checks and remaining regularity constructor

The checker replays the eigenstate receipt and preregisters108 exact reversible transformed kernels,972 filtered paired readouts,192 rational transport budgets and the three falsifiers. These finite controls are not SU2 dynamics; independent review of the source analysis remains open.

Next executable issue: derive a volume/parameter-uniform weighted gradient estimate for log(Q_U(T)1) from the actual finite-source Hamilton-Jacobi/Bochner equation, using the existing positive gradient matrix. Use source compactness and full support to determine whether psi has a positive quasilocal continuous representative and whether the transformed semigroup has a Feller realization. The present L2 construction supplies neither conclusion. This is a source regularity problem with executable estimates, not a request for a missing external map. It does not replace the original magnetic vacuum or discharge continuum/root gates.

Contract: `research/kitaev/contracts/yang-mills-probe-doob.v1.json`.
Checker: `research/kitaev/checkers/check_yang_mills_probe_doob.py`.
Receipt: `research/kitaev/results/yang-mills-probe-doob-v1.json`.
