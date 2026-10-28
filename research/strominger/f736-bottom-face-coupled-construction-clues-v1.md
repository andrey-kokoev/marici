# Calculate the bottom face and tetrahedral filler together

## Correction to the working target

Do not first choose an arbitrary F736 face modification and then append a tetrahedral certificate. The bottom face and higher coherence belong to one dependent construction. Two incident tetrahedra must use the SAME F736 witness on their shared boundary.

This source search found an explicit coupled law and an analytical positive-lift architecture. It does not newly construct the physical lift or run verification tools.

## 1. Prior research states the coupling explicitly

`research/voevodsky/combining-h234-and-h134-localizes-the-open-class-to-the-kernel-of-positive-to-signed-forgetfulness.md` uses

    H124 o (H234 * eta12) = H134 o (eta34 * H123).

Faithful observer whiskering recovers the bottom H234 from the other witnesses. The paper explicitly says the H234 and H134 positive lifts are NOT independent choices: they must lie over this same signed horn. Signed asymptotic coherence is already supplied; the stronger physical positive lift is not inferred from it.

`research/voevodsky/the-first-elementary-conductor-tetrahedron-has-four-transfer-equations-and-one-higher-coherence-equation.md` separately emphasizes that equality of edge composites is weaker than equality of the chosen face homotopies. This is why a strict chart equation does not independently discharge the tetrahedral filler.

## 2. The actual bottom faces in the F736 patch

Extracted from the existing `research/voevodsky/results/esd7_explicit_analytical_census.json` (read, not regenerated):

| tetrahedron | local vertices 1,2,3,4 | H123 | H124 | H134 | bottom H234 |
|---|---|---|---|---|---|
| T324 | V104,V105,V111,V113 | F731 | F732 | F736 | F745 |
| T325 | V104,V110,V111,V113 | F734 | F735 | F736 | F760 |

Let e_ID denote its geometric edge map, H_ID its chosen face modification. Both tetrahedra have local edge34=E539 and edge13=E514. Their two actual pasting equations are

    H732 o (H745 * e511)
       = H736 o (e539 * H731),                 [T324]

    H735 o (H760 * e513)
       = H736 o (e539 * H734).                 [T325]

Composition is right to left. Each side in the first equation reduces e539 e519 e511 to e515; each side in the second reduces e539 e535 e513 to e515.

The tetrahedral fillers Theta324 and Theta325 are the specified equalities/higher comparisons between these seams. They cannot be certified by comparing only final scalar readouts. H736 must be literally the shared face datum (or related by an explicitly supplied common-boundary identification), not chosen independently on the two sides.

Thus the retained package to calculate is

    (H736, H745, H760, Theta324, Theta325)

with the other faces/edges and their domains specified, not a lone H736 value. Where the other faces are also unknown they remain components of this same dependent boundary problem, not assumed inputs disguised as established witnesses.

## 3. Occurrence extraction identifies where the analytical parent witness sits

The actual words, retaining zero-based occurrences4 and5, are

    V104: (...,2,4,4)
    V105: (...,2,3,4)
    V110: (...,1,4,4)
    V111: (...,1,3,4)
    V113: (...,1,2,4),

where the omitted first four entries are all1.

In T324, increment order is3,1,2. In T325 it is1,3,2.

- F745 has occurrence triples (2,1,1) at occurrence4 and (3,3,2) at occurrence5. Each component triangle is degenerate, while the two changing coordinates require retained inter-occurrence compatibility.
- F760 has (1,1,1) at occurrence4 and (4,3,2) at occurrence5: its nondegenerate component is the geometric reverse H234 witness.
- F732 also carries (4,3,2) at occurrence5, with occurrence4 triple (2,2,1).
- F735 has only degenerate component triangles; it compares the occurrence4 change with a direct occurrence5 change.
- F731/F734 compare the two orders of the disjoint occurrence4/5 changes.

This gives a useful coupled construction pattern: carry one chosen analytical reverse-H234 witness into F760 and F732 with the required source-labelled whiskers; use retained disjoint-occurrence comparisons for the other faces; derive/check the SAME H736 and both Theta equations. The equations then compare two placements of the same analytical witness, rather than independently selecting bottom and filler data.

This is a conditional extraction pattern, not an assertion that the needed analytical realization comparison and whiskers are already identified. Degenerate component triangles do not justify deleting cross-occurrence coherence or residual coordinates.

## 4. Faithful recovery calculates bottom and coherence as one pair

In a target where the relevant faces are invertible, rearrange the tetrahedral equation to obtain

    H234 * eta12
      = H124^(-1) o H134 o (eta34 * H123).

Apply inverse faithful whiskering on the observer-generated essential image. The recovery must return not only H234 but its comparison identifying its whiskering with the displayed seam. That comparison is the tetrahedral coherence witness. In higher-categorical language, the solution is a point in the homotopy fiber of the whiskering map over the prescribed composite, not a separately chosen face followed by an unrelated assertion that the boundary closes.

Source: `research/voevodsky/face-234-is-uniquely-recovered-on-the-observer-generated-geometric-subcategory-by-faithful-whiskering-along-the-integrated-representation.md`.

For this patch apply the construction twice over the shared H736, using e511 for T324 and e513 for T325, only after proving that these ACTUAL fine edge whiskerings have the required lift/recovery property. The parent theorem for U_S does not automatically establish that property for every fine edge. Alternatively, construct the whole patch as the image of one already-defined analytical simplex with its boundary identifications.

H124 inverse is available in the declared signed asymptotic quotient, not as an exact finite-cutoff inverse. The representative cutoff remainder must remain in the finite data.

## 5. For a positive physical calculation: one shared block, not two independent bonds

`research/voevodsky/the-two-missing-bonds-are-one-schur-douglas-positivity-condition.md` gives the coupled candidate

    C = G_physical^T - (D)_+
      = G_physical^0 - (D)_-,

and the external odd endpoint coupling b, with

    K = [[C,b],[b*,1]].

The equivalences are

    K >= 0
      iff C >= b b*
      iff b = C^(1/2) c for a contraction c.

The equality defining C is the common-bulk part of H234; the actual Green endpoint coupling b is the H134 boundary part. Calculating them together on the SAME source/regulated carrier is the proposed analytic route. Independently choosing a Jordan decomposition for each side loses the required common physical remainder.

This note proves the equivalence under its carrier/domain identifications; it does NOT prove the source estimate ||b* u||^2 <= <u,C u>. On unbounded/form carriers, domains and closed realizations must be fixed before using a bounded block argument.

`research/voevodsky/the-four-face-tetrahedral-horn-unfolds-to-a-polarity-cube-and-a-k-axis-four-cube.md` adds that both polarities must share that bulk before compression, and successor maps must transport the common factorization. Polarity and refinement are separate axes.

## 6. How to obtain b without assuming the desired metric equality

`research/voevodsky/correction-the-external-green-comparison-is-a-boundary-triple-problem-not-a-direct-intertwiner.md` rules out a naive direct intertwiner between the first-order Euler connection and second-order endpoint Laplacian.

Its replacement is an endpoint-augmented Heisenberg/Clifford carrier with a boundary triple/Weyl function retaining the contour differential and endpoint residues. A generalized Nevanlinna kernel has one negative square before odd-parity cancellation. The required positive statement is cancellation under source compression, not signed trace equality.

The internal derived endpoint row cannot be substituted for the externally normalized Green row without a comparison. A joint graph can retain both as separate source-labelled legs if metric equality has not been proved.

## 7. Retain the residual carrier, not only its scalar shadow

`research/voevodsky/the-correct-top-coherencer-is-the-mapping-cone-package-of-the-codiagonal-not-its-scalar-quotient.md` supplies an architectural clue: retain a relative cone [G -> Y] so source directions lost by scalarization survive as kernel data, with the adjoint supplied by an actual Green mate.

This paper concerns a higher cone/determinant comparison, not a ready-made F736 constructor. Its applicable lesson is to calculate the boundary map and its relative witness on the retained carrier together; scalar residual cancellation does not recover the erased states or their energy.

## Constructive target after this search

Calculate one coupled patch object carrying both actual bottom faces, the common F736 face, and both tetrahedral comparisons. Use the parent analytical H234 representative and a specified reverse mate in the SAME target. Place it consistently on F760 and F732, retain the disjoint-occurrence comparisons, and enforce the two explicit seam equations above.

If positive physical identification is required, construct C and the external b jointly from the regulated source/Green data and prove the common Schur--Douglas bound; do not infer it from signed coherence or internally defined endpoints. Preserve exact observer placements, finite-cutoff remainder and Mellin endpoints throughout.

This search changes the target from an isolated face-filler task to a dependent bottom-face-and-tetrahedral-coherence calculation. It does not claim that the resulting analytical F736 package or positive inequality has been constructed.
