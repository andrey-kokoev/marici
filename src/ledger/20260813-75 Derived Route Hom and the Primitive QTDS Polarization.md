# Derived Route Hom and the Primitive QTDS Polarization

## Record

Date: 2026-08-13

Status: exact local derived-Hom and coefficient-module theorem, conditional on
the four-facet belt being the occurrence/Čech descent of the complete route
envelope.  Forward correction (entry 76): the actual scalar source caps and
cube exist and close the belt integrally.  What remains open is the loaded
derived Beck--Chevalley attachment from the disjoint route faces to that belt.

Forward correction (entry 82): the attachment remains open only as a
comparison with an independently loaded route-first presentation.  It is not
needed to define the target-first normal symbol, because scalar support
descent precedes the single facewise PC loading.

Entry 74 identified a canonical oriented relative/Borel--Moore map class but
left two questions unresolved:

1. does the loaded mapping complex have hidden negative-degree ambiguity or
   integral torsion;
2. what does the sum of the two scalar refinements in each quadrilateral mean
   intrinsically at the half-object level?

Both questions now have exact answers.  The normalized degree-zero route
class is unique and torsion-free.  A single degree-one belt class survives in
the bare route-to-belt Hom.  Entry 76 shows that actual scalar caps kill it;
the class therefore pinpoints a missing route attachment, not missing scalar
cells.  The two scalar
refinements in one quadrilateral become equal weighted classes after
localization, so their QTDS sum is twice one primitive Laurent class.

## One weighted interval over the polynomial ring

For one quadrilateral region write

\[
A_r=\mathbf Z[X_{r0},X_{r1}]
\]

and consider

\[
K_r^{\mathrm w}
=
\left[
A_rh_r
\xrightarrow{d}
A_re_{r0}\oplus A_re_{r1}
\right],
\qquad
dh_r=X_{r1}e_{r1}-X_{r0}e_{r0}.
\]

There is an exact sequence

\[
0
\longrightarrow A_rh_r
\xrightarrow{(-X_{r0},X_{r1})}
A_re_{r0}\oplus A_re_{r1}
\xrightarrow{\phi_r}
(X_{r0},X_{r1})
\longrightarrow0,
\]

where

\[
\phi_r(e_{r0})=X_{r1},
\qquad
\phi_r(e_{r1})=X_{r0}.
\]

Consequently

\[
H_0(K_r^{\mathrm w})\simeq(X_{r0},X_{r1}),
\qquad
H_i(K_r^{\mathrm w})=0\quad(i>0).
\]

The polynomial answer is torsion-free and generically rank one, but it is not
a free rank-one module at the joint coordinate zero.  This rank jump is real
boundary information and must not be erased in the statement of the global
theorem.

After Laurent localization

\[
R_r=A_r[X_{r0}^{-1},X_{r1}^{-1}],
\]

the ideal becomes the unit ideal and

\[
H_0(K_r^{\mathrm w}\otimes R_r)\simeq R_r.
\]

In this localized module define

\[
g_r
=
[X_{r0}e_{r0}]
=
[X_{r1}e_{r1}].
\]

This is a Laurent generator.  Polynomially its image is the common monomial
\(X_{r0}X_{r1}\) inside the nonprincipal ideal, not a global free generator.

## The three-region weighted cube

For the eight-point rank-two core \(Q\), the three pairs of variables are
disjoint.  Tensoring the preceding resolutions gives

\[
K_Q^{\mathrm w}
=
\bigotimes_{r=0}^{2}K_r^{\mathrm w},
\]

and

\[
H_0(K_Q^{\mathrm w})
\simeq
I_Q
:=
\prod_{r=0}^{2}(X_{r0},X_{r1}),
\qquad
H_i(K_Q^{\mathrm w})=0\quad(i>0).
\]

Thus the polynomial target is again torsion-free and generically rank one,
but nonfree.  Over the fully Laurent ring \(R\),

\[
K_Q^{\mathrm w}\simeq R[0].
\]

The degree ranks of the free resolution remain

\[
(8,12,6,1).
\]

## Exact derived-Hom calculation

The four physical charts form the belt

\[
B=\partial I^2\times I\simeq S^1.
\]

Treating this belt as the source obtained after the occurrence/Čech descent
and relative Borel--Moore identification, the exact integral cellular Hom
complex into the ordinary cube has cochain dimensions

\[
(8,60,172,232,144,32)
\]

in degrees \(-3,-2,-1,0,1,2\), and differential ranks

\[
(8,52,120,111,32).
\]

Integral strong-deformation retracts, not only rational ranks, give

\[
H^{-1}=0,
\qquad
H^0=\mathbf Z,
\qquad
H^1=\mathbf Z,
\]

with no torsion.  Restoring the weighted coefficients gives

\[
H^{-1}\operatorname{RHom}(B,K_Q^{\mathrm w})=0,
\]

\[
H^0\operatorname{RHom}(B,K_Q^{\mathrm w})\simeq I_Q,
\qquad
H^1\operatorname{RHom}(B,K_Q^{\mathrm w})\simeq I_Q
\]

over the polynomial ring, and

\[
H^0\simeq R,
\qquad
H^1\simeq R
\]

after full Laurent localization.

The four chart-gluing equations have a saturated rank-one kernel.  The
ordered normal line fixes its sign, while the complete weighted vertex
restrictions fix its unit normalization.  Therefore the admissible
degree-zero carrier has one positive normalized class.  There is no hidden
negative-degree ambiguity and no division by two is required.

## What the surviving \(H^1\) means

The degree-one class is the circle of the belt.  It is not a second map class
and it is not evidence of nonzero physical curvature.  It identifies the
degree in which the absent source coherence must be supplied:

\[
B
\subset
B\cup K^-
\subset
B\cup K^-\cup K^+
\subset
I^3.
\]

At the level of undecorated cellular carriers:

- one cap kills the belt \(H^1\);
- two caps produce the boundary sphere and its \(H^2\);
- the cube kills that sphere class.

The weighted target caps and cube were forced in entry 74.  That does not
construct their occurrence-decorated source counterparts.  The remaining
question is whether the normalized belt class lies in the image of the
restriction map

\[
H^0\operatorname{RHom}
\bigl(C_*(B\cup K^-),K_Q^{\mathrm w}\bigr)
\longrightarrow
H^0\operatorname{RHom}
\bigl(C_*(B),K_Q^{\mathrm w}\bigr),
\]

and then whether the two extensions are coherently filled by a source cube.

This turns the vague request for a global comparison into one explicit
extension problem.

## The scalar-edge relation is internal to the source

For the representative core \(Q=\{03,05\}\), the route pentagon and companion
square have the exact labels

\[
P:
\quad
C=\{13,35,57\},
\quad
\partial P=(17,37,03,05,15),
\]

\[
S:
\quad
C=\{02,04,06\},
\quad
\partial S=(46,03,05,24).
\]

The exchanged endpoint labels \(15\) and \(37\) are not names of target-square
lines.  Polynomially their mapping-cone quotient is the torsion-free nonfree
ideal

\[
(X_{15},X_{37}),
\]

and it becomes a split free rank-one module only after endpoint Laurent
localization.  The Cousin relation is

\[
X_{15}\ell_{15}=X_{37}\ell_{37}.
\]

Both endpoint quotient lines are killed by the supported double-Gysin map.
Hence the handle \(H_s\) of entry 74 is a source null-homotopy whose target is
zero.  It does not identify either endpoint with a companion-square
occurrence.

This coefficient typing and the belt/cube equations close exactly under all
eight deck rotations.

## The primitive polarization class

Define the regional QTDS occurrence tensor

\[
c_r
=
X_{r0}e_{r0}+X_{r1}e_{r1}.
\]

In localized homology,

\[
\boxed{
[c_r]=2g_r.
}
\]

Therefore at eight points

\[
\boxed{
[c_0\otimes c_1\otimes c_2]
=
8\,g_0\otimes g_1\otimes g_2.
}
\]

The factor eight is an index or normalization effect.  The Hom cohomology is
torsion-free; no \(2\)-torsion has appeared.  If one retained only the fully
polarized tensor, its span would be the index-eight submodule of the Laurent
carrier.  The complete chart restrictions contain individual vertex anchors
and select the primitive normalized class instead.

This has a direct QTDS interpretation.  Entry 27 proves that for a retained
full quadrangulation the regional numerator factor is

\[
X_{d_r^0}+X_{d_r^1}.
\]

The weighted complex refines this to \(c_r\).  The two scalar resolutions are
not two unrelated interactions: after derived scalar-flip descent they are
the two endpoint representatives of one Laurent class, and the QTDS factor is
their polarization.

For an original four-point quadrilateral the physical boundary-side terms
vanish, so this same sum is

\[
X_{ac}+X_{bd}
=
-2K_A\mathbin\cdot K_C.
\]

Thus the familiar coefficient two in the quartic QTDS rule is visible as the
two-endpoint polarization of a primitive scalar-derived class.  At an
internal quartic vertex, the omitted physical-side terms live in adjacent
core strata and participate in propagator cancellation.  Consequently this
local result does not by itself prove the global Jordan identity or the full
core-incidence strictification.

More generally, for a full quadrangulation of a \(2m\)-gon with \(m-1\)
quadrilateral regions, the same localized calculation gives

\[
\left[
\bigotimes_{r=1}^{m-1}c_r
\right]
=
2^{m-1}
\bigotimes_{r=1}^{m-1}g_r.
\]

This is a structural interpretation of the already proved all-arity
occurrence formula, not an additional rescaling of the amplitude.

## Epistemic verdict

Promote:

1. the polynomial weighted cube resolves the occurrence ideal \(I_Q\);
2. after Laurent localization, the belt-to-cube derived Hom has
   \(H^{-1}=0\), one normalized \(H^0\) carrier, one belt \(H^1\), and no
   torsion;
3. the endpoint Cousin relation is an internal source mapping cone and maps
   to target zero;
4. the full eight-occurrence polarization is eight times the primitive
   Laurent class, not a torsion class;
5. the result and all coefficient labels are deck covariant.

Retain as conditional:

> The four-facet belt is the complete occurrence/Čech and relative
> Borel--Moore descent of the physical nontransverse route envelope.

Forward correction (entry 76):

> The occurrence-decorated source caps and cube are actual faces of the
> fixed-core scalar associahedron, and their weighted cellular resolution
> extends the belt integrally.  The remaining open map is the dependent
> route-to-belt Beck--Chevalley attachment.

Reject:

> The route ambiguity is caused by integral torsion or by several inequivalent
> degree-zero derived maps.

Also reject:

> The factor eight permits division by two, or directly proves the horizontal
> Jordan identity.

The weighted cube is vertical coherence inside one fixed quadrangulation.
The Jordan defect remains a horizontal comparison among different
quadrangulations and must be tested only after the dependent route-to-belt
attachment is constructed.

## Next executable theorem

Entry 76 completes the cap/cube experiment over the polynomial ring.  The
next theorem is to construct the constrained derived map from the dependent
pentagon/square Čech totalization to the four side facets of the actual
regional cube.  It must realize the normalized positive \(H^0\) class, send
the scalar-edge cone to zero, commute with ordered double residue and deck
rotation, and compose with the regional Pochhammer/Cousin map.  Only after
this Beck--Chevalley attachment closes should the eight horizontal route
kernels be compared with the Jordan defect.

## Reproducible certificate

Run:

    rustfmt --check research/nima/check_route_kernel_hom_complex.rs
    rustc --edition=2021 -D warnings -O research/nima/check_route_kernel_hom_complex.rs -o "$env:TEMP\\marici-route-hom.exe"
    & "$env:TEMP\\marici-route-hom.exe"

Certificate SHA-256:

    d30219fdb71c5f6df7350965ec9b91b8cac3e4c266080165f543809940e9ed04

## Decision

The eight-point local comparison now has the form

\[
\boxed{
\text{one normalized derived route class}
+
\text{one belt extension degree}
+
\text{a primitive scalar polarization}.}
\]

The immediate frontier is no longer uniqueness of the route map or existence
of scalar caps.  It is the dependent route-to-belt Beck--Chevalley
attachment.  Success would close the first genuinely nontransverse
factorization coherence of \(\mathsf J\) before pairing.

## Internal dependencies

- Entry 26: vertex-local QTDS numerator identity.
- Entry 27: all-arity regional occurrence factorization.
- Entry 38: finite-\(\alpha'\) undecorated Pochhammer/Cousin class.
- Entries 70--74: coefficient Gysin, nontransverse no-go, constructible
  descent, and weighted route cube.
- research/nima/check_route_kernel_hom_complex.rs.
