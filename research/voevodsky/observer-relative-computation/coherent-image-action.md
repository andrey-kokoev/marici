# Higher-valued factors induce coherent native comparison actions

Fresh safe Cubical Agda --ignore-interfaces check passed for `agda/ObserverCoherentImageAction.agda`; retained output: `results/agda-coherent-image-action.log`. The previous15-module audit predates this new file and is not a current receipt for it.

## General result, without a set-valued target assumption

For an admissible image, projection to the output induces equivalences on identity types because membership is propositional. The new module proves that the inverse path lift preserves identity and composition. It does not merely assert that a lift exists.

Given ANY witnessed image factor from f to g, define its actual output representative at x as the visible projection of post(arrive_f(x)). Its action on collisions f(x)=f(y) is obtained by the coherent image-path lift followed by the actual postprocessor.

Agda checks:

- identity comparisons map to identity comparisons;
- composition of comparisons is respected;
- every SPECIFIED base triangle induces a triangle of observed comparisons;
- an explicit retained comparison relates each actual output representative to the named output g(x).

No set assumption on the output is used. Consequently this supplies necessary coherent structure in a setting where the previous set-valued existence/uniqueness theorem does not automatically apply.

## Exact scope

The action laws are stated at the factor's native output representatives. The module does NOT silently identify those representatives with g(x). Their connecting equality is output-comparison. To obtain laws for the earlier named-endpoint collision action, one must transport/conjugate along those comparisons and account for their coherence. That is the next leaf.

These are necessary properties derived from an existing factor. They do not show that every proposed identity/composition-preserving action reconstructs a factor, nor prove completeness of any finite list of higher coherence conditions. Specified triangles are respected; arbitrary cycles are not asserted fillable.

Thus the earlier non-retainable loop assignment is not evidence that comparison direction is temporal. Its problem is incompatibility with an actual coherent action. The present result has no clock, geometric measure or physical-record assumption.
