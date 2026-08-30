# The Toeplitz boundary index is the Euler logarithmic derivative

## Local polarized valuation carrier

Fix a prime `p`. Let `V` be the unilateral shift on the valuation basis
`e_0,e_1,...`:

\[
Ve_r=e_{r+1}.
\]

Its depth-`k` boundary defect is

\[
P_k=I-V^kV^{*k}.
\]

This is the projection onto

\[
\operatorname{span}\{e_0,\ldots,e_{k-1}\},
\]

and hence

\[
\operatorname{Tr}P_k=k.
\]

The integer `k` is not an assigned prime-power multiplicity. It is the index
of the `k`-step unilateral valuation transport: exactly `k` partners are lost
at the polarization boundary.

## Transgression of the Euler logarithm

Put `z=p^{-s}` in the Euler chamber. The connected cyclic expansion is

\[
-\log(1-z)=\sum_{k\ge1}\frac{z^k}{k}.
\]

Pair each cyclic word with its source boundary defect. Then

\[
\sum_{k\ge1}
\frac{z^k}{k}\operatorname{Tr}P_k
=
\sum_{k\ge1}z^k
=
z\frac{d}{dz}\bigl[-\log(1-z)\bigr].
\]

Thus the Toeplitz boundary map implements the Euler logarithmic derivative:
the rank `k` boundary index cancels the cyclic automorphism weight `1/k`.
This is one operation, not two independent appearances of `k`.

Since

\[
-\frac{d}{ds}
\bigl[-\log(1-p^{-s})\bigr]
=(\log p)\sum_{k\ge1}p^{-ks},
\]

every prime power receives the same primitive weight `log p`. The von
Mangoldt rule is therefore the boundary-index image of the connected Euler
cycle:

\[
\frac1k
\times
\operatorname{rank}P_k
\times
\log p
=
\log p.
\]

## One new boundary cell per depth

The defects are nested and satisfy

\[
P_k-P_{k-1}=|e_{k-1}\rangle\langle e_{k-1}|.
\]

Consequently each new prime-power depth contributes exactly one new boundary
cell. This explains simultaneously:

- why prime powers occur;
- why mixed squarefree labels do not become primitive von Mangoldt atoms;
- why the coefficient is independent of exponent after logarithmic
  differentiation;
- and why the first two depths can occupy exceptional completion grades even
  though their local incidence rule is uniform.

## Reciprocal orientation

On the bilateral valuation carrier, the shift is invertible and `P_k=0`.
The defect appears only after choosing a valuation cone. The opposite cone
has the oppositely oriented unilateral index. Fourier exchanges the cones,
so the local current is a relative boundary class rather than an absolute
positive operator on one tower.

This prevents a false inference: the index formula explains the arithmetic
current but does not orient the completed theta comparison or confine zeros.
The RH-bearing construction must still sew the two oppositely oriented
boundary currents with the archimedean source.

## Falsifiers

The explanation fails for any proposed valuation model in which:

1. the depth-`k` defect does not have rank `k`;
2. the cyclic coefficient is not `1/k`;
3. mixed-prime words acquire a unilateral defect in a primitive prime ray;
4. Fourier is claimed to preserve the sign of the polarized index;
5. the local index identity is promoted directly to global zero confinement.

## Result

The uniform von Mangoldt coefficient at `p^k` has a source-level index
explanation. A length-`k` connected Euler cycle carries weight `1/k`, while
its unilateral valuation transport loses `k` boundary states. Their pairing
is one boundary cell at every depth, and Mellin differentiation supplies its
weight `log p`.
