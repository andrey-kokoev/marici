# Separated Boundary Support Prevents Cancellation but Not Annihilation

Epistemic-graph event: 1333.

For a quotient tower, write

`Omega_(r q)=Omega_r S_q+S_r Omega_q`.

If the images of the two summands lie in disjoint terminal boundary-stratum
subspaces, a zero composite forces both transported defects to vanish.  To
deduce the original stage defects, however, `S_q` must detect the later
defect—surjectivity suffices—and `S_r` must be injective on the earlier
defect image.

This matters for deck quotients: their formal Betti maps are surjective but
not injective.  Even with separated supports, a later quotient can annihilate
an earlier defect in its kernel.  For example, `S_r=[1 0]` kills a nonzero
`Omega_q` supported on `(0,1)`, leaving the composite defect zero.

Therefore source-labelled support eliminates cancellation but does not
replace one-bit testing unless faithfulness on every defect image is also
proved.

Research note:
`research/grothendieck/separated-support-boundary-defect-detection.md`.
