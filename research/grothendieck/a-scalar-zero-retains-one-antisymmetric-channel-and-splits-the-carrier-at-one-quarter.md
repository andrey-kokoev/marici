# A scalar zero retains one antisymmetric channel and splits the carrier at one quarter

## Faithful coordinates for the three-channel packet

For

\[
\xi=C+U+V,
\qquad
C=\frac12,
\]

introduce

\[
S=C+U+V,
\qquad
A=U-V,
\qquad
B=2C-U-V.
\]

The linear transformation is invertible before fixing \(C\):

\[
C=\frac{S+B}{3},
\qquad
U+V=\frac{2S-B}{3},
\]

with \(U-V=A\).  On the completed theta source, \(C=1/2\) is fixed, so

\[
S+B=\frac32.
\]

The full source curve is therefore faithfully represented by the scalar
readout \(S\) together with the antisymmetric comparison channel \(A\).

## What survives at a zero

At a scalar zero,

\[
S=0,
\qquad
B=\frac32,
\qquad
U+V=-\frac12.
\]

Thus a zero does not erase the packet.  It fixes the symmetric control
contrast and leaves the antisymmetric channel \(A\) as the complete residual
coordinate:

\[
U=-\frac14+\frac A2,
\qquad
V=-\frac14-\frac A2.
\]

The scalar zero fiber is an affine line, not a null object.

## Reciprocal fixed locus

Reciprocity acts by

\[
S\longmapsto S,
\qquad
B\longmapsto B,
\qquad
A\longmapsto-A.
\]

Complex conjugation acts by \(A\mapsto\overline A\).  On the combined fixed
locus \(s=1-\overline s\), one has

\[
A=-\overline A,
\]

so \(A\) is purely imaginary.  Therefore a critical-line zero has

\[
U=-\frac14+i\alpha,
\qquad
V=-\frac14-i\alpha
\]

for some real \(\alpha\).

This supplies an exact meaning for the quarter offset in the channel
geometry: at cancellation, the fixed completion carrier \(1/2\) is shared
equally between the two reciprocal sectors, producing the baseline
\(-1/4\) in each.  This is not yet an identification with every earlier
appearance of \(1/4\), but it is a source-derived occurrence rather than a
fitted spectral shift.

## Revised loss-of-meaning statement

The scalar readout loses meaning at a zero only because it discards \(A\).
The complete relational state remains:

\[
(S,A,B)=\left(0,A,\frac32\right).
\]

On the critical line its residual lives on the imaginary \(A\)-axis.  An
off-line zero would be the same scalar cancellation with a residual channel
not fixed by reciprocal conjugation.

RH can therefore be sharpened to:

\[
S(s)=0
\quad\Longrightarrow\quad
s=1-\overline s,
\]

while the observable signature of the target locus is

\[
S=0,
\qquad
A\in i\mathbb R,
\qquad
B=\frac32.
\]

The converse implication from \(A\in i\mathbb R\) to the base fixed locus is
not automatic.  Proving it for zero states would itself be an RH-equivalent
source-faithfulness theorem.  Hostile carriers must be tested against this
residual coordinate rather than only against \(S\).

## Next gate

The source curve should now be studied in the faithful two-coordinate chart

\[
s\longmapsto(S(s),A(s)).
\]

The sharp target is a source-derived orientation or monotonicity law that
prevents \(S\) from vanishing when \(A\) is outside the imaginary fixed axis.
This is strictly stronger than scalar positivity and strictly weaker than
reconstructing the entire labelled theta source.

