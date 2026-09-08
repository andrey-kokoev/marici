# Five-point analytic residue and normalization interface

## Question

Which additional data turns the universal Laurent coefficient at a channel divisor into an analytic residue, and which normalization and pole choices remain external?

## Claim boundary

This packet derives a local meromorphic-form residue from the universal five-point Laurent identity. It does not identify that form with a canonically normalized scattering amplitude, choose a contour or boundary value, or import a positive-geometry canonical form.

## Local coefficient

Let

\[
m_5(a)=\sum_{(i,j)\in E(C_5)}\frac{1}{a_i a_j}
\]

in the localized coordinate ring. For the divisor `D_i={a_i=0}`, the formal coefficient is

\[
c_i=\operatorname{Coeff}_{a_i^{-1}}(m_5)
   =a_{i-1}^{-1}+a_{i+1}^{-1}.
\]

Equivalently, `c_i=(a_i m_5)|_{D_i}`. This statement uses the declared normal coordinate `a_i`; it is not yet a residue of a differential form.

## Meromorphic one-normal form

Choose a local defining function `u_i` for `D_i`, a tangential form `eta_i`, and a meromorphic form

\[
\Omega=N(a)\,m_5(a)\,du_i\wedge\eta_i,
\]

where `N` is regular along `D_i`. If `u_i=a_i`, then

\[
\operatorname{Res}_{D_i}(\Omega)
  =N|_{D_i}\,c_i\,\eta_i|_{D_i}.
\]

If `u_i=h_i a_i` with `h_i` a nonvanishing regular unit, then the same geometric form must transform its scalar coefficient by the inverse Jacobian. With that transformation, the Poincare residue is coordinate invariant. Holding the scalar function fixed while replacing `da_i` by `du_i` instead multiplies the residue by `h_i|_{D_i}`; this is a normalization change, not coordinate invariance.

For the ordered ambient form

\[
\Omega=N m_5\,da_0\wedge\cdots\wedge da_4,
\]

and tangential order `eta_i=da_0 wedge ... wedge omit(da_i) wedge ... wedge da_4`, the convention `Omega=(da_i/a_i) wedge Res + regular` gives

\[
\operatorname{Res}_{D_i}(\Omega)=(-1)^i N|_{D_i}c_i\eta_i.
\]

Changing ambient or normal orientation changes this sign.

## Separation of remaining inputs

- `N`: coupling, external-state, and amplitude normalization; not fixed by Laurent factorization.
- `u_i`: source-derived local channel coordinate; replacing it without transforming the form introduces a Jacobian.
- `eta_i`: tangential measure and orientation.
- `i0` or contour choice: boundary-value and integration prescription; it does not alter the algebraic coefficient identity.
- physical record map: absent.

## Disposition

The universal coefficient identity canonically determines the residue only after a meromorphic differential form and its normal/tangential orientation are declared. With `u_i=a_i` and unit normalization, the residue is the adjacent lower-point weighted sum, up to the explicit wedge-order sign. No current source fixes `N`, a pole prescription, or physical readout.
