# 1658 — Cubic Weyl Evolution First Adds a Central Grade at the Third Momentum Moment

## Question

Entry 1657 supplies the correctly typed homogenized CCR algebra. Determine whether normal ordering changes the primitive interaction coherence or first appears only in higher moment coefficients.

## Primitive relations

With

\[
[q,p]=i\hbar,
\qquad
H_{\rm int}=\frac{q^3}{3},
\]

the primitive evolution rules remain

\[
Dq=p,
\qquad
Dp=-q^2.
\]

Hence Entry 1655's primitive co-Leibniz defect receives no ordering correction.

## Normal-ordered hierarchy

The exact commutator formula is

\[
[p^m,q^3]
=
\sum_{k=1}^{\min(m,3)}
(-i\hbar)^k k!
\binom mk\binom3k
q^{3-k}p^{m-k}.
\]

Therefore

\[
D(p^m)
=
-m q^2p^{m-1}
+2i\hbar\binom m2qp^{m-2}
+2\hbar^2\binom m3p^{m-3}.
\]

The first central term occurs at \(m=3\):

\[
\boxed{
D(p^3)
=
-3q^2p^2+6i\hbar qp+2\hbar^2.
}
\]

The checker verifies the formula through \(m=32\); all thirty degrees \(m\ge3\) carry a nonzero \(\hbar^2\) contribution.

## Narrow result

\[
\boxed{
\text{Quantum ordering leaves the primitive cubic coherence unchanged but enriches the higher-moment filtration beginning at }p^3.
}
\]

The central \(2\hbar^2\) term is genuine quantum coefficient data. It does not define a new carrier incidence and does not invalidate the commutative associated grade. Instead it shows precisely where the quantum filtered module departs from its classical symbol.

## Durable artifacts

- research/benincasa/checkers/weyl_cubic_normal_ordering.rs
- research/benincasa/results/weyl-cubic-normal-ordering.json
- research/benincasa/weyl-cubic-normal-ordering.md

## Next falsifier

Compute the co-Leibniz defect on \(p^3\) in the homogenized CCR coalgebra and test the ternary cocycle including the \(2\hbar^2\) term. Determine whether primitive-\(\hbar\) coproduct absorbs the central grade coherently or leaves a supported quantum residual.
