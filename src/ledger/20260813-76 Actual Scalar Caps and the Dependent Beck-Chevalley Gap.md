# Actual Scalar Caps and the Dependent Beck--Chevalley Gap

## Record

Date: 2026-08-13

Status: exact eight-point regional source-carrier and polynomial cellular-
resolution theorem.  The caps and cube are now intrinsic scalar faces.  The
remaining nontransverse step is a loaded derived Beck--Chevalley attachment
from the dependent route Čech object to their four-facet belt.

This entry forward-corrects the diagnosis in entries 73--75.  The surviving
belt class did not mean that the scalar source lacked caps or a cube.  Those
cells were already present in the exact-core associahedral face, but had not
been identified with the weighted route complex.  What is absent is the
correspondence attaching the disjoint pentagon/square route faces to that
regional face.

## The actual fixed-core source

Fix the representative rank-two physical core

\[
Q=\{03,05\}.
\]

It cuts the octagon into the three quadrilaterals

\[
(0123),\qquad(0345),\qquad(0567).
\]

Their two scalar refinements are

\[
(02,13),\qquad(04,35),\qquad(06,57).
\]

Consequently the exact-core associahedral face is the actual scalar face

\[
\boxed{
K_Q
=
K_4\times K_4\times K_4
\simeq I^3.
}
\]

Its cell census is

\[
(C_0,C_1,C_2,C_3)=(8,12,6,1).
\]

The four physical route supports are the side facets

\[
P_+:x_2=1,\qquad
P_-:x_0=1,\qquad
S_+:x_2=0,\qquad
S_-:x_0=0.
\]

The two complementary facets are not formal target copies.  They are the
literal scalar associahedral faces

\[
K_Q^- = Q\cup\{04\},
\qquad
K_Q^+ = Q\cup\{35\},
\]

and \(K_Q\) itself is the unique scalar three-face containing both.  An
exhaustive census of all 132 octagon triangulations verifies these
identifications and their uniqueness.

## The weighted cube is a scalar cellular resolution

Let

\[
A=\mathbf Z[X_{00},X_{01},X_{10},X_{11},X_{20},X_{21}].
\]

For a cube vertex \(v=(v_0,v_1,v_2)\in\{0,1\}^3\), define its opposite
monomial

\[
m_v
=
\prod_{r=0}^{2}X_{r,1-v_r}.
\]

For a cube face \(F\), let

\[
m_F
=
\operatorname{lcm}\{m_v\mid v\in\operatorname{Vert}(F)\}.
\]

The multigraded cellular differential

\[
\boxed{
d[F]
=
\sum_{F'\prec F}
\epsilon(F,F')
\frac{m_F}{m_{F'}}[F']
}
\]

is exactly the three-factor weighted interval differential of entries
74--75:

\[
d h_r
=
X_{r1}e_{r1}-X_{r0}e_{r0}.
\]

Thus

\[
K_Q^{\mathrm w}
=
\bigotimes_{r=0}^{2}K_r^{\mathrm w}
\]

is not merely a convenient target complex.  It is the minimal cellular
resolution supported on the actual scalar face \(K_Q\) of the occurrence
ideal

\[
I_Q
=
\prod_{r=0}^{2}(X_{r0},X_{r1}).
\]

If

\[
w_v=\prod_rX_{r,v_r},
\]

then

\[
w_vm_v
=
\prod_{r=0}^{2}X_{r0}X_{r1}.
\]

The opposite labeling is therefore the cubical complement to the raw
occurrence weight.  It is forced already in one interval by the syzygy

\[
-X_{r0}a+X_{r1}b=0,
\]

whose primitive polynomial solution is

\[
(a,b)=(X_{r1},X_{r0}).
\]

This complement relation is intrinsic to the local scalar resolution.  It is
not yet an identification with the global inverse scalar intersection
pairing.

## Regional Pochhammer/Cousin telescoping

Let \(\mathbb P(F)\) denote the undecorated face-tube symbol supplied by the
facewise Pochhammer/Cousin construction of entry 38.  On the regional scalar
cube define

\[
\boxed{
\chi_Q([F])=m_F\,\mathbb P(F).
}
\]

For every incidence \(F'\prec F\),

\[
\frac{m_F}{m_{F'}}m_{F'}=m_F.
\]

Hence the weighted cellular boundary and the ordinary face-tube boundary
commute term by term:

\[
\chi_Qd=d_{\rm PC}\chi_Q.
\]

This is an exact polynomial associated-grade statement on every cell of the
actual regional cube, conditional only on the undecorated facewise tube map
already isolated in entry 38.  It does not by itself construct the loaded
map on the dependent route pentagons.

## The integral cap and cube extension

Let \(B_Q\) be the union of the four physical side facets.  Topologically,

\[
B_Q\simeq S^1\times I.
\]

The exact integral sequence is now realized by scalar faces:

\[
\begin{array}{c|c}
\text{carrier}&(H_0,H_1,H_2,H_3)\\ \hline
B_Q&(\mathbf Z,\mathbf Z,0,0)\\
B_Q+K_Q^-&(\mathbf Z,0,0,0)\\
B_Q+K_Q^-+K_Q^+&(\mathbf Z,0,\mathbf Z,0)\\
K_Q&(\mathbf Z,0,0,0).
\end{array}
\]

The boundary of the first cap is primitive: adjoining it raises the saturated
two-boundary rank by one and kills the belt generator integrally.  The second
cap completes the sphere, and the unique scalar cube fills it.

With all facet orientations induced from \(I^3\), the weighted equations
force the two relative cap coefficients to be

\[
(1,1)
\]

and the cube coefficient to be

\[
1.
\]

All equations hold over \(A\).  Neither Laurent localization nor division by
two is required.  The two orders of physical normal contraction satisfy the
expected Koszul relation

\[
\iota_E\iota_D(D\wedge E)=+1,
\qquad
\iota_D\iota_E(D\wedge E)=-1,
\]

and the complete statement rotates through the eight-element deck orbit.

Therefore the vertical fixed-\(Q\) cap/cube obstruction is zero.

## Why the route faces do not supply the attachment

The representative dependent route faces are

\[
P=\{13,35,57\},
\qquad
S=\{02,04,06\}.
\]

The first is a pentagon and the second a square.  Their scalar vertex sets are
disjoint, their union is crossing, and no associahedral three-face contains
both.  Moreover,

\[
P\cap K_Q=\{(1,1,1)\},
\qquad
S\cap K_Q=\{(0,0,0)\}
\]

at the level of triangulation vertices.  In contrast, their physical
double-Gysin images occupy four entire side facets of \(K_Q\).

It follows that

\[
\boxed{
\text{route-to-belt attachment}
\neq
\text{ordinary scalar face restriction}.
}
\]

The nonzero \(P/S\) cross-chart overlaps found in entries 72--75 live inside
the coefficient fiber \(\mathcal L_Q\); they are not geometric intersections
of scalar faces.

The scalar-edge mapping-cone term

\[
H_s
=
\frac{X_{15}}{u_{15}}\ell_{15}
-
\frac{X_{37}}{u_{37}}\ell_{37}
\]

also cannot be the missing attachment.  Supported double Gysin kills both
endpoint quotient lines, and its labels \(15,37\) are distinct from the
regional cap flip \(04,35\).

This separates two operations that had been conflated:

1. the scalar-edge Cousin counit removes the rank-six endpoint excess;
2. the dependent Beck--Chevalley map attaches route descent to the regional
   belt.

The first is known formally.  The second is the remaining theorem.

## Corrected categorical target

Let \(\mathcal C_Q^{\rm route}\) denote the occurrence-decorated Čech/Cousin
totalization of the four marked route charts \(P_\pm,S_\pm\), including their
extension-by-zero coefficient intersections, and let

\[
B_Q^{\mathrm w}\subset K_Q^{\mathrm w}
\]

be the four-facet weighted belt.

The next object is a degree-two derived attachment

\[
\boxed{
\beta_Q^{\alpha'}
\in
\operatorname{RHom}\!\left(
\mathcal C_Q^{\rm route},
B_Q^{\mathrm w}[-2]
\right).
}
\]

It must be a loaded Beck--Chevalley comparison in the sense that the square

\[
\begin{array}{ccc}
\mathcal C_Q^{\rm route}
&\xrightarrow{\ \beta_Q^{\alpha'}\ }&
B_Q^{\mathrm w}[-2]\\
\big\downarrow{\chi_{\rm route}}
&&
\big\downarrow{\chi_Q}\\
\operatorname{PC}_{\alpha'}(\mathcal R_Q;\mathcal L)
&\xrightarrow{\ G_{D,E}^{\rm PC}\ }&
\operatorname{PC}_{\alpha'}(B_Q;I_Q)[-2]
\end{array}
\]

commutes in the derived category.  The notation records the required typing;
it does not assert that the presently incomplete loaded route map
\(\chi_{\rm route}\) already exists globally.

The attachment must satisfy:

1. its relative fundamental class is the normalized positive route class of
   entries 74--75;
2. its vertex restrictions are the established four-term occurrence anchors;
3. it sends the scalar-edge cone \(H_s\) to zero;
4. it sends coefficient Čech overlaps to the corresponding belt overlaps;
5. ordered \(D,E\) residues differ by the Koszul sign;
6. it is equivariant under deck rotation.

Once this belt attachment exists, no further cap choice is needed.  The
actual scalar faces \(K_Q^-,K_Q^+\) and \(K_Q\), together with \(\chi_Q\),
extend it with the uniquely normalized coefficients \(1,1,1\).

## Consequence for the QTDS polarization

Entry 75 showed, after Laurent localization, that

\[
[X_{r0}e_{r0}+X_{r1}e_{r1}]
=
2[X_{r0}e_{r0}]
=
2[X_{r1}e_{r1}].
\]

The present theorem strengthens the provenance of this relation: the
weighted interval is the minimal resolution on an actual scalar
quadrilateral face.  The factor two is therefore a genuine endpoint
polarization inside scalar boundary geometry, rather than a copied target
normalization.

This still does not prove that the local complement map is the restriction of
the global inverse scalar pairing, nor does it prove the horizontal Jordan
identity.  Those are separate comparisons.

## Epistemic boundary

Established:

1. the exact-core source is the actual scalar cube \(K_4^3\);
2. its two caps are \(Q+04\) and \(Q+35\), and its cube is unique;
3. opposite monomials make it the minimal polynomial cellular resolution of
   \(I_Q\);
4. the regional weighted face map telescopes with the undecorated PC
   boundary;
5. the first cap kills the primitive belt class integrally;
6. the second cap and cube close the sphere with unique coefficient \(+1\);
7. all statements respect ordered residues and the eight-step deck action;
8. the dependent \(P/S\) route faces are not subfaces of a common scalar
   carrier.

Open:

1. the occurrence-decorated derived Beck--Chevalley attachment
   \(\beta_Q^{\alpha'}\);
2. its finite-
   \(\alpha'\) realization as one loaded Pochhammer/Cousin natural
   transformation;
3. identification of the opposite-monomial complement with the restriction
   of \(I_{\rm scalar}^{-1}\);
4. horizontal assembly around the quadrangulation compatibility complex and
   comparison with the Jordan defect.

Reject:

> The surviving \(H^1\) of the bare belt proves that the scalar geometry has
> no source caps or cube.

Also reject:

> The route pentagon, its companion square, and the regional cube form an
> ordinary common-face diagram in the associahedron.

## Next executable theorem

Construct the complete Hom complex for

\[
\operatorname{RHom}
(\mathcal C_Q^{\rm route},B_Q^{\mathrm w}[-2])
\]

using the actual extension-by-zero route coefficient systems and the actual
regional lcm resolution.  Impose the known vertex anchors, \(H_s\mapsto0\),
ordered residues, and deck covariance.  Compute:

1. whether the constrained degree-zero cycle exists over the polynomial
   ring;
2. whether its obstruction class vanishes before Laurent localization;
3. whether the normalized solution is unique up to homotopy;
4. whether composing it with the regional \(\chi_Q\) gives the five-term
   loaded Cousin identity on one route pentagon.

This is the smallest exact test that can close or falsify the first dependent
factorization coherence of the scalar half-object before pairing.

## Reproducible certificate

Run:

    rustfmt --check research/nima/check_decorated_source_cap.rs
    rustc --edition=2021 -D warnings -O research/nima/check_decorated_source_cap.rs -o "$env:TEMP\\marici-decorated-source-cap.exe"
    & "$env:TEMP\\marici-decorated-source-cap.exe"

Certificate SHA-256:

    81828d55d754cb25acac89ef42abf02e709e2f3e67c1ede16a0e0fe714998556

## Decision

Promote:

> The fixed-core weighted route cube, its two caps, and its 3-cell are
> intrinsic scalar associahedral carriers.  Opposite monomial labels turn
> that actual cube into the minimal polynomial resolution of the occurrence
> ideal, and the cap/cube extension closes integrally.

Retain as the immediate frontier:

> Construct the loaded derived Beck--Chevalley attachment from the dependent
> route Čech object to the four-facet boundary of this regional resolution.

## Internal dependencies

- Entry 27: fixed-core regional marked-Catalan identification.
- Entry 38: undecorated facewise Pochhammer/Cousin map.
- Entries 72--73: constructible route descent and four-facet belt.
- Entries 74--75: normalized derived route class and weighted Hom theorem.
- research/nima/check_decorated_source_cap.rs.
