# Spatial and Euclidean-source connected-correlation bounds

## Question, claim boundary and disposition

Do the constructed joint source packets cluster with quantitative spatial and Euclidean-semigroup separation, without confusing one observable's decay with a complete spectral theorem?

**Written bounds:** in the unchanged fixed spatial SU(2) lattice regime, set

\[
R=4096r/3<9/64,\quad a=4/3,\quad
\alpha=8R/9<1/8,\quad c=1/2-3R>5/64,
\quad m=\kappa c.
\]

Real continuous cylinder observables satisfy a Dobrushin spatial covariance bound. Real smooth cylinders satisfy a joint spatial/Euclidean-source exponential bound. Arbitrary bounded separated insertion blocks have exponential decay in their source-parameter separation. All statements concern the actual thermodynamic state and identified source semigroup, conditional on the written upstream analytic results; independent review remains open.

These are upper bounds. They neither prove a nonzero interacting observable nor supply a continuum theory, physical length/energy conversion, physical clock or four-dimensional covariance. The next source question is an explicit nonzero gauge-invariant connected-correlator witness.

## Issue-boundary conjecture

- **Problem:** a gapped stationary packet need not have spatial locality, and a fast single correlator may miss a slow sector.
- **Conjecture:** the source's weighted spatial influence and Hessian bounds, together with the complete closed-form inequality, force quantitative clustering of its retained observable packets.
- **Rivals:** spectral positivity without geometric locality; observer blindness to a slow sector; discarding Ricci damping in the mixed estimate; interpreting a zero-compatible upper bound as interaction/nontriviality evidence.
- **Risky consequences:** an oscillation spatial estimate for all real continuous cylinders, a product spatial/parameter estimate for smooth cylinders, and a complete separated-block estimate.
- **Falsification/disposition:** exact finite Gibbs and reversible-chain controls below test the mechanisms; nonlocal-reset and hidden-slow-sector models reject the two shortcuts without refuting the scoped source bounds.

## Spatial bound from the actual conditional specification

Let nu be the actual infinite-volume vacuum measure, C_ij the nonnegative symmetric single-link influence majorant from the thermodynamic construction, and D=(I-C)^(-1). Its weighted rows satisfy

\[
\sup_i\sum_j a^{d(i,j)}D_{ij}\le(1-\alpha)^{-1},
\qquad
\sup_i\sum_j a^{d(i,j)}(D-I)_{ij}
\le\alpha/(1-\alpha).
\]

For a real continuous cylinder h let delta_i(h) be its single-link oscillation, and L(h)=sum_i delta_i(h). Temporarily tilt nu by exp(epsilon*g), where g is a bounded real cylinder, solely to differentiate an expectation. This is an auxiliary comparison measure, not a change to the selected source. Its single-link conditional discrepancy from nu is at most |epsilon|*delta_i(g)/4 by the normalized likelihood-oscillation inequality. Dobrushin comparison against the original specification gives

\[
|\operatorname{Cov}_\nu(f,g)|
\le\frac14\sum_{i,j}\delta_i(f)D_{ij}\delta_j(g).
\]

Indeed differentiation at epsilon=0 is justified by boundedness of f,g and equals covariance. The tilted law has the original Gibbs specification plus the finite-support tilt; for sufficiently small epsilon its influence row also remains strictly contracting, so the standard comparison hypotheses hold. No analyticity of an infinite partition function is used.

For finite supports K,L of f,g and ell=d(K,L), this yields

\[
|\operatorname{Cov}_\nu(f,g)|
\le\frac{L(f)L(g)}{4(1-\alpha)}(3/4)^\ell.
\]

If K and L are disjoint, D may be replaced by D-I in the sum, giving the stronger prefactor alpha/[4(1-alpha)]<1/28. This bound vanishes with R at fixed separated observables, as expected at the product-Haar source r=0. It does not prove that any covariance is nonzero when r>0.

## Keep the Ricci damping in gradient transport

Iteration 2 used a nonnegative symmetric Hessian block majorant h^Lambda with weighted rows and columns at most 3R. Its gradient domination discarded Ricci damping to obtain a boundary comparison. On the radius-two SU(2) product, Ricci is exactly 1/2 on every link tangent block, so retaining that term gives instead

\[
\|\nabla_iP_s^\Lambda f\|_\infty
\le\sum_j B_s^\Lambda(i,j)
\|\nabla_j f\|_\infty,
\qquad
B_s^\Lambda=e^{-\kappa s/2}\exp(\kappa s h^\Lambda).
\]

This is the same finite-product differentiated heat equation/Kato argument as before. B_s is entrywise nonnegative and symmetric, has the matrix semigroup law, and has weighted row/column bounds exp(-m*s). The estimate does not identify a nonsmooth gauge orbit space with a Riemannian manifold.

## Joint spatial and Euclidean-source bound

For real smooth cylinders f,g define F_i=||gradient_i f||_infinity, G_i=||gradient_i g||_infinity and M(f)=sum_i F_i. At every finite box containing their supports, symmetry and integration by parts give the exact centered identity

\[
\operatorname{Cov}_{\nu_\Lambda}(f,P_t^\Lambda g)
=2\kappa\int_0^\infty\sum_i
\nu_\Lambda(\nabla_iP_s^\Lambda f\cdot
\nabla_iP_{s+t}^\Lambda g)\,ds.
\]

It follows by differentiating nu_Lambda(P_s f*P_(s+t)g) in s and using convergence to the constant sector. The finite-box positive gap justifies the limiting product of means; no clustering is presumed in this identity.

Gradient domination bounds the absolute integrand by F^T B_s^T B_(s+t) G=F^T B_(2s+t) G. If ell=d(K,L), the weighted matrix estimate gives

\[
F^TB_{2s+t}G
\le (3/4)^\ell e^{-m(2s+t)}M(f)M(g).
\]

Integration and the actual finite-box propagator/state comparison give

\[
|\operatorname{Cov}_\nu(f,P_tg)|
\le\frac{M(f)M(g)}{c}
(3/4)^\ell e^{-mt},\qquad t\ge0.
\]

All constants are uniform over boxes before taking this limit. Passing a finite scalar inequality after source comparison avoids assuming convergence of infinite sums of limiting gradients.

The parameter-sensitive curvature inequality also passes through the already declared form closure, so the complete source generator has gap at least m, not just the conservative 5kappa/64. Hence independently

\[
|\operatorname{Cov}_\nu(f,P_tg)|
\le e^{-mt}\sqrt{\operatorname{Var}_\nu(f)
\operatorname{Var}_\nu(g)}.
\]

One may take the smaller amplitude. The second bound extends to arbitrary L2 source observables; the first needs the stated finite-support smoothness and gradient norms. Neither exponent is a mass in calibrated continuum units.

## Complete separated insertion blocks

Let F be a bounded gauge-invariant insertion polynomial supported at Euclidean source parameters at most zero, and G one supported at parameters at least t>=0. The constructed joint law gives conditional functions

\[
u(x)=\mathbb E[F\mid X_0=x],\qquad
v(y)=\mathbb E[G\mid X_t=y].
\]

The Markov property factors their centered pairing as <u-nu(u), P_t(v-nu(v))>. Conditional expectation contracts centered L2 norm. Therefore

\[
|\mathbb E[\overline F G]-\overline{\mathbb E F}\,\mathbb E G|
\le e^{-mt}\sqrt{\operatorname{Var}_{\rm path}(F)
\operatorname{Var}_{\rm path}(G)}.
\]

This addresses full finite insertion blocks, not a chosen two-point reader alone. Gauge restriction is inherited from the source semigroup. It supplies no additional spacetime covariance or independence claim for overlapping blocks.

## Exact controls and hostile models

The dependency-free checker freshly replays the multi-time-state receipt. It checks:

- a weakly coupled positive binary Gibbs law, its exact conditional influence, covariance response and spatial comparison matrix;
- weighted damped-gradient resolvent majorants on a connected finite matrix, without replacing exponential functions by floating-point samples;
- the complete weighted contraction inequality for powers of the legitimate rational chain and separated nonlinear block covariances.

The rational chain/resolvent controls are explicitly finite analogues, not calculations of the spatial SU(2) propagator.

Two deliberate failures distinguish the required hypotheses. A nonlocal reset generator has a fixed gap but covariance 4/5 between arbitrarily distant assigned sites, rejecting 'gap alone implies spatial decay'. A product chain has a fast observed coordinate with decay ratio 1/3 and an independent slow coordinate with ratio 1-1/N, rejecting a whole-source gap inferred from the fast reader. The source proofs exclude these rivals by the weighted geometry and full-domain form inequality, respectively.

**Disposition:** quantitative source clustering is supplied by the written argument, with all exact controls passing when freshly run. An actual nonzero gauge-invariant connected-correlator witness remains separate. The parent continuum-correlation gate stays open.

Contract: `research/kitaev/contracts/yang-mills-source-clustering.v1.json`.
Reproduce: `python research/kitaev/checkers/check_yang_mills_source_clustering.py`.
Receipt: `research/kitaev/results/yang-mills-source-clustering-v1.json`.
