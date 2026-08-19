# 919 — The Off-Diagonal Exceptional Line Glues with a Degree-Zero Hecke Modification

## Globalization problem

Entry 918 constructs the off-diagonal exceptional image in the (a)-chart of

[
E=mathbf P(n_a,n_y,n_q),
]

where

[
n_a=A_4-1,
qquad
n_y=Y-1,
qquad
n_q=Q-1.
]

Its scalar factor is (1/U), with

[
U=rac{n_y}{n_a}.
]

The projective image is constant locally. The remaining question is whether this line glues over all three standard Rees charts.

## Chart factors

Use the following coordinates.

On the (a)-chart:

[
U=rac{n_y}{n_a},
qquad
V=rac{n_q}{n_a},
qquad
f_a=rac1U.
]

On the (y)-chart:

[
A=rac{n_a}{n_y},
qquad
W=rac{n_q}{n_y},
qquad
f_y=A.
]

On the (q)-chart:

[
C=rac{n_a}{n_q},
qquad
D=rac{n_y}{n_q},
qquad
f_q=rac CD.
]

## Exact overlap audit

The Symbolica checker verifies

[
f_yig|_{acap y}
=A
=rac1U
=f_a,
]

[
f_qig|_{acap q}
=rac{1/V}{U/V}
=rac1U
=f_a,
]

and

[
f_qig|_{ycap q}
=rac{A/W}{1/W}
=A
=f_y.
]

No additional unit or sign appears.

Therefore the rank-one projective image of Entry 918 glues globally on (E).

## Global divisor

The common rational factor is

[
f=rac{n_a}{n_y}.
]

Its divisor is

[
oxed{
operatorname{div}(f)=D_a-D_y,
}
]

where

[
D_a={n_a=0},
qquad
D_y={n_y=0}.
]

The (q)-direction has coefficient zero. The divisor has projective degree zero.

Thus the globally typed coefficient object is a constant projective line with a degree-zero Hecke/Cartier lattice modification:

[
oxed{
mathcal L_{m off}^{m mer}
=
mathbf Qlangle r_{m tan}angle
otimes
mathcal O_E(D_a-D_y).
}
]

## Correction to the local description

Entry 918's (a)-chart pole at (U=0) is the (D_y) part of this divisor. The complementary zero on (D_a) lies outside that affine chart and becomes visible only after gluing. The global datum is therefore (D_a-D_y), not merely a single local pole.

## Narrow conclusion

The off-diagonal order dependence is completely absorbed by the existing Rees exceptional geometry:

[
oxed{
	ext{constant projective line}
+
	ext{degree-zero lattice modification }D_a-D_y.
}
]

No new carrier cell, divisor, or fitted normalization is introduced.

## Next falsifier

Test the reflected (z)-flag and the reflection overlap. The expected divisor is

[
D_a-D_z.
]

The decisive question is whether the (y)- and (z)-lines are exchanged strictly by the source reflection or require an additional sign/unit on their common exceptional atlas.
