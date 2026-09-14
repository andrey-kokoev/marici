# The Folner trace-density completion turns the divergent translation orbit into a canonical bulk Hilbert feature

## Motivation

The cutoff kernels

\[
K_M^k(x,y)
=1_{[-M,M]}(y)k(x-y)
\]

have Hilbert--Schmidt norm of order `sqrt(2M)` and possess no normalized strong limit in the ordinary Hilbert--Schmidt space.

The correct limit records norm **per unit translation volume**.

## Trace-density pairing

For two convolution kernels `k,l in L^2(R)`, define

\[
\langle
K_M^k,
K_M^l
\rangle_{dens}
=
\frac1{2M}
\langle
K_M^k,
K_M^l
\rangle_{HS}.
\]

A direct calculation gives

\[
\begin{aligned}
\langle
K_M^k,
K_M^l
\rangle_{HS}
&=
\int_{-M}^{M}
\int_\mathbb R
\overline{k(x-y)}l(x-y)dxdy\\
&=
2M
\langle k,l\rangle_{L^2(\mathbb R)}.
\end{aligned}
\]

Therefore

\[
\boxed{
\langle
K_M^k,
K_M^l
\rangle_{dens}
=
\langle k,l\rangle_2
}
\]

for every `M`, not merely asymptotically.

## Density-null quotient

Let `mathscr K` be a space of regulated kernel families `T=(T_M)_(M>=1)` for which all density pairings under consideration have limits. Define

\[
\|T\|_{dens}^2
=
\lim_{M\to\infty}
\frac1{2M}
\|T_M\|_{HS}^2.
\]

Let

\[
\mathscr N_{dens}
=
\{T:
\|T\|_{dens}=0\}.
\]

After polarization, quotient and complete:

\[
\boxed{
\mathcal H_{bulk}
=
\overline{
\mathscr K/\mathscr N_{dens}
}^{\|\cdot\|_{dens}}.
}
\]

This is a Hilbert space of trace-density germs. Two families differing by a boundary contribution of `o(M)` Hilbert--Schmidt mass define the same bulk feature.

## Canonical bulk embedding

Define

\[
\Xi:
L^2(\mathbb R)
\longrightarrow
\mathcal H_{bulk},
\qquad
k
\longmapsto
[(K_M^k)_M].
\]

The exact density identity gives

\[
\boxed{
\langle\Xi(k),\Xi(l)\rangle_{bulk}
=
\langle k,l\rangle_2.
}
\]

Thus `Xi` is an isometry. On the closed span of regulated translation-invariant kernels it is unitary:

\[
\boxed{
\mathcal H_{bulk}^{tr}
\cong
L^2(\mathbb R_{difference}).
}
\]

The divergent orbit has become one canonical **bulk Hilbert feature**, but not one vector line. Every observer kernel supplies its own vector `Xi(k)` in the common `L^2` bulk.

## Translation-module action

Translations in the center variable preserve the density seminorm. Convolution and Fourier multipliers act on the difference kernel. Consequently `H_bulk^tr` carries the regular module action of the scaling-group von Neumann algebra.

The density inner product is the GNS inner product of the Plancherel trace:

\[
\boxed{
\|\Xi(k)\|_{bulk}^2
=
\tau(A_k^*A_k).
}
\]

For an observer `g`, this is

\[
\tau(U(g)^*U(g))
=
\|g\|_2^2
=h(1).
\]

This recovers the coefficient of the volume counterterm without collapsing all observers to one direction.

## Boundary families vanish in density but retain finite part

Suppose `D_M` is supported in a center-variable boundary layer of uniformly bounded width and has uniformly bounded local Hilbert--Schmidt density. Then

\[
\|D_M\|_{HS}^2
=O(1),
\]

so

\[
\frac1{2M}
\|D_M\|_{HS}^2
\to0.
\]

Hence `[D]=0` in `H_bulk`.

Such a family can nevertheless have a nonzero unnormalized finite trace. Therefore the bulk density quotient and boundary finite-part space must both be retained:

\[
\boxed{
\text{regulated feature}
\longmapsto
(\text{bulk density class},
\text{relative boundary class}).
}
\]

The first coordinate controls the positive volume divergence; the second carries the Weil finite part.

## Two-scale version

For inner and outer logarithmic windows `L=log Lambda` and `M=log R`, use the outer density normalization

\[
\frac1{2M}.
\]

If `M/L -> rho in (1,infinity)`, then the inner window occupies density fraction

\[
\frac{L}{M}
\to
\rho^{-1}.
\]

Thus the correlated limit parameter `rho` is visible as an angle/weight in the bulk Gram matrix. It cannot be omitted before proving independence of `rho` in the relative boundary class.

## Semilocal generalization

Let the module map provide the noncompact logarithmic coordinate

\[
\ell_S(x)=
\log|x|_S.
\]

Choose Folner windows

\[
F_M
=
\{x:
|\ell_S(x)|
\le M\}
\]

modulo the compact/norm-one directions and normalize by their scaling Haar volume `vol(F_M)`.

For translation-covariant semilocal kernels, define

\[
\langle T,U\rangle_{dens,S}
=
\lim_{M\to\infty}
\frac1{\operatorname{vol}(F_M)}
\langle
T_M,U_M
\rangle_{HS}.
\]

When the limit exists, it agrees with the semifinite Plancherel trace pairing

\[
\boxed{
\langle T,U\rangle_{dens,S}
=
\tau_S(T^*U).
}
\]

This identifies the correct home for the translation-invariant closure of `ran E_S`: a Hilbert module/GNS space over `VN(C_S)`, represented concretely by trace-density germs.

## Corrected feature decomposition

The former vector ansatz should be replaced by a two-coordinate map

\[
\boxed{
Q_\Lambda P_RU_S(g)
\longmapsto
\left(
\Xi_S(g),
\mathfrak b_{\Lambda,R,S}(g)
\right),
}
\]

where

\[
\|\Xi_S(g)\|_{bulk}^2=h(1)
\]

and `mathfrak b` is the relative boundary germ after removal of the bulk module in the density sense.

No assertion is yet made that the boundary germ converges positively. The construction does type the bulk subtraction without selecting a nonexistent fixed divergent vector.

## Exact next gate

Define a boundary seminorm or relative correspondence satisfying both:

1. density-null bulk boundary layers remain visible when their unnormalized finite trace is taken;
2. the two-by-two regulated Halmos Gram matrix descends to a positive matrix-valued relative functional.

This requires a two-scale relative space rather than the density quotient alone.

## Disposition

The translation-volume divergence has a canonical positive realization:

\[
\boxed{
\mathcal H_{bulk}^{tr}
\cong
L^2(\mathbb R_{difference})
}
\]

through the Folner trace-density completion. It is the GNS bulk of the Plancherel trace. The remaining Weil information lies in a separate boundary finite-part coordinate, which must now be constructed compatibly with the positive Gram block.
