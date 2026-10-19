# One electron–proton arrow and a fold-retaining potential attachment

## Constructed results

Two separately typed constructions are now executable:

1. A declared single coefficient arrow between the existing electron and proton
   carriers has a one-dimensional dark electron direction. An explicit pair
   of different admitted electron states has the same norm, persistent scalar
   relation and proton-facing amplitude.
2. The repaired potential interface, keeping mode separate from attachment
   position, retains **all 24 fold-chart interiors**. Its fibre at the realized
   host point is the whole potential direction sphere, not the two points of
   the old fixed-position rule.

These are not yet one physically identified electron–proton model. In
particular, the spinor-to-potential map and potential-mode-to-link map have not
been supplied. The calculation preserves that missing connection instead of
calling different uses of a complex coordinate the same interface.

## 1. The coefficient arrow is an explicit candidate

Use the existing proton 1,836-transfer store and electron 144-transfer spinor
store. The declared additional arrow is

    electron raw face0 spin0 -> proton raw AB:x, weight1.

Both endpoints are actual ports, but this choice and coefficient are a test
contract, not a source-selected physical hydrogen interaction. A one-way
coefficient arrow is not a Hermitian reciprocal Hamiltonian coupling.

The electron encoding is

    Jz=(P_0z,P_1z,P_2z,P_3z)/sqrt(2),
    J^dagger J=I2.

For exact arithmetic the checker uses E=sqrt(2)J, so E^dagger E=2I2; this does
not change the stored native operators or turn the encoding into norm gain.
Every native electron stage fixes the entire encoded doublet.

Let ell be the face0 spin0 row of E. Restricted to admitted electron inputs,
the arrow reads the scalar ell z, up to the displayed encoding normalization.
After proton projection its output is

    N_proton e_(AB,x) ell z.

This map has rank one because both factors are nonzero. It cannot transmit
the full two-complex-dimensional doublet in a single reading.

## 2. An exact same-link, same-norm electron pair

For ell=(ell_0,ell_1), define

    d=(-ell_1,ell_0),
    b=(conjugate(ell_0),conjugate(ell_1)),
    z_+=b+d, z_-=b-d.

Then

    ell d=0,
    b^dagger d=0,
    ||b||^2=||d||^2>0.

Thus z_+ and z_- differ but give the same link reading and the same norm. In
the actual stored face frame,

    ||z_+||^2=||z_-||^2=1+sqrt(3)/3,
    ell z_+=ell z_-=1/2+sqrt(3)/6.

The encoded states Ez_+ and Ez_- are fixed by L_e,G_e,N_e and remain distinct.
A common normalization makes both unit states without removing the ambiguity.

The persistent electron relation also agrees:

    B(z,Cz)=||z||^2,
    Cz=(-conjugate(z_1),conjugate(z_0)).

This independently verifies that the unit scalar relation is not a full
spinor decoder. It is not identified with the coefficient arrow, and Cz is
not an additional occupied electron.

## 3. What a second comparison would resolve

Existing binary tetrahedral spin actions supply exact logical matrices U.
For the source quaternion rotations i and j, each stacked observer

    [ell; ell U]

has rank two. The receipt stores both full 2-by-2 inverses. Consequently two
readings at the same fixed arrow, with one admitted source rotation applied
to retained/reproducible electron input, reconstruct the complete logical seed.

This explicitly extends the processing/readout permission; it is not a second
reading inferred to exist merely because the link is named an arrow. Holding
both state and observer in a passively changed frame adds no information.
The fixed coefficient row is not itself a rotation-invariant scalar; the
persistent norm relation is invariant and remains insufficient.

No physical state preparation, cloning, phase reference, rotation gate or
proton-to-electron reverse interaction is derived by this algebraic decoder.

## 4. Repair the potential attachment instead of discarding folds

The existing source atlas B is a refined tetrahedral boundary sphere with
20 vertices, 36 triangles and provenance in all 24 original fold-chart
interiors. Its map Gamma:B->Z is the existing source-bound selected-mode
projection into a complex mode disk.

The host T is the subdivided small triangle (F_ABC,A,B), with inward depth h_T.
The failed earlier rule imposed the additional equation

    z=j(x), where j(x)=L_AB applied to geometric position x.

That rule retained only eight fold interiors. The repair retains a separate
mode variable at the host interface:

    host:      T x Z -> I x Z, (x,z)->(h_T(x),z),
    potential: I x B -> I x Z, (t,v)->(t,Gamma(v)).

Their actual fibre product is

    R={((x,z),(t,v)):t=h_T(x), z=Gamma(v)}.

Eliminating only the determined variables t,z gives a canonical isomorphism

    R ~= T x B.

The forward map sends (x,v) to ((x,Gamma(v)),(h_T(x),v)); the inverse retains
(x,v). Hence every compatible pair has exactly one mediator, and location is
not forced to equal a coefficient value.

## 5. Full construction and verification of fold retention

The product is triangulated by the staircase construction with global vertex
orders. Each host triangle times each potential atlas triangle contributes
six four-simplices. All 1,296 maximal cells have exact affine dimension four.
The complete cell counts are

    vertices140, edges1266, triangles3396,
    tetrahedra3564, four-simplices1296.

Its mod-two Betti numbers are (1,0,1,0,0), consistent with a disk times a sphere.
This is an information-space dimension, not an extra physical spatial dimension.

The checker tests depth and the independently computed mode map against
simplicial interpolation at a generic rational point of every maximal cell.
All 24 original fold-chart interiors occur in active cells, not only as
retained source metadata.

At the host barycentre q, h_T(q)=0, the full potential boundary B remains:
20 vertices, 36 triangles and sphere homology (1,0,1). The earlier rule z=j(q)
gave only two compatible directions. Both results use the same source atlas;
the difference is the attachment equation.

The repaired atlas also retains an explicit pair of different potential
vertices with identical complex mode Gamma(v). Thus keeping the complex mode
alone still loses a realization witness; the fibre product keeps both v and
Gamma(v). The coefficient-link dark state and this fold-witness ambiguity are
different kernels and must not be conflated.

## What this says about adding the electron

The one coefficient arrow alone is insufficient to expose the admitted
electron doublet, even with its scalar unit relation known. Retaining the
potential-realization witnesses prevents a separate geometric loss, but does
not automatically repair the spinor link kernel.

A complete combined interface must now specify maps relating the retained
logical state z, the complex mode Gamma(v), the link scalar ell z, and the
witness v. Their compatibility must be verified; they cannot be identified
merely because two of them are complex-valued. The repaired product is
available for testing that map without the old forced-position constraint.

For unrestricted spinor amplitudes, a compact potential direction space and
its bounded mode cannot encode the unbounded scalar ell z through a fixed
continuous map alone. An amplitude/radial record or a normalized input domain
must be stated. This is a type/domain requirement, not a chosen mass or radius.

## Verification

    python research/voevodsky/checkers/check_proton_electron_single_link_potential.py

Checks pass for every native electron-stage intertwiner, the exact link kernel
and equal-norm pair, the persistent bilinear relation, both source-rotation
readout inverses, source-atlas integrity, every product-cell dimension and
interface map, complete topology, active fold owners and same-mode witness.
The first implementation compared list and tuple containers in a mode-map
assertion; that execution defect was corrected and the checker refrozen.
No source equation or acceptance condition was changed.

Current SCC fingerprint:
`261f013b5f83c823c204e6432581ecd4e31cccb342fe469c5152039d1c484bcc`.

Artifacts:

- `inputs/proton-electron-single-link-potential-v1.json`.
- `results/proton-electron-single-link-potential-v1.json`.
- `scc-models/proton-electron-single-link-potential-v1.json`.

Shared source stores are read-only. This is a candidate coefficient coupling
and a fold-retaining geometric attachment, not a physical bound-state model,
Hamiltonian conversion, charge/mass derivation or RH realization.
