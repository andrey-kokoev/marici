# T: geometric chart cycle and coefficient transport

## Direct identification test

Using the five abstract vertices in coefficient-reference order
`[a,b,u,v,c] = [C0/M2, M0, C1, M1, C2]`, the geometric cycle
`a->b->c->a` fixes u/v and permutes the selected facets P->N->E->P.
Its coordinate pullback is `[4,0,2,3,1]`, of order three.

The existing native five-coefficient transfers are

```
PN = [3,1,2,0,4]     (order 2)
NE = [0,4,2,3,1]     (order 2)
```

A single common basis conjugation preserves order, so it cannot turn that
coordinate cycle into either native permutation. Geometric-coordinate cycling
and native coefficient transport are different actions in this representation.
This only tests the direct/common-basis identification, not every possible
chart-dependent construction of T.

## A compatible chart-dependent transport

Retain a five-coordinate coefficient space over each presentation. The existing
maps define chart frames relative to P:

```
F_P = identity
F_N = PN
F_E = NE after PN = [3,4,2,0,1]
```

Transport from a chart A to B is `F_B after inverse(F_A)`. This exactly
reproduces PN and NE. Its E->P map is the explicitly inferred inverse composite.
All 27 composition triangles among P,N,E close exactly.

This is a flat coefficient bundle/transport model over the three presentations:
geometry specifies the facet, while a chart-dependent map carries coefficient
data. Coherence is guaranteed by the constructed frames; it is not an
independent derivation of those frames or native E->P dynamics.

## Metric transport

The original five-point metric is retained. Under the geometric facet cycle:

- P->N changes some edge lengths in all 24 examples;
- N->E changes some edge lengths in all 24;
- E->P preserves edge lengths in 8 and changes them in 16.

Thus these three facets support a chart construction with differing intrinsic
metrics. They are not three congruent orientations under a rigid order-three
rotation. Symmetrizing the metric would replace source geometry and was not done.

## Current form of the conjecture

A concrete candidate is:

1. A glued four-dimensional reference simplex T.
2. Three selected three-dimensional facet presentations, each setting a
   different barycentric coordinate to zero.
3. Full coefficient data carried by chart-dependent transitions.
4. An explicit seam occurrence transition for C0/M2 still to be supplied.

The assignment a=realization, b=M, c=C remains compatible with the tested
reversal but not derived by this calculation. Barycentric a has not been
identified with the integer realization-origin grading. The seam identifies
abstract reference vertices while its occurrences C0 and M2 have different
roles/indices; those distinctions must be transported, not erased.

No production/viewer changes.

```sh
node research/strominger/checkers/probe_T_transition_law.mjs
```

Evidence: `results/T-transition-law/verification.json`.
