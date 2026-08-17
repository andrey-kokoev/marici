# 20260817-355 — Double-Soft Physical Comparison Is a Two-Axis Rees Module

## Question

Entry 353 extended the physical Cut--nearby comparison through either individual site-soft branch. The remaining corner is

[
x=X_1=0,qquad y=X_2=0,
]

where both site-soft normals vanish simultaneously.

The hard-to-vary claim is:

[
oxed{
	ext{the double-soft corner produces a new mixed class, torsion prime, or
support generator not obtained from the two soft axes and occurrence
identifications.}
}
]

## Frozen maps

Retain the source occurrence matrices

[
Phi_{m exc}
=
egin{pmatrix}
1&-1&1&-1\
1&1&-1&-1\
1&-1&-1&1
end{pmatrix},
]

[
J=
egin{pmatrix}
2&0&1\
0&2&1\
0&0&1
end{pmatrix},
qquad
K=
egin{pmatrix}
0&0&1&-1\
0&1&0&-1\
1&-1&-1&1
end{pmatrix},
]

with

[
Phi_{m exc}=JK,
qquad
ker K=mathbb Z(1,1,1,1),
qquad
operatorname{coker}K=0.
]

The physical enhanced coordinates are

[
(y e_3,;x e_5,;e_6).
]

Thus the two-normal Rees operator is

[
D(x,y)=operatorname{diag}(y,x,1).
]

## Exact comparison

Over

[
R=mathbb Z[x,y],
]

exact multiplication gives

[
oxed{
D(x,y)Phi_{m exc}
=
(D(x,y)J)K.
}
]

Unimodular row operations

[
R_1mapsto R_1-yR_3,
qquad
R_2mapsto R_2-xR_3
]

reduce (D(x,y)J) to

[
operatorname{diag}(2y,2x,1).
]

After permutation, the exact presentation is

[
oxed{operatorname{diag}(1,2x,2y).}
]

## Why there is no ordinary Smith form

The ring (mathbb Z[x,y]) is not a principal ideal domain, and the second determinantal ideal is not principal. Therefore a one-variable Smith triple is not a valid invariant at the double corner.

The correct Fitting ideals are

[
oxed{
I_1=(1),
qquad
I_2=(2x,2y),
qquad
I_3=(4xy).
}
]

The nonprincipal ideal ((x,y)) records the already frozen transverse intersection of the two site-soft Cartier divisors. It is not evidence for a third carrier generator.

## Multi-Rees grades

At the ordinary origin (x=y=0), only the unit direction survives:

[
operatorname{rank}_{(0,0)}=1.
]

The other two directions occur separately in the first normal grades:

[
operatorname{rank}_{(1,0)}=1,
qquad
operatorname{rank}_{(0,1)}=1.
]

There is no additional primitive direction in grade ((1,1)). Hence

[
oxed{
1+1+1=3,
}
]

recovering the generic conductor/enhanced rank as a two-axis Rees object.

## Result

The tested claim is falsified.

- no new torsion prime appears;
- the only integer saturation remains the existing two occurrence factors of (2);
- support is exactly (x=0), (y=0), and their ordinary intersection;
- no product-only (xy) class appears;
- the diagonal occurrence relation remains the sole relation;
- the filtered Cut--nearby comparison remains exact.

Thus

[
oxed{
	ext{double-soft physical comparison}
=
	ext{one central grade}
oplus
	ext{one }x	ext{-grade}
oplus
	ext{one }y	ext{-grade}.
}
]

No new carrier datum is required.

## Classification

| Datum | Home |
|---|---|
| unit direction | ordinary double-soft fiber |
| (2x) direction | (X_1)-Rees grade plus occurrence saturation |
| (2y) direction | (X_2)-Rees grade plus occurrence saturation |
| ((2x,2y)) | existing two-axis soft incidence |
| (4xy) determinant | product of frozen soft normals and occurrence factors |
| new carrier structure | none |

## Scope

This is the integral occurrence/Rees comparison after the source orientation twist and common Leray normalization. It does not yet:

- sew all three cyclic marked-Cut sectors at the double-soft point;
- include simultaneous collision with an independent conductor or elliptic discriminant;
- construct a global integral basis over the entire energy arrangement;
- establish the full wavefunction normalization omitted by the source.

## Evidence

- `research/benincasa/double-soft-rees-certificate.json`;
- `research/benincasa/marici-gm/src/bin/double_soft_rees.rs`;
- entries 301, 308, 312, 353.

## Next falsifier

Transport the two-axis presentation cyclically to all three (q_{mathcal G_{ij}}) sectors while retaining the six lower-denominator occurrences. Compute the global occurrence/Cech gluing at pairwise and triple site-soft intersections. A non-Cech relation, new torsion prime, or divisor outside the frozen signed-energy arrangement would falsify global shared-carrier assembly.
