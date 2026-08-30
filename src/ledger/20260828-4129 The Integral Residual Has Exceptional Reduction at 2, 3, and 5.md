# 4129 — The Integral Residual Has Exceptional Reduction at 2, 3, and 5

## Claim

The fixed primitive integral residual matrix has full tested rank

\[
2{,}194
\]

at

\[
p=7,11,13,31991,32003,32009,32027,32029,
\]

but loses rank at \(p=2,3,5\).

The exact census is:

| \(p\) | Rank | Quotient dimension | Defect from 2,194 |
|---:|---:|---:|---:|
| 2 | 2135 | 143 | 59 |
| 3 | 2028 | 250 | 166 |
| 5 | 2069 | 209 | 125 |
| 7 | 2194 | 84 | 0 |
| 11 | 2194 | 84 | 0 |
| 13 | 2194 | 84 | 0 |

## Interpretation

The arithmetic anomaly is not generic small-characteristic instability. Among tested small primes it is concentrated at

\[
2,3,5.
\]

These are exact modular rank drops of one frozen integer matrix, not comparisons between independently normalized finite-field presentations.

If the characteristic-zero rank is exactly 2,194, the defects become the numbers of Smith invariant factors divisible by the corresponding primes:

\[
t_2=59,
\qquad
t_3=166,
\qquad
t_5=125.
\]

That identification remains conditional because the present modular data prove only

\[
\operatorname{rank}_{\mathbf Q}R\ge2{,}194.
\]

A characteristic-zero upper certificate is still required.

## Consequence for splitting

Plain vector-space splitting is automatic and therefore scientifically empty. The first typed obstruction is integral. The exceptional reductions show that an integral section, if it exists, cannot be inferred from the good-prime vector spaces alone.

The next finite test is prime-local Smith analysis at \(2,3,5\), beginning with valuations of determinantal minors or ranks modulo \(p^k\). Prime-local work should remain separate from the unresolved characteristic-zero upper-bound certificate.

## Durable artifact

`research/benincasa/results/interaction-net-integral-residual-small-prime-ranks.json`

Sequence claim: `seqclaim-1c2ee613fc1b1e2764ee062b`.
