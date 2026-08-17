---
authors:
  - marici.Benincasa
date: 2026-08-17
---
# Relative Two-Cut Overlap Requires Bang Extension

## Question

Entry 357 constructed the common carrier curve but found no double pole in
the frozen physical form. This entry tests the independent geometric claim

\[
\boxed{
\text{the frozen relative pairs define an ordinary proper Gysin span across
the }(12,23)\text{ overlap.}
}
\]

The Cayley--Menger compactification, source divisors, occurrence labels, and
residue orientation are frozen. No opposite-sector denominator is inserted
into either physical summand.

## Pairwise boundary pullbacks

Let

\[
C=C_{12,23}=\{q_{\mathcal G_{12}}=q_{\mathcal G_{23}}=0\}
\]

be the double cover of Entry 357. At generic kinematics the nonconstant
pullbacks of the two sector boundaries are

\[
D_{12}|_C=\{b=y+z,\ b=x+y,\ b=x\},
\]

and

\[
D_{23}|_C=\{b=y+z,\ b=x+y,\ b=z\}.
\]

The first two points come from the shared one-site denominators. The unequal
points are the frozen lower occurrences

\[
b=x\quad(q_{\mathfrak g_{23}}),
\qquad
b=z\quad(q_{\mathfrak g_{12}}).
\]

The other restricted lower and one-site forms are generically nonzero
kinematic constants and create no fiber divisor.

Thus

\[
\boxed{D_{12}|_C\ne D_{23}|_C}
\]

away from special collision support such as (x=z).

## Proper-Gysin falsification

The minimal common restriction object is

\[
C^\circ=C\setminus(D_{12}|_C\cup D_{23}|_C).
\]

It maps to both sector opens

\[
U_{12}=S_{12}\setminus D_{12},
\qquad
U_{23}=S_{23}\setminus D_{23}.
\]

But (C^\circ\to U_{12}) is not closed: its closure contains the interior
point (b=z). Similarly, (C^\circ\to U_{23}) has the missing interior
point (b=x). Hence neither map is proper, and the proposed ordinary closed
Gysin span does not exist.

Making it proper would require adding (q_{\mathfrak g_{12}}) to the
sector-12 boundary and (q_{\mathfrak g_{23}}) to the sector-23 boundary.
Those forms exist globally, but they are absent from the corresponding
frozen source summands. Such cross-occurrence completion changes the
coefficient object and is not an admissible repair.

Therefore the tested claim is falsified.

## Surviving support-sensitive span

Non-properness is not absence of all correspondence. Each map

\[
p_{12}:C^\circ\to U_{12},
\qquad
p_{23}:C^\circ\to U_{23}
\]

is a canonical locally closed immersion. The support-sensitive calculus
therefore types the two extraordinary restrictions and their separate
extension-by-zero maps. It does **not** by itself type

\[
p_{23!}p_{12}^*:
D(U_{12})\longrightarrow D(U_{23})
\]

as a degree-zero cohomological correspondence: the counit on the target
requires (p_{23}^!), not (p_{23}^*). By codimension-one purity,

\[
p_{ij}^!\mathcal L_{ij}
\simeq p_{ij}^*\mathcal L_{ij}[-2](-1).
\]

On (C^\circ), the two extraordinary restrictions come from the same frozen
pre-residue double cover and are identified after the normal orientations
and their Koszul sign are retained. The resulting object maps *into* each
sector by the two localization counits. It is a common supported cospan, not
a transition map between the full sector objects.

This correction was forced by the subsequent coefficient type audit. It is
not a Čech restriction map, a map of the rank-twelve Gauss--Manin
connections, or a statement about the physical relative chain.

## Narrow result

\[
\boxed{
\text{ordinary proper Gysin overlap fails, while the locally closed overlap
supports a canonical extraordinary supported cospan.}
}
\]

The unequal occurrence marks do not force a new carrier stratum. They force
the use of support-sensitive functoriality and preserve sector-specific
coefficient boundaries.

## Classification

| Datum | Classification |
|---|---|
| common curve (C) | existing Cayley--Menger carrier |
| shared marks | existing source coefficient boundary |
| (b=x) versus (b=z) | occurrence-resolved sector coefficient data |
| union-open (C^\circ) | canonical source-boundary refinement |
| closed Gysin span | falsified |
| locally closed extraordinary cospan | canonically typed |
| full-sector transition arrow | not supplied |
| new carrier datum | none |

## Evidence

- `research/benincasa/marici-gm/src/bin/relative_pair_gysin_gate.rs`;
- `research/benincasa/relative-pair-gysin-gate-certificate.json`;
- Entries 188, 229, 356, and 357.

## Next falsifier

Determine whether the frozen source supplies a specialization or retraction
from either full rank-twelve object to the common extraordinary supported
object. Such a map, together with the opposite counit, would produce a
transition. Test whether any candidate:

1. has the frozen Koszul sign;
2. respects the rank-nine algebraic/rank-three marked filtration;
3. commutes with the parameter connection away from the union boundary; and
4. introduces no support beyond the five source-derived overlap marks.

Failure of the coefficient identification or connection compatibility would
leave only a carrier-level span. Success would supply the first genuine
cross-sector derived overlap arrow without converting the physical period
sum into a Čech cocycle.
