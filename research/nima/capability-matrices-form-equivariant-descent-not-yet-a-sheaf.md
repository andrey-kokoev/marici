# Capability matrices form equivariant descent data, not yet a cross-sector sheaf

Owner: `marici.Nima`

## Conjecture tested

Sector coefficient matrices might be local presentations of one sheaf-like
capability object.  The first hostile test uses the independently constructed
cosmological occurrence charts `G12`, `G23`, and `G31`.

## Positive result

The rank-26 quotient presentations have invertible cyclic transitions.  The
rank-seven annihilator planes satisfy exact contragredient transport from
`G12` to independently constructed `G23` and `G31` presentations.  Around the
three-cycle,

\[
T_{31,12}T_{23,31}T_{12,23}=I_{26}.
\]

Thus the matrices are not unrelated sector tables.  They are local frames of
one coefficient object with exact descent under relabelling.

## Typing correction

The source has no `G12`--`G23` double-pole overlap.  These are not ordinary
open sets with restriction maps, so calling the result a Čech sheaf on the
physical base would invent intersections that do not exist.

The correct current object is an **equivariant vector bundle on the cyclic
action groupoid**, or equivalently a representation/descent datum for the
labelled chart groupoid:

```text
local coefficient frames
  + invertible relabelling transitions
  + identity cocycle around the C3 orbit
  = equivariant descent object
```

This is sheaf-like in the broad sense that local presentations and transition
laws determine a global object, but the indexing category is a groupoid of
source relabellings rather than the open-set lattice of a topology.

## Why this is not yet a capability sheaf

The seven-plane is a coefficient annihilator/quotient.  No state-updating
successor operations have been attached to its elements.  Therefore the audit
establishes a coefficient bundle, not an operational capability bundle.

The upgrade requires three additional maps:

1. turn each local coefficient class into an admissible successor operation;
2. prove the chart transitions intertwine composition of those operations;
3. show diagnostic records restrict/select those local operations naturally.

Only then would policies become sections of a genuine capability stack or
sheaf.

## Cross-sector boundary

Nothing yet glues scattering, cosmology, flavor, and topology as charts of one
base.  Their source categories differ.  The defensible conjecture is that
each sector may carry its own capability fibration, and natural comparison
functors may later assemble them into a stack over a higher context category.
Calling the sectors themselves stalks of one matrix is premature.
