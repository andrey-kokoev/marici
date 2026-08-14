# The Eight-Point Polarity Link and the Failure of Arity-Indexed \(K_{2,m}\)

## Record

Date: 2026-08-13

Status: superseded in part by entry 68. The counterexample to
\(m=n/2\) and every marked-boundary \(K_{2,3}\) calculation remain exact.
The claimed global \(K_{2,8}\) requires collapsing each rank-one fiber even
though that fiber has two connected components. It is therefore a coarse
quotient, not the canonical scalar carrier. The raw rank-zero/rank-one
incidence is two disjoint eight-road stars; rank-two cells are required to
compare the polarities.

The eight-point scalar parity-core carrier does not canonically produce
\(K_{2,4}\). If connected components are forgotten and every exact rank-one
fiber is collapsed only by its physical-core label, one obtains the coarse
quotient \(K_{2,8}\). Entry 68 proves that the fibers are disconnected and
that this quotient is not the scalar homotopy carrier.

On each of the eight marked physical boundaries, the scalar presentation does
canonically restrict to

\[
\boxed{K_{2,3}},
\]

the established six-point suspension carrier. Thus \(m\) is neither an arity
index nor, globally, merely the number of rank-one labels. It is meaningful
only for a local connected incidence link.

## Scalar derivation of the global carrier

Let \(\operatorname{Tri}_8\) be the 132 octagon triangulations. A diagonal is
physical when its endpoints have opposite parity, and the parity core of a
triangulation \(T\) is

\[
\rho(T)=\{D\in T:D\text{ is physical}\}.
\]

The exact core-rank distribution is

\[
|\rho|=0:4,
\qquad
|\rho|=1:32,
\qquad
|\rho|=2:96.
\]

Retain scalar flip adjacency before making any target graph.

### Polarity components

The four zero-core scalar triangulations are not four independent polarity
centers. Under flips that remain in the zero-core fiber, they form exactly two
connected components of size two:

\[
\pi_0\{T:\rho(T)=\varnothing\}
=
\{\Pi_+,\Pi_-\}.
\]

One-step rotation exchanges the two components. They are the scalar-derived
polarity pair.

### Physical roads

There are exactly eight distinct rank-one physical cores,

\[
\{D\},
\qquad
D\in\mathcal D_{\rm phys}.
\]

Each rank-one core fiber contains four scalar triangulations, but it splits
into two connected interval components. For every polarity component
\(\Pi_\varepsilon\) and physical label \(D\), exactly one scalar flip enters
the matching interval component; it does not enter the component of the
opposite polarity.

Thus the canonical connected-fiber contraction is

\[
\boxed{
K_{1,8}^{+}\sqcup K_{1,8}^{-}.
}
\]

Collapsing both disconnected components over a common label \(D\) produces
the coarse quotient \(K_{2,8}\). The enumeration in this entry verifies that
quotient's labelled incidence and full dihedral covariance, but entry 68
shows why its cycles are not intrinsic scalar homology.

## Why the tempting \(K_{2,4}\) quotient is wrong

Half-turn rotation pairs the eight physical diagonals into four antipodal
orbits. Quotienting by those orbits would manufacture \(K_{2,4}\).

That quotient is not an admissible scalar-core contraction.

For every antipodal pair

\[
\{D,r^4D\},
\]

the pair itself is a genuine noncrossing rank-two physical core. Its exact
fiber contains eight scalar refinements. Identifying \(D\) with \(r^4D\)
therefore collapses a two-channel factorization stratum to rank one and merges
distinct physical poles.

Hence:

\[
\boxed{
K_{2,4}\text{ is a symmetry quotient, not the scalar incidence carrier.}
}
\]

The falsified statement is the guessed identification \(m=n/2\), not the
abstract all-\(m\) suspension theorem.

## Every physical boundary recovers \(K_{2,3}\)

Fix any physical diagonal \(D\). It cuts the octagon into a quadrilateral and
a hexagon. The scalar boundary has

\[
28
=
2\cdot14
\]

triangulations and factors as

\[
\operatorname{Tri}_4\times\operatorname{Tri}_6.
\]

The two quadrilateral triangulations are a spectator scalar flip. Quotienting
that factor leaves all fourteen hexagon triangulations.

Inside the fiber of the marked core \(\{D\}\):

1. the four scalar triangulations form two core-preserving flip components of
   size two;
2. precisely three additional physical diagonals are compatible with \(D\);
3. after quotienting the quadrilateral spectator, each polarity component
   meets each compatible extension once.

Thus the link of every marked physical core is

\[
\boxed{
\operatorname{Link}_{D}
\operatorname{Inc}_{\rm sc}(8)
\simeq
K_{2,3}.}
\]

The computation passes all 48 local center-road incidence checks across the
eight choices of \(D\).

This is an exact self-factorization statement at the carrier level: the
six-point suspension carrier is reconstructed on every eight-point physical
boundary.

## The Cut changes core rank

The local \(K_{2,3}\) is not obtained by deleting five roads from the
coarse \(K_{2,8}\) quotient, nor from either canonical global star.

Globally:

- the centers come from connected components of the rank-zero core fiber;
- the roads are rank-one physical cores.

After cutting on \(D\):

- the local centers come from connected components of the rank-one fiber over
  \(\{D\}\);
- the local roads are the compatible rank-two cores
  \(\{D,E\}\).

Thus a physical Cut shifts the filtration:

\[
\boxed{
(\text{rank }0\to\text{rank }1)
\quad\longmapsto\quad
(\text{rank }1\to\text{rank }2).
}
\]

This explains why marked-road deletion on an isolated \(K_{2,m}\) graph was
the wrong naturality test. The correct Cut is a link/Gysin operation on the
entire core-stratified scalar carrier.

## The core-incidence cosheaf

Let \(\mathcal P_n\) be the poset of partial physical cores. For
\(P\in\mathcal P_n\), let

\[
\mathcal F_P
=
\{T:\rho(T)=P\}
\]

be its exact-core scalar fiber, with scalar-flip incidence retained. Define

\[
\Pi(P)=\pi_0(\mathcal F_P)
\]

after quotienting only spectator scalar factors appropriate to the marked
boundary, and let

\[
\operatorname{Ext}(P)
=
\{e\notin P:P\cup\{e\}\in\mathcal P_n\}.
\]

A local suspension graph occurs only when the connected extension fibers
are incident to both local polarity components. The eight-point rank-zero
link fails this condition and is two disjoint stars. After marking a physical
channel \(D\) and quotienting the spectator quadrilateral factor, the
rank-one link does satisfy it:

\[
K_{\{D\}}=K_{2,3}.
\]

Thus a suspension object is a property of a typed local link, not a formal
construction from the set \(\operatorname{Ext}(P)\) alone. Entry 68 gives
the general regional-polarity component formula.

## Relation to the existing scalar coefficient cosheaf

Entries 27, 32, and 37 construct the occurrence-level coefficient system and
its strict physical Gysin maps

\[
G_e:\mathcal L(P)\longrightarrow\mathcal L(P\cup\{e\}).
\]

The new incidence result identifies the carrier on which the first two ranks
of those maps live. It suggests that the Ward circuit object should be a
local-homology coefficient system

\[
\mathcal W(P)
=
H_1(K_P)
\cong
\operatorname{sgn}_{\Pi(P)}
\otimes
\widetilde H_0(\operatorname{Ext}(P)).
\]

A physical Cut should compare \(\mathcal W(P)\) with
\(\mathcal W(P\cup\{e\})\) through the Gysin/link map, not through a graph
homomorphism \(K_{2,m}\to K_{2,m'}\).

That comparison has not yet been constructed. The exact eight-point data make
it finite and typed.

## Conceptual consequence

The all-\(m\) suspension theorem remains the correct local algebra:

\[
\widetilde H_0(R_m)
\xrightarrow{\sim}
H_1(S^0*R_m).
\]

What changes is its indexing. The scalar master does not present a single
arity-labelled sequence

\[
K_{2,3},K_{2,4},K_{2,5},\ldots.
\]

It presents a stratified family of local links whose valence is the number of
allowed one-step physical extensions at the current core.

This is a stronger fit to the carrier-first picture. Factorization does not
act on one fixed graph. It moves to a new link in a self-similar incidence
cosheaf.
## Next experiment

Retain connected components separately and add all rank-two physical-core
fibers. Determine whether their actual scalar faces connect the two global
stars through the known eight-triangle/four-square Möbius carrier, and whether
the link at every marked \(D\) is the local \(K_{2,3}\) suspension. This is the
correct higher-core Gysin test; there is no canonical
\(\Gamma_\varnothing:A_7\to H_1(K_{2,8})\) to compare.

## Reproducible certificate

Run:

```text
rustc --edition=2021 -D warnings -O research/nima/check_eight_point_polarity_carrier.rs -o "$env:TEMP\\marici-eight-point-polarity.exe"
& "$env:TEMP\\marici-eight-point-polarity.exe"
```

The certificate derives all triangulations and labelled incidences, constructs
the coarse \(K_{2,8}\) quotient, rejects the antipodal \(K_{2,4}\) quotient by
exhibiting genuine rank-two fibers, verifies full dihedral covariance, and
recovers \(K_{2,3}\) on all marked boundaries. Entry 68 and
`check_global_polarity_incidence.rs` supply the required connected-fiber
correction.

## Internal dependencies

- Entries 21--24: the six- and eight-point scalar presentation carriers.
- Entries 27, 32, and 37: the core-filtered scalar coefficient cosheaf and
  strict physical Cut coaction.
- Entries 64--66: suspension and cross-normal coefficient relations.
- Entry 68: regional polarity fibers and the correction of the coarse quotient.
- `research/nima/check_eight_point_polarity_carrier.rs`: labelled quotient and
  marked-boundary certificate.
- Entries 21--24: the six- and eight-point scalar presentation carriers.
- Entries 27, 32, and 37: the core-filtered scalar coefficient cosheaf and
  strict physical Cut coaction.
- Entries 64--66: suspension and cross-normal coefficient relations.
- `research/nima/check_eight_point_polarity_carrier.rs`: exact certificate.