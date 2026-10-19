# Structured-space carrier selectors

Rejected placement implementation: the centered/scaled overlay below did not
meet the requirement that every vertex occupy a lattice node. It is replaced
by `vacuum-space-lattice-cells-v7.md`. The old receipt and screenshots are
archived under the `overlay-v6` names in the viewer results directory.

## Question

Operator requests selectors for lone proton, lone neutron, lone electron and all together in the existing realization-space viewer.

## Claim boundary

Five selectors are implemented: Empty, Lone proton, Lone neutron, Lone electron, All three. Empty remains the default. The display imports the existing `carrier.mjs#trial` four-vertex source bodies: C0/M0/C1[M1], M0/C1/M1[C2], and M1/C1/C2[M2]. The electron retains the previously declared reflected M2 source extension.

`vacuum-carriers.mjs` applies one common similarity to all source vertices, normalizing every tetrahedron edge to one and aligning the proton active face with the selected R frame. Lone views select subsets of that one embedding; they do not recenter individual bodies. Combined views therefore retain both exact shared faces and six distinct source vertex identities. Each body is a four-face volumetric mesh, with two directed window arrows, source vertex labels, wireframe and short P/N/E label.

This is a source-carrier display overlay, not a construction of lattice attachments or proof of natural support/persistence in the proposed vacuum. Changing selected R transports the displayed geometry by the declared frame embedding, retaining source identities; it does not derive a particle realization law. Plane visibility, role exchange and 60-degree frame controls remain independent.

## Disposition

Implemented at the unchanged route `/experiments/particle-overlap-tetrahedron/vacuum.html`. The owning publisher includes `vacuum-carriers.mjs` in both public mirrors.

The live run `structured_command_execution:e_24480_1792169188961560200_18` passed 70 checks. After shortening/separating the displayed P/N/E labels, final fresh SCC closure `structured_command_execution:e_24480_1792169261414646200_21` also passed all 70 with refreshed source hashes. Added tests verify each lone view has only its own four vertices and one nonzero-volume tetrahedron, actual rendered four-face buffers, unit edge lengths, unchanged positions between lone/combined modes, two shared faces, selection retention on R changes, Empty removal, invalid-choice rejection and mobile combined selection.

Receipt and screenshots: `research/strominger/results/vacuum-space-viewer/`, including `lone-proton-scene.png`, `lone-neutron-scene.png`, `lone-electron-scene.png`, `all-carriers-scene.png` and `all-carriers-mobile-scene.png`. Source snapshots were visually inspected.

Changes remain uncommitted; no deployment performed.
