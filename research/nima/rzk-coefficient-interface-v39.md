# v39: branch-supported line and reverse transgression

**Fixed-beta specialization:** [`rzk-coefficient-interface-v40.md`](rzk-coefficient-interface-v40.md)
records that the old primary class becomes exact after the physical D03 graph,
while its retained first symbol and the distinct X35 occurrence summand require
separate types.

Two modules record the newly constructed portion of the mixed-variance test.

`rzk/49-branch-rees-excess-and-occurrence-line.rzk.md` checks the product-Rees
source maps on the repeated-normal excess packet. Branch selection sends the
primitive excess `eta_u` to `eta_x`; the complementary-minor return sends it to
`tau_plus*eta_u`, not to `eta_u`. It also separates a principal occurrence
line from its multiplication map after branch selection: the line/dual pairing
is one while multiplication into the selected scalar branch is zero.

`rzk/50-finite-dual-transgression.rzk.md` records the finite homogeneous dual
variance. The primal connecting map sends the generic class to the short
obstruction; after integral dualization the reverse connecting map sends the
short functional to the generic functional. Both relevant pairings are one.
This preserves, rather than kills, the primitive transgression.

Fresh checks passed:

- module 49: 71-file closure, 26.95 seconds;
- module 50: 4-file closure, 0.85 seconds.

Evidence is in `results/49-branch-rees-excess-and-occurrence-line.typecheck.json`
and `results/50-finite-dual-transgression.typecheck.json`.

Scope: these modules formalize the key source coefficient identities, the
line-versus-zero-image distinction, and the direction of the finite dual
transgression. The 215-state purity comparison, nine-term obstruction,
82/89-generator selected Hom calculations, and identification with any spatial
supported Verdier dual remain certificate-backed or open. No physical parity
or complete exceptional correspondence is asserted.
