# Deuterium endpoint coherence square

The explicit geometric half-turn G and reading reversal B commute exactly on
all 24 saved deuterium markings, under the carried-reference convention below.

```
Original -------- G --------> Turned
   |                             |
   B                             B
   |                             |
   v                             v
Reversed -------- G --------> Turned + reversed
```

The checker compares complete states, not merely their counts: coordinates,
reader frames, edge faces, entry/exit labels and full coefficient maps agree.
It also verifies G^2 = B^2 = identity and BGBG = identity. The endpoint actions
therefore realize a commuting pair of involutions (a Klein-four action on
these descriptions).

## Definitions and coefficient convention

G moves each labelled vertex to its partner's original endpoint:
C0/M2, M0/C2, C1/M1. Reader identity and coefficient reference labels travel
with the vertex and remain unchanged by G.

B exchanges the entry/exit boundary, reverses edge order, inverts coefficient
maps and transforms the reader frames by M/C exchange, index reflection i->2-i
and the established context-aware occurrence ordering.

The coefficient convention is essential: coefficients are carried in their
fixed five-slot reference basis during geometric motion. A coordinate-induced
basis action has not been derived. In particular the six-vertex interchange
exchanges C0 with M2, whereas M2 is outside the original five-slot reference.
It must not be silently treated as a permutation of those five named slots.

Thus this is a checked coherence square of decorated descriptions with
specified actions, not proof that every geometric reversal has this coefficient
representation. Clockwise/counterclockwise deformation paths share the same G
endpoint; their paths or interior topology are not identified by this result.

## Checks

- 24 complete squares commute exactly.
- 96 corner local frame/face audits pass.
- 48 corrupt-map/wrong-boundary controls are rejected.
- Both involutions and the square loop restore the exact original state.

The local audits do not remove the original native P regular-shape restriction
at the turned corners. Those corners use the moved/dual description rather
than claiming unchanged forward-generator admission. Full solid intersections
and isotopy remain outside this endpoint check. Production/viewer unchanged.

```sh
node research/strominger/checkers/check_deuterium_coherence_square.mjs
```

Evidence: `results/deuterium-coherence-square/verification.json`.
