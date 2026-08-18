---
authors:
  - marici.Benincasa
date: 2026-08-17
---
# The Five Omitted Base-Point Coordinates Are Gauge Variables, Not Canonical Connection Entries

## Question

Entry 385 proposed testing the five omitted columns
[
3,4,5,6,7
]
at elliptic base points with the frozen marked lattice
[
(2,1,1;0,0,0,0).
]
This assumes that those columns are uniquely defined by the cohomological
reduction. Test that assumption before assigning valuations.

## Frozen diagnostic

Use the same source reduction engine and the two (x=1) base-point
representatives
[
[0:1:0]leftrightarrow(0,2),
qquad
[2:1:0]leftrightarrow(2,0).
]
For each point inspect:

- both point-blowup charts;
- both (u)- and (v)-derivative systems;
- source rows (0,1,2) and the double-pole row (8);
- exceptional directions (2,3,7,13,21);
- normal samples (31,32,47,61,85).

No free coordinate is set to zero and then called canonical. A coefficient is
declared fixed only when the reduction equations determine it independently
of every free exact-lift variable.

## Result

At both base-point representatives and for every tested row, the nonfixed
column mask is
[
oxed{248}.
]
Since
[
248=2^3+2^4+2^5+2^6+2^7,
]
the nonfixed columns are exactly
[
oxed{{3,4,5,6,7}}.
]
The complementary columns
[
oxed{{0,1,2,8,9,10,11}}
]
are fixed throughout the census. These are precisely the canonical
seven-coordinate projection tested in Entries 382--385.

Thus the five omitted quantities vary with the exact-lift choice. Their
individual poles or denominators are not invariants of the quotient
Gauss--Manin connection.

## Verdict

The proposed next test from Entry 385 is rejected as ill-typed:
[
oxed{	ext{one cannot demand logarithmicity of columns }3,dots,7
	ext{ before specifying a source-defined splitting.}}
]
This does not prove that no canonical splitting exists. It proves only that
the current reduction equations do not supply one and that the ordinary RREF
choice of zero free variables would be an unmotivated splitting.

The surviving statement is
[
oxed{	ext{the seven-column quotient is the complete fixed coordinate
subsystem in the tested twelve-column reduction.}}
]

## Classification

| Datum | Classification |
|---|---|
| columns (0,1,2,8,9,10,11) | canonical quotient coefficient data |
| columns (3,dots,7) | exact-lift gauge variables |
| choice of free-variable section | additional coefficient splitting datum |
| new support divisor | not tested or required here |
| new carrier cell | none |

## Next falsifier

Replace coordinatewise pole tests by a gauge-invariant one. Freeze the affine
solution module of exact lifts and compute either:

1. the extension class of the five-dimensional gauge module over the
   seven-dimensional fixed quotient; or
2. its first nontrivial Fitting/Pluecker data after the base-point lattice
   ((2,1,1;0,0,0,0)).

The finite question is whether that invariant module is logarithmic over the
already frozen soft and Cayley--Menger tangent cones. A failure requiring a
new coefficient filtration is a coefficient-architecture failure. Only
support outside those cones is a carrier-level falsifier.

## Epistemic boundary

The census is exact over the working finite field and uniform over 50 sampled
blowup points per representative. It does not prove global nonexistence of a
geometric splitting, compute the extension class, or address the physical
relative chain.

## Evidence

- `research/benincasa/marici-gm/src/bin/marked_tangency_support.rs`;
- `research/benincasa/exact-lift-gauge-noncanonicity-certificate.json`;
- Entry 385.
