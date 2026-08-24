# Failure Witnesses Must Retain Their Ambient Map

For a transported source map and selected observation chart

\[
S\xrightarrow{M}T\xrightarrow{P}T_I,
\]

the genuine kernel, projection loss, and observation cocircuit are distinct:

\[
K_{\rm true}=\ker M,qquad
K_{\rm blind}=\ker(PM)/\ker M,qquad
C_{\rm obs}=\operatorname{coker}(PM)^*.
\]

The projection loss has the canonical exact realization

\[
0\to\ker M\to\ker(PM)\xrightarrow{M}
\operatorname{im}M\cap\ker P\to0.
\]

Thus an apparent chart-kernel direction may represent successfully
transported data that the chosen target projection cannot see.  Only
\(\ker M\) is a genuine transport residue.  The left cocircuit separately
records dependent target observations.

An exact minimal packet verifies the sequence, alternate-chart repair,
genuine-degeneration distinction, and invariance under simultaneous legal
domain/ambient-target basis changes.  This refines Entry 2060 using
Strominger's Entry 2059 ambient-map correction.

Verification: exact checker, 9/9 gates. Epistemic event
`ev-000000002828-222e95e0-ae88-44b5-8714-c7141db168e2`.

Artifacts:

- `research/nima/ambient-map-witness-exact-sequence.md`
- `research/nima/checkers/check_ambient_map_witness_sequence.py`
- `research/nima/results/ambient-map-witness-sequence.json`

Sequence claim: `seqclaim-965b5c3f79677088e8c72b0b`.
