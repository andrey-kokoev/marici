# The theta-history Gram contains two distinct wall-scale contributions

## Tail decomposition

The completed-theta history has the exact form

\[
H_\Phi
=
M_\Phi I+B,
\qquad
B=H_KD_t,
\]

where

\[
M_\Phi
=
\int_0^\infty\Phi(r)\,dr.
\]

Assume the frozen theta normalization makes \(M_\Phi\) real. Then

\[
H_\Phi^*
=
M_\Phi I+B^*.
\]

## Odd part

The scalar wall mass cancels from the causal odd operator:

\[
H_\Phi-H_\Phi^*
=
B-B^*.
\]

Thus reciprocal orientation is carried entirely by the derivative-tail
propagation. The theta mass contributes no independent odd scalar.

This agrees with the constructor typing: wall mass is reflection-even, while
the connection derivative and causal direction carry the reciprocal
character.

## Even graph energy

The history Gram expands as

\[
H_\Phi^*H_\Phi
=
M_\Phi^2I
+
M_\Phi(B+B^*)
+
B^*B.
\]

Therefore the canonical graph energy is

\[
S_{\mathrm{gr}}
=
\frac12
\left[
(1+M_\Phi^2)I
+
M_\Phi(B+B^*)
+
B^*B
\right].
\]

The two identity-looking terms have different provenance:

1. \(I\) is the domain or retained coefficient-wall energy;
2. \(M_\Phi^2I\) is the squared output wall mass inside
   \(H_\Phi^*H_\Phi\).

They must not be merged before the history-comparison map proves they inhabit
one source frame.

## Reciprocal squares

The exact blocks remain

\[
D_\pm
=
\frac12(I\pm iH_\Phi)^*(I\pm iH_\Phi).
\]

After substituting \(H_\Phi=M_\Phi I+B\),

\[
I\pm iH_\Phi
=
(1\pm iM_\Phi)I
\pm iB.
\]

Hence the scalar part already has modulus

\[
|1\pm iM_\Phi|
=
\sqrt{1+M_\Phi^2}.
\]

The dangerous cancellation is between this complex wall coefficient and the
tail operator \(B\), not between a unit wall and the full history viewed as
an unrelated perturbation.

## Improved tail criterion

If \(B\) is bounded and

\[
\|B\|
<
\sqrt{1+M_\Phi^2},
\]

then

\[
\|(I\pm iH_\Phi)f\|
\ge
\left(
\sqrt{1+M_\Phi^2}-\|B\|
\right)
\|f\|.
\]

Therefore

\[
D_\pm
\ge
\frac12
\left(
\sqrt{1+M_\Phi^2}-\|B\|
\right)^2I.
\]

This can be sharper than the coarse condition \(\|H_\Phi\|<1\), because
the known wall mass is treated exactly rather than estimated as part of the
history norm.

## First-moment estimate

From \(B=H_KD_t\),

\[
\|Bf\|
\le
\|K\|_1\|D_tf\|.
\]

Thus on a source carrier where

\[
\|D_tf\|
\le
C_D\|f\|,
\]

a sufficient shifted-history condition is

\[
C_D\|K\|_1
<
\sqrt{1+M_\Phi^2}.
\]

On the joint graph carrier, \(B\) is bounded into the analytic output, but
an endomorphism estimate still requires the source and output norms to be
identified by the authorized comparison.

## Normalization correction

The coefficient extraction cannot summarize the theta history by one wall
number \(M_\Phi\). At quadratic level it must retain:

\[
I,
\qquad
M_\Phi^2I,
\qquad
M_\Phi(B+B^*),
\qquad
B^*B,
\qquad
B-B^*.
\]

Only a source identity may combine these into a smaller weighted square.

## Hostile

Identify the coefficient-window wall \(I\) with the theta output wall
\(M_\Phi I\), then also retain the domain identity in
\(I+H_\Phi^*H_\Phi\). This silently counts one wall comparison twice while
still producing a positive analytic square.

A second hostile deletes \(M_\Phi^2I\) as redundant. The odd history is
unchanged, but the even coercive scale is wrong.

## Frontier

The window/seam comparison must be quadratic and provenance-sensitive. Its
next exact test is whether the source wall maps to:

- the graph-domain identity \(I\);
- the output mass channel \(M_\Phi I\);
- or a diagonal relation connecting both.

Until this is frozen, the shifted-history factorization is analytically exact
but its wall normalization is not yet a constructor theorem.
