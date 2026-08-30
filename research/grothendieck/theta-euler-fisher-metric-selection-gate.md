# Positive Fock grammar selects the Euler Fisher metric

## 1. Metric-selection question

The adelic product formula selects the charge-zero hyperplane but not a
quadratic form on it. In the Euler chamber, the positive symmetric-power
source supplies the missing metric canonically.

For a prime \(p\), put

\[
  x_p=p^{-s},
  \qquad \Re s>1.
\]

The local Euler factor

\[
  Z_p(s)=\frac1{1-x_p}
\]

is the partition function of the geometric occupation law

\[
  \Pr_s(N_p=k)
  =(1-x_p)x_p^k,
  \qquad k\ge0.
\]

This probability law is not fitted: it is exactly the positive
symmetric-power/Fock grammar of one primitive prime generator.

## 2. Canonical local quadratic form

The score for variation of \(s\) is

\[
  \partial_s\log\Pr_s(N_p=k)
  =
  -(\log p)\bigl(k-\mathbb E_sN_p\bigr).
\]

Therefore its Fisher information is

\[
  I_p(s)
  =
  (\log p)^2\operatorname{Var}_s(N_p)
  =
  (\log p)^2
  \frac{p^{-s}}{(1-p^{-s})^2}.
\]

Direct differentiation gives the same quantity:

\[
  I_p(s)=\partial_s^2\log Z_p(s)>0
  \qquad(s>1).
\]

Thus the prime source selects both the \((\log p)^2\) displacement weight and
its occupation-dependent coefficient. The previously arbitrary quadratic
form becomes the covariance metric of the labelled source.

## 3. Global Euler metric

Absolute convergence in \(\Re s>1\) permits summation:

\[
  \partial_s^2\log\zeta(s)
  =
  \sum_p I_p(s)
  =
  \sum_{p,k\ge1}
  k(\log p)^2p^{-ks}
  >0
\]

on the real Euler ray. Equivalently, this is the variance of the total
logarithmic prime occupation in the product Gibbs state.

The metric is diagonal in primitive prime labels. Mixed composite paths
exist in the tensor/Fock state but do not become new primitive directions.
This preserves the distinction \(\Lambda(p^k)=\log p\) and
\(\Lambda(pq)=0\).

## 4. Relation to theta curvature

For any positive exponential family,

\[
  \partial_s^2\log Z
  =
  \operatorname{Var}_s(\text{logarithmic scale}).
\]

The source-side squared separation identity is the two-copy form of this
variance:

\[
  \operatorname{Var}(U)
  =
  \frac12\mathbb E(U-V)^2.
\]

Hence the recurring curvature

\[
  FF''-(F')^2
\]

is not merely reminiscent of a metric. In a positive convergence chamber it
is precisely the unnormalized Fisher covariance of two independently labelled
source copies.

## 5. Completion obstruction

This theorem does not extend automatically to the critical strip. The Euler
product probability state ceases to exist there as a normalizable product
measure, and analytic continuation of
\(\partial_s^2\log\zeta(s)\) need not preserve a covariance interpretation.
Endpoint and gamma completion are coupled to the divergent prime degree.

Thus the Nima Lakatos closure remains intact:

\[
\boxed{
\text{positive Fock grammar selects the metric in the Euler chamber;}
\quad
\text{it does not orient its completed continuation}.}
\]

The unresolved object is still the coupled remainder
\(C_Y\), now interpretable as the obstruction to descending the finite Euler
Fisher metrics to one positive completed adelic metric.

## 6. Sharpened target

For a finite prime set \(S\), form the exact product probability state and
its Fisher form \(I_S\). Add the archimedean completed source before taking a
limit. The desired theorem is not termwise convergence of
\(\sum_pI_p\), but convergence of the renormalized all-place form after the
product-formula null direction has been quotiented:

\[
  I_{\mathbb A}^{\mathrm{ren}}
  =
  \lim_S
  \left(
    I_\infty^{(S)}
    +\sum_{p\in S}I_p
    -\text{shared degree counterterm}
  \right)
  \ge0.
\]

Every term and counterterm must be derived from the completed source. If this
limit exists as a closed positive form, it supplies the missing metric
selection and a precompression orientation law. If it equals the Weil/Pick
form only after assuming RH, the construction is circular.

## 7. Falsifiers

The programme fails if:

1. the archimedean counterterm is not uniquely source-selected;
2. two admissible exhaustions give inequivalent renormalized forms;
3. the limit has a negative direction;
4. the product-formula null line is not the complete divergent direction; or
5. positivity can be stated only after scalar analytic continuation.

## 8. Scope

The geometric occupation law, local Fisher identity, and positive Euler-ray
sum are exact for \(s>1\). Their covariance interpretation canonically selects
the quadratic metric in that chamber. No completed positive limit,
critical-strip continuation of the probability state, determinant identity,
or RH theorem is claimed.
