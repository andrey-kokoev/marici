# v191: ambient conductor transport is canonically ramified and odd

The higher-order conductor face does not remain at `xi=-kappa` along the
ordinary x-collar. After restricting the exceptional kernel to the exact qg2
strict transform, its discriminant as a polynomial in xi has a generic simple
factor x. Therefore the conductor roots split with Puiseux order `sqrt(x)`.

After the base change `x=h^2`, a conductor branch has

`xi=-kappa+c h+O(h^2)`

with

`c^2=(kappa-2)(kappa-1)(kappa+1)/(2p)`.

Deck transformation `h -> -h` exchanges the two branches and supplies the
character -1. Thus the odd orientation needed to compare with the log
primitive is not an added sign: it is the canonical monodromy of the ambient
ramified conductor transport. This refines v188's formal relative-cut sign
line and explains why the normalized wall Kummer character can be trivial
while ambient transport is odd.

The unramified prism of v190 is valid on the qg2 wall but insufficient at its
conductor face. The remaining geometric target is the ringed filtered Q map on
this ramified nearby-cycle double cover.

Evidence is `results/qg2-ramified-conductor-transport.json`.
`rzk/219-qg2-ramified-conductor-transport.rzk.md` passes all eight declarations
without assumptions.
