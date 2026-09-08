# v49: cubical supported-dual critical edge

**Recollement update:** [`rzk-coefficient-interface-v50.md`](rzk-coefficient-interface-v50.md)
separates finite union duality from all-thickening local cohomology and records
that both Q obstructions persist on the genuine open complement.

`rzk/64-cubical-supported-dual-critical-edge.rzk.md` identifies the cubical
spatial dual cell type with the existing generated 215-cell loaded target type
and internalizes the critical complementary-support incidence.

The relative interval has an actual edge `J` and its marked-D25 generic lower
vertex. Its upper endpoint is absent as a relative face, so

    boundary J = -[D25].

With the verified product orientation the short-support representative is
`Xi_B=-J` and the generic representative is `Xi_Q=[D25]`. Rzk proves

    boundary Xi_B = Xi_Q

using integral sign involutivity, and proves that the corresponding short and
generic coordinate evaluations are both one. The module separately types the
full, endpoint-complement, and generic-tripod supports, both endpoint
meridians, and the strict cubical/AW diagonal compatibility assertions.

A fresh 72-file transitive closure passed in 41.68 seconds. Evidence:
`results/64-cubical-supported-dual-critical-edge.typecheck.json`.

Scope: the critical edge and its primitive evaluations are native Rzk. The
complete 215-column signed cube identification, 575 relative coefficient
frames, 2,304 multiplication arrows, cap coassociativity matrices, endpoint
collar operators, and 2,816 supported-tensor columns remain certificate-backed.
The physical normalization-sheet morphism into this kernel is still absent.
