# The reciprocal Euler ratio supplies a canonical finite odd normalization candidate

## Exact local expansion

Let

[
gamma_p(z)
=
rac{1-p^{-1/2}e^{-zlog p}}
{1-p^{-1/2}e^{zlog p}}.
]

Put (a=p^{-1/2}) and (L=log p). Near (z=0),

[
loggamma_p(z)
=
2sum_{nge1}rac{a^n}{n}sinh(nLz).
]

Therefore

[
left.partial_zloggamma_p(z)ight|_{z=0}
=
2Lsum_{nge1}a^n
=
rac{2Lp^{-1/2}}{1-p^{-1/2}}.
]

This derivative is positive in the frozen orientation and changes sign under
(zmapsto-z).

## Odd Gram candidate

A natural endpoint-Gram normalization is

[
h_p^{mathrm{Euler}}
=
rac12
left.partial_zloggamma_p(z)ight|_{z=0}
=
rac{(log p)p^{-1/2}}{1-p^{-1/2}}.
]

The factor (1/2) matches the convention that the skew Hermitian block is

[
ih_p
egin{pmatrix}
0&1\
-1&0
end{pmatrix}.
]

This is a candidate normalization, not yet a linking theorem.

## Source agreement targets

The source already provides three reciprocal-odd quantities:

1. the signed zero-section position current;
2. the odd logarithmic Euler response;
3. the tail--principal-value Wronskian current.

The desired finite linking theorem is

[
h_p^{mathrm{zero}}
=
c_0h_p^{mathrm{Euler}},
qquad
h_p^{mathrm{Wr}}
=
c_Wh_p^{mathrm{Euler}},
]

with nonzero source-derived constants (c_0,c_W) fixed by the same sign frame.
If the odd mixed sector is one-dimensional, these equations cross-calibrate
three presentations of one coordinate. If it is two-dimensional, they are
insufficient without a rank-two observer theorem.

## Asymptotic budget

The Euler candidate obeys

[
h_p^{mathrm{Euler}}
sim
rac{log p}{sqrt p}.
]

Thus it decays at prime scale and belongs to every positive exponential dual
rung. After multiplying by the primitive--square coefficient product, its
diagonal contribution is bounded by a constant multiple of

[
rac{log p}{p^2},
]

which is absolutely summable. The odd port introduces no new seam divergence
on the prime diagonal.

Finite faithfulness nevertheless requires normalization relative to the norm
of the odd basis vector. Decay of the scalar coordinate alone is not loss of
faithfulness if the source odd vector has the same scale.

## Positivity compatibility

For the full endpoint Gram

[
G_p=
egin{pmatrix}
a_p&x_p+ih_p\
x_p-ih_p&b_p
end{pmatrix},
]

positivity requires

[
(h_p^{mathrm{Euler}})^2
le
a_pb_p-x_p^2.
]

This is now a falsifiable comparison between the independently derived even
Green plane and the odd Euler normalization. Failure has three possible
meanings:

- the chosen normalization constants are wrong;
- the complete form is not positive Hermitian;
- the odd port belongs to an enlarged coefficient space rather than the same
  two-dimensional Gram.

It must not be repaired by rescaling (h_p) after the fact.

## Determinant cross-check

If the determinant lens independently supplies

[
Delta_p=det G_p,
]

then

[
|h_p|
=
sqrt{a_pb_p-x_p^2-Delta_p}.
]

Agreement with (h_p^{mathrm{Euler}}) tests the magnitude, while the
reciprocal odd current fixes the positive or negative branch. This is the exact
three-lens calibration.

## Remaining theorem

The source calculation must prove that

[
Phi_p^{mathrm{odd}}
left(
rac{B_{alpha,p}-B_{alpha,p}^*}{2i}
ight)
=
h_p^{mathrm{Euler}}
]

in the frozen normalization, and identify the same number through the
zero-section and polarized Wronskian ports.

Until that triangle commutes, (h_p^{mathrm{Euler}}) is only the strongest
available candidate for the missing imaginary Gram coordinate.
