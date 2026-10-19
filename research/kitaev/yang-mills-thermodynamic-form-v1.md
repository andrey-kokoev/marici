# Thermodynamic closed gradient form and fixed-source spectral separation

## Question and claim boundary

Does the equal-time thermodynamic vacuum admit a closed source-normalized energy form, and does the finite-box Poincare inequality survive its closure?

**Written construction:** at fixed kappa>0 and 0<=r=lambda/kappa<27/262144, the smooth-cylinder gradient form on L2(nu_infinity) is densely defined and closable. Its closure has constants as its entire kernel and satisfies

\[
q_\infty(f)\ge\frac{5\kappa}{64}
\|f-\nu_\infty(f)\|_2^2.
\]

Its nonnegative self-adjoint generator therefore has spectrum contained in {0} union [5kappa/64,infinity). The gauge-invariant restriction has the same lower bound. This is an infinite spatial-lattice closed-form theorem in source units, conditional on the written thermodynamic-measure and finite-curvature theorems, not an independently reviewed continuum result.

**Not constructed:** convergence of finite-box propagators to this generator, a full source-compatible quantum state, multi-time source correlations, spatial refinement, reconstructed physical time, physical energy calibration, or continuum Yang–Mills. Core energy convergence below must not be promoted to strong-resolvent convergence.

## Issue-boundary conjecture

- **Problem:** an equal-time probability measure fixes multiplication expectations but does not select a closed energy generator.
- **Conjecture:** the actual finite-source gradient identity supplies a canonical cylinder form; summable conditional logarithmic derivatives make its adjoint densely defined, and local weak convergence passes the uniform Poincare bound through closure.
- **Rivals:** a positive but nonclosable form; use of the wrong vacuum gradient or energy scale; loss of the bound outside the core; identification of a chosen closed extension with an unproved finite-volume operator limit.
- **Risky consequences:** a uniformly bounded integration-by-parts drift, a dense adjoint test domain, convergence of all smooth-cylinder source energies, and a whole-closure spectral inequality.
- **Strongest tests and disposition:** exact finite ground-state identities and nonclosability/energy-scale/hidden-extension hostiles accompany the analytic argument. Source propagator identification remains the first unresolved comparison cell.

## Typed carrier, source operation and domain

Keep the previous packet's probability measure nu=nu_infinity on X=SU(2)^E, E the countable oriented nearest-neighbor spatial links of Z^3. This is not a continuum field space. Let C be the complex smooth cylinder functions, including constants, and H=L2(X,nu). Continuous cylinders are uniformly dense in C(X), and smooth cylinders approximate them uniformly; hence C is dense in H.

For each oriented link e and each of the three orthonormal radius-two SU(2) left generators X_ea, define

\[
D_0f=(X_{ea}f)_{e,a},\qquad
q_0(f,g)=\kappa\sum_{e,a}\int
\overline{X_{ea}f}\,X_{ea}g\,d\nu.
\]

The sum is finite on C. Its target is the Hilbert direct sum of copies of L2(nu), not a compressed loop reader. The coefficient kappa and generator normalization are exactly those in the finite-source ground-state identity. The closure will be taken in norm squared ||f||_2 squared + q_0(f), not in probability convergence alone.

The source relation is explicit. On any box Lambda containing the supports of f and g, finite multiplication by its normalized positive vacuum gives

\[
\langle\Omega_\Lambda f,
(H_\Lambda-E_{0,\Lambda})\Omega_\Lambda g\rangle
=q_\Lambda(f,g)
=\kappa\sum_{e,a}\nu_\Lambda(
\overline{X_{ea}f}X_{ea}g).
\]

All integrands and inner products are continuous cylinders. Local weak convergence proves convergence of q_Lambda(f,g) and nu_Lambda(conjugate(f)g) to q_0(f,g) and nu(conjugate(f)g). This is convergence of source forms on the declared cylinder core, without a common-Hilbert operator limit claim.

## Conditional integration by parts

The actual log interaction is 2Phi from the predecessor. Its Fourier norm controls derivatives: for a spin j_e mode, ||d pi(X_ea)||<=j_e<=1+C_pi. Thus ||X_ea Phi_A||_infinity<=W(Phi_A), and

\[
\beta_{ea}=2\sum_{A\ni e}X_{ea}\Phi_A,
\qquad \|\beta_{ea}\|_\infty\le2R,
\quad R=4096r/3<9/64.
\]

The sum and its defining single-link derivatives converge uniformly. Each conditional single-link log density is a uniformly convergent interaction sum with this derivative. Its normalizer depends only on the exterior coordinates, not on the integrated link. Haar integration by parts on SU(2), followed by the DLR identity, therefore gives for cylinder f,g

\[
\int\overline g\,X_{ea}f\,d\nu
=-\int\bigl(X_{ea}\overline g+
\beta_{ea}\overline g\bigr)f\,d\nu.
\]

No global infinite-product log density or differentiable Radon–Nikodym derivative is assumed. This is a one-link conditional calculation, justified by the uniformly summable derivative tail.

## Closability and the closed form

Let v=(v_ea) be a finite-component vector of smooth cylinders in the derivative target. Integration by parts identifies its adjoint image as

\[
D_0^*v=-\sum_{e,a}(X_{ea}v_{ea}+\beta_{ea}v_{ea})\in H.
\]

Finite-component smooth vectors are dense in the Hilbert direct sum, so D_0 has a dense adjoint domain and is closable. Explicitly, if f_n tends to zero in H and D_0 f_n tends to w in the target, then inner products against every such v tend to zero by this adjoint identity; their density gives w=0. This rules out a hidden gradient limit on a vanishing state sequence.

Let D be the graph closure of D_0. Define Dom(q_infinity)=Dom(D) and q_infinity(f,g)=kappa<Df,Dg>. This is the closure of q_0, is densely defined and nonnegative, and contains 1 with zero form energy. The closed-form representation theorem produces a unique nonnegative self-adjoint A_infinity associated with this particular closed form. It does not prove that other candidate extensions or finite-box operator limits coincide with it.

## Passing the uniform bound through the declared closure

Iteration 10 derives the weighted-product Poincare inequality for every smooth function on each finite box, before restriction to gauge invariants. Thus for every f in C and every sufficiently large box,

\[
q_\Lambda(f)\ge\frac{5\kappa}{64}
\bigl(\nu_\Lambda(|f|^2)-|\nu_\Lambda(f)|^2\bigr).
\]

Passing to the thermodynamic limit is legitimate term by term because f, |f| squared and its finitely many squared derivatives are continuous cylinders. It gives the same bound for q_0. For general f in Dom(q_infinity), choose its defining graph-core sequence f_n. L2 convergence controls means and variances, while graph convergence controls q_0(f_n). Hence the inequality extends to the entire closed-form domain.

It follows that ker(q_infinity)=span{1}. The spectral theorem then gives the asserted lower bound on the orthogonal complement. This spectral assertion concerns A_infinity in the declared source-normalized Hilbert space. It is not a statement about an unidentified reconstructed physical Hamiltonian.

## Gauge-invariant restriction

The compact product vertex gauge group acts unitarily on H because nu is gauge invariant. On smooth cylinders, the link gradient components transform by orthogonal adjoint rotations, so q_0 is invariant. This invariance passes to its closure. Gauge averaging P_G is therefore a bounded form contraction and maps C to gauge-invariant smooth cylinders; only finitely many vertex variables act on any one cylinder.

Consequently P_G C is graph-dense in the gauge-invariant restricted domain. The restriction to H_G=ran(P_G) is a closed densely defined form, and its associated self-adjoint operator has the same constant kernel and lower bound 5kappa/64. No smooth geometry on a singular gauge orbit space is used.

## Exact regressions and exclusions

The checker freshly verifies the thermodynamic predecessor receipt and the finite-source curvature receipt. A three-site actual-ground-state analogue has shifted source matrix

\[
S=\begin{pmatrix}2&-1&0\\-1&1&-1\\0&-1&2\end{pmatrix},
\qquad\Omega=(1,2,1),\qquad
\nu=(1,4,1)/6.
\]

Conjugation by Omega gives weighted self-adjoint A with spectrum 0,2,3. Its form is ((f_0-f_1)^2+(f_1-f_2)^2)/3, and the exact weighted Poincare constant is 2. Rational principal minors verify the entire matrix inequality, not just sampled vectors. Finite gradient/adjoint matrices independently verify integration by parts.

Deliberate failures retained by the checker:

1. On finite sequences in ell2, T f=sum_n n f_n has f^(n)=e_n/n tending to zero while T f^(n)=1. Its positive square form is nonclosable; positivity cannot replace the adjoint proof.
2. Multiplying the finite weighted generator by 1/N leaves its vacuum measure unchanged and collapses its gap to 2/N. The energy coefficient must remain source-derived and fixed.
3. Appending an unobserved state with energy 1/N preserves every old-core calculation but violates the claimed global gap. Dense-core identification, not a finite list of observables, excludes such an extension.

The analytic closability and closure-limit arguments are written proofs using standard Hilbert-space facts; the checker does not mechanically prove these all-domain statements or independently review their upstream hypotheses.

**Disposition:** the closed thermodynamic gradient form and its source-unit spectral inequality are supplied at the fixed strong-coupling lattice scope. The enabled successor is actual finite-box propagator/form-limit comparison on changing vacuum Hilbert spaces. It must establish a genuine limit theorem rather than rebrand core convergence as one.

Packet: `research/kitaev/contracts/yang-mills-thermodynamic-form.v1.json`.
Reproduce: `python research/kitaev/checkers/check_yang_mills_thermodynamic_form.py`.
Receipt: `research/kitaev/results/yang-mills-thermodynamic-form-v1.json`.
