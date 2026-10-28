# Step back from the P-only-unwrapped ESD7 candidate

## What is actually asymmetric

`fibration-steps-v1.json` assigns five corner labels: **+P, −P, +N, −N, E**. E has no second signed corner. The carrier is already declared `face-glued-esd7-pair`.

Independently of those labels, the native ESD7 tetrahedral geometry has a boundary edge strip with **7 P-oriented and 6 E-oriented triangles**. The probe recovers this directly from geometric faces, without growth-rule assignments or E-tip overrides. Thus:

- the corner-state construction treats P and E differently;
- the tetrahedral termination also treats their native orientations differently;
- the first statement has not been proved to cause the second. The ESD7 geometry is an input to the current corner construction, not a derived consequence of it.

The prior viewer and its checked native wiring are left unchanged as reference data.

## An explicit geometric duality

Use the existing native lattice, but not its ESD7 envelope:

- lattice vertices: integer `q=(q0,q1,q2,q3)` with `sum(q)=1`;
- P tetrahedron: vertices `b-e_i`, where `sum(b)=2`;
- E tetrahedron: vertices `a+e_i`, where `sum(a)=0`;
- N octahedron: vertices `d-e_i-e_j`, `i<j`, where `sum(d)=3`.

Choose a native octahedron centre `c=(1/2,1/2,1/2,-1/2)`. The operation

`D(q)=2c-q`

is an exact lattice isometry and involution. It exchanges P and E tetrahedra, preserves octahedral kind, exchanges native P/E triangle orientations, and preserves face adjacency. This is geometric duality, **not yet a phase law on complete particle/fibre states**.

It cannot preserve a P-biased tetrahedral envelope. Requiring the sector to be invariant under D removes that particular bias without discarding individual P cells.

## Independent symmetric-sector family

Take whole native cells inside

`|q_i-c_i| <= r+1/2`, for integer `r>=0`.

This domain is an octahedron. Its edge length is `n=2r+1` native units. These coordinate bounds are an explicit new sector assumption, not a uniquely derived physical boundary condition. The generator imports neither ESD7 geometry nor corner assignments and has no target particle counts.

| Edge units | P cells | N cells | E cells | Surface P cells | Surface E cells | P faces | E faces |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 0 | 1 | 0 | 0 | 0 | 4 | 4 |
| 3 | 16 | 19 | 16 | 12 | 12 | 36 | 36 |
| 5 | 80 | 85 | 80 | 40 | 40 | 100 | 100 |
| 7 | 224 | 231 | 224 | 84 | 84 | 196 | 196 |

P/E equality follows from a witnessed cellwise involution, not from counting selected subsets or assigning extra weights. No existing cells are identified with one another or partially clipped.

### What happens at the edges

Every one of the twelve macro-edges meets two oppositely terminated faces:

- one incident strip: `n P, n−1 E`;
- the other incident strip: `n−1 P, n E`;
- both strips together: **`2n−1 P, 2n−1 E`**.

For n=7 this is **7/6 paired with 6/7**, or **13/13**. A single odd-length strip still has an endpoint excess. The new sector supplies its dual termination on the adjacent face instead of repeating the same bias. This does **not** turn the original thirteen-triangle strip into a balanced strip, nor remove exactly one P.

## Checks and limits

`tests/pe-symmetric-sector.test.mjs` checks the original asymmetric corner specification and 7/6 strip, then checks radii 0–3 for:

- exact integer lattice coordinates and whole-cell shapes;
- involutive cell and face duality, with P/E exchanged;
- face adjacency preserved under duality;
- equal P/E whole-cell, surface-cell and boundary-face counts;
- all twelve edge-strip pairs balanced;
- connected cell adjacency, no nonmanifold faces, closed boundary edges and Euler characteristic 2;
- total native cell volume equal to the enclosing octahedron volume.

Run:

```
node --test tests/pe-symmetric-sector.test.mjs
node scripts/probe-pe-symmetric-sector.mjs
```

The small sizes are a structural scan, not a fit to Pb-208. In particular, **80 P / 85 N / 80 E is not a nearly completed Pb model**: there is no admitted reason to add two charged cells or forty-one neutral cells.

Remaining work: derive a P/E-symmetric state construction upstream of the corner assignment; decide whether its admissible spatial sector is this octahedron or another invariant domain; establish a full-state duality/phase operation; only then consider physical inventory and attachments. The present probe supplies a tested geometric counterexample to the necessity of P-privileged ESD7 termination, not a replacement nuclear model.
