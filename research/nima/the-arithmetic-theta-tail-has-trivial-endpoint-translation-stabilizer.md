# The Arithmetic Theta Tail Has Trivial Endpoint Translation Stabilizer

## Source theorem already available

Grothendieck's finite-translate theorem gives the completed theta asymptotic

\[
\frac{\Phi(u+d)}{\Phi(u)}
\longrightarrow0
\qquad
(u\to+\infty)
\]

for every fixed \(d>0\). The source carrier contains the arithmetic tail atoms

\[
F_n(q)=\Phi(q+\log n).
\]

Their endpoint values are

\[
\delta_0(F_n)=\Phi(\log n).
\]

## Positive translations

For \(a>0\),

\[
\frac{\delta_a(F_n)}{\delta_0(F_n)}
=
\frac{\Phi(\log n+a)}{\Phi(\log n)}
\longrightarrow0.
\]

Therefore \(\delta_a(F_n)\ne\delta_0(F_n)\) for every sufficiently large
integer \(n\). No positive translation stabilizes endpoint incidence on the
arithmetic tail carrier.

## Negative translations

Let \(a<0\) and set \(d=-a>0\). For sufficiently large \(n\), both
\(\log n\) and \(\log n-d\) lie in the positive tail. Applying the same
asymptotic with \(u=\log n-d\) gives

\[
\frac{\Phi(\log n)}{\Phi(\log n-d)}
\longrightarrow0.
\]

Hence \(\Phi(\log n-d)\ne\Phi(\log n)\) eventually. No negative translation
stabilizes the endpoint either.

It follows that

\[
\operatorname{Stab}(\delta_0)=\{0\}
\]

on the source-generated arithmetic tail carrier.

## Completion typing

Finite separation alone would not normally survive completion. Here the
relevant endpoint functional is already continuous in the native tail graph
energy:

\[
\lVert G+f\rVert_2^2
=
\lVert h'\rVert_2^2
+a^2\lVert h\rVert_2^2
+a|h(0)|^2.
\]

Thus endpoint incidence is not reconstructed after completion; it is one of
the controlled graph coordinates.

Right translations act continuously on the half-line tail domain but move
the endpoint. Negative translations are not global automorphisms of the
half-line carrier. Consequently no nonzero translation becomes a hidden
symmetry merely by passing to the boundary-bearing graph completion.

## What this closes

The logarithmic-origin torsor is pointed by the actual theta endpoint before
Haar projection. The character family \(n^{ia}\) remains a valid abstract
Mellin twist, but only \(a=0\) preserves the complete source incidence.

This supplies a source-derived phase reference. It does not yet prove the
orientation of the completed endpoint--gamma--prime interaction. The next
gate is whether the gamma and prime boundary maps are covariant relative to
this pointed endpoint frame. If either is compared only after scalar
completion, the phase reference is lost again.

## Finite falsifier

For any proposed nonzero stabilizing translation \(a\), choose an arithmetic
label \(n\) beyond the asymptotic threshold. The single endpoint comparison

\[
\Phi(\log n+a)-\Phi(\log n)
\]

is nonzero and falsifies the claimed symmetry.

