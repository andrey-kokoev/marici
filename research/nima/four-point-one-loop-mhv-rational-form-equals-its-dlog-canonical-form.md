# Four-point one-loop MHV rational form equals its dlog canonical form

The source formula is

$$
\Omega_4^{(1)}
=
\frac{\langle d^2A\,AB\rangle\langle d^2B\,AB\rangle
      \langle1234\rangle^2}
{\langle AB12\rangle\langle AB23\rangle
 \langle AB34\rangle\langle AB41\rangle}.
$$

On the affine line chart

$$
A=(1,0,a,b),\qquad B=(0,1,c,d),
$$

with external twistors the standard basis, the relevant brackets are

$$
\langle AB12\rangle=ad-bc,
\quad
\langle AB23\rangle=d,
\quad
\langle AB34\rangle=1,
\quad
\langle AB41\rangle=a.
$$

The four source coordinates reduce to

$$
q_1=\frac{a}{b},
\qquad
q_2=-\frac{ad-bc}{b},
\qquad
q_3=-\frac d b,
\qquad
q_4=\frac1b.
$$

Their logarithmic Jacobian is exactly

$$
\det\left(\frac{\partial\log q_i}{\partial(a,b,c,d)}\right)
=
\frac1{ad(ad-bc)}.
$$

Therefore, with the displayed wedge orientation,

$$
d\log q_1\wedge d\log q_2\wedge d\log q_3\wedge d\log q_4
=
\frac{da\wedge db\wedge dc\wedge dd}
{\langle AB12\rangle\langle AB23\rangle
 \langle AB34\rangle\langle AB41\rangle}.
$$

This is the sourced rational box form. Its rational factor has `GL(2)` loop-basis weight `-4`; the projective line measure has weight `+4`, so the complete form has weight zero. Every external twistor also has projective weight zero.

The identity is checked exactly by `check_four_point_one_loop_mhv_dlog_identity.py`.

## Claim boundary

This is a pre-integration canonical-form identity. It does not evaluate the infrared-divergent box integral or choose a regulator.
