# Combined-control encoder conjecture: invariant falsification attempt

## Question and tested contract

Can the existing software polar encoder be refined into source-bound controls,
with accuracy and composition witnesses? The operator requested falsification,
not another constructor level. The tested obligation is forward realization on
the existing 24-coordinate native/bank carrier plus 21 occurrence-memory slots.

This audit tests a declared mathematical control model: independently selectable
phase families of 21 native seam projectors, 18 framed source-bank projectors,
and 21 local record-write projectors. All use the inherited metric. Native
rotation conjugates the six frame-zero bank projectors into the other frames;
this identity is checked. The fixed native and storage Hamiltonians are not
redefined. Independent switching and arbitrary pulse parameters are assumptions
of this candidate control model, not a new hardware admission.

Rivals: (a) a common fixed component separates ready input from polar output;
(b) orthogonal disconnected control components block transfer; (c) these
obstructions disappear under the already recovered combined family, leaving
compilation and quantitative certification unresolved.

## Exact test

Checker: `checkers/check_encoder_combined_control_invariants.py`.
Receipt: `results/encoder-combined-control-invariants.json`.

All matrix arithmetic uses rational numbers. The checker reconstructs record
writes from the actual residual rows and metric, verifies projector identities,
then constructs their direction Gram matrix together with the stored seam and
bank controls. It computes the common kernel and graph of nonzero metric
pairings. It separately verifies the native-rotation frame conjugacies.

The 60 rank-one directions span 44 dimensions of the 45-dimensional carrier.
Their nonorthogonality graph is connected. The single common fixed direction
has zero occurrence-memory component, constant native triangle amplitude
1484/1331, and bank coordinates (10/11,1,1,10/11,1,1).

Its residual Bx is zero. Therefore the existing polar encoder fixes it exactly:
W x=0 and (I-W^sharp W)x=x. This uses the polar theorem rather than a floating
SVD evaluation. Native energy annihilates the same direction, and native
rotation fixes it.

Thus neither the common fixed space nor disconnected orthogonal components
separates the encoder from this combined control family. Connected direction
span is reported as such: this checker does not calculate a dynamical Lie
algebra or supply an implementing word.

## Why the swaps-only argument is insufficient

Every local record swap fixes the entire residual graph

    {(x,Bx): x in the 24-coordinate native/bank space}.

The checker verifies this on all 24 graph-basis columns for all 21 writes.
However, all 39 native seam and framed bank projectors act nontrivially on that
graph. Their phase families do not fix it pointwise. Consequently the graph
invariant from the restricted write-only family cannot obstruct the combined
family. This is an exact negative control against reusing a restricted-class
no-go as a full control obstruction.

## Disposition

The conjecture is **not falsified by these tests**, and is not verified.
The executable result is narrower: the tested fixed-space and component
obstructions fail for the combined mathematical control model.

Still unproved: a control-word synthesis algorithm, arbitrary-accuracy numerical
certificates, composition of those certificates into a WG instance, and the
operational availability of independently switchable phase controls. Merely
forming a new projector exponential does not supply the latter capability.
Endpoint-only reachability also remains distinct from this continuous model.

Fresh execution:

    python research/strominger/checkers/check_encoder_combined_control_invariants.py

Exit 0; active rank 44, fixed dimension 1, one nonorthogonality component,
39 breakers of the write-only pointwise graph invariant. Consumed source
receipts and this checker are hash-recorded and checked unchanged during the
run. Their predecessor suites and the numerical encoder were not rerun. No
Agda compilation, SCC registration, graph publication, commit or push is claimed.
