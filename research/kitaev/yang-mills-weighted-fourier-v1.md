# Iteration 8 — frequency-weighted repair and the remaining support loss

## Question and disposition

Can the nonlinear remainder map rejected in iteration 7 be bounded in a representation-weighted norm, without concealing the volume dependence in a constant?

**Yes globally:** a weighted Fourier-algebra norm gives a frequency- and volume-independent quadratic map bound. It constructs the actual finite-source log ground function when |lambda/kappa| times the plaquette count is less than1/96.

**Not yet locally:** the source is extensive in the whole-box norm. Its link-anchored norm is bounded independently of volume, but the proved overlap estimate requires an extra support-cardinality moment. No anchored contraction or fixed-coupling uniform remainder is obtained. `faithful-excitation-detection` stays open.

[Contract](contracts/yang-mills-weighted-fourier.v1.json). This is a repair of a specific proof space, not a new physical regulator or a claimed continuum limit.

## Explicit norm and imported harmonic analysis

For a product SU(2) irrep pi with spins j_e define J_pi=sum_e j_e, C_pi=sum_e j_e(j_e+1), and d_pi its dimension. With normalized Haar Fourier coefficients use

\[
\|f\|_{A^s}=\sum_\pi (1+J_\pi)^s d_\pi
\|\widehat f(\pi)\|_{trace},\qquad s=0,1.
\]

A0 is the compact-group Fourier algebra. Absolute Fourier summation controls sup norm. The A1 weight also controls every first left-invariant derivative, so A1 embeds in C1 at each finite graph. All modes are retained; there is no finite-spin completion shortcut.

Unitary Clebsch–Gordan decomposition, trace-class coefficient norms and compact-group Fourier inversion are imported standard harmonic analysis. In a tensor product, total spin of any output obeys J_output<=J_input1+J_input2. Thus1+J_output<=(1+J_input1)(1+J_input2), and A0,A1 are Banach algebras. Haar centering deletes the trivial Fourier block and has norm at most1. These facts apply also before imposing gauge invariance.

## The derivative product and inverse estimates

For a fixed edge and unit Lie generator, the representation generator has operator norm j_e. Hence, with m_e(f)=sum_pi j_e d_pi ||fhat(pi)||_trace,

\[
\|X_{ea}f\|_{A^0}\le m_e(f),\qquad
\sum_e m_e(f)\le\|f\|_{A^1}.
\]

There are three Lie directions per edge. The algebra inequality therefore gives

\[
\|\Gamma(f,g)\|_{A^0}
\le3\sum_e m_e(f)m_e(g)
\le3\|f\|_{A^1}\|g\|_{A^1}.
\]

For a physical nonconstant Fourier block, Gauss invariance prohibits degree-one nontrivial support. The source graph has girth four, so at least four nontrivial spins occur and J_pi>=2. Also C_pi>=3J_pi/2, since each nonzero SU(2) spin is at least one half. Consequently

\[
(1+J_\pi)/C_\pi\le1
\]

on all nonzero physical blocks. The centered inverse therefore satisfies

\[
\|L^{-1}h\|_{A^1}\le\|h\|_{A^0}.
\]

For general kinematic nonconstant blocks the safe constant is2 instead; it must not be substituted silently for the physical argument. Combining the physical inverse with the derivative estimate proves

\[
\boxed{\|B(f,g)\|_{A^1}\le3\|f\|_{A^1}\|g\|_{A^1},
\quad B(f,g)=L^{-1}\Gamma(f,g)_c.}
\]

The scalar Gamma of physical functions is invariant even though the individual derivative components are not. The inverse and centering preserve this sector. This proves the global estimate that failed in the sup-norm-only space. High frequencies are now charged in the input norm.

## An actual fixed-point construction, with its volume cost visible

Each elementary plaquette trace is the sum over16 index choices of four fundamental matrix-coefficient products. Each factor has A0 norm1, regardless of whether the link is forward or inverse; the fixed Fourier support has J=2. Hence its A1 norm is at most48. This is an upper bound, not an unsupported exact trace norm after partial inversion. For P plaquettes,

\[
\|S/6\|_{A^1}\le8P.
\]

On real invariant mean-zero A1 functions the actual log equation is

\[
u=rL^{-1}S/2+B(u,u)=rS/6+B(u,u).
\]

Set alpha=8|r|P and R=2alpha. The ball of radius R is preserved because alpha+3R squared<=R when12alpha<=1. The Lipschitz constant is at most6R=12alpha. Thus for

\[
|r|P<1/96
\]

the map is a strict contraction. Its solution has norm at most16|r|P.

This is a solution of the actual source equation, not a Taylor surrogate. Exponentiating the real bounded C1 solution gives a strictly positive H1 weak eigenfunction. The distributional chain rule and the continuous right-hand side justify the weak Schrödinger equation; elliptic regularity makes it smooth. Uniqueness of the positive compact-source ground eigenfunction identifies it with the actual Omega, up to normalization. No prior mass-gap assumption enters this identification.

The permitted r interval shrinks as1/P. This does not prove a nonzero fixed-coupling thermodynamic regime. In this tiny global window the earlier elementary min–max estimate already gives a stronger gap bound than the density comparison; the contribution here is a controlled proof space and actual log-wavefunction construction, not an improved spectral estimate.

## Passing to anchored interactions: an explicit unresolved loss

Decompose functions into connected-support interactions Phi_A. Define

\[
N(\Phi)=\sup_e\sum_{A\ni e}\|\Phi_A\|_{A^1},
\quad N_{card}(\Phi)=\sup_e\sum_{A\ni e}|A|\|\Phi_A\|_{A^1}.
\]

These are norms on specified interaction decompositions, not a claim that a canonical decomposition has already been constructed for the full ground function. The source decomposition into plaquettes has N(S/6)<=4 times8=32, independently of volume.

Assign B(Phi_A,Psi_B) to A union B. It vanishes if the edge supports are disjoint and otherwise preserves connected support. To bound output terms containing an anchored edge, split whether the edge lies in A or B. For each A, sum over overlap links j in A to bound all B meeting A. The result is

\[
N(B(\Phi,\Psi))\le3\bigl[
N_{card}(\Phi)N(\Psi)+N(\Phi)N_{card}(\Psi)\bigr].
\]

This is volume independent but not closed in N alone. A support weight can absorb a cardinality factor only with a change of weight or an additional moment; such a change must be accounted for in an iteration. No fixed-point theorem in the anchored norm is asserted. The bound may be improvable by retaining the edge-resolved frequency information instead of taking the coarse global quadratic estimate; the current result does not prove that the support loss is unavoidable.

## Exact controls, strongest residual and next operation

The checker verifies Fourier fusion dimension/weight inequalities, physical inverse ratios on a family of seven-link spin assignments, the source index-count bound, and the contraction inequalities at rational parameters. It also checks the overlap-cardinality estimate on explicit finite interaction supports. These regressions accompany the all-spin harmonic-analysis proof; no sampled mode range replaces it.

The frequency problem has been repaired. The strongest unresolved residual is now precisely the anchored cardinality loss, not an unnamed 'coherence' or 'completion' premise. Next retain edge-resolved frequency weights or use a rigorously controlled interaction-norm scale, and prove a closed majorant estimate before asserting convergence.

`faithful-excitation-detection` remains open, as do continuum construction and the independent atomic source. No fixed-coupling volume-uniform remainder or continuum gap is exported.

Reproduce: `python research/kitaev/checkers/check_yang_mills_weighted_fourier.py`.
Receipt: `research/kitaev/results/yang-mills-weighted-fourier-v1.json`.
