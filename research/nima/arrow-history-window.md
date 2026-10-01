# Deconstructed arrows with a retained-history window

## Construction

The proposed split is now implemented as a finite typed view:

    active arrow = (occurrence ID, displayed source, displayed target),
    history window = (retained root ID, ordered parent path, original occurrence ID),
    transport = whether this row is currently presented in reversed orientation.

This is not the literal real and imaginary parts of a complex number. The active component is a presentation of arrows; the window is a reference into the full retained construction. A phase reading can be recovered through that window, but does not replace it.

Inputs are the retained half-turn packets from `paw-half-turn-promotion.md` and the group/reversed-unpack pattern from `table-fibration.md`. This Python checker is a finite adapter of those ideas, not a new Agda proof identifying the native table constructors with spatial rotations.

## Arity four deconstructs without erasing its origin

Take two independently executed positive half-turn pairs and promote their composition:

    root = ((r_1,r_2),(r_3,r_4)).

All four r_i have physical angle +pi but distinct occurrence IDs. The root has physical angle 4pi, rotor lift +1, and retained promotion depth two.

Deconstruction produces four arity-one rows, each carrying a window:

| Arrow | Parent path from the root |
|---|---|
| r_1 | (0,0) |
| r_2 | (0,1) |
| r_3 | (1,0) |
| r_4 | (1,1) |

Following a window recovers both the primitive event and its exact ancestry. The root label remains present even if the displayed arrows are regrouped. An empty identity has no arrow rows, but still retains its own root label: an empty visible table does not erase its identity.

## What the next presentation cycle does

Group the active arrows by displayed source, then unpack with the source and target reversed. Each row's reversal flag is toggled at the same time. The history window still points to the original event; resolving its currently presented orientation swaps the event endpoints and negates its half-turn direction.

Do that grouping/reversal step twice:

    original rows
      -> source families
      -> transposed rows
      -> source families of transposed rows
      -> original rows.

Grouping may change display order. The stored paths and occurrence IDs recover the original order, so the final rows equal the initial rows after canonical reordering. Reassembly recovers the same retained root, including the same original ordered half-turn events.

Transposing rows is a presentation operation, not an execution of reverse physical turns. In particular, the transposed rows in their old event order need not form a composable path. The adapter refuses path reassembly while rows are reversed. To execute an inverse path one would need both reversed event order and reversed events, plus new occurrence records for any new execution.

## The window moves with the arrow

Validation requires:

- the window root equals the presentation's retained root;
- the parent path resolves to a primitive leaf of that root;
- the primitive occurrence matches both the arrow and its window;
- displayed endpoints agree with the event and its transported reversal flag;
- the whole presentation contains every expected occurrence exactly once;
- cached histories agree with histories reconstructed through parents.

Thus simply swapping displayed endpoints without transporting the window orientation is rejected. So are missing or duplicated rows, forged paths, forged occurrences, and swapping in a window from another identical-looking completed turn.

A +pi and a -pi half-turn have the same vector endpoints, but their windows resolve to opposite signed directions. This is a concrete case where the active endpoint view alone cannot determine the next replay operation.

## Closure remains distinct from history

The following all have rotor reading +1 and zero ordinary imaginary rotor coefficient:

- the empty identity;
- a +pi turn followed by a -pi turn;
- four positive pi turns.

Their retained variations are respectively 0, 2pi and 4pi, and their signed angles are 0, 0 and 4pi. The checker reconstructs these distinctions after three complete presentation cycles. Two separate four-turn constructions also remain distinct despite agreeing on all those coarse readings.

The new presentation-operation log grows even when the rows return. It is not erased by the row isomorphism and is kept separate from physical turn history. The retained packet ledger itself is unchanged by these view operations: they generate neither additional half-turn events nor new spatial dimensions.

## Depth and verification

The original packet ancestry remains bounded by the earlier maximum depth three. The test uses depth-two arity-four packets and three finite presentation cycles. It does not reset physical ancestry to zero by calling the current view arity one, discard parents, or claim indefinite bounded-memory replay.

    python research/nima/checkers/check_arrow_history_window.py

Fresh checks pass for deconstruction, parent-path lookup, full occurrence coverage, three four-stage presentation cycles on four different roots, phase/history recovery, reassembly, independent occurrence identities, opposite-direction ambiguity and six hostile controls.

Artifact: `results/arrow-history-window.json`.

## What is now available

The next operation can act on a small arrow presentation while obtaining parent identity, direction and accumulated history through a typed window. The history is accessible without being mistaken for an imaginary scalar or re-counted as a fresh independent operand.

A physical next-cycle update or a new identity-promotion rule is still a separate operation to supply. This result establishes the interface and its transport law, not a proton model, a physical readout, or growth caused by regrouping alone.
