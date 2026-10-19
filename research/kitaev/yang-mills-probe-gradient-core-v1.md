# Actual tilted gradient form, operator core and weak logarithmic drift

## Source and question

Iteration9/100 addresses `small-probe-gradient-form-core:v1`. Is the conservative small-probe transform the closure of the ACTUAL tilted cylinder gradient operator, rather than just an abstract unitary semigroup with matching cylinder energies?

Keep X=SU(2)^E, radius-two link geometry, kappa>0,0<=R<9/64,c=1/2-3R,m=kappa*c and real smooth gauge-invariant local U with ||U||<=delta<=m/8. All parameters and rates are source units. In each ORIGINAL source let H_0=L2(nu), D be the closed source cylinder gradient, V=Dom(D), q(f,g)=kappa<Df,Dg>, and A its nonnegative self-adjoint generator. The propagator-comparison packet proves that smooth cylinders C are an OPERATOR core for A, not only a form core.

The preceding packets supply (A+U)psi=E psi, nu(psi^2)=1, and the positive continuous representative

\[
H^{-1}\le\psi\le H,\qquad
\sum_i(4/3)^{d(i,K)}\operatorname{Lip}_i(\log\psi)\le L:=M_U/m,
\quad H=\exp(2\pi L).
\]

Here K is a finite support set for U; M_U=sum_i||gradient_i U||_infinity. The actual tilted probability is nu_U=psi^2 nu and Jf=psi f is unitary from H_U=L2(nu_U) to H_0. The previously constructed generator is T=J^-1(A+U-E)J. This packet identifies its form, domain and core. Same-set comparisons below use the bounded identity H_U<->H_0, NOT an inner-product isometry. No finite/infinite original-Hilbert coordinate copying is introduced.

## Issue-boundary DPC

- **Problem:** the multiplier is continuous and positive, but neither a weighted gradient domain nor a cylinder operator core follows from that alone.
- **Conjecture:** source weak derivatives and the log-Lipschitz bound make psi and its inverse form-domain isomorphisms. The eigen-equation cancels all zeroth-order terms. The resulting weak drift is infinitesimally A-bounded, giving a full resolvent range and excluding a hidden extension.
- **Rivals:** bounded continuous multiplication preserves Sobolev domains automatically; ignore the logarithmic drift; identify an operator by its cylinder energies alone; invoke self-adjoint perturbation in the WRONG measure.
- **Risky consequences:** equality of full form domains, cylinder form AND L2 operator cores, equality of operator domains as function sets under bounded measure comparison, and the actual source weak drift beta+2D log psi.
- **Strongest falsifiers:** a positive bounded cusp multiplier sends1 outside H1; omitting the drift changes a norm-small continuous-circle energy by1/1026; an unresolved range defect would invalidate the operator-domain conclusion even after the form calculation.
- **Disposition:** the written weak-gradient/multiplier and Neumann-range proofs below supply these L2 claims. Classical smooth drift and a C(X) generator cylinder core remain separate. Independent analytic review remains open.

## Weak derivatives, before using a product rule

The spectral eigenvector belongs to Dom(A), hence V. The closed D is identified with weak one-link derivatives by the original conditional integration-by-parts formula. Each finite-link conditional density is positive C1 with logarithmic derivative beta_i; this does NOT require a global density of nu relative to product Haar.

On each link fiber the continuous psi and log psi are Lipschitz. Finite-dimensional Rademacher and conditional Haar integration by parts identify their fiber gradients with the corresponding closed-gradient components, by testing against finite-component smooth cylinder fields. There are only countably many components. Smooth scalar extensions of log and inverse from[H^-1,H] give the closed chain rules, so

\[
D\log\psi=\psi^{-1}D\psi,\qquad
D(\psi^{-1})=-\psi^{-1}D\log\psi,
\qquad
\|D\log\psi\|_{L^\infty(\nu;\ell^2)}\le L.
\]

The last bound uses the retained sum of BLOCK Lipschitz constants, not three times that sum. Consequently both ||Dpsi||_(infinity;ell2) and ||D(psi^-1)||_(infinity;ell2) are at most H L.

For completeness, the product rule is obtained from the closed source derivation, not postulated on arbitrary functions. Smooth bounded scalar truncations of graph-core sequences give uniformly bounded core approximants for bounded real members of V. The scalar chain rule follows by closedness and dominated convergence of the derivatives. Products of two such bounded sequences converge in the gradient graph norm, yielding D(fg)=f Dg+g Df for bounded V members. Truncate a general f in V, then use the L-infinity bound on Dpsi to pass psi*f through the graph closure. Real/imaginary decomposition gives the complex version. Thus multiplication by psi and psi^-1 are inverse bounded maps V->V, with, for example,

\[
\|D(\psi f)\|_2\le H\|Df\|_2+HL\|f\|_2.
\]

No multiplication claim is made for an arbitrary merely positive continuous function.

## Identify the entire closed form

Define on C the actual weighted cylinder form q_(U,0)(f,g)=kappa*nu_U(D conjugate(f) dot Dg). Since H^-2 nu<=nu_U<=H^2 nu, its form norm is equivalent to the original gradient form norm. It is closable, its closure q_U has domain V as a set of functions, and C is a form core.

The form of T has domain J^-1 V=V by the multiplier result. On cylinders use the weak eigen-equation against the legitimate V test psi*conjugate(f)*g:

\[
q(\psi,\psi\overline f g)+\nu((U-E)\psi^2\overline f g)=0.
\]

The product rule therefore gives the exact identity

\[
q(\psi f,\psi g)+\nu((U-E)\psi^2\overline f g)
=\kappa\nu(\psi^2D\overline f\cdot Dg).
\]

Both forms are closed on V and C is a core there (bounded U-E does not change the original form norm). Hence their closures agree: q_U is the full form of T, not just its cylinder restriction. Its constant kernel and gap>=m-2delta>=3m/4 are the already established SAME-SOURCE spectral assertions, now attached to the weighted gradient form. No curvature bound for the new drift is assumed.

## Conditional weak drift and the L2 cylinder operator

The tilted conditional density is the original conditional density times psi^2, divided by a normalizer independent of the integrated link. Fiber weak integration by parts gives

\[
\nu_U(\overline g X_{ia}f)
=-\nu_U\bigl((X_{ia}\overline g+
[\beta_{ia}+2X_{ia}\log\psi]\overline g)f\bigr).
\]

Thus beta_U=beta+2D log psi is the ACTUAL weak logarithmic drift. Its increment satisfies weighted block L-infinity sum<=2M_U/m; the predecessor's off-support improvement gives<=2M_U(c^-1-2)/kappa outside K. The original beta need not be globally ell2; only this localized increment is claimed to be so.

For f in C set

\[
S f=A f-2\kappa D\log\psi\cdot Df=:A f+Kf.
\]

This is an H_U function even if the weak drift has no continuous representative. Integration by parts and the established form core put f in Dom(T), with Tf=Sf. This does NOT yet identify an operator core.

## Full range excludes an unobserved closed extension

Use H_0 for estimates: A is self-adjoint there, whereas K need NOT be symmetric there. For f in Dom(A),

\[
\|Kf\|_{H_0}\le2\sqrt\kappa L\|A^{1/2}f\|_{H_0}
\le\eta\|Af\|_{H_0}+\frac{\kappa L^2}{\eta}\|f\|_{H_0}.
\]

It follows that S=A+K on Dom(A) is closed, with its graph norm equivalent to A's graph norm, and C is an operator core for S. Equivalence of H_0 and H_U norms transfers this closedness/core statement under the bounded identity, without falsely asserting symmetry in H_0.

More importantly the spectral theorem gives

\[
\|K(\alpha+A)^{-1}\|_{H_0\to H_0}
\le\sqrt{\kappa/\alpha}\,L.
\]

Choose alpha=kappa*(1+4L^2). The squared bound is L^2/(1+4L^2)<1/4. The factorization

\[
\alpha+S=\bigl[I+K(\alpha+A)^{-1}\bigr](\alpha+A)
\]

has a bounded Neumann inverse and FULL range, also in the equivalent H_U space. T is a closed extension of S because it extends its cylinder core. For v in Dom(T), solve (alpha+S)u=(alpha+T)v; then injectivity of alpha+T gives v=u. Therefore

\[
\operatorname{Dom}(T)=\operatorname{Dom}(A)\quad
\text{as function sets under bounded measure comparison},\qquad
T=A-2\kappa D\log\psi\cdot D,
\]

and smooth cylinders are an L2(nu_U) operator core. This is a range/graph proof, not an inference from matching energies. It also proves that multiplication by psi and its inverse preserve Dom(A). Gauge averaging yields the corresponding invariant form/operator cores; it uses compact-group averaging of the established cores and commutation with the actual generators, not quotient-space differentiability.

The Feller generator is the C(X) part of this consistent L2 generator, with its already specified conjugated domain. A cylinder L2 generator value may only be measurable, so a C(X) cylinder core or classical smooth log drift has NOT been proved.

## Exact controls and next constructor

The checker freshly replays the quasilocal predecessor. A continuous-circle analogue has A=-kappa*partial_theta^2, raw positive psi=1+epsilon*cos(theta), E=0, U=-Apsi/psi and normalization1+epsilon^2/2. For epsilon<=1/16 its potential norm<=kappa/15<kappa/8. Rational Fourier coefficients verify the weak eigenfunction cancellation, weighted integration by parts and ground-state form identity on192 parameter/Laurent-test packets. At kappa=1,epsilon=1/16 and f=cos(theta), omission of the weak drift changes the energy by1/1026. The same model has <1,A cos>_(nu_U)-<A1,cos>_(nu_U)=32/513: the original A is not symmetric in the tilted measure. These are NOT SU2 source eigenfunctions.

On[0,1] w=1+x^(1/4) has1<=w<=2 and bounded inverse, but integral_(1/N^2)^1 |w'|^2 dx=(N-1)/8. Thus w*1 is not in H1; normalization does not repair this failure. Six exact cuts retain this hostile. Rational spectral/Young envelopes check the Neumann bound and graph inequalities; they do not mechanically prove the infinite-dimensional domain argument.

Next executable issue: transport the localized weak drift IN GRADIENT NORM across the actual changing finite-source states, then construct operator-graph recovery on the proved core. Uniform psi/inverse convergence alone does not control derivatives. Use the exact eigen-energy identity kappa*nu_Lambda(|Dpsi_Lambda|^2)=E_Lambda-nu_(Lambda,U)(U), original conditional integration by parts for weak component transport, and retained weighted tails. Specify varying-Hilbert gradient convergence through based finite-component tests plus norms, not coordinate copying. This is a new gradient/operator comparison cell beyond the already proved fixed-input Feller transport.

Contract: `research/kitaev/contracts/yang-mills-probe-gradient-core.v1.json`.
Checker: `research/kitaev/checkers/check_yang_mills_probe_gradient_core.py`.
Receipt: `research/kitaev/results/yang-mills-probe-gradient-core-v1.json`.
