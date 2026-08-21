# 1414 — The First Fiber-Numerator Grade Does Not Restore Five-Site Order-One Exactness

## Status

Replicated finite-field rank exclusion at a fixed numerator and scalar-degree
bound. Not a characteristic-zero or all-degree theorem.

## Question

The constant-numerator five-site projective test found no labelled primitive
whose divergence reproduces a genuine first-order fiber derivative. Is that
failure merely caused by freezing the primitive numerator?

Enlarge every one of the 180 labelled source terms by the first
fiber-coordinate numerator basis

\[
1,\qquad u_1,\qquad u_2,\qquad u_3,
\]

for each of the three source derivatives. This gives

\[
180\cdot3\cdot4=2160
\]

primitive columns. Permit scalar coefficients in the fiber parameter \(t\)
through degree three.

## Repaired sampling contract

The first 1500-sample attempt exposed a sampler defect: a seed reduced
linearly modulo \(p\) has only \(p\) states and therefore cannot generate
1500 distinct samples when \(p=1009\). The repaired checker expands
\((p,\mathrm{seed},\mathrm{offset})\) with BLAKE2b into four independent
field coordinates. A two-prime smoke test preceded the authoritative rerun.

## Rank result

At 1500 distinct samples, both independent primes give

\[
\begin{array}{c|c|c|c|c}
p&\operatorname{rank}P&\operatorname{rank}[P\;R]&
\operatorname{rank}[P\;R\;\partial_tR]&
\dim\mathcal R_{\partial_t}\\
\hline
1009&1389&1393&1397&0\\
1013&1389&1393&1397&0
\end{array}
\]

Here \(P\) is the enlarged labelled-primitive matrix and the four columns in
each scalar block are \(1,t,t^2,t^3\). Since all four derivative columns add
rank modulo \([P\;R]\), no nonzero scalar polynomial of degree at most three
multiplies \(\partial_tR\) into the enlarged primitive span.

Therefore

\[
\boxed{
\text{the first fiber-coordinate numerator grade does not restore a genuine
five-site order-one relation through scalar degree three.}
}
\]

## Meaning

The earlier failure is not a constant-numerator artifact at the first
available numerator grade. If a projective labelled order-one relation exists,
it requires higher numerator structure, a different source-derived complex,
or additional supported/coherence data. Increasing a preferred primitive
section without changing its typing has now failed twice.

This supports the structured-ambiguity diagnosis only negatively: enlarging
representatives is not a substitute for deriving the admissible
transformation or relative-support object. It does not identify that object.

## Limits and next falsifier

The result is modular and sample-based. It tests numerator basis
\((1,u_1,u_2,u_3)\) and scalar degree at most three only. It does not exclude
quadratic fiber numerators, rational numerator modules, or derived boundary
cells.

The sharp next step is not an unbounded numerator escalation. Entry 1404
proves that the asymmetric Kummer profile used here admits no affine lift of
the source \(C_5\) action, so cyclic averaging on this chart is prohibited.
There are two typed continuations:

1. retain this chart and test only the associated-graded quadratic
   top-symbol module, without claiming cyclic descent; or
2. return to the generic cyclicly labelled Kummer base, construct the
   equivariant primitive module there, and specialize only afterward.

A relative boundary cell or coherence homotopy remains preferable if it can
be derived from the source before either numerator escalation.

## Evidence

- `research/nima/check_five_site_projective_labelled_order_one_linear_numerators.py`
- `research/nima/results/five-site-projective-labelled-order-one-linear-numerators.json`
- run manifest:
  `C:/Users/andrey/.codex/tmp/marici-nima-linear-numerator-1500-rerun.json`
- allocator claim: `seqclaim-155e290548e9924fb02ba22f`
