# v47: regulator vertices and orbit-source assembly

**Endpoint/Q compatibility:** [`rzk-coefficient-interface-v48.md`](rzk-coefficient-interface-v48.md)
records the forced beta-squared Q order and the nonzero beta-times-short-boundary
obstruction hidden by the supported Q-nullhomotopy.

`rzk/61-regulator-vertex-decomposition.rzk.md` introduces all fourteen labelled
triangulation vertices and the native nine-vertex vector representing the
supported map difference. It separately records the two fixed-primary cycle
directions: `Psi` has both endpoint-top coordinates, while `Z` has only the
negative endpoint coordinate. The endpoint quotient retains an explicit
nonzero eight-vertex vector; endpoint removal therefore does not erase the
comparison obstruction.

`rzk/62-orbit-source-assembly-gate.rzk.md` gives the common-intersection tensor
and closed-support union different types. The intersection class has degree-six
placement and reuses the checked strict Q section. Union dual strata occur in
degrees two, three, and four, are classified as having no derived Q section,
and retain the local pair operation on the separating open. The intersection
is instead contractible on the six-parameter generic open. A primitive typed
localized divisibility obstruction records the failed union section.

Fresh checks passed with 71-file and 76-file transitive closures. Evidence is
in `results/61-regulator-vertex-decomposition.typecheck.json` and
`results/62-orbit-source-assembly-gate.typecheck.json`.

Scope: Rzk records the finite labelled decomposition and the decisive assembly
type distinctions. The 462-state Hom reduction, Bockstein Smith matrix,
28-generator union resolution, its full dual differential, and the proof that
the union section space is empty remain certificate-backed. No native physical
assembly is selected.
