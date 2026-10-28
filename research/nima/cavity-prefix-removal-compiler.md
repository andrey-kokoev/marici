# Full-port cavity prefix removal compiles in the declared component model

## Question, claim boundary and disposition

The frozen comparison in `cavity-prefix-removal-compiler-protocol.md` passes. The actual source mirror/loss components, correct output rewiring, reversed inverse words and retained three-round optical maps implement the suffix-transported correction on the full ten-mode carrier.

This is a **conditional component-model construction**. It assumes inverse component controls and coherent access to all retained modes. It does not provide apparatus access, an interval encoding, a physical-time comparison, or physical WG-I3. No detector is included.

SCC obligation: forward realization and route/coherencer compatibility. Owner-local manifest: `scc-models/cavity-prefix-removal-compiler.json`.

## Source extraction and port comparison

The checker imports both source modules without calling their main entrypoints. It extracts and executes only the assignment prefix defining Aspect's actual m1, m2, loss and dilation matrices. No foreign result writer runs. Source hashes are checked before and after the calculation.

Aspect's component product is loss*m2*m1, with output roles (y_r,y_t,x_next,y_e). The retained round requires (y_r,x_next,y_t,y_e). The explicit swap of positions 1 and 2 is therefore part of the compiled operation, not a cosmetic relabelling after comparison.

Embedding the ordered component list and that swap into slots (1+3k,0,2+3k,3+3k) exactly recovers the independently implemented `round_map(k)` for k=0,1,2. These are 30 full input-column comparisons, not one analyzer response.

## Corrected operation and retained execution

For each contiguous segment [0,1], [0,2], [1,2], set A=W_i and S=W_j ... W_(i+1), rightmost acting first. Construct inverses by reversing the actual component list and transposing each factor, including rewiring. The chronological correction word is

    inverse(suffix), inverse(first round), suffix.

Its operator is D=S A^T S^T. Exact multiplication of the compiled words gives

    D(SA)=S.

The original segment and appended correction are recorded separately. Their combined execution word differs from the suffix-only execution, although their final full-state actions agree. No historical event is erased by the identity.

For the declared passive lift, Gamma is multiplicative and Gamma(W*) is its inverse. Thus the matrix equality induces the same equality on each symmetric-power sector, and on the Fock direct sum. This all-sector conclusion uses the existing symmetric-power construction, not extrapolation from the checker. It still concerns supplied passive dynamics, not independent selection of those dynamics.

## Fresh exact verification

`python research/nima/checkers/check_cavity_prefix_removal_compiler.py` passed:

- three component/round squares, all ten input columns;
- three contiguous segment correction squares;
- all 198 occupation-basis columns in sectors N=0,1,2 across those segments;
- 9,378 factorial-metric Gram entries;
- original and correction execution words retained in the receipt.

Receipt: `results/cavity-prefix-removal-compiler.json`. Arithmetic is rational throughout; no numerical tolerance or fitted coefficient is used.

## Deliberate failures

- Omitting output rewiring produces eight nonzero matrix entries in each round comparison, with first residual 9/125.
- Transposing factors without reversing chronological order fails the full correction comparison in every tested segment.
- Applying only the first-round inverse fails in every segment. For [0,1] the residual has 40 nonzero entries, starting with 1275281/1953125.
- The untouched mode-9 amplitude observer agrees for every input even under that wrong [0,1] correction. Full action still differs. A selected scalar equality therefore cannot certify the required state recovery.

No environment-discard inverse was attempted. The complete ports remain present, and discarded ports are not represented as invertible matrices.

## Stopping condition

The previously missing cavity-specific component comparison is now constructed. Stop this model-level task rather than rerunning generic inverse algebra or enlarging the test into an unbounded simulator.

Two independent interfaces remain absent: a source-justified interval-to-segment encoding with trim semantics, and a calibrated apparatus control package permitting coherent collection, inverse operations and replay on these exact ports. The result is available to those future comparisons but does not satisfy them. Physical/source-law selection and causal-map tasks remain blocked, not refuted.
