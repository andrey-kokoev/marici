# Prime Recursion Lifts Every Scalar Zero Through Filtered Endpoints

## Exact source recursion

The completed labelled theta source satisfies, for every prime \(p\),

\[
\Phi(u)
=
\Phi_{p\nmid}(u)
+
p^{-1/2}\Phi(u+\log p).
\]

Here \(\Phi_{p\nmid}\) retains exactly the labels not divisible by \(p\).
For the bilateral transform

\[
X(z)=\int_{\mathbb R}\Phi(u)e^{zu}\,du,
\]

translation gives

\[
\int_{\mathbb R}
p^{-1/2}\Phi(u+\log p)e^{zu}\,du
=
p^{-1/2-z}X(z).
\]

Therefore the primitive filtered endpoint is exactly

\[
X_{p\nmid}(z)
=
\left(1-p^{-1/2-z}\right)X(z).
\]

This is the source coherence absent from the hostile two-label packet.

## Valuation tower

Let \(X_{p,r}\) denote the transform of labels having exact
\(p\)-adic valuation \(r\). Iterating the same shift gives

\[
X_{p,r}(z)
=
p^{-r(1/2+z)}
\left(1-p^{-1/2-z}\right)X(z).
\]

Consequently,

\[
X(z)=0
\quad\Longrightarrow\quad
X_{p,r}(z)=0
\]

for every prime \(p\) and every valuation depth \(r\geq0\).

Thus the scalar zero equation does lift through the entire family of
prime-filtered endpoint equations for the actual theta source.

## Why RH still does not follow

The formula is an identity of entire scalar continuations. The common-domain
theorem concerns something stronger: simultaneous realization of the labelled
prime currents in the opposite weighted sector riggings.

Multiplication by

\[
1-p^{-1/2-z}
\]

proves filtered endpoint nullity but supplies no bound on the absolute
prime-current family. In particular, it does not turn the critical sums

\[
\sum_p p^{-1-\varepsilon/2+\Re z},
\qquad
\sum_p p^{-1-\varepsilon/2-\Re z}
\]

into convergent source norms. At a zero, every analytically continued
coordinate may vanish even though the labelled pre-completion packet lacks a
common realization.

Hence two layers must remain separate:

- prime-recursive endpoint descent, which is exact and now proved;
- completion-stable labelled admissibility, which remains open and selects the
  seam.

## Corrected obstruction

The hostile two-label packet from the preceding result is not theta
admissible. It violates prime-scale recursion. It remains useful as the
smallest proof that endpoint lifting is not formal; the theta constructor is
doing genuine work.

But the recursion closes only the endpoint wall. The remaining wall is
topological and analytic: does the recursively coherent zero packet lift
before completion to a single state in the common graph domain of all
primitive currents?

## Next falsifier

Construct finite prime cutoffs of the recursively coherent labelled zero
packet and measure their graph norms in both reciprocal sector riggings.

The route fails if the endpoint equations vanish at every cutoff while one of
the two primitive-current graph norms diverges as the cutoff grows. Such a
witness would prove that exact descent of scalar coordinates does not imply
descent of the state carrying those coordinates.

## Explanatory gain

The earlier phrase “one thing that is actually two things” now has an exact
instance. A filtered zero has:

1. an algebraic coordinate, controlled by prime recursion;
2. a realization as a boundary-bearing labelled state, controlled by
   completion.

Theta arithmetic supplies the first. RH requires the second to exist
simultaneously in both reciprocal sectors only on the seam.

