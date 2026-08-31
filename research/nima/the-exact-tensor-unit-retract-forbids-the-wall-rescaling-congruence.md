# The exact tensor-unit retract forbids the wall-rescaling congruence

## Question

The independent wall/tail history block

\[
G_{\rm hist}=\begin{pmatrix}1+M^2&M\\M&1\end{pmatrix}
\]

is abstractly congruent to the saturated block

\[
G_{\rm sat}=\begin{pmatrix}1+M^2&0\\0&1\end{pmatrix},
\]

but the triangular congruence requires wall scale
\(s=\sqrt{1+M^2}\).  This note checks that scale against the already proved
canonical tensor-unit retract.

## Exact retract constraint

Let \(\iota\) be the diagonal-orbit inclusion of one source copy and let
\(\epsilon_1\) be evaluation at the multiplicative tensor unit followed by the
frozen inverse normalization.  The established categorical identity is

\[
\epsilon_1\iota=I.
\]

Let \(W=\operatorname{ran}\iota\) be the tensor-unit wall line, and let \(T\)
be the tail channel killed by the wall counit.  A source-natural change of
auxiliary coordinates must preserve the counit square:

\[
\epsilon_1 S\iota=I.
\]

For a triangular wall/tail transformation

\[
S(w,t)=(aw,cw+t),
\]

with \(\epsilon_1|_T=0\), one has

\[
\epsilon_1S\iota=aI.
\]

Therefore exact counit compatibility forces

\[
a=1.
\]

This is not merely a choice of Hilbert normalization: replacing \(a\) by a
nonunit scalar changes the recovered Stieltjes boundary copy.  Compensating by
rescaling \(\epsilon_1\) would replace the canonical counit and destroy the
already checked identity rather than prove compatibility with it.

## Conflict with the block congruence

The exact triangular history-to-saturated calculation gives two necessary
conditions:

\[
c=-Ma,
\qquad
|a|^2=1+M^2.
\]

The completed theta mass satisfies \(M>0\), so

\[
|a|=\sqrt{1+M^2}>1.
\]

This contradicts the source-natural requirement \(a=1\).  Hence no triangular
congruence that preserves both the tail associated grade and the canonical
tensor-unit counit converts \(G_{\rm hist}\) into \(G_{\rm sat}\).

The conclusion is invariant under a phase convention: exact recovery fixes
\(a=1\), while metric matching fixes its modulus strictly above one.

## What remains possible

This rules out only a two-port, counit-preserving triangular identification.
Three routes remain logically available:

1. **History target.**  The source-authorized completed Green form is
   \(G_{\rm hist}\), and the saturated zero-cross-term form is only a different
   observer topology, not the first-Adams target metric.
2. **Additional Schur port.**  A third metric-bearing channel contributes the
   missing \(M^2\) wall energy after the counit-preserving shear
   \((w,t)\mapsto(w,t-Mw)\).  The two-port history block then reduces to
   \(I\), so the extra port must return exactly \(M^2\|w\|^2\) and no unwanted
   mixed term.
3. **Nontriangular typed comparison.**  A source theorem may mix wall and tail
   in both directions while preserving the counit as a morphism of the full
   completed object.  Such a map must be written explicitly and tested against
   the tail quotient, odd port, reflection, and radicals; abstract positive
   congruence is insufficient.

## Sharpened Schur specification

Under the canonical counit-preserving shear

\[
S_0=\begin{pmatrix}1&0\\-M&1\end{pmatrix},
\qquad
S_0^*G_{\rm hist}S_0=I,
\]

the exact deficit relative to the saturated target is

\[
G_{\rm sat}-I=
\begin{pmatrix}M^2&0\\0&0\end{pmatrix}.
\]

Thus an additional-port repair is now completely specified: its Schur return
on the independent wall/tail block must be the rank-one positive operator

\[
M^2P_W.
\]

The next source search should therefore look for a retained wall observer with
amplitude \(M\), orthogonal after the counit-preserving shear, rather than for
wall–tail vanishing or arbitrary rescaling.

## Status

The canonical tensor-unit retract answers the previous binary question: the
required wall rescaling is **not source-natural**.  G1.1 remains open.  The
earliest constructive alternative is now the explicit rank-one Schur return
\(M_\Phi^2P_W\), or a proof that the shifted-history form itself is the target.
