# GNS coherencer for rank-uniform prime control

## Question

What single higher object would make all finite-rank relative prime bounds coherent rather than a sequence of unrelated matrix estimates?

## Claim boundary

A bounded self-adjoint operator on the leading archimedean Hilbert completion is a sufficient higher object, but not a necessary one. The correct general object is a closable symmetric quadratic form bounded below by \(-1\), with an associated self-adjoint operator that may be unbounded above. Constructing this semibounded form remains open.

## Reference Hilbert space

Fix admissible \(t,h\). Let \(\mathcal P\) be the polynomial algebra in

\[
z=1-e^{-hr}.
\]

A separately proved positive leading archimedean form defines

\[
\langle p,q\rangle_\Gamma
=
\int
\overline{p(z(r))}q(z(r))
\,d\mu_{\Gamma,t,h}(r).
\]

After quotienting its null space and completing, obtain the GNS Hilbert space

\[
\mathcal H_{\Gamma,t,h}.
\]

## Coupled gamma-remainder and prime form

Let

\[
\mathfrak p_{t,h}(p,q)
\]

be the coupled sesquilinear form consisting of the gamma remainder plus the source-regularized prime contribution. The full gamma form is not assumed positive. A rank-uniform relative bound is precisely the existence of \(C<\infty\) such that

\[
|\mathfrak p_{t,h}(p,q)|
\leq
C
\lVert p\rVert_\Gamma
\lVert q\rVert_\Gamma
\]

for all polynomials.

If this holds, the Riesz theorem produces a bounded operator

\[
T_{P,t,h}:
\mathcal H_{\Gamma,t,h}
\longrightarrow
\mathcal H_{\Gamma,t,h}
\]

with

\[
\mathfrak p_{t,h}(p,q)
=
\langle p,T_{P,t,h}q\rangle_\Gamma.
\]

Reality and symmetry of the prime form make \(T_{P,t,h}\) self-adjoint.

## Finite observers

Let \(G_N\) and \(P_N\) be the archimedean and prime matrices on polynomials of degree below \(N\). The normalized finite observer is

\[
T_N
=
G_N^{-1/2}P_NG_N^{-1/2}.
\]

Compatibility under polynomial inclusion and

\[
\sup_N\lVert T_N\rVert<\infty
\]

are sufficient to produce one bounded operator. They are not necessary for positivity: the upper spectral edges may diverge while every lower edge remains at least \(-1\). The general passage to one higher object instead requires a common dense core, a closable symmetric form, and a rank-uniform lower bound.

## Positivity criterion

Ignoring already controlled positive corrections, the completed form is

\[
\langle p,(I+T_P)p\rangle_\Gamma.
\]

Its all-rank positivity is equivalent to

\[
\inf\operatorname{spec}(I+T_P)
\geq0,
\]

or

\[
\inf\operatorname{spec}(T_P)
\geq-1.
\]

The stronger norm condition

\[
\lVert T_P\rVert<1
\]

is sufficient but not necessary.

## Coherence structure

The higher operator simultaneously observes all finite prime matrices through orthogonal compression. Conversely, the compatible finite matrices jointly determine the operator on the dense polynomial subspace when their norms are uniformly bounded.

The coherence residue has two components:

1. compatibility residue: whether degree restriction of \(P_{N+1}\) equals \(P_N\);
2. boundedness residue: whether \(\sup_N\lVert T_N\rVert\) is finite and whether the lower spectral edge stays above \(-1\).

The first should vanish algebraically from the common-measure formulation. The second contains the RH-strength analytic difficulty.

## Relation to near-null observers

The vectors \((1-y)^m\) test selected Rayleigh quotients of \(T_P\). Their Laguerre and frequency descriptions identify dangerous directions but do not control the full operator norm or lower spectral edge.

A proof must either:

- establish a uniform form bound on all polynomials;
- identify a core family whose span is dense and whose bounds extend by closure;
- or exhibit a structural factorization of \(I+T_P\) as a positive operator.

## Disposition

Rank-uniform quantitative coherence requires a closable coupled form on the leading archimedean GNS space whose associated self-adjoint operator is bounded below by \(-1\); boundedness in both spectral directions is only a sufficient special case. The next executable test is closability and a uniform lower form bound on the Bernstein polynomial core under the source regularization.

## Verification

- `research/voevodsky/checkers/check_gns_coherencer_rank_uniformity.py`
- `research/voevodsky/results/gns_coherencer_rank_uniformity.json`
