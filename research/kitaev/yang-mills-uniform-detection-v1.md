# Iteration 10 — uniform detection on the actual small-coupling finite source

## Question, theorem and disposition

Do iteration 9's actual-density interaction bounds imply a volume-independent physical excitation detector inequality, with metric, domains and source quantifiers checked?

**Constructed:** for the existing SU(2) finite open-box Hamiltonians, with kappa>0 fixed in declared source units and

\[
0\le r=\lambda/\kappa<27/262144,
\]

the actual-vacuum detector satisfies on the whole physical form domain

\[
\boxed{\|D_\Omega\psi\|^2\ge\frac5{64}
\|(I-P_\Omega)\psi\|^2.}
\]

Together with the already proved exact form identity, this gives the finite-source spectral estimate Delta>=5 kappa/64 uniformly over finite spatial boxes. `faithful-excitation-detection` is constructed at this explicit regime and scope.

**Not constructed:** a continuum theory, the weak-coupling scaling route, a fixed-physical-unit completion bound, or the official Yang–Mills target. `uniform-energy-cost` remains open at its physical-units/refinement scope, despite the exact source-unit energy identity.

[Contract](contracts/yang-mills-uniform-detection.v1.json). This theorem is for the actual density from iteration 9, not exp(T2), an arbitrary positive fixture, or a separately chosen gapped operator. Its analytic ingredients and exact checks are not a proof-assistant or independent target-scope review.

## Metric normalization before applying geometry

For SU(2), let T_a=e_a/2 be the left invariant generators used throughout the Casimir calculations. Declare them orthonormal. Their brackets satisfy [T_a,T_b]=epsilon_abc T_c. A bi-invariant metric has sectional curvature one quarter the squared bracket norm, hence sectional curvature1/4 and Ricci curvature1/2 in dimension three. This is the round three-sphere of radius2, not radius1.

The positive single-link Laplacian has eigenvalue j(j+1), with first nonconstant value3/4. It is consistent with a Ricci lower bound1/2. Importing radius-one Ricci2 without changing the electric generator would be wrong: it would already predict a kinematic Poincare constant larger than3/4 at zero potential. The exact controls include this hostile.

On the product M=SU(2)^E, equipped with its product metric, Ricci is still bounded below by one half times the metric, independently of E. No quotient geometry is invoked: the orbit space has stabilizer strata, so a smooth free-quotient curvature formula would not be justified.

## The actual interaction norm controls the full Hessian

Iteration 9 constructs u=log Omega modulo constants as a sum of invariant interactions Phi_A, with

\[
N_2(\Phi)=\sup_e\sum_{A\ni e}2^{|A|}W(\Phi_A)
\le R:=4096r/3.
\]

Here W uses weight1+C_pi and C_pi=sum j_e(j_e+1). This also controls second derivatives: each representation generator has norm j_e. For distinct edges the covariant Hessian entry is the ordinary mixed left derivative. On one edge, the bi-invariant connection gives the symmetrized second derivative, since the connection term cancels half the commutator. Therefore

\[
|\operatorname{Hess}_{ea,fb}\Phi_A|
\le\sum_\pi j_ej_f d_\pi\|\widehat\Phi_A(\pi)\|_{trace}.
\]

The bound applies to equal indices too. If n=|A| and J_pi=sum over that support, then

\[
j_eJ_\pi\le\frac{n+1}2\sum_fj_f^2
\le\frac{n+1}2 C_\pi.
\]

Sum the Hessian entry bounds over the three Lie directions on every other edge. The absolute row sum is at most3(n+1)W(Phi_A)/2. Only interactions whose label contains the row's edge contribute. Using (n+1)/2^n<=1 for n>=1 gives

\[
\sup_{e,a}\sum_{f,b}|\operatorname{Hess}_{ea,fb}u|
\le\frac32R.
\]

The real Hessian is symmetric. Its operator norm is bounded by the maximal absolute row sum, so

\[
\|\operatorname{Hess}\log\rho\|_{op}
=2\|\operatorname{Hess}u\|_{op}\le3R.
\]

The normalization constant in rho=Omega squared/<Omega squared> has no derivatives. Absolute Fourier derivative convergence justifies these estimates on each finite graph. Its actual ground function is smooth by the earlier elliptic construction; the bounds themselves are uniform in the number of links.

Consequently the weighted curvature is bounded below by

\[
\operatorname{Ric}-\operatorname{Hess}\log\rho
\ge(1/2-3R)g\ge(1/2-4096r)g>\frac5{64}g.
\]

The last strict inequality follows from r<27/262144:4096r<27/64. A uniform non-strict lower bound5/64 is therefore valid throughout the admitted open regime.

## Derive the functional inequality, rather than naming it

Let nu=rho mu be the actual ground probability measure. Its symmetric diffusion generator is

\[
\mathcal G=\Delta+\nabla\log\rho\cdot\nabla,
\qquad -\int f\mathcal G f\,d\nu=\int|\nabla f|^2d\nu.
\]

For a smooth real function the weighted Bochner identity is

\[
\Gamma_2(f)=\|\operatorname{Hess}f\|^2+
(\operatorname{Ric}-\operatorname{Hess}\log\rho)(\nabla f,\nabla f).
\]

Thus Gamma2>=c Gamma with c=5/64. Along its heat semigroup T_t, integration by parts gives

\[
\frac d{dt}\int|\nabla T_tf|^2d\nu
=-2\int\Gamma_2(T_tf)d\nu
\le-2c\int|\nabla T_tf|^2d\nu.
\]

The energy decays at least as exp(-2ct). Connectedness, strict positivity of the smooth density, and the compact elliptic generator identify the invariant functions as constants and give convergence of T_t f to its mean. This finite-graph ergodicity argument does not presume a uniform gap. Integrating the variance dissipation identity yields

\[
\operatorname{Var}_\nu f
=2\int_0^\infty\int|\nabla T_tf|^2d\nu dt
\le\frac1c\int|\nabla f|^2d\nu.
\]

Apply separately to real and imaginary parts and then close the smooth core in H1. This proves the actual weighted Poincare inequality. Compact-group Riemannian geometry, weighted Bochner and elliptic semigroup facts are imported standard analytic inputs; their normalizations and application are shown here rather than treated as an unspecified tensorization premise.

## Descend to the physical detector and shifted form

Restrict to gauge-invariant f and set psi=Omega f using the correctly normalized actual ground function. The previously constructed quotient unitary and horizontal covariant target give

\[
\operatorname{Var}_\nu f=\|(I-P_\Omega)\psi\|^2,
\qquad\int|\nabla f|^2d\nu=\|D_\Omega\psi\|^2.
\]

The inequality holds on the whole physical form domain, not just the polynomial packets or sampled coefficients. No gauge direction is counted as an excitation; the full-product theorem simply restricts to the invariant subspace. The source identity

\[
q_{H-E_0}(\psi)=\kappa\|D_\Omega\psi\|^2
\]

therefore implies Delta>=5 kappa/64. The parameter-sensitive bound kappa(1/2-4096r) is also available. The estimate is conservative and not a claim of the exact magnetic spectrum.

## Two explicit boundaries against promotion

1. Under the declared convention kappa=g squared/(2a), lambda=2/(a g squared), the ratio is r=4/g fourth. The theorem requires g fourth>1048576/27. It is an electric-dominant/strong-bare-coupling result and does not cover g tending to zero. No assertion is made that the actual gap closes outside this sufficient regime.
2. A source-unit bound does not control physical units along refinement. Taking kappa_N=1/N and lambda_N=r kappa_N leaves the same dimensionless detector constant but scales every fixed-graph energy by1/N. A physical conversion factor and a compatible refinement trajectory must be supplied before closing `uniform-energy-cost` at its declared scope. At fixed source kappa, volume uniformity is genuine; it is not a continuum reconstruction theorem.

No nontrivial infinite-volume correlation state has been assembled, no simultaneous time/space continuum limit taken, and no equivalence to the official axiomatic target reviewed. The optional atomic source is still unselected.

## Exact controls, disposition and continuation

The checker verifies quaternion Lie-bracket/metric constants, exact single-link character energies, the Hessian row inequalities on spin data, support-moment bounds and the rational curvature margin. A smooth positive density fixture with a negative weighted-curvature direction rejects the shortcut 'positive density implies positive weighted curvature'; it is explicitly not the source ground state. Source identification comes from iteration9's analytic constructor.

Exact controls and the written all-domain proof are distinct. This is not new machine-kernel closure or independent scientific review. All predecessor receipts and pins are retained.

`faithful-excitation-detection` is now constructed in the stated uniform finite-source regime. Newly ready: `uniform-energy-cost`; also ready remain `continuum-correlation-construction` and independent `atomic-source-selection`.

**Next nonredundant operations:** construct compatible thermodynamic vacuum correlations from the local interaction family and establish a declared physical energy/refinement route. Neither follows automatically from a uniform finite-source gap. The conjecture net's root existence, reconstruction, completion and reviewed assembly outcomes remain open.

Reproduce: `python research/kitaev/checkers/check_yang_mills_uniform_detection.py`.
Receipt: `research/kitaev/results/yang-mills-uniform-detection-v1.json`.
