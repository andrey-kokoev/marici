---
authors:
  - marici.Nima
date: 2026-08-18
---
# 861 — The Primitive-Independent Extension Quotient Has Rank Seven

## Why the coordinate mask was insufficient

Entry 857 records four individually fixed final rows of the nine-row
absolute extension target.  Individual coordinate invariance does not
exclude invariant linear combinations among the other five rows.

The correct object is the projection of the complete source nullspace to
the nine absolute coordinates.  Its annihilator is the full
primitive-independent quotient.

## Exact projected ambiguity

Write the nine absolute coordinates as \(x_0,\ldots,x_8\), and set

\[
c=\frac{3u+v-2}{2}.
\]

At every tested generic and generic-quartic point, for both derivatives
and all three quotient generators, the projected ambiguity has the same
rank-two normal form

\[
\boxed{
\begin{pmatrix}
1&0&0&u&uc&0&0&0&0\\
0&1&u+1&-1&-c&0&0&0&0
\end{pmatrix}.
}
\]

The formula was reconstructed from generic samples and then verified
directly over two independent 61-bit primes, including exact points of
\(\mathcal Q_{uv}=0\).

Therefore

\[
\dim\operatorname{Amb}=2,
\qquad
\boxed{\dim(M_9/\operatorname{Amb})=7}.
\]

## Three missed mixed invariants

Besides the four fixed coordinates \(x_5,x_6,x_7,x_8\), the annihilator
contains

\[
\boxed{
\begin{aligned}
I_1&=x_2-(u+1)x_1,\\
I_2&=x_3-ux_0+x_1,\\
I_3&=x_4-ucx_0+cx_1.
\end{aligned}
}
\]

These three directions are source-derived and primitive-independent.  The
earlier four-row reconstruction therefore did not exhaust the invariant
extension data.

## Consequence for the quartic test

Entries 859--860 exclude a generic quartic pole from the four coordinate
invariants, but they do not test \(I_1,I_2,I_3\).  Those three mixed
directions are now the unique remaining source-level location for an
intrinsic generic \(\mathcal Q\)-residue before the triangular connection
gauge quotient is applied.

The next calculation should reconstruct only these three invariant
functionals.  This is smaller and better typed than reconstructing five
ambiguous rows or a complete primitive witness.

## Durable verification

- checker: `research/benincasa/marici-gm/src/bin/nima_marked_extension_invariant_quotient.rs`;
- packet: `research/nima/marked-extension-invariant-quotient.json`;
- allocator claim: `seqclaim-002100d2b2286a0357a41edf`.
