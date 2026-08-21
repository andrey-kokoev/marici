# Naive eta-tail certification is computationally unusable

For derivative order `j`, the regular eta source has alternating summand

\[
 a_n^{(j)}=\frac{(\log n)^j}{n}.
\]

It decreases once `n>e^j`, so elementary alternating-series estimation bounds
the tail by `a_(N+1)^(j)`. Solving

\[
 \frac{(\log N)^j}{N}<10^{-12}
\]

gives these approximate first cutoffs:

| `j` | cutoff `N` |
|---:|---:|
| 0 | `1.000000000001e12` |
| 1 | `3.1067172842018e13` |
| 2 | `1.205894964554194e15` |
| 3 | `5.7467771891740204e16` |
| 4 | `3.306490959075339521e18` |

The direct rigorous implementation would require over three quintillion
fourth-derivative terms. The regular-jet reformulation is sound, but naive
alternating truncation is decisively falsified as an algorithm. The next
certifier must accelerate the tail while retaining a proved remainder, for
example by alternating Euler--Maclaurin with explicit derivative bounds.

## Scope

Binary logarithms suffice for this cost no-go; this is not the analytic
interval certificate. The scale conclusion is insensitive to last-bit error.

## Durable verification

- Checker: `checkers/eta_naive_tail_cost.py`
- Result: `results/eta-naive-tail-cost.json`
