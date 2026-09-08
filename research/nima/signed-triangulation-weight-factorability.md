# Signed triangulation-weight factorability

## Question

When can signs of real triangulation coefficients be absorbed into signs of labelled facet equations?

## Claim boundary

This is an `F2` incidence problem for nonzero real weights. Magnitudes obey the positive-real binomial gate separately; complex phases require another coefficient group.

Write each facet sign as `(-1)^(s_c)` and each triangulation sign as `(-1)^(e_T)`. Factorability is the linear system

\[
e=A s\pmod 2.
\]

It holds exactly when `e` is orthogonal to every vector in the `F2` left kernel of the triangulation-channel incidence matrix. Each kernel vector says that the product of a specified set of triangulation signs must be positive.

Exact row reduction over `F2` is performed directly, without using rational rank. At five points the cyclic pair-incidence matrix has rank four rather than rational rank five. Its one sign invariant is

\[
\prod_{T=1}^{5}\operatorname{sign}(w_T)=+1.
\]

Thus a single negative five-point coefficient cannot be absorbed by real facet signs, even though arbitrary positive magnitudes can be absorbed at five points. The checker also records the independent sign-relation counts at four, six, and seven points and verifies every displayed kernel vector against every channel column.

## Disposition

Real coefficient comparison requires two gates: positive magnitudes must satisfy the rational logarithmic binomials, and signs must satisfy the `F2` parities. The five-point sign product is already scale-invariant and must be included in the source-embedding acceptance test.
