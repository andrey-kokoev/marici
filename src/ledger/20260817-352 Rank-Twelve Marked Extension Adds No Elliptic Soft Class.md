# 20260817-352 — The Rank-Twelve Marked Extension Adds No Elliptic Soft Class

## Question

Entry 351 closed the site-soft supported extension in the homogeneous nine-master (q_{mathcal G_{12}})-only module. The physical three-denominator sector contains three additional conductor/top quotient classes, so that result did not yet test the canonical marked localization extension

[
0	o H^2(S_E)	o H^2(S_Esetminus W_E)
	o H^1(W_E)(-1)	o0
]

of ranks (9	o12	o3).

The hard-to-vary claim tested here is:

[
oxed{
	ext{one of the three marked extension columns acquires a nonzero elliptic
principal part on }X_1X_2=0.
}
]

## Frozen extension columns

At (E=0), put (x=X_1), (y=X_2), and (s=x+y). Retain the source-derived algebraic vector

[
v_0=x^2y^2igl((x^2-y^2)e_7+2e_8-2e_9igr).
]

The complete marked algebraic block from Entry 300 is

[
Theta_{101}^{m fix}
=-rac{e_4}{4xy}
-rac{v_0}{4x^3y^3s},
]

[
Theta_{110}^{m fix}
=-rac{e_2}{4xy}
+rac{v_0}{4x^3y^3s},
]

[
Theta_{111}^{m filt}
=rac{e_6}{8s}.
]

No lift, support summand, or carrier cell is changed.

## Exact Gysin identity

At (E=0), the infinity-Gysin map on ((e_7,e_8,e_9)) is

[
e_7mapstoomega_0,
]

[
e_8mapstorac{y^2}{2}omega_0-rac{x^2}{2}omega_2,
]

[
e_9mapstorac{x^2}{2}omega_0-rac{x^2}{2}omega_2.
]

Therefore

[
R_inftyigl((x^2-y^2)e_7+2e_8-2e_9igr)=0
]

as a polynomial identity. The other coordinates (e_2,e_4,e_6) are already in the algebraic Gysin kernel.

## Soft principal parts

At (y=0), multiply the two wall columns by (y) before specializing. Their (v_0)-tails become finite multiples of

[
x^2e_7+2e_8-2e_9,
]

whose Gysin image remains zero on the specialized fiber.

At (x=0), exact source involution gives the corresponding vector

[
-y^2e_7+2e_8-2e_9,
]

again with zero Gysin image.

The primitive top column has denominator (s=x+y), so it is regular at either individual site-soft branch when the other site energy is nonzero.

Consequently,

[
oxed{
operatorname{rank}
R_infty!left(
operatorname{PP}_{X_1X_2=0}C_{m alg}
ight)=0.
}
]

## Executable replication

The polynomial identity, generic wall-column images, and both soft principal limits were checked at 128 samples over each of

[
p_1=2305843009213693951,
qquad
p_2=2305843009213693921,
]

with zero mismatches.

## Narrow result

Adding the three conductor/top classes of the canonical rank-twelve marked extension introduces simple Tate/Kummer soft poles internal to the algebraic kernel, but no new elliptic supported extension:

[
oxed{
	ext{rank-twelve soft nearby data}
=
	ext{existing algebraic soft poles}
+
	ext{the previously known elliptic degeneration}.
}
]

No new carrier datum is required.

## Scope

This establishes a de Rham/Gysin statement for the frozen marked total-energy residue. It does not yet:

- pair the marked extension with the global physical relative chain;
- construct the chain-level Cut--nearby commutator;
- prove an integral normal form through the soft collision;
- include simultaneous (x=y=0);
- sew the three cyclic (q_{mathcal G_{ij}}) sectors.

## Evidence

- `research/benincasa/marked-soft-support-certificate.json`;
- `research/benincasa/marked-soft-support-replication-certificate.json`;
- `research/benincasa/marici-gm/src/bin/marked_soft_support.rs`.

## Next falsifier

Pair the canonical physical Leray chain with the rank-twelve localization sequence at the corner

[
E_T=q_{mathcal G_{12}}=y_{12}=0.
]

Compute both orders of specialization—Cut then nearby, and nearby then Cut—using the frozen positive Cayley--Menger sheet and signed-minor boundary. The first nonzero commutator outside existing soft support or graph homology would falsify the current shared-calculus claim.
