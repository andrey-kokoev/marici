# Four-Point Faithfulness Does Not Compose to Five Points

The faithful endpoint-projective-central packet on four marked points does not
become faithful on five points by observing every four-point deletion face.

The point-push loop

\[
\beta=[[[x_1,x_2],x_3],x_4],
\qquad x_1x_2x_3x_4=1,
\]

is a nonempty freely reduced word of length twenty two after eliminating
\(x_4\). It therefore defines a nontrivial five-point mapping class through
the Birman point-pushing injection. Deleting any one of the five marked
points trivializes it.

Thus

\[
0\ne\beta\in\bigcap_{i=1}^{5}\ker(d_i).
\]

The obstruction is five-ary Brunnian coherence: every four-point face is
individually trivial and even perfectly observed, while their joint filling
is not. A new five-point port is required.

Evidence:

- `research/strominger/four-point-faithfulness-does-not-compose-to-five-points.md`
- `research/strominger/checkers/five_point_brunnian_four_marginal_hostile_checks.py`
- `research/strominger/results/five_point_brunnian_four_marginal_hostile_checks.json`

Verification: 8/8 exact gates passed. Checker SHA-256:
`547ba5e45877327eb063b4acd7b8c84f68d3353d282ab18a2e762b281f5b5131`.
