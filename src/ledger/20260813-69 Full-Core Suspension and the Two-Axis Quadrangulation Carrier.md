# Full-Core Suspension and the Two-Axis Quadrangulation Carrier

## Record

Date: 2026-08-13

Status: exact eight-point combinatorial and integral-homology theorem. It
executes the rank-two falsifier posed in entry 68. The proposed identification
of the scalar rank-two completion with the known Möbius carrier is false.

The positive replacement is more structured. After contracting only
connected exact-core fibers, the scalar rank-at-most-two carrier has homotopy
type

\[
K_{2,12}=S^0*\operatorname{Quad}_8,
\]

where the twelve roads are the full octagon quadrangulations, not the eight
rank-one physical channels. The Möbius carrier instead organizes
compatibility and coherence *among* those quadrangulations. These are two
different axes of one derived incidence calculus.

## The claim that was tested

Entry 68 left two precise questions:

1. Does the honest rank-two scalar completion recover the eight-triangle,
   four-square Möbius carrier?
2. Does its marked link at a physical channel recover the local
   \(K_{2,3}\) suspension?

The answers are respectively

\[
\boxed{\text{no}}
\qquad\text{and}\qquad
\boxed{\text{yes}}.
\]

The negative answer is not a lack of enough scalar cells. The exact
associahedral cells are present, but their boundaries have a different typing
from the guessed \(\Gamma_8\) fillers.

## Exact octagon census

Let \(\operatorname{Tri}_8\) be the 132 octagon triangulations and let the
physical core retain diagonals joining vertices of opposite parity.

The exact fibers in core ranks zero through two are:

\[
\begin{array}{c|c|c}
\text{core rank}&\text{number of connected components}&
\text{component type}\\ \hline
0&2&I\\
1&16& I\ \text{(two over each of eight channels)}\\
2&12&I^3\ \text{(one over each quadrangulation)}.
\end{array}
\]

Thus the rank-zero/rank-one incidence is the disjoint union

\[
K_{1,8}^{+}\sqcup K_{1,8}^{-}.
\]

Every rank-two core is a compatible pair \(Q=\{D,E\}\), hence a full
quadrangulation of the octagon. Its exact fiber contains eight triangulations
and has the one-skeleton of a cube.

## Why the cube does not fill \(\Gamma_8(e_D-e_E)\)

The octagon associahedron has 300 two-faces. For every rank-two core \(Q\),
the six square faces internal to its cube are core-constant. After the exact
fiber is contracted, all six boundaries become zero. Across the twelve
quadrangulations this gives

\[
12\cdot 6=72
\]

core-constant squares, none of which has boundary
\(\Gamma_8(e_D-e_E)\).

The actual transverse faces are different. For each pair
\((Q,\varepsilon)\), with \(\varepsilon\in\{+,-\}\), there is exactly one
associahedral route face comparing the two paths through \(D\) and \(E\) on
the same polarity sheet. There are

\[
16\ \text{squares}+8\ \text{pentagons}=24
\]

such faces. A pentagon has two zero-core vertices in the same connected
interval, so after connected-fiber contraction it becomes the same four-edge
route cell as a square:

\[
P_\varepsilon
\longrightarrow D_\varepsilon
\longrightarrow Q
\longrightarrow E_\varepsilon
\longrightarrow P_\varepsilon.
\]

This is a same-sheet homotopy. A single route face never crosses from
\(+\) to \(-\), and therefore cannot itself be a polarity suspension square.

## The honest rank-two carrier

After contracting connected exact-core fibers and retaining the 24 transverse
route cells, the cellular ranks are

\[
(\operatorname{rank}C_0,
  \operatorname{rank}C_1,
  \operatorname{rank}C_2)
=(30,64,24).
\]

The integral boundary matrices satisfy

\[
\partial_1\partial_2=0,
\]

with exact Smith data

\[
\operatorname{SNF}(\partial_1)=1^{29},
\qquad
\operatorname{SNF}(\partial_2)=1^{24}.
\]

Consequently

\[
H_0\cong\mathbb Z,
\qquad
H_1\cong\mathbb Z^{11},
\qquad
H_2=0.
\]

There is also a direct homotopy description. For each polarity, the route
cells form a contractible sheet. The two sheets intersect precisely in the
twelve discrete rank-two fibers. Their union is therefore homotopy equivalent
to the suspension of that twelve-point set:

\[
\operatorname{hocolim}
\bigl(\operatorname{Core}_{\le2}(\operatorname{Tri}_8)\bigr)
\simeq
S^0*\operatorname{Quad}_8
\simeq K_{2,12}.
\]

This does **not** restore the rejected rule “one \(K_{2,m}\) per arity.” It
identifies the correct eight-point indexing set only after the full-core rank
is reached. At six points full quadrangulations already have rank one, so the
three channels and the three quadrangulations happen to coincide.

## The inadmissible \(K_{2,8}\) quotient

If the two disconnected components over every rank-one channel are first
merged, one manufactures a coarse \(K_{2,8}\). Attaching one abstract square
for each compatible pair \(\{D,E\}\) then gives boundaries

\[
\Gamma_8(e_D-e_E).
\]

In \(H_1(K_{2,8})\cong A_7\), their incidence matrix has Smith form

\[
1^7\oplus 0^5,
\]

so the imposed quotient complex has

\[
H_0\cong\mathbb Z,
\qquad H_1=0,
\qquad H_2\cong\mathbb Z^5.
\]

This is a valid abstract suspension of the compatibility graph, but it is not
the contraction of connected scalar fibers. The merger that creates its
polarity-crossing squares is precisely the noncanonical step.

## Why the Möbius carrier is a second axis

Let \(G_8\) be the compatibility graph whose eight vertices are physical
channels and whose twelve edges are octagon quadrangulations. It is the
Möbius ladder, with

\[
H_1(G_8;\mathbb Z)\cong\mathbb Z^5.
\]

The known medial carrier contains eight channel triangles, four square
relations, and a residual octagon. The four square cycles together with the
octagon span a sublattice of \(H_1(G_8)\) with Smith invariants

\[
(1,1,1,1,2).
\]

Equivalently, the octagonal boundary is twice the Möbius core; after the final
cell is attached one sees the familiar \(\mathbb Z/2\) class of
\(\mathbb{RP}^2\).

This proves that the Möbius object is not the connected-fiber rank-two
homotopy colimit:

\[
H_\bullet(\text{rank-two scalar carrier})
=(\mathbb Z,\mathbb Z^{11},0),
\]

whereas

\[
H_\bullet(\text{Möbius carrier})
=(\mathbb Z,\mathbb Z,0).
\]

The two objects play complementary roles:

\[
\begin{array}{c|c}
\text{vertical axis}&\text{horizontal axis}\\ \hline
\text{global polarity descent}&
\text{quadrangulation compatibility}\\
S^0*\operatorname{Quad}_8&
\text{triangles, squares, and octagon on }G_8\\
\text{transition between two dictionaries}&
\text{coherences among full-core roads}.
\end{array}
\]

At six points \(G_6=C_3\), so its road compatibility complex and the
three-road suspension are small enough to masquerade as a single triangle.
Eight points is the first arity at which the two directions separate.

## Marked Cut is a degree-shifting Gysin map

Fix one physical channel \(D\). Its rank-one fiber has two connected
components; these become the two centers of the local carrier. Exactly three
rank-two quadrangulations contain \(D\). After contracting the spectator
quadrilateral factor, these become the three roads. Hence the marked link is
honestly

\[
K_{2,3}.
\]

The Gysin map lowers the core rank:

\[
G_D:\{D,E\}\longmapsto q_E.
\]

A single quadrangulation maps to a road, not to a local cycle. Only a
sum-zero difference suspends:

\[
\Gamma_D\bigl(q_E-q_F\bigr)
\in H_1(K_{2,3};\mathbb Z).
\]

All eight marked channels, 48 center-road incidences, and 24 local
four-circuits pass exactly. Therefore factorization is typed as

\[
\boxed{
\text{global full-core coefficient}
\xrightarrow{\ G_D\ }
\text{local road coefficient}
\xrightarrow{\ \Gamma_D\ }
\text{local Ward circuit}.}
\]

It is not a graph-deletion map
\(H_1(K_{2,8})\to H_1(K_{2,3})\).

## Revised all-arity trajectory

For a \(2p\)-gon, the number of full quadrangulations is the Fuss--Catalan
number

\[
Q_{2p}
=\frac{1}{2p-1}\binom{3p-3}{p-1}
=3,12,55,273,\ldots
\]

for \(2p=6,8,10,12,\ldots\).

The eight-point theorem motivates, but does not prove, the all-arity
candidate

\[
\mathcal V_{2p}
\simeq
S^0*\operatorname{Quad}_{2p}
\]

for the vertical full-core polarity carrier. The horizontal object should be
a cellular resolution of the quadrangulation flip/compatibility complex. A
minimal algebraic shadow is the sequence

\[
C_1(\mathcal Q_{2p})
\xrightarrow{\partial_{\rm flip}}
\widetilde C_0(\operatorname{Quad}_{2p})
\xrightarrow{\Gamma}
H_1(S^0*\operatorname{Quad}_{2p}),
\]

with higher cells encoding relations among flips. This is a conjectural
trajectory, not yet an all-arity scalar theorem.

The more invariant candidate is the Grothendieck construction or homotopy
colimit of connected exact-core fibers over the physical-core poset, equipped
with the occurrence coefficient cosheaf and regional-polarity orientation
line. It replaces the idea of a strict arity-indexed operator algebra by a
derived, homotopy-coherent dictionary between self-factorizing carriers.

## Next coefficient-level falsifier

The topological carrier is now typed. The missing datum is the coefficient
map. For each of the 24 transverse route faces, attach the actual scalar
residue line and polarity transport, then test whether

\[
G_D(Q_E-Q_F)
\]

intertwines the occurrence differential with the local Ward suspension

\[
\Gamma_D(q_E-q_F)
\]

before gauge/BRST descent. This must be checked facewise and with the
one-step-rotation orientation local system. Agreement only after summing the
amplitude is not sufficient.

## Reproducible certificate

Run:

```text
rustfmt --check research/nima/check_eight_point_rank_two_gysin.rs
rustc --edition=2021 -D warnings -O research/nima/check_eight_point_rank_two_gysin.rs -o "$env:TEMP\\marici-rank-two-gysin.exe"
& "$env:TEMP\\marici-rank-two-gysin.exe"
```

The certificate exhausts all 132 triangulations and 300 associahedral
two-faces, derives all connected exact-core fibers and transverse route
faces, computes both integral chain complexes and their Smith data, compares
the Möbius face lattice, and checks every marked link/Gysin incidence.

Certificate SHA-256:

```text
80a15902886bd3b4cfda13fbfedf2513a2b275000fdc83fb237d82a1a00e6318
```

## Internal dependencies

- Entries 21--27: scalar polarity transfer and core-filtered factorization.
- Entries 31, 32, and 37: associahedral envelope and occurrence-level Gysin
  coaction.
- Entries 60--66: circuit resolution, flow torsor, suspension, and conductor
  transgression.
- Entries 67--68: coarse eight-point quotient and its regional-polarity
  correction.
- `research/nima/check_eight_point_rank_two_gysin.rs`: exact certificate.
