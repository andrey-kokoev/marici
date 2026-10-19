# Actual finite-box propagators converge to the thermodynamic gradient generator

## Question, claim boundary and disposition

Does the closed cylinder form of iteration 1 generate the limit of the actual finite-box vacuum propagators, rather than an unidentified extension sharing their local energy values?

**Written comparison theorem:** at fixed source kappa>0 and 0<=r=lambda/kappa<27/262144, the actual ground-state-conjugated finite-box semigroups converge uniformly on smooth cylinder observables, uniformly on bounded Euclidean-semigroup parameter intervals. The limit is a symmetric contraction semigroup on L2(nu_infinity). A resolvent range approximation proves that smooth cylinders are an operator core; its generator is therefore exactly the closed gradient-form generator constructed previously. Local propagator matrix elements and their norms converge in the changing vacuum Hilbert spaces.

The analytic proof uses the predecessor interaction/state/form results and finite-dimensional elliptic semigroup/one-form maximum-principle facts. Exact regressions are not independent verification. This is a fixed spatial-lattice, strong-bare-coupling source comparison, not spatial refinement, Lorentz/Euclidean spacetime reconstruction, physical time calibration, or continuum Yang–Mills. Multi-time insertion packets remain the next explicit construction.

## Issue-boundary conjecture

- **Problem:** core energy convergence can select the wrong limiting operator through hidden high-frequency directions.
- **Conjecture:** connected support weights control the full Hessian and distant-boundary drift discrepancy. Gradient domination then gives a uniform semigroup limit and a resolvent range criterion identifying the actual closure.
- **Rivals:** discarded crossing-cluster labels; a missing spatial influence moment; finite energy agreement with a different Schur-complement limit; treating identical coordinates as an exact isometry between different vacuum measures.
- **Risky consequences:** a weighted Hessian row bound 3R, an explicit exponential-in-distance propagator bound, and graph-norm recovery of limiting resolvents by smooth finite-box resolvents.
- **Falsification/disposition:** the checker tests the weighted matrix mechanism and exhibits an exact hidden-mode resolvent defect despite identical core energies. The written range argument, not that core agreement, supplies the operator identification.

## Source and comparison carrier

Use the predecessor's retained global interaction Phi and R=4096r/3<9/64, with N_2(Phi)<=R. Let a=4/3. The spatial metric d joins distinct links sharing an elementary plaquette. Every retained label A is connected for this metric.

On a finite box Lambda define V_Lambda=2 sum_(A contained in Lambda) Phi_A, beta_Lambda=gradient V_Lambda, and

\[
G_\Lambda=\kappa\sum_{i\in\Lambda}
(\Delta_i+\beta_{\Lambda,i}\cdot\nabla_i),
\qquad P_t^\Lambda=\exp(tG_\Lambda).
\]

The source identity is exact:

\[
P_t^\Lambda f=\Omega_\Lambda^{-1}
\exp[-t(H_\Lambda-E_{0,\Lambda})]
(\Omega_\Lambda f).
\]

Here t is the declared Euclidean semigroup parameter of the lattice source, not a newly reconstructed physical clock. On the full compact product X=SU(2)^E, extend P_t^Lambda by independent source-normalized link Brownian semigroups outside Lambda. This auxiliary extension gives contractions on the common C(X) comparison carrier. When f is supported inside Lambda the exterior extension does nothing to its finite-box dynamics.

Hilbert spaces remain H_Lambda=L2(nu_Lambda), or their auxiliary exterior-Haar extensions, and H_infinity=L2(nu_infinity). The common cylinder algebra maps into each by evaluation. Its inner products converge; no exact finite-box isometry or infinite-product density ratio is assumed.

## Weighted Hessian and boundary drift

Write w_(A,pi)=d_pi*||Phi_A_hat(pi)||_trace and C_pi=sum_i j_i(j_i+1). Iteration 10's covariant Hessian calculation bounds the norm of the 3 by 3 (i,j) block of Hess(V_Lambda) by

\[
h^\Lambda_{ij}=6\sum_{A\subseteq\Lambda:A\ni i,j}
\sum_\pi j_i j_j w_{A,\pi}.
\]

This is a symmetric nonnegative matrix, including its diagonal. The factor 6 is twice the three-direction operator-norm bound; the same-link covariant Hessian uses the symmetrized generator product, not an uncorrected frame derivative.

For n=|A|, J=sum_i j_i, and i in A, j_i J <= (n+1)C_pi/2. Since d(i,j)<=n-1,

\[
\sup_i\sum_j a^{d(i,j)}h^\Lambda_{ij}
\le3\sup_i\sum_{A\ni i}
(n+1)a^{n-1}\sum_\pi C_\pi w_{A,\pi}
\le3R.
\]

The last step uses (n+1)a^(n-1)/2^n<=1 for n>=1: equality holds at n=1,2, and the subsequent sequence decreases. Symmetry gives the same weighted column bound. These constants are independent of the box.

For Lambda contained in Gamma and i in Lambda, retained-label naturality gives the crossing-cluster identity for beta_Gamma,i-beta_Lambda,i. The derivative block norm is at most 2W(Phi_A), using sqrt(3)<=2. Thus, with h_i=d(i,Lambda^c),

\[
\|\beta_{\Gamma,i}-\beta_{\Lambda,i}\|_\infty
\le4\sum_{A\ni i,A\not\subseteq\Lambda}W(\Phi_A)
\le2R\,2^{-h_i}\le2R\,a^{-h_i}.
\]

The same estimate holds with Gamma replaced by infinity. No global vacuum max/min comparison is used.

## Finite-dimensional gradient domination

For a smooth cylinder f supported in K contained in Lambda, put g_i(t)=||gradient_i P_t^Lambda f||_infinity and g_i(0)=||gradient_i f||_infinity. The finite-product one-form heat equation gives

\[
g_i(t)\le\sum_j
[\exp(\kappa t h^\Lambda)]_{ij}\,g_j(0).
\]

For clarity, the mechanism is the differentiated heat equation: the connection Laplacian acts on the gradient, Ricci contributes a nonpositive term to its norm evolution, and Hess(V_Lambda) couples link-gradient blocks. Kato's norm inequality and the parabolic maximum principle dominate each block norm by the positive scalar system with coefficients kappa*h_ij. The product SU(2) Ricci tensor is nonnegative, so dropping its damping is legitimate. Regularizing a vanishing block norm and then removing the regularization justifies that step. This uses a finite-dimensional compact smooth manifold only; no infinite-dimensional stochastic existence theorem is presumed.

The weighted column estimate and the triangle inequality imply

\[
\sum_i a^{d(i,K)}g_i(t)
\le e^{3\kappa Rt}M(f),
\qquad M(f)=\sum_{j\in K}\|\nabla_j f\|_\infty.
\]

## Uniform source-semigroup limit

Compare both finite systems on Gamma, extending Lambda by independent Brownian links. Duhamel's identity and contraction give

\[
\|P_t^\Gamma f-P_t^\Lambda f\|_\infty
\le\kappa\int_0^t\sum_{i\in\Lambda}
\|\beta_{\Gamma,i}-\beta_{\Lambda,i}\|_\infty
\|\nabla_iP_{t-s}^\Lambda f\|_\infty\,ds.
\]

Gradients outside Lambda vanish. Let h_K=d(K,Lambda^c). Since h_i>=h_K-d(i,K), the preceding estimates yield

\[
\|P_t^\Gamma f-P_t^\Lambda f\|_\infty
\le\frac23(e^{3\kappa Rt}-1)
(3/4)^{h_K}M(f).
\]

At R=0 both drifts vanish and the difference is zero. This bound proves a uniform Cauchy limit on every bounded parameter interval and every exhaustion. Common larger boxes compare different exhaustions. Denote the limit by P_t f. Extend by sup-norm contraction and density from smooth cylinders to C(X).

Positivity, preservation of 1, and the semigroup identity pass to this limit. To pass composition, first approximate P_s f by a fixed cylinder and use contraction; one must not apply a fixed-cylinder convergence assertion to an uncontrolled varying input. Strong continuity follows by a fixed-box approximation on a bounded parameter interval and finite-box strong continuity. Thus P_t is a Feller semigroup on the compact product.

Each extended finite-box measure is invariant and symmetric for its semigroup. Uniform function convergence and weak measure convergence pass both identities to nu_infinity. Hence P_t extends to a strongly continuous symmetric contraction semigroup on H_infinity; call its nonnegative self-adjoint generator A_tilde.

## Resolvent range recovery identifies the extension

On smooth cylinders define the quasilocal generator

\[
Gf=\kappa\sum_i(\Delta_i f+
\beta_{\infty,i}\cdot\nabla_i f).
\]

Only finitely many derivatives occur. Its coefficients are continuous and uniformly convergent interaction sums. For fixed f, G_Lambda f tends uniformly to Gf. Passing P_t^Lambda f-f=integral_0^t P_s^Lambda G_Lambda f ds through the uniform limit puts f in the Feller and L2 generator domains, with A_tilde f=-Gf.

Core agreement is not yet enough. Fix alpha>3kappa R and smooth cylinder f supported in K. The finite resolvent

\[
u_\Lambda=(\alpha-G_\Lambda)^{-1}f
=\int_0^\infty e^{-\alpha t}P_t^\Lambda f\,dt
\]

is a smooth function of the finite box by elliptic regularity. Uniform semigroup convergence, boundedness and the exponentially small integral tail give u_Lambda tending uniformly to u=(alpha+A_tilde)^(-1)f. The boundary drift and integrated gradient estimates also give

\[
\|(\alpha-G)u_\Lambda-f\|_\infty
\le\frac{2\kappa R}{\alpha-3\kappa R}
(3/4)^{h_K}M(f)\longrightarrow0.
\]

This is an explicit graph-range recovery sequence, not energy matching alone. It proves u_Lambda tends to u in the graph norm of A_tilde. Smooth cylinder right-hand sides are dense in L2(nu_infinity); applying the bounded resolvent shows their images are graph-dense in Dom(A_tilde). Consequently smooth cylinders are an operator core and hence a form core for A_tilde.

Integration by parts identifies its form on those cylinders with the predecessor q_0. Their closures must agree. Therefore A_tilde=A_infinity, the generator of the declared closed gradient form. The fixed-source spectral lower bound 5kappa/64 is now attached to the actual semigroup limit at this lattice scope.

## Changing-state propagator comparison and gauge descent

For continuous cylinder f,g, uniform semigroup convergence and weak convergence of the extended measures give

\[
\nu_\Lambda(\overline f P_t^\Lambda g)
\longrightarrow\nu_\infty(\overline f P_t g),
\qquad
\nu_\Lambda(|P_t^\Lambda g|^2)
\longrightarrow\nu_\infty(|P_tg|^2).
\]

The norm statement follows from uniform convergence to a continuous function, not merely pointwise matrix elements. Together with asymptotic cylinder inner products, these are the declared varying-Hilbert comparison arrows. Global spectral convergence of all finite-box eigenvalues is not asserted.

The finite source semigroups commute with vertex gauge transformations, as does the exterior Brownian comparison extension. Uniform limits commute as well. The comparison and generator identification therefore restrict to the gauge-invariant Hilbert subspace without an orbit-space smoothness assumption.

## Exact tests, surviving scope and next operation

The checker freshly replays iteration 1's receipt, verifies weighted support/Casimir bounds, positive matrix-power and resolvent majorants, and exact boundary graph-range estimates on a connected finite fixture. It includes two hostiles:

- K_n=[[1,-n],[-n,2n^2]] has constant observed core energy 1, but recovery vectors (1,1/(2n)) have energy 1/2. At alpha=1 its observed resolvent tends to 2/3 rather than the candidate 1/2: defect 1/6. The graph-range argument is therefore indispensable.
- Copying a coordinate vector between the uniform three-state measure and (1,4,1)/6 changes its squared norm by 1/3. Finite-box coordinate equality is not exact Hilbert isometry.

These finite calculations do not mechanically prove the one-form gradient domination, source harmonic analysis, state limit or operator-core theorem. Independent analytic review remains open. The newly enabled operation is construction of compatible actual-source multi-time insertion packets and reflection positivity from this identified semigroup. The parent continuum-correlation gate remains open.

Contract: `research/kitaev/contracts/yang-mills-propagator-comparison.v1.json`.
Reproduce: `python research/kitaev/checkers/check_yang_mills_propagator_comparison.py`.
Receipt: `research/kitaev/results/yang-mills-propagator-comparison-v1.json`.
