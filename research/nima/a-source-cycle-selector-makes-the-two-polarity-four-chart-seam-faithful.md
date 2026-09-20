# A source cycle selector makes the two-polarity four-chart seam faithful

## Question and conjecture

Can one construct, rather than merely label, a two-polarity/four-chart packet with a source-preserving fourth-to-first successor seam and a determinant image?

The conjecture tested is that retained graph incidence plus a cycle selector supplies the missing reconstruction needed for such a seam. The rival keeps all four Fourier charts of the boundary response but discards the cycle coordinate. A second rival closes the fourth chart by Fourier alone and ignores the independently declared source successor.

SCC obligation: finite forward realization, attachment transport, and mixed polarity/seam compatibility. The source is the oriented graph cycle on four labelled vertices and edges. This is an exact finite model of the mechanisms in the prior-research audit, not a construction of the theta/amplituhedron comparison.

## Independent source operations and carrier

Use column vectors on E=C^4 with edge e_j directed from vertex j to vertex j+1 modulo 4. Let S e_j=e_(j+1). The graph boundary is

\[
B=S-I.
\]

The graph cycle h=(1,1,1,1) spans ker B. Mark the edge e_0 and retain its coefficient via Z=(1,0,0,0). This is a declared chord selector, not a determinant-fitted row.

Define

\[
O c=(Bc,Zc)\in\mathbb C^4\oplus\mathbb C.
\]

The first three boundary coordinates together with Z determine c uniquely. If P selects those four rows of O, the source recovery is

\[
R=(PO)^{-1}P,\qquad RO=I.
\]

The response carrier is im O, not all of C^5. Its source-pulled inner product is defined by making O an isometry. No assertion is made that O is isometric for the ambient Euclidean metric. The marked edge and graph size are model inputs, not predictions of the amplituhedron.

## Four charts and two polarities

Let F be the normalized four-point Fourier transform,

\[
F_{jk}=\frac12 i^{-jk},\qquad F^2=P_{\rm ref},\quad F^4=I.
\]

For polarity sigma in {+1,-1} and phase j in {0,1,2,3}, define

\[
A_{\sigma,j}=\operatorname{diag}(F^{\sigma j},1),\qquad
O_{\sigma,j}=A_{\sigma,j}O,\qquad
R_{\sigma,j}=RA_{\sigma,j}^{-1}.
\]

Each realized chart has exact source recovery R_sigma,j O_sigma,j=I. The phase step is U_sigma=diag(F^sigma,1). The cycle coordinate is retained through all four Fourier presentations.

Source reflection sends an oriented edge to the negative of the reflected edge:

\[
D=-S^{-1}P_{\rm ref},\qquad
D^2=I,\quad BD=P_{\rm ref}B,\quad DS=S^{-1}D.
\]

The anti-linear source polarity is c -> D conjugate(c). Its induced map from the positive to negative response chart is

\[
y\longmapsto O_{-,j}D\,\overline{R_{+,j}y}.
\]

It is antiunitary in the declared source-pulled metrics and reverses the source successor. The implementation verifies its chart squares and mixed seam square. This is not merely coefficient conjugation with orientation omitted.

## Source-induced seam

Independently choose labelled graph translation S as the positive successor and S^-1 as the negative successor. On the realized images construct

\[
W_\sigma=O S^\sigma R_{\sigma,3}.
\]

Then

\[
W_\sigma O_{\sigma,3}=O S^\sigma,
\qquad
W_\sigma U_\sigma^3 O=O S^\sigma.
\]

Thus one four-phase traversal lands in phase zero of the successor source state, not the original state. Iterated traversals give S^(sigma k) on the source. In this particular four-edge model S^4=I; no unbounded successor theorem is inferred.

The seam is invertible between its four-dimensional realized images, with inverse O_sigma,3 S^(-sigma) R. Its extension as a five-dimensional matrix is singular. Taking the determinant of that ambient extension would incorrectly report loss of invertibility.

This construction does not select S from the Fourier transform. Label translation is explicit source input; replacing it by identity defines a different system. The relation between this graph successor and an arithmetic or amplituhedron successor remains unconstructed.

## Finite falsifiers and determinant image

For h=(1,1,1,1), every Fourier-transformed history component is zero, while every retained cycle coordinate equals 1. Therefore keeping four history charts without the cycle selector still loses a nonzero source state. Adding polarity does not repair that loss either.

The second hostile replaces W_+ by the ordinary Fourier wrap. It returns O rather than OS and has a nonzero source-transport residual. Four-chart closure alone is therefore not successor-seam compatibility.

On source coordinates, the seam reduces to

\[
R W_+ O_{+,3}=S.
\]

Its top exterior map gives the determinant-line transport. In the fixed oriented source frame its scalar is det S=-1. In contrast the five-dimensional extension has determinant zero.

Only after this image-level construction, use K=S-I to evaluate the finite plus-convention regularized determinant:

\[
\operatorname{Tr}K=-4,\qquad
\operatorname{Tr}K^2=4,\qquad
\det_3(I+K)=-e^6.
\]

These are trace coordinates of the graph successor. They are not identified with Euler primitive or square currents. No logarithm branch or positive-energy interpretation is imposed on the negative determinant.

## Verification and disposition

`research/nima/checkers/check_two_polarity_four_chart_cycle_seam.py` passes 24 exact symbolic checks. Result: `research/nima/results/two-polarity-four-chart-cycle-seam.json`.

The first run encountered a symbolic-equality defect in the final regularizer check: an unsimplified expression was compared directly to 6. Explicit simplification repaired that check; the fresh run passed without changing any expected mathematical value.

Constructed at finite graph-source strength: all eight realized charts, source recovery, oriented anti-linear polarity, a source-induced successor seam, mixed polarity/seam compatibility, a cycle-loss hostile, and determinant transport on the correct image carrier.

Not constructed: the map from this graph packet to the actual theta or NNMHV history source, prime-ratio attachments, Euler trace comparison, archimedean sewing, or any completion. The model neither explains nor reproduces the earlier -4/5 residual. Its substantive result is instead an explicit omitted-cycle witness and a seam whose determinant exists only after the correct response image has been identified.
