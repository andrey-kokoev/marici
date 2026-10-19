# Triangular-torus realization of the candidate rung-12 field

## Outcome

The construction passes as an **exact A4-equivariant encoding of the decorated twelve-channel field**. It preserves endpoint incidence, the supplied field metric, the named L/G/corner-cycle operators, and the existing ordered-parent comparison protocol.

The qualification matters: the metric and internal operations are **retained decorations**, not derived from the flat torus. The torus is not a tetrahedral cell complex, and its eight triangular faces do not implement the 137 comparison slots.

No native isotope geometry, double helix, separating sheet or physical torus is established by this result.

## Spatial construction

Use triangular-lattice coordinates with basis e1 and e2 at 60 degrees, and quotient by twice the lattice. Label the four vertex classes

```
A=00, B=10, C=01, D=11.
```

Orient edges along

```
d0=(1,0), d1=(-1,1), d2=(0,-1).
```

A channel is a pair (u,dj), with endpoint u+dj modulo two. Each class has one outgoing channel to every other class, so there are exactly twelve directed channels. This gives an explicit bijection with the existing twelve ordered endpoint pairs.

The 120-degree rotation has matrix

```
R = [-1 -1]
    [ 1  0].
```

It cycles d0,d1,d2 and preserves the triangular metric. The twelve affine maps

```
x -> R^k x + t,  k=0,1,2,  t in {00,10,01,11}
```

realize V4 semidirect C3. The checker verifies all 144 products, identifies their vertex permutations with the independently supplied proper tetrahedral A4 actions, and checks channel equivariance.

This is a selected orientation-preserving subgroup of torus symmetries, not the full symmetry group of the unoriented tessellation. A 60-degree rotation does not preserve the chosen directed-edge convention. Inversion is invisible on the four vertex classes but remains nontrivial on the torus and its lifted directions.

The planar covering group is infinite: planar translations do not become order two until the spatial torus quotient is taken.

## Field and metric

Place the source's three complex corner coefficients on each directed channel, retaining the source positive fiber metric K3. The complete field is C12 tensor C3, with metric I12 tensor K3.

Under the endpoint bijection:

- L is the same rank-one component projector P on every channel;
- G averages each component over the twelve channels;
- C is the same named internal corner-cycle matrix on every channel.

All twelve torus actions preserve the metric and commute with these three operators. The checker also verifies the coordinate-realization square against the independently supplied native spatial-vector action:

```
U_native B = B U_torus.
```

Thus the internal coefficients are not being incorrectly treated as fixed Cartesian spatial vectors. B remains the source's actual arrow-dependent realization map.

The torus's flat two-dimensional positional metric is **not** identified with the complex field metric. G is a retained global averaging operation, not a nearest-neighbor torus rule. No intrinsic geometric derivation of K3, P or C is claimed.

## The two order-three operations are different

The spatial 120-degree rotation permutes channels and their endpoints. The named corner cycle acts inside each three-component channel.

The checker verifies that they are different operators. The spatial action is field-metric unitary; the supplied internal corner cycle is not. Sharing order three does not identify them or provide an admissible replacement for either.

## Reference and comparisons

A directed reference remains explicit. The A4 action transports reference choices; fixing one directed reference leaves only the identity in this endpoint A4 subgroup.

For all twelve reference choices, the torus field is passed through the existing comparison encoder and recovered exactly. All twelve group actions are checked for each reference, giving **144 ordered-parent comparison equivariance checks**.

The original 121 arrow-pair slots plus 16 state-pair slots are retained. They are not replaced by torus triangles or by arbitrary nearest-neighbor comparisons.

## Topology and lifted paths: the correspondence has limits

The toroidal triangular cellulation has

```
V=4, E=12, F=8,
Euler characteristic = 0,
Betti numbers = (1,2,1).
```

The checker constructs both boundary matrices, verifies boundary-of-boundary zero, and computes ranks 3 and 7 exactly. There are two distinct underlying edge classes between each unordered vertex pair; orienting them gives the two opposing endpoint channels. This is a cellulation with parallel edges, not a four-vertex simplicial triangulation.

The tetrahedral boundary instead has six edges, four faces and Euler characteristic two. There is no cell-complex isomorphism between these surfaces.

A further distinction is visible in a two-channel return. Traversing (u,dj) and then the channel from its endpoint back to u has lifted displacement **2*dj**, not zero. It closes on the torus but winds around it. The reverse-labelled channel is not geometric retracing of the first torus edge.

Consequently the endpoint bijection alone does not preserve arbitrary lifted-path homotopy or justify identifying torus loops with tetrahedral return paths. Any proposed native transport interpretation must explicitly retain the deck displacement or supply an appropriate lift rule.

## Realization history is not quotiented

Only the spatial lattice address is reduced modulo two. Realization origin, coefficient history and native transfer provenance are not torus coordinates and are not identified periodically. This construction introduces no new phase-advance law.

## Reproduce

```
python research/strominger/checkers/check_toroidal_rung12.py
```

Outputs:

- `research/strominger/results/toroidal-rung12/verification.json`
- `research/strominger/results/toroidal-rung12/torus-channels.svg`

The checker freshly reruns the underlying exact field classification and refibration checks. The drawing is a fundamental parallelogram with repeated boundary labels, not an asserted embedding of a flat torus in three-dimensional space. Production rules and the viewer are unchanged.
