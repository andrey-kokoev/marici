# 1645 — Temporal Composition Commutes with Cut Only Before Internal Pushforward

## Interchange test

Entry 1644 selects exact exponential composition.  Test whether temporal composition commutes with labelled Cut sewing after each step has already been reduced to an observed channel.

## Exact memory falsifier

Use one observed binary occurrence, one internal occurrence initialized in (|0\rangle), and CNOT as the global interaction.  On the observed state (|+\rangle\langle+|):

1. One interaction followed by internal pushforward gives complete dephasing.
2. Retaining the same internal occurrence through two interactions gives (U^2=I), hence restores the input exactly.
3. Pushing forward after step one, resetting the discarded internal state, and applying the reduced channel again remains dephasing.

Therefore

\[
\operatorname{Tr}_E\!\left[U^2(\rho\otimes|0\rangle\langle0|)U^{\dagger2}\right]
\ne
\Phi_U\!\left(\Phi_U(\rho)\right).
\]

The checker finds two differing off-diagonal matrix entries: identity on the retained global route versus zero on the stepwise-pushforward route.

## Typed interpretation

Temporal composition and labelled Cut sewing do commute on the global object retaining the internal occurrence.  The failure appears only after applying internal pushforward before temporal sewing.  That pushforward forgets memory required by the second step.

Hence the comparison is

\[
\boxed{
\text{compose then push forward}
\not\simeq
\text{push forward each step then compose reduced channels}
}
\]

on repeatedly interacting or correlated support.

This is not evidence for a new carrier cell.  It confirms Entry 1641's coefficient typing: the correct temporal object is a process tensor retaining labelled internal memory.  Ordinary channel composition is valid only on a Markov/product stratum where the internal occurrence may be independently reset.

## Durable artifacts

- `research/benincasa/checkers/temporal_cut_memory_obstruction.rs`
- `research/benincasa/results/temporal-cut-memory-obstruction.json`
- `research/benincasa/temporal-cut-memory-obstruction.md`

## Next falsifier

Construct the two-step process tensor with the internal occurrence retained and derive the Markov/product restriction as an actual factorization condition.  Test whether vanishing conditional mutual information, covariance cross-blocks, or another source-derived criterion exactly characterizes when early internal pushforward commutes with temporal composition.