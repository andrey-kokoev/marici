# Theta log-concavity forces positive local band-boundary curvature

## Bounded question

Does the completed theta source pass the smallest exact falsifier for
tilt-monotonicity of its translation-defect energy?

## Curvature formula

Let

\[
g(x)=\Phi(|x|),
\qquad
f_a(x)=e^{ax}g(x),
\]

and

\[
\mathcal C_a(D)
=
\frac12\|f_a-\tau_Df_a\|_2^2.
\]

Using

\[
\mathcal C_a(D)=W_a(0)-W_a(D),
\]

differentiate twice at \(a=0\). For the translated term, set

\[
y=x-\frac D2.
\]

Then

\[
\mathcal C_0''(D)
=
4\int_{\mathbb R}
y^2
\left[
g(y)^2
-
g\!\left(y+\frac D2\right)
g\!\left(y-\frac D2\right)
\right]dy.
\]

## Source curvature orientation

The completed theta source is already proved strictly log-concave. Midpoint
log-concavity gives

\[
g\!\left(y+\frac D2\right)
g\!\left(y-\frac D2\right)
\le
g(y)^2.
\]

For \(D>0\), strict log-concavity makes the inequality strict away from the
degenerate midpoint set. Since the weight \(y^2\) is positive away from zero,

\[
\mathcal C_0''(D)>0
\qquad
(D>0).
\]

Reflection makes \(\mathcal C_a(D)\) even in \(a\), so

\[
\mathcal C_0'(D)=0.
\]

Analyticity in the tilt parameter now implies, for every fixed \(D>0\), the
existence of \(\varepsilon_D>0\) such that

\[
\partial_a\mathcal C_a(D)>0
\qquad
(0<a<\varepsilon_D).
\]

Equivalently,

\[
J_a(0)>J_a(D)
\]

for sufficiently small positive outer tilt.

## Meaning

The first surviving conditional-band boundary requirement is locally true for
the completed theta source. Its orientation is explained directly by source
log-concavity:

source midpoint dominance produces positive curvature of translation
distinguishability under tilt.

This is stronger than a numerical anchor and weaker than the required global
outer-sector theorem. It does not prove that

\[
\partial_a\mathcal C_a(D)\ge0
\]

for every \(a>0\).

## Relation to the flagged-plane correction

The translation-defect norm is a full Gram quantity, while the desired
conditional boundary current is its tilt derivative. Vanishing of one chosen
Fourier or Plücker coordinate need not mean loss of the full source plane.
The present theorem therefore supplies a local oriented flag coordinate, not
a claim that the ambient Gram plane degenerates.

A global proof still needs a source-derived transverse cone that preserves the
sign of this derivative under finite tilt.

## Result

The smallest curvature falsifier fails to falsify the route:

\[
\mathcal C_0''(D)>0
\]

for every \(D>0\). The completed source begins in the correct boundary-current
chamber.

The next sharp question is whether the derivative can cross zero at finite
positive \(a\). The first such crossing, if any, is the genuine obstruction.

## Sharp falsifier

Find \(D>0\) and the smallest \(a_*>0\) satisfying

\[
\partial_a\mathcal C_{a_*}(D)=0
\]

with negative sign immediately afterward. Such a crossing ends global
tilt-monotonicity while preserving the proved local theorem.
