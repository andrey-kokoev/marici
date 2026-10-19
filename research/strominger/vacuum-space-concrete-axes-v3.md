# Empty structured space: concrete signed axes on three realization planes

The constant role assignment described here is superseded by
`vacuum-space-alternating-R-v4.md`: each R step now exchanges M/C roles while
preserving this concrete-label and central-plane presentation.

## Question

Operator correction: `[M|C]` was schema, not a literal axis label. Display M+, M-, C+, C-, with one signed pair repeated. Apply the full R=0 plane formatting to R=+1 and R=-1 as well.

## Claim boundary

The global MMC/CCM assignment remains unchanged. `axisLabel` now emits only the assigned role and sign. MMC yields M+, M-, M+, M-, C+, C-; CCM exchanges the repeated pair. Schema alternatives remain internal metadata, not visible axis labels.

R=-1,0,+1 now share full grid color/opacity, axis and arrow opacity, signed labels, and hexagonal boundaries. Selection changes the readout and origin marker, not the formatting of these three planes. Outer levels remain faint context unless selected; single-frame isolation still displays only its selected plane.

No geometry, rotational admission law or particle binding is inferred from the display correction. SCC obligations remain forward realization and typed-frame attachment transport.

## Disposition

Implemented in the existing owned experiment and both public mirrors. Route unchanged: `http://127.0.0.1:8766/experiments/particle-overlap-tetrahedron/vacuum.html`.

The fresh live-server run passes 41 checks (`structured_command_execution:e_24480_1792167336766351000_9`). Fresh SCC closure also passes all 41 (`structured_command_execution:e_24480_1792167347330575600_10`). Checks compare actual rendered plane-material colors/opacities, require the correct repeated concrete pair on each central plane under both XOR assignments, test selection-independent formatting, and verify all 18 signed labels are visible on mobile. The mobile scene screenshot was visually inspected.

Receipt and screenshots: `research/strominger/results/vacuum-space-viewer/`.
Checker: `node research/strominger/checkers/check_vacuum_space_viewer.mjs --base-url=http://127.0.0.1:8766`.
SCC: `python research/aspect/scc/scc.py check vacuum-space-viewer-v1 --verbose`.

Supersedes the bracketed-label presentation in `vacuum-space-typed-R-v2.md`. Changes remain uncommitted; no deployment performed.
