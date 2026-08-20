# Coefficient Gysin Squares and the Nontransverse Pentagon Gap

## Record

Date: 2026-08-13

Status: exact eight-point partial theorem and sharp typing obstruction.  The
coefficient-valued marked-Cut comparison closes on all sixteen transverse
square carriers.  It is not yet a theorem on the full twenty-four-face
carrier: the remaining eight faces are dependent associahedral pentagons and
require a rank-preserving scalar coefficient transport which has not been
defined.

The correct verdict on the full comparison is therefore

\[
\boxed{\text{inconclusive, with the missing map isolated exactly}.}
\]

This is not a numerical failure of factorization.  Every rank-two occurrence
fiber factors exactly.  The gap is the absence of a morphism on one specific
kind of same-core scalar edge.

## The square that was tested

Entry 69 identifies the vertical eight-point carrier as the homotopy colimit
of two contractible polarity sheets meeting in the twelve full
quadrangulation fibers.  Marking a physical channel \(D\) gives the local
six-point suspension carrier \(K_{2,3}\).  At the coefficient level the
desired comparison has the form

\[
\begin{array}{ccc}
\ker\!\left(
\bigoplus_{Q\in\operatorname{Quad}_8}\mathcal L_8(Q)
\longrightarrow
H_0(U_+;\mathcal L)\oplus H_0(U_-;\mathcal L)
\right)
\xrightarrow{\delta_{\rm MV,8}}
H_1(\mathcal V_8;\mathcal L)\\
\downarrow^{G_D} && \downarrow^{G_D^{\rm link}}\\
\mathcal L_4(\varnothing)\boxtimes
\widetilde C_0(R_3;\mathcal L_6)
\xrightarrow{1\boxtimes\Gamma_D}
\mathcal L_4(\varnothing)\boxtimes
H_1(K_{2,3};\mathcal L_6).
\end{array}
\]

Here \(\delta_{\rm MV,8}\) is the coefficient-valued connecting morphism,
not the constant-coefficient suspension obtained by identifying all full-core
fibers.  The certificate tests the finite cellular data needed to type this
diagram.

## Exact full-core coefficient fibers

For every octagon quadrangulation

\[
Q=\{D,E\},
\]

the three quadrilateral regions independently choose one of two scalar
diagonals.  Hence

\[
\operatorname{rank}\mathcal L_8(Q)=2^3=8.
\]

For either marked channel, the basis factors canonically as

\[
\boxed{
\mathcal L_8(\{D,E\})
\cong
\mathcal L_4(\varnothing)
\boxtimes
\mathcal L_6(q_E),
}
\]

with ranks

\[
8=2\cdot4.
\]

The audit verifies all

\[
12\cdot2\cdot8=192
\]

marked basis factorizations and all forty-eight center--road incidences.  No
amplitude summation or QTDS target data is used.

The scalar coefficient sign also factors correctly:

\[
(-1)_{8\rm pt}
=
(-1)_{4\rm pt}(+1)_{6\rm pt}.
\]

## Coefficient maps commute, Gysin maps anticommute

On a compatible pair \(D,E\), the occurrence-level physical maps of entry 32
satisfy

\[
G_EG_D=G_DG_E.
\]

This is an equality of degree-zero Laurent/occurrence maps.  The actual
Cousin/Gysin operation also carries the normal-orientation line

\[
\operatorname{or}(N_D)\wedge\operatorname{or}(N_E).
\]

Consequently the two iterated degree-one maps obey the Koszul relation

\[
\widetilde G_E\widetilde G_D
=
-\widetilde G_D\widetilde G_E.
\]

The certificate finds twelve positive and twelve negative marked
factor-orientation identifications, exactly as required by exchanging the two
normal factors.  Thus ``commuting Cuts'' and ``anticommuting Gysin
differentials'' are not competing claims; they live in different degrees.

## The sixteen strict route squares

Among the twenty-four transverse associahedral route faces, sixteen have core
rank pattern

\[
[0,1,2,1].
\]

They are literal squares.  Both routes begin at the same zero-core scalar
presentation and add the compatible physical channels in opposite orders.
The established strict coaction therefore applies without adding any new
transport:

\[
P_\varepsilon
\xrightarrow{G_D}
D_\varepsilon
\xrightarrow{G_E}
Q

=

P_\varepsilon
\xrightarrow{G_E}
E_\varepsilon
\xrightarrow{G_D}
Q
\]

at occurrence level, with the preceding Koszul sign after adjoining normal
orientations.

The supported face audit expands forty source records to 160 rank-two
occurrence records and finds exact equality in both physicalizing orders.
This proves coefficient flatness on every square route before gauge or BRST
descent.

## Why the eight pentagons are different

The other eight route faces have pattern

\[
[0,0,1,2,1].
\]

Each contains an initial scalar flip

\[
T_0\longleftrightarrow T_1,
\qquad
\rho(T_0)=\rho(T_1)=\varnothing,
\]

followed by the two dependent physicalization routes.  The two routes do not
therefore start in the same occurrence fiber.  To write their comparison one
first needs a rank-preserving map

\[
\tau_s:
\mathcal L(T_0)longrightarrow\mathcal L(T_1)
\]

on the scalar flip \(s\), together with its residue-line and deck transport.

Entries 32 and 37 do not define this map.  Entry 32 defines the physical
coaction.  Entry 37 proves mixed base change on independent product cells.
The pentagon is the first dependent, nontransverse \(A_2\) cell and lies
outside that theorem's stated domain.

Accordingly, an equation such as

\[
d_{\rm occ}G_D
=
\Gamma_DG_Dd_{\rm occ}
\]

is not false on these faces.  It is not yet typed because
\(d_{\rm occ}\) has no declared coefficient component on the same-core
scalar edge.

There are two legitimate ways the missing datum could appear:

1. a strict, deck-equivariant scalar-flip transport \(\tau_s\) satisfying the
   pentagon relation;
2. a degree-one Pochhammer/Cousin homotopy whose boundary is the discrepancy
   between the two coefficient routes.

The second is the natural possibility if the occurrence module is only an
associated grade of a larger nearby-cycle complex.

## Marked link and local suspension

After the full-core coefficient has factored on a marked channel \(D\), the
three compatible cores become three distinct local road summands.  Only then
is the reduced difference module formed.  For every pair of local roads,

\[
q_E-q_F\in\widetilde C_0(R_3),
\]

the Mayer--Vietoris suspension gives the four-edge circuit

\[
\Gamma_D(q_E-q_F)\in H_1(K_{2,3}).
\]

All twenty-four such reduced-road circuit checks pass.  This confirms the
typing

\[
\boxed{
\text{factor the coefficient fiber}
\longrightarrow
\text{form a reduced road difference}
\longrightarrow
\text{suspend}.}
\]

Applying \(\Gamma_D\) before factorization would identify unrelated
occurrence bases and is prohibited.

## Holonomy and the surviving index-two class

One-step deck rotation exchanges the two regional-polarity sheets, but its
eight-step orbit is not the residual compatibility octagon.  Thus deck
oddness by itself does not define pointwise transport on the edges of that
octagon.

The finite audit exhibits two distinct deck-equivariant edge-sign extensions.
They differ pointwise, yet both have trivial holonomy on all five cycle
generators of the Möbius ladder.  Independently, the physical normal-line
comparison on a compatibility edge is the exchange

\[
\operatorname{or}(N_D)\wedge\operatorname{or}(N_E)
\longleftrightarrow
\operatorname{or}(N_E)\wedge\operatorname{or}(N_D),
\]

and the route face stays on one polarity sheet.  Around the residual octagon
the three holonomies are therefore

\[
(h_{\rm normal},h_{\rm polarity},h_{\rm tensor})
=(+1,+1,+1).
\]

Consequently no sign line already present in this audit removes the integral
index

\[
\boxed{2}
\]

of the four square cycles plus the octagon inside
\(H_1(G_8;\mathbb Z)\).  A future nontrivial resolution must come from the
missing coefficient face maps or higher cells, not from relabelling the
existing deck signs.

## Structural interpretation

The scalar master is not yet presenting a strict flat local system on the
coarse core-poset carrier.  What is established is a partially defined
bivariant calculus:

\[
\begin{array}{c|c}
\text{transverse physical intersections}
&\text{strict coefficient base change}\\
\text{normal orientation lines}
&\text{Koszul Gysin signs}\\
\text{dependent scalar/physical pentagons}
&\text{Cousin transport still required}.
\end{array}
\]

This is evidence for the stronger derived picture.  Normal extraction,
factorization, and suspension behave like operations in a recollement or
six-functor calculus; nontransverse base change is supplied by a higher
comparison rather than silently identified with a strict square.

## Next falsifier

On each of the eight pentagons, retain the complete occurrence basis at all
five vertices and ask whether the regional Catalan construction determines
\(\tau_s\) without target input.  Require simultaneously:

1. linearity over the scalar kinematic ring;
2. compatibility with the physical Gysin maps;
3. the signed pentagon boundary relation;
4. one-step deck covariance;
5. marked-Cut factorization.

If two inequivalent transports satisfy all existing axioms, the scalar grade
does not determine the lift and a Pochhammer/Cousin enrichment is necessary.
If none exists strictly but the discrepancy is a canonical boundary, the
pentagon supplies the first genuinely derived base-change homotopy.

Forward result: entry 71 executes this falsifier. Strict Laurent support
already obstructs a weight-preserving endpoint isomorphism, while the common
rank-eight fiber admits both \(+\operatorname{Id}\) and
\(-\operatorname{Id}\) under every currently established fixed-core, Cut,
orientation, and deck constraint. The two choices give pentagon defects zero
and \(-2\operatorname{Id}\). An edgewise transport is therefore not
intrinsic; the next object is the full loaded five-facet Cousin face.

Entry 72 then proves the underlying occurrence repair: replace the missing
transport by a constructible common-label span and reconstruct each full
rank-eight fiber through two saturated Čech gluings. The finite-alpha-prime
loaded realization of that diagram remains open.

## Reproducible certificate

Run:

```text
rustfmt --check research/nima/check_eight_point_coefficient_gysin.rs
rustc --edition=2021 -D warnings -O research/nima/check_eight_point_coefficient_gysin.rs -o "$env:TEMP\\marici-coefficient-gysin.exe"
& "$env:TEMP\\marici-coefficient-gysin.exe"
```

Certificate SHA-256:

```text
057979dfd8e20abc2512604556de09c0228fdfd57607b79cacf03dcd4a5fad55
```

The executable enumerates all 132 triangulations and 300 associahedral
two-faces, isolates the sixteen squares and eight pentagons, constructs every
rank-eight full-core occurrence fiber, verifies marked factorization and
orientation signs, checks all local suspension circuits, and computes the
Möbius-lattice index and available sign holonomies.

## Internal dependencies

- Entries 24 and 27: scalar coorientation and regional occurrence
  coefficients.
- Entries 31--38: associahedral envelope, strict physical coaction, mixed
  base change, and finite-alpha-prime Cousin orientation lines.
- Entries 64--66: Mayer--Vietoris suspension and the local Ward conductor.
- Entries 68--69: regional polarity fibers and the two-axis rank-two carrier.
- `research/nima/check_eight_point_coefficient_gysin.rs`: exact certificate.
