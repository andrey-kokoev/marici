# The raw two-ray four-grade Plucker point is fixed, so the missing complexity lives in translation and Green history

## Coefficient packet

Before applying the opposite translations `U_L` and `U_-L`, the exact
four-grade rays have coefficient matrix

\[
M(L)=
\begin{pmatrix}
-2\pi L^2&8\pi L&4\pi^2L^2&-8\pi^2L\\
-2\pi L^2&-8\pi L&4\pi^2L^2&8\pi^2L
\end{pmatrix}
\]

in the ordered grade basis `(f_0,f_1,f_2,f_3)`.

## Exact minors

Its six `2 by 2` minors are

\[
\begin{aligned}
P_{01}&=32\pi^2L^3,&
P_{02}&=0,\\
P_{03}&=-32\pi^3L^3,&
P_{12}&=64\pi^3L^3,\\
P_{13}&=0,&
P_{23}&=64\pi^4L^3.
\end{aligned}
\]

They satisfy the Plucker equation

\[
P_{01}P_{23}-P_{02}P_{13}+P_{03}P_{12}=0.
\]

After projectivization all dependence on `L` cancels:

\[
[P_{01}:P_{02}:P_{03}:P_{12}:P_{13}:P_{23}]
=
[1:0:-\pi:2\pi:0:2\pi^2].
\]

Thus the raw eight coefficients determine one fixed point of `G(2,4)`, rather
than a varying eight-dimensional chart.

## Consequence

The source-fixed even/odd coefficient packet already has complete linear
coherence. Its same-parity minors vanish and its mixed-parity minors have fixed
ratios. No transverse factor such as

\[
1-p^{-2\operatorname{Re}z}
\]

can arise from these raw Plucker coordinates.

The nontrivial dependence enters only after the two rows are placed at opposite
translations and evaluated in the completed relative Green/history form:

\[
g_+=U_L(E+O),
\qquad
g_-=U_{-L}(E-O).
\]

Accordingly, the relevant positive-geometric object is not the coefficient
plane alone. It must retain the translated incidence map and its Green metric,
with the fixed Plucker point serving as the internal four-grade fiber.

## Revised geometry

The candidate carrier has the form

\[
\{\text{fixed four-grade Plucker fiber}\}
\longrightarrow
\mathcal X_{\rm translated\ history}
\longrightarrow
\mathcal A_{n,2,4},
\]

or, infinitesimally, a translated-history orbit through the fixed coefficient
plane. The missing rung-four information is orbit/metric curvature, not an
additional raw coefficient minor.