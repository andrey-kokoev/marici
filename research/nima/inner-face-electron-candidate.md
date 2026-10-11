# First trial: a minimal tetrahedral excitation on an inner proton-like face

## Hypothesis and scope

Test the operator's suggestion that the first electron appears as a smallest tetrahedron on an innermost face of the proton-like structure. Treat this as a proposed source-supported birth, not an established electron constituent of a proton.

Freshly inspected the existing proton-like viewer/source geometry, the geometry implementation, nested-electron work, and the actual retained tetrahedral constructor. The previous nested-electron syntax supplies an attachment operation; it does not derive this proposed birth.

## Explicit geometric trial

The viewer's source is an eight-vertex, twelve-triangle boundary: four tetrahedral corners and four face centers. For an interior-cell trial, cone its triangles to the symmetry-fixed center O. This adds a center and twelve tetrahedra. The source used such cone volumes in its volume calculation, but did not thereby supply a WG particle-birth operation or assert twelve physical constituents.

Exact results:

- Each cone cell has volume 2/9; their total is 8/3.
- There are eighteen internal faces, each already shared by two tetrahedra.
- The twelve cells form one orbit under the proper tetrahedral symmetry.
- The internal faces have symmetry orbits of sizes six and twelve.

Thus neither a unique bottom cell nor a unique inward face is selected by the unmarked symmetric geometry. An actual retained root or construction history could select one; a camera's downward direction cannot do that job. The trial does not assume that an arbitrary marked seed must preserve every symmetry of the unmarked body.

## Two meanings of popping up

### Attach a new cell to an existing internal face

Choose the internal triangle OAB as an explicit trial mark, not a selected physical location. Appending a tetrahedron with a fresh apex gives that triangle three incident tetrahedra. This is not an ordinary manifold-ball attachment at an interior face.

A WG incidence complex may allow such branching. Therefore the three-coface result is not a universal prohibition: it tells us that this interpretation needs a branched higher-cell source, rather than an unnoticed ordinary spatial subdivision. The apex position, geometry and birth rule remain unspecified.

### Refine the existing interior

Insert the centroid of OAB and perform its stellar subdivision. The two incident tetrahedra become six, giving sixteen tetrahedra in total. Each new tetrahedron has volume 2/27. The outside boundary and total volume are unchanged.

This constructs genuinely smaller cells on an internal face, but is a refinement of the same body, not yet a new independent excitation. Interior subdivision of one child gives four cells of volume 1/54; repeated subdivision can continue indefinitely. Thus geometric size alone supplies no first positive minimum under these trial operations. A discrete native constructor could impose a minimum, but that must be tested in its own grammar rather than inferred from this picture.

## What the existing native constructor actually does

`RetainedTetrahedralPackage.Cells.build` receives four vertices, all six edges and three triangle witnesses. It completes the fourth face together with tetrahedral coherence while preserving its input. Its WG generator retains an already completed package unchanged.

A single face is therefore not enough to invoke this constructor as a birth rule. With that face supplied, a new local tetrahedral request still needs an apex, three incident edges and two further horn-face witnesses. Successful horn completion would construct a coherence witness, not automatically a new spatial volume or electron.

No new arbitrary excitation dynamics or electron mass formula was inserted to bypass this input boundary.

## Outcome and next useful experiment

The hypothesis now has a concrete distinction to test:

1. **Subdivision:** smaller cells, no new demonstrated particle observable.
2. **Branched attachment:** a genuinely additional cell, requiring an admitted birth rule and retained interface.
3. **Native horn completion:** a generated higher witness, requiring actual horn inputs and a separate physical readout.

The most useful next step is the third: choose the inward face by the existing marked construction history and inspect whether its retained neighboring records supply the missing horn inputs without inventing a new apex or seeding the desired target. If so, distinguish the resulting package from a re-presentation of the old body before testing persistence, detachment, charge or spin.

This first test neither identifies an electron nor rules out a source-derived internal-boundary excitation. It rules out treating a smaller drawn tetrahedron, by itself, as the creation mechanism.

## Verification

`python research/nima/checkers/check_inner_face_tetrahedron_candidate.py` passes exact rational volume, incidence, symmetry-orbit, boundary and subdivision checks. Receipt: `results/inner-face-tetrahedron-candidate.json`. The existing viewer and historical geometry result were not changed. No new Agda proof or physical particle identification is claimed.
