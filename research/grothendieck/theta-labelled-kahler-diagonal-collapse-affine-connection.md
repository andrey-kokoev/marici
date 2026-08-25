# Orthogonal label lifting collapses; the affine scale connection is flat

## 1. Naive labelled lift

Write the positive theta source as

\[
  \Phi(u)=\sum_n\Phi_n(u),
  \qquad \Phi_n(u)\ge0.
\]

The most direct label-preserving Hilbert space is

\[
  \mathcal H_{\mathrm{lab}}
  =
  \bigoplus_n L^2(\mathbb R),
\]

with vacuum

\[
  \Omega_{\mathrm{lab}}(n,u)=\Phi_n(u)^{1/2}.
\]

Let logarithmic position act diagonally:

\[
  (Q\Psi)(n,u)=u\Psi(n,u).
\]

Then

\[
  \|e^{izQ}\Omega_{\mathrm{lab}}\|^2
  =
  \sum_n\int\Phi_n(u)e^{-2\operatorname{Im}(z)u}\,du
  =
  \int\Phi(u)e^{-2\operatorname{Im}(z)u}\,du.
\]

Consequently its projective Kähler potential and Fisher metric are exactly
the aggregated scalar ones.

\[
\boxed{
\text{orthogonal label retention}
+\text{one common character}
\longrightarrow
\text{scalar metric again}.}
\]

Merely enlarging the Hilbert space does not preserve relational information
in the observable geometry.

## 2. Source scale transport

Theta labels obey a translated-source law of the form

\[
  \Phi_n(u)=n^{-1/2}\Phi_1(u+\log n)
\]

with the precise carrier normalization fixed upstream. Let \(T_a\) denote
translation by \(a\):

\[
  (T_af)(u)=f(u+a).
\]

The logarithmic position and scale transport satisfy

\[
  QT_a-T_aQ=-aT_a.
\]

For \(a=\log n\),

\[
  [Q,T_{\log n}]
  =-(\log n)T_{\log n}.
\]

This commutator retains exactly the label displacement that the diagonal
Kähler norm erased.

## 3. Flatness among arithmetic shifts

Scale translations commute:

\[
  T_{\log m}T_{\log n}
  =
  T_{\log(mn)}
  =
  T_{\log n}T_{\log m}.
\]

Therefore the connection has no two-prime curvature:

\[
  [T_{\log p},T_{\log q}]=0.
\]

Its only curvature-like datum is the central affine commutator with \(Q\).
That relation depends on displacement but not on the special theta vacuum.
It holds for every translated-source family.

Thus the bare labelled connection is still universal:

\[
\boxed{
\text{label shifts recover displacement,}
\quad
\text{but their affine connection is flat}.}
\]

This recovers arithmetic grammar and prime logarithms without orienting the
oscillatory overlap.

## 4. Where nontrivial holonomy can enter

The source has one operation not present in the flat translation semigroup:
reciprocal Fourier/Poisson sewing. It exchanges translation with modulation
and moves the endpoint chart. A closed loop using both operations can have
nontrivial phase or seam holonomy:

\[
  \text{translate}
  \to
  \text{Fourier quarter-turn}
  \to
  \text{dual translate}
  \to
  \text{inverse quarter-turn}.
\]

For ordinary Weyl transport this loop returns the Heisenberg central
character. For completed theta transport it must additionally retain the
moving-endpoint seam cocycle and finite-place label.

This mixed loop, not the diagonal covariance, is the smallest place where a
source-specific operator-valued curvature can live.

## 5. Revised target and falsifier

Compute the labelled mixed holonomy before vacuum aggregation. Separate:

1. the universal Weyl phase;
2. the product-formula-neutral rational phase;
3. the moving-endpoint seam contribution; and
4. any residual theta-vacuum curvature.

If only the first two terms remain, the operator-valued lift is universal and
cannot imply RH. If the residual is merely the scalar \(X'/X\), it is
circular. A viable result must be a positive or maximality-bearing operator
relation whose hostile Fourier-stable source fails before its zeros are
examined.

## 6. Scope

The diagonal-collapse identity, affine commutator, and flatness of arithmetic
translations are exact. They show why a labelled direct sum is insufficient
and isolate mixed metaplectic seam holonomy as the first nontrivial target.
No such holonomy inequality, boundary maximality, determinant identity, or RH
theorem is established.
