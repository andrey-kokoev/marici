---
authors:
  - marici.Nima
date: 2026-08-18
---
# 755 — The Off-Diagonal Connection Block Is the Global Extension Cocycle

## Direct representative

In the Gysin-adapted frame of Entry 754, write

\[
\nabla_V=
\begin{pmatrix}
\nabla_T&0\\
C&\nabla_E
\end{pmatrix}.
\]

Flatness of \(\nabla_V\) implies

\[
\boxed{\nabla_{\operatorname{Hom}}C=0,}
\]

where \(C\) is a degree-one element of
\(\operatorname{DR}\operatorname{Hom}(T,E)\).  Therefore the extension has
the direct representative

\[
[V]=[C]\in
H^1_{\rm dR}\!\left(B,\operatorname{Hom}(T,E)\right).
\]

A gauge \(X:T\to E\) changes

\[
C\longmapsto C+
\nabla_{\operatorname{Hom}}X.
\]

Consequently the extension splits precisely when \(C\) is exact.  The
Čech differences of Entry 754 are the descent presentation obtained after
solving this equation locally; they are not an additional invariant.

## What the existing tests establish

The committed computations probe restricted exactness problems:

- Entry 721: no primitive \(X\) polynomial of total degree at most ten;
- Entry 722: no primitive of the form \(N/f\), with one declared divisor
  \(f\) and numerator degree at most ten;
- Entries 724--725: no leading residue obstruction, and no extension
  residue at \(P_6\) or \(\mathcal Q\).

None computes the full class \([C]\).  In particular, a primitive can have
simultaneous poles on several ordinary source divisors even when no
single-divisor primitive exists.

## Correct finite complex

Let

\[
D_{m src}=u,v,y(1-y)(1+y)(v-u)(y-u^2)(y+u^2)P_6,
\]

with \(\mathcal Q\) deliberately omitted.  For pole bound \(m\) and numerator
degree bound \(d\), define

\[
K^0_{m,d}=
\left\{
\frac{N(u,v)}{D_{\rm src}^{m}}:
N\in\operatorname{Mat}_{2\times2},\ \deg N\le d
\right\}.
\]

The next matrix is the coefficient map

\[
\nabla_{\operatorname{Hom}}:
K^0_{m,d}longrightarrow K^1_{m+1,d+\Delta},
\]

augmented by the exact serialized coefficient vector of \(-C\).  The rank
test

\[
\operatorname{rank}[\nabla_{\operatorname{Hom}}\mid -C]
=
\operatorname{rank}\nabla_{\operatorname{Hom}}
\]

is the bounded splitting condition.  Failure at one bound is only a
filtered nonexactness result; stabilization across increasing \((m,d)\), or
an independent cohomological dimension theorem, is needed for an absolute
nonsplitting claim.

## Independent projector check

A solution \(X\) produces a horizontal idempotent projector onto \(E\).
Conversely such a projector supplies a splitting.  The projector equations
must be run with the same denominator and degree filtration.  Agreement
prevents a false result caused by the chosen block gauge.

## Narrow conclusion

\[
\boxed{
\text{compute }[C]\text{ directly in filtered twisted de Rham cohomology;
local Čech gauges are its descent realization.}
}
\]

## Evidence

- Entries 721--725 and 754;
- `research/benincasa/marici-gm/gysin-adapted-reconstruction-d12.json`;
- `research/benincasa/marici-gm/gysin-polynomial-split-d10.json`;
- allocator claim `seqclaim-b20b919026dae23f3cf1bacd`.
- epistemic event
  `ev-000000000369-2e727536-b006-43dc-b8e4-fada6d46f338`.

## Next computation

Materialize the \((m,d)\) rank table for \(m=0,1,2\) and increasing \(d\),
using the exact adapted connection and the source denominator above.  Export
kernel dimensions, augmented-rank defects, validation points, and the
matching horizontal-projector census.
