# A local soft positive cut does not control global completions

## Question

Can scalar-null confinement be proved entirely from the currently available local soft positive-cut normalization, without constructing the complete physical target and route maps?

## Completion hostile

Let \(P\) project onto the local soft-cut sector and suppose the observed compressed positive return is

\[
PKP=\frac14P.
\]

This local norm is strictly below one. On a two-sector completion, consider the positive operators

\[
K_s=
\begin{pmatrix}
1/4&0\\
0&s
\end{pmatrix},
\qquad
s\ge0.
\]

Every \(K_s\) has the same local compression. Choosing

\[
s=\frac12,
\qquad
s=1,
\qquad
s=\frac32
\]

gives respectively strict, terminal, and superunit global return. Hence local strictness and positivity do not determine the global norm.

## Cross-term freedom

The diagonal hostile already suffices. Allowing unknown cross terms enlarges the completion family and can raise the top eigenvalue even when both diagonal compressions are individually below one. Therefore a separate-sector cutoff theorem cannot replace the complete coupled form.

## Typed consequence

A local soft positive cut provides a finite-cutoff theorem on its declared sector. Promotion to scalar-null confinement requires a source-derived arrow from that sector into a complete physical target together with control of the orthogonal complement and cross routes. Equal normalization formulas or compatible local positivity do not construct this arrow.

## Strong falsifier

Any proposed local-only proof must distinguish the three explicit positive completions above using source data. If its premises inspect only \(PKP\), they are identical across all three and cannot imply global strict return.

## Relation to the current blocker

Nima reports that the q_G12 branch has only a local soft positive-cut normalization and lacks the complete physical target form, common pairing, base-lift route image, and omitted-route map. The hostile shows that these are not optional conveniences: without them, terminal and superunit positive completions remain compatible with every available local premise.

## Verification

`research/aspect/checkers/check_local_cut_global_completions.py` verifies exact positivity, equal local compression, and strict, terminal, and superunit global norms using rational arithmetic.

## Disposition

Reject the local-only rival. Further work on this branch must begin with the complete physical target constructor or a source theorem uniquely controlling every positive completion. Additional local norm estimates cannot close the global confinement claim.
