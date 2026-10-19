# Reversible movement into phase modes and back

For proton/electron workflow commands and count conventions, see the
[arrow assembly guide](../../docs/arrow-assembly.md).

**Subsequent hostile test:** `centroid-admission-refinement-counterexample.md`
shows that cellwise centroid admission fails subdivision invariance. The exact
reversible dynamics below still pass; the admission hypothesis must be restricted
to canonical supporting facets or explicitly declared resolution-dependent.

## Exact step

For a source-generated facet, let v be its centroid relative to the common
fixed center. For each supplied linearized isometry R, calculate its exact
finite order m and let zeta be a primitive m-th root of unity. Define

    z_k = (1/m) sum_(t=0..m-1) zeta^(-k*t) R^t v.
    advance: z_k -> zeta^k z_k.
    decode: sum_k z_k = v; after advance, sum_k zeta^k z_k = Rv.

All operations use exact rational cyclotomic arithmetic. No floating-point
threshold decides whether a mode is present. The k=0 channel is retained, not
deleted. Advancing with inverse phases reverses the step.

For several generators, re-encode at every step; do not assume they share one
eigenbasis. The demonstrated schedule uses the supplied generator list in order
and repeats it. This is a spectral implementation of the supplied source action,
not a newly derived force law or a uniquely selected physical clock.

Implementation: `checkers/evolve_relative_geometry_modes.py`.

## Source records contain no neutron exclusion

- Proton: `inputs/relative-proton.json`.
- Neutron: **`inputs/mode-neutron.json`**, both seed roles are plain `carrier`.
- Electron: `inputs/relative-electron.json`.

The old explicitly protected neutron source remains separately available for
comparison. The new neutron input contains neither rim exclusions nor target
faces. Its two interface channels arise because all their nonzero-frequency
centroid modes vanish. Proton/electron attachment-pole records remain retained
source data.

## Checked result

| Source | Moving centroid channels | Fixed centroid channels | Generator orders | Return under the declared list schedule |
|---|---:|---:|---|---:|
| Proton | 4 | 0 | 3,3 | 6 individual generator applications |
| Neutron | 6 | 2 | 3 | 3 applications |
| Electron | 5 | 0 | 5 | 5 applications |

These periods follow from the already supplied actions and schedule. They do
not establish the earlier conjectured electron-three/proton-five physical
periods. Nor are these cell channels the historical 1836 coefficient arrows.

An active facet has a nonzero k!=0 mode under at least one generator. This
exactly recovers the same marked target geometries and subdivisions as the
previous centroid-displacement test. The two neutron caps remain stored as
fixed centroid channels, not erased geometric cells.

## Verification

`checkers/check_relative_geometry_mode_motion.py` freshly checks:

- encode/decode identity for every facet and generator;
- phase advancement equals the actual source isometry;
- inverse phases recover the prior state;
- conjugate pairing of modes;
- pairwise mode orthogonality in the supplied metric and exact energy equality;
- every step of the reversed scheduled history, not just the final return;
- exact target distances, cells, subdivisions, center and attachment marks;
- covariance under rational changes of frame and translations;
- primitive-root arithmetic and Fourier cancellation for orders 1 through 12.

**Loss control:** deleting the fixed mode prevents recovery of both neutron cap
centroids. Retention is mathematically necessary for reversibility.

**Resolution control:** every cap has moving corners even though its centroid
is fixed. Thus the distinction is at the declared centroid-channel resolution,
not a claim that the entire cap has no dynamics. Changing the state to include
all labelled corners would make all eight facets carry some moving data.

### Commands

    python research/voevodsky/checkers/evolve_relative_geometry_modes.py --source research/voevodsky/inputs/mode-neutron.json --output research/voevodsky/results/mode-motion-neutron.json
    python research/voevodsky/checkers/check_relative_geometry_mode_motion.py

Fresh run passed. Receipts:

- `results/relative_geometry_mode_motion.json`: independent comparisons, controls,
  source/implementation hashes.
- `results/mode-motion-proton.json`, `mode-motion-neutron.json`,
  `mode-motion-electron.json`: exact encoded modes, all source facet records,
  selected geometry, and complete finite centroid traces.

## Remaining question

There is now an explicit reversible movement procedure. What remains conjectural
is why **centroid-mode support** should select the assembled cell carrier. This
choice reproduces the three targets without manual neutron exclusions, but is
not yet derived from the primitive WG source or the stored coefficient protocol.

## Energy-accounting bridge

`geometric-phase-energy-bridge.md` now reconstructs the existing proton/belt
triangle modes, native Hamiltonians and seam projectors from the full retained
geometry with explicit native adapters, and connects them to the existing
persistent-occupation controls. Centroid-only data lose chirality; the electron
five-cycle does not preserve its existing spinor attachment cell. Thus this is
a checked partial bridge, not a new shared three-species energy law.
