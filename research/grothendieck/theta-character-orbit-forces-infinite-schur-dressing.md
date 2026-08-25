# Character transport forbids a finite invariant vacuum flag

## 1. General orbit theorem

Let \(\mu\) be a positive measure whose support contains an interval, and let

\[
  (U_xf)(u)=e^{ixu}f(u)
\]

on \(L^2(\mu)\). If \(f\ne0\) on a set of positive measure, then

\[
  \operatorname{span}\{U_xf:x\in\mathbb R\}
\]

is infinite dimensional.

Indeed, for distinct \(x_1,\ldots,x_N\), a relation

\[
  \sum_{j=1}^Nc_jU_{x_j}f=0
\]

implies

\[
  \sum_{j=1}^Nc_je^{ix_ju}=0
\]

on a positive-measure set where \(f\ne0\). The exponential polynomial is
analytic, hence vanishes identically, and all \(c_j\) are zero.

## 2. Application to the completed vacuum

The completed theta density is positive on intervals, and its diffusion
ground state is the constant vacuum in the weighted space. Therefore

\[
  \overline{\operatorname{span}}\{U_x\Omega:x\in\mathbb R\}
\]

cannot lie in any finite-dimensional diffusion spectral subspace.

Infinitesimally,

\[
  \left.\frac{d}{dx}U_x\Omega\right|_{x=0}
  =
  iQ\Omega.
\]

Since \(Q\Omega=u\) is not constant in the theta measure,

\[
  (I-P_\Omega)Q\Omega\ne0.
\]

Thus character transport couples the vacuum to excited modes at first order.

## 3. Consequence for determinant reduction

No finite source-derived invariant flag can make the mixed crossing
triangular for all \(x\). In particular, the equality

\[
  \det_{\mathrm{full}}T_x
  =
  u(x)\,\langle\Omega,W_x\Omega\rangle
\]

cannot be justified by saying that only finitely many excited channels
decouple and contribute a harmless determinant.

\[
\boxed{
\text{character covariance forces infinite Schur dressing}.}
\]

If the full determinant has the same divisor as \(X\), the excited
contribution must be controlled as an infinite coherent unit, not removed by
finite truncation.

## 4. Stronger closure interpretation

This theorem is the continuous-character analogue of forced infinite prime
transport closure. Both say:

\[
\text{a small observation block}
\xrightarrow{\text{authorized transport}}
\text{an infinite source module}.
\]

The physical vacuum coefficient remains a valid scalar readout, but its
faithfulness to the full transported module requires a separate theorem.

## 5. Revised target

Seek an infinite triangular factorization

\[
  T_x
  =
  L_x
  \begin{pmatrix}
    X(x) & 0\\
    0 & D_x^\circ
  \end{pmatrix}
  R_x,
\]

where:

1. \(L_x\) and \(R_x\) are source-derived invertible transition operators;
2. \(D_x^\circ\) is Fredholm and has a nowhere-zero determinant;
3. the factorization follows from modular/scale coherence rather than zero
   data; and
4. a hostile source fails the factorization before its divisor is inspected.

This is an operator-valued Wiener--Hopf or scattering factorization problem,
not a finite matrix reduction.

## 6. Falsifier

One zero of \(\det D_x^\circ\), or one failure of invertibility of the
transition factors, disproves divisor faithfulness. Equally, if the
factorization works for every analytic positive vacuum, it supplies no
theta-specific RH mechanism.

## 7. Scope

Infinite dimensionality of the character orbit and first-order
vacuum--excited coupling are exact. They exclude finite invariant-flag
explanations. No infinite factorization, determinant-unit theorem, or RH
result is established.
