# The Clark sheet involution is the sign character of the polarization line

## Question

What scalar cocycle does the native Clark sheet involution induce on the
trace energy and on the oriented seam polarization?

## Clark-output basis

Use the output vector

\[
y=\begin{pmatrix}P\\Q\end{pmatrix}.
\]

The even trace energy is represented by

\[
I=\begin{pmatrix}1&0\\0&1\end{pmatrix},
\]

while the odd sheet polarization is represented by

\[
\eta=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
\]

The sheet involution (a\mapsto-a) exchanges (P) and (Q), hence acts by

\[
S=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

## Even and odd characters

Directly,

\[
S^*IS=I,
\]

but

\[
S^*\eta S=-\eta.
\]

Therefore

\[
|P|^2+|Q|^2
\]

is sheet-even, while

\[
|P|^2-|Q|^2
\]

is sheet-odd.

The conformal multiplier on the polarization line is the nontrivial
character of (C_2):

\[
\chi(S)=-1,
\qquad
\chi(S^2)=1.
\]

## Jet-reflection basis

On the common first jet (x=(F,F')), oriented spectral reflection reverses
the derivative coordinate and is represented locally by

\[
R=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
\]

For the Clark symplectic matrix (Delta_a),

\[
R^*\Delta_aR=-\Delta_a.
\]

Thus sheet swap and oriented jet reflection are both anti-isometries of the
polarization. Their composition is an isometry:

\[
\chi(SR)=1.
\]

This is the algebraic core of the reciprocal two-sheet cancellation.

## What the even scalar readout loses

Any readout factoring only through the even trace energy identifies the two
orientations. It cannot distinguish a constructor word with multiplier
(+1) from one with multiplier (-1) when their even energy is the same.

The lost datum is not an additional amplitude coordinate. It is the torsor
bit specifying the orientation of the polarization line.

A source unit, vacuum, or named sheet may fix that sign frame
mathematically. Such a frame still does not construct a physical operation
that preserves it.

## Closed-word coherence

For a composable word of sheet and reflection constructors, the induced
multiplier is the product of their signs. A closed word that returns the
underlying jet carrier but has odd sign acts nontrivially on the polarization
line.

Therefore a coherent network must satisfy one of three conditions:

1. every declared identity loop has even sign;
2. an orientation cell records and cancels the odd sign;
3. the target intentionally quotients the polarization orientation.

The third choice is legitimate only when no downstream constructor requires
the odd current.

## Theta consequence

The two-sheet energy sum can be positive and sheet-even while the seam
polarization remains odd. Adding the sheets cancels the odd current; it does
not prove that either individual sheet has a preferred sign.

The actual Fourier--Tate constructor must now be assigned its multiplier on
the polarization line. If its ordered action is unavailable, the scalar
completed section cannot determine that multiplier.

## Falsifier certificate

    {
      "code": "clark_sheet_sign_character_erased",
      "even_metric_multiplier": 1,
      "polarization_multiplier": -1,
      "underlying_sheet_action": "swap",
      "downstream_odd_current_required": true
    }

## Disposition

The Clark sheet involution realizes the nontrivial (C_2) character on the
polarization line while acting trivially on total trace energy. The missing
sheet datum is exactly an orientation torsor bit, and network coherence is a
parity law for constructor words.

## Claim boundary

This theorem covers the algebraic sheet swap and local jet reflection. It
does not derive the full Fourier--Tate action, identify its physical
implementation, or prove that every completed constructor is an invertible
conformal action on the first jet.
