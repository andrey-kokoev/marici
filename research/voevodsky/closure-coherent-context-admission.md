# Coherent comparisons lift through arbitrary finite contexts

## Proved

`agda/ClosureCoherentContextAdmission.agda` lifts an endpoint-coherent comparison through any finite one-hole bracketing context, with arbitrary finite siblings and arbitrary attachment maps.

The input contains the actual equivalence, a normalization path, both external port witnesses, and their higher compatibility with that normalization path. The output retains all five fields, so lifting can continue through the next ancestor.

The resulting contextual comparison is admitted by the existing normalizer. Its equivalence is the recursively constructed `LiftSpan` comparison, not a replacement by the generated normal-form map.

## Parent step

`agda/ClosureContextualForkAdmission.agda` handles simultaneous changes of both children. It uses the left child's last-port coherence and the right child's first-port coherence on the shared attachment boundary.

The composition theorem first compares normalization after the actual parent comparison with the composite child frames. A path of pushout comparison frames then moves those composites to the source normalizer, carrying the attachment-square witnesses along with them. Applying `appendFrame` produces the parent normalization square.

The unused external ports are inherited from the left child's first port and the right child's last port. Their higher cells are preserved, rather than discarded after proving the parent square.

Identity siblings are explicit specializations. Their port coherence contracts the extra left unit in the composite witness; it is not assumed judgmentally reflexive.

## Port propagation

`agda/ClosureContextualPortCoherence.agda` proves the helper needed to propagate an endpoint square through an inclusion and a flattening map.

It accounts for the leading composition unit in the parent normalization path and the associativity/distribution corrections in the prescribed endpoint witnesses. Those corrections are essential for recursive contextual lifting.

## Regressions

`agda/ClosureContextualForkAdmissionRegression.agda` uses circle pieces attached along Unit, with provably noninvertible attachment maps.

The child equivalence is the identity, but its normalization path and port witnesses rotate around the circle. Both left and right parent admissions type-check, including specializations with arbitrary siblings. Detectors prove that the parent normalization squares retain the nontrivial chosen data. Replacing the port witness by reflexivity while retaining the normalization path is proved impossible.

`agda/ClosureCoherentContextAdmissionRegression.agda` embeds this coherent change under three alternating ancestors, with two-piece siblings. The resulting tree has seven pieces and depth four.

It checks complete compatible admission and retention of the actual recursively constructed equivalence. A constructor-level detector, including every intervening attachment face, observes the original hole's nontrivial circle loop. The admitted contextual equivalence cannot collapse that loop.

## Verification

Fresh final-source command:

`agda --ignore-interfaces --transliterate -i research/voevodsky/agda -i C:/Users/andrey/tools/cubical-agda/cubical-0.9 research/voevodsky/agda/ClosureCoherentContextAdmissionRegression.agda`

Exit 0, approximately 55 seconds. The closure includes both new regressions and all three new theorem/helper modules, each using `--safe --cubical --guardedness`, without holes or postulates.

An intermediate detector generalized over already specialized Unit indices elicited Cubical Agda's unsupported-indexed-match warning. It was replaced by a constructor-level detector for the regression's explicit context; the final fresh check has no such warning. The general contextual lifting theorem remains recursive over arbitrary labels and contexts.

This check does not rerun the separate arbitrary-root or selected-higher regression closures; their prior verification records remain separate.

## Remaining gate

This closes contextual closure for **coherent** comparisons. It does not automatically turn an unpointed `Admitted` edge into that stronger input.

To apply it to every previously admitted native root rotation, construct the two port witnesses and both higher port coherences for the chosen native normalization path. The word append induction currently retains first-endpoint coherence; the full root-rotation port package still needs to be supplied.

A separately implemented strict contextual map must also be compared with the actual `LiftSpan` map, including its attachment-path unit corrections. Neither identification is silently assumed here.
