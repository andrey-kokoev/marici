# v51: first-conductor and coherent primary frames

**Descent update:** [`rzk-coefficient-interface-v52.md`](rzk-coefficient-interface-v52.md)
records seven local unit lifts whose twelve overlap residues form a primitive
nontrivial Cech torsor, so local existence does not produce a global unit lift.

`rzk/66-first-conductor-framed-deformations.rzk.md` prevents the weight-zero
rigidity result from being transported to first conductor degree. It records
nine endpoint/Q-zero cycle directions, six nonzero supported-map directions at
the fixed regulator grade, and the two-term Y02 carrier with annihilator modes
`beta,X13,X15,X35`. A frame-level classifier explicitly returns rigidity only
at occurrence weight zero and six map directions at first negative conductor
order.

`rzk/67-coherent-endpoint-q-primary-frame.rzk.md` records the genuine boundary
object containing full Q14 and both endpoint-top two-term packets, together
with the 448-state coherent fibre and 412-state strict kernel models. All twelve
weight-zero coherent supported-map classes are classified as changing the
primary. The primary-fixed fibre is contractible when nonempty, but the
specified `-beta*chi` primary has empty fibre. The framed chi generator is
primitive and uses the strict/faithful annihilator status from module 63.

Fresh transitive checks passed (closures of 6 and 74 files). Evidence is in
`results/66-first-conductor-framed-deformations.typecheck.json` and
`results/67-coherent-endpoint-q-primary-frame.typecheck.json`.

Scope: these modules encode the decisive degree/frame distinctions and finite
class labels. The nine explicit polynomial cycles, annihilator completeness,
448-to-412 contraction, free chi detector, and polynomial homology normal forms
remain certificate-backed. No physical endpoint frame or Delta_J is selected.
