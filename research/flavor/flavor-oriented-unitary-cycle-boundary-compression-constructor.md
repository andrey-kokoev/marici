# Oriented Unitary Cycle Boundary-Compression Constructor

## Question

Can WP852's partial-isometry relation be derived from a more primitive source
operation instead of imposed directly on the flavor path?

## Lossless source cycle

Let (U) be the oriented four-cycle transport

\[
Ue_0=e_1,
\quad Ue_1=e_2,
\quad Ue_2=e_3,
\quad Ue_3=e_0.
\]

It is unitary and has no preferred endpoint. Introduce an explicitly declared
boundary operation that removes the return channel (e_3\to e_0). With
(P_j=e_je_j^*), the open transport is

\[
C=(I-P_0)U=U(I-P_3).
\]

The WP852 relations now follow rather than being postulated:

\[
C^*C=I-P_3,
\qquad
CC^*=I-P_0,
\qquad
C^4=0.
\]

Thus lossless source transport fixes every surviving link magnitude, while a
rank-one boundary compression creates the directed path and its endpoints.

## Relative orientation

The boundary current is

\[
J=C^*C-CC^*=P_0-P_3.
\]

Reversing the source cycle and the removed channel gives (-J). Hence the
sign is relational: it is fixed relative to the oriented boundary port. The
construction does not reveal an absolute sign of the original closed cycle.
Adding the boundary changes the physical groupoid from cyclic unitary
transport to the stabilizer groupoid preserving the marked source and sink.

## Magnitude and phase fiber

A phase-weighted lossless cycle still has unit-modulus links. After the return
edge is removed, a diagonal number-preserving unitary eliminates all three
surviving phases. The open-path fiber is therefore one orbit and its defect
singular value is exactly one. This derives WP852's normalization from
unitarity plus the boundary operation.

The dimensionless unit is not yet the measured portal coupling. Carrying it
to (g_n-g_m) requires a source-calibrated map from the boundary current to
canonically normalized flavor currents. Multiplication by an arbitrary gauge
coupling after compression would reopen the continuous magnitude fiber.

## Threshold statement

Exact unitary dilation preserves the rank-one defect identity as long as the
same return port remains resolved. Tracing out, merging, or failing to resolve
that port can erase the orientation record. Therefore this packet establishes
algebraic survival under source-unitary transport, not survival through an
unspecified physical threshold. A threshold theorem must intertwine the
marked projections (P_0,P_3), not merely the unmarked charge spectrum.

## Physical-instrument gate

The constructor has a clear operational type: prepare a lossless four-port
cycle, terminate or monitor one directed return port, and tomographically test
the two defect projections. But no admitted flavor experiment currently
identifies those four ports with flavor source states or maps the defect
current into a calibrated `physical16` response.

## Classification

Conditional source-generated relational selector and normalizer. It makes the
open-path asymmetry unavoidable once a lossless oriented cycle and a marked
boundary termination are admitted. It fixes the internal sign relative to the
port and fixes the dimensionless defect magnitude. It does not yet derive why
flavor possesses this cycle and boundary, nor the RG flow, threshold
intertwiner, or physical readout.

## Verification

Run:

```text
uv run --with sympy python research/flavor/checkers/wp854_oriented_unitary_cycle_boundary_compression_constructor.py
```
