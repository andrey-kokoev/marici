# Theta convolution factors through its wall mass and an integrated derivative tail

## Completed-theta history

The causal seam operator used in the shifted-history square is the
half-line convolution

\[
(H_\Phi c)(t)
=
\int_0^\infty
\Phi(r)c(t+r)\,dr,
\]

where \(\Phi\) is the completed theta kernel. This is not the primitive
Volterra operator.

Define its tail kernel

\[
K(r)
=
\int_r^\infty\Phi(s)\,ds.
\]

Then

\[
K'(r)=-\Phi(r),
\qquad
K(0)=M_\Phi
=
\int_0^\infty\Phi(s)\,ds.
\]

## Exact integration-by-parts factorization

On a rapid differentiable core,

\[
H_\Phi c
=
-\int_0^\infty K'(r)c(t+r)\,dr.
\]

Integration by parts gives

\[
(H_\Phi c)(t)
=
M_\Phi c(t)
+
\int_0^\infty
K(r)c'(t+r)\,dr.
\]

If \(H_K\) denotes half-line convolution with the tail kernel \(K\), then

\[
H_\Phi
=
M_\Phi I
+
H_KD_t.
\]

This is an exact source-derived decomposition.

## Meaning of the two terms

The first term is the wall channel:

\[
M_\Phi I.
\]

The second term is the propagated derivative channel:

\[
H_KD_t.
\]

Therefore the completed-theta history does not require an unrelated map from
the ordered derivative port. It is assembled from precisely:

1. a wall-mass coefficient;
2. the derivative current;
3. a causal tail propagator.

This is the first direct constructor bridge between the window connection
defect and the completed-theta convolution.

## Bounded tail propagation

Because \(\Phi\) decays rapidly,

\[
\|K\|_{L^1(0,\infty)}
=
\int_0^\infty r\Phi(r)\,dr
\]

when \(\Phi\ge0\). More generally the absolute first moment bounds
\(\|K\|_1\).

Young's inequality gives

\[
\|H_Kg\|_2
\le
\|K\|_1\|g\|_2.
\]

Hence

\[
H_\Phi:
H^1\longrightarrow L^2
\]

is continuous through the wall-plus-derivative factorization, with

\[
\|H_\Phi c\|
\le
M_\Phi\|c\|
+
\|K\|_1\|c'\|.
\]

On the source joint graph, the derivative term is already controlled by the
comoving connection topology.

## Relation to the ordered port

On the wall-killed sector, the ordered port is the inverse derivative:

\[
S_{\mathrm{ord}}D=-2I.
\]

Thus

\[
H_\Phi S_{\mathrm{ord}}D
=
-2H_\Phi.
\]

More usefully, the factorization shows that the derivative current entering
the ordered port is the same current consumed by \(H_K\). The ordered
history records orientation; \(H_K\) supplies bounded completed-theta
propagation.

They are complementary constructors, not competing definitions of one
operator.

## Reflection

The reflected causal history has the opposite half-line kernel. Reflection
fixes the scalar wall mass and exchanges the derivative-tail term with its
adjoint orientation. Therefore

\[
H_\Phi-H_\Phi^*
\]

has no independent scalar wall contribution when the wall coefficients match;
its oddness is carried by the two oriented tail propagators.

This is exactly the typing required for the auxiliary history numerator.

## Normalization consequence

The identity coefficient in the theta-history carrier is not automatically
one. The factorization supplies

\[
M_\Phi I.
\]

To compare it with the coefficient-window wall represented as \(I\), one
must prove the source normalization or retyping map that sends
\(M_\Phi I\) to the declared wall coefficient \(\sqrt\lambda I\).

The factorization exposes this coefficient rather than hiding it.

## New finite gate

The history-comparison arrow now reduces to the compatibility of three
source maps:

\[
\text{window wall}
\longrightarrow
M_\Phi I,
\]

\[
\text{window connection derivative}
\longrightarrow
D_t,
\]

\[
\text{theta tail synthesis}
\longrightarrow
H_K.
\]

The second is controlled by the moving-center connection theorem. The third
is bounded by the theta first moment. The live authority question is the
first map and the exact coefficient frame.

## Hostile

Drop the boundary term in integration by parts and write
\(H_\Phi=H_KD_t\). The odd derivative response remains correct, but the
wall mass disappears, so the shifted-history square receives the wrong
identity coefficient.

## Frontier

The previously missing kernel-synthesis arrow has an exact candidate:

\[
H_\Phi
=
M_\Phi I+H_KD_t.
\]

What remains is to transport this identity through the two-ray
half-density/window comparison and prove that its wall term is the same
source wall used by the multiplication-history Gram.
