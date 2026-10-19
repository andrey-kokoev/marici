# Disconnected-source factorization and spatial clustering of bounded probes

## Question and stratum

Can two spatially separated completed probe functionals be compared to an actual product source, without replacing the infinite state by free-boundary marginals?

SCC obligation: forward tensor realization, retained-label restriction coherence and state-based scalar comparison. Keep the SU2 source and its declared Euclidean semigroup parameter. Let kappa>0, 0<=r<27/262144, R=4096r/3, c=1/2-3R, alpha=8R/9, eta_R=R/2+alpha/(1-alpha), and

\[
C_R=\max\{2R/c,44\eta_R/7\},\qquad a=4/3.
\]

Use two bounded smooth nonnegative real gauge-invariant multiplication probes V,W on finite nonempty supports K,L, with ell=d(K,L)>=2 in the plaquette-link graph. M sums link-gradient sup norms. Coordinates and graph distance retain their lattice-source types, without physical clock or length calibration.

## Issue-boundary DPC

- **Problem:** the previous comparison was written for boxes, whereas disconnected buffered cuts are needed for exact source factorization; disjoint coordinate sets alone do not establish independence or a factorization of constrained Hilbert spaces.
- **Conjecture:** retained-label restriction constructs actual free-cut vacua on arbitrary finite edge sets. At graph separation at least2 the full coordinate Hamiltonian, vacuum and probe operators tensor-factor; the shape-independent boundary comparison then supplies spatial clustering.
- **Named rivals:** use a free law as an infinite-state marginal; admit a distant disconnected interaction label under only an unweighted influence bound; infer tensor factorization after a shared gauge projection; assert independence from matching regional readouts.
- **Risky consequences:** exact tensor identities for the full source packet, uniform boundary budgets for irregular cuts, and a coupling-sensitive decay bound for completed probe readouts.
- **Strongest falsification:** a weak binary pair with identical fair one-site marginals has probe defect1/204 and influence1/17, unchanged under arbitrary distance assignments. A shared-symmetry control has invariant projector ranks2 versus1 and witness residual1. Neither permits the proposed shortcuts.
- **Disposition:** the written argument below supplies actual free-cut factorization and an upper clustering bound. Analytic source review remains open; no sign, nonzero interacting response, gauge-Hilbert tensor decomposition or continuum result follows.

## Canonical free cuts, not newly chosen states

For any finite edge set S, define the actual free-cut Hamiltonian H_S by retaining its link Casimirs and precisely those source plaquette terms whose full edge sets lie in S. Choose an induced box Gamma containing S and apply P_S, deletion by retained label, to its interaction fixed point. The algebraic identity

\[
A\cup B\subseteq S\quad\Longleftrightarrow\quad
(A\subseteq S)\land(B\subseteq S)
\]

and the already established intrinsic Haar centering, electric inverse and gradient contraction show that P_S Phi^Gamma solves the S source equation. This uses no convexity or connectedness of S. Its interaction norm remains at most R; containing-box naturality proves independence of Gamma. In particular this is the restriction of the existing common Phi, not a fitted interaction on a new geometry.

Set u_S=sum_(A subset S)Phi_A. The same source fixed-point equation makes exp(u_S) a positive eigenfunction of H_S; its finite-product C2 regularity suffices, and elliptic regularity gives smoothness. The ground-state transform gives

\[
\langle\Omega_S g,(H_S-E_S)\Omega_S g\rangle
=\kappa\sum_{i\in S}\int|\nabla_i g|^2\Omega_S^2\,d\mu_S.
\]

Thus its eigenvalue is the ground energy and the normalized positive eigenfunction is the actual vacuum. The connected configuration manifold SU2^S makes the zero-gradient sector constant even if the spatial edge graph is disconnected. Its law is exactly dnu_S=Z_S^(-1)exp(2u_S)dmu_S, not a marginal of nu.

The quantitative comparison also extends to these cuts. Deleting labels cannot increase the inherited Hessian or influence majorants. For i in S, a crossing connected label has at least h_i+1 edges, h_i=d(i,S complement), so the old drift discrepancy2R*a^(-h_i) and specification discrepancy R*2^(-h_i-1) remain valid. The positive weighted gradient estimate on SU2^S and the interior resolvent comparison use these distances and weighted row bounds only. There is no spatial differential boundary: free boundary means deletion of interaction terms on a compact link-product manifold.

Compare fixed S inside larger boxes Gamma and pass their already constructed propagator limit on C(X). The same Duhamel, word-gradient and state comparison arguments therefore give, for any local nonnegative probe U supported in J inside S,

\[
|Z_U(T)-Z_{S,U}(T)|
\le C_R T M(U)a^{-d(J,S^c)}.
\]

The bounded-probe completion is the prior strong product construction on this finite product. This extension does not assume an exhaustion by disconnected sets or a new infinite-volume state.

## Buffered geometry and the full tensor packet

Put b=floor(ell/2)>=1 and

\[
S_1=\{i:d(i,K)<b\},\qquad
S_2=\{i:d(i,L)<b\},\qquad S=S_1\cup S_2.
\]

The plaquette-link graph has degree at most12, so these neighborhoods of finite supports are finite. Each support has complement distance at least b in its own region and in S. The triangle inequality gives d(S1,S2)>=ell-2(b-1)>=2. No elementary plaquette can span both regions, since any two of its distinct edges are adjacent. No connected retained label contained in S can meet both regions either.

Use the full link carrier X_S=X_S1 times X_S2. The Haar Hilbert spaces tensor for H and Omega; the vacuum-weighted spaces tensor for P by the product measure. Operator sums are understood on the tensor core and its self-adjoint closure. This proves the compatible identities

\[
H_S=H_{S_1}\otimes I+I\otimes H_{S_2},\quad
E_S=E_{S_1}+E_{S_2},\quad
\Omega_S=\Omega_{S_1}\otimes\Omega_{S_2},\quad
\nu_S=\nu_{S_1}\otimes\nu_{S_2},\quad
P_t^S=P_t^{S_1}\otimes P_t^{S_2}.
\]

The interaction route agrees: every surviving label lies in one component, hence u_S=u_S1+u_S2 and the normalization integrals multiply. Keeping labels, including attachments larger than minimal function support, is essential to the restriction route.

For every finite insertion partition, full operators satisfy

\[
F_{\pi,V+W}^S
=F_{\pi,V}^{S_1}\otimes F_{\pi,W}^{S_2}.
\]

This uses the tensor composition law, not commutation between multiplication and propagation within a component.

## Finite falsifiers and completion

The binary hostile has normalized weights [[9,8],[8,9]]/34. Both marginals are fair, while the conditional influence is1/17. For positive probe factors f=(1,1/2), g=(1,1/3), its joint expectation is103/204, versus the product102/204. Declaring its two-site coupling label to connect arbitrarily distant assigned sites leaves defect1/204 unchanged: small unweighted influence alone supplies no distance decay. It violates the required connected-label/weighted-spatial hypothesis, not the scoped source theorem.

A separate shared Z2 symmetry flips two bits diagonally. Its invariant projector (I+flip tensor flip)/2 has rank2; the product of regional invariant projectors has rank1. The character (1,-1,-1,1) survives the former and is killed by the latter, with sup-norm discrepancy1. Consequently the tensor packet above is proved on the full link carrier. Gauge equivariance then permits the stated individually gauge-invariant V,W; it does not identify the entire invariant Hilbert space with the tensor of regional invariant spaces.

Pass the exact finite-partition tensor identity through the established strong C(X) product limits, first on simple tensors, then on all continuous functions by their density and contraction. This gives Q_(T,V+W)^S=Q_(T,V)^S1 tensor Q_(T,W)^S2, consistent with the actual product vacuum Hilbert space. The infinite vacuum Hilbert space is not identified with that space. Noncollapse is retained by

\[
e^{-T(\|V\|+\|W\|)}\le Q_{T,V+W}^{S}1\le1.
\]

No division by a probe expectation is used.

## Scalar clustering comparison

Only now integrate against the actual product free-cut state:

\[
Z_{S,V+W}(T)=Z_{S_1,V}(T)Z_{S_2,W}(T).
\]

All these positive readouts are at most1. Add the joint-probe boundary error and the two single-probe errors, using M(V+W)=M(V)+M(W) for disjoint supports. The result is

\[
|Z_{V+W}(T)-Z_V(T)Z_W(T)|
\le2C_R T[M(V)+M(W)](3/4)^{\lfloor\ell/2\rfloor}
\le\frac{36}{5}T[M(V)+M(W)](3/4)^{\lfloor\ell/2\rfloor}.
\]

The first coefficient vanishes at R=0. The result is uniform in insertion partitions and survives their completed scalar limits. It is an upper bound linear in the sum of gradient budgets, not a bilinear susceptibility estimate. Constant-probe connected readouts vanish exactly, although this coarse bound need not register that when only one probe is constant.

A fraction-only separation planner chooses the least b>=1 making2*C_R*T*(M(V)+M(W))*(3/4)^b<=epsilon and requires ell>=2b. For T=1, gradient sum at most2 and epsilon=1/1000, the universal coefficient gives separation68; R=9/128 gives56. These are sufficient-budget minima for this cut construction, not optimal source correlation lengths.

## Verification boundary and next constructor

The checker freshly replays the probe-limit receipt; tests4096 retained-label union restriction predicates, buffered interval-label geometry at separations2 through16,90 full tensor operator products with distinct regional states, the two hostiles, and24 rational separation budgets. The finite interval and chain controls are not SU2 truncations. The promotion to arbitrary cuts and completed probes is the written source and strong-topology argument, not the finite test count.

Next executable issue: construct the mixed amplitude response of log Z_(zV+wW)(T) at zero from bounded-operator Duhamel derivatives, and derive a bilinear spatial susceptibility bound from the actual source covariance/gradient transport. Preserve the zero-coupling behavior and original base state. Do not differentiate this coarse absolute error inequality as though it controlled derivatives. Independent analytic review, physical calibration and continuum/root gates remain separate.

Contract: `research/kitaev/contracts/yang-mills-probe-clustering.v1.json`.
Checker: `research/kitaev/checkers/check_yang_mills_probe_clustering.py`.
Receipt: `research/kitaev/results/yang-mills-probe-clustering-v1.json`.
