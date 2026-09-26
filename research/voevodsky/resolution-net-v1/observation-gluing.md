# Joint observation is witnessed compatibility, not temporal advancement

Fresh safe Cubical Agda check passed for `agda/ResolutionNetObservationGluing.agda` with --ignore-interfaces. Log: results/agda-observation-gluing.log. This is a new module, not covered by the older whole-prototype audit receipt.

## Construction

Two probes p:L→X and q:R→X have an overlap support K with access maps into L and R. For each overlap occurrence, retain the actual equality witness relating its two images in X.

The joint support is a homotopy pushout, explicitly constructed as a higher inductive type with left/right points and overlap paths. Its probe into X retains those paths.

Two local observations glue precisely when supplied with dependent paths across each overlap. The construction preserves BOTH local observations and the chosen overlap witnesses. Every joint observation reconstructs from its two local restrictions and its overlap action.

This proves gluing for the constructed joint support. It is NOT a blanket descent theorem for arbitrary ambient subsets, nor a claim that every pair of positive-support observations is compatible. Higher overlap requirements for more elaborate covers have not been proved here.

## Checked obstruction

Take two point probes into the double cover. Each independently admits a Bool observation. Join their supports using two comparisons: one reflexive, one traversing the nontrivial loop.

The reflexive comparison requires the local values to agree. The loop comparison flips the value and requires the right value to be the opposite of the left. No pair of Bool values satisfies both. Agda checks that there is NO coherent joint observation, even though each point supports observations.

Thus positive local support is not additive evidence for a global observer. Compatibility is mathematical content, not an implementation detail. The structure with these constraints still exists; what fails to exist is a section meeting all constraints simultaneously.

## Foundational interpretation

No clock or reduction relation appears. Joint observation is formed by mathematical compatibility and gluing, not by moving one local state into another. The two local values are not secretly global assignments; their possibility does not imply simultaneous global realization.

This gives a direction-free composition mechanism for the observation proposal. It does not establish an ontology of physics, a geometric area measure, probability, physical causality, or identification of all conventional execution with observation. It is a checked model of witnessed access and compatibility.
