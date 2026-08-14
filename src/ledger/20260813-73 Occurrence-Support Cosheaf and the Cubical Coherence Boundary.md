# Occurrence-Support Cosheaf and the Cubical Coherence Boundary

## Record

Date: 2026-08-13

Status: exact eight-point support and target-carrier theorem, together with a
conditional formal totalization.

The nontransverse pentagon problem now separates into three logically
different statements:

\[
\boxed{
\begin{array}{c}
\text{constructible source coefficients}
\\[2pt]
\text{exact fixed-core cubical target}
\\[2pt]
\text{physical loaded Gysin naturality}.
\end{array}}
\]

The first two are established exactly.  The third is not.

The four physical support charts recover every basis vector of the relevant
rank-eight occurrence fiber, but they form only the four side facets of a
cube.  The two missing cap squares and the cube 3-cell give the correct target
coherence.  Occurrence support alone, however, does not select a chain map
from a five-edged route pentagon to a four-edged target square.

## The route-face coefficient cosheaf

Let \(F\) be one of the twenty-four octagon route faces and let \(\sigma\) be
a cell of \(F\).  Define

\[
\mathcal L_F(\sigma)
=
\mathbf Z\langle
d\mid d\text{ is a scalar diagonal fixed on }\sigma
\rangle .
\]

For a specialization from a cell to a boundary cell, the map is the canonical
inclusion on diagonal labels.  On every route face,

\[
\operatorname{rank}\mathcal L_F(F^\circ)=3,\qquad
\operatorname{rank}\mathcal L_F(E^\circ)=4,\qquad
\operatorname{rank}\mathcal L_F(v)=5.
\]

The complete system splits as a direct sum of rank-one
extension-by-zero coefficient systems:

\[
\boxed{
\mathcal L_F
\cong
\bigoplus_d i_{d,!}\mathbf Z_{S_d}.
}
\]

Here a common diagonal has support \(S_d=F\), while every noncommon diagonal
is supported on exactly one closed boundary edge and its two endpoints.
Thus the scalar coefficient is constructible rather than locally constant.
No endpoint transport is required or expected.

The exact audit covers

\[
8\text{ pentagons}+16\text{ squares},
\]

checks 312 generating specialization maps, and checks 176 rank-one support
summands.  For the representative pentagon,

\[
C=\{13,35,57\},
\qquad
(f_0,\ldots,f_4)=(17,37,03,05,15).
\]

The scalar flip span of entry 72 is the restriction of this cosheaf to one
closed edge:

\[
\mathbf Z^5
\longleftarrow
\mathbf Z^4
\longrightarrow
\mathbf Z^5.
\]

The exchanged endpoint quotient lines are therefore ordinary
extension-by-zero boundary contributions.  Their augmented relation

\[
d h_s=X_{15}-X_{37}
\]

is the weight shadow of this support diagram, not a bare scalar homotopy.

## Every rank-two core has an honest cube

Every one of the twelve octagon rank-two physical cores is a
quadrangulation.  Fixing such a core \(Q\) cuts the octagon into three
quadrilateral regions.  Refining each region chooses one of two diagonals, so
the fixed-core associahedral face is

\[
\boxed{
K_Q
\cong
K_4\times K_4\times K_4
\cong
I^3.
}
\]

The audit checks all twelve cubes, their 96 vertices, and all

\[
12\cdot 27=324
\]

cells of their cubical face posets.

There are two support profiles:

1. eight pentagon--companion-square cores have four distinct physical
   supports \(P_+,P_-,S_+,S_-\);
2. four square--square cores have only two distinct supported facets.

The four-chart coherence problem therefore belongs specifically to the first
eight cores.  It is not an all-core statement.

For the representative

\[
Q=\{03,05\},
\]

the four supported subsets are literal coordinate facets:

\[
\begin{array}{c|c|c}
\text{chart}&\text{facet}&\text{outward sign}\\ \hline
S_+&x_2=0&-1\\
S_-&x_0=0&-1\\
P_+&x_2=1&+1\\
P_-&x_0=1&+1.
\end{array}
\]

The missing faces are the opposite caps

\[
x_1=0,\qquad x_1=1,
\]

and the unique cube cell \((*,*,*)\).

## What the two-stage Čech theorem did and did not cover

Entry 72 proves saturated coefficient descent:

\[
0\to\mathbf Z^2
\to\mathbf Z^4\oplus\mathbf Z^4
\to\mathbf Z^6\to0,
\]

\[
0\to\mathbf Z^4
\to\mathbf Z^6\oplus\mathbf Z^6
\to\mathbf Z^8\to0.
\]

Flattening the four charts gives

\[
\boxed{
0
\longrightarrow
\mathbf Z^8
\longrightarrow
\mathbf Z^{16}
\longrightarrow
\mathbf Z^8
\longrightarrow0.
}
\]

Every occurrence basis vector belongs to exactly two charts, there are four
rank-two pairwise overlaps, and there are no triple intersections.  Every
nonzero Smith factor is one.

This is an exact cover of the rank-eight vertex module.  It is not a
geometric cover of \(I^3\).  The union \(B_Q\) of the four chart facets has
cell census

\[
(C_0,C_1,C_2,C_3)=(8,12,4,0)
\]

rather than

\[
(8,12,6,1).
\]

Equivalently,

\[
B_Q\cong S^1\times I.
\]

The flattened cover is saturated in every cellular degree of the belt:

\[
\begin{array}{c|c}
\text{degree}&\text{exact sequence}\\ \hline
0&0\to\mathbf Z^8\to\mathbf Z^{16}\to\mathbf Z^8\to0\\
1&0\to\mathbf Z^4\to\mathbf Z^{16}\to\mathbf Z^{12}\to0\\
2&0\to0\to\mathbf Z^4\to\mathbf Z^4\to0.
\end{array}
\]

Thus entry 72 computed the complete coefficient and belt descent correctly,
but its word “cover” must be read degreewise: the four physical charts do not
contain the cap 2-cells or the 3-cell.

## Caps, cube, and exact higher coherence

Let \(K_Q^+\) and \(K_Q^-\) be the two missing cap squares, with the
orientations induced from \(I^3\), and orient the belt by its four outward
side facets.  The exact cubical identities are

\[
\boxed{
\partial B_Q
=
-\partial(K_Q^++K_Q^-),
}
\]

and

\[
\boxed{
B_Q+K_Q^++K_Q^-
=
\partial I_Q^3.
}
\]

The integral homology audit gives

\[
\begin{array}{c|c|c}
\text{carrier}&(C_0,C_1,C_2,C_3)&(H_0,H_1,H_2,H_3)\\ \hline
B_Q&(8,12,4,0)&(\mathbf Z,\mathbf Z,0,0)\\
B_Q+\text{one cap}&(8,12,5,0)&(\mathbf Z,0,0,0)\\
\partial I_Q^3&(8,12,6,0)&(\mathbf Z,0,\mathbf Z,0)\\
I_Q^3&(8,12,6,1)&(\mathbf Z,0,0,0).
\end{array}
\]

The two caps are two fillings of the belt generator.  The cube 3-cell is the
higher homotopy comparing those fillings.  This is the first completely
explicit cubical coherence cell in the scalar incidence calculus.

It also explains why previous audits found no local curvature.  A genuine
constructible coefficient functor has flat incidence squares locally.  The
nontrivial datum appears in the global belt cycle and in the cells that fill
it, not as an asymmetric edge defect.

## Formal loaded totalization

For the representative core, form the tensor totalization of:

1. the flattened four-chart Čech complex;
2. the cellular tube complex of the belt, caps, and cube;
3. the ordered two-normal Koszul complex for \(D\) and \(E\).

With total differential

\[
d_{\rm tot}
=
d_{\rm Cech}
+(-1)^a d_{\rm tube}
+(-1)^{a+t}d_{\rm normal},
\]

the exact checker verifies

\[
d_{\rm tot}^2=0
\]

on 4512 basis symbols.  It also verifies the formal relation

\[
\operatorname{Res}_{D,E}^{\rm formal}d_{\rm tot}
=
d_{\rm tot}\operatorname{Res}_{D,E}^{\rm formal}
\]

on every basis symbol.  The two ordered contractions obey

\[
\iota_E\iota_D(D\wedge E)=+1,
\qquad
\iota_D\iota_E(D\wedge E)=-1.
\]

Conditional on the undecorated facewise Pochhammer chain map of entry 38,
these cellular generators have formal loaded tube symbols.  The existing
exact-core product supplies formal symbols for the caps and cube.

This proves that the proposed algebraic totalization is consistent.  It does
not prove that it is the physical finite-\(\alpha'\) Gysin map.

## The remaining nonuniqueness

Occurrence support determines the four target square facets and their
inclusions.  It does not determine maps from the route-face edges and
2-cells.

The support-only enumeration finds:

\[
20+20=40
\]

pentagon-to-square cellular lifts, twenty for each orientation, and

\[
4+4=8
\]

square-to-square lifts, four for each orientation.

One formal candidate collapses the scalar flip edge of the pentagon, maps the
companion square isomorphically, and sends the four chart faces to the
oriented belt.  It is a valid cellular model.  Nothing in the presently
established occurrence support, cut ordering, or deck data selects it from
the other lifts.

Consequently:

\[
\boxed{
\text{target cubical exactness}
\not\Rightarrow
\text{physical Gysin naturality}.
}
\]

The caps and cube make any correctly oriented belt discrepancy exact after a
route-to-cube lift is supplied.  They do not construct that lift.

## Interpretation

The emerging object is not a strict operator algebra on amplitudes.  At this
arity it has:

- constructible coefficient systems rather than constant fibers;
- Gysin correspondences rather than invertible transports;
- Čech colimits rather than pointwise identifications;
- cap homotopies and cube coherences rather than strict equalities.

The appropriate provisional name remains

\[
\boxed{
\text{bivariant constructible homotopy-coherent incidence calculus}.
}
\]

The fixed-core cube supplies an explicit first higher coherence law.  The
unresolved physical input is a natural transformation from route-face loaded
Pochhammer/Cousin complexes to this cubical target.

## Reproducible certificates

Run:

    rustfmt --check research/nima/check_occurrence_support_cosheaf.rs
    rustc --edition=2021 -D warnings -O research/nima/check_occurrence_support_cosheaf.rs -o "$env:TEMP\\marici-occurrence-support.exe"
    & "$env:TEMP\\marici-occurrence-support.exe"

    rustfmt --check research/nima/check_cubical_gysin_coherence.rs
    rustc --edition=2021 -D warnings -O research/nima/check_cubical_gysin_coherence.rs -o "$env:TEMP\\marici-cubical-gysin.exe"
    & "$env:TEMP\\marici-cubical-gysin.exe"

    rustfmt --check research/nima/check_loaded_cech_totalization.rs
    rustc --edition=2021 -D warnings -O research/nima/check_loaded_cech_totalization.rs -o "$env:TEMP\\marici-loaded-cech.exe"
    & "$env:TEMP\\marici-loaded-cech.exe"

Certificate SHA-256 values:

    check_occurrence_support_cosheaf.rs
    58603679078082413a8a74f736cd239cfae2149c5ceb3e648dc9d02dc209c3ba

    check_cubical_gysin_coherence.rs
    53693b0eaebd724d24e8fd35eddc08924cbd342e53bf61aa5f28176b1fbcd6c1

    check_loaded_cech_totalization.rs
    492c0669f8b102198dbaceb0495b27f8c56075703cee740cafbfb6d943a60fa4

## Decision

Promote:

> The route-face diagonal coefficient is an extension-by-zero constructible
> cosheaf.  Every rank-two core has an exact fixed-core cube, and on the eight
> four-chart cores its physical supports form the side belt.  Two cap squares
> and the cube 3-cell provide an exact target coherence.  The associated
> formal Čech--tube--normal totalization squares to zero and has a formal
> residue chain map.

Retain as conditional:

> The formal pentagon-collapse carrier is the finite-\(\alpha'\) physical
> double-Gysin natural transformation.

Reject:

> Recovering the rank-eight occurrence module from four support charts already
> proves a geometric cover or a physical chain map.

## Next experiment

Construct the actual degree-shifted map

\[
G_{D,E}^{\alpha'}:
\operatorname{PC}_{\alpha'}(F;\mathcal L_F)
\longrightarrow
\operatorname{PC}_{\alpha'}(I_Q^3;\mathcal L_Q)[-2]
\]

on route faces, edges, and vertices.  Its formulas must:

1. select one of the forty pentagon lifts intrinsically;
2. include the \(X_{15}\) and \(X_{37}\) quotient lower terms;
3. respect the two normal orientation orders;
4. extend over both caps and the cube;
5. satisfy
   \[
   G_{D,E}^{\alpha'}d_{\rm PC}
   =
   d_{\rm PC}G_{D,E}^{\alpha'}
   \]
   generator by generator;
6. rotate through the eight-core deck orbit.

Only this experiment can close the nontransverse finite-\(\alpha'\) gap.

## Internal dependencies

- Entries 27 and 32: regional occurrence fibers and strict physical support
  coaction.
- Entry 38: undecorated facewise Pochhammer/Cousin chain map and the corrected
  transverse domain.
- Entries 69--72: rank-two carrier, coefficient Gysin audit, transport no-go,
  and saturated constructible descent.
- research/nima/check_occurrence_support_cosheaf.rs.
- research/nima/check_cubical_gysin_coherence.rs.
- research/nima/check_loaded_cech_totalization.rs.
