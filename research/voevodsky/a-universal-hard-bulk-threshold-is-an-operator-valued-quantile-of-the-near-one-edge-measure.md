# A universal hard bulk threshold is an operator-valued quantile of the near-one edge measure

## Edge correction operator

Let the polarized rescaled near-one measures converge to an operator-valued positive measure

\[
\nu(E)
\]

on the observer source, meaning

\[
\nu_{g,h}(E)
=
\langle g,
\nu(E)h\rangle.
\]

The difference between soft dyadic and hard-threshold residuals at parameter `a>0` is the form

\[
\boxed{
\Delta_a
=
\int_0^\infty
D_a(x)d\nu(x),
}
\]

where

\[
D_a(x)
=1-e^{-x}
-
1_{\{x>a\}}.
\]

A hard threshold reproduces the soft positive boundary exactly when

\[
\boxed{
\Delta_a=0
}
\]

as an operator/form identity on the observer core.

## Quantile equation

Rearranging gives

\[
\boxed{
\nu((a,\infty))
=
\int_0^\infty
(1-e^{-x})d\nu(x).
}
\]

The right side is the total soft-residual edge mass. The left side is the hard-residual tail mass.

Thus a universal hard threshold is an **operator-valued quantile** of the edge measure.

## Scalar factorization theorem

Assume the edge law factorizes as

\[
\boxed{
\nu_{g,h}(E)
=G(g,h)\rho(E)
}
\]

for one positive observer Gram form `G` and one positive scalar measure `rho`.

Then

\[
\Delta_a
=Gd_a
\]

with

\[
d_a
=
\int
(1-e^{-x})d\rho(x)
-
\rho((a,\infty)).
\]

Therefore the universal operator equation reduces to the scalar quantile condition

\[
\boxed{
\rho((a,\infty))
=
\int
(1-e^{-x})d\rho(x).
}
\]

## Existence

Suppose `rho` is finite and has no atom obstructing the target tail value. Set

\[
M_{soft}
=
\int
(1-e^{-x})d\rho(x).
\]

Since

\[
0
\le
1-e^{-x}
<1
\]

for finite `x`,

\[
0
\le
M_{soft}
\le
\rho((0,\infty)).
\]

The tail function

\[
T(a)
=
\rho((a,\infty))
\]

is decreasing and right-continuous, with

\[
T(0)
=
\rho((0,\infty)),
\qquad
T(a)
\to0.
\]

If `T` is continuous at the target level, an `a` exists with

\[
T(a)=M_{soft}.
\]

If `rho` has a positive density almost everywhere on its support, the solution is unique.

## Atoms and randomized thresholds

If `rho` has an atom at the required quantile, no deterministic strict/non-strict threshold may attain the exact target. One can interpolate the threshold atom:

\[
1_{\{x>a\}}
+
theta1_{\{x=a\}},

\qquad
0\le\theta\le1.
\]

This is a positive contraction rather than an orthogonal projection unless `theta` is zero or one.

Hence an atomic edge law may force retention of a soft/partially occupied bulk feature.

## Failure without factorization

For each diagonal observer `g`, normalize its edge measure by its total mass:

\[
\bar\nu_g
=
\frac{
\nu_{g,g}
}{
\nu_{g,g}([0,\infty))
}.
\]

Its preferred scalar threshold solves

\[
\bar\nu_g((a_g,\infty))
=
\int
(1-e^{-x})d\bar\nu_g(x).
\]

If two observers have unique thresholds with

\[
\boxed{
a_g
\ne
a_h,
}
\]

then no universal hard spectral projection can reproduce the soft residual for both.

This is a finite two-observer falsification test.

## Polarized obstruction

Agreement of all diagonal thresholds is necessary but not sufficient. The operator identity also requires the polarized measures:

\[
\boxed{
\nu_{g,h}((a,\infty))
=
\int
(1-e^{-x})d\nu_{g,h}(x)
}
\]

for every pair `g,h`.

Diagonal equality implies polarized equality only if it holds as a quadratic-form identity for every linear combination `g+z h`, not merely for a selected test list.

## Angular-character factorization

A sufficient semilocal hypothesis is

\[
\boxed{
\nu_{g,h}^{\chi,\psi}(dx)
=G_{\chi,\psi}(g,h)\rho(dx)
}
\]

with one common radial edge profile `rho` for every angular block. Rapid angular decay then assembles the operator-valued identity.

If the Tate phase produces character-dependent edge profiles `rho_chi`, a universal threshold requires all of them to share the same quantile:

\[
\rho_\chi((a,\infty))
=
\int
(1-e^{-x})d\rho_\chi(x)
\]

for one `a`. Polynomial summability alone does not imply this.

## Relation to universal prolate edge laws

Classical Landau--Widom asymptotics often produce a universal transition profile after centering by the time--band counting function. If the observer-weighted semilocal edge theorem has the stronger factorized form

\[
\nu_{g,h}
=G(g,h)\rho_{univ},
\]

then the hard threshold is derived canonically from `rho_univ` by the quantile equation.

A bare eigenvalue-counting asymptotic is insufficient: it determines `rho_univ` only for the unweighted trace and does not prove observer factorization.

## Relation to absolute-Gram convergence

If the soft residual satisfies

\[
K_{\Lambda,m}^{soft}
\to
q_{|A_S|},
\]

and the operator quantile equation holds, then the calibrated hard residual has the same limit:

\[
\boxed{
K_{\Lambda,m,a}^{hard}
\to
q_{|A_S|}.
}
\]

If the equation fails, the hard limit differs by `Delta_a` and therefore realizes a different positive boundary.

## Computable finite-packet test

On a finite packet `E_0`, materialize the matrix-valued edge distribution `nu^(E_0)`. For candidate `a`, compute

\[
\boxed{
M_a^{E_0}
=
\nu^{E_0}((a,\infty))
-
\int
(1-e^{-x})d\nu^{E_0}(x).
}
\]

Then:

- `M_a=0` certifies hard/soft equivalence on the packet;
- `||M_a||` bounds the Gram discrepancy;
- incompatible zero sets for nested packets disprove a universal threshold;
- convergence of one common zero across a dense packet tower is evidence for a global hard bulk projection.

## Categorical consequence

The soft dyadic feature is functorial in `B` and strictly coherent in depth. The hard feature becomes functorial only after adjoining the quantile `a` as data derived from the limiting operator-valued edge law.

Therefore a hard projection should be represented as a **chosen calibrated retraction** of the soft filtered tower, not as an intrinsic node preceding spectral analysis.

## Disposition

The exact hard-bulk gate is

\[
\boxed{
\nu((a,\infty))
=
\int
(1-e^{-x})d\nu(x).
}
\]

Under a universal factorized edge law, this is one scalar quantile equation and determines the hard threshold. Without factorization, two observer packets with different preferred quantiles already rule out any universal orthogonal bulk projection. The canonical positive construction should therefore retain the soft dyadic tower unless this operator-valued quantile identity is proved.
