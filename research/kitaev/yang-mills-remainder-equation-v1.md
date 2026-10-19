# Iteration 7 — exact connected remainder equation and a failed contraction norm

## Question and disposition

Can the uniform local coefficient bounds of iteration 6 be closed into an actual-source remainder estimate by a simple anchored sup-norm contraction?

**Rejected:** that proposed nonlinear norm bound. A smooth physical one-plaquette sequence has fixed support and uniformly bounded sup norm, while the centered inverse of its squared gradient has an unbounded low-character projection. The missing estimate is not merely a volume-counting issue: this norm already fails at fixed volume.

**Constructed:** the exact centered log-ground-state remainder equation and an all-order formal connected-support recursion. These identify an executable next problem, but do not prove convergence or a uniform gap. `faithful-excitation-detection` stays open.

[Contract](contracts/yang-mills-remainder-equation.v1.json). No Hamiltonian, vacuum, gauge quotient or units are replaced.

## The actual nonlinear equation

Put L=H0/kappa, r=lambda/kappa, S=sum of fundamental plaquette traces, and

\[
\Gamma(f,g)=\sum_{e,a}X_{ea}f\,X_{ea}g.
\]

For the real positive actual ground function Omega, write u=log Omega modulo an additive constant. The chain rule for the positive electric Laplacian is

\[
L(e^u)/e^u=Lu-\Gamma(u,u).
\]

The dimensionless eigen-equation is therefore Lu-Gamma(u,u)-rS/2=E0/kappa-rP. Integrating against Haar, <Lu>=<S>=0, so

\[
Lu=rS/2+\Gamma(u,u)_c,
\qquad f_c=f-\langle f\rangle_\mu.
\]

This centers against Haar, not against the unknown ground-weighted measure; changing that centering would change the equation.

Let u_star=r u1+r squared u2, where u1=S/6 and u2 is the mean-zero coefficient of log Omega supplied by iteration 6. Thus Lu2=Gamma(u1,u1)_c. The exact defect of u_star is

\[
Lu_* -rS/2-\Gamma(u_*,u_*)_c
=-2r^3\Gamma(u_1,u_2)_c-r^4\Gamma(u_2,u_2)_c.
\]

For the actual remainder w=u-u_star, with its additive constant fixed by Haar mean zero,

\[
\boxed{Lw=2r^3\Gamma(u_1,u_2)_c+r^4\Gamma(u_2,u_2)_c
+2\Gamma(u_*,w)_c+\Gamma(w,w)_c.}
\]

This is an exact equation at every finite graph and real source parameter, not an asymptotic assumption. A small-remainder solution still has to be proved in a suitable function space. The omitted normalized log probability density differs from 2w only by a constant, so its single- and mixed-link oscillations are precisely the corresponding oscillations of 2w.

The source terms through orders three and four have finite connected support by the known coefficients. Their local support alone does not control the inverse/nonlinear iteration.

## What can be proved about all orders without convergence

The formal Taylor coefficients, centered individually, satisfy

\[
u_1=S/6,\qquad
u_n=L^{-1}\sum_{k=1}^{n-1}\Gamma(u_k,u_{n-k})_c\quad(n\ge2),
\]

The electric inverse here is on the Haar mean-zero subspace. For a function of a finite link set A, the product heat semigroup and its centered integral representation preserve dependence on A. Thus L inverse preserves that support; it also preserves gauge invariance. Subtracting a constant does not enlarge support.

Gamma vanishes between edge-disjoint supports. Starting with single plaquettes, induction decomposes every order-n coefficient into functions supported on link-connected unions of at most n plaquettes, allowing a plaquette to be repeated in the perturbation order. Two clusters meeting only at a vertex have no gradient contraction. This proves formal connectedness at every order.

It does not bound the number or size of coefficient functions in a norm suitable for summing the series. Formal locality is weaker than convergence, and fixed-box analytic perturbation is weaker than uniform convergence in box size.

## A concrete failure of a sup-norm-only closure

Consider an anchored interaction norm built from the sums of sup norms of cluster functions containing a fixed link. A tempting missing lemma would be

\[
\|L^{-1}\Gamma(f,f)_c\|_{anchor}
\le C\|f\|_{anchor}^2
\]

with one constant independent of representation frequency and box size. This is false even when all functions have the same single-plaquette support.

Embed the observable in any source box: the other links do not enter it, so their electric derivatives vanish and the centered inverse preserves its four-link support. Use its conjugacy angle theta and x=cos theta. The full four-link electric operator on a class function is

\[
Lf=-(1-x^2)f''+3xf',\qquad
\Gamma(f,f)=(1-x^2)(f')^2.
\]

For n>=3 let

\[
f_n=\tfrac12[\cos(n\theta)+\cos((n+2)\theta)].
\]

These are smooth gauge-invariant Chebyshev trace polynomials on the actual plaquette source. They have Haar mean zero and sup norm at most1, independently of n. Their support never grows. Let chi2=4x squared-1. It has Haar mean0, norm1 and L chi2=8 chi2.

The exact Fourier/Haar calculation gives

\[
\langle\Gamma(f_n,f_n),\chi_2\rangle_\mu
=\frac{n(n+2)}8.
\]

One way to verify it is to use Gamma=(partial_theta f) squared and the normalized Haar weight (2/pi)sin(theta) squared. Only the cross-frequency cos(2 theta) term contributes for n>=3; the higher frequencies are orthogonal against the weight times chi2. Self-adjointness of the centered inverse then implies

\[
\left\langle L^{-1}\Gamma(f_n,f_n)_c,\chi_2\right\rangle
=\frac{n(n+2)}{64}.
\]

Since chi2 has norm1, the output L2 norm, hence its sup norm, is at least that growing quantity. The alleged anchored quadratic bound cannot hold on these fixed-support inputs. The constant subtracted in the centering has no effect on the chi2 projection.

This is not a low-energy sequence: the input frequencies grow. The actual electric gap is still3 kappa. The counterexample rejects an unrestricted sup-norm-only Banach-space estimate for the proof map, not spectral separation, an order-/frequency-weighted expansion, all cluster expansions, or the Yang–Mills hypothesis. Restricting the proof to a finite spin cutoff would hide rather than repair the missing frequency control.

## Exact verification and a safe next operation

The checker represents f_n as rational Chebyshev polynomials, applies the actual radial Casimir and carré du champ, and integrates exactly using the SU(2) moments <x^(2m)>=Catalan(m)/4^m. It verifies the projection formula for n=3,...,12, the test character normalization and the nonzero cubic/quartic defect on the one-plaquette source. The all-n Fourier argument above, not those ten fixtures, proves unboundedness.

It separately checks connected-support joins on finite box fixtures. Those checks regress the support induction; they do not assert that the formal series converges.

**Next operation:** choose a derivative- or representation-weighted connected norm. Prove its nonlinear product bound and centered inverse bound, tracking their support-size dependence, before using any fixed-point theorem. If those bounds cannot be supplied, another ready branch remains available; the actual-source uniform remainder must stay open.

No volume-uniform detection, convergent cluster expansion, continuum reconstruction or atomic claim occurs here.

Reproduce: `python research/kitaev/checkers/check_yang_mills_remainder_equation.py`.
Receipt: `research/kitaev/results/yang-mills-remainder-equation-v1.json`.
