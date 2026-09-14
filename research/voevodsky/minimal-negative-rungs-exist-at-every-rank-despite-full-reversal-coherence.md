# Minimal negative rungs exist at every rank despite full reversal coherence

For every \(n\geq3\), let \(G_n\) have diagonal entries one and constant off-diagonal entry \(r_n\). Its eigenvalues are

\[
1-r_n
\]

on the transverse subspace and

\[
1+(n-1)r_n
\]

on the all-ones line.

Choose

\[
r_n=-\frac12\left(\frac1{n-2}+\frac1{n-1}\right).
\]

Then

\[
1+(n-1)r_n<0,
\]

so the full rank-\(n\) packet is indefinite. But every proper principal packet has rank at most \(n-1\), and its smallest eigenvalue is bounded below by

\[
1+(n-2)r_n>0.
\]

These packets have maximal permutation symmetry and therefore exact reversal coherence.

Thus a first negative rung can occur at any prescribed finite rank while every proper coordinate reduction remains positive.

## Consequence

No branching hierarchy made only from deletion, restriction, or proper coordinate subpackets can be jointly conservative for negativity. A negative all-channel correlation can be invisible on every such branch.

To retain it, some branch must carry the mixed all-channel mode

\[
p=u_1+\cdots+u_n.
\]

But compressing this mode to one coordinate preserves its composite ancestry. Its scalar positivity is not inherited from primitive one-channel positivity.

Therefore the desired reduction family faces a sharp no-go:

- branches ending in genuinely primitive coordinate leaves can lose negativity;
- branches guaranteed to retain negativity must carry composite correlation data to their leaves.

Reversal, incidence, and arbitrary finite local coherence do not remove this obstruction. A source-specific identity must rule out the equicorrelation-type collective negative mode directly.

## Verification

```text
python research/voevodsky/checkers/check_arbitrarily_late_minimal_negative_rungs.py
```

Artifacts:

- `research/voevodsky/checkers/check_arbitrarily_late_minimal_negative_rungs.py`
- `research/voevodsky/results/arbitrarily_late_minimal_negative_rungs.json`
