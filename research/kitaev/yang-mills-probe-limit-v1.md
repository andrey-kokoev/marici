# Bounded local probe: product completion on the actual source carrier

## Question and obligation

Does the mesh-uniform word comparison extend to a source-derived, refinement-compatible bounded probe, rather than an arbitrary infinite insertion product?

SCC stratum: forward product realization, asymptotic refinement coherence and state-based readout transport. Keep the actual source P_s, P_s^Lambda, nu and nu_Lambda from the propagator packet. The coordinate s is its Euclidean semigroup parameter. No physical-clock interpretation is added.

## Issue-boundary DPC

- **Problem:** bounded finite-word errors do not establish a limit for an arbitrary insertion family.
- **Conjecture:** exponential factors of one fixed bounded nonnegative local multiplication probe have a unique bounded-perturbation completion on the existing source carrier; a strong product theorem, not insertion count alone, supplies refinement independence.
- **Rivals:** exact sewing of mixed propagation/insertion steps; convergence from count growth without shrinking maximum width; silent normalization into a new vacuum; inferred operator-norm convergence from strong continuity.
- **Risky consequences:** arbitrary shrinking-mesh partitions give the same operator on each fixed vector; spatial and partition limits sew; the completed readout retains the original two distinct vacuum measures and their boundary error.
- **Strongest falsification:** the finite reset-generator/control below has mixed commutator norm1, a nonshrinking-mesh degree-two limit defect1/8, and a constant-probe normalization defect strictly between5/8 and19/30.
- **Disposition:** the written construction supplies strong completion and state-based comparison. Exact controls do not independently verify the imported source analysis. No operator-norm product theorem, new vacuum or continuum result is inferred.

## Source operation, types and finite composition cells

Retain kappa>0, 0<=r<27/262144, R=4096r/3, c=1/2-3R, m=kappa*c, alpha=8R/9 and eta_R=R/2+alpha/(1-alpha).

Fix a finite nonempty spatial K and a real smooth gauge-invariant cylinder V supported there, with 0<=V<=v=||V||_infinity. It is an auxiliary multiplication probe, with units inverse to the source parameter so that delta V is dimensionless. Write B=M_V, E_delta=M_(exp(-delta V)), and

\[
F_\delta=P_\delta E_\delta,\qquad
F_\pi=F_{\delta_1}\cdots F_{\delta_N},
\quad \delta_j>0,\quad \sum_j\delta_j=T,
\quad |\pi|=\max_j\delta_j.
\]

Use C(X), X=SU2^E, with the sup norm and the existing auxiliary exterior-Brownian extensions of finite-box semigroups. Each F_delta is a positive contraction. Its finite-box analogue uses the same V and actual P_delta^Lambda, with K inside Lambda. Outputs F_pi^Lambda 1 are box-measurable, so their finite-state readout does not depend on the exterior auxiliary extension.

Bare insertions sew exactly: E_delta E_epsilon=E_(delta+epsilon). Mixed steps generally do not: P_delta and M_V need not commute. Partition refinement is a directed approximation in a common Banach space, not an exact identification of its finite products.

A finite falsifier uses G=J_p-I, p=(1,1,1)/3, B=diag(0,1,2), and formal step z. The induced maximum-row norm of [G,B] is1. For S_h=exp(hG)exp(-hB), the degree-two coefficient of S_h^2-S_(2h) is h^2[G,B]. More generally the degree-two coefficient of a partition product minus exp(z(G-B)) is

\[
-\frac12\left(\sum_j\delta_j^2\right)[G,B].
\]

For widths (1/2,1/[2(N-1)],...,1/[2(N-1)]), this coefficient has limit norm1/8 although N grows. This is a formal analytic-germ obstruction, not a numerical claim that the full exponential error equals1/8. Uniform and ramp-width partitions instead have shrinking mesh.

## Completion and its actual topology

Put W=v-V>=0. The positive Dyson series

\[
Q_T=e^{-vT}\sum_{k\ge0}
\int_{0<s_1<\cdots<s_k<T}
 P_{s_1}M_W P_{s_2-s_1}\cdots M_W P_{T-s_k}\,d^k s
\]

has zeroth term e^(-vT)P_T. Each integrated norm is at most v^k T^k/k!, so the series converges uniformly on bounded parameter intervals on C(X). Splitting each ordered simplex at a composition cut proves Q_s Q_t=Q_(s+t). The series solves the bounded-perturbation integral equation and has generator G-B on Dom(G). It is strongly continuous, positive, and contractive: the positive majorant sums to e^(-vT)e^(vT)=1.

In H=L2(nu), the same operators equal exp[-T(A+M_V)], where A is the already identified nonnegative self-adjoint source generator. Bounded self-adjoint perturbation leaves Dom(A) and its smooth-cylinder operator core unchanged. The C(X) and H constructions agree by the bounded-perturbation integral equation on their common dense continuous carrier. The finite-box statement is separate in H_Lambda=L2(nu_Lambda); it is not an isometry claim between vacuum spaces. Gauge equivariance passes termwise.

Here is the needed arbitrary-partition product argument. Duhamel's equation gives

\[
Q_hg=P_hg-\int_0^h P_{h-s}B Q_sg\,ds.
\]

Subtract F_hg=P_hg-integral_0^h P_h B E_sg ds. Using contractions and ||(I-E_s)g||<=sv||g|| gives

\[
\|(F_h-Q_h)g\|
\le h\{v\omega_Q(g,h)+\omega_P(Bg,h)\}
 +\tfrac12v^2h^2\|g\|,
\quad
\omega_U(g,h)=\sup_{0\le s\le h}\|(U_s-I)g\|.
\]

For fixed f and T0, the orbit O_f={Q_s f:0<=s<=T0} and B O_f are compact. Strong continuity and contraction imply uniform small moduli on these compact sets, by a finite-net argument. Telescoping products against Q uses only g in O_f and yields, for every partition with T<=T0,

\[
\|(F_\pi-Q_T)f\|
\le T_0\{v\omega_Q(O_f,|\pi|)
 +\omega_P(B O_f,|\pi|)
 +\tfrac12 v^2|\pi|\|f\|\}\longrightarrow0.
\]

This proves strong convergence in C(X), uniformly on bounded source-parameter intervals, over arbitrary partitions as maximum width tends to zero. It also gives strong L2 convergence for these vectors; contraction and density extend it to every vector of each fixed original Hilbert space. It does not substitute a supremum over the whole Banach unit ball for a compact orbit.

## Spatial transport and sewing

The source packet already proves P_s^Lambda f->P_s f in C(X), uniformly for s in bounded intervals, for every fixed f. Let d_Lambda(t)=||(Q_t^Lambda-Q_t)f||. Subtracting their Duhamel equations gives

\[
d_\Lambda(t)\le
\|(P_t^\Lambda-P_t)f\|
+\int_0^t\|(P_{t-s}^\Lambda-P_{t-s})B Q_s f\|\,ds
+v\int_0^t d_\Lambda(s)\,ds.
\]

The first two terms tend uniformly to zero: B O_f is compact and the source convergence extends uniformly over compact sets by contraction. Gronwall gives Q_t^Lambda f->Q_t f uniformly on bounded intervals. For a fixed partition the original convergence and contractions also give F_pi^Lambda f->F_pi f. Thus both iterated spatial/partition limits equal Q_T f in C(X). No exact finite-box marginal or free-box contraction in L2(nu) is used.

Noncollapse is retained before scalarization: positivity of the Dyson terms implies

\[
e^{-vT}\le Q_T1\le1.
\]

For constant V=1 and T=1, Q_T1=e^(-1), not1. Taylor remainders give11/30<e^(-1)<3/8. Normalizing this value to1 erases a positive probe response, with defect strictly between5/8 and19/30. The original nu is generally not invariant for Q; it is the base state used to read this probe, not a newly constructed ground state.

## Scalar readout and boundary budget

Only now define Z_V(T)=nu(Q_T1) and Z_(Lambda,V)(T)=nu_Lambda(Q_T^Lambda1). The chain rule gives M(exp(-delta V))<=delta M(V). Apply the mesh-word theorem to f0=1 at coordinate0 followed by f_j=exp(-delta_j V) at t_j=sum_(k<=j)delta_k. Its total gradient budget is at most T M(V). Passing the established strong product limits through the two bounded expectation maps proves

\[
|Z_V(T)-Z_{\Lambda,V}(T)|
\le\frac{18}{5}T M(V)(3/4)^b,
\qquad b=d(K,\Lambda^c).
\]

The sharper complementary budget also passes by ordinary Riemann integration. With D_R=2R/c, S_R=2pi eta_R and phi_m(T)=(1-exp(-mT))/m,

\[
|Z_V(T)-Z_{\Lambda,V}(T)|
\le(3/4)^b M(V)
\{D_R[T-\phi_m(T)]+S_R\phi_m(T)\}.
\]

Both summands are nonnegative; their measures and roles remain distinct. Replacing S_R by44 eta_R/7 gives a rational coefficient majorant. T=0 and V=0 are exact identity cases. The uniform finite-word bound additionally proves a simultaneous scalar limit for any exhaustion with b->infinity and any partitions with shrinking mesh: compare the two finite partition readouts first, then use the fixed infinite-source product convergence. This does not claim a simultaneous operator-norm limit.

## Controls, boundary and next issue

The fraction-only checker replays the mesh-word receipt, checks ten partition families through degree6, tests the mixed coarsening coefficient, tests commuting zero/constant probes, checks right-Riemann coefficient bounds, and runs24 probe-buffer planners. Formal matrix coefficients and finite positive controls are not the promotion to the strong topology; that arrow is the compact-orbit/Dyson argument above. Analytic source review remains open.

The next executable issue is spatial factorization of two completed probe functionals supported far apart: construct two disconnected buffered finite-source regions, verify actual vacuum/semigroup factorization there, and transport it to a distance-decaying bound for Z_(V+W)-Z_V Z_W. In particular, do not replace a free-boundary state by a marginal or assume factorization without checking retained-label connectedness. This is a fixed-lattice correlation constructor, not spatial continuum refinement or a parent/root discharge.

Contract: `research/kitaev/contracts/yang-mills-probe-limit.v1.json`.
Checker: `research/kitaev/checkers/check_yang_mills_probe_limit.py`.
Receipt: `research/kitaev/results/yang-mills-probe-limit-v1.json`.
