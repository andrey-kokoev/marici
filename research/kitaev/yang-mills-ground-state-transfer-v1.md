# Iteration 3 — actual-vacuum detector and finite reflection-positive transfer

## Question and disposition

Can the failed raw electric gradient be repaired using the independently specified source Hamiltonian, and does this furnish an actual finite gauge transfer family rather than another loop cutoff?

Yes at fixed finite spatial graph. The actual ground-state transform gives an exact closed-form identity, a faithful detector, and an explicit positive all-coupling finite-graph gap bound. A symmetric temporal heat-kernel transfer step supplies a finite reflection-positive gauge source. The resulting quantitative estimate deteriorates with graph volume. Thus it supplies no volume-uniform or continuum mass gap.

**Net advance:** `finite-gauge-source` is constructed at the explicitly revised Hamiltonian/anisotropic heat-kernel regularization scope. This is not an unannounced completion of the previously mentioned isotropic four-dimensional Wilson-action task. No equivalence to that action or to the official continuum target is claimed. The source, units and changed regulator are recorded in the [contract](contracts/yang-mills-ground-state-transfer.v1.json); earlier packets and pins remain retained.

## Finite source family, not just the two-loop fixture

Keep SU(2), normalized product Haar and the gauge action on ordered links from iteration 2. In addition to its seven-link graph, take open cubic spatial boxes with L>=2 vertices per direction. Order vertices lexicographically, positive-direction links by initial vertex and then axis, and elementary square boundaries by the ordered pair of axes. Each square has the usual two forward and two inverse links. All vertices, including boundary vertices, obey the Gauss constraint; no external charges are admitted.

There are E=3L^2(L-1) links and P=3L(L-1)^2 elementary plaquettes. The simple graph has girth four. Use

\[
H=H_0+V,\quad H_0=\kappa\sum_e(-\Delta_e),\quad
V=\lambda\sum_p(1-\tfrac12\operatorname{Tr}W_p),
\quad0\le V\le B:=2\lambda P.
\]

Here kappa>0 and lambda>=0 are declared source energy parameters. The positive link Casimir in spin j is j(j+1). No physical lattice-spacing trajectory is inferred from these choices. The Hilbert space is the Haar gauge-invariant subspace; the smooth invariant polynomial core and its closed form are those of the actual compact-group operator. Standard elliptic theory, Peter–Weyl completeness, compact resolvent, Feynman–Kac and the symmetric product formula are imported analytic results, not proof-assistant derivations.

The spin-network support/girth argument from iteration 2 applies to every one of these boxes. Therefore the physical Haar kinetic Poincare constant is exactly 3: a fundamental square loop attains the lower bound. This is not the kinematic constant 3/4, and no uncharged one-edge excitation is smuggled through the quotient.

## Source-derived vacuum, unitary and detector

On the full connected compact manifold SU(2)^E, H has a smooth strictly positive ground function Omega. The heat kernel is positivity improving, so this normalized positive function is unique. Gauge symmetry commutes with H; uniqueness implies Omega is gauge invariant. In particular it is also the physical vacuum. These statements use the independently specified elliptic operator, not a presumed gap estimate. Its existence is not an explicit numerical solution for Omega.

Let E0 be its eigenvalue, normalize integral Omega squared dmu=1, and put dnu=Omega squared dmu. The map U:f->Omega f is unitary from L2(nu) to L2(mu), preserving gauge invariance and sending 1 to the actual vacuum. For smooth invariant f, integration by parts and H Omega=E0 Omega give

\[
q_{H-E_0}(\Omega f)
 =\kappa\sum_{e,a}\int\Omega^2|X_{ea}f|^2\,d\mu.
\]

Define the covariant derivative packet

\[
D_\Omega\psi=(\Omega X_{ea}(\psi/\Omega))_{e,a}.
\]

Its components rotate under the vertex adjoint actions just as in iteration 2; its squared norm is gauge invariant. It kills exactly the vacuum span, not the old constant state. Since Omega is smooth and has a positive minimum on this fixed compact manifold, multiplication/division by Omega preserves H1. Smooth gauge-invariant functions are a form core. Thus the identity extends to the entire physical form domain, with no equality asserted merely on a finite spin window.

Write m=min Omega squared and M=max Omega squared. For invariant f, the physical Haar Poincare inequality and minimization over constants give

\[
\operatorname{Var}_\nu f
\le M\operatorname{Var}_\mu f
\le\frac M3\int|\nabla f|^2d\mu
\le\frac M{3m}\int|\nabla f|^2d\nu.
\]

Consequently

\[
\|D_\Omega\psi\|^2\ge\frac{3m}{M}
\|(I-P_\Omega)\psi\|^2,
\qquad\Delta\ge3\kappa m/M>0.
\]

This repairs both interface inequalities at fixed graph: the energy coefficient is exactly kappa and the detector constant is 3m/M. Gauge covariance, normalization, the actual vacuum and domains are all explicit. It does not yet make those constants uniform in graph size or physical units.

## Explicit bound without solving for Omega

For the normalized single-link heat kernel with s=kappa t, character expansion gives

\[
k_s(g)=\sum_{n\ge0}(n+1)e^{-s n(n+2)/4}\chi_n(g),
\qquad |\chi_n(g)|\le n+1.
\]

Choose s=8 log 2. Since n(n+2)>=3n for n>=1,

\[
|k_s(g)-1|\le\sum_{n\ge1}(n+1)^2/64^n
 =\frac{16193}{250047}<\frac18.
\]

The finite rational identity follows by differentiating the geometric series; the infinite majorization is the written analytic argument, not an extrapolation from sampled n. Thus 7/8<=k_s<=9/8. The product free kernel on E links lies between (7/8)^E and (9/8)^E.

Feynman–Kac gives e^{-Bt}k_t^0(x,y)<=K_t^V(x,y)<=k_t^0(x,y). Apply the ground eigenfunction equation exp(-tH)Omega=exp(-tE0)Omega at any two points. The common exponential and integral Omega cancel in the ratio, yielding

\[
\frac{\max\Omega}{\min\Omega}
\le e^{Bt}(9/7)^E.
\]

Squaring this estimate and substituting t=8 log 2/kappa yields the completely source-parametric certificate

\[
\boxed{\Delta\ge
3\kappa(7/9)^{2E}2^{-32P\lambda/\kappa}>0.}
\]

For the two-plaquette seven-link graph this is 3 kappa times (7/9)^14 times 2^{-64 lambda/kappa}. It remains strictly positive where the earlier sufficient bound 3 kappa-2 lambda is zero or negative. It is extremely conservative, not a new sharp spectrum computation.

For cubic boxes both E and P grow extensively. This certificate tends to zero as L grows, including at lambda=0 where the actual electric gap is exactly 3 kappa. The lambda=0 hostile is particularly decisive: collapse of this bound cannot be identified with collapse of the actual gap. The bound's failure to be volume uniform is an unresolved mechanism, not evidence against the continuum problem.

## Actual temporal transfer, Haar action and reflection positivity

Let P_G be normalized vertex gauge averaging. It is the orthogonal Gauss projection, commuting with H0 and V. For tau>0 define

\[
S_\tau=P_G e^{-\tau V/2}e^{-\tau H_0}e^{-\tau V/2}P_G.
\]

On the physical subspace this is a positive, self-adjoint, injective trace-class operator. Indeed S_tau=B_tau^* B_tau with B_tau=e^{-tau H0/2}e^{-tau V/2}P_G. Compact-group heat trace and bounded multiplication give trace class; the projection does not introduce negative states.

Before gauge averaging, its kernel is exactly

\[
e^{-\tau V(U')/2}\prod_e
k_{\kappa\tau}(U'_eU_e^{-1})e^{-\tau V(U)/2}.
\]

The projected kernel averages an endpoint over independent vertex Haar gauge variables. Using such a variable at each temporal slice gives independent time-slice gauge symmetry; these variables are the temporal gauge connectors, not missing physical link states. This is an explicit nonnegative anisotropic heat-kernel action: minus the logarithm of the displayed product, with the specified Haar integrations and half-potentials at slab boundaries. Heat kernels are strictly positive, so that action is defined. It is not the isotropic Wilson plaquette action.

For an even periodic temporal cylinder with N slabs, Z_N=Tr_phys(S_tau^N) is finite and positive. Bounded gauge-invariant multiplication insertions define the correlation state by the same trace. Reflection reverses the temporal order and complex conjugates the insertions. For insertions confined to one half, the two halves pair into Tr(A^* A)/Z_N>=0; S_tau^{1/2} handles cuts through slabs. This supplies temporal reflection positivity and the actual transfer operator, not merely nonnegative Boltzmann entries. Arbitrary complex linear combinations of half-cylinder insertions obey the same norm-square identity.

At fixed graph, the symmetric product formula gives S_(T/N)^N -> exp(-TH) strongly on the physical Hilbert space. This controls time refinement only. Finite-slab vacua need not equal Omega exactly; Omega belongs to the limiting Hamiltonian. No simultaneous spatial limit, rotational covariance restoration, continuum correlations or target equivalence is asserted. The clock parameter here is the declared Euclidean semigroup parameter; physical time remains a reconstruction obligation.

## Exact controls and strongest surviving rival

The checker first verifies graph counts/girth on L=2,3 boxes, the rational tail bound, its normalization and the bound's source/volume dependence. These checks support, but do not replace, the all-size written arguments.

For an independent exact analogue, take the three-site path kinetic matrix

    K = [[1,-1,0],[-1,2,-1],[0,-1,1]],
    V = diag(2,0,2), Omega proportional to (1,2,1), E0=1.

The shifted spectrum is exactly 0,2,3. The weighted identity is

\[
\langle\psi,(H-1)\psi\rangle
=2(\psi_0-\psi_1/2)^2+2(\psi_1/2-\psi_2)^2.
\]

Raw differences have nonzero norm squared 2 on the unnormalized ground vector; the repaired detector vanishes. The kinetic Poincare comparison predicts 1/4, below the actual gap 2. Rational principal minors prove the full matrix inequality, and coefficient fixtures independently regress the form equality. This is a source analogue, not a finite-spin SU(2) truncation or computation of its unknown vacuum.

Rational positive transfer steps of the form M(I+delta K)^{-1}M pass the matrix positivity controls. An entrywise nonnegative swap matrix fails operator positivity on (1,-1,0), rejecting 'nonnegative kernel alone implies reflection positivity'. This controls the distinction used in the B^*B proof; it does not replace that infinite-dimensional proof.

The strongest remaining rival is extensive degeneration of the ground-density comparison. The current proof is compatible with both a uniform true gap and a collapsing true gap as volume grows. The next executable operation is quotient descent for this actual-vacuum packet and a sharper local/volume comparison that does not use the global max/min density ratio. The continuum-correlation gate is also newly ready but unconstructed.

## Reproduction and boundary

`python research/kitaev/checkers/check_yang_mills_ground_state_transfer.py`

Receipt: `research/kitaev/results/yang-mills-ground-state-transfer-v1.json`.

This turn constructs the finite source/temporal transfer gate and repairs the finite-graph detector. It proves no atomic-particle statement, physical continuum theory, volume-uniform magnetic estimate, universal identity gap or official Yang–Mills target.
