# 1664 — Only a Predeclared Time-Reversal Character Removes the Residual Derivative Counterterm

## Symmetry audit

Entry 1663 leaves the Hermitian family

\[
H_\lambda=qpq+\lambda\hbar q.
\]

Test which ordinary source symmetries can distinguish the finite counterterm.

## Symmetry characters

Under phase-space inversion

\[
q,p\mapsto-q,-p,
\]

both \(qpq\) and \(\hbar q\) are odd.

Under canonical scaling

\[
q\mapsto s q,
\qquad
p\mapsto s^{-1}p,
\]

both have weight \(+1\).

Thus parity and scaling leave \(\lambda\) unconstrained.

Under antiunitary time reversal,

\[
q\mapsto q,
\qquad
p\mapsto-p,
\]

the characters differ:

\[
qpq\mapsto-qpq,
\qquad
\hbar q\mapsto+\hbar q.
\]

Therefore a source requirement that the interaction be purely time-reversal odd forces

\[
\boxed{\lambda=0.}
\]

The checker verifies all 257 integer values of \(\lambda\); only zero has the pure odd character.

## Narrow result

\[
\boxed{
\text{The residual counterterm is removed by time-reversal parity only when that parity is independently frozen in the source.}
}
\]

This condition cannot be assumed in a cosmological sector carrying a chosen time orientation, Bunch--Davies boundary condition, or time-asymmetric regulator. If the source does not preserve the required antiunitary character, \(\lambda\) remains renormalization-scheme coefficient data.

Carrier geometry, Cut coherence, parity, and scaling do not determine it.

## Durable artifacts

- research/benincasa/checkers/derivative_counterterm_symmetry.rs
- research/benincasa/results/derivative-counterterm-symmetry.json
- research/benincasa/derivative-counterterm-symmetry.md

## Next falsifier

Audit the actual cosmological source action and boundary prescription before applying this conditional theorem. Determine whether the relevant derivative interaction has a declared antiunitary time-reversal character. If not, stop the ordering branch at the scheme parameter rather than setting \(\lambda=0\) by analogy.
