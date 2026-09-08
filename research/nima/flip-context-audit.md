# Flip-context independence audit

## Question

Does a facet minor directly certify independence of a quadrilateral flip increment from surrounding triangulations?

## Claim boundary

The certificate is an identity in formal function values, not an assumption of triangle additivity. Finite enumeration covers every pair of regional flips across each cut at n=6..8.

Across a cut c, write T_ab=L_a union {c} union R_b. The change of the left flip increment under the right flip is

\[
[f(T_{11})-f(T_{01})]-[f(T_{10})-f(T_{00})]
=f(T_{00})+f(T_{11})-f(T_{10})-f(T_{01}).
\]

This is exactly the mixed facet minor. Thus vanishing minors make a flip increment invariant under each move in a separated surrounding region. Any two surrounding triangulations are connected by regional flips. Applying the identity successively across the quadrilateral sides removes all context dependence; a side that is a polygon boundary has no surrounding triangulation to vary.

The checker constructs 6, 70, and 536 ordered-region certificates for n=6,7,8, verifies that all four completions are genuine polygon triangulations, and compares formal coefficient vectors over the integers. A function equal to one on T_11 and zero elsewhere gives residual one, so separability is an operative assumption even in characteristic two.

## Disposition

The context-independence edge of the local-factorization converse has an explicit one-minor certificate. Together with the pentagon sign audit this supports the division-free converse proof. It does not identify physical coefficient data or a source embedding.
