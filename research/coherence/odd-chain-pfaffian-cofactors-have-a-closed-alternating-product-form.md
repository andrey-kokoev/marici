# Odd-chain Pfaffian cofactors have a closed alternating-product form

## Setup

Let an odd chain have \(2m+1\) vertices and gaps

\[
x_0,\ldots,x_{2m-1}.
\]

Its canonical signed cofactor vector is

\[
v_i=(-1)^i\operatorname{Pf}(M_{\widehat i}).
\]

## Even coordinates

For \(i=2r\), deleting the even pivot separates the remaining vertices into two even chains. Therefore

\[
v_{2r}
=
\left(\prod_{j=0}^{r-1}x_{2j}\right)
\left(\prod_{j=r}^{m-1}x_{2j+1}\right).
\]

These are exactly the residual-pivot products whose prime valuations appeared in the top-divisor minimum formula.

## Odd coordinates

For \(i=2r+1\), one Pfaffian pair crosses the deleted vertex and contributes the two-gap path weight \(x_{2r}x_{2r+1}\). Including the cofactor sign,

\[
v_{2r+1}
=-
\left(\prod_{j=0}^{r-1}x_{2j}\right)
 x_{2r}x_{2r+1}
\left(\prod_{j=r+1}^{m-1}x_{2j+1}\right).
\]

Thus every coordinate is one explicit alternating monomial; no recursive Pfaffian evaluation remains.

## Kernel identity

Substituting these monomials into the chain matrix gives

\[
Mv=0.
\]

The cancellation is polynomial, so the closed vector is valid over every commutative ring. Over an integral base, dividing its coordinates by their gcd \(D_m\) gives the primitive residual generator.

## Boundary charges

The endpoint coordinates are

\[
v_0=x_1x_3\cdots x_{2m-1}=q_{\rm in},
\]

\[
v_{2m}=x_0x_2\cdots x_{2m-2}=q_{\rm out}.
\]

Hence the two alternating residual charges are literally the two endpoint Pfaffian cofactors. The full null vector interpolates between them through the crossing monomials above.

## Formalization target

The arbitrary-size Agda proof can now avoid a general-purpose Pfaffian library in its residual branch:

1. define the displayed monomial vector recursively;
2. prove its row cancellations;
3. identify its endpoints with incoming/outgoing folds;
4. separately prove that these monomials equal Pfaffian cofactors.

Steps one through three are ring-generic. Primitive normalization requires gcd structure; hyperbolic contraction requires selected-gap units.

## Verification

```text
python research/coherence/check_odd_chain_cofactor_closed_form.py
```

The checker compares every coordinate with recursive Pfaffian minors and verifies the kernel identity for 180 exact-rational chains through thirteen vertices.

Artifacts:

- `check_odd_chain_cofactor_closed_form.py`
- `odd-chain-cofactor-closed-form.v1.json`
