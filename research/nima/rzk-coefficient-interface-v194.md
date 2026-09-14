# v194: source occurrence label for the qg2 road class

The qg2 endpoint/conductor coordinate is explicitly identified with the
source-labelled cyclic Leray edge by

`v=2(xi+1)/(1-kappa)`.

This sends `xi=-1` to `v=0` and `xi=-kappa` to `v=2`. Pulling back the
G31-to-G12 Leray transition connection gives

`dlog((xi+1)/(xi+kappa))`,

with residue vector `(1,-1)` at endpoint and conductor. This is exactly the odd
relative orientation carried by the road class. The three source Leray frames
have transition product one, so the label is part of a closed cyclic cocycle,
not an unlabelled local choice.

Together with v193, the ramified branch-difference road class now descends to
the selected logarithmic line with a fixed G31-to-G12 occurrence label. The
remaining road gate is equality with the independently defined raw physical
Cech defect; occurrence provenance itself is no longer missing.

Evidence is `results/qg2-occurrence-leray-descent.json`.
`rzk/222-qg2-occurrence-leray-descent.rzk.md` passes all eight declarations
without assumptions.
