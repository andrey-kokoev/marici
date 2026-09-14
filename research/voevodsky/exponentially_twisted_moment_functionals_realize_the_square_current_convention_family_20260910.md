# Exponentially twisted moment functionals realize the square-current convention family

## Question

Can the prime-square row be placed in an explicit analytic transpose range without choosing between repository conventions that retain or suppress a logarithmic multiplicity factor?

## Claim boundary

Yes. Every row of the form \(P(\log p)p^{-1}\), with \(P\) a fixed polynomial, is the pullback of a finite linear combination of exponentially twisted moments on translated cut atoms. This covers both the constant \(p^{-1}/2\) square endpoint coefficient and the \((\log p)p^{-1}\) current convention. It does not identify which convention an undeclared external G4 interface uses.

## Problem

With primitive synthesis columns

\[
Ke_p=p^{-1/2}c_{\log p},
\qquad
c_a(q)=\Phi(q-a),
\]

a square row

\[
b_p=P(\log p)p^{-1}
\]

requires an analytic functional \(L_P\) satisfying

\[
L_P(c_a)=P(a)e^{-a/2}.
\]

## Bold conjecture

An untwisted finite moment functional is sufficient for the square row.

## Named rivals

1. Half-density decay requires the source-derived exponential twist \(e^{-q/2}\).
2. The constant and logarithmic square conventions require unrelated analytic functionals.
3. A fitted primewise functional is necessary because translated packets do not generate exponential-polynomial sequences.

## Twisted moments

For \(j\ge0\), define

\[
M_j^-(f)=\int_{\mathbb R}q^je^{-q/2}f(q)\,dq.
\]

Let

\[
\mu_j^-=
\int_{\mathbb R}u^je^{-u/2}\Phi(u)\,du.
\]

Translation gives

\[
M_j^-(c_a)
=e^{-a/2}
\sum_{r=0}^j
\binom jr a^{j-r}\mu_r^-.
\]

The coefficient of \(a^j\) is \(e^{-a/2}\mu_0^-\). For the positive Gaussian source, \(\mu_0^->0\). Therefore the triangular map from

\[
(M_0^-,\ldots,M_m^-)
\]

to

\[
e^{-a/2}(1,a,\ldots,a^m)
\]

is invertible. Every fixed polynomial \(P\) has a unique functional

\[
L_P=\sum_{j=0}^{\deg P}\lambda_jM_j^-
\]

such that

\[
L_P(c_a)=P(a)e^{-a/2}.
\]

Thus the two square conventions are members of one source-generated moment family rather than unrelated repairs.

## Continuity rung

For degree \(m\), use a half-density position graph whose norm contains

\[
\|(1+q^2)^{(m+1)/2}e^{-q/2}f\|_2.
\]

Then

\[
|M_j^-(f)|
\le
\left\|
\frac{q^j}{(1+q^2)^{(m+1)/2}}
\right\|_2
\|(1+q^2)^{(m+1)/2}e^{-q/2}f\|_2
\]

for \(0\le j\le m\), after increasing the polynomial exponent by one when required at the endpoint degree. This is precisely an exponentially conjugated position graph, compatible with the already declared half-density history spaces.

The untwisted-moment conjecture fails because it produces polynomials in \(a\) but not the required factor \(e^{-a/2}\).

## Transpose identity

For \(a=\log p\),

\[
(K'L_P)_p
=p^{-1/2}L_P(c_{\log p})
=p^{-1/2}P(\log p)p^{-1/2}
=P(\log p)p^{-1}.
\]

Hence

\[
b_P\in K'(\mathcal G_{-,m}'),
\]

where \(\mathcal G_{-,m}\) is the corresponding exponentially twisted position graph.

For the endpoint normalization \(P=1/2\), only \(M_0^-\) is needed. For the logarithmic-current normalization \(P(a)=a\), a centered combination of \(M_0^-\) and \(M_1^-\) suffices.

## Adams covariance

Grade raising sends \(a=k\log p\) to \(ra\). The exponential-polynomial family transforms by

\[
P(a)e^{-a/2}
\longmapsto
P(ra)e^{-ra/2}.
\]

This stays inside the finite twisted-moment module of the same polynomial degree, with the Euler cocycle providing the relative factor. The transpose family therefore carries the required finite-dimensional Adams action without a primewise fit.

## Strongest residual

The construction assumes one common translated atom and the negative half-density conjugation. If the square analytic column uses a different source packet, its twisted moments must be computed separately. Equality of coefficient decay alone does not identify the packets.

The external G4 convention remains a source-identification question. The range theorem covers either named coefficient once its local column is the retained translated theta cut atom.

## Disposition

Square-current analytic provenance is constructed for the complete convention family \(P(\log p)p^{-1}\) on exponentially twisted position-graph duals. The primitive and square rows now occupy distinct but compatible dual rungs: untwisted centered position moment for the primitive row, half-density-twisted moments for the square row. Connected and archimedean rows remain to be classified.
