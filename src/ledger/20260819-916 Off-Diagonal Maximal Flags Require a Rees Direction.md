# 916 — Off-Diagonal Maximal Flags Require a Rees Direction

## Uniformity falsifier

Entries 912–914 close the (D_3)-orbit of the diagonal maximal flag

[
(a,x,q)=(s_{14},s_{23},s_{235})=0.
]

The same source block also contains off-diagonal subchannel poles

[
y=s_{35},
qquad
z=s_{25},
qquad
q=x+y+z.
]

The next question is whether

[
(a,y,q)=0
]

and its reflected (z)-partner carry the same ordinary or filtered packet.

## Numerical discovery

For the source-normalized transition

[
widehat T_3=
sin(pi q)sin(pi a),
M_{m block}mathcal S^T,
]

the diagonal approach (a=q=y=h) has a finite nonzero limit. The corresponding (z)-approach behaves likewise. By contrast, the (x)-flag norm decays linearly, in agreement with Entry 912.

This numerical distinction does not define an ordinary corner value; it only motivates the exact order test.

## Exact six-route test

Keep (X) tangential and use multiplicative Laurent coordinates

[
Q=XYZ,
qquad
Z=rac{Q}{XY}.
]

The six orders of

[
A_4	o1,
qquad
Y	o1,
qquad
Q	o1
]

give the following numbers of nonzero matrix entries:

[
egin{array}{c|c}
	ext{order}&	ext{nonzero entries}\
hline
(A_4,Y,Q)&0\
(A_4,Q,Y)&0\
(Y,A_4,Q)&6\
(Y,Q,A_4)&6\
(Q,A_4,Y)&0\
(Q,Y,A_4)&6
end{array}
]

Every route is finite after exact cancellation, but the routes disagree.

Therefore

[
oxed{
operatorname{Sp}_{a=y=q=0}widehat T_3
	ext{ is not an ordinary order-independent specialization.}
}
]

The finite diagonal-path limit is a chosen normal direction, not a canonical pullback.

## Reflection

The source reflection exchanging labels (2leftrightarrow3) fixes (x=s_{23}) and exchanges

[
y=s_{35}
longleftrightarrow
z=s_{25}.
]

Hence the same classification applies to the (z)-flag.

## Narrow conclusion

The maximal flags split into at least two coefficient-geometric types:

[
oxed{
egin{array}{c|c}
x	ext{-flag}&	ext{ordinary value }0, 	ext{first conormal grade rank }1\
y/z	ext{-flags}&	ext{ordinary iterated specialization order dependent}
end{array}
}
]

This falsifies uniformity of the local coefficient packet. It does not require a new carrier stratum: all three flags already belong to the frozen associahedral/channel carrier.

## Next falsifier

Construct the source-derived multi-Rees space for the off-diagonal ideal

[
(a,y,q)
]

using valuations read from the complete transition, not a fitted diagonal path. Determine its exceptional divisor, chart transitions, and whether the finite diagonal limit descends to a canonical associated-grade class.
