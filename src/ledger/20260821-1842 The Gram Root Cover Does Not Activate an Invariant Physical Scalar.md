# 1842 — The Gram Root Cover Does Not Activate an Invariant Physical Scalar

## Deck character upstairs

Entry 1841 requires the root cover

\[
\pi:z\longmapsto\Omega=z^2.
\]

The polar square-root coefficient is generated upstairs by

\[
z^{-1}.
\]

Under the deck involution \(\tau(z)=-z\),

\[
\tau(z^{-1})=-z^{-1}.
\]

Thus the polar line is anti-invariant even though its local monodromy has been
trivialized on the cover.

## Trace obstruction

The ordinary normalized trace is

\[
\operatorname{Tr}_{\mu_2}(z^{-1})
=
\frac12\left(z^{-1}+(-z)^{-1}\right)
=0.
\]

Consequently

\[
\boxed{
\operatorname{rank}(\pi_*\mathcal L_{m polar})^{+}=0,
\qquad
\operatorname{rank}(\pi_*\mathcal L_{m polar})^{-}=1.
}
\]

The Gram root cover alone does not produce an invariant physical scalar.

## Required physical datum

A nonzero descended pairing requires another anti-invariant factor, such as a
source-derived orientation line or physical relative-chain character.  The
product of the two sign characters can then be invariant.

No such physical-chain character is present in the current five-cycle
incidence packet.  Therefore polar physical activation remains undefined,
not zero: the coefficient line exists, but its required dual sign object has
not been supplied.

## Architectural consequence

Again no carrier change is required.  The missing object is sector-specific
coefficient/Betti data:

\[
\boxed{
\mu_2\text{ sign local system}
\otimes
\text{anti-invariant physical orientation}.
}
\]

This sharply separates ramified coefficient descent from carrier incidence.

## Next falsifier

Audit the primary five-cycle contour, if available, for its Gram-root deck
character.  If it is anti-invariant, compute the normalized pairing.  If it is
invariant, the polar coefficient is physically invisible.  If no contour is
available, retain activation as undefined without fitting a sign.

## Evidence

- `research/benincasa/checkers/five_site_region_pair_gram_root_trace.py`
- `research/benincasa/results/five-site-region-pair-gram-root-trace.json`
- Entries 1840--1841
- allocator claim: `seqclaim-f081cf7c4d0de3b1dff511d7`
