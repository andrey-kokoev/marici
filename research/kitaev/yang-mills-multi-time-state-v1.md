# Joint source insertion state, reflection positivity and its null quotient

## Question, claim boundary and disposition

Do the actual thermodynamic source semigroup and stationary vacuum measure sew into one positive family of joint Euclidean insertion packets, with the correct reflection-positive Hilbert space?

**Written construction:** for the unchanged spatial SU(2) lattice, fixed source kappa>0 and 0<=lambda/kappa<27/262144, the identified reversible Feller semigroup defines compatible stationary joint probability kernels for every finite set of real Euclidean source parameters. Their continuous gauge-invariant insertion moments are limits of the actual finite-box vacuum operator strings. Arbitrary finite positive-half insertion polynomials satisfy reflection positivity. The reflection-positive null quotient completes to L2(nu_infinity)_G, and positive shifts recover the already identified source semigroup and its generator.

This is a lattice-source Euclidean reconstruction on the declared multiplication-observable algebra. It is not an assertion of four-dimensional Euclidean rotation covariance, spatial refinement, physical clock/energy calibration, completeness for an independently specified local electric/Weyl field algebra, or continuum Yang–Mills. The analytic proof remains conditional on the independently unreviewed upstream constructions; rational tests are regression evidence only.

## Issue-boundary conjecture and rivals

- **Problem:** positive two-point samples do not construct a jointly positive source state, and a reflection-positive path vector need not represent a nonzero Hilbert vector.
- **Conjecture:** source transition kernels, stationarity and reversibility sew all insertion packets. Conditional expectation at the reflection plane factors the complete reflection form and identifies exactly its radical.
- **Rivals:** inconsistent marginal packets; a signed higher joint law hidden behind positive pair marginals; a stochastic reversible transition without positive half-step factorization; treating reflection-null vectors as ordinary probability-null functions.
- **Risky consequences:** deletion/coalescence consistency, positivity of every cylinder polynomial square, convergence of finite source strings, and one common Gram factorization for every reflected word pair.
- **Falsification/disposition:** exact rational joint-law, reflection-Gram and null-space tests accompany the written construction. Explicit signed-triple and wrong-reflection-kernel hostiles show why lower tests cannot substitute for these witnesses.

## Source kernels and joint packets

Let X=SU(2)^E with its compact countable product topology, nu=nu_infinity, and P_s=exp(-sA_infinity), s>=0, from the actual propagator comparison. Positivity and P_s1=1 give a Borel probability kernel p_s(x,dy) by Riesz representation. Its dependence on x is weakly continuous. The Feller semigroup law gives Chapman–Kolmogorov, with p_0(x,dy)=delta_x(dy). Invariance and symmetry give stationary detailed balance:

\[
\nu(dx)p_s(x,dy)=\nu(dy)p_s(y,dx).
\]

For ordered parameters t_1<...<t_n in R define

\[
\mu_{t_1,\ldots,t_n}(dx_1\cdots dx_n)
=\nu(dx_1)\prod_{j=1}^{n-1}
 p_{t_{j+1}-t_j}(x_j,dx_{j+1}).
\]

These are positive normalized probability measures, not just bilinear forms on a sampled observer family. Integrating an interior coordinate uses Chapman–Kolmogorov; integrating the earliest coordinate uses stationarity; the last uses kernel normalization. Repeated parameters are identified by the diagonal kernel, so simultaneous insertions multiply on the same X coordinate. Permuting labelled insertions means reordering their pairs (t_j,f_j), not permuting an operator string without its parameters.

The resulting projective family defines a probability measure on the cylinder sigma algebra of X^R by the Kolmogorov extension theorem for standard Borel single-site spaces. No continuity of sample paths or extra path topology is claimed or needed for this finite-packet construction. The real parameter is the source Euclidean semigroup coordinate, not automatically a physical time.

For continuous insertions f_j the moment is

\[
S((t_j,f_j)_{j=1}^n)
=\nu\bigl(f_1P_{t_2-t_1}
(f_2P_{t_3-t_2}(\cdots f_n))\bigr).
\]

Products and finite linear combinations define a normalized positive functional on the entire continuous cylinder algebra: E(conjugate(F)F)>=0 follows from the joint probability measures. Gauge-invariant insertions form a positive subalgebra. Common gauge transformations of all configuration coordinates preserve the joint kernels; independently rechoosing a gauge at each parameter is not asserted as an extra source law.

## Actual finite-box source strings converge jointly

For a box containing all spatial supports, the finite moment is exactly

\[
\langle\Omega_\Lambda,
M_{f_1}e^{-(t_2-t_1)(H_\Lambda-E_{0,\Lambda})}
M_{f_2}\cdots
 e^{-(t_n-t_{n-1})(H_\Lambda-E_{0,\Lambda})}
M_{f_n}\Omega_\Lambda\rangle.
\]

Ground-state conjugation turns this into the corresponding nested P_s^Lambda moment with nu_Lambda. Let the right-nested functions be u_j^Lambda=f_j P_(t_(j+1)-t_j)^Lambda u_(j+1)^Lambda. Uniform semigroup convergence on each fixed continuous function and contraction show u_j^Lambda tends uniformly to u_j by backward induction: separate the varying-input difference from the fixed limiting input before applying convergence. Weak convergence of the vacuum measures then passes the final integral.

The same argument handles any finite sum of insertion words and their products. Thus joint positivity and sewing belong to the actual common source limit, not to an unrelated Markov process selected after matching a two-point correlator. Stationarity follows from parameter differences and the invariant initial measure; parameter reversal follows from detailed balance. No spatial continuum covariance is inferred.

## Reflection form on the complete positive-half algebra

Let F be any finite linear combination of insertion words whose parameters are nonnegative, including zero. Define Theta F by reversing the signs of its parameters and conjugating its coefficients and insertions. Put

\[
J F(x)=\mathbb E[F\mid X_0=x].
\]

For one word with 0<=s_1<...<s_m this is

\[
J\left(\prod_j f_j(X_{s_j})\right)
=P_{s_1}\bigl(f_1P_{s_2-s_1}
(\cdots f_m)\bigr).
\]

The formula also covers zero parameters via P_0=I and coalescence. Detailed balance makes the conditional negative-half law given X_0 the same as the positive-half law read from the plane. The joint Markov kernels make the two halves conditionally independent given X_0. For any two positive-half polynomials F,G, including shared zero-parameter insertions,

\[
\mathbb E[(\Theta F)G]
=\int\overline{JF}\,JG\,d\nu.
\]

This factors the entire reflection Gram matrix at once. In particular the reflected square is nonnegative for every finite complex linear combination. Stationarity gives the same statement at any reflection plane, not just at a chosen grid origin. The underlying continuous self-adjoint semigroup also has P_s=P_(s/2)^*P_(s/2), so no link-plane positivity is inferred from stochastic entries alone.

## Radical, gauge Hilbert space and source shifts

The reflection radical is exactly ker(J) in L2(nu), not the ordinary path-probability null ideal. Quotienting the positive-half algebra by this radical and completing maps isometrically by J into L2(nu). Because F=f(X_0) is allowed, its image contains all continuous f; hence the image is dense and the completion is precisely L2(nu).

On the gauge-invariant insertion algebra, J lands in H_G because the source semigroup commutes with gauge transformations. Zero-parameter gauge-invariant cylinders are dense in H_G by compact gauge averaging. Therefore the physical restriction of this lattice-source reflection quotient is exactly H_G, with no undeclared additional null directions.

Positive source shifts sigma_s satisfy

\[
J(\sigma_s F)=P_s JF.
\]

This follows directly from the Markov kernel composition law. It identifies the reconstructed contraction semigroup, rather than merely matching its two-point samples. Its generator is the previous A_infinity restricted to H_G, and its source-unit separation remains at least 5kappa/64. Neither this spectral statement nor the word 'reconstruction' supplies the missing continuum/physical-scale bridge.

## Exact controls and surviving frontier

The checker uses the reversible rational chain Q=(I+A)^(-1), where A is the three-site ground-state generator from iteration 1. Q is a declared discrete finite analogue, not a calculation of exp(-sA) or a spatial SU(2) truncation. It checks all 243 five-coordinate joint atoms, marginal deletion with the two-step kernel, reversal, word sewing and reflected word-pair Gram factorization. Exact principal minors verify a reflection matrix; a nonzero ordinary path vector is shown to lie in the reflection radical.

Three deliberate failures are retained:

1. Signed triple weights (1+2s_1s_2s_3)/8 have positive uniform pair marginals but four negative atoms. Pair checks cannot establish a joint probability state.
2. The positive-entry reversible transition [[1/4,3/4],[3/4,1/4]] has flip-observable link-reflection value -1/2. Stochasticity and reversibility alone do not give all-plane reflection positivity or a positive half-step factorization.
3. For the legitimate chain, F=f(X_1)-(Qf)(X_0) has JF=0 but strictly positive ordinary path L2 norm. Quotienting the wrong null space would produce the wrong reconstructed Hilbert space.

The written source-compatible multi-time state and its reflection quotient are supplied at fixed lattice scope. The parent continuum-correlation gate remains open. The next executable research question is quantitative spatial/Euclidean-source clustering and a nontrivial gauge-invariant observable test; this checks what correlations survive rather than identifying a stationary positive packet with an interacting continuum theory.

Contract: `research/kitaev/contracts/yang-mills-multi-time-state.v1.json`.
Reproduce: `python research/kitaev/checkers/check_yang_mills_multi_time_state.py`.
Receipt: `research/kitaev/results/yang-mills-multi-time-state-v1.json`.
