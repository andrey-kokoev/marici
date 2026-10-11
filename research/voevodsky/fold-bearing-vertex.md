# Iteration 3: a vertex with an actual inward-direction fiber

## What changed, and what did not

Iteration 2 found that the original depth pullback has only one point over the realized center. Its folds survive in a neighborhood, not in that literal point fiber.

This iteration constructs a **new** pullback with a resolved potential factor. It does not claim to have discovered a hidden sphere inside the old point or to have compressed the old object without changing it. The old realization and its full source witness remain retained as the blowdown target.

The host T and its realized barycenter q are unchanged. The potential tetrahedron C still supplies all 24 barycentric inward-fold flags. Write B=sd(boundary Delta^3); B is the direction sphere, with 14 vertices, 36 edges and 24 triangles. Completing each boundary flag with the original body barycenter recovers its full inward-fold flag.

## 1. Resolve the potential center without erasing its directions

Replace the potential factor by

```text
C_hat = [0,1] x B,
h_hat(t,v) = t.
```

The endpoint t=0 now retains the approach direction v. Inward contraction acts by

```text
(t,v) -> ((1-s)t, v).
```

Thus directions remain present even when the inward depth reaches zero. The original potential complex is recovered through the explicit radial blowdown

```text
beta_C(t,v) = (1-t)b + t v,
b = (1/4,1/4,1/4,1/4).
```

All of {0} x B maps to b. Off t=0 this map is invertible onto C minus its center. It is a resolution, not an isomorphism: C_hat has sphere homology, while C is a ball.

## 2. The actual new interface square

Keep the original host map h_T(x)=1-3 min(x_i) and form

```text
Q  -------> C_hat
|             |
v             v
T ---h_T----> [0,1].
```

Explicitly,

```text
Q = {(x,(t,v)): h_T(x)=t} = T x B.
p_T(x,v) = x,
p_hat(x,v) = (h_T(x),v).
```

These maps and the new pullback are PL. The stored triangulation orders the interval inward, 1 before 0, so the projections are simplicial on the actual retained product cells, not merely abstract continuous maps.

For arbitrary compatible PL maps a:X->T and d:X->C_hat, write d=(t,v). Compatibility gives t=h_T a. The unique mediator is z -> (a(z),v(z)). This is PL; both projections recover the input maps. Uniqueness follows from the ordered pair coordinates. This is the new square's universal property.

The literal fiber over the realized host vertex is now

```text
p_T^(-1)(q) = {q} x B = S2.
```

It contains all 24 potential boundary flags, with their retained completion to the body barycenter. This is an actual fiber, not just a root hash pointing to unrelated geometry.

### Counts

| Object | f-vector |
| --- | --- |
| Resolved potential C_hat | (28, 122, 168, 72) |
| New pullback Q | (98, 852, 2268, 2376, 864) |
| Fiber over q | (14, 36, 24) |

The new pullback is homeomorphic to D2 x S2 and has mod-2 Betti numbers (1,0,1,0,0). The fiber has (1,0,1). The 864 four-cells retain every host/potential flag pairing.

These are cell counts, not coefficient-transfer arrow costs.

## 3. Comparison with the old pullback: an explicit category boundary

The map to the old pullback P is

```text
beta_Q(x,v) = (x, (1-h_T(x))b + h_T(x)v).
```

Its image satisfies the original depth equality. Every point away from the center has a unique direction lift. At the center every direction maps to the same old vertex; no inverse direction can be inferred there.

**The radial blowdown is generally not PL in these finite product triangulations.** It is continuous semialgebraic. Along t=s and v(s)=(1-s)v0+s v1 its potential coordinate is

```text
(1-s)b + s v0 + s^2(v1-v0).
```

Taking v0=(1,0,0,0) and v1=(1/2,1/2,0,0) gives a nonzero quadratic coefficient. This restriction cannot be affine on any nonempty parameter interval, so no finite subdivision makes this radial map PL.

Accordingly, the new pullback's universal property is in PL spaces; the radial comparison diagram is in continuous semialgebraic spaces. The original PL maps also belong to that larger category. This distinction is retained in the packet, rather than silently treating the blowdown as a PL equivalence.

## 4. Belt and transport: what follows now?

The host has not changed. The six-panel belt still follows from its six vertex-edge-face flag sectors and a positive-depth truncation. Its number of panels remains a property of that flag convention, not an intrinsic particle count.

Keeping the potential directions does **not** force the previous odd sheet-swap. For every fixed v, the new space contains a disk section T x {v}. The six radial triangles in that disk still impose

```text
boundary_bit_i = radial_bit_i XOR radial_bit_(i+1).
```

Their sum is zero. Exhaustion of all 64 radial assignments again finds two extensions for all-zero boundary labels and no extension for a single odd boundary swap. All fourteen direction vertices have these actual disk sections in the stored complex.

So an everywhere flat two-sheet transport on Q cannot restrict to odd belt holonomy on such a section. Potential-center resolution alone does not remove the obstruction. A branch locus, nonflat transport, or removal/resolution of the host center would be a further change of construction, not a consequence of the maps already built.

## 5. The remaining semantic distinction

There is still **one host vertex q**, now carrying a sphere fiber. There is no longer just one ordinary vertex of Q above q: the fiber has fourteen vertices and their higher cells.

Thus this realizes “one visible host vertex retaining inward directions” as a fiber-bearing vertex. It does not satisfy the different demand “exactly one point of the total pullback, whose ordinary point fiber is simultaneously a sphere.” The original point realization and the resolved fiber-bearing realization are related by the explicitly lossy blowdown, not identified.

The fold grammar and depth interface remain declared hypotheses. This does not identify an electron or derive a neutron. A remaining executable obligation is to attach this direction-bearing interface to the selected proton triangle's actual typed coefficient frame, checking which alignments and fold records it preserves. Without that attachment map, no replacement H-1/H-2 coefficient-arrow counts are justified.

## Verification and retained artifacts

All 20 checks passed, including:

- fresh complete source verification;
- the new simplicial projection maps and commuting square;
- the exact exceptional fiber and all fold completions;
- mediators and unique off-center lifts at all 864 cell interiors;
- blowdown into the original pullback;
- inward contraction through depth zero;
- the non-PL comparison warning and flat-holonomy obstruction;
- honestly rehashed projection/fold mutations and complete serialized replay.

```text
python research/voevodsky/checkers/check_fold_bearing_vertex.py
```

- `research/voevodsky/checkers/check_fold_bearing_vertex.py`
- `research/voevodsky/results/fold_bearing_vertex_store.json`
- `research/voevodsky/results/fold_bearing_vertex.json`

Root: `f58a01fbb60d83f1bdb24c23f56c10f9f69d314a67a0ad17cfd49e41b846751e`.
