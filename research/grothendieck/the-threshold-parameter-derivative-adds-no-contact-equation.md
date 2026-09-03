# The threshold-parameter derivative adds no independent contact equation

## Prime source derivatives

Write the completed translated kernel as

\[
\Theta(t,\xi)=A(t,\xi)-C(t)R(t,\xi),
\qquad
C(t)=\frac1{2\sqrt{\pi t}},
\]

where

\[
R(t,\xi)=\sum_{n\ge2}c_n(t)\cos(\xi\log n),
\qquad
c_n(t)=\frac{\Lambda(n)}{\sqrt n}
 e^{-(\log n)^2/(4t)}.
\]

Define

\[
R_2(t,\xi)=\sum_{n\ge2}c_n(t)(\log n)^2\cos(\xi\log n).
\]

Then

\[
\partial_tR=\frac{R_2}{4t^2},
\qquad
C'=-\frac{C}{2t},
\]

so

\[
\partial_t\Theta
=
\partial_tA+rac{C}{2t}R-rac{C}{4t^2}R_2.
\]

## Redundancy with heat curvature

The Gaussian equation gives

\[
\partial_t\Theta
=-\frac{1}{4t^2}\partial_\xi^2\Theta-rac{1}{2t}\Theta.
\]

At a double contact, `Theta=0`, hence

\[
\partial_t\Theta
=-\frac{1}{4t^2}\partial_\xi^2\Theta.
\]

Therefore imposing the threshold-direction sign `partial_t Theta <= 0` is exactly equivalent to the already required spatial minimum condition `partial_xi^2 Theta >= 0`. In prime variables this is the same `R_2` curvature constraint already present in the moment-ellipse packet.

## Consequence

Differentiating in the Gaussian-width parameter does not add a new arithmetic moment or overdetermine a putative first contact. The independent contact data remain:

1. value, fixing the prime cosine sum `R`;
2. character slope, fixing the sine moment `I_1`;
3. character curvature, constraining `R_2`;
4. higher character derivatives or stronger positive moment matrices.

Any exclusion must strengthen the prime trigonometric moment constraints or the completed archimedean bounds. Repackaging curvature through `partial_t` cannot close the contact.

## Disposition

Do not create a separate threshold-velocity branch. Continue from the value--slope ellipse and curvature covariance inequality in `prime-moment-ellipse-double-contact-obstruction.md`; the next genuinely stronger certificate uses higher character moments with common prime cutoffs.
