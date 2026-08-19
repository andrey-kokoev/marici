# 900 — The Trivalent Six-Point Vertex Has No Residual Braid Associator

## Frozen source vertex

Use the source intersection

\[
m_{\alpha'}(123456\mid126435)
=
\frac1{
\sin\pi s_{12}
\sin\pi s_{34}
\sin\pi s_{345}}.
\]

The corresponding common vertex has the compatible normal set

\[
\mathcal N=(12,34,345).
\]

All subamplitudes are trivalent. No contact term or nontrivial lower-point coefficient block is inserted.

## Six ordered histories

There are six orders in which the three normal residues can be taken. For a permutation \(\sigma\in S_3\), tubular orientation transforms by

\[
d\arg H_{\sigma(1)}\wedge
d\arg H_{\sigma(2)}\wedge
d\arg H_{\sigma(3)}
=
\operatorname{sgn}(\sigma)
d\arg H_1\wedge d\arg H_2\wedge d\arg H_3.
\]

The ordered triple residue transforms by the same sign:

\[
\operatorname{Res}_{\sigma(3)}
\operatorname{Res}_{\sigma(2)}
\operatorname{Res}_{\sigma(1)}
=
\operatorname{sgn}(\sigma)
\operatorname{Res}_{3}
\operatorname{Res}_{2}
\operatorname{Res}_{1}.
\]

Hence every ordered history has total transition

\[
\operatorname{sgn}(\sigma)^2=1.
\]

## Braid test

The two reduced words for reversing three normals are

\[
s_1s_2s_1,
\qquad
s_2s_1s_2.
\]

Both reach the same order and each gives orientation sign \(-1\) and residue sign \(-1\). Their total maps are identical:

\[
(-1)(-1)=+1.
\]

Thus the braid relation closes without a residual scalar, sign, or rank-one associator.

## Source coefficient reconstruction

Each normal contributes the source half-monodromy cell

\[
2i\frac{e^{\pi i s_H}}{e^{2\pi i s_H}-1}
=
\frac1{\sin\pi s_H}.
\]

Their product reproduces the complete source formula. At a generic nonresonant point the numerical error is

\[
4.56\times10^{-16}.
\]

The durable packet is at

research/benincasa/string-six-point-vertex-braid.json.

## Narrow result

For this source codimension-three trivalent vertex,

\[
\boxed{
\text{all six histories}
\simeq
\text{one oriented triple residue},
\qquad
\text{braid associator}=0.
}
\]

The existing flagged-normal and Koszul orientation calculus is sufficient. No higher string-specific coherence primitive is required at this vertex.

## Scope boundary

This conclusion is restricted to a normally crossing vertex with a rank-one Koba–Nielsen local system and trivalent subamplitudes. It does not control a six-point block in which different vertices and an internal four-point self-intersection mix.

## Next falsifier

Use the source \(2\times2\) six-point KLT block containing both trivalent and four-point self-intersection contributions. Reconstruct every entry from Pochhammer cells, invert the block, and test whether the mixed sine sums arise without a new determinant divisor or coherence term.
