# 895 — The String Sine Propagator Is a Half-Monodromy Pochhammer Cell

## Source construction

For the local source loading

\[
z^s(1-z)^t,
\]

Mizera's Pochhammer regularization of the interval has endpoint coefficients

\[
\frac1{e^{2\pi i s}-1},
\qquad
-\frac1{e^{2\pi i t}-1}.
\]

An adjacent loaded chamber meeting the first endpoint contributes the half-turn branch phase

\[
e^{\pi i s}.
\]

With the source boundary orientation, its complete local coefficient is therefore

\[
\boxed{
\frac{e^{\pi i s}}{e^{2\pi i s}-1}
=
-\frac{i}{2\sin\pi s}.
}
\]

Thus the sine propagator is not an independent trigonometric decoration. It is the quotient of a half-monodromy occurrence by the full-loop Pochhammer boundary operator.

## Deformation-independence audit

The source gives four deformations of the same regularized four-point self-intersection. In exponential notation they are

\[
-\frac1{M_s-1}-1-\frac1{M_t-1},
\]

\[
-\frac{M_s}{M_s-1}+1-\frac{M_t}{M_t-1},
\]

\[
-\frac1{M_s-1}-\frac{M_t}{M_t-1},
\]

and

\[
-\frac{M_s}{M_s-1}-\frac1{M_t-1},
\qquad
M_x=e^{2\pi i x}.
\]

They reduce identically to

\[
\frac{i}{2}
\left(
\frac1{\tan\pi s}
+
\frac1{\tan\pi t}
\right).
\]

The durable checker verifies both the adjacent half-monodromy identity and equality of all four deformations at a generic nonresonant point. The maximum errors are respectively

\[
1.11\times10^{-16},
\qquad
2.78\times10^{-17}.
\]

The evidence packet is at

research/benincasa/string-half-monodromy-cell.json.

## Narrow result

The local coefficient mechanism needed by Entry 894 is now typed:

\[
\boxed{
\text{oriented adjacent occurrence}
+
\text{half-monodromy}
+
\text{Pochhammer regularization}
\longrightarrow
\text{sine coefficient}.
}
\]

This supports the shared-calculus architecture more strongly than the numerical period identity alone. The incidence wall is unchanged; finite string structure resides in the rank-one Koba–Nielsen local system and its regularized boundary calculus.

## Scope boundary

This is the universal one-normal-direction cell. It does not yet prove that the complete five-point circuit is the boundary of one oriented two-dimensional regularized associahedral chain.

## Next falsifier

Assemble the labelled codimension-one cells around the five-point circuit and compute its full twisted boundary. The coefficients must reproduce both numerator phases

\[
\sin\pi(s_{12}+s_{23}),
\qquad
\sin\pi s_{24},
\]

with the common denominator \(\sin\pi s_{12}\), without adding a fitted two-cell or changing source orientations.
