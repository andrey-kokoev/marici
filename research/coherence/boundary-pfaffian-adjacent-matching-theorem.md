# Boundary Pfaffians select the adjacent matching at every even rank

## Theorem

Let

\[
0<a_{(0)}<a_{(1)}<\cdots<a_{(2m-1)}
\]

be distinct half-line shift lengths. Form the oriented window two-cochain

\[
\mathcal F_{ij}=K_{j,i}-K_{i,j},
\qquad
K_{j,i}=R_{a_j}S_{a_i}-S_{a_i}R_{a_j},
\]

and its fully symmetrized operator Pfaffian cup. Then its endpoint readout is

\[
\boxed{
\rho_0(\operatorname{Pf}_{2m}\mathcal F)
=
\operatorname{or}(a_0,\ldots,a_{2m-1})
\operatorname{ev}_{L_{2m}},
}
\]

where

\[
L_{2m}
=
\sum_{r=0}^{m-1}
\left(a_{(2r+1)}-a_{(2r)}\right).
\]

The normalization of the symmetrized cup is the one induced by operator expansion; no factorial remains in the endpoint coefficient.

## Step 1: the endpoint pair kernel

Directly from the half-line support formula,

\[
(\mathcal F_{ij}f)(0)
=
\operatorname{sgn}(a_j-a_i)
 f(|a_j-a_i|).
\]

Test this functional on the separating exponential family

\[
f_t(x)=e^{-tx},\qquad t>0.
\]

The pair kernel becomes the antisymmetric scalar matrix

\[
M_{ij}(t)
=
\operatorname{sgn}(a_j-a_i)e^{-t|a_j-a_i|}.
\]

## Step 2: ordered chamber factorization

In the increasing chamber and for \(i<j\), set

\[
x_k=e^{-t(a_{(k+1)}-a_{(k)})}.
\]

Then

\[
M_{ij}=x_i x_{i+1}\cdots x_{j-1}.
\]

This is a multiplicative chain matrix. Its Pfaffian satisfies

\[
\operatorname{Pf}M_{2m}
=x_0x_2\cdots x_{2m-2}.
\]

One proof uses the Pfaffian recurrence along the first row. Every non-adjacent pairing term cancels with the term obtained by switching the first crossing/nesting, because chain weights obey

\[
M_{ik}M_{j\ell}=M_{i\ell}M_{jk}
\qquad(i<j<k<\ell).
\]

Only the adjacent noncrossing matching survives. Therefore

\[
\operatorname{Pf}M_{2m}(t)
=
\exp\left(
-t\sum_{r=0}^{m-1}(a_{(2r+1)}-a_{(2r)})
\right).
\]

## Step 3: recover the evaluation functional

At finite rank, endpoint expansion of the operator Pfaffian is a finite signed combination of point evaluations. Equality on every \(f_t\) says that its finite atomic Laplace transform is

\[
e^{-tL_{2m}}.
\]

Uniqueness of finite atomic Laplace transforms forces the functional itself to be

\[
\operatorname{ev}_{L_{2m}}.
\]

Returning from increasing order to the supplied frame multiplies the Pfaffian by its permutation sign. This proves the theorem.

## Minimum matching

For ordered points on a line, any crossing or nested perfect matching can be uncrossed without increasing total length. Strict ordering shows that the unique minimum cost is the adjacent matching, with cost \(L_{2m}\).

Hence the theorem can be stated equivalently as

\[
\boxed{
\text{endpoint boundary Pfaffian}
=
\text{oriented evaluation at minimum perfect-matching cost}.
}
\]

## Why this is deeper than an optimization coincidence

The minimizer is not chosen by comparing scalar costs. It is selected algebraically:

- half-line support turns pair relations into the chain kernel;
- antisymmetry forms its Pfaffian;
- the chain identity cancels every non-adjacent matching;
- the surviving exponent records the adjacent matching cost.

Thus geometric order and fermionic alternation implement the minimization as an identity.

## Arithmetic specialization

For \(a_i=\log p_i\),

\[
L_{2m}
=
\log
\prod_{r=0}^{m-1}
\frac{p_{(2r+1)}}{p_{(2r)}}.
\]

The endpoint invariant is therefore the alternating product of consecutive ordered primitive scales, together with the orientation line of the original frame.

## Scope

This theorem concerns finite distinct half-line shifts. Coincident lengths require a degenerate/Pfaffian limit. Infinite-rank completion requires independent summability and determinant-line control. Neither is implied by the finite identity.
