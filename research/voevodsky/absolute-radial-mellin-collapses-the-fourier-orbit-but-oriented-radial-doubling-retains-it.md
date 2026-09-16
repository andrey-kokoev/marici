# Absolute radial Mellin collapses the Fourier orbit but oriented radial doubling retains it

## Question

Does the symmetric Hurwitz seed give a faithful strong-dual interface for the generic four-port Fourier orbit?

## Claim boundary

No. Absolute radialization identifies reflected support ports and conjugate character ports, collapsing the four-cycle to a two-cycle. Keeping positive and negative radial channels separately repairs the loss and yields an explicit oriented Hurwitz/periodic seed. Hilbert Green regularity is still not claimed.

## Collapse under absolute radialization

For \(a=r/q\), absolute radial Mellin pushforward gives

$$
\mathcal M_{|\cdot|}(P_a)
=\zeta(s,a)+\zeta(s,1-a).
$$

But \(-a\equiv1-a\pmod1\), so

$$
\mathcal M_{|\cdot|}(P_{1-a})
=\zeta(s,1-a)+\zeta(s,a)
=\mathcal M_{|\cdot|}(P_a).
$$

Similarly,

$$
\mathcal M_{|\cdot|}^{\times}(C_r)
=2\sum_{n\ge1}\cos(2\pi rn/q)n^{-s}
=\mathcal M_{|\cdot|}^{\times}(C_{-r}).
$$

Therefore the kernel contains

$$
P_a-P_{1-a},
\qquad
C_r-C_{-r}.
$$

The generic four-dimensional orbit maps to at most two dimensions. In character language, the \(\pm i\) sectors are erased. Thus the symmetric Hurwitz seed realizes only the Fourier half-turn quotient.

## Oriented radial double

Retain the positive and negative half-lines as distinct channels. Define

$$
\mathcal M_{\rm or}(T)
=
\left(
\langle T|_{x>0},x^{-s}\rangle,
\langle T|_{x<0},|x|^{-s}\rangle
\right).
$$

For the support port,

$$
\mathcal M_{\rm or}(P_a)
=
\bigl(\zeta(s,a),\zeta(s,1-a)\bigr),
$$

while

$$
\mathcal M_{\rm or}(P_{1-a})
=
\bigl(\zeta(s,1-a),\zeta(s,a)\bigr).
$$

Reflection is now the channel swap rather than an identification.

For the character ports, after retaining the zero atom separately,

$$
\mathcal M_{\rm or}^{\times}(C_r)
=
\left(
\sum_{n\ge1}e^{2\pi irn/q}n^{-s},
\sum_{n\ge1}e^{-2\pi irn/q}n^{-s}
\right),
$$

and \(r\mapsto-r\) swaps the channels. The two components are the conjugate periodic Dirichlet sections, not their cosine compression.

## Fourier orbit

Poisson/Hurwitz functional equations exchange the oriented support pair with the oriented character pair. Successive transforms retain

$$
P_a\to C_{-r}\to P_{1-a}\to C_r\to P_a
$$

without collapsing reflection. Hence the oriented radial double is the minimal radial target compatible with the generic order-four orbit.

## Endpoint completion

Each Hurwitz component has residue one at \(s=1\). Endpoint completion must therefore retain the oriented residue vector

$$
(1,1),
$$

rather than first summing it to the scalar residue two. This preserves the reciprocal channel swap.

## Disposition

The previously constructed symmetric Hurwitz seed is only the half-turn shadow and cannot supply the full G4 intertwiner. The corrected source-derived seed is the oriented pair \((\zeta(s,a),\zeta(s,1-a))\), together with conjugate periodic-character channels and the oriented endpoint residue \((1,1)\). This gives the properly typed order-four interface on the strong-dual radial double.