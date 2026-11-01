# Whole-assembly reflection construction from a regular 4-simplex

## Executed construction

The seed is the regular 4-simplex

\[
v_i=e_i-\tfrac15(1,1,1,1,1),\quad i=0,\ldots,4,
\]

in the hyperplane of R5 whose coordinate sum is zero. All ten squared edge lengths are 2. Every copy retains all five ordered vertices, its full affine map, parent copy and construction word.

The working triangular face is `(v0,v1,v2)`. The white edge is `[v0,v1]`. Both 120-degree rotations use `v0` as center, following variant A of `research/chatgpt/reflection_experiment_note.md`.

The complete accumulated assembly is retained and cloned at every operation:

| Stage | Retained histories | Distinct full 4-simplexes |
|---|---:|---:|
| Seed | 1 | 1 |
| White reflection | 2 | 2 |
| First 120-degree rotation | 4 | 4 |
| Computed outer-red reflection | 8 | 8 |
| Second 120-degree rotation | 16 | 14 |

The two coincident-copy pairs remain separate history records.

## Exact 4D coordinates and metric

Let `a=v1-v0`, `b=v2-v0`, and `g=(v0+v1+v2)/3`. Write

\[
x=v_0+ua+vb+s(v_3-g)+t(v_4-g).
\]

The last two basis vectors are orthogonal to the working plane. The seed coordinates are

```
v0 = (0,   0,   0, 0)
v1 = (1,   0,   0, 0)
v2 = (0,   1,   0, 0)
v3 = (1/3, 1/3, 1, 0)
v4 = (1/3, 1/3, 0, 1)
```

with Gram matrix

```
[ 2  1   0    0  ]
[ 1  2   0    0  ]
[ 0  0  4/3  1/3 ]
[ 0  0  1/3  4/3 ]
```

This metric, rather than an identity metric in the hidden coordinates, makes the five vertices a regular simplex. The checker verifies the exact isometric embedding into R5 and affine rank four.

## Operations and dynamically selected red edge

The working-plane maps, extended by identity on `(s,t)`, are

\[
W(u,v)=(u+v,-v),\qquad R(u,v)=(-u-v,u).
\]

After cloning the first rotated assembly, maximize `u+v` over **every vertex of every current full simplex**. The resulting support is `h=1`. Enumerating actual simplex edges on that support finds the geometric segment `[v1,v2]`.

The red reflection is therefore

\[
E(u,v)=(1-v,1-u).
\]

The supporting direction `(1,1)` is fixed by the protocol; the supporting level and actual edge occurrences are computed from the enlarged assembly. No final closing map is added.

All maps preserve the full Gram matrix. Both reflections square to identity, and both rotations have order three.

## Full-cell contacts and exact return

The fourteen distinct cells have a connected shared-edge graph with fourteen edges. Removing its tree branches leaves the actual six-cell central circuit.

For **every** shared edge, the checker derives its metric reflection and verifies that it maps all five vertices of one full cell to all five vertices of the next. Along the central circuit, the six affine maps compose to the exact identity:

\[
S_6S_5S_4S_3S_2S_1=\mathrm{id}.
\]

Both the linear part and translation return, and the composed inherited-vertex permutation fixes all five labels.

The full simplicial face counts are

\[
(f_0,f_1,f_2,f_3,f_4)=(43,126,140,70,14),
\]

with Euler characteristic 1.

Full-cell intersections are checked using an exact reduction: each hidden vertex projects strictly inside its working triangle, while distinct projected triangles have disjoint interiors. A shared boundary point therefore has zero hidden-coordinate weights. The full intersections are precisely the computed shared edges, vertices, or empty sets. The geometry is not identified by projection alone.

## Controls

- Changing the first rotation center to the white-edge midpoint produces a supporting corner but no red supporting edge. The requested red reflection is refused.
- Moving a hidden vertex leaves the planar projection unchanged but changes the full cell and destroys regularity.
- Removing the red reflection's translation fails to fix its supporting edge.

## Files and reproduction

- Construction: `regular_simplex_reflection.py`
- Checker: `checkers/check_regular_simplex_reflection.py`
- Exact receipt: `results/regular-simplex-reflection-v1/verification.json`
- Diagram: `results/regular-simplex-reflection-v1/assembly.svg`

The diagram shows the working-face assembly and the six-cell circuit alongside an oblique projection displaying all five vertices and ten edges of every full simplex. Floating point is used only for drawing; construction, intersections, metric checks and frame composition use exact rational arithmetic.

```sh
python research/strominger/checkers/check_regular_simplex_reflection.py
```
