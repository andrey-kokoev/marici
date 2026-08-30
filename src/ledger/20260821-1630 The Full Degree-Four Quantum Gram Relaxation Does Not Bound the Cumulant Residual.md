# 1630 — The Full Degree-Four Quantum Gram Relaxation Does Not Bound the Cumulant Residual

## Falsifier

Entry 1629 found unbounded mixed fourth moments in a minimal \((1,Q^2,S)\) Gram object.  Test whether the missing \(P^2\) row and column, the complete covariance block, and all quadratic commutator entries remove that unbounded direction.

## Full parity-even basis

Use

\[
(1,Q,P,Q^2,S,P^2),
\qquad
S=\frac{QP+PQ}{2},
\qquad
[Q,P]=2i.
\]

On the parity-even specialization the odd \((Q,P)\) block decouples from the even quadratic block.

Freeze

\[
\langle Q^2\rangle=1,
\qquad
\langle S\rangle=0,
\qquad
\langle P^2\rangle=2,
\qquad
\langle Q^4\rangle=2.
\]

The covariance uncertainty condition passes:

\[
1\cdot2-0^2\geq1.
\]

## Exact unbounded family

For arbitrary real

\[
Z=\operatorname{Re}\langle Q^2S\rangle,
\]

choose

\[
\langle S^2\rangle=Z^2+5,
\qquad
\langle P^4\rangle=4Z^2+9,
\]

and set the remaining real quadratic cross entries to zero.

The canonical commutators force

\[
\operatorname{Im}\langle Q^2S\rangle=2,
\]

\[
\operatorname{Im}\langle Q^2P^2\rangle=0,
\]

\[
\operatorname{Im}\langle SP^2\rangle=4.
\]

The leading \((1,Q^2,S)\) determinant is exactly one.  The Schur cost of the \(P^2\) column is \(4Z^2+8\), so the full even-block Schur complement is also exactly one.

Thus the entire degree-four Gram matrix is positive definite for every \(Z\).

The checker verifies 1,001 exact members with \(-500\leq Z\leq500\).

## Narrow result

\[
\boxed{
\text{Degree-four quantum Gram positivity and exact canonical commutators do not bound the mixed fourth-cumulant direction on a fixed covariance fiber.}
}
\]

Therefore Entry 1627's residual functional is unbounded on this truncated relaxation.  Dynamical control requires extension/localizing conditions from degree six or eight, not merely completion of the degree-four matrix.

## Type qualification

The constructed packets are exact positive truncated noncommutative moment functionals.  This does not prove that each extends to a trace-class density operator.  The failure of the degree-four relaxation means precisely that extension data are necessary.

## Architectural consequence

The coefficient system requires a genuine moment tower or a source-derived finite closure.  A standalone \(\kappa_4\) object—even when accompanied by every degree-four Gram entry—is insufficient.  This strengthens the warning

\[
\text{associated grade}
\not\Rightarrow
\text{complete physical coefficient object}.
\]

No new carrier stratum is indicated.

## Durable artifacts

- `research/benincasa/checkers/full_even_degree4_gram_unbounded.rs`
- `research/benincasa/results/full-even-degree4-gram-unbounded.json`
- `research/benincasa/full-even-degree4-gram-unbounded.md`

## Next falsifier

Apply the degree-six flat-extension criterion to this exact family.  Determine whether any nonzero \(Z\) admits a rank-preserving extension compatible with multiplication by \(Q\) and \(P\).  If flat extension forces a bound or a discrete locus, derive it; if unbounded extensions survive, the required coefficient object is necessarily infinite or source-cutoff dependent.
