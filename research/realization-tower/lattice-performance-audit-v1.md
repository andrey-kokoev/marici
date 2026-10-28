# Lattice viewer rendering audit

## Reproduced bottlenecks

Profiled default lattice, extent 6, and six-carrier helium at 1100x760, browser
DPR2, headless Chromium using SwiftShader. Instrumentation counts WebGL draws
and wraps application animation-frame callbacks. It does not measure physical
GPU frame times or claim a stable FPS on the operator's device.

| Mode | Draws/frame before | Draws/frame after | Median callback CPU ms before / after |
|---|---:|---:|---:|
| Default lattice | 100 | 32 | 1.3 / 0.4 |
| Extent 6 | 180 | 32 | 2.2 / 0.4 |
| Helium | 24 | 18 | 0.9 / 0.5 |

Pixel count in the test viewport decreased from 2,371,200 to 1,333,800
(43.75% less) by capping renderer DPR at 1.5 instead of 2. After optimization,
all sampled idle windows had zero callbacks and zero draws. Callback counts
during interaction depend on automation and scheduling; they are not FPS.

Receipts:
- [Before](results/lattice-ui/profile-before.json)
- [After](results/lattice-ui/profile-after.json)

## Changes

1. Four instanced plane-family meshes replace individual transparent disks.
   Double-sided transparent planes no longer render two passes each.
2. Transparent helium and interval surfaces also render in one pass.
3. The per-label loop no longer reads `host.clientWidth/clientHeight` after
   writing another label's positions. Viewport dimensions are cached on resize;
   labels use transform translations and one reusable projection vector.
4. Requests triggered inside rendering do not queue redundant frames.
5. Rebuild disposal explicitly releases InstancedMesh-owned GPU buffers as well
   as shared geometry/material resources.
6. Expensive extent/distance rebuilds commit on release or a 75 ms input pause.
   The before/after rotation profiles precede this final debounce-only change;
   it does not alter the geometry or per-frame draw count.

## Remaining limitations

- High-overlap transparency still consumes fill bandwidth. Family instancing
  reduces draw submission, not the number of visible plane fragments.
- Coloured intersecting transparent families and bodies have ordinary Three.js
  sorting limitations, not order-independent transparency.
- Topology rebuilds still take tens of milliseconds on the test machine.
  Their scheduling is improved; their computation is not claimed free.
- Selecting a constituent or changing construction mode still rebuilds that
  small overlay. Geometry is not rebuilt during camera rotation.
- Software GL is a reproducible diagnostic, not a substitute for testing the
  operator's actual browser, GPU and display.

Reproduce with `node scripts/profile-realization-lattice.mjs`.
Geometry, mouse/touch selection, camera drag, controls and helium visual
regressions are covered separately by `pnpm lattice:test`.
