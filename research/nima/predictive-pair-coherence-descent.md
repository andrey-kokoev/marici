# Native normalization coherence descends to predictive phase state

## Question and answer

Can an existing coherence condition be evaluated from the 60-state predictive
quotient rather than the full retained word?

**Yes for transported normalization coordinates.** A finite realization of the
existing native condition descends to the quotient. A faithful fixed coordinate
assignment indexed only by the 20 joint endpoints is obstructed by nontrivial
loop action. This is not yet a native compiler instantiation or physical
proton/electron admission law.

## Existing rule inspected

`agda/DependentNormalizationCoherence.agda` defines a presentation with an
expression and a coordinate equivalence to a common normalized carrier. Its
`CoherentMap P R` requires, for every input x, an output y with

    coordinates_R(y) = coordinates_P(x).

For a supplied action U this becomes

    C_R composed with U = C_P.

Its `advance` constructor transports coordinates by the inverse of a supplied
equivalence. `NativeNormalizationRouteCompiler` compiles supplied coherent maps.
`ThreeRecordTriangleRegression` demonstrates both a coherent direct link and
rejection of a conflicting link, on its distinct Boolean presentation example.

These formal definitions provide an existing law to test. They do not themselves
bind the original proton/electron arrows to that Boolean example, or select a
physical source-admission predicate. The earlier missing-binding audit remains
valid; we do not identify its AC map with the actual CA primitive.

## Finite realization using actual source actions

Use the entire reachable orbit of labelled centroid frames as a finite carrier
X. It has 60 elements. Each actual source generator acts as a permutation U_a
of X, computed using the existing native mode-step function on every frame.

For each predictive state s, compose the source actions along its retained
witness to get W_s. Define

    C_s = inverse(W_s).

This is precisely the finite permutation form of transported coordinates, not
a fitted scalar phase or a newly chosen update law.

Crucially, using one witness does not by itself prove descent from histories.
The checker verifies:

1. Each initial one-arrow history has exactly its state's W_s.
2. For every admitted transition s --a--> t, U_a W_s = W_t as permutations
   on **all 60 frames**, not just the currently prepared frame.
3. The state graph is closed, as freshly checked by the phase bridge.

Induction then shows that every valid nonempty history projecting to s has the
same full action W_s and the same C_s. Thus no unrecorded choice of witness
remains in this finite coordinate assignment. The abstract native law is
realized here by exact finite permutations; no Agda carrier or compiler binding
has been constructed in this change.

## Coherence target gate

There are three predictive states above each of the 20 joint endpoints. For
every one of the 150 admitted transitions, test all three candidate target
presentations at the required endpoint against

    C_candidate U_a = C_source.

Exactly the actual successor passes:

- **150 coherent candidate targets**;
- **300 incoherent candidate targets**.

Both existing rung transports preserve the projected state and hence this
coordinate equation. Prepending a complete proton ABC loop gives a distinct
history but leaves its full action and normalization coordinates unchanged;
this is tested for all 60 witnesses. Provenance remains distinct in the
existing quotient-contract checker.

This gate detects a wrong target presentation. It does **not** reject any of
the currently endpoint-admitted operations with its actual transported target.
Transporting coordinates is a coherence construction, not a new dynamical
selection principle.

## Endpoint-only obstruction

The actual proton word

    AB, BA, AB, BC, CA

returns to joint endpoint (A,E) but has a nonidentity action on X. The electron
word EA, AB, BC, CD, DE returns to that endpoint with identity action.
The receipt records a moved frame witnessing the nonidentity permutation.

If a single faithful coordinate equivalence C_(A,E) served this endpoint and
all those operations were coherent, the closed proton route would imply

    C_(A,E) W_loop = C_(A,E).

Injectivity forces W_loop = identity, contradicting the witness. Therefore
endpoint labels alone cannot index fixed faithful presentations admitting all
these actions. The three phase states over each endpoint retain the needed
coordinate distinction.

This obstruction does not apply to a deliberately nonfaithful scalar reading,
to a changed operation set, or to presentations carrying additional phase data.
Nor does it forbid a different physical model.

## What this resolves and what remains

The 60-state quotient is sufficient not just for the selected future scalar
readings, but also for the transported-coordinate coherence condition of this
finite source-action realization. No extra history field is needed for that
condition.

Still missing is an independently supplied physical restriction: for example,
which fixed comparison target, conservation condition or interaction request
must be respected rather than freely transported. Such a restriction would
need its own typed binding and descent test. Generic coordinate transport
cannot supply that selection, a physical clock or an energy calibration.

## Verification

    python research/nima/checkers/check_predictive_pair_coherence_descent.py

Fresh result: **1114 exact checks pass**, after rebuilding the phase and endpoint
bridges. Receipt: `results/predictive-pair-coherence-descent.json`.
It includes the complete finite frame carrier, presentations, coordinate and
request permutations, nontrivial-loop witness and input hashes.

The Agda sources were inspected and hashed, not modified or freshly compiled
by this checker. This result is exact Python verification of a finite
realization of their equation, not a new formal theorem.
