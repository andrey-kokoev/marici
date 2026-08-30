# Finite zero packets have strict full-interval energy

## Vacuum transversality

On the arithmetic coefficient module, the Mellin readout is

\[
\ell_s(e_n)=n^{-s}.
\]

For the multiplicative vacuum,

\[
\ell_s(e_1)=1.
\]

Hence

\[
\ker\ell_s\cap\operatorname{span}\{e_1\}=0.
\]

Multiplication by the completed archimedean factor does not change this
inside the open critical strip: the Gamma factor is nowhere zero, and the
elementary completion zeros lie at the excluded endpoints.

Thus a nonzero scalar-null coefficient packet cannot be supported only on the
vacuum.

## Full interval energy

The primitive interval plus all valuation-excess intervals give coefficient

\[
\log n.
\]

For a finite packet

\[
c=\sum_nc_ne_n,
\]

define the coupled energy

\[
\mathcal E(c)
=
2\int_{\mathbb R}e^{-\pi u^2}\,du
\sum_n|c_n|^2\log n.
\]

Since the Gaussian integral is one,

\[
\mathcal E(c)=2\sum_n|c_n|^2\log n\ge0.
\]

Its kernel is exactly \(\operatorname{span}\{e_1\}\). Vacuum transversality
therefore gives

\[
c\ne0,quad \ell_s(c)=0
\quad\Longrightarrow\quad
\mathcal E(c)>0
\]

for every finite-support packet.

## What is genuinely proved

This is a universal finite algebraic theorem. It uses:

1. the source-derived two-front Gaussian density;
2. the exact primitive-plus-excess identity;
3. the Mellin character on the vacuum;
4. no zero locations or fitted positivity.

Every finite scalar cancellation necessarily involves a nonvacuum label, and
every nonvacuum label crosses at least one positively oriented prime-scale
interval.

## Why this is not RH

The completed Riemann section is not presently represented as the readout of
a vector in the Hilbert completion of this finite coefficient module. The
distinguished Euler packet is not square summable in the displayed energy,
and relative heat finite part acts only after a boundary subtraction.

Consequently three limit statements remain unproved:

1. the zero-to-state bridge lands in a completion of the full interval
   energy domain;
2. the two-front Green identity extends continuously to that completion;
3. no normalized zero-state escapes through the scale boundary while its
   energy becomes invisible.

Finite strict positivity does not imply any of these.

A further scope correction is proved in
`full-interval-energy-is-state-norm-not-riemann-overlap.md`. The interval
energy depends only on coefficient magnitudes and is the radial derivative of
the transported source norm. It does not by itself supply the mixed
source–observer Green identity required to constrain a Riemann zero.

## Sharp completion falsifier

A sequence of finite packets \(c_X\) falsifies the proposed completion if

\[
\ell_s(c_X)\to0,
\qquad
\|c_X\|_{\mathrm{source}}=1,
\qquad
\mathcal E(c_X)\to0,
\]

while its relative theta/Fock limit is nonzero. Such a sequence can only
concentrate toward the vacuum or escape to a boundary grade not controlled by
\(\log n\).

The primitive, square, constant–delta, and archimedean graph seminorms must
exclude precisely this escape.

## Result

Every nonzero finite-support Mellin-null packet has strictly positive full
interval energy. The squarefree and vacuum kernels are both repaired at the
finite algebraic level. The sole remaining obstruction is construction and
strict completion of the actual theta zero-state domain.
