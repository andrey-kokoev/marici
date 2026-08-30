# 2892 — The Opposite Internal Bypass Has an Exact Soft Finite-Part Shift

## Rational route coefficient

Let

\[
\delta=\xi+\kappa,
\qquad
a=1-\kappa,
\qquad
B=\frac{3-\kappa}{(1-\kappa)^2}.
\]

The internal marked residue of Entry 2885 has the exact partial fraction
decomposition

\[
64p^4R
=
-\frac{B}{\delta+a}
+\frac{B}{\delta}
-\frac{2}{a\delta^2}
+\frac{2(1+\kappa)}{\delta^3}.
\]

An exact primitive is

\[
F_R(\delta)
=
\frac1{64p^4}
\left[
B\log\!\left(\frac{\delta}{\delta+a}\right)
+\frac{2}{a\delta}
-\frac{1+\kappa}{\delta^2}
\right].
\]

## Pointed route difference

The basepoint \(t=2\), equivalently \(\xi=1\), has

\[
\delta_0=1+\kappa.
\]

Therefore the two globally continued route primitives differ by

\[
\Delta P_{\rm route}
=
2\pi i
\left[
F_R(\delta)-F_R(1+\kappa)
\right].
\]

Near the soft endpoint \(t=\xi+1=0\), the additional logarithmic coefficient,
before multiplying by \(2\pi i\), is

\[
-\frac{B}{64p^4}.
\]

After subtracting that logarithm in the same pointed coordinate \(t/2\), the
finite route shift is

\[
\operatorname{FP}_{\rm route}
=
\frac{2\pi i}{64p^4}
\left[
B\log\!\left(-\frac{1-\kappa}{1+\kappa}\right)
-\frac{4}{(1-\kappa)^2}
\right].
\]

The source negative-imaginary boundary value fixes the branch of the displayed
logarithm.

## Consequence

The opposite bypass is physically distinguishable before any coarse trace. It
changes both:

- the soft logarithmic coefficient;
- the pointed finite part.

These changes are predicted by the existing marked Leray packet. They are not
free subtraction constants and do not require adding carrier support.

## Interpretation

The source \(i\epsilon\) prescription now has an explanatory role: it selects
one of two globally distinct affine transports whose difference is calculated
independently from the internal marked incidence.

## Remaining gate

Compose this exact route correction with the complete rank-two elliptic period
block and test whether the source-selected branch contributes only to the
algebraic/Tate extension or also changes the elliptic quotient.

## Durable artifacts

- `research/benincasa/check_soft_internal_route_finite_part.py`
- `research/benincasa/soft-internal-route-finite-part.json`

