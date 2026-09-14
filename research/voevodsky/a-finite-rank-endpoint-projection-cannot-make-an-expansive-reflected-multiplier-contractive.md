# A finite-rank endpoint projection cannot make an expansive reflected multiplier contractive

## Proposed complementary contraction

The endpoint-projection construction proposed

\[
L_{S,L}
=(I-P_{end,L})M_{\Theta_S}^*
\]

and asked whether

\[
\|L_{S,L}
\|
\le1
\]

could hold even when the full reflected multiplier is not contractive. Here `P_end,L` has rank at most two.

In an infinite-dimensional Hardy or strip limit, finite-rank projection cannot remove essential multiplier expansion.

## Essential-norm invariance

Let `T` be a bounded operator and `P` a finite-rank orthogonal projection. Then

\[
(I-P)T=T-PT,
\]

and `PT` is finite rank. Hence

\[
\boxed{
\|(I-P)T\|_{ess}
=
\|T\|_{ess}.
}
\]

Therefore

\[
\boxed{
\|(I-P)T\|
\ge
\|T\|_{ess}.
}
\]

Applied to `T=M_Theta^*`, this gives

\[
\boxed{
\|(I-P_{end})M_\Theta^*\|
\ge
\|M_\Theta\|_{ess}.
}
\]

Thus complementary contractivity requires at least

\[
\|M_\Theta\|_{ess}
\le1.
\]

A rank-two endpoint projection can remove at most discrete singular directions, not expansion present in the essential spectrum.

## Bounded Hardy multiplier case

If `Theta` is a bounded analytic multiplier on an ordinary Hardy domain, then

\[
\|M_\Theta\|
=
\|M_\Theta\|_{ess}
=
\|\Theta\|_{L^\infty(boundary)}

=
\|\Theta\|_{H^\infty}
\]

under the standard hypotheses. Consequently

\[
\|(I-P_{end})M_\Theta^*\|
\le1
\]

implies

\[
\|\Theta\|_\infty
\le1.
\]

In that setting the proposed endpoint-compressed condition is not weaker than Schur contractivity at the essential level.

It may remove finitely many singular values above one for a compact perturbation of a contraction, but it cannot repair multiplier expansion on a set of positive boundary measure.

## Strip boundary issue

For the local ratio

\[
\varphi_p(z)=
\frac{m_p^\#(z)}{m_p(z)},
\qquad
m_p(z)=1-p^{-1/2-iz},
\]

one has unit modulus on the central real line, but the natural analytic strip also has the boundary line

\[
\operatorname{Im}z=1/2.
\]

The denominator `m_p` vanishes there at

\[
z=-\frac{2\pi n}{\log p}+\frac{i}{2}.
\]

Hence `varphi_p` is not a bounded multiplier on the full open half-strip approaching that boundary. Its norm cannot be controlled by its unimodular values on the central line alone.

This resolves the apparent contradiction between:

- `|varphi_p(t)|=1` for real `t`;
- failure of the Schur inequality in the strip interior;
- blow-up near the upper endpoint boundary.

A Hardy theory for the strip sees both boundary components, and the upper-boundary singularities form infinitely many prime-frequency channels.

## Infinite-rank survival

Even if one regularizes away from `Im z=1/2`, the prime ratio has regions where its modulus exceeds one. Reproducing kernels concentrated near distinct such regions give asymptotically independent expansive vectors. As the regularization approaches the boundary, their number is unbounded because the zeros occur at every

\[
-\frac{2\pi n}{\log p}+\frac{i}{2}.
\]

Deleting the two-dimensional endpoint span cannot remove this sequence. Thus the prime expansion is not carried solely by the endpoint harmonic modes.

This gives an operator-theoretic version of the infinite-rank truncated-translation obstruction.

## Consequence for the projected factorization

The decomposition

\[
M_\Theta^*
=P_{bulk}M_\Theta^*
+
P_{end}M_\Theta^*
\]

remains exact, but the hoped-for estimate

\[
\|P_{bulk}M_\Theta^*\|
\le1
\]

cannot follow from finite-rank endpoint removal when `M_Theta` has essential expansion.

Therefore the assertion

\[
\text{every expansive direction is endpoint-harmonic}
\]

is false for the raw reflected multiplier carrier once prime boundary channels are active.

## Required renormalization

The primes must first be absorbed into a different common metric or conjugated carrier. Let `W_S` be a source-derived, generally nonunitary weight or outer multiplier, and consider

\[
\widetilde T_S
=W_S
M_{\Theta_S}^*
W_S^{-1}.
\]

Only after proving

\[
\|\widetilde T_S\|_{ess}
\le1
\]

can a finite-rank endpoint projection plausibly remove the residual discrete expansion.

The semilocal Sonin weighting is a candidate for `W_S`, because it makes Euler amplification isometric at each finite stage. But the exact trace observer must be transported through the same conjugation; otherwise the Weil form is changed.

## Revised two-stage theorem

A viable endpoint reduction requires:

1. **essential renormalization**
   \[
   \|W_SM_{\Theta_S}^*W_S^{-1}\|_{ess}
   \le1;
   \]
2. **finite endpoint repair**
   \[
   \|(I-P_{end})
   W_SM_{\Theta_S}^*W_S^{-1}
   \|
   \le1;
   \]
3. **Douglas domination** of the residual endpoint feature by the resulting defect operator.

The first step is infinite-rank and prime-bearing. The latter two can be finite-dimensional.

## Disposition

The raw endpoint-projection fork is closed:

\[
\boxed{
\|(I-P_{end})M_\Theta^*\|_{ess}
=
\|M_\Theta\|_{ess}.
}
\]

A rank-two endpoint projection cannot turn an essentially expansive reflected multiplier into a contraction. The correct order is: first use a semilocal prime-dependent metric to remove essential expansion, then identify and repair any remaining endpoint defect.
