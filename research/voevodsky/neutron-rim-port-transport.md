# Neutron rim ports: exact matching and reversible transport trial

## Constructive follow-up

`native-rim-phase-adapter.md` (interaction iteration 2) supplies a reversible
local adapter retaining the norm deficit and a moving electron-port policy.
The original fixed-port and direct-isometry obstructions below remain valid;
full native operator/spinor coupling and collective closure are still open.

## Result

There is an exact **conditional boundary-interface construction**, with important
obstructions to interpreting it as native carrier coupling or physical flow.

1. Match lower rim L0,L1,L2 to proton A,B,C.
2. Match upper rim U0,U1,U2 to electron A,B,C inside its ABCD attachment cell.
3. The raw source metrics do **not** match: rim edge squared is 3, while both
   target triangles have edge squared 8. The explicit neutron length scale
   sqrt(8/3) makes the full port Gram matrices agree.
4. Boundary label identification and detachment are exactly reversible when
   constituent provenance and the retained attachment-face records accompany them.
5. All six triangle bijections transport the full boundary Fourier record
   reversibly. Orientation reversal swaps the nontrivial mode indices.
6. The proton source group contains the required face-preserving three-cycle.
   The electron's supplied five-cycle does not preserve its ABC triangle or
   ABCD attachment cell under any nonidentity power.
7. Matching the edge does **not** match the native incident-panel phase mode:
   their squared norms differ even after the explicit metric scaling.

This is not a demonstrated bound state, passage through volumes, or automatic
conversion of a real spatial channel into an independent complex spatial region.

## Correction to the preceding discussion

The viewer `papers/witness-generators/proton-neutron-assembly.html` already has
an illustrative belt-between-tetrahedra arrangement: lower rim to proton ABC,
upper rim to electron ABC, with the scale sqrt(8/3) explicitly declared. The
previous conversational answer missed this existing geometric placement.

This test gives an exact source-metric and phase-interface audit of that idea.
It does not promote the viewer's isotope labels to physical identifications.

## Source and port conventions

The common proton source has metric with diagonal 8 and off-diagonal 4 in three
dimensions; take A,B,C as its unit-coordinate vertices and D as the origin.
The electron source uses the analogous four-dimensional metric, with A,B,C,D
unit-coordinate vertices and E the origin. Thus ABC lies in the retained ABCD
facet opposite the electron seed. These are explicit source-label conventions,
not an assumed vertex-ID match to every renderer frame.

The neutron coordinates and six panels come from
`results/four_six_center_cones.json`, with metric diag(3,1,1). The supplied action
comes from `inputs/mode-neutron.json`.

After multiplying the neutron metric by 8/3, the two-vector Gram matrix based
at either rim's vertex 0 equals the ABC Gram matrix. Consequently barycentric
coordinates give an affine isometry of each **two-dimensional port plane**.
No full-dimensional isometry from a 3D neutron carrier to a 4D electron carrier
is asserted. The overall scale is supplied, not a predicted physical length.

## Boundary attachment and detachment

Use the three non-ABC faces of the proton tetrahedron as a disk-like boundary
patch; use the three non-ABC faces of the electron's ABCD cell as another patch.
Attach them along the lower and upper rim loops, respectively. The resulting
boundary surface has

    V = 8, E = 18, F = 12, V-E+F = 2.

The checker verifies connectedness, two incident faces at every edge, opposite
edge orientations, and a single circular link at every vertex. This is a closed
sphere-type boundary surface.

It is a claim about these boundary patches, **not** the full pentachoron boundary
or the center-cone volume. In particular, no ordinary hollow tunnel or nonsingular
filled 3D interior follows from this surface construction.

Keep each face's constituent tag and both constituent attachment-face records.
A JSON serialization/replay test inverts the rim identifications, restores all
original patch faces, and restores the two full tetrahedral boundaries. Merely
forgetting which constituent supplied an identified vertex is not a reversible
operation.

## Real coordinates and complex boundary channels

For an ordered port triple x0,x1,x2, use omega^3=1 and

    z_k = (1/3) sum_i omega^(-ki) x_i,
    x_i = sum_k omega^(ki) z_k.

The checker works exactly in Q(omega). The coefficient-slot norm obeys

    sum_i |x_i|^2 = 3 sum_k |z_k|^2.

This is a declared boundary-coordinate transform, not an identification with the
native carrier coefficient protocol. It also applies componentwise to the actual
real corner coordinates. For real inputs, z1 and z2 are conjugate channels.

Every triangle permutation has the form pi(i)=a+s*i modulo 3, with s=+1 or -1.
The transported channel is

    z'_k = omega^(-ka) z_(s*k).

The tests cover all six permutations on a basis and an additional complex probe.
Reversing orientation exchanges k=1 and k=2; it is not in general complex
conjugation on arbitrary complex inputs, nor a derived charge-conjugation law.

Both rim centroids are fixed by the neutron rotation, but both rims' corner
records have nonzero moving channels. Discarding z0 loses a constant input.
There is therefore no demonstrated assignment of one hole to a real-only role
and the other to a complex-only role.

## Independent amplitudes need a retained mismatch channel

Geometric coincidence does not establish equality of two independent port
states x and y. For a reversible comparison retain both

    average = (x+y)/2,
    difference = (x-y)/2.

Then x=average+difference and y=average-difference, with

    ||x||^2 + ||y||^2 = 2(||average||^2 + ||difference||^2).

The six basis inputs are checked, as are encode/decode on both outputs. Dropping
the difference collapses nonzero inputs (x,-x) to the same average as vacuum.
Thus a lossless general interface needs the independent mismatch information;
an additional physical law could restrict states to difference=0, but geometric
identification alone does not impose it. The particular average/difference
implementation is a supplied reversible adapter, not the uniquely required one.

## Source-action compatibility: a real obstruction on the electron side

With Li mapped to A,B,C in index order, the neutron action induces

    A -> C -> B -> A

on the lower port. Enumerating the group generated by the two retained proton
source actions finds this face-preserving action. A chronological zero-indexed
generator word is [0,0,1,0]. This is a selectable generated action, not a claim
that the old proton generator-list schedule automatically performs it.

On the upper port the induced action is A -> B -> C -> A. The electron's supplied
source action is the five-cycle E -> A -> B -> C -> D -> E. Its group has no
nonidentity member preserving ABC, or even ABCD. Consequently the fixed upper
port does not intertwine a nontrivial neutron rotation with a power of that
supplied electron action.

A moving attachment port or an additional, justified electron operation could
change this result. Neither is silently added here. Existing five-cell spin
transport is a separate construction, not an automatic solution of this
particular fixed-rim matching problem.

## Native phase mismatch remains after geometric matching

For the native local triangle (F,a,b), use the existing geometric character

    mode = F - (a+b)/2 + i*sqrt(3)*(a-b)/2.

Its physical squared norm is

    |F-(a+b)/2|^2 + (3/4)|a-b|^2.

For a belt panel incident on the lower rim, after the same 8/3 metric scaling,
this equals **4198/675**. For either target ABC face it equals **20/3**.

Thus identifying the shared edge cannot be extended to an isometric equality
of these native local mode vectors. Their panel centroids and transverse geometry
differ. A normalization, projection, dilation or other native phase adapter would
be additional data with additional obligations; none is inferred from the
successful boundary-slot Fourier transport.

## Interpretation and next gate

The holes can consistently serve as **geometric boundary ports** in a declared
assembly. Boundary records can be transferred through real/complex coordinates
without information loss, and attachment can be undone when provenance is kept.

Not yet established:

- native phase/operator coupling across either rim;
- compatibility of a fixed upper port with the electron's supplied five-cycle;
- a holding, indication, binding, energy-exchange or physical transport function;
- connectivity of filled volumes or different real/complex roles for the two holes.

Next construct and test an explicit native phase adapter, retaining its mismatch
or auxiliary channels, and decide whether the electron port moves or requires
an additional admitted stabilizing action. These are concrete missing operations,
not reasons to repeat the already successful metric and boundary replay tests.

## Reproduction

```sh
python research/voevodsky/checkers/check_neutron_rim_port_transport.py
```

Passes. Receipt: `results/neutron_rim_port_transport.json`, with source hashes,
interface maps, induced actions, phase controls, native norm obstruction and
boundary-surface checks.
