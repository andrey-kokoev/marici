# Sector phase charge is conserved only after retaining the infinity caps

## Finite rectangle

Let `E_+` be the endpoint-reduced Euler section in the right half-plane. Fix

\[
\frac12<\sigma_0<\sigma_1
\]

and a height `T` such that `E_+` has no zero on the boundary of the rectangle

\[
R=[\sigma_0,\sigma_1]\times[-T,T].
\]

Define the upward vertical phase variation

\[
W_\sigma(T)
=
\int_{-T}^{T}
\partial_t\arg E_+(\sigma+it)\,dt.
\]

Let `C_T` be the combined phase variation along the upper and lower
horizontal caps with counterclockwise boundary orientation. The argument
principle gives the exact conservation law

\[
2\pi N_R
=
W_{\sigma_1}(T)-W_{\sigma_0}(T)+C_T,
\]

where `N_R` is the number of zeros in `R`, counted with multiplicity.

Equivalently,

\[
W_{\sigma_0}(T)
=
W_{\sigma_1}(T)+C_T-2\pi N_R.
\]

## Conjugation doubles the cap

Because `E_+(conj(s))=conj(E_+(s))`, the two horizontal cap integrals are
equal after their boundary orientations are included. Writing

\[
A_T(\sigma)
=
\operatorname{Im}\frac{E_+'}{E_+}(\sigma+iT),
\]

one obtains

\[
C_T
=
-2\int_{\sigma_0}^{\sigma_1}A_T(\sigma)\,d\sigma.
\]

Thus symmetric truncation does not cancel the infinity contribution. It
doubles one oriented cap.

## Euler anchor and the two ways charge can change

Choose `sigma_1>1`. The Euler product gives a canonical zero-free phase in
that chamber. Moving the vertical observer from `sigma_1` toward the critical
seam can change its winding only through two typed channels:

1. a divisor vortex crosses the finite slab, contributing `2 pi N_R`;
2. phase flux enters through the horizontal infinity caps, contributing
   `C_T`.

There is no third finite source. Exact cutoff anomaly connections have zero
residue and only change the choice of phase frame.

This is the differential form of the conservation law:

\[
d\,d\arg E_+
=
2\pi\sum_\rho m_\rho\,\delta_\rho.
\]

Away from the divisor the phase connection is flat; zeros are its quantized
vortices.

## Completion obstruction

Passing to `T -> infinity` requires an explicit infinity port. Polynomial
vertical growth is enough for bounded type, but it does not by itself make
`C_T` vanish along every truncation. A limit that retains only the two
vertical phase records can therefore manufacture or erase apparent charge.

The RH-bearing transport statement must control the pair

\[
(\kappa_{\mathrm{rel}},C_\infty)
\]

together. Proving that the Euler-anchored relative phase class reaches the
seam trivially requires either:

- a source-derived sequence of heights on which the renormalized cap flux
  vanishes;
- an exact theta--Poisson formula identifying the limiting cap as a declared
  boundary current;
- or a conservation law showing that the cap cannot inject anti-diagonal
  charge.

Ignoring `C_infinity` is not a harmless limiting convention.

## Relation to the multi-tower picture

The two sector phase towers are not closed by their reciprocal comparison
alone. Their comparison tower has its own boundary tower at spectral
infinity. The minimal complete phase object therefore has three components:

1. right-sector phase transport;
2. left-sector phase transport;
3. the common infinity-cap current controlling their relative descent.

This is the phase-theoretic realization of the previously predicted
projective infinity germ.

## Scope

This packet proves the finite-height conservation law and identifies the
mandatory infinity channel. It does not evaluate its completed theta limit,
exclude finite divisor vortices, or prove RH.
