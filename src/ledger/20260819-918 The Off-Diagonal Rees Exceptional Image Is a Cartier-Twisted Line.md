# 918 — The Off-Diagonal Rees Exceptional Image Is a Cartier-Twisted Line

## Frozen blowup

Entry 916 proves that the off-diagonal flag

[
(a,y,q)=(s_{14},s_{35},s_{235})=0
]

has no ordinary order-independent specialization. The source poles are simple in all three normals, so the first admissible resolution is the ordinary Rees blowup

[
operatorname{Bl}_{(a,y,q)}.
]

No weights are fitted from the diagonal path.

In multiplicative Laurent coordinates, take the (a)-chart

[
A_4-1=H,
qquad
Y-1=UH,
qquad
Q-1=VH.
]

The exceptional divisor is (H=0).

## Implementation repair

The first draft checker accidentally reused a multiplicative-specialization helper and evaluated (H=1). That affine slice was rejected before admission. The repaired checker substitutes

[
oxed{H=0}
]

after exact pullback and cancellation. Only the repaired calculation is evidence for this entry.

## Exact exceptional matrix

The corrected exceptional restriction has six nonzero entries, all in the second row:

[
R_E=
rac1U
egin{pmatrix}
0&0&0&0&0&0\
r_1&r_2&r_3&r_4&r_5&r_6
end{pmatrix},
]

where the (r_i) are nonzero rational functions of the tangential KLT letters

[
X,A_2,A_3,B_{24},B_{34}.
]

They contain neither (U) nor (V). Consequently

[
operatorname{rank}R_E=1,
]

and the projective image

[
[R_E]inmathbf P^5
]

is constant over the generic (a)-chart.

## Cartier typing

The affine representative has a simple pole on

[
U=0,
]

the exceptional direction where (y) vanishes faster than (a). Multiplication by the source-derived local equation (U) produces a regular nonzero generator.

Thus the canonical object is not an affine-normalized vector. It is the Cartier-twisted line

[
oxed{
mathcal L_{m off}
simeq
mathcal O_E([U=0])otimes
mathbf Qlangle r_{m tan}angle
}
]

on this chart, with a constant projective image and divisor-controlled normalization.

The ratio (V=(Q-1)/(A_4-1)) does not enter the exceptional class.

## Narrow conclusion

The Rees blowup resolves Entry 916's finite order dependence without adding a carrier stratum:

[
oxed{
	ext{order-dependent ordinary limits}
longrightarrow
	ext{canonical projective rank-one exceptional line}
+	ext{ Cartier twist}.
}
]

The diagonal path (U=V=1) merely chooses one affine frame of this line.

## Scope and next falsifier

Only the (a)-chart has been computed. Global descent requires the (y)- and (q)-charts and their overlap transitions. The next test must verify that the three local projective lines glue and that their Cartier transition functions are exactly those induced by the Rees blowup. Failure of gluing would invalidate the global line while leaving the local calculation intact.
