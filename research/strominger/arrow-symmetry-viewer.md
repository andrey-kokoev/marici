# Arrow, phase and process: a 3D viewer

## Question

Show process reversal as forward/reverse traversal through the arrow construction, replacing the process-phase ring. Operator instruction: “do that. and i don't need snapshot”. Active obligation: forward realization of this corrected display.

Open `C:/Users/andrey/src/marici/research/strominger/arrow-symmetry-viewer.html` directly in a browser; it requires no server or network access.

## Claim boundary

The display now has three actions:

- SU(2): the rotating gold arrow frame, retaining its quaternion/spinor lift;
- SO(2): the cyan complex-phase ring;
- Z2: reversal of the pink traversal through Input, L, G, N.

The first version's assignment of a second SO(2) to process was an assistant-added cyclic interpretation, not a consequence of the operator's forward/reverse flow. That assignment is withdrawn. The displayed direct product SU(2) × SO(2) × Z2 keeps reversal independent of arrow orientation and complex phase; coupling those actions would require a different composition law.

The process orders are

    forward: Input -> L -> G -> N,
    reverse: N -> G -> L -> Input.

The arrows indicating traversal flip on the same open path. Applying the flip twice restores its order and cursor position. Next stage, Play traversal and Restart expose the sequence; playback stops at the endpoint rather than wrapping around a circle. Traversal position is display state, not a phase or another group parameter.

L, G and N are the retained electron construction's stage names. Reverse traversal reads their order backwards; it does not implement inverses of the noninvertible projectors. The stage positions are diagram layout, not source-derived spatial coordinates. No physical time, mass or momentum is assigned by the display.

The spatial frame alone still identifies q and -q, so the separate quaternion/spinor readout is retained. A 360-degree turn returns the frame with opposite spinor; 720 degrees returns both. Camera controls change only the view.

## Disposition

Eighteen numerical geometry and actual-browser checks pass, including the binary involution, the shared forward/reverse path, double flip, independent factor controls, endpoint stopping, spinor return, mobile layout and offline execution. No image is generated or linked by this revision.

Reproduction:

```sh
node research/strominger/checkers/check_arrow_symmetry_viewer.mjs
```

Receipt: `research/strominger/results/arrow-symmetry-viewer.json`. These are implementation tests of the declared display, not a physical symmetry derivation.

Fresh headless Chromium execution: `structured_command_execution:e_41980_1791826191919110300_4`, exit code 0. No shared source or particle stores were modified.
