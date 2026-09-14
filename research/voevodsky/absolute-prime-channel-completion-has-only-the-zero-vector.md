# Absolute prime-channel completion has only the zero vector

## Candidate completion

A natural attempt to globalize the compact-window prime forms is to control every translated channel separately. For a function \(f\), this would require finite energy

\[
E_P(f)=
\sum_{n\geq2}
\frac{\Lambda(n)}{\sqrt n}
\lVert T_{\log n}f\rVert_2^2.
\]

Here \(T_a\) is translation by \(a\).

## No-go theorem

Translations are unitary, so

\[
\lVert T_{\log n}f\rVert_2
=
\lVert f\rVert_2.
\]

Therefore

\[
E_P(f)
=
\lVert f\rVert_2^2
\sum_{n\geq2}
\frac{\Lambda(n)}{\sqrt n}.
\]

The coefficient series diverges. It already diverges after restriction to primes. Consequently

\[
E_P(f)<\infty
\]

holds only for \(f=0\).

Thus independent square-summation of all prime translation channels produces a trivial domain and cannot serve as the global graph completion.

## Consequences

The finite-window forms cannot be globalized by taking absolute values or positive squares prime by prime. Any nontrivial completion must preserve cancellation among infinitely many terms. In particular, it must use at least one of:

- joint gamma-prime regularization;
- oscillatory summation before taking norms;
- a source-prescribed subtraction;
- a distributional form topology rather than an absolute channel norm.

This also limits the channel-bundle analogy. Prime channels cannot be treated as mutually independent positive fibers and then Hilbert-summed. Their global arithmetic coherence is intrinsically conditional and nonlocal.

## Disposition

The absolute prime-channel graph-norm route is closed. The first surviving construction is the polarized jointly regularized kernel

\[
K(s,t)=Q_{\Gamma+P}(r_s,r_t),
\]

with gamma and prime contributions combined before completion. Without exact off-diagonal values of this kernel, the closability criterion cannot be evaluated.

## Verification

```text
python research/voevodsky/checkers/check_prime_translation_graph_norm_no_go.py
```

The checker computes increasing partial weight sums through one million and verifies the unitary-energy reduction.

Artifacts:

- `research/voevodsky/checkers/check_prime_translation_graph_norm_no_go.py`
- `research/voevodsky/results/prime_translation_graph_norm_no_go.json`
