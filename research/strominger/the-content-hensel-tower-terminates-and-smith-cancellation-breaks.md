# The content Hensel tower terminates and Smith cancellation breaks

## Predictions tested

The first-jet theorem suggested two bold higher-order predictions:

1. the exceptional class \(n\equiv2\pmod3\) has a unique lift with an
   additional factor of 3 in \(d_1\);
2. the cancellation
   \[
   v_3(d_3)=v_3(d_2)+v_3(d_1)
   \]
   persists on every lift.

Both predictions are false.

## First unfitted lift fiber

The three representatives modulo 9 are

\[
n=2,5,8.
\]

Their valuation packets are:

\[
\begin{array}{c|ccc|c}
n&v_3(d_1)&v_3(d_2)&v_3(d_3)&v_3(I)\\
\hline
2&2&5&7&0\\
5&2&4&6&0\\
8&2&4&7&1
\end{array}
\]

No representative has \(v_3(d_1)\ge3\). Therefore the content tower
terminates at valuation two.

## Higher information moves to larger minors

Although \(d_1\) is constant across the lift fiber, \(d_2\) and \(d_3\)
are not. The first-jet content partition is therefore too coarse to capture
the second congruence layer.

The higher distinction migrates:

\[
\text{entry content}
\longrightarrow
\text{higher determinantal divisors}.
\]

This is not a deeper zero of the same content coordinate.

## Cancellation failure

At \(n=8\),

\[
v_3(d_3)-v_3(d_2)-v_3(d_1)
=7-4-2
=1.
\]

Thus one factor of 3 survives in the snake index. The terminal quotient is
not uniformly blind to the higher jet.

The correct hierarchy is:

- modulo 3, the source jet distinguishes three classes;
- modulo 9, the content port remains constant on the exceptional fiber;
- higher minors split that fiber;
- the Smith quotient detects at least one of the new classes.

## Explanatory revision

The first-jet theorem remains exact at its declared grade. It does not
self-close under higher congruence lifting.

The system is not governed by one scalar Hensel tower. Successive congruence
layers can change which determinantal grade carries the information.

This suggests a determinantal filtration rather than a content filtration:

\[
(d_1,d_2,d_3)
\]

must be retained as a graded residual packet. Projecting to \(d_1\) alone
loses the higher lift; projecting immediately to the Smith ratio can either
erase or preserve it depending on the class.

## Theorem status

The three representatives of the first unfitted lift fiber are computed
exactly. The rank defect persists in all three. Six of six hostile-result
gates pass.

## Claim boundary

This is a finite modulus-9 classification of the exceptional mod-3 fiber. It
does not yet classify all nine residue classes or prove a general recurrence
for the full determinantal valuation packet.
