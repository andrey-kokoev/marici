# The relative difference-row norm is the positive `H^(1/2)` phase energy of the Tate symbol

## Recentered projection pair

Let

\[
Q_\gamma
=M_\gamma
\Pi
M_\gamma^*,
\qquad
Q_0
=\Pi,
\]

and

\[
\Delta Q
=Q_\gamma-Q_0.
\]

Assume `gamma` is a smooth unimodular phase on the real line after endpoint/index terms are separated.

The Hadamard difference row is

\[
D
=
\frac12
(F_{Q_\gamma}-F_{Q_0}),
\]

so

\[
\boxed{
D^*D
=
\frac12
(\Delta Q)^2.
}
\]

## Divided-difference kernel

The regular kernel of `Delta Q` is

\[
\boxed{
\Delta q(s,t)
=
\frac1{2\pi i}
\frac{
\gamma(s)
\overline{\gamma(t)}-1
}{s-t}.
}
\]

Since `|gamma(t)|=1`,

\[
|\gamma(s)
\overline{\gamma(t)}-1|
=
|\gamma(s)-\gamma(t)|.
\]

## Observer-localized Hilbert--Schmidt norm

For an observer Mellin multiplier `M_m`,

\[
(\Delta Q M_m)(s,t)
=
\Delta q(s,t)
m(t).
\]

Therefore

\[
\begin{aligned}
\|\Delta Q M_m\|_2^2
&=
\frac1{4\pi^2}
\iint_{\mathbb R^2}
\frac{
|\gamma(s)-\gamma(t)|^2
}{|s-t|^2}
|m(t)|^2dsdt.
\end{aligned}
\]

Define the nonnegative phase-energy density

\[
\boxed{
\kappa_\gamma(t)
=
\frac1{4\pi^2}
\int_\mathbb R
\frac{
|\gamma(s)-\gamma(t)|^2
}{|s-t|^2}ds.
}
\]

Then Tonelli's theorem gives the exact identity

\[
\boxed{
\|\Delta Q M_m\|_2^2
=
\int_\mathbb R
\kappa_\gamma(t)
|m(t)|^2dt.
}
\]

## Difference-row Gram

Because the difference row has two equal opposite components,

\[
\boxed{
\|D M_m\|_2^2
=
\frac12
\int
\kappa_\gamma(t)
|m(t)|^2dt.
}
\]

For polarized observers,

\[
\boxed{
\langle
D M_{m_g},
D M_{m_h}
\rangle_{HS}
=
\frac12
\int
\kappa_\gamma(t)

overline{m_h(t)}
m_g(t)dt.
}
\]

Thus the positive Gram of the relative difference row is a multiplication form.

## Cutoff independence

The common phase `e^(2iLs)` cancels after recentering. Hence `kappa_gamma` contains no cutoff parameter `L`.

Therefore the positive difference-row graph norm is exactly cutoff independent:

\[
\boxed{
q_D(g)
=
\frac12
\int
\kappa_\gamma
|m_g|^2.
}
\]

This is the intrinsic positive energy of Tate/reference deformation.

## Relation to fractional Sobolev energy

The global homogeneous `H^(1/2)` seminorm of `gamma` is

\[
[\gamma]_{\dot H^{1/2}}^2
=
\iint
\frac{
|\gamma(s)-\gamma(t)|^2
}{|s-t|^2}dsdt.
\]

The function `kappa_gamma(t)` is its local energy density in the second variable. Thus

\[
\boxed{
q_D(g)
=
\text{observer-weighted local }H^{1/2}
\text{ phase energy}.
}
\]

The bare global seminorm may be infinite because of center-volume or conductor growth; observer weighting makes the relevant integral finite.

## Natural positive graph domain

Define

\[
\boxed{
\mathcal D_D
=
\left\{
m:
\int
(1+\kappa_\gamma(t))
|m(t)|^2dt
<\infty
\right\}.
}
\]

With norm

\[
\boxed{
\|m\|_{\mathcal D_D}^2
=
\int
(1+\kappa_\gamma)
|m|^2,
}
\]

this is a Hilbert space, being a weighted `L2` space. The map

\[
m
\longmapsto
D M_m
\]

is bounded from `D_D` into the Hilbert--Schmidt ideal.

This gives a canonical positive completion of the relative difference row without using the Weil form as its norm.

## Angular assembly

For angular character `chi`, define

\[
\kappa_\chi(t)
=
\frac1{4\pi^2}
\int
\frac{
|\gamma_\chi(s)-\gamma_\chi(t)|^2
}{|s-t|^2}ds.
\]

The semilocal relative-energy domain is

\[
\boxed{
\mathcal D_{D,S}
=
\left\{
(m_\chi):
\sum_\chi
\int
(1+\kappa_\chi)
|m_\chi|^2
<\infty
\right\}.
}
\]

Conductor projections act diagonally and commute with this positive multiplication form.

## Linear-phase calibration

Take

\[
\gamma_b(s)
=e^{ibs}.
\]

Then

\[
\kappa_{\gamma_b}(t)
=
\frac1{4\pi^2}
\int
\frac{|e^{ib(s-t)}-1|^2}{|s-t|^2}ds.
\]

Using the standard difference integral,

\[
\boxed{
\kappa_{\gamma_b}(t)
=
\frac{|b|}{2\pi},
}
\]

independent of `t`.

Hence

\[
\boxed{
q_D(m)
=
\frac{|b|}{4\pi}
\|m\|_{L^2(ds)}^2.
}
\]

The positive relative norm detects the absolute spectral-flow magnitude, while the signed trace detects the oriented coefficient `b`.

This is the finite-dimensional polarity principle in continuous Hardy form.

## Comparison with the Tate connection

The signed Tate multiplier is

\[
w_\gamma(t)
=
\frac1i
\partial_t
\log\gamma(t).
\]

The difference-row norm uses `kappa_gamma>=0`, not `|w_gamma|` pointwise. For a linear phase they agree up to normalization:

\[
\kappa_{\gamma_b}
=
\frac{|w_{\gamma_b}|}{2\pi}.
\]

For a nonlinear phase, no general identity

\[
\kappa_\gamma
=
c|w_\gamma|
\]

holds. The former is nonlocal in the phase; the latter is a local derivative.

## Boundedness gate for the cross form

A direct bounded relative realization on `D_D` would follow from an inequality

\[
\boxed{
|w_\gamma(t)|
\le
C
(1+\kappa_\gamma(t))
}
\]

almost everywhere, or a corresponding integrated form bound.

Then

\[
\left|
\int
\overline{m_h}
m_gw_\gamma
\right|
\le
C
\|m_h\|_{\mathcal D_D}
\|m_g\|_{\mathcal D_D}.
\]

This would extend the Tate boundary continuously from the Schwartz core to the canonical positive difference-energy completion.

The inequality is exact for linear phases up to constants but remains to be established for local Tate gamma factors.

## Endpoint/index energy

A finite-rank index row contributes an additional positive finite-dimensional norm. Define

\[
\mathcal D_D^{completed}
=
\mathcal D_D
\oplus
\mathcal H_{index}
\]

with the endpoint graph norm. This keeps the regular phase energy and winding multiplicity separately typed.

## Relation to raw common volume

The graph norm `D_D` controls only the relative difference row. It does not make the common row Hilbert--Schmidt.

Thus it supplies a finite positive boundary-energy space for deformation, while the full relative current still uses the common module in the cross pairing.

## Disposition

The observer-localized Tate/reference difference has the exact positive Gram

\[
\boxed{
q_D(g,h)
=
\frac12
\sum_\chi
\int
\kappa_{\gamma_\chi}(t)
\overline{m_{h,\chi}(t)}
m_{g,\chi}(t)dt.
}
\]

This canonical cutoff-independent weighted `L2` form is the positive graph norm of the relative deformation row. The next analytic gate for completion beyond the Schwartz core is domination of the local Tate derivative by the nonlocal phase-energy density.
