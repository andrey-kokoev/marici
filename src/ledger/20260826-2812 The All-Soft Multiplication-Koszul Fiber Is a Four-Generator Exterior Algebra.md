# 2812 — The All-Soft Multiplication-Koszul Fiber Is a Four-Generator Exterior Algebra

## Frozen specialization

At \(x=y=z=0\), the six multiplication factors specialize to

\[
(K,q_{g1},q_{g2},q_{g3},q_{g23},q_{g31})
=(0,b,a,a+b,b,a).
\]

The following four labelled directions have zero multiplication differential:

\[
e_K,
\quad r_3=e_{g3}-e_{g2}-e_{g1},
\quad r_{23}=e_{g23}-e_{g1},
\quad r_{31}=e_{g31}-e_{g2}.
\]

## Unimodular normal form

The source-labelled change of generators from the five marked factors to

\[
(e_{g2},e_{g1},r_3,r_{23},r_{31})
\]

has determinant \(-1\). It transforms the marked sequence to

\[
(a,b,0,0,0).
\]

Including the zero Cayley–Menger factor, the all-soft multiplication-Koszul homology is therefore

\[
H(K_{\rm mult}|_0)
\simeq
\mathbb F\otimes
\Lambda(e_K,r_3,r_{23},r_{31}),
\]

with graded dimensions

\[
(1,4,6,4,1)
\]

and total dimension \(16\).

## Normal-order typing

The three marked-relation generators are ordinary first-normal directions associated with the external maximal ideal \((x,y,z)\).

The Cayley–Menger generator is different. The external degrees of the coefficients of \(a^4,a^2b^2,b^4,a^2,b^2,1\) are

\[
(2,2,2,4,4,6).
\]

Thus \(K_{\rm CM}\) begins at second external normal order. The fourth exterior generator is existing Cayley–Menger coefficient data in the second Rees grade, not another first-normal soft incidence and not a new Carrier divisor.

## Narrow conclusion

The all-soft multiplication-Koszul fiber is completely classified. Its four primitive directions split as

\[
3\text{ first-normal marked relations}
\quad+\quad
1\text{ second-normal Cayley–Menger relation}.
\]

This does not yet identify the cohomology of the full de Rham totalization, its Gysin image, or a physical source-cycle pairing. The next falsifier is to compute the induced de Rham differential on this labelled exterior grade and compare its surviving classes with the existing soft and Cayley–Menger Gysin maps.

## Durable artifacts

- `research/benincasa/check_rank26_all_soft_costalk.py`
- `research/benincasa/rank26-all-soft-costalk.json`
