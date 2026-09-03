# Checkerboard parity does not yield adjacent Gale-cover dominance

## Question

Does every opposite-sign Gale cover carry at least as much mass on its terminal-total-positive endpoint as on its negative endpoint?

## Claim boundary

No. The first terminal case and first cover already give

\[
\{0\}<\{1\},
\]

with total-oriented values \(p_0>0\) and \(-n_1<0\), but

\[
p_0-n_1<0.
\]

The exact residual is

\[
-16285320568112443777180372297047363267417973934192109631132771459959146094794295020487527950796835594090521989757371060074819186532299919205108827944504627763049636020824964323171643079885602802428909977600000.
\]

Thus no universal adjacent pairing follows from the parity character. This does not contradict the positive terminal total: the next positive term on the chain can repair the pair deficit.

## Disposition

The smallest observed repair block is the alternating triple \(\{0\}<\{1\}<\{2\}\), for which the two positive endpoints can jointly cover the negative middle. Test all nonzero two-cover chains for this three-term parity-block inequality. Survival would expose a bounded local mechanism beyond greedy edge pairing; failure would force larger or branching Hall neighborhoods.
