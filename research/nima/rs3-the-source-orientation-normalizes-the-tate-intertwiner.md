# Source orientation normalizes the unequal-energy Tate intertwiner

Date: 2026-08-23

The character match between the unequal-energy cotangent line and the
mod-three Tate line can be upgraded to an explicit source-derived map.

Let

\[
A=\mathbf F_3[C_3],\qquad I=\ker(\varepsilon:A\to\mathbf F_3),
\qquad H_{\rm Tate}=I/(g-1)I.
\]

The ordered unequal-energy coordinate supplies the oriented source
difference.  Define

\[
\boxed{
d(X_2-X_3)\longmapsto[g-g^{-1}]\in H_{\rm Tate}.
}
\]

Writing \(t=g-1\), characteristic three gives

\[
(g-g^{-1})+t=2t^2.
\]

Since \((g-1)I=\langle t^2\rangle\), the image is \(-[t]\), hence is
nonzero and generates the one-dimensional Tate quotient.  Rotation is
trivial modulo \((g-1)I\), while reflection \(g\leftrightarrow g^{-1}\)
negates the class.  This exactly matches the cotangent character of
\(d(X_2-X_3)\).

The normalization is not fitted: reversing the source ordering reverses both
the unequal-energy coordinate and the occurrence difference.  Once the
source labels and their orientation are frozen, the scalar ambiguity of the
one-dimensional character match is removed.

Two negative controls distinguish the construction from an arbitrary
one-dimensional projection:

- the even occurrence pair \(g+g^{-1}\) is reflection-even;
- it is not in the augmentation ideal, so it cannot represent the Tate
  kernel direction.

This completes the coefficient map but not physical activation.  Ordinary
unsplit sewing factors through \(\varepsilon\) and therefore annihilates
the target.  A nonzero observable requires the independently derived
soft-Gysin or another supported relative readout.

Grothendieck's theta correction remains essential: this genuine
augmentation-kernel theorem is sector-specific and must not be reinterpreted
as saying that all odd seam data lie in the kernel of theta sewing.
