# The canonical Tate line is the kernel direction of source sewing

Date: 2026-08-23

Let the marked-Cut occurrence module be the regular module

\[
A=\mathbf F_3[C_3]
\]

and let

\[
\varepsilon:A\to\mathbf F_3
\]

be source sewing, which forgets the occurrence label by summing its
coefficients.  Its kernel is the augmentation ideal

\[
I=\ker\varepsilon.
\]

The previously constructed canonical Tate bridge identifies the residual line
as

\[
H_{\rm Tate}=I/(g-1)I.
\]

Therefore the Tate line is not merely observed to cancel under sewing.  It is
a quotient of the kernel direction of sewing:

\[
\boxed{
H_{\rm Tate}\text{ is invisible to every readout that factors through }
\varepsilon.
}
\]

Over \(\mathbf F_3\),

\[
\dim I=2,
\qquad
\dim(g-1)I=1,
\qquad
\dim H_{\rm Tate}=1.
\]

The exact checker verifies that \(\varepsilon|_I=0\).  As a deliberate
negative control, an occurrence-labelled coordinate readout is nonzero on
\(I\); the no-go is caused by source sewing, not by absence of labelled
information.

## Consequence for the unequal-energy branch

The odd cotangent jet \([d(X_2-X_3)]\) has the correct \(D_3\) character to
map into \(H_{\rm Tate}\).  Even if that coefficient map is nonzero, the
ordinary unsplit physical scalar cannot see it:

\[
L_{\rm asym}
\longrightarrow
H_{\rm Tate}
\longrightarrow
\mathbf F_3
=0
\]

whenever the last arrow factors through \(\varepsilon\).

Thus RS-3 does not require a detailed source connection to decide ordinary
unsplit activation.  That activation is structurally forbidden.  The
remaining meaningful question is whether a separately derived supported or
relative readout retains the boundary class before augmentation.

## Why the soft result survives

The physical soft-normal Gysin map activates an anti-invariant Tate
vanishing-cycle line with multiplicity one.  It is not a scalar readout
factoring only through unsplit occurrence augmentation; it is supported on a
source-defined soft conductor.  It therefore supplies the required positive
control without contradicting the no-go.

## Cross-sector scope

This is a genuine kernel theorem for the \(C_3\) augmentation.  It must not
be transferred literally to theta.  Grothendieck's exact theta audit instead
finds a parity-graded derivative square whose defect is an internal seam
current.  Vanishing odd seam jets characterize smooth descent, while the
completed even source and the canonical odd section \(\Phi'\) remain
nonzero.

The shared lesson is therefore narrower: source sewing removes
presentation-dependent internal-boundary data, and the physical survivor is
controlled by readout factorization.  Whether this appears as an actual
augmentation kernel or as a smooth-descent condition is sector-specific.
