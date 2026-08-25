# Dilation separates the test state from the arithmetic zeta spectrum

Author: `marici.Grothendieck`

## 1. Universal matrix coefficient

Let \(h\in\mathcal S(\mathbb R)\) be even with \(h(0)=0\), and define

\[
 \mathcal A_h(u)
 =
 \langle\Delta_{\mathbb Z},R_uh\rangle
 =
 e^{u/2}\sum_{n\in\mathbb Z}h(ne^u).
\]

Put

\[
 s=\frac12+iz.
\]

In the initial Mellin convergence chamber,

\[
\begin{aligned}
 \int_{\mathbb R}\mathcal A_h(u)e^{izu}\,du
 &=
 2\sum_{n\ge1}
 \int_0^\infty h(nx)x^{s-1}\,dx\\
 &=
 2\sum_{n\ge1}n^{-s}
 \int_0^\infty h(y)y^{s-1}\,dy.
\end{aligned}
\]

Therefore

\[
\boxed{
 \mathcal X_h(s)
 =
 2\zeta(s)\mathcal M[h](s).}
\]

This is a universal separation law for the dilation matrix coefficient of the
integer comb.

## 2. The minimal theta state supplies only the local factor

For

\[
 h=f=D(D+1)e^{-\pi x^2},
\]

\[
 \mathcal M[f](s)
 =
 \frac12s(s-1)\pi^{-s/2}\Gamma(s/2).
\]

Hence

\[
 \mathcal X_f(s)
 =
 s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)
 =
 2\xi(s).
\]

The state-side minimal Euler operator explains the completion polynomial,
gamma factor, reciprocal center, and absence of unwanted local factors. But
the nontrivial zeta divisor is carried by the arithmetic comb factor
\(\zeta(s)\).

## 3. Responsibility for zeros

If \(\mathcal M[h](s)\) is nonzero in the open critical strip, then

\[
 \mathcal X_h(s)=0
 \quad\Longleftrightarrow\quad
 \zeta(s)=0
\]

there. Changing the archimedean test state within this zero-free Mellin class
does not change the nontrivial zero locations.

Conversely, a higher-Hermite state may insert additional polynomial or local
Mellin zeros, but it cannot remove an off-line zeta zero without itself
containing a cancelling pole, which an entire Mellin factor from a Schwartz
state does not provide.

Therefore:

\[
\boxed{
\text{minimal-state rigidity protects the completion presentation;}
\quad
\text{RH orientation belongs to the arithmetic boundary spectrum}.}
\]

## 4. Explanation of the earlier rank-one collapse

The separation

\[
 \mathcal X_h(s)=2\zeta(s)\mathcal M[h](s)
\]

is the scalar manifestation of multiplicity one for even dilation spectrum.
At each spectral parameter, the state contributes one scalar Mellin
amplitude and the comb contributes one scalar arithmetic amplitude. Their
cross-spectrum is their product.

This explains why the two-vector positive spectral lift was fiberwise rank
one and why no strict Schur complement could appear.

## 5. Consequence for the metaplectic programme

The real metaplectic representation has achieved an exact Explanation of:

1. the completed source;
2. reciprocal symmetry;
3. the half and quarter shifts;
4. the archimedean gamma factor;
5. the admissible state;
6. integral sampling; and
7. the distributional arithmetic boundary.

But its one-place dilation spectrum leaves the global arithmetic coefficient
as \(\zeta(s)\). A proof of RH must use structure internal to that coefficient
which is invisible after replacing the comb by one scalar Mellin amplitude.

The next rotation must therefore expose the multiplicative/prime
factorization of the comb.

## 6. Adelic reformulation target

The natural enlarged object is the global restricted tensor product:

\[
 \text{real Gaussian/minimal descendant}
 \ \widehat\otimes\
 \prod_p\text{integral }p\text{-adic vacuum},
\]

with the rational lattice embedded diagonally and global Fourier duality
acting place by place.

In such a formulation:

- the real place supplies the gamma and quarter-floor carrier;
- finite places supply Euler factors;
- the product formula supplies global coherence;
- the diagonal rational boundary replaces an independently inserted prime
  sequence; and
- the explicit-formula/Weil quadratic form becomes the candidate global
  positivity law.

This is structurally the next necessary enlargement, not optional abstraction.

## 7. Hostile criterion

Any proposed real-place positivity proof that uses only

\[
 f,\quad\Delta_{\mathbb Z},\quad\mathcal F,\quad R_u
\]

must confront the separation formula. If its inequality would hold for every
test state with zero-free Mellin transform, it has not supplied new control of
\(\zeta(s)\).

The proof must instead constrain the arithmetic amplitude itself, for example
through:

1. all-prime local positivity;
2. a global product-formula cancellation;
3. an adelic self-dual cone;
4. a Weil explicit-formula quadratic form; or
5. a source-derived scattering operator on the idele class group.

## 8. Scope

The universal separation formula and assignment of the archimedean and
arithmetic factors are exact in the convergence chamber and continue with the
completed source under the established hypotheses. The adelic carrier and
global positive law are research targets. No arithmetic coercivity or RH
theorem is claimed.
