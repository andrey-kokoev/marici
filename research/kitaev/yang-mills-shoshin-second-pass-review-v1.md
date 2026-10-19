# Shoshin second-pass brief: audit the actual localization and domain arguments

This document is self-contained and intended to be forwarded verbatim to a reviewer WITHOUT project read/write access. Local paths at the end are provenance only, not required reading. Status: prepared for external handoff; not dispatched and not independently accepted.

## Assignment and correction to the first brief

Thank you for the first literature audit. Its divergent physical-gap calculation is accepted as a useful CONDITIONAL obstruction. Its caution that continuous Hilbert-Schmidt derivatives do not imply generator-domain membership is also correct.

However, the first brief omitted an existing weighted block-ell1 estimate, and summarized away the existing graph-range and generator-extension arguments. Please audit the arguments below, rather than assume these conclusions were obtained just from an L2 gap or Hilbert-Schmidt regularity.

Return a verdict for EACH of review units R1-R4: valid under listed inputs; valid after an explicit additional verification; a new lemma is required; or false, with a counterexample/first failed implication. Do not treat our descriptions as certified proofs. If an input is itself unproved, identify that dependency explicitly. Prefer the first precise failure over a generic demand for more regularity.

All claims below are written candidates. No finite regression suite independently certifies them. Your cited bibliography remains supplied literature evidence, not bibliography independently checked by our project session.

## Common source and notation

Spatial links are those of Z3, with SU(2) variables, independent orientations and inverse variables on reversed links. Finite graphs are induced open cubic boxes. All vertices obey Gauss invariance and there are no external charges.

The source Hamiltonian on gauge-invariant product-Haar L2 is

H_Lambda=kappa*sum_e(-Delta_e)+lambda*sum_p(1-(1/2)Tr W_p).

Invariant orthonormal frames satisfy [X_a,X_b]=epsilon_(abc)X_c. The metric is the radius-two round S3: Ric=1/2 and positive Casimir j(j+1). Let Omega_Lambda be the normalized strictly positive actual ground function. The actual state is nu_Lambda=Omega_Lambda^2*Haar and its ground-transformed positive generator is A_Lambda. The Markov sign is -A_Lambda.

Assume the source-specific connected expansion has been proved with retained connected labels and anchored absolute Fourier C2 control:

N2(Phi)=sup_e sum_(A containing e)2^|A| W(Phi_A)<=R,
R=4096(lambda/kappa)/3<9/64.

A label is not compressed when its resulting function happens to depend on fewer variables. Its exact restriction is label deletion, not taking probability marginals. This input identifies the finite densities as Z_Lambda^-1 exp(2 sum_(A subset Lambda)Phi_A)*Haar. Its proof and numerical norm constants are NOT supplied here; please keep them conditional.

The infinite configuration space X=SU(2)^E is compact metrizable. Let d(i,j) be the link metric joining links sharing a plaquette; finite metric balls are finite. Set a0=4/3 (this is a spatial weight, NOT lattice spacing), c=1/2-3R and m=kappa*c.

The local log-density derivatives beta_i=D_i(2 sum Phi_A) are continuous bounded fields. Assume there is one symmetric nonnegative derivative majorant h, dominating all finite and limiting covariant Hessian blocks of the log density, with BOTH weighted rows and columns bounded:

sup_i sum_j a0^d(i,j) h_ij<=3R.

The same holds for finite majorants. This is a Hessian/DRIFT majorant, not the Dobrushin matrix of conditional-law influences. Also assume actual boundary drift discrepancies obey

||beta_(Gamma,i)-beta_(Lambda,i)||_infinity<=2R*a0^-d(i,Lambda^c)

inside Lambda, and fixed-component uniform recovery in the limit. No global ell2 norm of beta_Lambda-beta is asserted.

The actual original states, extended by exterior Haar, converge weakly to a unique full-support state nu. Distinct Hilbert measures are not identified. Exterior source processes are independently Brownian; inside each box the dynamics is unchanged.

Fix a smooth real gauge-invariant U supported in a finite K, with ||U||<=delta<=m/8. Let M_U=sum_i||D_i U||_infinity, L=M_U/m and g=m-2delta>0. Bounded perturbation gives a positive normalized lowest eigenvector psi_Lambda of A_Lambda+U and psi of A+U in their OWN L2 spaces, eigenvalues E_Lambda,E in[-delta,delta], and relative gap at least g. Based spectral filtering and weak convergence of tilted states psi_Lambda^2 nu_Lambda to psi^2 nu are separate assumed earlier inputs.

Crucially, neither L2 eigenvectors nor their gaps are used alone to claim continuous representatives.

## R1. Weighted log-filter localization and uniform ground-vector completion

For each finite smooth retained truncation put q_Lambda(T)=exp[-T(A_Lambda+U)]1 and F_Lambda(T)=log q_Lambda(T). Positivity gives exp(-delta T)<=q<=exp(delta T).

With L0_Lambda=-A_Lambda=kappa*Delta+kappa*beta_Lambda dot D,

partial_T F=L0_Lambda F+kappa*|DF|^2-U, F(0)=0.

All Hessians in this argument are Levi-Civita covariant Hessians. Their scalar symmetry gives, for every block i,

< D_i F, D_i sum_j |D_j F|^2 >
=2 sum_j <D_j F,D_j(|D_i F|^2/2)>.

Thus the nonlinear term becomes common advection by2kappa*DF. It is not estimated as an extra uncontrolled zeroth-order Hess(F) term. With gamma_i=|D_i F| and u_i=||D_i U||_infinity, the proposed Kato inequality is

(partial_T-L0_Lambda-2kappa*DF dot D)gamma_i
<=-kappa*gamma_i/2+kappa*sum_j h_(Lambda,ij)*gamma_j+u_i.

Regularize the norm at zero. A spatially constant cooperative supersolution eliminates the advective term, giving

||D_i F_Lambda(T)||_infinity
<=integral_0^T [exp(-kappa*s/2)*exp(kappa*s*h_Lambda)u]_i ds.

The weighted COLUMN bound yields

sum_i a0^d(i,K)||D_i F_Lambda(T)||_infinity
<=((1-exp(-mT))/m)*M_U<=L.

Only the finite smooth truncations are differentiated. For completed C2 coefficients, approximate by retained harmonic truncations preserving these bounds; finite-dimensional diffusion and bounded-potential stability give uniform q convergence on bounded T intervals. Coordinate Lipschitz bounds pass by lower semicontinuity. No D3 bound is assumed.

For normalized h_(Lambda,T)=q_Lambda(T)/||q_Lambda(T)||_(L2(nu_Lambda)), the same log-gradient bound holds. Since each link has geodesic diameter2pi, it implies osc(log h)<=2pi L, and hence H^-1<=h<=H with H=exp(2pi L). This uses the block-ell1 estimate, NOT just an ell2 gradient bound.

The weighted estimate gives uniform tails outside finite neighborhoods of K and thus equicontinuity on compact X. Arzela-Ascoli gives precompactness in C(X). For the infinite source, L2 convergence of the filters to psi identifies every uniform cluster point with the same L2 vector; full support identifies its continuous representative uniquely. For finite-to-infinite vectors, combine uniform cluster points with weak actual-state and tilted-state convergence: chi^2 nu=psi^2 nu, then positivity and full support give chi=psi. Thus the claimed completion is psi_Lambda->psi and inverse convergence uniformly on X.

At this stage only coordinate Lipschitz regularity is asserted. R3 below identifies actual continuous gradients. Once that identification is valid, the preceding estimate becomes

sum_i a0^d(i,K)||D_i log psi_Lambda||_infinity<=L.

In particular, your proposed target already follows, with sigma=log(a0):

sup_Lambda sup_x sum_i exp(2sigma*d(i,K))|D_i log psi_Lambda(x)|^2<=L^2.

**Please audit:** the Kato/common-advection calculation, approximation preserving the majorant, and both compactness/identification limits. If valid, do not list weighted localization as an absent object. Distinguish failure of its source Hessian input from failure of this conditional argument.

## R2. Scalar operator core by graph-range recovery, then tilted Banach range

### Original scalar generator

For a smooth cylinder f supported in K, assume the finite one-form comparison gives

sum_i a0^d(i,K)||D_i P_t^Lambda f||_infinity
<=exp(3kappa R t)*M(f),
M(f)=sum_i||D_i f||_infinity.

Duhamel with the boundary drift bound yields

||P_t^Gamma f-P_t^Lambda f||_infinity
<=(2/3)(exp(3kappa R t)-1)*a0^-d(K,Lambda^c)*M(f).

Contraction and cylinder density construct a C0 Feller limit P_t on C(X). Its symmetry/invariance in nu identify a symmetric L2 semigroup separately. For a cylinder f the generator integral identity passes to the limit, with

L0 f=kappa*sum_i(Delta_i f+beta_i dot D_i f).

For alpha>3kappa R define u_Lambda=(alpha-L0_Lambda)^-1 f. Then u_Lambda converges uniformly to the actual limiting Feller resolvent applied to f, and

||(alpha-L0)u_Lambda-f||_infinity
<= [2kappa R/(alpha-3kappa R)]*a0^-d(K,Lambda^c)*M(f).

Each u_Lambda depends only on its finite box. With C2 completed coefficients it need not be C-infinity: finite-dimensional elliptic regularity gives C2 regularity; approximate on that finite compact product in C2 by smooth functions, choosing errors small enough for the uniform generator graph residual. No bound uniform in the number of smoothing coordinates is needed. The approximants are smooth CYLINDERS.

Thus the cylinder closure has resolvent range dense in C(X), not just agreement of local energies. This is the claimed C(X) operator core for the original positive generator A_C. The L2 core and equality with the closed gradient form are obtained through the corresponding graph recovery and integration by parts.

### Tilted scalar generator

R1 gives the actual Feller similarity

P_(U,t)f=exp(tE)*psi^-1 exp[-t(A_C+U)](psi*f).

R3 below supplies r=D log psi in B=C(X;ell2). Scalar reverse Poincare and closure of the gradient give

||D(alpha+A_C)^-1||_(C->B)<=sqrt(pi/(2kappa alpha)).

Set Kf=-2kappa*r dot Df on D(A_C). Then

||K(alpha+A_C)^-1||<=sqrt(2pi*kappa/alpha)*L ->0.

The proposed operator S=A_C+K on D(A_C) is closed with equivalent graph norm, has the original cylinder core and full alpha-resolvent range for large alpha.

To identify the actual positive tilted Feller generator T_C, use its consistent L2 realization T: cylinders have Tf=A f-2kappa*r dot Df with continuous right side. Apply the Feller resolvent to (alpha+T)f; L2 consistency identifies its value with f and full support identifies the two continuous versions. Hence T_C extends the cylinder operator and, by closedness, S. Surjectivity of alpha+S and injectivity of alpha+T_C imply D(T_C)=D(S).

**Please audit:** each range/extension step, the use of consistency, and the finite smoothing. We are not inferring an operator core from a form core or from HS regularity. A proof using either shortcut would be invalid.

## R3. One-form semigroup, actual generator domain and continuous second derivative

The construction order matters: the one-form semigroup is first built from finite original paths, NOT defined by a presumed infinite differential expression.

Use inverse Levi-Civita stochastic parallel transport on each fixed link, with Ricci factor exp(-kappa*t/2), to define connection semigroups S_t^Lambda on B=C(X;ell2). Fixed-link finite-path/parallel-transport stability and density of finite-output cylinder fields give strong convergence in B on bounded t intervals. The limiting S_t is C0 and has norm<=exp(-kappa*t/2).

Let M_Lambda=kappa*Hess V_Lambda, where V_Lambda is the log density. Weighted rows/columns bound its multiplier norm by3kappa R. Entrywise uniform convergence plus weighted COLUMN tails gives M_Lambda F->MF in B first for finite-output fields and then for all F by density and uniform bounds. This is strong convergence of bounded operators ON B, not merely pointwise convergence at each x, and not global operator-norm convergence.

Bounded perturbation/Dyson series constructs H_t and H_(U,t), limits of the corresponding actual finite one-form semigroups, with

||H_t||<=exp(-mt), ||H_(U,t)||<=exp[-(m-delta)t].

Finite differentiated semigroup identities, smooth truncations and closed fibre differentiation give DP_t f=H_t Df. For the finite ground vectors,

Dpsi_Lambda=-integral_0^infinity exp(tE_Lambda)H_(Lambda,U,t)(psi_Lambda DU)dt.

Uniform ground-vector convergence, strong one-form convergence, and the common exp(-g*t) integral bound yield convergence in B to v. Integration along one-link curves identifies v=Dpsi. Consequently r_Lambda->r in B, and the R1 weighted Lipschitz bound applies to these actual derivatives.

### The vector Banach argument

Let P_t^B act componentwise; write -A_B for its generator. Finite-output smooth cylinder fields are claimed to be an operator core because output projections commute with the semigroup and approximate both F and A_B F uniformly, while R2 supplies the scalar core.

Trace the scalar reverse-Poincare variance inequality over output components:

||partial P_t^B F||_(C(HS))^2
<=(P_t|F|^2-|P_t^B F|^2)/(2kappa t)
<=||F||_B^2/(2kappa t).

Thus ||partial(alpha+A_B)^-1||<=sqrt(pi/(2kappa alpha)). There is no spatial-volume factor.

With C_a z=(1/2)e_a cross z, the flat-frame expression of the connection generator on the cylinder core is

-A_B+J+Z0,
(JF)_i=2kappa*sum_a C_a X_(ia)F_i,
(Z0F)_i=kappa*C(beta_i)F_i-kappa*F_i.

The -kappa term includes both connection-square and Ricci contributions. The actual semigroup exp(tE)H_(U,t) has generator G extending the proposed cylinder expression

G0=-A_B+J+Z,
Z=Z0+M-U+E.

Use ||JF||<=sqrt(3)*kappa*||partial F||_(C(HS)) and a bounded multiplier estimate ||Z||<=b (the notes use b=kappa*(1+4R)+2delta). For alpha=64kappa*(1+b/kappa)^2,

||(J+Z)(alpha+A_B)^-1||<=81/256<1/2.

The proposed realization G0 on D(A_B) is therefore closed with the cylinder core and full alpha-resolvent range.

### EXACT extension step to audit

For each finite-output cylinder F, pass the finite-source identity

exp(tE_Lambda)H_(Lambda,U,t)F-F
=integral_0^t exp(sE_Lambda)H_(Lambda,U,s)G_(Lambda,0)F ds

to the limit in B. This requires BOTH strong semigroup convergence and G_(Lambda,0)F->G0 F in B; bounded operators act on varying vectors only after controlling that variation. It places F in D(G) and gives GF=G0F. Closedness and the cylinder core then give G0 subset G.

For any z in D(G), solve (alpha-G0)y=(alpha-G)z using full range. Injectivity of alpha-G gives z=y. Hence D(G)=D(A_B).

The Bochner integral for v above is minus the zero-resolvent of the exponentially stable actual G, so v belongs to D(G) and Gv=psi DU. Only NOW infer v in D(A_B), then partial v in C(HS), and finally

partial r=psi^-1 partial v-r tensor r.

No Hessian multiplier is differentiated. The finite-to-infinite second derivative comparison uses strong convergence of derivative-resolvents and uniformly convergent Neumann inverses, and also needs checking.

**Please audit:** the connection signs/constants, density of the vector core, the actual extension identity and zero-resolvent use. Your disjoint-plaquette HS counterexample warns against a shortcut; locate whether any step here actually uses that shortcut. Also verify the bounded beta normalization used in b, rather than assuming component and block norms coincide.

## R4. One jointly Borel strong map, compatibility and the same-noise application

Assume R1-R3 and the separately stated all-start-point martingale problem have been validated. The drift is

b_i=kappa*(beta_i+2r_i)

and the fixed marked Stratonovich equation uses sigma=sqrt(2kappa) times the invariant fields X_(ia). The derivative majorant and leafwise force Lipschitz bound give pathwise uniqueness by first proving ell2 leaf membership with a factorial Volterra remainder, then Gronwall. Do not use the conditional-law influence matrix as the drift derivative majorant.

The current notes assert a measurable weak-solution kernel and a compatible conditional-law construction; their PARAMETERIZED measurability explanation is short. This is a genuine request for an expanded proof, not a claim the fixed-law Kurtz theorem alone already supplies every quantifier.

### Proposed parameterized expansion for review

1. For deterministic x, obtain a Borel kernel x->P_x of continuous state paths from the all-start-point Feller/martingale solution.
2. Construct the countable marked Brownian paths by antidevelopment on each link. A possible route uses ambient quaternion coordinate martingales (state coordinates minus their continuous bounded drift integrals), smooth invariant coframes, and dyadic left-sum approximations to their Ito integrals. Uniform coordinate increment/bracket bounds should give summable L2 error bounds along a fixed dyadic subsequence, for each x. If this works, define a Borel antidevelopment functional by the limit, with a default value on the failure set. No exceptional set common to all uncountably many x is claimed.
3. This gives a Borel kernel x->Q_x(dy,dw), with fixed Wiener marginal gamma and the intended compatible joint solution law for every deterministic x. Verify steps1-2 rather than merely postulate them.
4. Construct a jointly Borel disintegration K(x,w;dy) satisfying Q_x(dy,dw)=gamma(dw)K(x,w;dy) for EVERY x, not just for almost every x under one preparation measure. One possible construction is conditional kernels on increasing countable partitions of Wiener space, using the common marginal gamma, followed by a Borel limit/default operation. Please cite or prove the parameterized disintegration statement with this quantifier.
5. For fixed x, two conditionally independent state copies given w remain solutions with w Brownian in their JOINT filtration, by temporal compatibility. Pathwise uniqueness implies K(x,w) is Dirac for gamma-almost every w. Its atom gives a jointly Borel F(x,w), using the Borel inverse of the Dirac embedding and a default outside its image.
6. Establish joint past-dependent versions at rational times, not merely a full-path measurable representation, so F(Xi,W) is adapted for EVERY initial distribution Xi independent of W. This can use parameterized conditional laws of past paths given past noise. Countably many rational times and path continuity should recover the full path.

This is a proposed expansion to scrutinize. Identify any needed measurable-selection, uniform approximation or compatibility theorem not justified by the supplied inputs. Do not promote full support of one initial law into an all-start-point result.

### Application to actual finite-source transport

Take Xi_Lambda->Xi in product probability on one initial space with the ENTIRE family independent of W. All finite and limiting maps use the SAME marked W; exterior Brownian padding does not alter native interior dynamics.

Uniform fourth coordinate increments and compact coordinates give joint tightness on the product path/noise space. For each smooth cylinder f retain

d<M_Lambda^f,W_(ia)>=sqrt(2kappa)*(X_(ia)f)(Y_Lambda)dt,

as well as state self/cross brackets and Brownian brackets. Test the martingales against the JOINT past of both state paths, their initials and noise. Bounded cylinder drift readers and Wiener moments give uniform integrability. Pass continuous drift/bracket readers, not stochastic integral continuity. Zero residual bracket identifies the limiting stochastic integrals. Pathwise uniqueness forces diagonal limits, hence convergence in probability on the ORIGINAL noise space.

For product-convergent deterministic initial states, the same proof with unchanged coefficients gives initial stochastic continuity. Compactness then gives sup_x E d_T(F_Lambda(x,W),F(x,W))^p->0. It does not give E sup_x or a perfect flow. Exact-marginal Skorokhod couplings of native states are choices of initial coupling, not automatic convergence of every coupling.

Please verify that this application is licensed once the parameterized theorem is repaired/expanded. No global ell2 norm of beta_Lambda-beta and no infinite-horizon change of measure is available or needed.

## Retained scope guards

Your HS/domain counterexample and C-operator-norm nonmixing example are accepted as guards, not yet as counterexamples to R1-R4. Require a concrete invalid inference before declaring one of these written units false.

The original/tilted nonconstant-probe stationary path laws remain singular over infinite observation time despite finite-horizon equivalence. Do not try to repair this closed obstruction with a global Girsanov argument.

The physical source matching kappa=g^2/(2a),lambda=2/(ag^2), with eta<27/262144, gives gap>40/(sqrt(27)*a). The two-time spectral inequality kills nonzero finite-energy positive-time correlation limits under the same clock when these correlations have finite limits at every positive time. This result is conditional on the source gap and matching; it does not prove continuum Yang-Mills triviality or exclude contact terms.

## Requested return

1. A table of R1-R4 with the first failed implication or a complete conditional acceptance.
2. Exact primary citations/theorem locations for each analytic import. Separate verified sources from inaccessible full texts and supplied references.
3. A dependency ledger distinguishing the unreviewed source interaction input from new defects in R1-R4.
4. At most three executable repairs, with the smallest additional lemma stated precisely.
5. A separate verdict on the parameterized strong-map expansion, especially the EVERY-x disintegration and joint adaptedness quantifiers.

Do not rewrite the continuum programme or repeat searches for an infinite-horizon density extension. No numerical regression suite, graph admission or our use of the word 'constructed' is independent mathematical certification.

## Provenance only (no access needed)

The underlying candidate arguments are in `yang-mills-probe-quasilocal-v1.md` (R1), `yang-mills-propagator-comparison-v1.md` and `yang-mills-probe-pointwise-core-v1.md` (R2), `yang-mills-probe-strong-noise-v1.md` (R3/R4), and `yang-mills-probe-coupled-transport-v1.md` (application), all under `research/kitaev/`. The new conditional scaling note is `research/kitaev/yang-mills-physical-scaling-obstruction-v1.md`. The parameterized expansion above is a proposed audit elaboration, not a silently revised frozen predecessor proof.
