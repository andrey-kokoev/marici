# Empty structured space: plane toggles and 60-degree realization steps

## Question

Operator requests: clicking an R label should toggle that plane between full rendering and the faint traces previously used on outer levels; support its node as well if label picking is unreliable. Rotation should be 60 degrees per realization step, not 30.

## Claim boundary

The default angular increment is now 60 degrees in the model, UI state and rotation control. The existing editable comparison controls remain. Per-step M/C exchange from v4 is preserved.

Each R label is an accessible toggle button. Clicking it or clicking within 14 CSS pixels of its origin node toggles that level's membership in `fullLevels`. Full rendering includes the stronger grid, axes/arrows, concrete signed labels and boundary; trace rendering retains the faint grid, axes and correspondence guides. Initially only R=-1,0,+1 are full. Selection does not override these choices. Visibility choices survive frame/role rebuilds, and the underlying geometry remains intact.

R labels are offset from the nodes to keep both click targets reachable. Enter/Space work on labels, and focus survives rebuilding. Pointer motion exceeding five CSS pixels marks an orbit drag and suppresses toggling, including when the pointer returns to its starting position. This is presentation control, not a physical process or selection law.

## Disposition

Implemented at the unchanged local viewer route `/experiments/particle-overlap-tetrahedron/vacuum.html`, with both public mirrors regenerated. Fresh live run `structured_command_execution:e_24480_1792168199513163800_15` and SCC closure `structured_command_execution:e_24480_1792168218070358900_16` each pass 58 checks. Added browser tests cover label hide/restore, outer-plane activation without selection, keyboard/focus, positive/negative node toggles, return-to-start orbit drag rejection, persistence, touch toggles, and 60-degree defaults.

Receipt and desktop/mobile screenshots: `research/strominger/results/vacuum-space-viewer/`. The mobile scene was inspected. Companion test command: `node research/strominger/checkers/check_vacuum_space_viewer.mjs --base-url=http://127.0.0.1:8766`.

Builds on `vacuum-space-alternating-R-v4.md`; changes remain uncommitted and not deployed.
