# The existing seam--endpoint theorem reduces the resolved-graph gate to one metric identification

## Status

Frontier reconciliation only. This packet does not claim G1.1 or RH.

## Existing theorem

The repository already proves much more than the current seam/endpoint TODO suggested. In
`moving-seam-transport-and-complete-endpoint-pushforward-form-an-exact-metric-natural-transformation.md`, the composite

\[
\text{weighted Adams incidence}
\longrightarrow
\text{moving-seam transport}
\longrightarrow
\text{complete wall--jump endpoint pushforward}
\]

is an exact metric natural transformation on the source-generated linear bundle. The same packet proves:

- unitary seam motion;
- exact rank-two endpoint faithfulness;
- reciprocal-grade preservation;
- exact word composition;
- strict contraction on every nonunit Euler-weighted Adams grade;
- commutation with prime cutoffs; and
- naturality in all four Fourier presentations, with no additional norm loss after summing the transported Grams.

Consequently, seam transport followed by endpoint attachment is **not** an open linear-constructor problem. Nor is Fourier-orbit or finite-cutoff compatibility open for that word.

## What is not yet identified

The newly selected G1.1 quadratic target is the resolved three-port graph

\[
\mathcal R_N f=(f,B_Nf,M_\Phi f),
\qquad
\mathcal R_N^*\mathcal R_N
=(1+M_\Phi^2)I+B_N^*B_N.
\]

The existing seam--endpoint theorem says that its composite preserves the object-indexed Mellin metric and the sum of the four transported Fourier Grams. It does not, in the cited theorem statement, explicitly identify that preserved metric with

\[
(1+M_\Phi^2)I+B_N^*B_N
\]

on the common source-generated incidence domain. In particular, its phrases “complete wall--jump endpoint pushforward” and “sum of transported Grams” do not by themselves prove that the three typed outputs are exactly

\[
f,\quad B_Nf,\quad M_\Phi f
\]

with the direct-sum polarization selected by the resolved branch.

This distinction matters: replacing the direct-sum polarization by the downstream history codiagonal would produce

\[
I+H_\Phi^*H_\Phi
\]

and insert the nonzero cross term \(M_\Phi(B_N+B_N^*)\). That replacement is not authorized.

## Reduced gate

The correct remaining seam/endpoint obligation is therefore one exact identification, not a new continuity proof:

> On the source-generated cutoff domain, identify the object-indexed Mellin/Fourier metric preserved by the existing seam--endpoint natural transformation with the resolved direct-sum three-port Gram \((1+M_\Phi^2)I+B_N^*B_N\), before any history codiagonal.

Equivalently, produce the commuting typed diagram

\[
\mathcal R_N\,A_N
=
\bigl(A_N^{(0)}\oplus A_N^{(B)}\oplus A_N^{(W)}\bigr)\mathcal R_N
\]

for the already constructed seam--endpoint word \(A_N\), with the three target maps matching the identity, tail, and output-wall ports. Once this is written, exact metric naturality immediately gives resolved-Gram preservation.

## Radical and completion consequence

If the identification is established isometrically on the source-generated pre-Hilbert space, radical descent for this generator word is automatic: a zero-norm vector maps to a zero-norm vector. Its extension to the corresponding completion is then contractive (isometric before Euler weighting). This does **not** by itself prove closed range for the full analytic--arithmetic source pushout, because that pushout contains additional bulk/external-port identifications.

## Revised frontier

The seam--endpoint generator word and its cutoff/Fourier continuity are closed. The earliest local question is the metric identification above. Beyond it, the cited theorem itself places the constructor frontier at compatibility with the even zero-trace bulk Green form, equivalently the complete bulk-plus-external-port Green identity and its anti-diagonal reduction.

The global closed-range, radical-compatibility, remaining Green-entry, and prime-uniform coercivity obligations remain open.
