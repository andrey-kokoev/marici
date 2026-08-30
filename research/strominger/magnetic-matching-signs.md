# Sign coherence fails, but the actual weights do not cancel

Companion to `checkers/magnetic_matching_sign_checks.py` (8/8, exit 0) and
`results/magnetic_matching_sign.json`. This packet executes Nima's directed
event 2721 and remains entirely combinatorial.

## Three distinct questions

For a Hall-selected square minor, distinguish:

1. **Support matching:** does its bipartite support admit a perfect matching?
2. **Sign-nonsingularity:** do all nonzero determinant terms have one oriented
   sign after any row/column sign normalization?
3. **Actual-weight noncancellation:** does the signed sum remain nonzero at the
   fold's rising-factorial integer weights?

Row and column sign flips multiply every determinant term by one common sign.
They cannot change relative term signs. Thus mixed oriented signs are an
invariant obstruction to sign-nonsingularity.

## The first mixed-sign block

Perfect-matching terms were enumerated for Hall-selected minors over

\[
2\le g\le8,\qquad0\le k\le4,\qquad1\le q\le15.
\]

The first mixed-sign block in lexicographic \((g,k,q)\) order is

\[
\boxed{(g,k,q)=(2,2,2).}
\]

Its selected rows are \((0,2,-3,-2,-6,-4)\). Exactly two determinant terms
survive:

\[
+604{,}800{,}000,qquad-3{,}024{,}000{,}000.
\]

Their sum is

\[
-2{,}419{,}200{,}000\ne0.
\]

Canonical row/column sign normalization leaves the same relative sign
mixture. Therefore the component family is not sign-nonsingular.

## The local mixed core

All unambiguous pivots factor out. The mixed part is the \(2\times2\) block

\[
H=
\begin{pmatrix}-10&100\\-30&60\end{pmatrix}.
\]

Its two matching terms give

\[
\det H=(-10)(60)-100(-30)=-600+3000=2400.
\]

The determinant survives by a factor-five dominance of one matching family,
not by common sign.

The entry \(-10\) is itself an aggregation of the two adjacent-path
contributions

\[
-10=32-42.
\]

Thus a naive positive LGV interpretation also fails at the aggregated-entry
level: opposite signs occur before the determinant is expanded. A finer
signed-network description might still organize these terms, but it would
need a genuine dominance or partial-cancellation identity rather than total
positivity.

## Wide actual-weight noncancellation

For every maximal pole block \(A_{15}\) in

\[
2\le g\le30,qquad1\le q\le60,
\]

the support matching was computed. Every full-Hall block was row-reduced
modulo the prime

\[
p=1{,}000{,}000{,}007.
\]

All 1,740 maximal blocks with complete Hall support have full column rank
modulo \(p\). Nonzero rank modulo a prime proves nonzero integer rank, so this
is an exact actual-weight noncancellation certificate, not probabilistic
evidence. Every smaller \(A_k\), \(k\le15\), is a column subset of the
corresponding maximal block and is therefore independent as well.

No complete-Hall actual-weight cancellation occurs in this widened range.

## Corrected proof target

The proposed sign-coherence theorem is falsified. The remaining unbounded
theorem cannot be

\[
\text{Hall existence}+\text{one oriented sign}.
\]

It must instead be

\[
\boxed{\text{Hall existence}+\text{weight-specific determinant dominance}.}
\]

Possible mechanisms include a signed-network expansion with incomplete
pairwise cancellation, a diagonal-dominance inequality after eliminating
forced pivots, or a closed product formula for the surviving matched minor.
None is yet proved for arbitrary \((g,k,q)\).

## Scope

This is a finite-range oriented-matching theorem. It falsifies structural
sign coherence and certifies actual-weight noncancellation over the displayed
ranges. It does not prove unbounded noncancellation and makes no statement
about potentials, residues, logarithms, or physics.

## Verification

`uv run --with sympy python -u research/strominger/checkers/magnetic_matching_sign_checks.py`
passes 8/8. Coverage: 518 explicitly enumerated Hall minors, the first mixed
block and its path split, and modular exact rank for 1,740 maximal blocks.

