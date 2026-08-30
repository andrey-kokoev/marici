# 1662 — Cut Coherence Cannot Select the Quantum Ordering of a Derivative Interaction

## Hostile test

Entry 1661 proves arity-uniform coherence for position-polynomial interactions, whose primitive force has no ordering ambiguity. Test a derivative interaction involving both \(q\) and \(p\).

## Classically equivalent quantum family

The Weyl quantization of the classical symbol \(q^2p\) is

\[
H_W
=
\frac13(q^2p+qpq+pq^2)
=
qpq.
\]

The Hermitian family

\[
H_\lambda
=
qpq+\lambda\hbar q,
\qquad
\lambda\in\mathbb R,
\]

has the same classical symbol.

Its primitive equations are

\[
Dq=q^2,
\]

\[
\boxed{
Dp=-(pq+qp)-\lambda\hbar.
}
\]

Thus \(\lambda\) changes the primitive quantum force while disappearing in the classical limit.

## Cut-coherence blindness

In the homogenized CCR coalgebra, \(\hbar\) is primitive. Therefore

\[
\Delta(-\lambda\hbar)
-\left(-\lambda\hbar_L-\lambda\hbar_R\right)
=0.
\]

The ordering shift contributes nothing to the co-Leibniz defect. The checker verifies this for 257 integer values of \(\lambda\); all 256 nonzero values change the primitive force, while all 257 leave the Cut defect unchanged.

## Narrow result

\[
\boxed{
\text{Cut sewing and higher coherence cannot determine the quantum ordering of a derivative interaction.}
}
\]

Once the ordering is frozen, the homogenized Weyl calculus remains coherent. But the choice itself must come from independent source authority:

- the primary Hamiltonian;
- a regulator;
- a symmetry or self-adjointness prescription;
- renormalization conditions.

This is a sharp boundary of the shared-carrier program. Carrier geometry and Cut calculus constrain transport of coefficient data; they do not manufacture missing sector dynamics.

## Durable artifacts

- research/benincasa/checkers/derivative_interaction_ordering.rs
- research/benincasa/results/derivative-interaction-ordering.json
- research/benincasa/derivative-interaction-ordering.md

## Next falsifier

Freeze Weyl ordering and test whether the resulting derivative interaction preserves the positivity/process-tensor architecture of Entries 1641–1646. In particular, determine whether its momentum-dependent Cut loading remains completely positive after internal pushforward or requires additional source-derived contact terms.
