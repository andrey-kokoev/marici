# A finer reversible source state, without filled seed faces

## Constructive result

The previous port gate showed that an arrival-port quotient cannot carry a distinguishing reversible full response. We now construct a finer reversible state directly from the ALREADY DECLARED free geometric realization of the seed, with no fitted matrices or numerical amplitudes.

Fix the base vertex A. At vertex v use

    State(v) = paths from node(A) to node(v)

in `SeedTetrahedronBridge.Realization`. A primitive occurrence e acts by

    advance(e,p)=p followed by edge(e).

Right concatenation with a geometric path is an equivalence, using concatenation with its reversed path as inverse. The existing Cubical `compPathrEquiv` supplies the equivalence and inverse laws.

This construction is canonical relative to the chosen base and the existing free geometric interpretation. It is not a claim that the bare directed graph selected a physical carrier, that an inverse is an executable seed traversal, or that this carrier has a finite-dimensional numerical realization.

## Both seed discrepancies survive as current effects

The existing `SeedFirstReturnActions.Effects` interpreter is instantiated with this State and these actual edge actions.

For the forward alternatives at initial state refl:

    AB       -> edge(AB),
    AD DB    -> edge(AD) followed by edge(DB),

up to the proved path unit laws. The existing `SeedFaceObstruction` distinguishes them in the free realization.

For the return alternatives, take the actual based state edge(AB) at B:

    BA       -> edge(AB) followed by edge(BA),
    BC CA    -> edge(AB) followed by edge(BC) followed by edge(CA).

A mathematical Boolean family that flips only across the independent BA occurrence separates BA from BC CA. Cancellation of their common AB prefix proves that these two current based-path states are unequal.

That family is a proof separator, not a chosen physical detector or a numerical assignment defining the state update. The update was already path concatenation.

The same separator proves

    edge(BA) != reverse(edge(AB)).

Thus reversible geometric action does not identify the separately supplied BA occurrence with the inverse of AB. Geometric inverses belong to the interpretation; the original directed occurrence alphabet remains unchanged.

## Why this avoids the previous obstruction

The new module instantiates the previous injective-action gate and proves that this full response does NOT factor through the source/final-occurrence quotient. That is expected: its current state retains distinctions deliberately omitted by the arrival observer.

No face equating the forward or return alternatives is required. The construction operates on each supplied path and preserves unequal outcomes rather than trying to fill their difference with an equality.

This is the positive counterpart of the earlier filled-source failure: free geometric paths support reversible transport even though specific parallel-path faces are absent.

## Actual native comparison boundary

For a current geometric state p at source(e), form the complete package

    at(source(e),p).

The actual path-concatenation equivalence gives a native `BoundaryGeneratedQuestions.Filler` from that package to

    at(target(e),advance(e,p)).

The marked-value witness is reflexivity because the target is the computed result. This filler is an equivalence between the ACTUAL boundary state types, with its actual point attachment. It is not an equality between AB and AD DB, nor an identification of the two return histories.

This distinction matters: the obstruction to filling a particular parallel-path equality does not prohibit a native operation between changing pointed packages.

## Source-only retained execution of arbitrary supplied words

The module then reuses `RetainedTransportResolution.Extension`, explicitly as the previously declared extension rather than silently altering the original Resolve signature.

For any initial vertex and based state:

1. The seed family contains only that initial complete package.
2. Every primitive step computes its actual target through the edge equivalence.
3. The output remembers the complete comparison evidence and its exact input packet.
4. A typed view exposes its current State(v) value for the next step without unwrapping or erasing its history.
5. `TransportOnly` certifies one seed and unary transports throughout.
6. Induction on an arbitrary supplied endpoint-typed seed word proves that its compiled current value equals the existing effect interpreter.
7. A separate retained field stores the original directed word verbatim.

The forward and return discrepancy proofs are transported to the actual compiled outputs. Thus this is not merely a proposed interface whose mathematical state transition has not been connected to a native execution constructor.

No schedule is inferred: the compiler accepts an explicitly supplied typed word. Its one-seed guarantee is about construction ancestry, not a claim of zero preparation or execution cost.

## Source interpretation and retention boundaries

The based state lives in the free geometric realization, where inverses and homotopies of paths are available. The original source also has directed occurrence histories. These are different objects.

The new theorem does not claim universal injectivity of the map from all raw directed histories into geometric states. It retains the directed word separately and proves the concrete seam distinctions needed here. It also proves that the state is strictly finer than the tested arrival-port response in the relevant sense.

There is no filled tetrahedron, equality of unequal seam effects, arbitrary matrix realization, phase selection, coefficient scale, or new energy budget in this construction.

## Consequence for the rung binding

A source-native reversible response carrier is now available in the declared geometric interpretation. The open gate is no longer "find any reversible action that distinguishes both seam legs".

What remains is to bind this actual carrier and operation to the intended horizontal constructor and observation:

- specify whether and how the promoted endpoint/table fields are built from these retained execution packets;
- specify the intended reader on their geometric state and retained provenance;
- if matching the137-row matrix fixture, provide a response interpretation respecting the path action and its observation, rather than identifying dimensions or borrowing nonzero coefficients;
- preserve the distinction between the original Resolve calculus and the explicitly reused unary transport extension.

The construction does NOT yet supply a scalar mixed response, its nonvanishing, physical calibration, or an identification with T9/J4. Distinct forward and return effects alone do not guarantee that a particular scalar mixed reader detects them.

## Verification

    pwsh -NoProfile -File research/nima/checkers/check_cubical_agda.ps1 -Module SeedGeometricResponseState -Fresh

Fresh safe Cubical/guardedness closure passed with ignored interfaces and stable inputs. It checks the actual source geometry, reversible edge actions, both seam discrepancies, BA/inverse-AB separation, failure of full-response descent to ports, native pointed fillers, single-seed retained compilation, exact effect agreement, and raw-route retention.

Artifact: `results/agda-SeedGeometricResponseState.json`.

No postulates or unresolved holes were added. Existing primitive data and update implementations were not modified. No physical selection or publication is claimed.
