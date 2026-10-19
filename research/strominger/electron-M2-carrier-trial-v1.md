# Trial: electron M1 C1 C2 [M2]

Operator-specified candidate, following the corrected P/N carrier binding:

    P = C0 M0 C1 [M1]
    N = M0 C1 M1 [C2]
    E? = M1 C1 C2 [M2].

P/N share the full M0/C1/M1 face. N/E share the full M1/C1/C2 face. P/E share
only the C1/M1 edge. The electron window reverses the neutron's last edge,
M1→C1 instead of C1→M1, then proceeds to C2. It is not a plain sliding triple.

## Declared geometric construction

Retain the existing unfolded P/N coordinates without modification. Their N/E
face has plane -5x+y+z=5. Reflect N's opposite vertex M0=(1,-1,-1) through this
plane to create a NEW M2=(-31/9,-1/9,-1/9). This chooses a regular tetrahedral
attachment on the opposite side from the neutron; it is a trial construction,
not an inferred native particle operation or a physical C/M grading law.

All18 within-body edge occurrences have squared length8. Each body's absolute
volume is8/3. Adjacent apices are on opposite sides of their respective shared
face. Both C2 and M2 lie strictly on N's side of the P/N plane x+y+z=-1, whereas
P's interior is on the other side. Therefore the nonadjacent E/P interiors also
do not overlap. There are six distinct vertices and twelve unique body edges.

M2 is not M0 renamed, not C2 renamed and not one of the original five source
vertices. No global six-vertex equidistance, common simplex, physical lattice or
space-filling assertion is made. The original pentachoron and its identities
remain retained separately; its complete metric was not flattened into3D.

## Identity and admissibility limits

The existing generic spectral attachment covers the original three triangular
windows on FIVE retained source labels, with explicitly added closing seams
and declared frame comparisons. The E window remains M1/C1/C2, so its existing
spectral record/branch is still displayed. That record does NOT recover a sixth
M2 coefficient or establish the native electron constructor. M2 currently has
an inspectable geometric identity/provenance record only. Native E stage,
metric, preparation, reader and primitive-history squares remain to be attached.

## UI and verification

The P/N-only default is preserved. Use **Try electron [M₂]** or

http://127.0.0.1:8766/experiments/particle-overlap-tetrahedron/?view=lattice&geometry=carrier&electron=m2

Trial v4 displays three actual body meshes and six node labels, with an explicit
Electron trial card and bracketed M2 in selection details. M2 is clickable.
Switching back to P/N removes the third body, M2 and the electron controls.
Source: `demos/particle-overlap-tetrahedron/carrier.mjs`, exported `trial`.

    python research/aspect/scc/scc.py check particle-tetrahedral-carrier-viewer-v1 --verbose

The guard checks actual mesh buffers, distinct identity, exact shared faces,
regularity/volumes, non-overlap, unchanged original P/N source, scoped proof
labels, P/N↔trial switching, direct URL reload, desktop/mobile output and labels.
The two preexisting chart/identity viewer profiles remain separate regressions.
Receipt: `results/particle-carrier-viewer/verification.json`.
