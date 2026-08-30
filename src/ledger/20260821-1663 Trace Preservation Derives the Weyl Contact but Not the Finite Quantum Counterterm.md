# 1663 — Trace Preservation Derives the Weyl Contact but Not the Finite Quantum Counterterm

## Positivity test

Entry 1662 shows that Cut coherence cannot select derivative-interaction ordering. Determine how much of the ordering is nevertheless forced by Hermiticity and first-order trace preservation.

## Monomial-ordering family

Use

\[
H_a=q^2p+a\,i\hbar q.
\]

Since

\[
(q^2p)^\dagger
=
pq^2
=
q^2p-2i\hbar q,
\]

one has

\[
H_a^\dagger
=
q^2p-(2+a)i\hbar q.
\]

Hermiticity requires

\[
a=-(2+a),
\qquad
\boxed{a=-1.}
\]

Therefore

\[
\boxed{
H_W=q^2p-i\hbar q=qpq.
}
\]

## Trace defect

For any other \(a\), the first-order evolution has trace defect

\[
-i\langle H_a-H_a^\dagger\rangle
=
2(a+1)\hbar\langle q\rangle.
\]

The checker tests 257 integer orderings. Exactly one is Hermitian; all other 256 have nonzero generic trace defect.

## Residual ambiguity

The family

\[
H_W+\lambda\hbar q,
\qquad
\lambda\in\mathbb R,
\]

remains Hermitian for every \(\lambda\). Hence positivity and trace preservation cannot select the finite real quantum counterterm.

## Narrow result

\[
\boxed{
\text{Trace preservation uniquely derives the Weyl contact needed to repair monomial ordering, but not all Hermitian quantum counterterms.}
}
\]

This refines Entry 1662. Source-independent consistency removes non-Hermitian orderings. Independent source or renormalization authority remains necessary only for the residual Hermitian parameter.

No new carrier structure is involved.

## Durable artifacts

- research/benincasa/checkers/derivative_ordering_trace_contact.rs
- research/benincasa/results/derivative-ordering-trace-contact.json
- research/benincasa/derivative-ordering-trace-contact.md

## Next falsifier

Test whether a predeclared discrete symmetry, time reversal, or scaling Ward identity removes the residual \(\lambda\hbar q\) term in the relevant cosmological derivative interaction. If no frozen symmetry distinguishes it, record \(\lambda\) as genuine renormalization-scheme coefficient data rather than attempting to derive it from Cut geometry.
