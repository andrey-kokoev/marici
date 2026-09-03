# Theta decay solves the wrong coefficient space without the Mellin square

## Two coefficient objects

For every fixed lower bound `u0 > 0`, Gaussian theta coefficients

\[
c_n(u)=2e^{-\pi n^2u},\qquad u\geq u_0,
\]

satisfy every polynomially weighted summability condition uniformly in `u`. Hence they give elements of Voevodsky's `B_epsilon` for arbitrary finite `epsilon`.

This does not embed the unsmoothed zeta Dirichlet series into that space. With height `H(n)=n`, direct evaluation gives the smoothed series

\[
\sum_{n\geq1}2e^{-\pi n^2u}n^{-z},
\]

whose Dirichlet coefficients are not the coefficients `1` of zeta. Uniqueness of Dirichlet coefficients prevents identifying these functions on a common right half-plane.

## Required Mellin square

The classical route applies a Mellin integral in the geometric variable `u` before identifying the result with the completed zeta function. The needed comparison is therefore a commuting square between:

1. the theta-kernel space with Gaussian decay;
2. integration in `u`, including convergence and regularization;
3. the completed analytic function with its gamma and polar terms;
4. the cutoff/affine filler completion.

A scalar map into `B_epsilon` omits the integration operator and cannot supply this square.

The reciprocal theta identity controls the small-`u` region only after splitting the integral, transporting it to the large-`u` region, and retaining the explicit singular terms. Those terms determine the completed normalization and cannot be discarded as boundary-null residue.

## Exact acceptance test

Materialize an operator-valued source map

\[
\iota_\theta:f\longmapsto(c_n(u))_{n\geq1}
\]

into a weighted function-valued sequence space, and a continuous Mellin operator `M`. Then verify that finite cutoff and limit commute with `M` on the declared strip and that the resulting function equals the externally normalized classical completed zeta formula, including gamma and polar terms.

## Disposition

Gaussian decay can establish completion of the theta kernel but not identification with zeta by itself. The first missing arrow is the continuous Mellin comparison square. Until it is supplied, Voevodsky's conditional filler theorem applies to a smoothed coefficient object and has no RH implication.
