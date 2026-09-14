# Closed-range Hankel theory splits the Suzuki coercivity gate

## Search result

The indexed PDF corpus contains no source on closed-range Hankel operators, Hartman's compactness theorem, or Toeplitz-corona criteria. A web/Crossref search located only general Hankel spectral references, including work on essential spectra of Hankel operators with piecewise-continuous symbols and finite-rank Hankel classifications; it did not locate a theorem specialized to Suzuki's completed-zeta symbol.

The relevant standard operator facts nevertheless sharpen the gate without deciding it.

## Leakage is a Hankel-type compression

Suzuki's leakage operator is

\[
L=P_-K|_{H_+},
\qquad
K=\mathcal F^{-1}M_\Theta J\mathcal F.
\]

After moving to the Fourier/Hardy boundary realization and accounting for the conjugation/reflection convention in `J`, this is an off-diagonal Hardy compression of multiplication by `Theta`: a conjugate-linear Hankel-type operator. Its modulus and closed-range behavior are therefore governed by the associated linear Hankel compression.

The coercivity requested previously is

\[
\|Lf\|\ge c\|f\|
\qquad(f\perp\ker L).
\]

Equivalently,

\[
0\notin\sigma(L^*L|_{(\ker L)^\perp}).
\]

## Compact closed range forces finite rank

A basic Hilbert-space theorem gives

\[
\boxed{
L\text{ compact and }\operatorname{ran}L\text{ closed}
\Longrightarrow
\operatorname{rank}L<\infty.
}
\]

Indeed, closed range makes `L` bounded below on `(ker L)^perp`. If that subspace were infinite-dimensional, an orthonormal sequence in it would have images separated by the lower bound, contradicting compactness.

Consequently, if Suzuki's leakage can be shown both compact and infinite-rank, the desired closed-range coercivity is impossible.

## Standard symbol bifurcation

For ordinary Hankel operators, two classical mechanisms are relevant:

1. Hartman-type theorems characterize compactness by approximation of the symbol modulo the analytic algebra by continuous symbols.
2. Kronecker-type theorems characterize finite-rank Hankel operators by rationality of the nonanalytic symbol component.

Applied conditionally to the correctly normalized Suzuki compression, they give the implication

\[
\Theta\text{ in the compact-Hankel symbol class}
+
\Theta\text{ nonrational modulo the analytic class}
\Longrightarrow
L\text{ compact, infinite-rank, and not closed-range}.
\]

The completed-zeta ratio is not expected to have a rational nonanalytic component. Thus **if** its boundary regularity places it in the compact-Hankel class, the coercive route is closed rather than helped.

This conditional statement must not be promoted to a theorem about `Theta`: its behavior at infinity and membership in the relevant half-plane `H^infinity+C`/VMO-type algebra have not been established here.

## Noncompact alternative

If `Theta` is outside the compact-Hankel class, closed range remains possible but becomes an essential-spectrum/Fredholm question. The exact condition is a gap at zero for the nonzero singular spectrum of `L`:

\[
\sigma_{ess}(L^*L)
\subseteq\{0\}\cup[c^2,1].
\]

For a unimodular symbol this is closely related to Fredholm properties of complementary Toeplitz compressions and, in favorable symbol algebras, to invertibility/corona conditions. Such a theorem would be global boundary information about `Theta`, not a consequence of pointwise unimodularity.

## Angle formulation

Let

\[
M=H_+,
\qquad N=KH_+.
\]

The nonzero singular values of the off-diagonal leakage and the principal angles between `M` and `N` are complementary. Closed range of `L` is equivalent to a positive Friedrichs-angle separation away from the intersection. Therefore the dichotomy is:

- compact infinite-rank leakage: principal angles accumulate at zero and no coercive gap exists;
- closed-range leakage: the two Hardy subspaces have a uniform angle off `V`.

This geometric statement is independent of the chosen Hankel convention.

## Consequence for regularized shorts

When `L` has nonclosed range, the correction

\[
L^*(LL^*+\epsilon I)^{-1}L
\]

converges strongly but not uniformly to the projection onto `closure(ran L^*)`. Its inverse factor has norm of order `epsilon^{-1}`, and no cutoff-independent Green identity can pass through it using ordinary operator-norm estimates.

Thus the regularized projected kernels may be source-defined and positive for every `epsilon>0` while their correction vectors diverge and their limit carrier collapses.

## Next exact source test

Before seeking an endpoint--gamma--prime Green identity involving `(LL*)^dagger`, determine the boundary symbol class of

\[
\Theta=E^\#/E.
\]

The decisive alternatives are:

1. prove the associated leakage compact; then prove infinite rank, which rules out closed-range coercivity;
2. prove it noncompact and calculate or bound its essential singular spectrum near zero;
3. bypass inversion entirely by deriving the arithmetic Green identity at the regularized level with estimates uniform as `epsilon downarrow 0`.

The third is the only route compatible with nonclosed range.

## Disposition

Closed-range Hankel theory does not presently certify the Suzuki carrier. It exposes a sharp fork:

\[
\boxed{
\text{compact infinite-rank leakage}
\Longrightarrow
\text{no coercive pseudoinverse},
}
\]

while the noncompact case requires a new Fredholm/essential-spectrum theorem for the completed-zeta boundary symbol. The source regularity class of `Theta` is now the first unresolved analytic datum.
