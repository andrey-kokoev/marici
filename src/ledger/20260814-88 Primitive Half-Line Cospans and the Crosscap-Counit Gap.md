# Primitive Half-Line Cospans and the Crosscap-Counit Gap

## Record

Date: 2026-08-14

Status: exact eight-point occurrence-carrier, additive cospan, integral Smith,
and local-system underdetermination theorem.  The twelve primitive regional
half-lines and all of their physical Gysin legs are explicit.  They do not
glue strictly in the occurrence-resolved cut complexes.  The shared channel
object has three road components, not one line.

There is a canonical carrier coinvariant quotient of those three roads.  As
an underlying lattice it is dual to entry 59's circuit-relation inclusion;
equivariantly, that duality requires the character

\[
\chi_N(\text{road rotation})=+1,\qquad
\chi_N(\text{road reflection})=-1,\qquad
\chi_N(\text{core exchange})=-1.
\]

The bounded (D=(0,3)) audit below proves that entry 86's recorded normal
transport does not itself supply this character.  No existing result promotes
the twisted lattice duality to an occurrence-resolved Pochhammer/Cousin chain
map on the full

\[
\mathsf J_4\boxtimes\mathsf J_6
\]

channel object.  Consequently the full coefficient class
\([\Theta_{O,\rm full}^{\rm PC}]\) is not yet typed.

Conditional on the unit primitive road quotient, the ordered-normal Gysin
signs select the nontrivial orientation local system on the candidate Möbius
hypercover carrier.
This is a conditional coefficient theorem, not an inference from bare
carrier topology.  The trivial and orientation systems are both
\(D_8\)-equivariant and both have positive holonomy around the residual
octagon, so an octagon product cannot distinguish them.  The decisive test is
the crosscap holonomy of the missing PC quotient.

## The twelve Alexander-complement chart generators

For every octagon quadrangulation \(Q=\{D,E\}\), the exact-core scalar fiber
is a three-cube.  Its three quadrilateral regions have scalar refinement
pairs

\[
(X_{r0},X_{r1}),\qquad r=0,1,2.
\]

For \(v\in\{0,1\}^3\), put

\[
w_v=\prod_rX_{r,v_r},
\qquad
m_v=\prod_rX_{r,1-v_r},
\qquad
M_Q=\prod_rX_{r0}X_{r1}.
\]

The certificate derives all six region variables from the actual
quadrilateral cells and checks

\[
w_vm_v=M_Q
\]

on every one of the \(12\cdot8=96\) exact-core triangulations.  The twelve
weighted interval relations in each cube identify

\[
w_ve_v=g_Q
\]

after Laurent localization.  Thus all eight occurrence representatives give
one primitive class, while their polarization is

\[
\sum_vw_ve_v=8g_Q.
\]

No division by eight enters the primitive normalization.

## The shared cut object is not a line

Fix a physical cut \(D\).  Precisely three quadrangulations contain it:

\[
Q_i=\{D,E_i\},\qquad i=0,1,2.
\]

The connected marked link is the genuine

\[
K_{2,3}=S^0*\{E_0,E_1,E_2\}.
\]

Write \(q_{D,E_i}\) for its three road vertices.  With the common normal
Pochhammer factor and ordered orientation line retained, the physical Gysin
leg has the established form

\[
\rho_{D,Q_i}(g_{Q_i})
=
\epsilon(D,E_i)\,q_{D,E_i}.
\]

Here \(\epsilon(D,E_i)\) is the contraction sign of the ordered two-normal
word.  For \([D\wedge E]\),

\[
\iota_D[D\wedge E]=[E],
\qquad
\iota_E[D\wedge E]=-[D],
\]

so the two ordered double residues anticommute exactly.

If \(Q_i\) and \(Q_j\) meet at \(D\), their normalized restrictions are the
distinct road vertices \(q_{D,E_i}\) and \(q_{D,E_j}\).  Hence

\[
\boxed{\text{strict chain-level gluing is false}.}
\]

There are two chain homotopies between them, one through each polarity
center.  Their difference is the primitive four-edge Ward circuit

\[
\Gamma_D(q_{D,E_i}-q_{D,E_j}).
\]

The checker verifies all 24 strict mismatches, all 48 center paths, all 24
Ward ambiguities, and the strict telescoping relation around each of the eight
road triangles.

## The road coinvariant and its dual circuit resolution

Let

\[
P_D=\mathbb Z\langle q_{D,E_0},q_{D,E_1},q_{D,E_2}\rangle
\cong\mathbb Z^3.
\]

At the carrier level there is a saturated exact sequence

\[
\boxed{
0\longrightarrow A_2
\longrightarrow P_D
\xrightarrow{\ \varepsilon_D\ }
\mathbf 1
\longrightarrow0,
}
\]

where

\[
A_2=\ker(x_0+x_1+x_2),
\qquad
\varepsilon_D(q_{D,E_i})=1.
\]

Thus the carrier \(H_0\) coinvariant is a canonical line quotient, and every
normalized chart leg becomes a unit after applying it.

Under the standard perfect pairing on the permutation module, this sequence
dualizes as an underlying lattice to

\[
\boxed{
0\longrightarrow\mathbf1
\xrightarrow{\ \Delta_D\ }
P_D^*
\longrightarrow A_2^*
\longrightarrow0.
}
\]

Entry 59's oriented circuit tags are not the untwisted road permutation
module.  If \(\chi_N\) is the character

\[
\chi_N(r)=+1,\qquad
\chi_N(s)=-1,\qquad
\chi_N(\sigma_{\rm core})=-1,
\]

for a road rotation \(r\), road reflection \(s\), and core exchange
\(\sigma_{\rm core}\), then, after the required cyclic index shift,

\[
\mathsf T_{\rm circ}\cong P_D^*\otimes\chi_N,
\qquad
\mathsf K_{\rm rel}\cong\chi_N.
\]

Thus entry 59's actual equivariant resolution is the \(\chi_N\)-twist of the
dual road sequence:

\[
0\longrightarrow\chi_N
\xrightarrow{\ \Delta_D^{\rm circ}\ }
P_D^*\otimes\chi_N
\longrightarrow A_2^*\otimes\chi_N
\longrightarrow0.
\]

Its underlying abelian groups are
\(0\to\mathbb Z_{\rm diag}\to\mathbb Z^3_{\rm tags}
\to H_1(K_{2,3})\to0\).  Equivalently,

\[
\boxed{
\varepsilon_D
=
(\Delta_D^{\rm circ})^\vee\otimes\chi_N
}
\]

at the lattice level.  The road coinvariant and Ward relation are therefore
twisted-dual derived presentations, not unrelated rank-one guesses.  Dropping
\(\chi_N\) would incorrectly identify the circuit relation line with the
trivial line: core exchange reverses every oriented tag even though it has
determinant \(+1\) on \(H_1\).

The derived-category statement must also use the correct exact triangle.  The
primitive line is

\[
\operatorname{cofib}(A_2\longrightarrow P_D)\simeq\mathbf1
\]

in

\[
A_2\longrightarrow P_D\longrightarrow\mathbf1
\longrightarrow A_2[1].
\]

The two-term complex \([P_D\xrightarrow{\varepsilon_D}\mathbf1]\) by itself
has \(A_2\) as its nonzero homology, up to degree convention/shift; it is not
the primitive quotient.  The dual triangle begins

\[
\mathbf1^\vee\longrightarrow P_D^\vee\longrightarrow A_2^\vee.
\]

This quotient must be distinguished from a cyclic section.  Any integral
\(C_3\)-invariant section has the form

\[
s(1)=a(1,1,1),
\]

and hence

\[
\varepsilon_Ds=3a.
\]

There is no integral equivariant section.  The unique invariant section after
inverting three is the average

\[
s(1)=\frac13(1,1,1).
\]

Only the splitting requires \(1/3\); the quotient \(\varepsilon_D\) itself is
integral and canonical.

## What entry 86 does and does not supply

Entry 86 constructs the occurrence-conjugated physical-core entry counit on
the marked direct sum and evaluates one six-point physical boundary in the
primitive line

\[
\mathsf J_4\boxtimes\mathsf J_4.
\]

It does not construct a three-road quotient

\[
\boxed{
\pi_D^{\rm PC}:
\operatorname{PC}(\mathsf J_4\boxtimes\mathsf J_{6,D})
\longrightarrow
\ell_D^{\rm prim}
}
\]

whose associated carrier map is \(\varepsilon_D\).  In particular, it does
not prove

\[
\pi_D^{\rm PC}\rho_{D,Q_i}(g_{Q_i})
=u_{D,Q_i}g_D
\]

with \(u_{D,Q_i}\) a normalized unit for all three roads, including the
occurrence marks, scalar Laurent weights, normal Pochhammer factor,
orientation line, and endpoint Cousin terms.

The bare adjoint formula is now a falsifiable test, not an established map:

\[
\pi_D^{\rm PC}
\stackrel{?}{=}
\mathbb D_{\rm Verdier}(\Delta_D^{\rm circ})
\]

As displayed it is not correctly typed: it omits \(\chi_N\), and entry 59
does not construct an occurrence-resolved circuit PC complex on which the
Verdier dual could already be taken.  A section and chain homotopy would be
additional data if a strong deformation retract, rather than a quotient, is
claimed.

Let \(C_D^{\rm road,PC}\) denote the complete marked road complex and let
\(C_D^{\rm circ,PC}\) denote the still-missing PC lift of entry 59's oriented
circuit-tag resolution.  The minimal candidate is a chain-level
twist-reversal pairing

\[
\boxed{
\Phi_D^{\rm PC}:
C_D^{\rm road,PC}
\longrightarrow
\mathbb D_{\rm Verdier}(C_D^{\rm circ,PC})\otimes\chi_N
}
\]

with associated carrier value

\[
q_{D,E_i}\longmapsto c_{i-2}^\vee\otimes e_{\chi_N}.
\]

Only after constructing this map would the typed adjoint formula be

\[
\boxed{
\pi_D^{\rm PC}
=
\bigl(\mathbb D_{\rm Verdier}(\Delta_D^{\rm circ})
\otimes\operatorname{id}_{\chi_N}\bigr)
\circ\Phi_D^{\rm PC},
}
\]

using \(\chi_N^\vee\otimes\chi_N\cong\mathbf1\).

## Bounded adjoint audit at \(D=(0,3)\)

The representative checker reconstructs the exact scalar associated grades
for all three induced six-point roads

\[
D_0=(0,3),\qquad D_1=(1,4),\qquad D_2=(2,5).
\]

Each road has a \(2\times2\) occurrence square.  For its occurrence generator
\(e_v\) of Laurent weight \(w_v\), the functional

\[
\lambda_i(e_v)=w_v^{-1}
\]

kills all four weighted interval boundaries and satisfies

\[
\lambda_i(w_ve_v)=1.
\]

Thus the three associated-grade primitive functionals exist integrally over
the Laurent ring.  This is not yet a functional on the complete PC complex.
After retaining entry 86's endpoint Cousin sign \(+1\), scalar-source sign
\(-1\), and entry-counit/coaction sign \(-1\), every one of the twelve marked
core entries has primitive period \(2\).  Each complete road has period \(4\),
so the exact road values furnished by that marked boundary calculation are

\[
(4,4,4),
\]

not a newly proved unit normalization.

The same checker computes the complete \(S_2^{\rm core}\times D_3\) character.
After the forced cyclic tag/road index shift,

\[
\langle gx,gc\rangle
=\chi_N(g)\langle x,c\rangle,
\]

and \((\Delta_D^{\rm circ})^\vee\otimes\chi_N\) has the three lattice values
\((1,1,1)\).  Entry 86, however, transports its recorded normal line by

\[
[dX_D]\longmapsto[dX_{gD}]
\]

with positive sign, and its marked primitive periods are invariant.  The
normal line alone therefore disagrees with \(\chi_N\) on six of the twelve
group elements.  This proves the bounded verdict

\[
\boxed{
\text{bare PC adjoint falsified; twisted PC adjoint untyped}.
}
\]

It does not prove that no physical orientation line can supply \(\chi_N\): the
required non-normal orientation factor is unresolved at this stage.
A falsifiable construction of \(\Phi_{03}^{\rm PC}\) must preserve the Laurent
weight inversion, satisfy the chain-pairing identity including endpoint
Cousin terms, and have signs \(+,-,-\) under one road rotation, one road
reflection, and core exchange.  No \(D_8\) extension is made before these
three representative tests pass.

Forward outcome (entry 89): the actual Borel--Moore/tangential orientation
system of the two-interval road faces is gauge-isomorphic to
\(\operatorname{sgn}_{\rm polarity}\otimes\operatorname{or}(C_3)=\chi_N\).
Thus the normal-line-only adjoint tested here remains false, but the complete
associated-grade pairing has the required character.  Its first missing PC
datum is entry 66's chain lift \(\boldsymbol\sigma_{\rm alt}\), and the result
is a boundary-costalk pairing rather than a quotient of the full lower
\(\mathsf J_6\) contact sector.

## The candidate medial Möbius hypercover carrier

The exact quadrangulation compatibility cell carrier has

\[
(\operatorname{rank}C_0,\operatorname{rank}C_1,
\operatorname{rank}C_2)
=(12,24,12),
\]

with eight cut triangles and four squares.  Its integral differentials obey

\[
d_1d_2=0,
\]

and have Smith forms

\[
\operatorname{SNF}(d_1)=1^{11},
\qquad
\operatorname{SNF}(d_2)=1^{12}.
\]

Consequently this cell carrier is a Möbius band \(M\) with

\[
H_\bullet(M;\mathbb Z)=(\mathbb Z,\mathbb Z,0).
\]

An exact free-face collapse leaves one vertex and one core edge.  The residual
octagon \(O\) satisfies

\[
\boxed{[O]=2[\gamma]}
\]

for the primitive Möbius core \(\gamma\).

This rank-one carrier homology is not by itself a scalar-derived coefficient
class.  Moreover, \(M\) is only a candidate truncated hypercover for the PC
totalization until its occurrence-resolved matching maps and cd-squares are
typed.

## Universal and sign local systems

Let

\[
R=\mathbb Z[u,u^{-1}]
\]

and let \(u\) be the crosscap monodromy.  Every face-edge collapse has a
Laurent-monomial unit coefficient.  The universal local-system cochain
complex therefore reduces exactly to

\[
R\xrightarrow{u-1}R.
\]

Hence

\[
H^0(M;R_u)=0,
\qquad
H^1(M;R_u)=R/(u-1),
\qquad
H^{>1}(M;R_u)=0.
\]

For the trivial specialization \(u=1\),

\[
H^\bullet(M;\mathbb Z)=(\mathbb Z,\mathbb Z,0).
\]

For the orientation specialization \(u=-1\), the exact integral Smith data
are

\[
\operatorname{SNF}(d_1^\eta)=1^{11}\oplus2,
\qquad
\operatorname{SNF}(d_2^\eta)=1^{12}.
\]

Thus

\[
H_\bullet(M;\mathbb Z_\eta)=(\mathbb Z/2,0,0),
\]

and

\[
H^\bullet(M;\mathbb Z_\eta)=(0,\mathbb Z/2,0).
\]

After tensoring with a characteristic-zero nonresonant PC field, the twisted
Möbius complex is acyclic.

The two mod-two local systems, trivial and orientation, are both
\(D_8\)-equivariant because \(H^1(M;\mathbb Z/2)\cong\mathbb Z/2\).  Both
have positive holonomy on \(O\), since \(O\) traverses the core twice.

## Conditional normal-sign theorem

Assume the missing PC quotient exists and has the unit road normalization

\[
\pi_D^{\rm PC}(q_{D,E_i})=g_D
\]

after the common Gysin factor is removed.  For adjacent charts, compare the
two ordered-normal contraction signs through that quotient.  The checker
computes the resulting voltage on all 24 compatibility edges.  It is closed
on all eight triangles and four squares and evaluates to

\[
1\pmod2
\]

on the Möbius core.  Therefore

\[
\boxed{
\text{unit primitive quotient}
\Longrightarrow
\text{orientation local system }\eta.
}
\]

For every one of the 16 dihedral actions and every one of the 24 edges, the
certificate proves the stronger explicit gauge formula

\[
v(g\cdot[Q,Q'])
=v([Q,Q'])+a_g(Q)+a_g(Q')\pmod2,
\]

where \(a_g(Q)\) is exactly the wedge-reordering sign needed to restore the
canonical sorted normal order after applying \(g\).  Thus the conditional
voltage is \(D_8\)-covariant up to this specified vertex gauge, not literally
invariant as an edge labeling.  Changing a chart's oriented generator is the
same kind of vertex gauge and does not change the crosscap class.

The implication is conditional exactly at \(\pi_D^{\rm PC}\).  Ordered
normal signs without a common primitive target do not define transition
units and do not select a local system.

## The residual octagon and the capped carrier

For universal monodromy, the outer octagon has holonomy \(u^2\).  It can be
capped only after imposing

\[
u^2=1.
\]

After the free collapses, the capped complex is the standard
\(\mathbb{RP}^2\) complex

\[
R/(u^2-1)
\xrightarrow{u+1}
R/(u^2-1)
\xrightarrow{u-1}
R/(u^2-1).
\]

At \(u=1\), the added octagon column gives Smith form

\[
1^{12}\oplus2,
\]

and

\[
H_\bullet(\mathbb{RP}^2;\mathbb Z)
=(\mathbb Z,\mathbb Z/2,0),
\]

\[
H^\bullet(\mathbb{RP}^2;\mathbb Z)
=(\mathbb Z,0,\mathbb Z/2).
\]

At \(u=-1\), the twisted octagon is already the boundary of the unique
signed relative fundamental chain made from the eight triangles and four
squares.  Capping produces

\[
H_\bullet(\mathbb{RP}^2;\mathbb Z_\eta)
=(\mathbb Z/2,0,\mathbb Z),
\]

\[
H^\bullet(\mathbb{RP}^2;\mathbb Z_\eta)
=(0,\mathbb Z/2,\mathbb Z).
\]

The twisted top class is the correctly typed *conditional carrier* for a
universal additive Jordan defect.  It is not a residual multiplicative
holonomy and it is not yet a scalar-derived coefficient class.

## Exact underdetermination

Before \(\pi_D^{\rm PC}\) is constructed, two inequivalent line systems are
compatible with the facewise carrier equations:

1. the trivial system;
2. the unique nontrivial orientation system.

Both are \(D_8\)-equivariant and both have outer-octagon holonomy \(+1\).
Thus no computation of

\[
T_7\cdots T_0
\]

can select between them; moreover the \(T_i\) are not defined before the
primitive quotient.

In the formal trivial-coefficient model, the face equations leave

\[
H^1(M;\mathbb Z)\cong\mathbb Z.
\]

The checker constructs two solutions, \(0\) and a primitive cocycle \(\omega\),
with octagon periods \(0\) and \(2\).  They have identical formal endpoint
and face equations.  This proves that bare cellular equations do not fix a
scalar Möbius/Jordan weight.  These formal solutions are logical witnesses of
underdetermination, not asserted physical PC lifts.

Therefore the requested trichotomy has the exact current answer:

1. strict raw occurrence-level gluing is false;
2. local derived gluing exists through either cut-center path;
3. global null-homotopy versus a nonzero Möbius/Jordan class is conditional on
   the missing primitive PC quotient and its crosscap character.

## Smallest next experiment

For \(D=(0,3)\), construct the occurrence-resolved circuit PC complex and the
single missing pairing

\[
\Phi_{03}^{\rm PC}:
C_{03}^{\rm road,PC}
\longrightarrow
\mathbb D_{\rm Verdier}(C_{03}^{\rm circ,PC})\otimes\chi_N.
\]

The smallest falsifiable seed calculation must:

1. send \(q_{03,E_i}\) to \(c_{i-2}^\vee\otimes e_{\chi_N}\) on the carrier;
2. reverse every scalar Laurent weight and satisfy the chain-pairing identity
   on the marked endpoint Cousin differential;
3. return sign \(-1\) under one road reflection and under core exchange, while
   returning \(+1\) under one road rotation;
4. explain how the exact marked periods \((4,4,4)\) descend to the claimed
   unit-normalized road generators without an untyped division or section.

Only if these representative tests pass should the \(D_8\) orbit be used to
define every other cut.  Only after that extension is it meaningful to decide
whether the normalized half-lines glue in the orientation system and whether
the capped twisted top class receives a nonzero scalar/Jordan coefficient.

## Exact certificate

Run:

```text
rustfmt --check research/nima/check_global_halfline_atlas.rs
rustc --edition=2021 -D warnings -O research/nima/check_global_halfline_atlas.rs -o "$env:TEMP\\marici-global-halfline-atlas.exe"
& "$env:TEMP\\marici-global-halfline-atlas.exe"
rustfmt --check research/nima/check_primitive_road_counit_adjoint.rs
rustc --edition=2021 -D warnings -O research/nima/check_primitive_road_counit_adjoint.rs -o "$env:TEMP\\marici-primitive-road-counit-adjoint.exe"
& "$env:TEMP\\marici-primitive-road-counit-adjoint.exe"
```

The global executable checks all twelve regional cubes and 96 rank-two occurrence
vertices, all 24 Gysin comparisons, the two center homotopies and Ward
ambiguity on every comparison, the road augmentation and its index-three dual
extension, all \(16\times24\) explicit wedge-reordering voltage identities,
the complete medial cell carrier, ordinary and sign Smith data, the universal
Laurent collapse, the residual octagon, the unique signed relative fundamental
chain, both capped specializations, and the conditional ordered-normal
crosscap voltage.  The representative executable checks all three \(D=03\)
road squares and twelve marked periods, the exact augmentation triangle, the
twisted circuit/road pairing for all twelve \(S_2^{\rm core}\times D_3\)
elements, and the six failures of the bare normal character.

Certificate SHA-256 values:

```text
d0a45f2e137d864f943163264df22b0e477678f0a996515dfa99d1fb7c4dcb85
87a419e39ec24a97afcd93922ec0909af25e98a9196d3da0aeffbade7fa96801
```

## Epistemic boundary

Established:

1. all twelve local primitive \(g_Q\) and their Alexander-complement
   occurrence representatives;
2. all physical residue/Gysin legs to the three-road cut objects;
3. failure of strict gluing and existence of two local center homotopies;
4. the saturated road augmentation and its \(\chi_N\)-twisted lattice duality
   with the circuit-tag resolution;
5. falsification of the bare PC adjoint with entry 86's recorded normal line;
6. the complete ordinary, Laurent, sign, and capped cell-carrier data;
7. exact underdetermination of the local system by outer-octagon holonomy;
8. conditional selection of the orientation system by a unit primitive
   quotient with the established ordered-normal signs.

Not established:

1. the occurrence-resolved PC quotient \(\pi_D^{\rm PC}\);
2. an occurrence-resolved circuit PC complex and the twist-reversal pairing
   \(\Phi_D^{\rm PC}\);
3. a cyclic section or strong deformation retract of the three-road object;
4. coefficient matching maps/cd-squares making the Möbius carrier an actual
   truncated hypercover;
5. a coefficient-valued residual two-cell/Jordan map;
6. a scalar-derived value of the twisted top class;
7. an invertible transition atlas on the raw regional PC complexes.

Reject:

> The shared rank-one physical core is already a literal coefficient line.

Also reject:

> Positive holonomy around the residual octagon proves that the primitive
> atlas has the trivial local system.

Also reject:

> The \(\mathbb Z/2\) class of the capped carrier is itself the scalar-derived
> Jordan obstruction.

## Decision

Promote:

> The eight-point primitive half-lines form an exact additive Gysin-cospan
> carrier with three-road channel objects.  Their carrier coinvariant is the
> \(\chi_N\)-twisted lattice dual of the Ward circuit relation, but the bare PC
> adjoint fails with the currently recorded normal line.  Its
> occurrence-resolved twist-reversal pairing is the missing counit datum.
> Conditional on a unit normalization, ordered normal signs give the
> orientation local system and the residual octagon bounds the signed relative
> fundamental chain.

Retain as the immediate frontier:

> Construct \(\Phi_{03}^{\rm PC}\), including the \(\chi_N\) twist and endpoint
> Cousin differential, before taking the adjoint of the circuit diagonal or
> extending by \(D_8\).  Do not infer the answer from abstract lattice duality
> or from the outer octagon.

## Internal dependencies

- Entry 59: nonsplit circuit-tag resolution and index-three obstruction.
- Entries 64--66: \(K_{2,3}\) suspension and Ward circuit normalization.
- Entry 69: full-core carrier and physical Gysin map.
- Entry 77: Alexander complement and primitive regional half-line.
- Entry 79: integral effective occurrence descent.
- Entries 82--83: target-first PC loading and additive octagon typing.
- Entries 86--87: occurrence entry counit and complete PC polarity homotopy.
- `research/nima/check_global_halfline_atlas.rs`.
- `research/nima/check_primitive_road_counit_adjoint.rs`.
