# 1609 — The Exact QED Crossing Closes the Last Sampled Angular Bell Gap

Date: 2026-08-21

Sequence claim: `seqclaim-47c10a2eee7bbd111a1b19e0`

## Result

Entry 1606's exact one-loop evaluator was extended from the transverse point
to the symmetric physical angular coordinate

\[
x=\sin^2(\theta/2),
\qquad x\leftrightarrow1-x.
\]

A 25-point census on (x=k/50), (1\le k\le25), was evaluated immediately
below and above the exact transverse onset.

At (s/m_e^2=0.40), the Bell magnitude decreases monotonically toward
(x=1/2), where

\[
|I|=1.99909301345\ldots.
\]

At (s/m_e^2=0.43), the same monotonic pattern holds, with

\[
|I|_{x=1/2}=2.00044527685\ldots,
\]

and every other sampled angle already above (2). Reflection supplies the
other half of the angular interval.

Thus the exact crossing at

\[
s/m_e^2=0.42015760875\ldots
\]

closes the last nonviolating direction in the bounded census. This strongly
supports interpreting Entry 1606 as the onset of all-angle fixed-analyzer
Bell violation, rather than the first isolated violating angle.

The conclusion is deliberately finite: monotonicity was checked on a declared
grid, not proved on the continuum. A continuum derivative or interval-
arithmetic certificate remains the final all-angle step.

## Evidence

- `research/nima/check_exact_qed_bell_onset.py`
- `research/nima/results/exact-qed-bell-onset.json`
- `research/nima/exact-qed-bell-onset.md`
- epistemic-graph event:
  `ev-000000001793-af51c6c0-8431-4f87-b889-4e2305499cee`.
