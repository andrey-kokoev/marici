# Admitting native rotation maps into normalization

## Status: a checked bridge, with a remaining general case

`agda/ClosureRotationAdmission.agda` introduces a certified edge interface for independently supplied maps between bracketings. It also proves admission for the actual three-piece associator when its two left attachment maps are equivalences.

This is not yet the theorem for arbitrary noninvertible attachments or arbitrary subtree rotations. In particular, the earlier Bool-to-Unit circle-producing spans do not satisfy the new positive theorem's invertibility hypotheses.

## Admission data and consequences

An `Admitted p q` contains an actual function between the two bracketed realizations and a proved square saying that normalizing after this function agrees with normalizing the source.

`matchesNormalForm` derives equality with the generated comparison. `actionEquiv` consequently proves that the supplied action is an equivalence. Neither the square nor equivalence of an arbitrary proposed map is invented by the interface.

`Presentations.pack` includes the map and its square in the compatible-presentation fiber. `agreesWithGenerated` compares the full record with the generated presentation, retaining its witness rather than just comparing functions.

## Routes of actual supplied maps

The new finite-route datatype stores admitted edges. Its semantics composes their supplied action functions, not substituted canonical maps.

`routeSquare` composes the edge witnesses. `routeNormalForm` and `compareRoutes` then compare actual composites with the normal-form endpoint comparison and with one another.

The type route is the concatenation of the univalence paths of these actual action equivalences. `closedTypeRoute` proves every admitted closed type route null-homotopic; `residualIsIdentity` proves its residual transport fixes every inhabitant.

These are type-path results. They do not trivialize internal loops in the realization or arbitrary independently supplied value-return witnesses.

## An independently proved native admission

`ThreeLeaf` uses the earlier constructor-defined `Chain.associate` and `Chain.unassociate`. It does not redefine either map as a normal-form comparison.

The hypotheses are that the two left legs of the three-piece chain are equivalences. Pushout-along-equivalence then makes the inclusion of the final piece into the left-associated realization an equivalence.

The two candidate maps into the normal realization compute identically on that final piece. Its inclusion equivalence extends this agreement to the whole source, proving `rotationSquare`. This square is a theorem derived from the span hypotheses, not an assumed compatibility field.

The inverse associator receives its square using the forward square and its already checked section law. `nativeMatchesGenerated` identifies the raw forward map with the generated comparison. `nativeEquivalenceRetained` also identifies its certified equivalence with the original reassociation equivalence.

The final piece may have arbitrary homotopy type; no set or contractibility assumption is used.

## Nontrivial regression and rejected candidate

`agda/ClosureRotationAdmissionRegression.agda` glues three copies of the circle along circle-valued identity attachments. The boundaries are nonempty higher types.

It checks:

- the native rotation's complete compatible-presentation comparison;
- null-homotopy of the actual forward/backward type route;
- identity residual action on every source value;
- preservation and nontriviality of a circle loop under the raw associator;
- impossibility of giving a constant replacement map the required admission square.

For the last test, a hypothetical square would certify the constant map as an equivalence. Its induced equivalence on path spaces would then identify the detected nontrivial source loop with reflexivity, a contradiction.

## Verification

Fresh final-source command:

`agda --ignore-interfaces --transliterate -i research/voevodsky/agda -i C:/Users/andrey/tools/cubical-agda/cubical-0.9 research/voevodsky/agda/ClosureRotationAdmissionRegression.agda`

Exit 0. Both added modules use `--safe --cubical --guardedness`, without holes or postulates. The dependency closure rechecks finite normalization and the earlier pentagon, reassociation, gluing, and dependent-boundary regressions. Existing source modules were not modified.

An incremental elaboration ambiguity in `routeNormalForm` was resolved by supplying its source and target bracket indices explicitly.

## Next obligation

The remaining normalization square for a general native rotation must account for noninvertible attachments, the recursively chosen endpoint-preservation witnesses, and word-index reassociation for variable subtrees. The admission interface and route theorem now state precisely what that proof must supply; they do not substitute for it.
