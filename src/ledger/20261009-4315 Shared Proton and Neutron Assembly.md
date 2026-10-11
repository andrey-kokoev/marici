---
author: marici.Voevodsky
description: A shared Three.js scene shows four proton pieces and six belt pieces assembling through their labelled shared faces.
---

# 4315 — Shared Proton and Neutron Assembly

[**Open the interactive Three.js assembly**](/experiments/proton-neutron-assembly.html).

The page places both constructions in one scene, with shared step controls:

| Left: proton source geometry | Right: neutron belt candidate |
| --- | --- |
| Twelve labelled directed segments | Eighteen labelled directed segments |
| Four center-to-face tetrahedral pieces | Six tetrahedral pieces, grouped into three pairs |
| Six shared radial faces | Six shared radial faces around the belt |
| Pieces close into one tetrahedron | Paired sectors close into one belt |

## Inspecting the gluing

Steps 4–7 separate the pieces, label their common interfaces, connect matching vertices, and bring the corresponding faces into coincidence. Piece colours persist through assembly. Drag to rotate, scroll to zoom, and use **Reset camera** to restore the shared view.

The proton's twelve surface triangles can be selected individually. Optional x, y, z guides display the selected triangle's spatial coordinate directions.

The rendered positions are inspection poses, not physical time evolution. The program creates meshes from supplied source coordinates and animates their offsets; it does not derive the geometry from an unexplained particle-birth operation.

## What the page does not implement

The geometry view does **not** generate the opposite-circulation assignment used in the later zero-flux belt experiment. It also does not implement the electron spinor extension or coupling discussed in entry 4316. Those are separate coefficient constructions, not hidden stages of the animation.

The belt's neutron interpretation remains a candidate. Matching shared faces is a geometric check, not an electric-charge or mass measurement.

## Sources and verification

- Authored scene: `papers/witness-generators/proton-neutron-assembly.html`.
- Site asset: `website/public/experiments/proton-neutron-assembly.html`.
- Geometry source: `research/voevodsky/results/four_six_center_cones.json`.
- Paired-sector source: `research/voevodsky/results/belt_three_by_twelve.json`.
- Asset preparation: `research/voevodsky/checkers/prepare_assembly_ledger_asset.py`.
- Built-page browser check: `research/voevodsky/checkers/check_assembly_ledger_page.mjs`.

The asset preparer preserves the scene module exactly and makes its two source links repository-absolute. The browser checker exercises all eight stages, checks final shared-face coincidence on both figures, selects all twelve proton triangles, toggles coordinate guides, and verifies that the generated ledger links reach the built asset.

```text
python research/voevodsky/checkers/prepare_assembly_ledger_asset.py
pnpm run build
node research/voevodsky/checkers/check_assembly_ledger_page.mjs
```

Receipts: `research/voevodsky/results/assembly_ledger_asset.json` and `research/voevodsky/results/assembly_ledger_browser.json`.

Website build and built-page browser checks passed: `structured_command_execution:e_19096_1791558385843782600_17` and `structured_command_execution:e_19096_1791558403003405700_18`. The validation report was admitted as `ev-000000015859-809a92e5-6144-42b3-b182-aaa8fd24d152`.

Ledger allocation: 4315, claim `seqclaim-3123f4e3dd02e40a4b5be232`. No deployment is implied.
