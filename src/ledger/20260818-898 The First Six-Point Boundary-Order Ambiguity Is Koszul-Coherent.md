# 898 — The First Six-Point Boundary-Order Ambiguity Is Koszul-Coherent

## Frozen source face

Use Mizera's six-point intersection

\[
\left\langle
\mathsf C(123456),
\mathsf C(124365)
\right\rangle.
\]

The two associahedra share the codimension-two edge

\[
F=(34)\cap(1234),
\]

where momentum conservation identifies the second normal letter with

\[
s_{1234}=s_{56}.
\]

Its source value is

\[
\boxed{
\left(\frac i2\right)^3
\frac1{\sin\pi s_{34}}
\frac1{\sin\pi s_{56}}
\left(
\frac1{\tan\pi s_{12}}
+
\frac1{\tan\pi s_{234}}
\right).
}
\]

The edge has two compatible normal histories:

\[
(34)\to(1234),
\qquad
(1234)\to(34).
\]

## Typed order comparison

The source orientation convention is

\[
d\arg H_{34}\wedge d\arg H_{1234}>0.
\]

Swapping the two normals contributes

\[
d\arg H_{1234}\wedge d\arg H_{34}
=
-d\arg H_{34}\wedge d\arg H_{1234}.
\]

The ordered double residue changes by the same Koszul sign:

\[
\operatorname{Res}_{1234}\operatorname{Res}_{34}
=
-\operatorname{Res}_{34}\operatorname{Res}_{1234}.
\]

Therefore the total transition is

\[
(-1)_{\rm orientation}(-1)_{\rm residue}=+1.
\]

The two iterated regularization histories define the same geometric coefficient class.

## Pochhammer reconstruction

Every trigonometric factor is independently compiled from Entry 895's exponential cells:

\[
\csc(\pi s)=
2i\frac{e^{\pi i s}}{e^{2\pi i s}-1},
\]

\[
\cot(\pi s)=
2i\left(\frac1{e^{2\pi i s}-1}+\frac12\right).
\]

At a generic nonresonant point, this assembly reproduces the source six-point formula with error

\[
2.87\times10^{-17}.
\]

After applying both order-transition signs, the two histories agree exactly in the checker. The evidence packet is at

research/benincasa/string-six-point-koszul-coherence.json.

## Narrow result

The first six-point boundary-order ambiguity closes under ordinary oriented residue calculus:

\[
\boxed{
\text{compatible normal histories}
+
\text{Koszul residue sign}
+
\text{tubular-orientation sign}
\Longrightarrow
\text{one class}.
}
\]

No new string-specific coherence generator is needed for this source codimension-two edge.

This is stronger than mere commutativity of scalar sine factors. Literal commutativity would discard the variance and orientation data; coherence holds because two independently forced antisymmetries cancel.

## Scope boundary

One edge does not prove all six-point iterated regularizations are strictly Koszul-coherent. In particular, this test has a rank-one Koba–Nielsen coefficient and normally crossing compatible normals.

## Next falsifier

Test a six-point codimension-three vertex with three compatible normals. Compare all six regularization orders and verify the full permutation sign law and braid coherence. A surviving associator there would be the first justified higher coefficient-coherence datum.
