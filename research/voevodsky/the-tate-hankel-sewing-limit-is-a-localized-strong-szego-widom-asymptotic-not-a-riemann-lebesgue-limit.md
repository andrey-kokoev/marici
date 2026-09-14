# The Tate--Hankel sewing limit is a localized strong-Szego/Widom asymptotic, not a Riemann--Lebesgue limit

## Tempting but invalid shortcut

The recentered Tate symbol is

\[
\sigma_{L,\chi}(s)
=
e^{-2iLs}\gamma_\chi(s).
\]

Because of the oscillatory exponential, one might expect every observer-localized sewing trace to vanish by the Riemann--Lebesgue lemma.

That conclusion is valid only when the remaining kernel is integrable in the difference variable. Hardy projection products have diagonal singularities, so the hypothesis fails at precisely the order that controls the cutoff asymptotic.

## Hardy kernel singularity

The Hardy projection has distribution kernel

\[
K_\Pi(s,t)
=
\frac12\delta(s-t)
+
\frac{c}{s-t-i0}
\]

with convention-dependent `c`. A product of two off-diagonal Hardy kernels produces a leading singularity

\[
\frac1{(s-t)^2}.
\]

After inserting the cutoff phase, the model integral is

\[
\int_\mathbb R
\frac{
1-
\cos(2Lr)
}{r^2}dr.
\]

It satisfies

\[
\boxed{
\int_\mathbb R
\frac{1-
\cos(2Lr)}{r^2}dr
=CL.
}
\]

Thus oscillation against the diagonal singularity creates linear cutoff growth rather than decay.

## First-order phase correction

Write

\[
\gamma_\chi(s)
=
e^{i\vartheta_\chi(s)}.
\]

Near the diagonal `s=t+r`,

\[
\vartheta_\chi(t+r)
-
\vartheta_\chi(t)
=
r\vartheta_\chi'(t)
+O(r^2).
\]

Therefore

\[
\gamma_\chi(t+r)
\overline{\gamma_\chi(t)}
=
1+i r\vartheta_\chi'(t)
+O(r^2).
\]

When multiplied by the Hardy `r^(-2)` singularity:

- the constant term produces the bulk `L` contribution;
- the linear phase term produces a principal-value `r^(-1)` contribution;
- the latter is governed by `vartheta_chi'(t)`.

But

\[
\boxed{
\vartheta_\chi'(t)
=
\frac1{i}
\partial_t
\log\gamma_\chi(t),
}
\]

which is exactly the local Tate/gamma connection entering the Weil distribution.

## Expected localized expansion

For an observer multiplier `m_(g,chi)`, the characterwise sewing trace should have an expansion of the form

\[
\boxed{
\mathcal E_{L,\chi}(g)
=
La_\chi(g)
+
b_\chi(g)
+
o(1).
}
\]

The coefficients have distinct origins:

\[
a_\chi(g)
=
\text{universal Hardy/Plancherel density},
\]

\[
\boxed{
b_\chi(g)
=
\int_\mathbb R
|m_{g,\chi}(t)|^2
c_\chi(t)
\frac1{i}
\partial_t
\log\gamma_\chi(t)dt
+
\text{endpoint term},
}
\]

where `c_chi` records the exact Hardy and Fourier normalization.

This is the operator-theoretic route by which the gamma/prime connection can reappear as the finite sewing term.

## Strong-Szego/Widom structure

The relevant classical pattern is:

1. truncate a Wiener--Hopf/Toeplitz operator to a long interval or half-line boundary;
2. conjugate by a unimodular scattering symbol;
3. insert a smooth observable;
4. expand the trace into volume, boundary, and symbol-phase terms.

Strong-Szego and Widom formulas give precisely this type of asymptotic. In the present notation, the theorem must be observer-localized, characterwise, and uniform enough to sum over the angular dual.

## Why the regular sinc model could vanish

The earlier half-line/sinc calculation had only one nonsingular cross-boundary kernel after the geometric overlap factor `-u` cancelled the sinc singularity. Its remaining integrand was `L1`, so Riemann--Lebesgue applied.

The exact Tate--Hardy ordering contains an additional Hardy projection and its diagonal singularity. Consequently the sinc model and the Tate--Hankel model are not the same trace expression unless an algebraic cancellation removes that extra singularity.

This distinction must be checked in the precise two-cutoff factorization.

## Bulk coefficient audit

A linear term `L a_chi(g)` in the sewing trace would modify the leading bulk density of the positive triple compression. Therefore one must determine `a_chi(g)`, not assume it vanishes.

Connes's product trace has universal coefficient

\[
2Lh(1).
\]

For the positive feature to have the same leading density, the summed sewing coefficient must satisfy

\[
\boxed{
\sum_\chi
a_\chi(g)
=0.
}
\]

This cancellation may follow from:

- opposite Hardy corners;
- the two cutoff polarities;
- observer polarization;
- subtraction of the two-copy bulk counterterm.

It is not implied by the previous `O(L)` bound.

## Finite coefficient and local Weil current

If the linear sewing coefficient cancels, the candidate finite term is the logarithmic derivative of the Tate scattering phase:

\[
\boxed{
\frac1{2i}
\partial_t
\log\gamma_S(\chi,t).
}
\]

After summing characters and local places, this is the same connection operator previously denoted

\[
V_{loc,S}(t).
\]

Thus the desired `C_34` comparison can be reformulated as equality between:

- the finite Widom boundary coefficient of the positive cutoff pair;
- the metric connection of the dual--canonical Tate pairing.

This is stronger and more precise than final scalar equality.

## Exact theorem required

For bounded observer packets and every angular character, prove

\[
\boxed{
\begin{aligned}
\mathcal E_{L,\chi}(g)
&=
La_\chi(g)\\
&\quad+
\left\langle
m_{g,\chi},
V_{\chi}m_{g,\chi}
\right\rangle\\
&\quad+
e_{end,\chi}(g)
+o_{g,\chi}(1),
\end{aligned}
}
\]

where

\[
V_\chi
=
\frac1{2i}
\partial_t
\log\gamma_\chi(t),
\]

and the remainder is rapidly summable in `chi`.

Then verify that the completed two-polarity bulk subtraction cancels

\[
\sum_\chi La_\chi(g).
\]

## Required uniformity

To sum angular modes, require for every `N`

\[
|o_{g,\chi}(1)|
\le
\epsilon_L
C_{g,N}
(1+|\chi|)^{-N},
\qquad
\epsilon_L\to0.
\]

Polynomial gamma-factor derivative growth is then dominated by rapid observer decay.

## Status of positivity

Even if the finite sewing coefficient equals the local Weil current, positivity is not automatic. The completed positive boundary norm must include:

- the positive triple-compression residual;
- the conjugate cutoff polarity;
- endpoint--gamma correction;
- Sonin/radical conditioning.

The Widom formula identifies the missing boundary coefficient; it does not by itself prove its sign.

## Disposition

The large-cutoff sewing problem is now identified as a localized strong-Szego/Widom theorem:

\[
\boxed{
\text{Hardy diagonal singularity}
+
	ext{cutoff oscillation}
+
	ext{Tate scattering phase}.
}
\]

Riemann--Lebesgue cannot be applied before removing the `1/(s-t)^2` singularity. The finite term is expected to be the logarithmic derivative of the Tate gamma factor, exactly the spectral connection on edge `C_34`.
