# Orientation-valued multi-residue

## Question

How can iterated channel residues be independent of an arbitrary ordering while retaining the required Koszul signs?

## Claim boundary

This construction packages normal-crossing residue orientation. It does not choose a contour, pole prescription, amplitude normalization, or physical orientation.

For a finite set `I` of channel divisors, define its orientation line

\[
\operatorname{or}(I)=\det(\mathbb Z^I).
\]

An ordering `sigma=(i_1,...,i_k)` gives a generator `[sigma]`. Permutation acts by its sign. If the ordinary ordered iterated residue is `r_sigma`, define

\[
\widetilde{\operatorname{Res}}_I(\Omega)
  =r_\sigma\otimes[\sigma]
\]

in the tangential-form target tensored with `or(I)`. Reordering by a permutation multiplies both factors by the same sign, so the tensor is invariant.

For disjoint channel sets `I,J`, wedge gives

\[
\operatorname{or}(I)\otimes\operatorname{or}(J)
\longrightarrow\operatorname{or}(I\sqcup J).
\]

This transport is associative and its symmetry is the Koszul sign `(-1)^(|I||J|)`. Consequently nested residues compose functorially after orientation-line transport; they do not commute as untwisted forms.

At five points each maximal compatible set has two channels. The exact checker verifies both orders for all five faces, canonicalizes them into the same orientation-valued element, and confirms direct and nested residues agree. Incompatible pairs have zero double Laurent coefficient and are not promoted to polygon faces.

## Disposition

The sign discrepancy is resolved by changing the residue codomain, not by suppressing signs. Multi-residue factorization is canonical in the orientation-twisted target. Contour and normalization data remain separate arrows.
