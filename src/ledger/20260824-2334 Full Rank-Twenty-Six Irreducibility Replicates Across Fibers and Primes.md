---
authors:
  - marici.Benincasa
date: 2026-08-24
---

# 2334 — Full Rank-Twenty-Six Irreducibility Replicates Across Fibers and Primes

## Replication target

Entry 2328 found

\[
\mathbf F_{32003}
\langle A_{X_1},A_{X_2},A_{X_3}\rangle
=M_{26}(\mathbf F_{32003})
\]

at \((X_1,X_2,X_3)=(2,3,4)\).  To distinguish a generic signature from an
accidental fiber or prime, repeat the complete source-cyclicity and generated
algebra calculation without reusing matrix entries.

## Exact census

\[
\begin{array}{c|c|c|c}
\text{field}&(X_1,X_2,X_3)&
\operatorname{rank}\operatorname{Sat}_\nabla(\Omega_{\rm src})&
\dim\langle A_{X_1},A_{X_2},A_{X_3}\rangle\\
\hline
32003&(2,3,4)&26&676\\
32003&(3,5,7)&26&676\\
32003&(5,7,11)&26&676\\
31991&(2,3,4)&26&676
\end{array}
\]

The four independently serialized connection digests are distinct, so the
replications did not replay one frozen matrix packet.

## Result

\[
\boxed{
\text{The typed rank-twenty-six source cyclicity and full-matrix-algebra
signature are stable across the tested generic fibers and primes.}
}
\]

This is strong discovery evidence for generic characteristic-zero absolute
irreducibility.  It is not by itself a characteristic-zero proof: the next
symbolic route would exhibit a finite set of \(676\) connection words with a
nonzero rational determinant.

## Consequence for the observer programme

At generic interacting scalar kinematics, no proper connection-invariant
blind sector appears in either the source or dual transport orbit.  The
remaining hostile tests are supported specializations, where irreducibility
may fail legitimately:

\[
\text{soft},\quad
\Lambda=0,\quad
\text{Landau},\quad
E_T=0,\quad
\text{marked walls},\quad
\text{elliptic degeneration intersections}.
\]

Any residual class must be computed as a supported cone there; generic rank
statistics no longer supply a plausible obstruction.

## Durable verification

- `research/benincasa/check_rank26_unsplit_source_cyclicity.py`;
- `research/benincasa/check_rank26_connection_algebra.py`;
- `research/benincasa/rank26-connection-algebra.json`;
- allocator claim `seqclaim-905472c93e4d1d3dc5a0c0be`.

