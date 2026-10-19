# Equal-time thermodynamic vacuum from retained connected interactions

## Question, claim boundary and disposition

Can the actual finite-box SU(2) vacua of iteration 9 determine one infinite-lattice equal-time probability state, rather than merely a family of volume-uniform bounds?

**Written convergence theorem:** in the unchanged regime 0 <= r=lambda/kappa < 27/262144, the actual finite-box multiplication expectations converge locally to a unique gauge-invariant, translation-invariant Gibbs probability measure on the countable spatial-link product. There is an explicit exponential boundary estimate below. The proof is conditional on iteration 9's analytic construction and imports the standard Dobrushin uniqueness/comparison theorem with its hypotheses checked here. Exact regression tests do not independently verify either analytic theorem.

This constructs a state on the commutative equal-time multiplication algebra only. It constructs neither the full quantum observable state nor multi-time correlations, a limiting Hamiltonian, transported quantum gap, spatial continuum limit or physical energy calibration. The existing conjecture-net root and pins are not changed.

The operator authorized proceeding along the thermodynamic-vacuum direction in `yang-mills-prior-research-clues-v1.md`.

## Issue-boundary conjecture and rivals

**Problem:** finite-volume ground states are not automatically compatible under marginalization.

**Conjecture:** retain every connected support label through the nonlinear construction. Label deletion is then an exact morphism of the interaction fixed-point equations; a single summable interaction determines the finite-box source densities and their unique thermodynamic Gibbs limit.

**Named rivals:** ambient Haar centering or electric inversion breaks naturality; minimization of function supports destroys outside attachments; finite-volume marginals are silently identified; diagonal convergence is mistaken for quantum reconstruction.

**Risky consequences:** exact interaction restriction for every pair of induced nested boxes, one common source-derived potential, and boundary-independent cylinder expectations with a quantitative rate. Failure of any source naturality cell invalidates the common-potential identification.

## Source, carrier and intrinsic operations

Use the infinite oriented nearest-neighbor edge set E of Z^3 and all elementary plaquettes. A finite box Lambda denotes its induced edge set. The single-site space is SU(2), with normalized Haar measure. An interaction component Phi_A is a real mean-zero gauge-invariant function of a finite edge set A, labelled by a connected union of elementary plaquettes. The label is retained even if a resulting function depends on fewer edges.

Use iteration 9's Fourier norm W and

\[
N_2(\Phi)=\sup_e\sum_{A\ni e}2^{|A|}W(\Phi_A),\qquad
R=4096r/3<9/64.
\]

The source interaction is p/6 on each plaquette. The nonlinear operation is B(f,g)=L^{-1}Gamma(f,g)_c, assigned label A union B; derivatives outside the input supports vanish. Here L is the positive sum of link Casimirs, and the inverse acts only on the centered part. These are the same operations as the actual ground-state construction, not a separately selected classical model.

For a function on A, extension to a larger ambient box tensors its Fourier modes with trivial representations. Dimensions, Casimir eigenvalues and Fourier trace norms are unchanged; product Haar centering is unchanged. The ambient link Casimir and gradient contraction act intrinsically on A. Thus B commutes with ambient extension. Gauge invariance is also unchanged, including at boundary vertices.

## Exact restriction cell: labels, not probability marginals

For Lambda contained in Gamma, let P_Lambda delete every interaction component whose label is not contained in Lambda. Do not substitute conditional expectation or minimal function support for this operation.

Since A union B is contained in Lambda exactly when both A and B are,

\[
P_\Lambda B(\Phi,\Psi)
=B(P_\Lambda\Phi,P_\Lambda\Psi).
\]

The source term restricts to precisely the plaquettes of the induced box, and P_Lambda contracts N_2. Therefore P_Lambda Phi^Gamma is in the same radius-R ball and solves exactly the Lambda fixed-point equation. Uniqueness of iteration 9's contraction gives

\[
P_\Lambda\Phi^\Gamma=\Phi^\Lambda.
\]

For each finite connected label A, choose any box containing A and define Phi_A from its fixed point. A larger common box proves independence of this choice. For a fixed edge and any finite collection of labels, one box contains the collection, so its anchored bound applies. Taking monotone limits of nonnegative norm sums gives N_2(Phi)<=R globally. This constructs the interaction; it is stronger than extracting an arbitrary subsequence of densities.

For every finite box the actual vacuum probability measure is exactly

\[
d\nu_\Lambda=Z_\Lambda^{-1}
\exp\!\left(2\sum_{A\subseteq\Lambda}\Phi_A\right)d\mu_\Lambda.
\]

This is a free-boundary Gibbs density for the common dimensionless log interaction 2Phi. It does not assert that nu_Lambda is a marginal of nu_Gamma. No globally summable log density relative to infinite product Haar is asserted; only anchored interaction sums converge.

## Infinite specification and existence

For finite D contained in E and exterior configuration eta, define the conditional density on D by

\[
\gamma_D(dx_D\mid\eta)=Z_D(\eta)^{-1}
\exp\!\left(2\sum_{A:A\cap D\ne\varnothing}
\Phi_A(x_D\eta_{D^c})\right)d\mu_D.
\]

The sum is absolutely and uniformly convergent: its norm is at most 2|D|R. Its terms are continuous, so the normalized kernels are continuous in the exterior configuration and satisfy specification consistency. The conditional algebra follows from cancellation of terms not meeting the resampled set. There is no assumption that the finite-box free-boundary measures are projectively consistent.

Extend each nu_Lambda outside its box by independent Haar. The countable compact product is compact metrizable; the probability measures have weakly convergent subsequences along any exhaustion. For fixed D, the omitted crossing-interaction tail

\[
\sum_{A:A\cap D\ne\varnothing,\ A\not\subseteq\Lambda}W(\Phi_A)
\longrightarrow0
\]

by anchored summability. The finite-box conditional kernels thus converge uniformly to gamma_D. Passing their conditional identities against continuous cylinder tests through a weak subsequence limit proves the DLR identities. Hence a Gibbs measure exists.

## Uniqueness and weighted influence

Let c_ij be the worst total-variation change of the single-link conditional law at i when only exterior link j changes. The log likelihood oscillation bound gives

\[
c_{ij}\le C_{ij}:=2\sum_{A\ni i,j}W(\Phi_A),\quad i\ne j,
\qquad C_{ii}=0.
\]

The normalized-likelihood inequality used is TV <= tanh(osc(log likelihood)/4) <= osc(log likelihood)/4. The factor 2 in C comes from the log interaction 2Phi. Iteration 9's support moment gives sup_i sum_j C_ij <= R/2 < 9/128. Continuous uniformly summable potentials on a countable compact product and this strict Dobrushin row bound satisfy the standard uniqueness theorem's hypotheses. Denote the unique measure by nu_infinity.

A stronger weighted estimate supplies spatial boundary control. Give E the graph metric d in which two distinct edges are adjacent when they belong to a common elementary plaquette. Every retained label A is connected in this graph, so d(i,j)<=|A|-1 for i,j in A. Set a=4/3. For m>=0,

\[
m(2/3)^m\le8/9.
\]

The maximum occurs at m=2,3; for m>=3 the next/current ratio is at most 8/9. Consequently

\[
\sup_i\sum_j a^{d(i,j)}C_{ij}
\le\frac89N_2(\Phi)\le\alpha:=8R/9<1/8.
\]

The positive resolvent D=(I-C)^{-1}=sum_(n>=0) C^n exists on bounded sequences, and the metric triangle inequality gives weighted row bound 1/(1-alpha).

## Boundary comparison for actual source measures

Compare the full specification with the interaction truncated to labels contained in Lambda. The latter's unique Gibbs measure is nu_Lambda times independent exterior Haar. For i inside Lambda their single-site conditional discrepancy is at most

\[
b_i\le\sum_{A\ni i,\ A\not\subseteq\Lambda}W(\Phi_A).
\]

Indeed the log conditional difference is a crossing sum with factor 2, whose oscillation is at most four times this sum. If h_i=d(i,Lambda^c), a crossing connected label has at least h_i+1 edges, giving b_i<=R*2^(-h_i-1)<=a^(-h_i). For i outside Lambda use b_i<=1 and h_i=0.

The standard Dobrushin comparison theorem bounds differences of real continuous cylinder expectations by sum_i delta_i(f)(Db)_i, where delta_i(f) is the single-link oscillation. Since h_i<=d(i,j)+h_j,

\[
|\nu_\Lambda(f)-\nu_\infty(f)|
\le\frac{1}{1-8R/9}
\sum_{i\in\operatorname{supp}f}
\delta_i(f)(3/4)^{d(i,\Lambda^c)}.
\]

In particular the prefactor is less than 8/7 throughout the admitted coupling window. Every exhausting box sequence has this same local weak limit. This is spatial boundary decay, not time evolution or a quantum spectral estimate.

Finite-box source measures are gauge invariant. The weak limit inherits every finitely supported vertex gauge transformation, and continuity extends to arbitrary vertex transformations on cylinder tests. The source operations commute with lattice translations, making the global potential translation covariant; uniqueness makes nu_infinity translation invariant. The limit is a normalized positive state on continuous multiplication observables; gauge-invariant cylinders give the stated equal-time vacuum sector.

## Falsification and disposition

The dependency-free checker exhausts retained-label restriction squares in a finite Walsh-mode analogue, checks intrinsic Casimir extension and exact weight/resolvent inequalities, and includes four deliberate failures:

- B(y,xy)=x still has label {x,y}; premature minimal-support compression gives restriction defect 1.
- Positive pair weights [[3,1],[1,1]] give first-site marginal 2/3 rather than the smaller free-box value 1/2: defect 1/6.
- A disconnected distant two-edge label preserves a small unweighted influence row but violates the spatial weighted bound: connected labels are indispensable.
- The two rational pure states with matrices [[1,1],[1,1]]/2 and [[1,-1],[-1,1]]/2 agree on diagonal measurements and disagree on the flip observable by 2. A commutative state does not determine the quantum state.

These tests discriminate the named rivals but do not mechanically prove the SU(2) fixed-point theorem or the imported Dobrushin theorems. The written naturality cell uses the actual Fourier operations; the finite analogue is a hostile, not their replacement.

**Disposition:** equal-time thermodynamic multiplication state constructed by the written argument at the existing strong-coupling lattice scope, subject to review of the stated analytic inputs. Next unresolved object: compatible multi-time quantum correlations using the actual transfer dynamics. No continuum-correlation or quantum-gap gate is closed by this packet.

Reproduce: `python research/kitaev/checkers/check_yang_mills_thermodynamic_vacuum.py`.
Receipt: `research/kitaev/results/yang-mills-thermodynamic-vacuum-v1.json`.
Contract: `research/kitaev/contracts/yang-mills-thermodynamic-vacuum.v1.json`.
