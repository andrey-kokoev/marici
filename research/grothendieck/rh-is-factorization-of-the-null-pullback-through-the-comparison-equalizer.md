# RH is factorization of the null pullback through the comparison equalizer

## Two independent constructions

Let (V) be the completed source-state space, let

\[
m(z)=M_z\Omega
\]

be the character-transport orbit, and let

\[
\varepsilon:V\longrightarrow\mathbb C
\]

be the completed scalar readout. Thus `X` is the composite

\[
X=\varepsilon\circ m.
\]

Independently, reciprocal parity (P) and real conjugation (C) define the
comparison map along the orbit:

\[
d(z)=(P-C)m(z).
\]

## The scalar-null pullback

Pull back the zero scalar along (X):

\[
Z_0
=
\{z:X(z)=0\}.
\]

This is the divisor observed in the completed scalar graph.

## The comparison equalizer

Pull back the zero state along (d):

\[
S
=
\{z:d(z)=0\}.
\]

The exact transported 2-cell calculation proves

\[
S=\{z:\Re z=0\}.
\]

Thus the critical seam is constructed without using the zero set.

## RH as a factorization

RH is precisely the statement

\[
Z_0\subseteq S.
\]

Categorically, the inclusion (Z_0\to\mathbb C) must factor through the
comparison equalizer (S\to\mathbb C). Because the equalizer inclusion is a
monomorphism, such a factorization is unique if it exists.

This is the exact missing 2-cell:

\[
Z_0\longrightarrow S.
\]

It is not supplied by defining either pullback. The scalar readout constructs
(Z_0); reciprocal–real comparison constructs (S); theta arithmetic must
construct the factorization between them.

## Why this is not a reformulation without gain

As a bare set inclusion, the statement is equivalent to RH. The gain is the
separation of authority:

1. (Z_0) is defined by the physical scalar readout;
2. (S) is defined independently by a source comparison;
3. the proof obligation is a naturality or descent factorization between
   those constructions;
4. a hostile source fails by producing a point of (Z_0\setminus S).

This prevents the seam from being fitted to the zeros and prevents scalar
symmetry from being mistaken for the missing implication.

## Constructor-level target

The desired factorization must be induced before scalarization by the full
labelled theta/Tate observer, including primitive, square, connected, seam,
and archimedean boundary channels. It must show that a source-authorized null
readout carries a canonical witness of reciprocal–real path equality.

An equality checked only after applying the scalar readout is circular. A witness
constructed by dividing by (X) is inadmissible. A finite-cutoff witness that
does not survive restricted-product completion is insufficient.

## Minimal falsifier

The falsifier is a source-admissible transported packet (m(z)) satisfying

\[
\varepsilon(m(z))=0,
\qquad
(P-C)m(z)\ne0.
\]

This is exactly a scalar-null state whose two half-plane meanings remain
distinguishable.
