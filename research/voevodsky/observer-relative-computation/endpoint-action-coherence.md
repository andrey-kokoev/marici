# Changing output representatives preserves coherent comparison action

Fresh safe Cubical Agda --ignore-interfaces check passed for `agda/ObserverEndpointAction.agda`; log: `results/agda-endpoint-action.log`. The older15-module audit predates this addition.

The factor's native outputs and the named outputs g(x) are related by retained source-arrival comparisons. The new module proves general path-conjugation laws: conjugating an identity remains an identity, and the intermediate representative comparisons cancel coherently under composition.

Applying those laws to the checked native image action gives identity and composition laws at the actual named endpoints g(x), for arbitrary higher-valued target types. No set assumption or identification of all equality witnesses is used.

Crucially, `earlier-agrees` relates this action pointwise to the ORIGINAL `Criterion.necessary` collision map from the set-descent development. It uses congruence over path composition, not an unproved assertion that the formulas are interchangeable. Consequently `earlier-unit` and `earlier-compose` establish the two laws for that original map itself.

Thus the earlier loop-on-identity counterexample is an instance of a general coherence constraint, not an accident of chosen representatives. Nontrivial arrival witnesses are retained and canceled through proved path laws; they are not assumed reflexive.

Scope: these remain necessary laws derived from an existing factor. Neither unit/composition alone nor this representative-change proof reconstructs a factor from an arbitrary comparison assignment. We have not proved completeness of a finite higher coherence interface, physical causality, or temporal execution direction.

Next continue the existing higher-descent-sufficiency branch. Seek a bounded positive reconstruction theorem (for example with a specified truncation level of the target and exactly stated coherence), rather than claiming the arbitrary higher-valued case follows from the set theorem. Keep source witness selection distinct from coherent elimination of merely inhabited fibres.
