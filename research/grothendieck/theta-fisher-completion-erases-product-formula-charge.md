# Raw prime Fisher completion erases the product-formula charge constraint

## 1. Weighted place-current space

Let \(V_{\mathrm{fin}}\) be the finite-support sequences
\((x_p)_p\). Give it the positive diagonal form

\[
  \|x\|_c^2=\sum_pc_p|x_p|^2,
\]

where \(c_p>0\) is the local source weight. For the critical geometric Fock
vacuum, the occupation variance is

\[
  c_p
  =
  \frac{p^{-1/2}}{(1-p^{-1/2})^2}
  \sim p^{-1/2}.
\]

Let \(\mathcal H_c\) be the Hilbert completion.

## 2. Charge functional

The unweighted product-formula charge on finite packets is

\[
  \varepsilon(x)=\sum_px_p.
\]

It extends continuously to \(\mathcal H_c\) exactly when

\[
  \sum_pc_p^{-1}<\infty.
\]

Indeed, this is the Riesz/Cauchy--Schwarz criterion for the coefficient
sequence \((1)_p\) in the dual weighted space.

At critical half-density,

\[
  c_p^{-1}\sim p^{1/2},
\]

so the sum diverges violently. If logarithmic charge weights \(\log p\) are
included instead, the continuity condition is even stronger and still
fails.

\[
\boxed{
\text{the product-formula charge is not continuous in the raw Fisher
topology}.}
\]

## 3. Density of charge-zero packets

The failure is operationally exact. Let \(x\in V_{\mathrm{fin}}\) and put

\[
  s=\varepsilon(x).
\]

Choose a prime \(q\) outside the support of \(x\), and define

\[
  x^{(q)}=x-se_q.
\]

Then

\[
  \varepsilon(x^{(q)})=0,
\]

while

\[
  \|x^{(q)}-x\|_c^2
  =
  c_q|s|^2
  \longrightarrow0
\]

as \(q\to\infty\), because \(c_q\to0\).

Therefore the algebraic charge-zero subspace is dense:

\[
  \boxed{
  \overline{\ker\varepsilon\cap V_{\mathrm{fin}}}^{\,\mathcal H_c}
  =
  \mathcal H_c.}
\]

Hilbert completion in the raw positive Fisher norm forgets the product
formula constraint.

## 4. Meaning

This is a concrete failure of contextual faithfulness:

\[
\text{finite labelled packets remember global charge}
\longrightarrow
\text{positive Hilbert completion forgets it}.
\]

The loss occurs because arbitrarily remote prime labels carry arbitrarily
small norm cost. A scalar or Hilbert observer cannot distinguish a charged
packet from a neutral packet whose compensator has escaped to infinity.

Thus the product formula cannot be imposed after this completion as an
ordinary closed hyperplane. Its kernel is not closed because its defining
functional is not continuous.

## 5. Required repair

A faithful all-place space must retain two topologies or a graph norm:

1. the positive Fisher/energy topology controlling local fluctuations; and
2. a charge topology in which \(\varepsilon\) is continuous.

Equivalently, use the closed graph of the charge map

\[
  x\longmapsto(\|x\|_c,\varepsilon(x))
\]

before imposing the product formula. The archimedean coordinate then supplies
the balancing charge as part of the graph, not as an independent positive
summand.

This suggests a relative or Krein/Pontryagin boundary space whose final
charge-zero quotient is positive, but the metric and domain must be derived
from the completed source.

## 6. Strong falsifier

Any proposed adelic Hilbert completion that uses only the local Fisher norm
and then declares the product formula as a closed boundary condition is
invalid: the condition has already become dense.

A viable construction must prove:

\[
  \varepsilon:
  \operatorname{Dom}\varepsilon
  \subset\mathcal H_{\mathrm{energy}}
  \longrightarrow\mathbb C
\]

is closed in a source-selected graph topology, and that rational transport
preserves this domain.

## 7. Scope

The dual continuity criterion and density proof are exact. They show that the
most natural positive prime Fisher completion is not faithful to global
integrality. No source-derived graph topology, all-place charge operator,
positive relative quotient, or RH theorem is constructed.
