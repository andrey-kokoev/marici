# Arbitrary-n one-loop MHV Kermit count and covariance

The sourced one-loop MHV integrand is

$$
\mathcal A_n^{(2),1}
=
\sum_{1<a<b<n}K[a;b],
$$

with

$$
K[a;b]
=
\frac{
\langle d^2A\,AB\rangle\langle d^2B\,AB\rangle
\langle AB\mid(1aa{+}1)\cap(1bb{+}1)\rangle^2
}
{
\langle AB1a\rangle
\langle ABa(a{+}1)\rangle
\langle AB(a{+}1)1\rangle
\langle AB1b\rangle
\langle ABb(b{+}1)\rangle
\langle AB(b{+}1)1\rangle
}.
$$

## Count

The labels satisfy

$$
2\le a<b\le n-1.
$$

Therefore

$$
N_K(n)=\binom{n-2}{2}=\frac{(n-2)(n-3)}2.
$$

This gives one term at four points and three terms at five points, matching the explicit source examples.

## External projectivity

Write

$$
N_{a,b}
=
\langle A1a(a{+}1)\rangle\langle B1b(b{+}1)\rangle
-
\langle B1a(a{+}1)\rangle\langle A1b(b{+}1)\rangle.
$$

Before squaring, `N_(a,b)` has weight two in label `1` and weight one in each occurrence of `a,a+1,b,b+1`. Its square therefore has weights four and two respectively, with multiplicities added when `b=a+1`. The six denominator brackets have exactly the same label incidence. Hence every external momentum twistor has net weight zero in every term.

## Loop-line covariance

Under a change of basis of the loop line,

$$
(A,B)\longmapsto(A,B)g,
\qquad g\in GL(2),
$$

every bracket `langle ABij rangle` acquires `det(g)`. The intersection numerator acquires one determinant and its square acquires `det(g)^2`. Thus the rational factor has weight

$$
\det(g)^{2-6}=\det(g)^{-4}.
$$

The projective line measure has the compensating weight `det(g)^4`, so each complete Kermit form is individually `GL(2)` invariant.

Consequently the arbitrary-n finite sum has zero external projective weight and is a well-defined form on the space of momentum-twistor lines.

## Evidence and boundary

`check_arbitrary_n_one_loop_mhv_kermit_covariance.py` checks the incidence calculation for every term through `n=50`. The theorem itself follows directly from the displayed source formula for every `n>=4`.

This does not yet prove cancellation of the nonlocal poles between Kermit terms, cyclic invariance of the sum, or any integrated amplitude statement.
