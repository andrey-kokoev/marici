# Failure Witnesses Must Retain Their Ambient Map

Entry 2060 described presentation and transport witnesses too compactly.  A
chart is not merely a matrix; it is a composite diagram

\[
S\xrightarrow{M}T\xrightarrow{P}T_I.
\]

Three different defects occur:

\[
\begin{aligned}
K_{\rm true}&=\ker M,\\
K_{\rm blind}&=\ker(PM)/\ker M,\\
C_{\rm obs}&=\operatorname{coker}(PM)^*
\simeq\ker((PM)^*).
\end{aligned}
\]

They mean:

- \(K_{\rm true}\): source distinctions erased by the full transport;
- \(K_{\rm blind}\): transported distinctions erased only by the selected
  observation chart;
- \(C_{\rm obs}\): dependent or unavailable target observations, represented
  by Strominger's primitive cocircuit.

There is a canonical exact sequence

\[
0\longrightarrow\ker M
\longrightarrow\ker(PM)
\xrightarrow{M}
\operatorname{im}M\cap\ker P
\longrightarrow0.
\]

Hence

\[
K_{\rm blind}
\simeq
\operatorname{im}M\cap\ker P.
\]

The right side says exactly what the chart failed to observe: source data that
was transported successfully into \(T\), but landed in the selector's blind
subspace.

The exact minimal packet reproduces Strominger's distinction.  The full map
is injective, the preferred chart has one artificial right kernel and one
left cocircuit, and an alternate chart removes both.  At genuine degeneration
the same right-kernel direction already lies in \(\ker M\), so the projection
loss quotient is zero.  Simultaneous legal changes of domain and ambient
target basis preserve all dimensions.

Software translation:

- \(M\): complete service response;
- \(P\): selected API/view projection;
- \(K_{\rm blind}\): information successfully returned by the service but
  omitted by that view;
- \(K_{\rm true}\): information the service itself erased;
- \(C_{\rm obs}\): selected fields that became functionally dependent.

The revised conjecture is that every presentation witness must be stored with
the full diagram \((M,P)\), not as an untyped null vector.

The exact checker passes 9/9 gates.

Artifacts:

- `research/nima/ambient-map-witness-exact-sequence.md`
- `research/nima/checkers/check_ambient_map_witness_sequence.py`
- `research/nima/results/ambient-map-witness-sequence.json`

Sequence claim: `seqclaim-965b5c3f79677088e8c72b0b`.
