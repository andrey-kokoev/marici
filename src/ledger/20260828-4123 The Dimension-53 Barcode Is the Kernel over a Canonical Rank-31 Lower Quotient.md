# 4123 — The Dimension-53 Barcode Is the Kernel over a Canonical Rank-31 Lower Quotient

## Correction

Entry 4118 correctly reported the stable free-column census

\[
84=53+22+7+1+1,
\]

but its interpretation of the 53 columns as a canonical top-block quotient was too strong. Free-column location in a stable RREF is not by itself an invariant quotient typing.

Exact projection ranks give the corrected sequence.

## Projection calculation

Split the 2,278 residual coordinates into:

\[
T:\ 120\text{ coordinates in }(3;22222),
\]

\[
L:\ 2{,}158\text{ lower-block coordinates}.
\]

For the diagonal-only presentation:

\[
\operatorname{rank}R_T=56,
\qquad
\dim(T/R_T)=64,
\]

\[
\operatorname{rank}R_L=1{,}608,
\qquad
\dim(L/R_L)=550.
\]

After including the projected mixed relations:

\[
\operatorname{rank}\pi_T(R)=120,
\]

so the full relation space projects onto every raw top coordinate. There is no raw top-block cokernel.

For the lower projection:

\[
\operatorname{rank}\pi_L(R)=2{,}127,
\]

hence

\[
\dim\operatorname{coker}\pi_L(R)
=
2{,}158-2{,}127
=
31.
\]

The full quotient has dimension 84. Therefore projection to the lower quotient has a 53-dimensional kernel:

\[
0
\longrightarrow
K_{53}
\longrightarrow
F_{84}
\longrightarrow
L_{31}
\longrightarrow
0.
\]

## Attachment accounting

The mixed relations add rank 530 beyond the diagonal presentation.

Their lower projection adds

\[
2{,}127-1{,}608=519
\]

independent constraints. The remaining

\[
530-519=11
\]

constraints govern the top component of the graph attachment.

Equivalently, the diagonal dimensions change as

\[
64+550=614
\]

to

\[
53+31=84.
\]

Thus the mixed attachment removes 11 top directions and 519 lower directions while retaining a 53-dimensional relative kernel over a canonical 31-dimensional lower quotient.

## Status of Entry 4118

Superseded interpretation:

- “53 is the canonical top-block quotient.”

Surviving evidence:

- the five-prime common pivot pattern;
- the free-column census \(53+22+7+1+1\);
- the conclusion that the full filtered object is 84-dimensional.

Correct interpretation:

- 31 is the canonical lower projected quotient;
- 53 is the relative kernel of the full quotient over that lower quotient.

## Next falsifier

Construct the connecting graph map from the 519-dimensional lower attachment image into the 64-dimensional diagonal top quotient. Determine whether its 11-dimensional top rank is nullhomotopic under source-authorized triangular changes. This is the correctly typed splitting test.

## Durable artifact

`research/benincasa/results/interaction-net-filtered-residual-projection-sequence.json`

Sequence claim: `seqclaim-2aa93a5db99648b46ed081b7`.
