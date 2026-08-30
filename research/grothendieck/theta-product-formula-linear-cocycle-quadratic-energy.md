# Product formula cancels linear seam charge and leaves quadratic energy

## 1. Placewise displacement

For \(q\in\mathbb Q_{>0}\), define its oriented scale displacement at each
place by

\[
  \lambda_v(q)=\log|q|_v.
\]

At the real place,

\[
  \lambda_\infty(q)=\log q,
\]

while at a finite prime,

\[
  \lambda_p(q)=-v_p(q)\log p.
\]

Only finitely many finite-place terms are nonzero.

Each \(\lambda_v\) is an additive one-cocycle for multiplicative transport:

\[
  \lambda_v(qr)=\lambda_v(q)+\lambda_v(r).
\]

The global product formula is exactly

\[
  \boxed{\sum_v\lambda_v(q)=0.}
\]

## 2. Linear Green anomalies

Suppose a moving-boundary Green calculation produces at every place the same
oriented linear seam charge

\[
  B_v(q)=c\,\lambda_v(q)
\]

for a source-fixed coefficient \(c\). Then adelic completion cancels it:

\[
  B_{\mathbb A}(q)
  =
  \sum_vB_v(q)
  =
  c\sum_v\lambda_v(q)
  =0.
\]

This gives a precise mechanism for the cancellation of sheet-odd first
moments encountered in the bilateral Clark/Green calculation. The real seam
term does not disappear internally; it is the archimedean component of a
globally neutral arithmetic charge.

The coefficient matching is essential. If the local normalizations differ,
the product formula does not apply. Thus Haar, additive-character, and Green
orientations must be derived from one adelic normalization.

## 3. A positive quadratic candidate

The simplest corresponding quadratic quantity does not cancel:

\[
  \mathcal E(q)
  =
  \sum_v\lambda_v(q)^2
  \ge0.
\]

It vanishes only for \(q=1\). For \(q=p^m\),

\[
  \mathcal E(p^m)
  =
  2m^2(\log p)^2.
\]

Thus there exists a natural-looking refinement that converts a neutral
first-order charge into a strictly positive second-order separation energy:

\[
\boxed{
\sum_v\lambda_v=0,
\qquad
\sum_v\lambda_v^2>0\quad(q\ne1).}
\]

This is the simplest candidate explanation for why order two is special.
The first variation is killed by global integrality; the second variation
measures how far a nontrivial rational transport separates its place labels.

## 4. Relation to the recurring curvature

The theta programme repeatedly reduced to a squared separation:

\[
  -\mathscr C_F(z)
  =
  \frac12
  \iint (u-v)^2
  \Phi(u)\Phi(v)e^{iz(u+v)}\,du\,dv.
\]

The adelic quadratic energy has the same formal origin. A transport label has
a place vector

\[
  \lambda(q)=(\lambda_v(q))_v
\]

lying in the charge-zero hyperplane. The counting-weight Euclidean norm is
\(\mathcal E(q)\). If the local Green forms derive precisely this metric,
the order-two source measure can be interpreted as the pushforward of
pairwise place-separation energy after scalar archimedean compression.

This does not yet orient the oscillatory transform, but it identifies the
positive quantity before projection:

\[
  \text{adelic charge-zero displacement}
  \longrightarrow
  \text{positive squared norm}
  \longrightarrow
  \text{oscillatory scalar curvature}.
\]

## 5. Metric-selection obstruction

The product formula selects the hyperplane

\[
  \sum_v\lambda_v=0,
\]

but it does not select a quadratic metric on that hyperplane. For every
positive weight packet \(c_v\), the form

\[
  \mathcal E_c(q)
  =
  \sum_v c_v\lambda_v(q)^2
\]

is positive and has the same zero set. Cross-place positive forms give still
more alternatives. Therefore positivity and charge cancellation alone do
not privilege \(\mathcal E\).

The correct metric must be derived from the normalized local Green forms,
Haar measures, and completed vacuum. This is a new authority gate:

\[
\boxed{
\text{product formula selects neutrality, not energy geometry}.}
\]

## 6. Deutsch--Popperian conjecture

**Adelic quadratic Green conjecture.** The completed theta boundary has a
placewise Green cocycle whose degree-one part is the product-formula charge
and whose degree-two polarization is a positive Hilbert-module energy. After
rational descent, its archimedean determinant shadow is the complete
Laguerre/de Branges curvature hierarchy of \(X\).

The conjecture explains rather than assumes:

1. why linear seam defects cancel;
2. why the first nontrivial invariant is quadratic;
3. why prime logarithms enter as displacement lengths; and
4. why scalar oscillation appears only after forgetting the finite-place
   direction of the displacement vector.

## 7. Immediate falsifiers

The conjecture fails at its first gate if:

1. the exact local Green seam terms are not proportional to
   \(\lambda_v(q)\) with one global normalization;
2. the placewise quadratic polarization has indefinite cross terms;
3. rational descent destroys closability of the energy form; or
4. its scalar compression yields only a universal covariance unrelated to
   the theta curvature; or
5. the purported quadratic energy is selected only by positivity rather than
   by the local source forms.

Product-formula cancellation alone is insufficient: it controls degree one,
whereas RH requires orientation of the compressed all-orders comparison.

## 8. Scope

The additive cocycle, product-formula cancellation, and positivity of every
displayed weighted quadratic form are exact. The product formula does not
select among those forms. Identification with the previously found sheet-odd
term and selection of the theta metric remain architectural until the local
Green normalizations are derived. No Hilbert-module energy, curvature
identity, determinant comparison, or RH theorem is claimed.
