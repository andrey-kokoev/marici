# Unitary cut supplies observability subject to the mixed angle

Let

$$
C_a:H\to H_{\rm tail,a}\oplus H_{\rm seam,a}
$$

be the complete cut. Since `C_a` is unitary,

$$
\|C_av\|=\|v\|.
$$

Thus the diagonal cut form

$$
b_{\rm cut}[v]=\|C_av\|^2
$$

has lower bound one and is a noncompact complementary observer to theta sampling.

Suppose the complete Green form is assembled as

$$
b[v]=b_{\rm cut}[v]+b_{\rm aux}[v]+2\operatorname{Re}c[v],
$$

where `b_aux>=0` contains theta, wall, reciprocal, linking, and normalized connected contributions. If the mixed term obeys

$$
|c[v]|
\le\rho\,
 b_{\rm cut}[v]^{1/2}b_{\rm aux}[v]^{1/2},
\qquad 0\le\rho<1,
$$

then

$$
b[v]
\ge(1-\rho)
\bigl(b_{\rm cut}[v]+b_{\rm aux}[v]\bigr)
\ge(1-\rho)\|v\|^2.
$$

Therefore the pointed arithmetic form satisfies

$$
f[v]=\|\Phi\|^2\|v\|^2
\le\frac{\|\Phi\|^2}{1-\rho}\,b[v].
$$

The compactness of theta sampling is no longer an obstruction once the full cut is retained. The only remaining analytic condition for domination is a uniform strict mixed-angle bound `rho<1` after radical descent and cutoff completion.

This estimate is valid only if the source Green identity includes the cut norm with its positive orientation. If the tail and seam are first codiagonalized into a cancelling boundary row, the unitary lower bound is lost.

Status: noncompact observability and relative form bound reduced to the uniform mixed-angle theorem.
