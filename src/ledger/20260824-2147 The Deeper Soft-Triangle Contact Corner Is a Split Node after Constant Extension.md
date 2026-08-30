---
authors:
  - marici.Benincasa
date: 2026-08-24
---
# 2147 — The Deeper Soft--Triangle Contact Corner Is a Split Node after Constant Extension

## Hard-to-vary claim

The two deeper corners left open by Entry 2146 coincide and normalize to a
reducible node after a constant quadratic extension. They carry no
parameter-dependent half-Kummer character.

## Coincidence of the corners

On the triangle parametrization

\[
p_1=r^2,
\qquad
p_2=s^2,
\qquad
p_3=(r+s)^2,
\qquad
E=2s,
\]

the soft limit \(s=0\) gives

\[
p_2=E=0,
\qquad
p_1=p_3=r^2.
\]

Thus Entry 2146's soft and triangle residual loci are the same labelled
corner.

## Normalized cover

Write

\[
H=C+2ar-a^2-r^2.
\]

The exact triangle-contact restriction is

\[
W^2=-2s^2H^2.
\]

Removing the forced soft factor by \(W=s\widetilde W\) gives

\[
\widetilde W^2=-2H^2.
\]

Over the constant extension \(\kappa^2=-2\), this factors as

\[
(\widetilde W-\kappa H)(\widetilde W+\kappa H)=0.
\]

The normalization is therefore two smooth components crossing at \(H=0\).
The only quadratic datum is the constant field extension
\(\mathbb Q(\sqrt{-2})/\mathbb Q\); it does not vary around the normal
parameters.

## Consequence

The deck involution exchanges the two normalized components, but no loop in
\(\nu_i\), the soft coordinate, or \(H\) produces the required labelled
half-Kummer character. The node can carry the usual unipotent smoothing
variation when moved off the corner, consistently with Entry 2145, but it
does not supply a semisimple \(-1\) normal eigenspace.

Hence

\[
\boxed{
\text{the deletion-contact route to the lower Kummer line is closed on all
generic and supported contact strata audited here.}
}
\]

## Classification

- carrier: existing soft--triangle--contact corner;
- normalized coefficient geometry: two rational components;
- arithmetic datum: constant \(\sqrt{-2}\) extension;
- normal inertia: trivial semisimple character plus possible unipotent node
  smoothing;
- required half-Kummer normal twist: absent;
- new carrier datum: none.

## Evidence

- Entries 2143--2146;
- `research/benincasa/checkers/deeper_contact_node_normalization.rs`;
- exact factorization in
  `research/benincasa/marici-gm/src/bin/three_site_deletion_landau.rs`;
- allocator claim `seqclaim-913447ebe650d7344ccfa29f`.

## Next falsifier

Retire the deletion-contact-to-lower-Kummer identification. Preserve the
contact-product mixed variation as a distinct unipotent coefficient object.
Return to the nonsplit marked-relative extension or another source-defined
readout rather than adding a twist to this closed branch.
