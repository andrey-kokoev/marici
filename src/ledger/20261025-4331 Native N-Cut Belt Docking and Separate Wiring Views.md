---
author: marici.Strominger
title: Native N-Cut Belt Docking and Separate Wiring Views
description: A native tetrahedral–octahedral belt docks to single-cell N-tip cuts without scaling; geometry and expanded wiring views retain distinct meanings.
---

# 4331 — Native N-Cut Belt Docking and Separate Wiring Views

**[Open the viewer](/experiments/native-belt/index.html?preset=native-belt)** · [Controls and verification boundaries](/experiments/native-belt-guide) · [Construction gallery](/experiments/)

## Subsequent viewer revision

The current Geometry view uses E-assigned replacements at the two former N tips and opposite-vertex alignment of the belt. A staggered native middle extension now has **32 P + 32 E exposed faces**, supported by 20 tetrahedra and 14 whole octahedra. Parents meet its poles at their E tips; this is vertex contact, not the original face docking described below. Wiring has subsequently been rebuilt as the actual native cell dual: **384 nodes (176 P, 126 N, 82 E)**, **792 shared-face links**, and **2 separately typed tip-contact links**. The former 64-arrow diagram is historical reference only. Node counts differ from Geometry-view exposed-face counts; neither supplies a transport map or physical particle identification. [Native wiring contract and tests](https://github.com/andrey-kokoev/marici/blob/main/research/strominger/native-belt-wiring.md). [Extension construction and checks](https://github.com/andrey-kokoev/marici/blob/main/research/strominger/belt-middle-extension.md).

## Original reference: geometric attachment

The belt consists of **8 tetrahedra and 6 whole octahedra** selected from the native ESD7 cellulation. Its boundary has 18 vertices, 48 edges and 32 unit triangles. Rigid placement preserves the parent unit edge length.

An intact N-facing parent has no correctly oriented boundary triangle for the axial belt patch. The selected construction instead removes **one unit tetrahedral N tip from each displayed parent**. The newly exposed face of its whole-octahedron neighbor matches the central unit triangle of the corresponding four-triangle belt patch. This is not the previously considered two-layer cut of four tetrahedra and one octahedron.

The coordinate check finds a maximum matching error below 2e-15. Every retained parent vertex and every belt vertex lie in opposite supporting half-spaces at the attachment face; therefore their cell interiors cannot overlap. Each displayed parent has 174 cells. The removed tip records and all 175 native occurrence records per parent remain available; a display cut does not erase the native fiber.

## Two presentations, not two constructions

**Geometry** shows the rigidly docked cells. Every belt triangle has an opaque P/E color from the native tetrahedral-orientation convention. Thick white borders mark the declared **inside-N / N-less sector**; this is a display convention, not an assertion that the native octahedra have disappeared.

**Wiring** expands axial layer spacing by 2.5 and transverse node spacing by 1.8, translating the parents outward for clearance. These are diagram coordinates, not stretched cells or new physical lengths. The graph identities and links are unchanged. Both views use screen-space V-label placement; V₁ and V₂ labels are suppressed in this belt assembly.

## Scope

This verifies geometric face attachment and non-overlap for the specified native subcomplex. It does **not** establish a full native field-transport map, common global lattice-phase registration, mechanical stability, particle identification, binding energy, or a physical evolution law. P/E face colors and normalized symbolic wiring are not substitutes for those missing contracts.

## Durable verification

- [Gluing packet](https://github.com/andrey-kokoev/marici/blob/main/research/strominger/belt-parent-gluing.md) and [V-label mechanics](https://github.com/andrey-kokoev/marici/blob/main/research/strominger/vertex-label-positioning.md).
- [Native construction](https://github.com/andrey-kokoev/marici/blob/main/research/realization-tower/belt-octahedral-surface.mjs) and [single-tip docking checker](https://github.com/andrey-kokoev/marici/blob/main/research/realization-tower/belt-N-cap-docking.mjs).
- `node --test tests/belt*.test.mjs tests/central-belt*.test.mjs tests/complex-visibility.test.mjs tests/vertex-label-layout.test.mjs` checks cell incidence, rigid lengths, face matching, half-spaces, retained records, coloring, diagram separation and label layout.
- `node scripts/test-neutron-belt.mjs` exercises the built viewer, both views, layer visibility, persistence and hidden V-labels. `node scripts/test-cell-vertex-view.mjs` checks rotation anchors, zoom and pan.
- `node scripts/prepare-native-belt-viewer.mjs` publishes locally bundled assets and licenses. `node scripts/test-native-belt-publication.mjs` checks the public route, launch preset, gallery return and persisted view switch. Browser/publication checks verify delivery, not physical interpretation.

Fresh verification: **54 focused tests passed**, the public-viewer browser check passed, and `pnpm run build` completed website generation, VitePress rendering and Pagefind indexing. The build reports bundle-size warnings; no deployment is implied.

Sequence allocation: `seqclaim-8799003162917ea4fdaff2d2`, entry 4331, claimed by `marici.Strominger`. This allocation receipt is not a scientific-evidence admission; no new epistemic graph evidence event is claimed here.
