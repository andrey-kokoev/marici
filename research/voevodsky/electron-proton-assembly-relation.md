# Electron/proton assembly: extension or refinement?

## Question

Test the proposed common growth sequence before assigning particle names to its stages. In particular, does the stored electron end at an open fan while the stored proton adds a cap and volume? Read the actual electron spinor and proton Merkle geometry stores, not the harmonized viewer stages.

## Exact source comparison

The electron's four stored normals correspond to all four faces ABC, ABD, ACD and BCD. Its source support is the complete tetrahedral boundary. The later five-vertex pentachoron visualization is a different, explicitly conditional geometric extension; this audit does not identify its extra faces with derived spinor degrees of freedom.

The proton store contains twelve oriented triangles (F_face,i,j), three per same outer face, where F_face is that face's centroid. For each oriented face (a,b,c), the subdivision chain is

    (F,a,b)+(F,b,c)+(F,c,a).

Its boundary equals the boundary of (a,b,c): radial internal edges cancel. The sum of these subdivisions agrees exactly with all twelve stored proton triangles, up to one global orientation convention. Both complete surface chains have zero boundary.

Thus the geometric relation already present is **a refinement of the same closed surface**, not an open electron surface capped by the proton. Refinement is not literal inclusion of simplicial face lists: one large face becomes a chain of three smaller faces with the same realized support and boundary.

## Separately test the open-to-closed proposal

Root at A and take the three incident faces ABC, ACD and ADB with consistent orientation. Their sum is an open disk with the three-edge boundary BCD. Attach the fourth face with cancelling orientation to obtain the closed tetrahedral boundary. Attaching a tetrahedral 3-cell is a further declared operation; a vanishing surface boundary alone does not create that filler.

This is a valid common growth prototype:

| Operation | Result |
|---|---|
| Retain root-to-branch arrows | Rooted skeleton |
| Add branch comparisons and their triangular witnesses | Three-face open fan |
| Attach the missing comparison face | Closed tetrahedral surface |
| Supply a volume witness | Filled tetrahedron |

These are not automatically the arity phases 1:1, 1:many, many:1, many:many. Source/target grouping and cell attachment remain different operations until a typed constructor connects them. Most importantly, the stored electron already includes the fourth face: it is not the intermediate three-face object.

## Coefficients do not follow from the support comparison

Electron local projectors satisfy sum P_i=2I and Tr(P_i P_j)=1/3 for i!=j. Their global encoder retains two independent components. Restricting that encoder to the three-face fan gives input Gram I-P_cap/2, with eigenvalues 1 and 1/2. It still has rank two. Thus capping the fan restores the original isometric normalization; it does not by itself turn a doublet into one coherent line.

The proton's stored collective selector has rank one. A lossless linear map from the electron's two-dimensional logical carrier into only that rank-one retained proton output cannot exist. A larger retained record, a changed representation or an explicitly information-losing selection could be constructed, but none follows merely by subdividing faces. This agrees with the earlier `geometry-selected-comparisons.md` audit, which found that the distinct face-local scalar views do not sew into one common global scalar view by restriction alone.

## Disposition

Neither proposed particle phase assignment is established by the current stores. The stopped-growth hypothesis survives as a new construction question, but not as a description of the existing electron/proton support pair.

The clean established comparison is:

- common oriented tetrahedral support;
- electron: four face-local spinor selections, with a coherent doublet;
- proton: twelve centroid-edge cyclic selections, with a coherent line;
- geometric refinement checked;
- source-faithful coefficient/transport adapter still missing.

A productive next experiment is to retain the rooted open-fan construction as a separately named prototype and test which completion or feedback operations the source supplies. Do not rename it electron solely because it appears earlier, or assume it becomes the stored proton when capped.

## Verify

    python research/voevodsky/checkers/check_electron_proton_assembly_relation.py

Receipt: `results/electron_proton_assembly_relation.json`. Fresh exact checks bind both stores, identify all electron face normals, reconstruct all proton triangles, verify facewise subdivision/boundary identities, and test the open-fan encoder Gram and local overlaps. The stored proton collective rank is read from its receipt, not independently re-derived by this checker. No physical particle identification or new dynamics is asserted.
