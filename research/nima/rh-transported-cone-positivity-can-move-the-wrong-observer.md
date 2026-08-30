# RH transported-cone positivity can move the wrong observer

## Result

A pointed cone can be transported covariantly through Mellin phase, but its positive dual observer must then move contragrediently. The resulting positive pairing need not equal the fixed Evans endpoint.

Let

\[
U=
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix},
\qquad
x=
\begin{pmatrix}
1\\1
\end{pmatrix},
\qquad
\ell=(1,1).
\]

The initial state lies in the positive cone and has endpoint value \(2\). After phase transport,

\[
Ux=(1,-1),
\]

so the fixed endpoint observer gives

\[
\ell Ux=0.
\]

If the observer is transported contragrediently,

\[
\ell_U=\ell U^{-1}=(1,-1),
\]

then

\[
\ell_UUx=2.
\]

Positivity is restored, but for a moved observer rather than the Evans observer.

## Tautological covariance

For every invertible \(U\),

\[
(\ell U^{-1})(Ux)=\ell x.
\]

Therefore transporting the cone and its dual observer together preserves the pairing automatically. This certifies correct variance, not zero exclusion for a separately fixed scalar readout.

This is the cone analogue of Grothendieck's theorem that invertible equivariant coherence preserves the Evans kernel.

## Missing comparison

A transported relational cone becomes RH-bearing only if the source also derives a comparison between the transported dual observer and the actual endpoint wall.

That comparison must show, on the admissible state relation, that

\[
\ell_{\mathrm{Evans}}(Ux)=0
\]

forces the positive covariant pairing to vanish. Without it, the construction has simply changed the question.

The comparison cannot be defined by dividing the two scalar readouts or by declaring the observer to move with the state.

## DPC verdict

Candidate: transport a pointed cone and its dual observer covariantly.

Verdict: algebraically valid but tautological.

Candidate: keep the actual Evans observer fixed.

Verdict: rejected by the two-ray phase-flip hostile.

Surviving candidate: a source-derived observer-comparison wall joining the covariant positive pairing to the fixed Evans endpoint, or a distinguished orbit on which those observers coincide.

## Finite falsifier

At a finite labelled cutoff:

1. transport an admissible positive state by a phase-flip element;
2. evaluate it with both the fixed Evans observer and the contragredient cone observer;
3. compute their difference on the source-defined state relation.

Any state with zero fixed endpoint and nonzero covariant positive pairing disproves the observer comparison.
