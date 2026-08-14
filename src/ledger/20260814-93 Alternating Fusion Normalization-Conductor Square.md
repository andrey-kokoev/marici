# Alternating Fusion Normalization-Conductor Square

## Record

Date: 2026-08-14

Status: exact integral algebraic theorem.  The two alternating fusion sheets
form a finite normalization/conductor square, and the entry-66 six-term
symbol is its canonical polarity-odd first associated grade.  This types the
sheet-resolved Cech/Cousin operation.  It does not construct a scalar
kinetic/BRST chain map or prove physical Cut descent.

## The fiber-product carrier

Put

\[
R=\mathbb Z[y_0,y_1,y_2],
\qquad
B_+=R[x_1,x_3,x_5],
\qquad
B_-=R[x_0,x_2,x_4],
\]

and let both augmentations

\[
\varepsilon_\pm:B_\pm\longrightarrow C=R
\]

be the zero sections in the short variables.  The alternating-fusion carrier
is the ring fiber product

\[
B=B_+\times_C B_-
=\{(f_+,f_-):\varepsilon_+(f_+)=\varepsilon_-(f_-)\}.
\]

There is a canonical isomorphism

\[
\boxed{
B\simeq
R[x_0,\ldots,x_5]/
\bigl(x_e x_o:e\in\{0,2,4\},\ o\in\{1,3,5\}\bigr).
}
\]

The map sends an odd short variable to that variable on the (+) sheet and
zero on the (-) sheet, and sends an even short variable in the opposite
way.  Every polynomial modulo the displayed monomial ideal has the unique
normal form

\[
a(y)+p_+(y;x_1,x_3,x_5)+p_-(y;x_0,x_2,x_4),
\]

where both (p_\pm) have zero short-variable constant term.  This proves both
injectivity and surjectivity onto the fiber product.  The certificate audits
the exhaustive (2^6) monomial-support types: 15 survive (one constant,
seven nonempty odd supports, and seven nonempty even supports), while all 49
mixed supports vanish.  Exponent sizes do not affect this classification.

## Normalization and conductor square

Let

\[
\widetilde B=B_+\oplus B_-.
\]

The two minimal-prime quotients of (B) are (B_+) and (B_-).  Both are
normal domains because they are polynomial rings over the UFD (R).  The
element

\[
e_+=(1,0)\in\widetilde B
\]

is integral over (B), satisfying (e_+^2-e_+=0), and

\[
\widetilde B=B[e_+].
\]

It follows that (widetilde B) is finite over (B) and is the integral
closure of (B) in its total quotient ring.  Hence

\[
\nu:\widetilde F=\operatorname{Spec}\widetilde B
=\operatorname{Spec}B_+\sqcup\operatorname{Spec}B_-
\longrightarrow F=\operatorname{Spec}B
\]

is the normalization.

Write

\[
J_+=(x_1,x_3,x_5),
\qquad
J_-=(x_0,x_2,x_4).
\]

The conductor in (widetilde B) is exactly

\[
\mathfrak c=J_+\oplus J_-.
\]

Indeed, multiplication by the two normalization idempotents forces both
zero-section values of a conductor element to vanish; conversely, a pair
with both values zero remains in (B) after multiplication by every element
of (widetilde B).  Therefore

\[
B/\mathfrak c\simeq C,
\qquad
\widetilde B/\mathfrak c\simeq C\oplus C.
\]

The precise conductor square has a doubled upper conductor:

\[
\begin{matrix}
\widetilde Z=\operatorname{Spec}(C\oplus C)
&\longrightarrow&\widetilde F\\
\downarrow&&\downarrow\nu\\
Z=\operatorname{Spec}C&\longrightarrow&F.
\end{matrix}
\]

It is Cartesian.  The normalization is finite, hence proper, and is an
isomorphism away from (Z).  Thus this is a normalization-conductor abstract
blow-up square, and hence a cdh distinguished square.  Referring only to
(Z=\operatorname{Spec}C) without its two-sheeted inverse image
(\widetilde Z) would not specify the square correctly.

The additive Mayer--Vietoris sequence is

\[
\boxed{
0\longrightarrow B
\longrightarrow B_+\oplus B_-
\xrightarrow{\ \varepsilon_+-\varepsilon_-\ }
C\longrightarrow0.
}
\]

Exactness follows directly from the fiber-product definition; surjectivity
uses ((a,0)\mapsto a).  Componentwise, every nonconstant monomial belongs to
one branch, while on constants the sequence is

\[
0\longrightarrow R\xrightarrow{(1,1)}R^2
\xrightarrow{(1,-1)}R\longrightarrow0.
\]

No averaging or inversion of (2) is involved.

## Canonical polarity-odd first normal symbol

For a glued section (f=(f_+,f_-)\in B), let

\[
a=\varepsilon_+(f_+)=\varepsilon_-(f_-).
\]

The conductor square canonically supplies the first branchwise normal map

\[
\operatorname{gr}_{\mathfrak c}^1(f)
=
\left(
[f_+-a]_{J_+/J_+^2},
-[f_--a]_{J_-/J_-^2}
\right).
\]

The minus sign is the orientation of the two-term Cech difference, or
equivalently the generator of the polarity sign line.  This map is intrinsic
to the augmented fiber product: it uses no extension of either branch
function into the missing normal directions.

For the entry-66 glued residues

\[
A_3^+=A_0+y_2x_1+y_1x_3+y_0x_5,
\qquad
A_3^-=A_0+y_1x_0+y_0x_2+y_2x_4,
\]

where

\[
A_0=-(y_0y_1+y_0y_2+y_1y_2),
\]

the map gives

\[
\boxed{
\sigma_{\rm alt}
=y_2\,dx_1+y_1\,dx_3+y_0\,dx_5
-y_1\,dx_0-y_0\,dx_2-y_2\,dx_4.
}
\]

In the ordered short-variable basis ((dx_0,\ldots,dx_5)), its coefficient
supports and signs are

\[
(-y_1,\ +y_2,\ -y_0,\ +y_1,\ -y_2,\ +y_0),
\]

exactly the six terms of entry 66.

## Cyclic transport and the polarity line

One-step rotation acts by

\[
x_j\longmapsto x_{j+1},
\qquad
y_i\longmapsto y_{i+1},
\]

with indices modulo (6) and (3), respectively.  It exchanges the two
normalization sheets and sends

\[
\tau(\sigma_{\rm alt})=-\sigma_{\rm alt}.
\]

The raw conormal symbol is therefore anti-equivariant and cannot be a
nonzero invariant integral section.  Let (L_{\rm pol}) be the polarity line
on which the sheet exchange acts by (-1).  Then

\[
\boxed{
\sigma_{\rm alt}\otimes e_{\rm pol}
\quad\text{is equivariant in}\quad
N^\vee_{Z/\widetilde F}\otimes L_{\rm pol}.
}
\]

Thus the polarity twist is forced, not a later character fit.

## What this proves and what it does not

This theorem canonically types the entry-66 operation as a sheet-resolved
associated-grade/Cech symbol on a normalization-conductor cdh square.  In
particular, it proves that the six supports, their signs, and the polarity
character come from scalar branch geometry before any Ward or road pairing.

It does **not** follow that the symbol is a morphism of scalar
kinetic/BRST complexes.  For such a lift, the actual differential must at
least:

1. preserve the two branch restrictions and the conductor filtration, so
   that the first associated grade is defined;
2. commute with the normalization/Cech descent maps;
3. induce on the associated grade a target differential compatible with the
   Ward complex;
4. satisfy the physical Cut and internal-state coevaluation identities.

Even under these necessary typing conditions, the chain identity

\[
d_{\rm Ward}\boldsymbol\sigma_{\rm alt}
=\boldsymbol\sigma_{\rm alt}d_{\rm scalar}
\]

must still be checked.  The conductor theorem supplies neither the unknown
scalar differential nor this identity.  It therefore closes the algebraic
typing gap behind entry 66, but not the chain-level or factorization gap of
entries 89--92.

## Consequence for the current formula objective

The first stage of entry 92's viable two-step construction now has a
canonical associated symbol:

\[
\text{contact relative complex}
\xrightarrow{\ G_D^{\rm Cousin}\ }
\mathcal R_D^{\rm circ,PC}
\xrightarrow{\ \mathbb D\Delta_D^{\rm circ}\ }
\mathsf J_D^{\rm road,PC}.
\]

At the alternating fusion conductor,

\[
\operatorname{gr}^1(G_D^{\rm Cousin})
\stackrel{?}{=}\sigma_{\rm alt}\otimes L_{\rm pol}.
\]

The equality is now a well-typed chain-lift objective.  It remains
conditional on a scalar kinetic/BRST complex that preserves the
branch/conductor filtration and obeys cdh/Cech descent.

## Exact certificate

Run:

```text
rustfmt --edition 2021 --check research/voevodsky/check_alternating_conductor_square.rs
rustc --edition=2021 -D warnings -O research/voevodsky/check_alternating_conductor_square.rs -o "$env:TEMP\\marici-alternating-conductor-square.exe"
& "$env:TEMP\\marici-alternating-conductor-square.exe"
```

The certificate verifies the exhaustive monomial-support presentation, the
universal constant-component exact sequence, all six coefficient supports
and signs, and the raw/twisted rotation characters.

Certificate SHA-256:

```text
9cc13a160afe2e6d8895274a33ef43c45ccc40f51eaa6fab78209aee897ad6dd
```

## Internal dependencies

- Entry 66: alternating-conductor symbol and Ward lift.
- Entry 89: boundary-costalk pairing and local polarity character.
- Entry 90: Cut-only descent falsifier and contact recollement objective.
- Entry 91: global relative contact carrier.
- Entry 92: vanishing of ordinary star restriction and loaded Cousin/Gysin
  objective.
- `research/voevodsky/check_alternating_conductor_square.rs`.
