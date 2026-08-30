# 1660 — The Complete First Quantum Cut Defect Needs No Ternary Cell

## Decisive coherence test

Entry 1659 computes the complete eight-term binary defect \(\Theta_D(p^3)\), including the central cross term \(4\hbar_L\hbar_R\). Test its full three-occurrence co-Hochschild identity.

## Exact three-factor Weyl calculation

Use occurrence-resolved generators

\[
(q_i,p_i,\hbar_i),
\qquad i=1,2,3,
\]

with

\[
[q_i,p_i]=i\hbar_i,
\]

vanishing cross-occurrence commutators, and primitive coproducts.

The checker normal-orders both routes:

\[
L
=
(\Delta\otimes1)\Theta_D
+(\Theta_D\otimes1)\Delta,
\]

\[
R
=
(1\otimes\Delta)\Theta_D
+(1\otimes\Theta_D)\Delta.
\]

For \(p^3\), each route contains 39 nonzero normal-ordered terms, of which three are pure-central occurrence terms.

The result is

\[
\boxed{L=R}
\]

coefficientwise, with no scalar residual.

## Narrow result

\[
\boxed{
\text{The complete first quantum co-Leibniz defect is already a coherent cocycle; no independent ternary quantum cell is required.}
}
\]

Primitive occurrence-labelled \(\hbar_i\) absorbs both ordering and sewing corrections. The quantum coefficient filtration enriches the binary defect but preserves its inherited higher coherence.

This closes the first quantum-ordering falsifier for the cubic moment \(p^3\). It does not prove all-arity closure for arbitrary interaction polynomials or renormalized field-theory products.

## Architectural consequence

At this tested grade, the cosmological process object is a coherent lax differential coalgebra in the homogenized CCR category:

- interaction determines the binary defect;
- normal ordering contributes central occurrence terms;
- coassociativity determines the ternary identity;
- fixed-\(\hbar\) specialization must occur only afterward.

No new carrier primitive is supported.

## Durable artifacts

- research/benincasa/checkers/weyl_p3_cohochschild_cocycle.rs
- research/benincasa/results/weyl-p3-cohochschild-cocycle.json
- research/benincasa/weyl-p3-cohochschild-cocycle.md

## Next falsifier

Generalize from the cubic potential to \(q^d/d\) and compute the first normal-ordering grades and co-Hochschild closure uniformly in \(d\). Determine whether the partition/binomial rule remains arity-uniform or whether some interaction degree introduces an independent quantum coherence.
