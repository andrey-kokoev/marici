# 1717 — Triple Nested Mixture Conditioning Has Trivial Associator

## Hard-to-vary claim

Three nested zero-marginal conditionings are exhausted by the labelled flag of
ordinary simplex-face blowups; changing parenthesization creates no additional
coherence class.

Freeze

\[
\pi_{0k}=\varepsilon\delta\theta t_k,
\qquad
\pi_{1k}=\varepsilon\delta s_k,
\qquad
\pi_{2k}=\varepsilon r_k,
\]

and preserve the three row occurrences.

## Parenthesization test

With \(T=\sum t_k\), \(S=\sum s_k\), and \(R=\sum r_k\), iterated
conditioning gives

\[
\frac{\delta(S+\theta T)}{R+\delta(S+\theta T)}
\frac{\theta T}{S+\theta T}
\frac{t_k}{T}
=
\boxed{
\frac{\delta\theta t_k}{R+\delta(S+\theta T)}
}.
\]

This is the direct normalized entry.  Reparenthesization changes only the
order in which the labelled normal coordinates are multiplied, and

\[
\delta(\theta T)=(\delta\theta)T.
\]

Hence the transition functions satisfy the associativity identity strictly.

## Result

The exceptional object is the labelled flag

\[
(\delta,\theta,[t_k]).
\]

There is no overlap associator, no new coefficient extension, and no new Cut
carrier stratum in the tested finite model.

## Durable artifacts

- `research/benincasa/checkers/triple_nested_simplex_associator.rs`
- `research/benincasa/results/triple-nested-simplex-associator.json`
- `research/benincasa/triple-nested-simplex-associator.md`

## Next falsifier

Replace the linearly ordered nesting by two incomparable vanishing mixture
faces.  Test the square of blowup charts for a nontrivial interchange class;
the chain case cannot detect such a class.
