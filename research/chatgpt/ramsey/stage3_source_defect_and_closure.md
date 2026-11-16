# Stage 3 — Native seam discrepancy, reflection closure, and two carrier controls

Date: 2026-11-09  
Status: Exact free-group and finite incidence checks. Conditional mathematical constructions; no new Marici-native 2-cell constructor or Agda proof claimed.

## Question

Given the actual six-arrow Marici source, can we generate an initial green comparison without stipulating a filler? Does the reflected pair of red/blue triangles force a triangulated closure?

## Frozen source and prior results

Vertices `A,B,C,D`; independently labelled directed occurrences:

```
AB: A->B    BC: B->C    CA: C->A
AD: A->D    DB: D->B    BA: B->A
```

Sources:
- [ActualSeedEndpointTable.agda](https://github.com/andrey-kokoev/marici/blob/main/research/nima/agda/ActualSeedEndpointTable.agda)
- [SeedSeamPathComparisonBoundary.agda](https://github.com/andrey-kokoev/marici/blob/main/research/nima/agda/SeedSeamPathComparisonBoundary.agda)
- [SeedFaceObstruction.agda](https://github.com/andrey-kokoev/marici/blob/main/research/nima/agda/SeedFaceObstruction.agda)
- [Source graph free realization](https://github.com/andrey-kokoev/marici/blob/main/research/strominger/source-graph-free-realization-v1.md)
- [Two triangles sharing an edge](https://github.com/andrey-kokoev/marici/blob/main/research/nima/two-triangles-shared-edge-half-phase.md)

The source supplies directed endpoints and retained histories. It does **not** supply a 2-cell making `AB=AD·DB`, or a relation `BA=(AB)^-1`. The free geometric realization has six distinct 1-cells; reversing a geometric path is available there, but need not be an independently admitted source occurrence.

Its unique nonidentity graph automorphism is

```
rho: A<->B, C<->D; AB<->BA, BC<->AD, CA<->DB.
```

## Result 1: canonical nonzero comparison *boundary*

Let `p=AB` and `q=AD·DB`, parallel from A to B. Define their based geometric discrepancy

`delta_A = p q^-1 = AB·DB^-1·AD^-1`.

The reflected parallel pair is `BA`, `BC·CA` from B to A. Set

`delta_B = BA·CA^-1·BC^-1`.

These are canonically *constructed loops* in the free geometric realization. Neither is an equality filler. The already-proved native obstruction prevents promoting `delta_A` to identity without changing the model or providing new source-authorized structure.

Choose the tree `AB, AD, CA` and basis of the fundamental group of the free realization (all loops based at A):

```
x = AB·BC·CA
y = AD·DB·AB^-1
z = AB·BA
```

Then `pi_1 = F(x,y,z)`, a free group of rank 3, and

```
delta_A = y^-1
AB·delta_B·AB^-1 = z·x^-1
```

Both are nontrivial freely reduced words. Distinct retained paths remain distinguishable independently of the group reduction.

## Result 2: reflected defects are not independent generators

A geometric symmetry of the unbased source, `rho^2=id`, induces a *based* automorphism via the transporter `AB`:

`Phi(w)=AB·rho(w)·AB^-1`.

Exact free-group substitution gives

```
Phi(x)=z·y
Phi(y)=x·z^-1
Phi(z)=z
Phi^2(w)=z·w·z^-1
Phi(delta_A)=AB·delta_B·AB^-1=z·x^-1
```

This produces the mirrored discrepancy from the first one without supplying a second independent rule. However, `Phi^2` equals conjugation by a retained return loop, not the strict identity as a based map. The central point `z=AB·BA` must not be discarded.

If, **as an additional premise**, one adjoins a face killing `delta_A` and requires reflection stability, the smallest normal closure contains `y` and `z·x^-1`. Its quotient group is

`F(x,y,z)/<<y,z·x^-1>>  =  Z`, with `x=z`, `y=1`.

One comparison alone leaves a free group of rank 2 and is not stable under reflection. The reflected pair leaves the return loop `z`; even this *forced quotient* does not achieve a simply connected closure.

## Result 3: a source-theoretic no-go via equivariant effects

Let every fiber be `Z`. Each edge `e` acts by reversible translation `t -> t + w_e`. Make the point-reflection action on values `t->-t`; equivariance requires `w_{rho(e)}=-w_e`.

Assign `w_AB=k`, `w_AD=a`, `w_DB=b` and reflected weights accordingly. Then

```
D_forward = k-a-b
D_reflected = -D_forward
```

Two explicit models with all operations reversible, reflected, and compatible with path composition:

| `k,a,b` | Forward discrepancy | Reflected discrepancy |
|---|---:|---:|
| `2,1,1` | 0 | 0 |
| `3,1,1` | 1 | -1 |

Therefore **incidence + point-reflection covariance + invertible effects + associative continuation** do not logically force equality of the two paths. A source-derived equality would fail in the second model. The canonical defect, not its vanishing, is derivable.

## Result 4: conditional 2-sphere from filled triangles

Strengthen the input: R and B are already actual 2-cells with boundary words

```
R: AB BC CA
B: AD DB BA
```

In the six-**distinct-edge** free realization there are exactly four simple 3-edge cycles, up to reversing and rotating each boundary word:

```
R:   AB BC CA
B:   AD DB BA
G1:  AB DB^-1 AD^-1
G2:  BA CA^-1 BC^-1
```

Require a closed orientable 2-dimensional Δ-complex, no new 0- or 1-cells, and that every 1-cell be incident to exactly two triangular 2-cells. Also require every vertex link to be connected and circular. Both G1 and G2 are forced: each of the six edges initially belongs to exactly one R/B face, and only those two new distinct triangular cycles fill all remaining edge incidences. Doubling R and B also saturates edges, but fails the link condition at A and B.

Verification: `V=4`, `E=6`, `F=4`, `chi=2`; each edge has two oppositely oriented face incidences, and every vertex link is a circle. Hence the connected orientable closed surface is `S^2`. The cellwise reflection pairs every vertex, edge and face without fixed cells, so the quotient is `RP^2`.

**Scope:** This is a Δ-complex with distinct edge occurrences: there are two pairs of triangular 2-cells having identical *vertex triples* but different 1-cell supports. It is not an abstract simplicial complex on the four displayed vertex labels; it can be subdivided into one. These triangles and their fillers are not native output of the seed; the filled-R/B and closure premises are explicit. An affine straight-simplex realization with four antipodal-labelled vertices would be degenerate, because the vertex set has only two opposite pairs and spans at most a plane.

## Carrier negative control: identify BA with AB reversed

If, instead, BA is represented by the **same geometric support** as AB with opposite direction, the underlying graph has five undirected 1-cells. Filled R and B now share an edge and form a disk (`V=4,E=5,F=2`). There are no unused existing 3-edge cycles that can complete a distinct-facet, closed simplicial sphere.

Adding the new `CD` edge and triangles `ACD` and `BCD` produces the combinatorial boundary of a tetrahedron: `V=4,E=6,F=4`, `chi=2`. Its vertex-exchange involution `(AB)(CD)` has fixed edge midpoints, so the quotient is a sphere with two order-two orbifold points, not `RP^2`. In a nondegenerate tetrahedron embedding that involution is a half-turn, **not** Euclidean point reflection. With the four original vertices constrained to literal antipodal pairs, all vertices are coplanar and any straight tetrahedron is degenerate.

Thus the carrier distinction — independent `AB` and `BA` paths vs opposite directions of one geometric support — materially changes both G and the quotient topology. The actual source retains the occurrence distinction and does not authorize collapsing it.

## Decision and next discriminator

1. Take as input either **filled R/B 2-simplices** or only **source-admitted directed occurrences**; do not silently switch.
2. Decide whether G generates *comparison boundary*, *response-valued equality*, *new cells*, or an *obstruction*. These are distinct types.
3. Construct the first local rule that produces an actual comparison **2-cell** or a justified nonvanishing obstruction, with no independent `alpha` parameter. Reflection will transport it to its mate.
4. Require stability under every admitted continuation, then test the first asymmetric branch. Only afterward ask whether the resulting filled complex is always a manifold or whether the closure rule is an additional premise.
5. For an actual 3D convex point-reflected polytope, use at least three independent antipodal vertex pairs; the minimal candidate is the six-vertex octahedron, not a four-vertex tetrahedron.

No Ramsey theorem or 3D-manifold theorem follows at this stage. No repo edits or new Agda compilation were made.

## Reproduction

Run `python check_stage3_defect.py`. The script uses the Python standard library and emits `stage3_defect_receipt.json`. It checks source path typing, automorphism, free-word reduction, based action and twisted square, translation countermodels, the four triangle-cycle census, face incidence, vertex links, orientation cancellation, duplicate-face negative control, and support-identified carrier control.
