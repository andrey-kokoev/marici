# Crystal boundary realization equals the Adams quadratic gate

Date: 2026-09-08

## Identification

The first Adams constructor is already source-defined on the faithful theta-label carrier.  Primewise,

\[
\mathbf C^{-1}\mathbf M s_p=\mathbf M b_p,
\]

with prime and theta labels retained and scalar theta synthesis postponed.  This supplies the linear comparison morphism needed to form a candidate crystal comparison fibre.

What remains missing is exactly the Hermitian realization required by the DAG boundary proposal.  Let `Q_p^lin` be the uniquely normalized linear map from the bivariate Stieltjes cell to the completed theta-history carrier.  A boundary Hermitian realization exists with the required source value only if

\[
\mathfrak G_p^{\mathrm{St}}(u,v)
=
\mathfrak G_p^\theta
\bigl(Q_p^{\mathrm{lin}}u,Q_p^{\mathrm{lin}}v\bigr)
\]

on the common rapid core after the declared radical quotients.

On the two-dimensional endpoint plane this is equivalent to four polarized matrix-unit tests

\[
(e_j,e_k),\qquad j,k\in\{1,2\}.
\]

The diagonal entries fix endpoint energies.  The off-diagonal entries fix real cross-correlation, reciprocal orientation, adjoint ordering, and the odd tail return.  Agreement only on `e2-e1` does not determine this form.

## Categorical consequence

The crystal construction does not remove the Adams quadratic gate.  It factors it:

\[
\text{label-valued linear constructor}
\longrightarrow
\text{comparison fibre}
\longrightarrow
\text{supported boundary crystal}
\longrightarrow
\text{Hermitian realization}.
\]

The first arrow is source-constructed.  Weighted prime completion is analytically available for the mixed channel.  The last arrow is defined precisely when the four matrix-unit identity and closure hold.  Therefore a purported crystal boundary map that writes down `D_bw` without these tests silently inserts the missing quadratic structure.

## Local source object

Before prime pushforward, the relevant object is the relative two-chart cell with basis

\[
(F_{\mathrm{in}},F_{\mathrm{out}},W_{\mathrm{const}}).
\]

Its still-undefined relative Green matrix `G_Cp` must satisfy:

1. oriented front balance;
2. the overlap relation `h_-+h_+=-1`;
3. rigged-transpose covariance;
4. reciprocal covariance;
5. annihilation of both declared radicals.

Contracting `G_Cp` with primitive and square face-incidence vectors produces the local mixed form.  Its four polarized entries are the concrete data needed by the crystal Hermitian realization.

## Disposition

DAG localization has reduced the search to an existing exact frontier rather than supplied a new theorem.  The next executable calculation is the one-prime `3×3` relative Green matrix and its induced `2×2` polarized endpoint Gram.  Seam support and Hermitian normalization cannot be certified before that matrix is source-derived.

## Inputs

- `research/nima/the-first-adams-constructor-is-closed-on-the-faithful-theta-label-carrier-not-after-scalar-augmentation.md`
- `research/nima/all-local-linear-adams-data-are-fixed-the-remaining-gate-is-quadratic-functoriality.md`
- `research/nima/the-adams-mixed-pairing-must-be-formed-before-prime-pushforward.md`
