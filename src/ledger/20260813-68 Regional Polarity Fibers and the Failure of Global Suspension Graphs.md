# Regional Polarity Fibers and the Failure of Global Suspension Graphs

## Record

Date: 2026-08-13

Status: exact combinatorial theorem for zero- and one-core scalar fibers,
proved directly and exhaustively audited through twelve points. It corrects
the global \(K_{2,8}\) claim of entry 67.

At six points, every rank-one physical-core fiber is connected and is incident
to both scalar polarity components. This exceptional fact gives the genuine
carrier \(K_{2,3}\).

From eight points onward, the exact-core fibers split into regional polarity
components. Contracting connected fibers does not give \(K_{2,r}\). At eight
points the raw rank-zero/rank-one incidence is two disjoint eight-road stars.
At ten and twelve points it is a bipartite multigraph with parallel incidences
and additional one-core components that do not meet rank zero.

The scalar master therefore carries a stratified diagram of regional
polarity fibers, not a single global suspension graph. Higher physical-core
cells or a homotopy colimit are required to compare the two global polarity
sheets.

## Zero-core factorization

Let \(n=2p\), color the polygon vertices alternately, and call a diagonal
physical when it joins opposite colors. For a triangulation \(T\), let
\(\rho(T)\) be its set of physical diagonals.

A zero-core triangulation contains only same-color diagonals. For \(n\ge6\),
it chooses one of the two color classes and a triangulation of the corresponding
\(p\)-gon. Hence the zero-core flip graph is

\[
\boxed{
\mathcal F_\varnothing
\cong
\operatorname{Ass}(p)\sqcup\operatorname{Ass}(p),
}
\]

where \(\operatorname{Ass}(p)\) is the flip graph of triangulations of a
\(p\)-gon. Each component has

\[
C_{p-2}
\]

vertices and is the one-skeleton of an associahedron of dimension \(p-3\).
One-step rotation exchanges the components.

This recovers the known count

\[
|\mathcal F_\varnothing|
=
2C_{p-2}.
\]

At \(n=4\), the two zero-core triangulations are joined by the quadrilateral
flip. This exceptional connected interval will be denoted by \(Q\).

The exact audits give:

| \(n\) | component size | component type |
|---:|---:|---|
| 6 | 1 | point |
| 8 | 2 | interval |
| 10 | 5 | pentagon |
| 12 | 14 | three-dimensional associahedron |

## Number of physical roads

There are \(p^2\) pairs of opposite-color vertices. Of these, \(2p\) are
boundary edges. Therefore the number of physical diagonals is

\[
\boxed{
r_{2p}=p(p-2).}
\]

The exact values are

\[
r_6=3,\qquad
r_8=8,\qquad
r_{10}=15,\qquad
r_{12}=24.
\]

These are distinct factorization labels and cannot be quotiented by a polygon
symmetry without merging physical divisors.

## Exact rank-one fiber theorem

Fix a physical diagonal \(D\). It cuts the \(2p\)-gon into even polygons of
sizes

\[
2a,\qquad2b,
\qquad
a+b=p+1.
\]

A triangulation has exact physical core \(\{D\}\) precisely when its
restrictions to the two cut polygons are zero-core triangulations. The
rank-one fiber therefore factorizes as a graph:

\[
\boxed{
\mathcal F_{\{D\}}
\cong
\mathcal Z_{2a}\square\mathcal Z_{2b},
}
\]

where

\[
\mathcal Z_4=Q
\]

and, for \(q\ge3\),

\[
\mathcal Z_{2q}
=
\operatorname{Ass}(q)\sqcup\operatorname{Ass}(q).
\]

Consequently,

\[
\boxed{
|\mathcal F_{\{D\}}|
=
4C_{a-2}C_{b-2}.}
\]

Let

\[
c(4)=1,
\qquad
c(2q)=2\quad(q\ge3).
\]

Then

\[
\boxed{
|\pi_0\mathcal F_{\{D\}}|
=
c(2a)c(2b).}
\]

This formula explains all previously puzzling one-core fibers:

- \(4+4\): one connected component;
- \(4+(2b\ge6)\): two components;
- \((2a\ge6)+(2b\ge6)\): four components.

The marked boundary itself is the full product of the ordinary triangulation
graphs of the two cut polygons. The exact link sizes at all chord orbits
through twelve points agree with this Cartesian product.

## Incidence from the global polarity sheets

A flip from a zero-core triangulation to core \(\{D\}\) chooses one
triangulation of each parity subpolygon on the two sides of \(D\). For each
global polarity sheet, the number of raw flip incidences to its compatible
rank-one component is

\[
\boxed{
\mu_D=C_{a-2}C_{b-2}.}
\]

The two global sheets behave as follows.

### The exceptional \(4+4\) case

Both global polarity points meet the same connected rank-one fiber. After
contracting that fiber, it is a common road between the two centers.

Every six-point physical diagonal is of type \(4+4\). There are three of
them, so the canonical connected-fiber contraction is

\[
K_{2,3}.
\]

This is why the six-point suspension bridge is genuine.

### The \(4+(2b\ge6)\) case

The rank-one fiber has two connected components. One is incident only to the
plus global polarity component and the other only to the minus component.
Each carries \(\mu_D=C_{b-2}\) raw incidences.

At eight points every physical road is of type \(4+6\), with
\(\mu_D=1\). Hence the canonical rank-zero/rank-one contraction is

\[
\boxed{
K_{1,8}^{+}\sqcup K_{1,8}^{-},
}
\]

not \(K_{2,8}\).

Collapsing the two disconnected components over each common road label
produces \(K_{2,8}\) only as a coarse quotient. It is not a cellular
contraction through connected scalar fibers and its artificial cycles do not
represent scalar homology.

### The \((2a\ge6)+(2b\ge6)\) case

The rank-one fiber has four connected components. Two are incident to the two
uniform global polarity sheets. The other two are mixed regional-polarity
components and have no rank-zero incidence.

These components are not spurious. They are the first evidence that cutting
allows the two regions to carry independent polarity choices.

## Exact census through twelve points

The component and multiplicity structure is:

| \(n\) | cut type | \(\mu_D\) | rank-one components | incidence |
|---:|---:|---:|---:|---|
| 6 | \(4+4\) | 1 | 1 | common to \(+\) and \(-\) |
| 8 | \(4+6\) | 1 | 2 | one per global polarity |
| 10 | \(4+8\) | 2 | 2 | two parallel incidences per polarity |
| 10 | \(6+6\) | 1 | 4 | two incident, two mixed/orphan |
| 12 | \(4+10\) | 5 | 2 | five parallel incidences per polarity |
| 12 | \(6+8\) | 2 | 4 | two incident, two mixed/orphan |

Thus two new effects appear beyond eight points:

1. raw rank-zero/rank-one incidence becomes a multigraph;
2. some one-core components are invisible from rank zero.

Neither effect can be represented faithfully by a simple \(K_{2,r}\).

## Regional polarity cube

The component formula has a direct conceptual meaning. A partial physical
core \(P\) cuts the polygon into even regions. Every non-quadrilateral region
has two zero-core polarity components; a quadrilateral has one connected
zero-core interval.

If

\[
s(P)
=
\#\{R\in\mathcal R(P):|R|\ge6\},
\]

then the exact-core fiber has

\[
\boxed{
2^{s(P)}
}
\]

connected regional-polarity components, before retaining the associahedral
factor inside each component.

The two global polarity components are the uniform vertices

\[
(+,+,\ldots,+),
\qquad
(-,-,\ldots,-)
\]

of this regional polarity cube. Mixed sign choices are precisely the
components that first appear after cutting.

This is the correct replacement for the idea that one fixed polarity
\(S^0\) is carried unchanged through all core strata.

## Consequence for suspension

The abstract theorem

\[
\widetilde H_0(R_m)
\xrightarrow{\sim}
H_1(S^0*R_m)
\]

remains exact. What fails is its naive global application to the first two
ranks of every scalar core poset.

At six points, the rank-one fibers themselves identify the two polarity
charts and produce the suspension graph.

At \(n\ge8\), rank-one fibers do not identify the global polarity charts.
Therefore

\[
H_1(\operatorname{Inc}^{(0,1)}_{\rm sc})=0
\]

for the simple eight-point rank-zero/rank-one skeleton, and there is no
canonical global class \(\Gamma_8(c)\) at that stage.

Any polarity-odd transgression must instead use:

1. higher physical-core strata;
2. the complete regional-polarity component diagram;
3. its cellular or homotopy-colimit realization;
4. the occurrence coefficient cosheaf and its Gysin maps.

The known eight-point Möbius carrier is a natural candidate for the first
rank-two completion, but that identification requires a separate exact
incidence theorem.

Entry 69 executes this test. The identification is false: the honest
connected-fiber rank-two completion has homotopy type \(K_{2,12}\), indexed
by full quadrangulations, while the Möbius carrier is a distinct compatibility
and coherence complex. The marked-link \(K_{2,3}\) statement survives and is
upgraded to an explicit degree-shifting Gysin calculation.

## Marked Cut versus global deletion

A marked physical Cut on \(D\) does not delete a road from a global
\(K_{2,r}\). It passes to the exact-core fiber \(\mathcal F_{\{D\}}\), then
factors it into the two cut polygons.

At eight points this fiber is

\[
Q\square
\left(
\operatorname{Ass}(3)_+\sqcup\operatorname{Ass}(3)_-
\right).
\]

Quotienting the spectator quadrilateral interval \(Q\) leaves two local
polarity points. Compatible rank-two extensions of \(D\) become the three
physical roads of the hexagon factor. Their scalar fibers are connected after
the same spectator quotient. Thus every marked boundary recovers the genuine
local carrier

\[
K_{2,3}.
\]

This positive local result from entry 67 survives unchanged.

The lesson is:

\[
\boxed{
\text{Cut is link/Gysin plus regional factorization, not graph deletion.}
}
\]

## Relation to the coefficient cosheaf

Entries 27, 32, and 37 already construct a strict occurrence-level physical
coaction

\[
G_e:\mathcal L(P)\longrightarrow\mathcal L(P\cup\{e\}).
\]

The regional polarity theorem describes the component carrier beneath that
coaction. A suitable Ward object should now be built from local or relative
homology of the entire diagram

\[
P\longmapsto
\mathcal F_P,
\]

not by applying \(H_1\) independently to a guessed \(K_{2,r(P)}\).

The natural candidate is a derived pushforward or homotopy colimit over the
physical-core poset, with the regional polarity line as coefficients. In that
language:

- connected associahedral factors encode choices of scalar refinement;
- the regional polarity cube encodes descent sheets;
- physical Gysin maps add a region and its two-slot coefficient;
- higher core cells supply the coherences that can connect uniform polarity
  sectors.

This is precisely the stratified incidence calculus anticipated by the
normalization/conductor theorem of entry 66.

## Corrected next experiment

Enumerate the rank-two physical cores at eight points and retain:

1. every connected component of each exact-core fiber;
2. every incidence from the two rank-one components over its boundary roads;
3. the actual scalar square or higher faces filling those incidences;
4. the orientation local system under one-step rotation.

Then compute the homotopy type and integral cellular homology of the
rank-at-most-two diagram.

The decisive questions are:

\[
\text{Does it recover the known Möbius carrier?}
\]

and

\[
\text{Does its marked link at }D\text{ recover the local }K_{2,3}
\text{ suspension?}
\]

A positive result would locate the first higher transgression. A negative
result would show that still higher cores or the full associahedral envelope
are essential.

## Reproducible certificate

Run:

```text
rustc --edition=2021 -D warnings -O research/nima/check_global_polarity_incidence.rs -o "$env:TEMP\\marici-global-polarity.exe"
& "$env:TEMP\\marici-global-polarity.exe"
```

The certificate derives the zero-core components and their associahedral
graphs, the physical-road count, every rank-one product fiber, component
count, raw incidence multiplicity, chord-orbit classification, and marked
boundary product through \(n=12\).

## Internal dependencies

- Entries 21--27: scalar polarity transfer and core-filtered factorization.
- Entries 31, 32, and 37: the associahedral envelope and strict physical
  coaction.
- Entries 64--67: the suspension theorem, conductor relation, and the
  now-corrected eight-point coarse quotient.
- `research/nima/check_global_polarity_incidence.rs`: exact certificate.
