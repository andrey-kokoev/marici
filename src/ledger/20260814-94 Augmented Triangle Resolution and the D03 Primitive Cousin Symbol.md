# Augmented Triangle Resolution and the D03 Primitive Cousin Symbol

## Record

Date: 2026-08-14

Status: exact integral associated-grade theorem and sharp chain-lift boundary.
Entry 93's sheet-resolved normalization--conductor square supplies the correct
source of the first loaded (D=(0,3)) Cousin/Gysin symbol.  The source does
not pass through ordinary restriction of the global Möbius orientation cycle.

The six alternating-conductor terms land first in the three-tag module.  They
belong to an exact augmented triangle resolution

\[
\boxed{
0\longrightarrow\mathbf1_{\rm or}
\xrightarrow{\Delta}
P_{\rm tag}
\xrightarrow{\partial_\triangle}
P_{\rm road}
\xrightarrow{\epsilon}
\mathbf1
\longrightarrow0.
}
\]

Applying \(\partial_\triangle\) produces the QTDS contact matrix.  Applying
the Verdier-dual relation map \(\Delta^\vee\) **before** road incidence gives
the primitive boundary normalization.  After retaining the polarity line,
all six supported values are (+1).

At (D=03), entry 86's actual endpoint Cousin terms and occurrence weights
extend this normalization uniquely to entry 89's four unit road occurrences,
with polarized value (4).  Thus the associated-grade source and its
primitive composite are proved.

The full PC chain map is not proved.  No established scalar first-jet/BRST
differential in the repository preserves the normalization--conductor
filtration, so the identity

\[
d_{\rm circ}^{\rm PC}G_{03}^{\rm Cousin}
=G_{03}^{\rm Cousin}d_{\rm scalar}
\]

cannot be tested without inventing data.  Physical-Cut naturality is proved
only on the associated symbol; the full chain-level square remains untyped.

## The integral augmented triangle

Let

\[
P_{\rm tag}=\mathbb Z\langle d_0,d_1,d_2\rangle,
\qquad
P_{\rm road}=\mathbb Z\langle q_0,q_1,q_2\rangle.
\]

With the orientations of entries 59, 64, 66, and 89, use

\[
\Delta(1)=(1,1,1),
\qquad
\epsilon(a_0,a_1,a_2)=a_0+a_1+a_2,
\]

and

\[
\partial_\triangle=
\begin{pmatrix}
0&-1&1\\
1&0&-1\\
-1&1&0
\end{pmatrix}.
\]

Then

\[
\partial_\triangle\Delta=0,
\qquad
\epsilon\partial_\triangle=0.
\]

The diagonal and augmentation are primitive.  The triangle matrix has rank
two and unit (2\times2) minors, so

\[
\ker\partial_\triangle=\operatorname{im}\Delta,
\qquad
\operatorname{im}\partial_\triangle=\ker\epsilon=A_2
\]

integrally.  Hence the displayed four-term sequence is exact without
inverting (3).

It is also Verdier self-dual up to orientation and degree reversal:

\[
\boxed{
\Delta^\vee=\epsilon,
\qquad
\partial_\triangle^\vee=-\partial_\triangle.
}
\]

This is the local self-dual carrier that was distributed across the road and
circuit discussions of entries 59, 64, and 89.

## The index-three gluing is intrinsic

Combine the primitive and contact branches into

\[
(\Delta^\vee,\partial_\triangle):
P_{\rm tag}\longrightarrow\mathbf1\oplus A_2.
\]

Using the first two road coordinates as an integral basis of (A_2), the
matrix is

\[
\begin{pmatrix}
1&1&1\\
0&-1&1\\
1&0&-1
\end{pmatrix}.
\]

Its Smith factors are

\[
\boxed{(1,1,3).}
\]

Therefore the primitive and QTDS branches jointly detect every rational tag,
but their integral image has index three.  The old (1/3) obstruction is not
an obstruction to the derived resolution.  It is precisely the nonsplit
integral gluing between the primitive quotient and the (A_2) contact
sector.  Retaining the augmented complex avoids every denominator.

## The conductor lands before incidence

Entry 93 identifies the alternating fusion carrier with a genuine
normalization--conductor cdh square and proves that its polarity-odd first
normal symbol has six sheet-resolved supports.  Taking the common
(y)-linear symbol gives the map

\[
K_{\rm alt}:N^\vee_{Z/\widetilde F}
\longrightarrow P_{\rm tag}
\]

with matrix

\[
K_{\rm alt}
=
\begin{pmatrix}
0&0&-1&0&0&1\\
-1&0&0&1&0&0\\
0&1&0&0&-1&0
\end{pmatrix},
\]

where columns are ordered as
((dx_0,dx_1,dx_2,dx_3,dx_4,dx_5)).
Every column is a signed individual tag.

Road incidence gives

\[
\boxed{
\partial_\triangle K_{\rm alt}
=
\begin{pmatrix}
1&1&0&-1&-1&0\\
0&-1&-1&0&1&1\\
-1&0&1&1&0&-1
\end{pmatrix}
=C_{\rm QTDS}.
}
\]

This recovers entry 66, but the order now matters.  The primitive branch is

\[
\boxed{
\Delta^\vee K_{\rm alt}
=(-1,+1,-1,+1,-1,+1).
}
\]

The even columns lie on the minus normalization sheet and the odd columns on
the plus sheet.  In the polarity line (L_{\rm pol}), the sheet orientations
are

\[
(-1,+1,-1,+1,-1,+1).
\]

Consequently

\[
\boxed{
(\Delta^\vee\otimes L_{\rm pol})K_{\rm alt}
=(1,1,1,1,1,1).
}
\]

No averaging, rational section, or division by (2) or (3) occurs.  The
primitive normalization is present before the contact incidence sends the
same tag data into (A_2).

## The (D=03) occurrence lift at associated grade

Entry 89 pairs the (D=03) road with (d_1^\vee).  The two relevant
conductor supports are

\[
dx_0\longmapsto-d_1,
\qquad
dx_3\longmapsto+d_1.
\]

After retaining the polarity line, both have positive primitive value.

The actual (D=03) road square is the tensor of the weighted intervals with
slots

\[
(x_0,x_1)\boxtimes(x_3,x_4).
\]

Use entry 86's marked endpoint counits, without forgetting their sink marks:

- on the plus sheet, the (x_3) sink term produces the occurrence weights
  (x_0x_3) and (x_1x_3);
- on the minus sheet, the (x_0) sink term produces the occurrence weights
  (x_0x_3) and (x_0x_4).

The common occurrence (x_0x_3) agrees on the two sheet-resolved sources; it
is not summed into a coefficient two.  For every displayed occurrence the
endpoint signs are

\[
(+1)_{\rm Cousin}
(-1)_{\rm scalar\ source}
(-1)_{\rm coaction}
=+1.
\]

Laurent duality pairs each weight with its inverse and gives unit value.  The
weighted-interval cocycle equations identify adjacent normalized occurrence
values.  Three unit corners therefore force the fourth:

\[
\boxed{
\begin{matrix}
x_0x_3&x_0x_4\\
x_1x_3&x_1x_4
\end{matrix}
\longmapsto
\begin{pmatrix}1&1\\1&1\end{pmatrix}.
}
\]

Thus the (D=03) associated-grade composite with entry 89's Verdier-dual
circuit map is exactly the primitive road boundary cocycle.  Its four
primitive occurrences have value one and its polarized value is four.
Dihedral transport gives the other two roads.

The ordered line at the nontrivial (D=03) stabilizer retains all three
factors:

\[
(-1)_{\rm tangential/C_3}
(-1)_{\rm polarity}
(+1)_{[dX_{03}]}
=+1.
\]

## Associated-grade Cut test

Two exact checks coexist without contradiction:

1. before incidence, (\Delta^\vee K_{\rm alt}\) gives the nonzero primitive
   normalization;
2. after incidence, every column of
   (C_{\rm QTDS}=\partial_\triangle K_{\rm alt}) lies in (A_2), hence has
   zero road augmentation.

Entry 86's complete endpoint residues are occurrence-wise equal on the two
polarity sheets:

\[
\operatorname{Res}_{03}^+
=\operatorname{Res}_{03}^-
=c_L\boxtimes c_R,
\]

with primitive-dual periods (4) and (4).  Therefore their physical
polarity difference vanishes.  The executable also verifies Ward closure of
all six post-incidence columns.

This proves the associated-grade physical-boundary square.  It does not prove
full PC Cut naturality because the source scalar differential and the image of
the circuit relation generator are not defined.

## Why ordinary global restriction still fails

For comparison, entry 91 identifies the five relative contact modes with
(H_1(\Gamma_8)).  Ordinary restriction of any graph cycle to the (D=03)
star obeys vertex conservation and hence lies in (A_2).  The checker verifies
that all five fundamental modes have primitive output zero.

Thus

\[
\text{global orientation cycle}
\xrightarrow{\rm ordinary\ restriction}A_2
\xrightarrow{\epsilon}0
\]

remains the wrong construction.  The positive result above uses the
normalization--conductor cdh square and lands in (P_{\rm tag}) **before**
triangle incidence.

## The exact remaining chain gap

The Ward target differential is established, and every one of entry 66's
seven-by-six columns is Ward closed.  But neither entry 93 nor any earlier
certificate constructs a scalar first-jet/BRST source differential preserving

1. the two normalization branches;
2. the conductor filtration;
3. the cdh/Čech comparison;
4. the PC Cousin and normal filtrations.

The checker retains the exact ambiguity witness from entry 89.  On the same
six source generators, both the zero differential and

\[
d(e_1)=e_0,
\qquad d^2=0,
\]

are square-zero.  The displayed Ward symbol is a chain map for the first and
not for the second.  Hence coefficient closure, endpoint signs, and the exact
augmented triangle cannot decide the full chain identity.

The next datum is not another sign or character.  It is an actual filtered
scalar first-jet/BRST complex and a lift

\[
\boxed{
G_{03}^{\rm Cousin}:
\operatorname{Tot}\check C
(\widetilde F\rightrightarrows\widetilde Z;
J_F^1\mathcal S)
\longrightarrow
\mathcal R_{03}^{\rm circ,PC}
}
\]

whose first conductor grade is (K_{\rm alt}\otimes L_{\rm pol}), whose
relation component realizes (\Delta), and whose endpoint restriction is the
entry-86 occurrence counit.  Only then can full physical-Cut naturality be
tested.

## Exact certificate

Run:

```text
rustfmt --edition 2021 --check research/voevodsky/check_d03_loaded_cousin_gysin_boundary.rs
rustc --edition=2021 -D warnings -O research/voevodsky/check_d03_loaded_cousin_gysin_boundary.rs -o "$env:TEMP\marici-d03-loaded-cousin-boundary.exe"
& "$env:TEMP\marici-d03-loaded-cousin-boundary.exe"
```

Certificate SHA-256:

```text
b4367cede237fdd81b0f0cbb2615b6e47951aaa8783eb519ba69724caeea9a79
```

## Decision

Promote:

> The first loaded (D=03) Cousin/Gysin symbol is sourced by the
> normalization--conductor cdh square and factors through the exact augmented
> triangle resolution.  Its incidence branch is the QTDS (A_2) contact
> symbol, while its Verdier-dual relation counit is the primitive road
> boundary symbol.  The two branches are jointly integral with index-three
> gluing, not a rational direct sum.

Retain as the immediate frontier:

> Construct the scalar first-jet/BRST differential preserving the conductor
> filtration and lift the proved associated symbol, endpoint Cousin map, and
> relation generator to one PC chain map.  Until then, full Cut naturality is
> conditional rather than falsified.

## Internal dependencies

- Entry 59: integral circuit-tag resolution.
- Entry 64: triangle suspension and orientation.
- Entry 66: six-term alternating-conductor and QTDS/Ward symbols.
- Entry 86: occurrence-resolved endpoint Cousin counit.
- Entry 89: Laurent road/circuit pairing and primitive normalization.
- Entries 91--92: contact recollement and ordinary-restriction no-go.
- Entry 93: normalization--conductor cdh square and polarity line.
- `research/voevodsky/check_d03_loaded_cousin_gysin_boundary.rs`.
