# 3902 — The Source Gamma Bockstein Selects the Odd Conductor Defect

## Question

Entry 3896 identified the unique failure of naive sheet evaluation as the pure odd root generator on the conductor cover. Is its missing coherence supplied by a source-derived normal operation, or would repairing descent require a fitted cell?

## Frozen operation

The twisted de Rham presentation already depends on the source exponent \(\gamma\). Its integration-by-parts rows contain

\[
(\gamma-k)\,\partial K.
\]

We lifted the complete finite presentation to the dual-number direction

\[
\gamma\longmapsto\gamma+\epsilon,
\qquad \epsilon^2=0,
\]

and performed elimination over the resulting dual-number algebra. Unit pivots were normalized; pure \(\epsilon\)-rows were retained as first-normal data and were never divided by \(\epsilon\).

No correction row or root-dependent projector was introduced.

## Result

At the physical value \(\gamma=-\tfrac12\), the degree-six numerator packet has a two-dimensional space of exact relations. The gamma-normal derivative induces a map

\[
\beta_\gamma:\operatorname{Rel}_2\longrightarrow Q_{26}.
\]

At both primes \(32009\) and \(32003\):

\[
\operatorname{rank}\beta_\gamma=1.
\]

More sharply:

- the relation invisible on the conductor root cover maps to zero;
- the relation whose conductor restriction is a nonzero pure odd multiple of \(a\) maps nontrivially;
- hence the kernel of \(\beta_\gamma\) is exactly the root-invisible relation line.

The support sizes of the two Bockstein images are respectively \(0\) and \(24\) in the fixed quotient-coordinate convention at both primes.

As an occurrence-hostile check, bare reuse of the same relation on the second conductor again selects the same nonzero source line, but its root remainder has both even and odd components. Therefore the phrase “odd conductor defect” is valid in the first labelled conductor chart; parity is not transportable without the independently derived occurrence transition.

## Narrow conclusion

The rank-one failure of naive sheet descent is not an arbitrary mismatch. The frozen source presentation already singles out the same line through its first gamma-normal Bockstein:

\[
\frac{\operatorname{Rel}_2}{\ker\beta_\gamma}
\cong
\operatorname{im}\beta_\gamma,
\]

and the nonzero source line is precisely the relation carrying the odd root defect.

This establishes a canonical line-level match. It does not yet construct the full specialization-cone chain map or prove equality of its normalization with the root residue coefficient.

## Interpretation

The missing constructor is now sourced rather than postulated: it is the first normal variation of the exact de Rham relations. Naive pointwise sheet evaluation forgot that normal coherence, which is why it failed by one dimension.

## Next falsifier

Construct the chain-level comparison between the gamma-Bockstein line and the weighted trace/anti-trace collision lattice. Verify:

1. independence from presentation pivots and primitive lifts;
2. deck decomposition after the labelled conductor transition, rather than bare reuse of first-chart parity;
3. equality of the source-fixed normalization, not merely equality of rank-one images.

Failure of any item would leave only a projective line match and would not repair descent.

## Artifacts

- `research/benincasa/checkers/check_rank26_conductor_gamma_bockstein.py`
- `research/benincasa/results/rank26-conductor-gamma-bockstein.json`
- `research/benincasa/results/rank26-conductor-gamma-bockstein-p32003.json`

Ledger sequence claim: `seqclaim-24c36d88bd6344c5ada6821b`.
