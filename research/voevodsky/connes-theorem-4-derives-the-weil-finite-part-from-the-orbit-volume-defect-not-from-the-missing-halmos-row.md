# Connes Theorem 4 derives the Weil finite part from the orbit-volume defect, not from the missing Halmos row

## Purpose of the audit

The Halmos two-projection decomposition supplies a canonical positive completion of the cutoff matrix. We asked whether the omitted second row of that matrix could have finite part equal to the endpoint--gamma correction.

The proof of Connes's semilocal Theorem 4 shows that this identification is not source-derived.

## Kernel computation in the proof

Connes writes the trace kernel on the semilocal quotient as a sum over `S`-units. After a Fourier transform in the transverse variable and changes of variables, the trace becomes

\[
\operatorname{Tr}(R_\Lambda U(h))
=
\sum_{q\in O_S^*}
\int_{	ext{cutoff domain}}
g_q(u)
\left(2\log\Lambda-\log|u|
ight)du
+
\operatorname{Err}_\Lambda.
\]

The source notation and normalizations are those of equations (28)--(30) in the proof.

The error is controlled by Lemma 2 and decays faster than every power:

\[
\boxed{
\operatorname{Err}_\Lambda
=O(\Lambda^{-N})
\quad\text{for every }N.
}
\]

Thus the theorem contains a stronger remainder estimate than the displayed `o(1)` statement.

## Origin of the universal divergence

Equation (31) proves

\[
\sum_{q\in O_S^*}
\int g_q(u)du
=h(1).
\]

Therefore the constant part of the orbit volume gives

\[
2h(1)\log\Lambda.
\]

This is a geometric volume term arising from the length of the scaling interval. It is not extracted from a prolate eigenmode or endpoint harmonic vector.

## Origin of every local Weil term

The nonconstant part is

\[
-\log|u|
=
-\sum_{v\in S}\log|u_v|_v.
\]

Equation (32), using the local calculation from Section V, proves for each `v in S` that

\[
\sum_{q\in O_S^*}
\int
g_q(u)(-\log|u_v|_v)du
=
\int_{k_v^*}^{\prime}
\frac{h(u^{-1})}{|1-u|_v}d^*u.
\]

Hence

\[
\boxed{
W_S(h)
=
\text{the }-\log|u|
\text{ defect of the semilocal orbit volume}.
}
\]

Gamma and finite primes arise uniformly from the decomposition of the global module into local logarithms.

## Endpoint normalization

The prime on the local integral denotes a principal-value distribution uniquely normalized by requiring its Fourier transform, relative to the basic character, to vanish at `1`.

Thus the local endpoint/normalization information is already built into each principal value. It is not added in Theorem 4 as a separate finite-rank term after the trace calculation.

For the globally completed explicit formula, pole evaluations must still be tracked according to the chosen test-function convention. But within the semilocal theorem, the finite-place functional is obtained directly from normalized local distributions.

## No second-row identity in the proof

The proof uses

\[
R_\Lambda=P_\Lambda\widehat P_\Lambda
\]

in its stated non-self-adjoint order. It never replaces this product with

\[
\widehat P_\Lambda
\]

or with the complete positive Halmos block. In particular, it gives no asymptotic formula for

\[
(I-P_\Lambda)
\widehat P_\Lambda
(I-P_\Lambda),
\]

nor for the omitted second row.

Therefore an assertion of the form

\[
\operatorname*{FP}
(\text{missing Halmos row})
=
\text{endpoint--gamma correction}
\]

is unsupported by the source theorem.

## Why the full Q-trace diverges differently

The Fourier cutoff `Q_Lambda=hat P_Lambda` has infinite-dimensional range on the noncompact semilocal space. For a translation/scaling convolution operator `A=U(g)`, the formal positive trace

\[
\operatorname{Tr}
(Q_\Lambda AA^*)
\]

retains the infinite center-of-mass volume that the left physical cutoff `P_Lambda` was introduced to remove. It is generally not trace class.

Thus the positive completion

\[
PQ
\longrightarrow
Q
\]

changes the divergence class of the trace. The subtraction `2h(1) log Lambda` from Theorem 4 does not renormalize it.

## Correct role of the Halmos block

The Halmos decomposition remains the exact finite-cutoff geometry of the pair `(P,Q)`. It identifies the sewing operator and the prolate angle modes. But its full positive row is a dilation of Connes's cutoff, not another trace covered by Theorem 4.

To use it positively, one needs a **relative** or **trace-per-unit-volume** functional on the full Halmos block whose first-row restriction agrees with Connes's trace finite part.

That functional must be constructed separately and shown to preserve positivity. Ordinary operator trace cannot do this on the full noncompact block.

## Candidate relative trace target

Let `tau_S` denote a semifinite trace or trace density associated with the scaling direction. A viable target would be

\[
\tau_S
\left(
W_\Lambda U(g)U(g)^*W_\Lambda^*
-
2\log\LambdaI_{vol}(g)
\right),
\]

where `I_vol(g)` is the source-derived identity density and the subtraction is implemented inside a relative trace class.

One would need to prove:

1. the relative operator is `tau_S`-trace class;
2. its relative trace equals `W_S(g*g*)`;
3. the subtraction corresponds to a common invariant module, not an arbitrary scalar counterterm;
4. positivity survives in the quotient or relative-trace cone.

None follows from Theorem 4 alone.

## Prime transition compatibility

The orbit-volume proof is naturally compatible with the additive decomposition

\[
-\log|u|_S
=
\sum_{v\in S}-\log|u_v|_v.
\]

Adding a place adds one local principal-value term. This gives exact functional transition compatibility.

It does not provide an operator embedding between the positive Halmos dilations for different `S`. Such an embedding must use the later semilocal Sonin stability theorem and preserve the relative trace density.

## Disposition

The finite-place Weil functional in Connes's theorem is produced by the geometric identity

\[
\boxed{
\text{cutoff orbit volume}
=
2\log\Lambda-\log|u|,
}
\]

not by the omitted second row of the two-projection Gram matrix.

The direct positive-Halmos-completion fork is therefore incomplete: its full trace has a different, generally infinite, volume divergence. The next valid object must be a semifinite or relative trace on the full positive dilation whose renormalized first-row boundary reproduces Connes's orbit-volume finite part.
