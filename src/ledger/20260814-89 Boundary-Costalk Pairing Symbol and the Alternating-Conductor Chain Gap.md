# Boundary-Costalk Pairing Symbol and the Alternating-Conductor Chain Gap

## Record

Date: 2026-08-14

Status: exact (D=(0,3)) associated-grade pairing theorem and first-chain-datum
obstruction.  The three occurrence-resolved road squares admit a canonical
Laurent-dual pairing with entry 59's oriented circuit-tag resolution after the
character twist

\[
\chi_N
=
\operatorname{sgn}_{\rm polarity}\otimes\operatorname{or}(C_3),
\qquad
\chi_N(\text{rotation},\text{reflection},\text{core exchange})
=(+1,-1,-1).
\]

The character is not a new normal line.  On the actual two-interval road
faces, the Borel--Moore/tangential orientation system is gauge-isomorphic to
this tensor product.  Entry 66 supplies its polarity-odd conductor factor and
entries 59/64 supply the oriented road-triangle factor.  Laurent twist reversal
commutes with relabeling, and entry 86's ordered normal line transports
positively.

This proves the pairing only on the factorization boundary costalk and only at
the scalar/Laurent associated grade.  The first unsupported chain datum is
entry 66's proposed

\[
\boldsymbol\sigma_{\rm alt},
\]

which would lift the alternating conductor symbol through the scalar
kinetic/BRST differential.  Without it, the occurrence-resolved circuit PC
complex and the target half of the Cousin chain-pairing identity are not
defined.  A full quotient of
(operatorname{PC}(\mathsf J_4\boxtimes\mathsf J_6)) has an additional
contact-kernel problem and is not implied by the boundary-costalk theorem.

## The actual road source complexes

For a six-point physical channel (D_i), the boundary product has two
quadrilateral factors.  Write their scalar variables as

\[
(X_{L0},X_{L1}),\qquad (X_{R0},X_{R1}).
\]

The occurrence-resolved source is the tensor of the two weighted intervals

\[
I_L\otimes I_R,
\]

where

\[
d h_L=X_{L0}e_{L0}-X_{L1}e_{L1},
\qquad
d h_R=X_{R0}e_{R0}-X_{R1}e_{R1}.
\]

The certificate reconstructs the two quadrilateral cells and all four scalar
slots directly from each of

\[
D_0=(0,3),\qquad D_1=(1,4),\qquad D_2=(2,5).
\]

It builds the complete tensor differential, including

\[
d(h_L\otimes h_R)
=dh_L\otimes h_R-h_L\otimes dh_R,
\]

and proves (d^2=0) on all three top cells.

For the occurrence vertex (e_{i,v}), (v=(v_L,v_R)), put

\[
w_{i,v}=X_{L,v_L}X_{R,v_R},
\qquad
\lambda_i(e_{i,v})=w_{i,v}^{-1}.
\]

Then (lambda_i) kills each weighted interval boundary.  The checker verifies
all twelve such equations and all twelve primitive normalizations

\[
\boxed{\lambda_i(w_{i,v}e_{i,v})=1.}
\]

This is integral over the Laurent ring; it uses no averaging, section, or
division by the number of occurrences.

## Exact character provenance

Act on the hexagon by

\[
j\longmapsto
\begin{cases}
j+a,&\text{rotation},\\
-j+a,&\text{reflection},
\end{cases}
\qquad a\in\mathbb Z/6.
\]

The parity of (a) records polarity/core exchange, and reflection reverses
the oriented road triangle.  For every group element and every road, the
certificate transforms:

1. both quadrilateral factors;
2. both ordered interval endpoint lists;
3. the Koszul sign from exchanging the two one-dimensional factors.

With the lexicographic road-face orientations, the signs form a line-system
cocycle.  Exactly two road gauges, differing by simultaneous global reversal,
identify it with

\[
\operatorname{sgn}_{\rm polarity}\otimes\operatorname{or}(C_3).
\]

After either gauge, its character is

\[
(+1,-1,-1).
\]

This is precisely (chi_N).  It explains the six mismatches in entry 88's
normal-line-only test: the missing sign was tangential/conductor orientation,
not an unrecorded sign of ([dX_D]).

Laurent inversion is strictly natural:

\[
g(w^{-1})=(gw)^{-1}.
\]

The certificate checks this and the tag/road index shift on all

\[
12\times3\times4=144
\]

group-road-occurrence combinations.

## The associated-grade pairing

Let (c_i) be entry 59's three oriented circuit tags, indexed as oriented
edges of the road triangle.  The carrier pairing is

\[
q_i\longleftrightarrow c_{i-2}^\vee.
\]

On occurrences define

\[
\boxed{
\Phi_{03}^{\rm gr}(e_{i,v})
=
w_{i,v}^{-1}
c_{i-2}^\vee\otimes e_{\chi_N}.
}
\]

The tag dual and (e_{\chi_N}) each acquire the sign (chi_N), so their
product is untwisted.  Together with Laurent naturality, this proves exact
equivariance of (Phi_{03}^{\rm gr}) on every occurrence.

The carrier differentials also match.  Entry 59 has

\[
\Delta^{\rm circ}(1)=c_0+c_1+c_2,
\]

while the road augmentation is

\[
\varepsilon(q_i)=1.
\]

Thus

\[
\Delta_{\rm circ}^\vee\Phi_{03}^{\rm gr}
=
\Phi_1^{\rm gr}\varepsilon
\]

road by road, with value vector ((1,1,1)).

This statement must not be confused with the primitive quotient.  The
two-term twisted dual circuit resolution

\[
[P\xrightarrow{\varepsilon}\mathbf1]
\]

has (A_2) as its nonzero homology, up to convention/shift.  The primitive
line is instead

\[
\operatorname{cofib}(A_2\longrightarrow P)\simeq\mathbf1.
\]

Accordingly, (Phi^{\rm gr}) pairs the road-difference resolution with the
dual circuit resolution.  It does not by itself construct a primitive-line
counit.

## Endpoint Cousin identity and integral normalization

Entry 86's marked endpoint path has coefficient (+1) at its terminal
Cousin face.  The scalar source coefficient and entry-coaction coefficient
are both (-1).  Hence every marked term has total sign

\[
(+1)(-1)(-1)=+1.
\]

There are two primitive source occurrences per sink mark, so each of the
twelve marked entries has value (2).  The two sink marks on a fixed polarity
road give

\[
(4,4,4)
\]

over the three roads.  This is exactly the polarized element

\[
c_L\boxtimes c_R
=(2g_L)\boxtimes(2g_R)
=4(g_L\boxtimes g_R).
\]

It is not a primitive generator which must be forced to value (1).  The
primitive occurrences already have value (1), while the polarized sum must
and does retain value (4).  No division by four occurs.

The road half of the chain-pairing identity is therefore exact:

\[
\lambda_i d_{\rm road}=0,
\]

including all endpoint Cousin signs.  The other half would require

\[
d_{\rm circ}^{\rm PC}
\]

and the image of the circuit relation generator.  Those data are not present.

## Minimal circuit PC complex and the first unsupported map

The smallest possible circuit lift would have three generators

\[
\mathcal T_i^{\rm PC}
\]

lifting the individually supported populated Ward circuits, one relation
generator

\[
\mathcal K_{\rm rel}^{\rm PC},
\]

and a differential whose carrier grade is

\[
d\mathcal K_{\rm rel}^{\rm PC}
=
\mathcal T_0^{\rm PC}
+\mathcal T_1^{\rm PC}
+\mathcal T_2^{\rm PC}.
\]

It must additionally contain the scalar first-jet coefficients, internal Ward
or BRST differential, PC lower-face terms, and the orientation line
(chi_N).  Entries 59/64 construct only its carrier grade.  Entry 66 derives
the coefficient symbol

\[
\sigma_{\rm alt}:
(\mathbb J_{\mathfrak f_+}\mathcal S,
 \mathbb J_{\mathfrak f_-}\mathcal S)
\longrightarrow
N_{Z/\widetilde F}^\vee\otimes\operatorname{sgn}_{\rm polarity}
\]

and proves that its six columns are Ward closed.  It explicitly does not
construct the chain map

\[
\boxed{
\boldsymbol\sigma_{\rm alt}:
\operatorname{Tot}\check C
(\{F_+,F_-\};\mathbb J_{\mathfrak f}\mathcal S)
\longrightarrow
\mathcal W_{\rm Ward}.
}
\]

The new certificate makes the logical gap finite.  It retains entry 66's
exact (7\times6) Ward symbol and target Ward differential.  The symbol is
closed.  On the same six source generators:

1. the zero square-zero source differential makes it a chain map;
2. the square-zero differential (e_1\mapsto e_0\) does not.

Both witnesses have the same modules and associated symbol.  Thus coefficient
closure cannot decide the chain-map identity without the actual scalar
kinetic/BRST differential and its map.  The first unsupported datum is exactly
(oldsymbol\sigma_{\rm alt}), not another normal-line sign.

## Boundary costalk is not the full half-object

The three road squares are the factorization boundary costalk of the lower
(mathsf J_6) object.  They do not exhaust

\[
\operatorname{PC}(\mathsf J_4\boxtimes\mathsf J_6).
\]

At the carrier level, the two polarity tripods restrict by

\[
\operatorname{Res}_{\partial}=[I_3\ I_3]:
P_+\oplus P_-\longrightarrow P_{\rm roads}.
\]

Therefore

\[
q_i^+-q_i^-\in\ker\operatorname{Res}_{\partial}.
\]

Entry 86 proves equality of the two polarized residues, and entry 87 retains
the nontrivial marked polarity homotopy (H_6^{\rm mark}).  These are the
physical occurrence-resolved warning that road restriction has a
central/contact kernel.

The certificate adjoins one abstract contact generator (z) with zero road
restriction.  Two functionals agree on every road generator and take values
(0) and (1) on (z).  Hence road data alone cannot choose a full-object
extension.  Declaring the counit to factor through boundary restriction would
kill the contact kernel, but that is an additional axiom.  Alternatively one
must derive its value from the alternating conductor/(H_6^{\rm mark}) sector
or prove an Adler/hidden-zero localization which removes it.

Thus the exact typing is

\[
\boxed{
\Phi_{03}^{\rm gr,\partial}
\text{ exists on the boundary costalk};
\qquad
\Phi_{03}^{\rm PC,full}
\text{ is not typed}.
}
\]

## Exact certificate

Run:

```text
rustfmt --check research/nima/check_primitive_pc_pairing_symbol.rs
rustc --edition=2021 -D warnings -O research/nima/check_primitive_pc_pairing_symbol.rs -o "$env:TEMP\\marici-primitive-pc-pairing-symbol.exe"
& "$env:TEMP\\marici-primitive-pc-pairing-symbol.exe"
```

The executable checks the three complete tensor weighted-interval complexes,
three (d^2=0) identities, twelve primitive cocycle equations, twelve
primitive unit values, 144 Laurent/equivariance identities, the complete
tangential orientation gauge and character, all twelve marked endpoint values,
the ((4,4,4)) polarization, the carrier differential square, Ward closure of
all six conductor-symbol columns, the two square-zero source-differential
witnesses, and the boundary/contact-kernel ambiguity.

Certificate SHA-256:

```text
78ccb47be5c20a6134f461b59e1aa2349740110162669b1f4a2fd28f280e4226
```

## Decision

Promote:

> The (D=03) factorization boundary costalk has an exact
> occurrence-resolved Laurent pairing with the twisted dual circuit carrier.
> Its character is the tangential/conductor line
> (operatorname{sgn}_{\rm polarity}\otimes\operatorname{or}(C_3)), and its
> primitive normalization is integral occurrence by occurrence.  The value
> four is the polarized sum of four unit primitive occurrences.

Retain as the immediate frontier:

> Construct (oldsymbol\sigma_{\rm alt}) with the actual scalar kinetic/BRST
> and endpoint Cousin differentials.  Use it to define the three circuit PC
> generators and their relation generator.  Only then test the full pairing;
> separately, type the (H_6^{\rm mark})/contact-kernel value or prove the
> precise localization through which the full (mathsf J_6) quotient factors.

## Internal dependencies

- Entry 38: facewise PC target, Borel--Moore/tangential chains, Cousin and
  normal differentials.
- Entry 59: oriented three-tag circuit resolution and relation character.
- Entry 64: suspension, road-triangle orientation, and carrier normalization.
- Entry 66: polarity-odd alternating conductor symbol and missing chain lift.
- Entry 77: primitive versus polarized weighted-interval normalization.
- Entries 86--87: marked endpoint counit, residue equality, and retained
  (H_6^{\rm mark}) contact homotopy.
- Entry 88: road coinvariant, local-system underdetermination, and the initial
  adjoint audit.
- `research/nima/check_primitive_pc_pairing_symbol.rs`.
