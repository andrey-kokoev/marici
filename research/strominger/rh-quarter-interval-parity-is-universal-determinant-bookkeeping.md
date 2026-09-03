# Quarter interval parity is universal determinant bookkeeping

## Question

Which part of the almost-principal sign law is universal, and which part is specific to the Hurwitz transfer?

## Claim boundary

The determinant-reordering identity holds at arbitrary matrix size. The terminal-bordered sign rule is verified in all 1,792 order-eight cases but is not yet proved for arbitrary Hurwitz size.

## Disposition

Move the exchanged row and column indices from sorted positions to terminal positions. The combined permutation sign is

\[
(-1)^{|S_{>i}|+|S_{>j}|}
=(-1)^{|S\cap(i,j)|}.
\]

All exact determinant equalities pass. After removing this universal factor, the terminal bordered minors obey

\[
\operatorname{sgn}u^{\rm term}_{S;i,j}=(-1)^{j-i+1},
\qquad
\operatorname{sgn}v^{\rm term}_{S;i,j}=(-1)^{j-i}.
\]

Thus interval parity requires no Hurwitz theorem; only the terminal sign rule does. The next leaf is `quarter-terminal-bordered-schur-signs`, rewriting terminal bordered minors as positive principal determinants times off-diagonal entries of principal Schur complements, to isolate a pivot-stable anti-checkerboard invariant.
