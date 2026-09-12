# Orientation reversal either changes type or doubles the realization

## Frozen sewing type

For oriented sewing alone, a residual line with charges

\[
(q_{\rm in},q_{\rm out})
\]

has rank-one pair behavior. This justified its one-dimensional realization relative to that protocol.

## Admit reversal

Let \(R\) reverse orientation and exchange the two charges:

\[
R(q_{\rm in},q_{\rm out})=(q_{\rm out},q_{\rm in}),
\qquad R^2=1.
\]

Using the two continuation words \(\{1,R\}\), the scalar Hankel matrix is

\[
H_R=
\begin{pmatrix}
q_{\rm out}&q_{\rm in}\\
q_{\rm in}&q_{\rm out}
\end{pmatrix}.
\]

Its determinant is

\[
\det H_R=q_{\rm out}^2-q_{\rm in}^2.
\]

Therefore its generic rank is two. Rank one occurs only on the self-dual or anti-self-dual loci

\[
q_{\rm out}=q_{\rm in}
\quad\text{or}\quad
q_{\rm out}=-q_{\rm in}.
\]

## Two lawful formulations

### Typed variance

Keep the residual one-dimensional, but let reversal change its orientation type:

\[
L_{\rightarrow}\xrightarrow{R}L_{\leftarrow}.
\]

Then reversal is a morphism between two typed fibers, not an endomorphism of one stationary state space.

### Stationary closure

Demand that reversal act internally. The minimal closed carrier is generically

\[
L_{\rightarrow}\oplus L_{\leftarrow},
\]

with dimension two. Its symmetric and antisymmetric lines diagonalize reversal.

Neither presentation is intrinsically preferable. They answer different questions: varying type preserves minimal local dimension, while stationary closure internalizes the context action.

## Consequence

The “two-way possibility” is not cosmetic. Once both orientations are executable, it appears mathematically as either:

- contravariant type transport; or
- a doubled state realization.

Thus

```text
one-dimensional primitive
+ admitted reversal
= two oriented one-dimensional fibers
  or one two-dimensional stationary fiber
```

This is the first explicit context that enlarges the static sewing realization.

## Verification

The checker tests 199 exact-rational charge pairs. Generic pairs have Hankel rank two; the three sampled self-dual or anti-self-dual cases have rank one:

```text
python research/coherence/check_reversal_context_hankel_rank.py
```

Artifacts:

- `check_reversal_context_hankel_rank.py`
- `reversal-context-hankel-rank.v1.json`
