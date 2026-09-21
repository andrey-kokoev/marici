# Enriched pre-compression block complex for packet refinement

The packet refinement result fixes the next construction: each block must retain its full relation tower before applying the first seam derivative.

For a block with event length n, define the enriched block object by the direct sum of its associated relation layers, with the canonical source attachments retained:

    E_block(n) = G^0 ⊕ G^1[1] ⊕ G^2[2] ⊕ ...,

where G^r=I^r/I^(r+1), and each successive connecting map is the one induced by multiplication and the source short exact sequence. The displayed grading is derived degree, not retained-letter degree.

For a cut tree, take the labelled external tensor of the enriched block objects, retaining every intermediate vertex. The refinement map is defined before compression by:

1. refining each event window into its smaller chamber windows;
2. applying the corner inclusion on every typed relation layer;
3. applying the source connecting maps;
4. reassociating the external tensor factors with the cochain signs;
5. only then applying the local seam derivative on the desired layer.

This order is forced. If a block is first replaced by its conormal seam image, an internal product such as `ab` is killed and no subsequent linear refinement can recover its three-seam image.

At relation power r, the minimal 2r-event packet contributes a raw r-seam tensor degree -r. The derived quotient shift sends it to degree -1. Thus the first three layers use shifts 0, -1, and -2 for dimensions 2, 24, and 720 respectively.

The construction is not an assertion that the direct sum is a split object in the original source-module category. The extension maps between layers are part of the enriched object. A packet refinement is admitted only when it commutes with those maps and with the retained middle-label decomposition.

The immediate finite acceptance test is the six-prime three-block hostile: compare refinement before compression with refinement after two-seam compression. The former must map the 720-dimensional triple-product layer into the three-seam carrier; the latter must fail on the explicit product `a b c`. This distinguishes a genuine enriched refinement map from a dimension-preserving but information-losing regrouping.

The resulting object is the source-side input for the eventual analytic Clark realization. No Green form, infinite completion, or terminal scalar descent is included until this enriched refinement is established.
