# Native three-leaf rotations under arbitrary finite contexts

## Proved

`agda/ClosureNativeLeafContextAdmission.agda` supplies both external port witnesses and their higher normalization coherence for the existing native three-leaf reassociator.

It retains the actual `Raw.reassociation` equivalence and the normalization square from `ClosureGeneralRotationAdmission.ThreeLeaf`. No attachment equivalence, truncation, or caller-supplied port coherence is required.

The resulting complete `Coherent` value feeds the previously checked contextual lifting theorem. Consequently, a native three-leaf rotation is admitted beneath arbitrary finite one-hole contexts, with arbitrary finite siblings.

## Endpoint coherence

The raw reassociator preserves its external ports judgmentally, so the port witnesses are reflexive. The higher cells are not simply asserted reflexive.

The proof explicitly contracts the selected normalization comparison at each external vertex. It also contracts the unit composites in the source and target normalization-port witnesses. A square then relates those prescribed witnesses along the actual normalization path.

These are contractions of particular unit-generated paths. They do not assert that arbitrary realization loops or independently supplied normalization witnesses are trivial.

## Strict contextual regression

`agda/ClosureNativeLeafContextAdmissionRegression.agda` places the rotation under three alternating ancestors, with two-piece siblings. The trees contain nine circle-valued pieces and have depth five. Their Unit-to-circle attachment maps are proved noninvertible.

The regression implements a separate strict contextual map: it applies the raw reassociator at the hole and sends each surrounding attachment path directly to its counterpart.

Constructor-level homotopies compare the recursively lifted map with this strict implementation at all three ancestors. The attachment clauses contract `LiftSpan`'s right-unit padding; the vertex clauses alone would not suffice.

Admission is transferred to the strict map itself. The regression checks its full compatible comparison, admission of its certified inverse, a closed forward/inverse type route, and identity residual transport.

A detector observes a nontrivial loop from the rotating subtree after the strict contextual map. Thus this concrete native contextual rotation cannot collapse that loop.

## Verification

Fresh final-source command:

`agda --ignore-interfaces --transliterate -i research/voevodsky/agda -i C:/Users/andrey/tools/cubical-agda/cubical-0.9 research/voevodsky/agda/ClosureNativeLeafContextAdmissionRegression.agda`

Exit 0 in approximately one minute, with no warnings. Both new modules use `--safe --cubical --guardedness`, without holes or postulates.

This closure rechecks the contextual lifting, port propagation, three-leaf admission, and imported regression dependencies. It does not rerun the separate arbitrary-three-subtree or selected-higher regression closures.

## Subsequent unrestricted result

The rotating hole contains three leaves, not three arbitrary subtrees. The enclosing context and siblings are unrestricted within the finite nonempty chain model.

The unrestricted gate is now closed separately by `ClosureNativeSubtreeContextAdmission`: paired append induction, transfer to arbitrary subtree ports, and dependent word-index coherence provide native rotations under arbitrary finite contexts. See [the construction and fresh ten-piece regression](closure-native-subtree-context-admission.md). Its newly constructed normalization square is not asserted equal to the selected square retained by the three-leaf theorem here.

The strict contextual-map identification above is checked for the explicit three-ancestor regression. A generic identification with independently implemented strict contextual maps is not claimed.
