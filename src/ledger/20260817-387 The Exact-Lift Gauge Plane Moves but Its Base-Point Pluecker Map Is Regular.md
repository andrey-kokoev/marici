---
authors:
  - marici.Benincasa
date: 2026-08-17
---
# The Exact-Lift Gauge Plane Moves but Its Base-Point Pluecker Map Is Regular

## Question

Entry 386 showed that master coordinates
[
3,4,5,6,7
]
are not individually fixed by the reduction equations. Replace any choice of
affine section by the homogeneous solution module and ask whether its
gauge-invariant Grassmannian data develops new support at the two elliptic
base-point representatives.

## Frozen construction

For each reduction system
[
Amathbf c=mathbf b
]
take the homogeneous kernel (ker A), project it to the twelve master
coordinates, and row-reduce that projected subspace. This construction does
not set free exact-lift variables to zero and does not choose a lift of
(mathbf b).

The census keeps the Entry 386 source rows, derivative axes, blowup charts,
exceptional directions, and base-point representatives. For the Pluecker
normal fits it uses the 25 exact finite-field samples
[
t=31,ldots,55.
]

## Rank and pivot result

At both representatives, for every tested row, chart, axis, direction, and
normal sample, the projected gauge module has
[
oxed{operatorname{rank}G=2}.
]
Its stable RREF pivot mask is
[
24=2^3+2^4,
]
so the pivot columns are (3,4), and
[
oxed{p_{34}=1}
]
throughout the tested locus.

The five nonfixed master coordinates therefore do not constitute five
independent gauge directions. They carry a moving rank-two plane
[
G_Xsubsetlangle e_3,e_4,e_5,e_6,e_7angle.
]
The plane is genuinely nonconstant: each row produces 50 distinct sampled
Grassmannian points at each representative.

## Pluecker valuation result

In the stable chart (p_{34}
e0), evaluate the ten minors in the order
[
(p_{34},p_{35},p_{36},p_{37},p_{45},p_{46},p_{47},p_{56},p_{57},p_{67}).
]
Across both base points, both point-blowup charts, five exceptional
directions, both derivative axes, and rows (0,1,2,8), every normalized minor
has nonnegative ordinary normal valuation. The rowwise minima are
[
oxed{(0,0,0,0)}
]
at each representative, and every Pluecker pole mask is zero.

Thus the Grassmannian map moves but extends regularly through every tested
base-point direction:
[
oxed{G_X	ext{ is nonconstant, rank-stable, and Pluecker-regular at the
tested elliptic base points}.}
]

## Falsification verdict

The first invariant replacement for the rejected coordinatewise test does not
produce a new support divisor. Rank does not drop, the pivot minor remains a
unit, and no normalized Pluecker coordinate has a normal pole.

This is evidence for a nontrivial coefficient extension over the unchanged
carrier, not evidence for a new carrier stratum. It also rules out the simpler
claim that the gauge module is a constant coordinate plane.

## Classification

| Datum | Classification |
|---|---|
| moving rank-two plane (G_X) | coefficient extension data |
| stable unit minor (p_{34}) | local trivializing chart |
| normalized Pluecker functions | gauge-invariant coefficient data |
| new base-point support divisor | absent in the tested census |
| new carrier cell | not required |

## Next falsifier

Leave the base-point tangent cones and compute the rational Pluecker map on a
generic two-parameter patch. Factor the denominators and rank-drop minors
against the frozen soft, Cayley--Menger, and elliptic discriminant factors.

A residual irreducible denominator is first classified as coefficient
support. It becomes a carrier falsifier only if it cannot arise from the
frozen relative Gauss--Manin geometry. Separately, compute whether the moving
plane defines a nontrivial extension class; regularity alone does not imply a
canonical splitting.

## Epistemic boundary

This is an exact census over the working finite field, not a symbolic
factorization theorem. It establishes regularity only at the two tested
elliptic base-point representatives and does not address global discriminant
extension, integral lattices, or the physical relative chain.

## Evidence

- `research/benincasa/marici-gm/src/bin/marked_tangency_support.rs`;
- `research/benincasa/gauge-plucker-basepoint-census.json`;
- Entry 386.
