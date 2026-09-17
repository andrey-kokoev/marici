# qRB microstep 115: minimal Gaussian-pair response graph

The missing enlargement is the pair-response graph with coordinates

$$
(h_{nm},F_{nm},h_{nm}(0)).
$$

For each ordered pair `(n,m)`, retain the source equation

$$
\mathcal A_{nm}\rho_{nm}^{[a,b]}
=\alpha_{nm}\bigl[g_{nm}(b,\cdot)-g_{nm}(a,\cdot)\bigr],
$$

with

$$
\mathcal A_{nm}
=\partial_t+2\pi\frac{n^2m^2}{n^2+m^2}t,
\qquad
\alpha_{nm}=\frac{m^2}{n^2+m^2},
$$

and initial value

$$
\rho_{nm}^{[a,b]}(0)
=\int_a^b e^{-\pi(n^2+m^2)x^2}\,dx.
$$

This graph retains the separation coordinate and pair asymmetry that the one-copy wall port forgets. Any map to the wall/linking carrier must be defined on these three coordinates and preserve their source equation.

Status: minimal enlarged input object specified; the map into the existing relative linking carrier remains open.
