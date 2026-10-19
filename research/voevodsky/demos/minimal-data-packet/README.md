# Proposed minimal data packet — interactive visual guide

Public URL: `/experiments/minimal-data-packet/`.

Authoritative files live here. `scripts/prepare-visualization-assets.mjs` copies the HTML, CSS, application, pure model, SVG preview and motivating sketch into `website/public/experiments/minimal-data-packet/`. It copies Three.js, OrbitControls and their MIT license from the existing local `research/nima/demos/paw-cycle/vendor/` directory. There are no CDN or remote runtime dependencies.

Entry 4322 (`src/ledger/20261014-4322 Configuration Coherence and the Candidate Constant 1836.md`) supplies the proposal, original sources and claim boundaries. The gallery and matter-atlas template link this separate foundational discussion without changing any catalogue record's scientific claims.

## Geometry and interaction

- Common mark at (0,0,0), positive endpoints a,b,c at the unit coordinate vectors.
- Signed continuation is supplied explicitly by the coordinate model.
- Choose an omitted direction, then a sign on each remaining direction: 3 × 2 × 2 sectors.
- Each square retains its omitted direction, signed axes, boundary and two ordered paths to a common corner.
- Select with a pointer or the keyboard-accessible dropdown; isolate the sector, toggle surfaces and negative endpoint guides, compare the two orders or trace a closed return.
- Playback moves markers along supplied boundaries. It does not execute an independently constructed recovery operation or produce a filling proof.
- The dimension slider changes counts only; the drawing remains n=3. In n dimensions the selected cells have dimension n−1, with n times 2^(n−1) sectors.
- The count is presented as three explicit products, with no auxiliary count symbols. At n=3 it evaluates to 108+432+1296=1836. Identification with actual source L/G/N arrows remains open.
- A second Three.js block below the lattice uses three unit rays toward vertices of a regular tetrahedron. The fourth ray is minus their sum and is a derived guide, not a new independent packet entry. The same sector records become twelve rhombi under an invertible linear coordinate change; central sheets are distinct from the tetrahedron's outer triangular faces.
- Both views share sector selection, path mode, progress and visibility controls while retaining independent orbit cameras. The dotted tetrahedral guide can be hidden separately. Sectors extend beyond it; it is not a clipping volume.
- `scene.js` is the shared renderer; `model.mjs` supplies the coordinate transformation. The map preserves incidences, compositions and the mark, rather than Euclidean angles.
- SVG selection/path playback and the full discussion remain available in both coordinate frames when WebGL fails.

The photograph is the operator-supplied motivating sketch, copied from `photo_2026-10-14_13-41-13.jpg`. It is not an input to any scientific checker.

## Electron-like n=2 trial

A third independent Three.js block at `#electron` displays a spin-ray sphere with a local two-direction signed cross, alongside the retained local phase. The source fixture is the existing four-face spinor, not a new physical particle model.

- `electron-model.mjs` decodes the exact trial's preparation, four source matrices and native projectors. Each discrete prefix is checked against its exact export. The current producer was replayed in isolation by the scientific trial without changing shared native artifacts.
- `electron.js` displays the source word U, V, U inverse, V inverse. Its composite is minus identity: the ray returns while the retained spinor changes sign. An optional phase-erased chart representative loses that distinction.
- The two base angles and retained initial phase can be varied separately. The phase circle uses an alpha/beta chart with an explicit pole switch; it is not a global trivialization or a physical orbit.
- The existing J encoder and its decoder are evaluated on every displayed spinor. Readouts retain signed bilinear amplitudes and all actual face blocks. Those source blocks are not identified with the proposed n=2 dependency sectors.
- Continuous rotation interpolation and the local tangent cross are supplied display data. The discrete source endpoints, not the interpolating paths or completed packet, are covered by the recorded exact trial.
- The build checks the trial's source hashes, then publishes `electron-trial.json` and the original native store. A bad display fixture fails independently of the two n=3 views.

Research scope: `research/voevodsky/electron-configuration-dimension-trial-v1.md`. In particular, two ray coordinates and a retained phase fiber are a candidate decomposition; a common dimension convention, source-grounded dependency ports and higher coherence remain to be established.

## Verification

```sh
python research/voevodsky/checkers/check_electron_configuration_dimension_trial.py
node research/voevodsky/checkers/prepare_packet_previews.mjs
node --test research/voevodsky/checkers/check_electron_packet_display.mjs
node --test research/voevodsky/checkers/check_minimal_data_packet_model.mjs
python research/matter/prepare_catalog_asset.py
pnpm run build
pnpm exec playwright test --config research/voevodsky/checkers/minimal-data-packet.playwright.config.mjs --reporter=list
```

The dedicated browser configuration serves the built site with a local static HTTP server, exercising the published files rather than a Vite-transformed source page. Tests check both desktop/mobile WebGL views, synchronized controls, counts, overflow, same-site dependencies, deliberate WebGL failure in both frames and atlas/gallery/ledger navigation. They verify transformed marker positions and common return endpoints. Additional desktop/mobile tests exercise the electron source word, sign-sensitive return, phase-erasure rival, preparation, decoder, SVG fallback and isolated source-mismatch rejection. Screenshots are written under `.ai/tmp/minimal-data-packet-browser/`.

The model checker verifies the twelve unique sectors, their unit-step closed boundaries, distinct intermediate points with a common corner, interpolation, the codimension-one formula, candidate product arithmetic, input bounds and reproducibility of the SVG preview. These are display/model checks, not a proof of the proposed capability theory, minimal independent witness count, proton identification or physical weight.

The additional model tests verify the tetrahedral rays' equal lengths and pairwise distances, zero barycenter, invertible basis, twelve rhombi and preservation of path interpolation.

Regenerate all three previews after changing a display model or its exported source fixture:

```sh
node research/voevodsky/checkers/prepare_packet_previews.mjs
```
