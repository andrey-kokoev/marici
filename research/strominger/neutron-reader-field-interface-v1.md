# A local belt-to-N-reader field interface

## Construction

The N reader's two active boundary faces are `buv` (incoming) and `cuv`
(outgoing). Split each into three centroid-edge patches. Two internal in-plane
component labels per patch give a 12-coordinate reader field.

Each of the native belt's three adjacent-face pairs has exactly this patch
incidence: two triangles sharing an edge, six centroid-edge patches. Choose
a marked map from the reference pair to `buv/cuv`, taking its shared edge to
`uv`, and transport that map by the belt's native C3 rotation for the other
pairs. All three ordered patch lists then agree slot by slot.

These are explicit affine/barycentric chart attachments. Components retain
the source's co-moving plane-frame labels and inner product. They are not
silently interpreted as Euclidean tangent components of the target faces.

## Exact native field interface

For the 36-coordinate belt field, define averaging and replication:

```
A(y)_i = (y_i + y_(i+12) + y_(i+24))/3
J(x)   = (x,x,x).
```

Give the reader field metric three times that of one belt sector. Then exact
full-matrix checks establish:

```
AJ = I_12
A* = J
JA = G
AL = P_reader A
LJ = J P_reader
N  = J P_reader A.
```

Here P_reader is the source-derived rank-one local mode of one twelve-slot
sector. Thus G is exactly the operation of descending to the co-moving reader
field and lifting back; N additionally selects its geometric cyclic mode.

No amplitudes are fitted. A has a 24-dimensional kernel: general unaligned
belt information remains in the original field and is not reconstructible
from the reader alone. J is an isometric lift for the stated metrics.

## Chart sewing is nontrivial

The three chart maps disagree on six shared-vertex occurrences when treated
as maps into one fixed marked tetrahedron. All completions of their pairwise
shared-vertex identifications to tetrahedral vertex permutations were tested:
two choices per overlap, eight combinations total. None has identity loop
monodromy.

Requiring each completion to be an even vertex permutation selects one choice
per overlap. In the documented reference marking its loop monodromy is

```
b <-> u,  c <-> v.
```

It has order two and exchanges the selected two reader faces with the other
two tetrahedral faces. This is a combinatorial marked-chart result, not a
physical spin phase or a proof that one belt circuit advances realization.
The even-permutation convention is explicit; it is not independently derived
as the physical sewing law. No triple-overlap condition is presumed where
there is no common source vertex.

Consequently the field interface is a co-moving local description, not a
single global identification of all belt vertices with four fixed reader
vertices. A geometric frame/transition record must be retained.

## Metric boundary

The source adjacent-face-pair distances are not proportional to those of the
marked N tetrahedron in any of the 24 saved T metric cases under the chosen
binding. The attachment is affine, not a metric similarity. Retaining the
internal source metric makes the operator interface exact, but identifying it
with the spatial tangent metric would require a further justified field map.

## Disposition

There is now a concrete local N-reader field, marked geometric chart maps and
an exact descent/lift factorization of the native N operators. A globally
sewn metric field over T, compatible with the P interface and all native
marked transports, remains unconstructed.

```sh
python research/strominger/checkers/check_neutron_reader_field_interface.py
```

Evidence: `results/neutron-reader-field-interface/verification.json`.
Production/viewer unchanged.
