# Reciprocal prime-chain blocks are locally acyclic across the critical strip

## Source-local bordered block

For one prime \(p\), let \(S_N\) be the nilpotent shift on the finite valuation
chain

\[
e_0,e_1,\ldots,e_N,
\qquad
S_Ne_k=e_{k+1},
\qquad
S_Ne_N=0.
\]

Set

\[
q=p^{-s},
\qquad
D_{p,N}^{+}(s)=I-qS_N.
\]

The inverse is the finite Neumann series

\[
(D_{p,N}^{+})^{-1}
=
\sum_{k=0}^{N}q^kS_N^k.
\]

Border the chain by its primitive vacuum and augmentation:

\[
\mathcal B_{p,N}^{+}(s)
=
\begin{pmatrix}
D_{p,N}^{+}(s)&e_0\\
\ell&0
\end{pmatrix},
\qquad
\ell(e_k)=1.
\]

Schur elimination gives

\[
\det\mathcal B_{p,N}^{+}(s)
=
-\ell(D_{p,N}^{+})^{-1}e_0
=
-\sum_{k=0}^{N}p^{-ks}.
\]

The truncated Euler factor is therefore produced by a labelled shift,
primitive boundary vector, and augmentation. It is not inserted as a scalar
matrix entry.

## Exact local zero locus

For \(q\ne1\),

\[
\sum_{k=0}^{N}q^k
=
\frac{1-q^{N+1}}{1-q}.
\]

Its zeros satisfy

\[
q^{N+1}=1,
\qquad
q\ne1.
\]

Hence every finite-chain zero has

\[
|q|=1.
\]

Since \(|p^{-s}|=p^{-\Re s}\), the positive valuation block is invertible for

\[
\Re s>0.
\]

Its finite truncation zeros lie on the boundary \(\Re s=0\), never in its open
contraction sector.

As \(N\) tends to infinity, the same Neumann series converges for \(|q|<1\)
and yields

\[
-\frac{1}{1-p^{-s}}.
\]

Thus the infinite local Euler block remains zero-free throughout
\(\Re s>0\).

## Reciprocal valuation block

The opposite Tate cone has parameter

\[
q_-=p^{s-1}.
\]

The identical construction is invertible whenever

\[
|q_-|<1,
\]

which is equivalent to

\[
\Re s<1.
\]

Therefore both source-derived local blocks are simultaneously invertible in
the entire open critical strip:

\[
0<\Re s<1.
\]

This is stronger than seam unitarity. The critical line is the locus where
the two contraction rates agree, but local acyclicity holds on both sides of
it.

## Consequence for the location of the unresolved mechanism

A zero in the critical strip cannot be attributed to a kernel of an
individual finite prime-valuation chain. Nor can it arise from the
corresponding infinite local Neumann block.

The only remaining locations are global:

- coupling the two valuation cones through a common boundary object;
- primitive and prime-square renormalization;
- archimedean endpoint completion;
- failure of restricted-product exactness;
- a nontrivial infinite-completion defect.

This recovers the earlier completion-at-infinity diagnosis from an explicit
source-local operator rather than from scalar provenance.

## Cartesian deletion

For a finite set of primes \(X\), take the direct sum of the bordered local
systems while retaining their boundary types. Adding a new prime \(p\)
adjoins one independently constructed valuation block. Deleting it recovers
the original labelled system exactly.

For two new primes \(p\) and \(q\), the finite direct-sum eliminations commute.
The corresponding determinant increments multiply, and the local
four-corner deletion square is strict.

This proves the arithmetic interior of the cartesian elimination gate. It
does not yet prove the completed global square, because the primitive,
prime-square, and archimedean boundary currents are not independent direct
summands.

## New finite falsifier

Any proposed global block must restrict to these local chains. At a finite
cutoff test:

1. each prime block has the source shift \(S_N\);
2. its primitive incidence is \(e_0\);
3. its augmentation is derived rather than fitted;
4. its determinant zeros occur only at \(|q|=1\);
5. prime deletion recovers the smaller operator;
6. any new interior kernel in \(0<\Re s<1\) is carried by a declared
   cross-prime or boundary coupling.

An undeclared interior kernel disproves source-locality. A declared one
identifies the exact global interaction that must bear the RH content.

## Disposition

The bordered shift is a real advance in arithmetic provenance. It derives
the Euler factor from a labelled operator and supplies an independent local
acyclicity law.

It also localizes the hard problem sharply: RH-strength content cannot reside
inside a prime chain. It must reside in the coherence and completion that
assemble already-acyclic reciprocal local sectors into the completed global
section.
