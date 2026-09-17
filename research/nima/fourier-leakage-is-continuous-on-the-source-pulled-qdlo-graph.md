# Fourier leakage is continuous on the source-pulled QDLO graph

## Enlarged retained graph

Use the source-derived phase-space graph norm

\[
\|f\|_{QD}^2=\|f\|_2^2+\|Qf\|_2^2+\|Df\|_2^2
\]

and retain the `L/O` coordinates

\[
M_af,\quad \mathcal Of,\quad \mathcal OM_af.
\]

Call the resulting joint carrier the `QDLO` graph. Observers and Laurent cut characters are admitted when they are graph multipliers: their symbols and first derivatives have the boundedness required by

\[
D(mf)=mDf+(Dm)f,
\qquad Q(mf)=mQf.
\]

## Leakage estimate

For the cutoff projection `P_R`, let

\[
A_R=P_R\mathcal F(I-P_R).
\]

The existing Mellin/de Rham estimates give

\[
\|A_Rf\|_2\le R^{-1}\|Qf\|_2
\]

for incoming leakage and the Fourier-dual estimate

\[
\|(I-P_R)\mathcal FP_Rf\|_2\le R^{-1}\|Df\|_2
\]

for outgoing leakage. Thus both directed leakage blocks are continuous from their correctly typed `QD` graph domains.

For an admitted multiplier `m`, the product rules bound `mf` in the same graph topology. Therefore `A_RM_m`, endpoint traces of `A_RM_m`, and the corresponding Laurent-character branches are continuous coordinates of the source-pulled `QDLO` graph. No bare-`L2` quasidiagonality is asserted.

## Refinement coherence with H and V

For nested cutoffs `P_X <= P_Y`,

\[
A_X
=P_X\mathcal F(P_Y-P_X)+P_X\mathcal F(I-P_Y).
\]

Precomposing this identity with any admitted multiplier, rooted product, or marked finite Laurent cut preserves it by linearity. Postcomposing with retained observation also preserves it by continuity. Consequently the shell decomposition is compatible with the already constructed `H` and `V` transports.

This compatibility is lax: multiplication need not commute with `P_X` or with Fourier transport. The higher face retains the induced commutator/leakage terms rather than setting them to zero.

## Result

The chart/completion face

\[
R\times q
\]

extends from the coefficient graph to the source-pulled `QDLO` graph. Its 2-cell is the nonzero leakage operator `A_R`, and its higher coherence is shell additivity after every admitted `H`, `V`, `L`, and `O` transport.

The remaining assembly task is combinatorial: package the six strict face families and this one lax family into a single eighth-dimensional coherence certificate. Analytic strictification of the `q` face is neither needed nor valid.
