# Arbitrary-n cyclic invariance of the one-loop MHV Kermit sum

## Theorem

Let `T_n^(r)` be the one-loop MHV Kermit decomposition anchored at cyclic label `r`, obtained by cyclically relabelling the sourced formula

$$
T_n^{(1)}=\sum_{1<a<b<n}K[a;b].
$$

Then for every `n>=4` and every anchor `r`,

$$
\Omega(T_n^{(r)})=\Omega(T_n^{(1)}).
$$

Hence the complete pre-integration one-loop MHV integrand is cyclically invariant.

## Internal boundaries

For a fixed anchor `r`, every nonlocal divisor has the form

$$
\langle AB\,r k\rangle=0
$$

with `k` nonadjacent to `r`. The arbitrary-n Kermit facet involution pairs its incident cells by replacing `k-1` with `k` while retaining the other cell label. The two induced facet orientations are opposite. Therefore all anchor-dependent internal facets cancel.

## External boundary

The uncancelled facets are precisely the cyclic local propagators

$$
\langle AB\,i(i+1)\rangle=0,
\qquad i\in\mathbb Z/n\mathbb Z.
$$

This set and its outward cyclic orientation do not depend on the chosen anchor. On each physical divisor, the incident Kermit residues form a triangulation of the same induced boundary positive geometry. Thus all anchored chains have the same oriented physical boundary canonical form.

## Canonical-form uniqueness

The sourced Kermit representations are triangulations of the same one-loop MHV positive geometry on the projective line space `Gr(2,4)`. Canonical forms are additive under oriented triangulation and uniquely determined by logarithmic residues on the oriented boundary, with no additional pole at infinity.

Consequently, for any anchors `r,s`,

$$
\partial T_n^{(r)}=\partial T_n^{(s)}
$$

implies

$$
\Omega(T_n^{(r)})=\Omega(T_n^{(s)}).
$$

Taking `s=r+1` proves invariance under the cyclic generator and therefore under every cyclic relabelling.

## Equivalent residue argument

The difference

$$
D_n^{(r)}=\Omega(T_n^{(r+1)})-\Omega(T_n^{(r)})
$$

has zero residue on every nonlocal divisor because each anchored sum cancels its own internal poles. It has zero residue on every physical divisor because the two sums induce the same boundary canonical form. Projectivity excludes a polynomial top-form remainder or a pole at infinity. Hence `D_n^(r)=0`.

## Executable evidence

`check_one_loop_mhv_kermit_cyclic_invariance.py` reconstructs the complete rational sum with every possible cyclic anchor and verifies exact equality at generic rational momentum-twistor kinematics for `4<=n<=9`.

## Claim boundary

This proves cyclic invariance of the sourced pre-integration one-loop MHV integrand. It does not establish reflection parity, integrated cyclicity after a regulator is chosen, or corresponding statements for NMHV loop integrands.
