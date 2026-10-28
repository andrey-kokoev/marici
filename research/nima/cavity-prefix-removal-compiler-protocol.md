# Frozen bounded test: full-port cavity prefix-removal compilation

## Question and scope

Does the actual component-level model of the retained three-round cavity implement the suffix-transported prefix-removal square on its complete optical carrier, with the correct port permutation and reversed factor order?

This is a conditional mathematical implementation comparison, not a physical control authorization, an interval encoding or a new proof of generic inverse-word algebra. SCC obligation: forward realization and route/coherencer compatibility. Imported linear optics and coherent access to all retained ports are explicit model assumptions. No measurement is requested.

## Frozen inputs

- `research/aspect/checkers/reciprocal_lossy_cavity_plant.py`: actual m1, m2, loss components and four-port product.
- `research/nima/checkers/check_physics_geometric_candidate.py`: actual `round_map(k)`, ten-mode labels, symmetric-power lift and factorial metric.
- `research/nima/physics-geometric-candidate-v1.md`: retained-port, preparation and number-sector scope.
- `research/nima/left-trim-suffix-transport-prior-review.md`: operator convention and existing noncommutation witness.

Use the frozen rational calibration and p=q=1. Do not change source coefficients, append modes or run foreign result writers.

## Construction to test

Extract the three actual four-port components. Embed each round using its existing labelled input slots and explicit output permutation: the component product outputs (y_r,y_t,x_next,y_e), whereas the retained round slots require (y_r,x_next,y_t,y_e). Compare the resulting full ten-mode matrix with `round_map(k)` on every input column, for k=0,1,2.

For each contiguous segment [i,j] of these rounds with i<j, set A=W_i and S=W_j ... W_(i+1). Construct D=S A^T S^T by reversing the actual component order and transposing the components, including inverse rewiring. Check the full matrix identity D(SA)=S independently of a symbolic cancellation shortcut. Retain original execution and appended correction as different words.

Check the induced action on all occupation basis columns in sectors N=0,1,2, with factorial metric; do not use the single prepared analyzer ray as a full-state certificate. Explain any all-sector extension by the previously declared symmetric-power composition theorem, not finite sampling alone. Detector events are excluded.

## Acceptance, hostiles and stopping rule

Accept this bounded comparison only if component/round reconstruction and correction squares agree exactly on all stated domains, source hashes remain stable and execution records are retained. Report any mismatch rather than changing conventions to force a pass.

Deliberate failures must include omitted output rewiring, unreversed inverse factor order, bare first-round inverse instead of suffix transport, and replacement of full-port recovery by a selected scalar/analyzer equality. Use a concrete lost-port collision if testing a discarded environment; do not model discard as an invertible transpose.

Stop after this comparison and its controls. A pass supplies a model-level compiled word conditional on inverse component controls. It does not supply access to emitted coherent modes, a physical reset/replay apparatus, a source-selected continuous generator, the interval [i,j] encoding, or either causal map. A failure rejects this specific implementation comparison, not optical realization generally.

## Execution status

At protocol freeze: specified, not executed. The subsequent execution and scoped disposition are recorded in `cavity-prefix-removal-compiler.md`; the broader physical realization cards remain blocked. The inputs, comparison and acceptance criteria above are unchanged.
