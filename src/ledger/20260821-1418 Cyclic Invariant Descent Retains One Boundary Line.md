# 1418 — Cyclic Invariant Descent Retains One Boundary Line

## Status

Source-normalized algebraic (C_5)-descent in the tested modular coefficient orbit.

## Source transition

The frozen five-cycle OFPT packet contains (36) cyclic term orbits, each of size five, and all (180) orientation-normalized term weights equal (+1).

Thus the labelled transition on a coefficient orbit is the unsigned cyclic permutation

\[
T=
\begin{pmatrix}
0&0&0&0&1\\
1&0&0&0&0\\
0&1&0&0&0\\
0&0&1&0&0\\
0&0&0&1&0
\end{pmatrix},
\qquad T^5=1.
\]

No fitted sign or transition unit is introduced.

## Canonical projector

Away from characteristic five, the invariant projector is

\[
P_{\rm inv}
=
\frac15\sum_{k=0}^4T^k
=
\frac15J_5,
\]

where (J_5) is the all-ones matrix.

The regular orbit splits canonically as

\[
\mathbf F_p[C_5]
=
\mathbf 1
\oplus
V_{\rm aug}.
\]

## Two-prime calculation

For Entry 1417’s first orbit vectors, the invariant coordinates are

\[
P_{\rm inv}(623,284,472,749,116)
=
245(1,1,1,1,1)
\quad\bmod1019,
\]

and

\[
P_{\rm inv}(207,6,82,588,481)
=
71(1,1,1,1,1)
\quad\bmod1009.
\]

Both are nonzero.

The complementary augmentation vectors have coordinate sum zero and are killed by (P_{\rm inv}).

## Narrow result

Ordinary algebraic cyclic descent produces

\[
\boxed{
(\text{Cut-defect line}\otimes\mathbf F_p[C_5])^{C_5}
\simeq
\text{Cut-defect line}.
}
\]

Thus the rank-five labelled coefficient orbit is not wholly presentation noise: one invariant boundary line survives. Its four-dimensional augmentation component records occurrence-resolved cyclic transport and disappears after ordinary invariants.

## Type boundary

This is an algebraic invariant descent, not yet a theorem that the physical string observable is obtained by ordinary (C_5)-invariants. A physical quotient could retain equivariant or twisted data. Such a different descent functor must be source-derived.

## Next finite falsifier

Identify the invariant line’s source functional before modular specialization. Test whether it is the cyclic average of a labelled residue/Gysin map and whether that average commutes with the declared radial boundary specialization.

Artifacts:

- `research/benincasa/results/five-cycle-ofpt-packet.json`
- `research/benincasa/results/five-site-cyclic-coefficient-orbit.json`
- `research/benincasa/results/five-site-cyclic-invariant-descent.json`

Allocator claim: `seqclaim-de4253f56016991419ec3c70`.
