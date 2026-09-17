# Catalan-to-oriented-Fourier intertwiner

## Existing source and target actions

For `4|n`, polygon quarter rotation gives a finite Catalan representation

\[
(H_n,q_n),\qquad q_n^4=1.
\]

Prior analytic work constructs the faithful oriented logarithmic Fourier carrier

\[
(\mathscr A,W_{or}),\qquad
W_{or}=\rho_*\mathcal F\rho_*^{-1},\qquad W_{or}^4=1.
\]

It retains the complete four-port orbit and loses no odd Fourier character.

## General equivariant realization form

Let

\[
P_j^{cat}=\frac14\sum_{k=0}^3i^{-jk}q_n^k,
\qquad
P_j^{an}=\frac14\sum_{k=0}^3i^{-jk}W_{or}^k.
\]

Any realization map `R_n:H_n -> A` intertwines the quarter rotations iff it decomposes as

\[
R_n=\sum_{j=0}^3R_{j,n},\qquad
R_{j,n}=P_j^{an}R_nP_j^{cat}.
\]

Equivalently,

\[
W_{or}R_n=R_nq_n.
\]

A faithful realization requires each `R_(j,n)` to be injective on the Catalan character sector of multiplicity `m_(j,n)`. The oriented function/distribution-valued carrier has room for all four sectors; scalar deck parity does not.

## Obstruction in the existing scalar contact readout

The direct Catalan/QTDS contact chain records one-step rotation only through deck oddness. That factors the `C4` action through `C2` and cannot distinguish characters `j=1` and `j=3` from a full quarter-turn orbit.

`check_catalan_deck_vs_fourier_character_loss.py` computes the missing rank. At `n=12`, a deck-only target loses 8,272 of 16,796 Catalan directions. As `n` grows, the lost fraction tends to `1/2`.

Therefore the desired intertwiner cannot land in the scalar contact readout. It must land in the oriented four-port carrier (or the equivalent function-valued `V4` history target).

## Quarter trace after intertwining

If `R_n` is characterwise injective and preserves the normalized finite trace on its Catalan image, then

\[
\tau_n^{an}(P_j^{an}|_{R_nH_n})
=\tau_n^{cat}(P_j^{cat})
\longrightarrow\frac14.
\]

Thus the quarter-limit transports automatically once the four characterwise maps `R_(j,n)` are constructed. The concrete missing datum is a source assignment of Catalan orbit representatives to oriented Fourier seeds; equivariant extension then defines the rest of `R_n`.
