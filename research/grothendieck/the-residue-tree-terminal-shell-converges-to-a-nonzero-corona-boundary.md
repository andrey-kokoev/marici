# The Residue-Tree Terminal Shell Converges to a Nonzero Corona Boundary

## Dual completion directions

The residue tree generated from the unramified vacuum has discrete label group

\[
A_p=\mathbb Q_p/\mathbb Z_p.
\]

Its Pontryagin dual is the compact group

\[
\widehat A_p=\mathbb Z_p.
\]

Finite residue packets form the algebraic inductive state space
\(\mathbb C_c[A_p]\). Finite-conductor observables on \(\mathbb Z_p\) form the
cylindrical test algebra, and their continuous dual is the corresponding
projective distribution space.

For \(r\in A_p\), the coset state

\[
e_r=1_{r+\mathbb Z_p}
\]

has Fourier transform

\[
\widehat e_r(\xi)=\chi_p(r\xi)1_{\mathbb Z_p}(\xi).
\]

This gives a source-derived nondegenerate pairing between finite residue
states and finite-conductor observables. It is the local finite Fourier
pairing at every tree depth.

## The escaping translation orbit

Let \(r_k=p^{-k}\) modulo \(\mathbb Z_p\). The states \(e_{r_k}\) have pairwise
disjoint support and satisfy

\[
\|e_{r_k}\|_2=1.
\]

Hence they do not converge strongly to zero. They do converge weakly to zero.
Indeed, every compactly supported locally constant additive test meets only
finitely many of the escaping cosets. Equivalently, on the Fourier side the
characters

\[
\chi_p(p^{-k}\xi)
\]

are orthogonal to every fixed finite-conductor observable once \(k\) exceeds
its conductor.

Thus the state--observable pairing is nondegenerate at every finite level but
has no uniform lower bound along the dilation orbit.

## Terminal difference shell

For the unramified vacuum \(e_0=1_{\mathbb Z_p}\), the terminal difference is

\[
\Delta_{r_k}e_0=e_{r_k}-e_0.
\]

Its norm is constant:

\[
\|\Delta_{r_k}e_0\|_2^2=2.
\]

Nevertheless,

\[
\Delta_{r_k}e_0\rightharpoonup-e_0.
\]

The omitted terminal shell therefore does not vanish in the natural weak
completion. Its escaping branch becomes invisible, while the stationary
common mode remains as a nonzero corona boundary.

The Fourier statement is identical:

\[
(\chi_p(p^{-k}\xi)-1)1_{\mathbb Z_p}(\xi)
\rightharpoonup
-1_{\mathbb Z_p}(\xi).
\]

## Consequence for current descent

The finite affine identity

\[
D_p\Delta_h=\Delta_{h/p}D_p
\]

continues to hold, but telescoping conductor cutoffs does not produce zero
terminal flux. The limiting boundary includes the unramified common mode.

Therefore the residue-tree pairing is:

- exact and nondegenerate on every finite packet;
- continuous against fixed cylindrical observables;
- noncoercive along dilation;
- insufficient for a vanishing-boundary Green theorem unless a separately
  sourced reciprocal or archimedean channel cancels the corona mode.

Deleting the common mode would manufacture exactness by quotient. Adding its
negative by hand would fit the desired current. Either move is unauthorized.

## Scope and next gate

This is a local completion theorem. It does not determine whether the
reciprocal local chart supplies the opposite corona mode, nor whether the
restricted product of those local cancellations converges.

The next exact test is doubled local sewing. Construct the reciprocal residue
tree independently, transport its terminal difference through local Fourier--
Tate normalization, and compare the two corona limits in the common boundary
frame. Cancellation must follow from opposite incidence orientation, not from
declaring the two copies equal.
