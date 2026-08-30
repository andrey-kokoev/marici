# The Eta-Squared Moore Cycle Is Explicit Before Artin Expansion

## Result

The first nonzero five-point homotopy residue now has an exact word in
Milnor's free simplicial group. In simplicial degree three, set

\[
w_{\eta^2}=[[x_0,x_1],[x_0,x_2]].
\]

Mikhailov identifies this commutator as the suspension-over-Hopf class

\[
\lambda_1\circ\lambda_1=\eta\circ\Sigma\eta
\in\pi_3(F[S^1])=\pi_4(S^2)\cong\mathbb Z/2.
\]

This is the missing source-derived Moore constructor. It is not the previously
tested nested Brunnian word, which belongs to the fillable subgroup.

## Exact face audit

In degree three the face maps on the free generators are

\[
\begin{array}{c|ccc}
 &x_0&x_1&x_2\\
\hline
d_0&x_0&1&x_1\\
d_1&x_0&x_1&x_1\\
d_2&x_0&x_1&x_0\\
d_3&1&x_1&x_0.
\end{array}
\]

Consequently,

\[
\begin{aligned}
d_0w_{\eta^2}&=[[x_0,1],[x_0,x_1]]=1,\\
d_1w_{\eta^2}&=[[x_0,x_1],[x_0,x_1]]=1,\\
d_2w_{\eta^2}&=[[x_0,x_1],[x_0,x_0]]=1,\\
d_3w_{\eta^2}&=[[1,x_1],[1,x_0]]=1.
\end{aligned}
\]

Thus the word is a strict Moore cycle, not merely a cycle after
abelianization or passage to an associated graded object. The checker performs
these substitutions in the free group and reduces the resulting words.

## Why nontriviality is separate

Deletion triviality proves only membership in the Moore-cycle subgroup. It
does not prove survival modulo Moore boundaries. Mikhailov's lower-central,
mod-two computation supplies the second certificate: the word represents
\(\lambda_1\lambda_1\), the nonzero generator of \(\pi_4(S^2)\), and has order
two there.

This yields the exact two-gate compiler:

1. free-group face reduction establishes the Brunnian/Moore condition;
2. the sourced homotopy computation establishes nonfillability.

The earlier nested commutator passed only the first gate.

## Remaining compiler

The simplicial injection of \(F[S^1]\) into the pure-braid object transports
this cycle to a spherical Brunnian five-braid. That establishes an explicit
constructor-level description, but this packet does not yet expand the image
into the standard five-strand Artin generators \(A_{ij}\).

The smallest remaining constructor is therefore:

```text
Milnor degree-three basis
  -> strand-doubling pure-braid basis
  -> five-strand spherical Artin normal form
```

It must preserve all four face identities and the nonzero quotient class. An
arbitrary Brunnian word cannot substitute for this map.

## Frozen-law consequence

Aspect's frozen-v2 rule is respected. Matrix associators may change a
presentation chart, but cannot turn a Moore boundary into this class or erase
this class in the authoritative filling quotient. The binary invariant is the
homotopy class, not any selected Artin word.

## Replay

```powershell
uv run python research/strominger/checkers/eta_squared_moore_cycle_compiler_checks.py
```
