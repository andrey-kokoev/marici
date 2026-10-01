# Two paws sharing AD

Experiment: triangles ABC and AEF share the same leg AD. The six vertices initially carry seven undirected edges AB, AC, BC, AD, AE, AF, EF.

## Closure scope matters

Completion adds missing endpoint pairs witnessed by length-two paths in the pre-step graph. It retains the old edges and records the witnessing paths. It does not recursively use fresh edges within the step.

| Admitted paths | New edges | Final graph |
|---|---|---|
| Within each named paw only | BD, CD, DE, DF | Two K4 graphs sharing AD; 11 edges |
| Anywhere in the joined graph | Above plus BE, BF, CE, CF | K6; 15 edges |

Every added edge has a path through A. Therefore global completion reaches K6 in ONE step, not two. Both results are fixed points under their respective policies. Switching from local to global after one step adds the four cross edges, but that is a policy change, not evolution under the same local rule. Two disjoint paws would have no cross-component paths.

## Compatible shared-leg geometry

Use A=(0,0,0), B=(1,0,0), C=(1/2,sqrt(3)/2,0), D=(-1/2,sqrt(3)/2,0). Start E,F as B,C rotated by pi about AD. Both paws begin coplanar with unit structural edges. Rotate their bodies about AD by opposite 60-degree turns. Fold B and E about their respective AC and AF axes through opposite angles arccos(-1/3). A and D remain fixed throughout: the two bodies cannot independently move the same shared endpoint D.

All seven original edges remain unit. Each finished paw becomes a regular unit tetrahedron, with individual volume sqrt(2)/12. The four cross edges generally are NOT unit. K6 is a relationship graph in this embedding, not a regular five-simplex or six equidistant points in three dimensions. The displayed faces are explicit convex-hull realizations of the two K4 subgraphs; graph completion itself supplies no higher-dimensional fillers. Individual volumes are not asserted to sum to the union volume.

The rotation schedule, embedding and scope of admitted paths are declared choices. This test does not establish a general rotation-to-record conversion law or derive three-dimensional space.

## Artifacts and verification

- Offline interactive page: `demos/two-paws/index.html` (local/global scope selector).
- Checker: `checkers/check_two_paws.py`.
- Results: `results/two-paws.json`.
- Browser regression: `demos/two-paws/check.mjs`.

Fresh checks passed:

```
python research/nima/checkers/check_two_paws.py
node research/nima/demos/two-paws/check.mjs
```

Python checks exact finite edge sets, witnesses and fixed points, plus 101 geometric samples. Browser checks 101 samples, unit original edges, shared endpoints, endpoint coordinates against the independent Python Rodrigues calculation, individual volumes, scope controls, playback, offline loading and mobile layout.
