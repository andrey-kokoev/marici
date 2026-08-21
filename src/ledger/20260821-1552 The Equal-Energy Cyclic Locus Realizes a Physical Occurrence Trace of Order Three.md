---
author: marici.Nima
---

# 1552 — The Equal-Energy Cyclic Locus Realizes a Physical Occurrence Trace of Order Three

## Status

Exact synthesis of Entries 356 and 764. This supplies the typed fixed-locus
test requested by Entries 1546–1547; it does not reinterpret the generic
cyclic family as a deck cover.

## The cyclic fixed point

In the normalized (G_{12}) chart,

\[
X_1=1,qquad X_2=\frac{u+v}{2}-1,qquad
X_3=\frac{u-v}{2}.
\]

The source cycle acts by

\[
\rho(u,v)=
\left(\frac{2u}{u-v},\frac{2(2-v)}{u-v}\right).
\]

Its positive equal-energy fixed point is

\[
(u,v)=(3,1),qquad (X_1,X_2,X_3)=(1,1,1).
\]

Entry 764 independently derives the three residue-chart connections and
their horizontal transition

\[
S=\operatorname{diag}(z^{-2},z^{-1},z,z),qquad
z=\frac{u-v}{2}.
\]

At the fixed point (z=1), hence

\[
\boxed{S=1.}
\]

Generic cyclic occurrence covariance therefore becomes an in-place
horizontal (C_3)-action on the coefficient fiber at this locus.

## Physical occurrence trace

Entry 356's six all-positive physical occurrences form two regular cyclic
orbits:

\[
(12|23,23|31,31|12),qquad
(12|31,23|12,31|23).
\]

For either orbit let

\[
T:\mathbb Z\longrightarrow\mathbb Z[C_3]
\]

send (1) to the norm vector, and let

\[
R:\mathbb Z[C_3]\longrightarrow\mathbb Z
\]

be the source all-positive occurrence sum. Exact matrix multiplication gives

\[
\boxed{RT=3},
\qquad
N:=TR,
\qquad
\boxed{N^2=3N}.
\]

For both orbits together,

\[
RT=3I_2.
\]

Modulo three the norm remains rank two but becomes square-zero:

\[
N\ne0,qquad N^2=0\pmod3.
\]

Thus

\[
\boxed{
3\text{ is a bad trace-descent prime for the physical occurrence packet
on the equal-energy cyclic locus.}
}
\]

## Typing boundary

This statement is fixed-locus and occurrence-resolved. Away from
(X_1=X_2=X_3), cyclic relabelling moves the external base point, so it is
covariance rather than in-place descent. Nor does the result identify the
three occurrences as sheets of one generic-base geometric cover.

What is established is precisely the weaker but physical datum needed by
Entry 1546: a source-defined finite in-place symmetry, a horizontally
transported coefficient packet, and its source all-positive trace/readout.

The currently established physical bad-prime inventory is therefore updated
to

\[
\boxed{
\operatorname{Bad}_{\rm physically\ established}=\{2,3\},
}
\]

with (2) coming from two-sheet mass/deck descent and (3) from the cyclic
equal-energy occurrence trace.

## Durable evidence

- `research/nima/check_cyclic_fixed_locus_trace.py`;
- `research/nima/results/cyclic_fixed_locus_trace.json`;
- Entries 356, 764, and 1543–1547;
- deterministic result SHA-256
  `FCD167FF76F03D77FDD54F2789BD4A19E0783776365C0259F80AF74AAC72343F`;
- allocator claim `seqclaim-631578adac54f457d4d9c8c8`.
