# One retained stateful interface for the shared proton requests

## Result

The geometric, spin and exchange readings now share a reusable execution
interface on the six already-bound proton ports. **3580 checks pass** across all
four generator lift-sign policies, all 53 words through depth six (including the
empty word), and both existing rung policies. A longer closed-cycle collision
is also checked.

Implementation: `checkers/retained_proton_operation.py`.
Checker: `checkers/check_retained_proton_operation.py`.
Receipt: `results/retained-proton-operation.json`.

## State and provenance are separate

An immutable `State` contains:

    (geometric predictive ID, logical spin vector,
     six exchange mismatches, sixteen conserved anchor coordinates).

An `Execution` separately retains the initial state, final state and ordered
primitive requests. Request order is not a newly allocated physical event ID.
The state interface does not reconstruct a unique history from its final value.

Each bound request updates geometry through the 60-state transition interface,
spin through its selected source-compatible lift, and mismatch through the
existing exchange recurrence. The anchor is unchanged. These are compatible
readings of one word, not an assertion that the three operations are physically
identical or coupled by a newly derived Hamiltonian.

The two proton generator signs are explicit constructor inputs. All four
combinations are checked; none is selected as physical. Electron requests are
rejected as unbound rather than assigned a silent identity exchange.

## API

- `prepare(spin, exchange)`: construct a state from a supplied logical doublet
  and the original 22 exchange coordinates at joint preparation (A,E).
- `step(state, request)`: one endpoint-admitted bound proton operation.
- `execute(initial, requests)`: ordered execution, including the empty word.
- `recover(execution)`: check the record and reverse spin/mismatch updates.
- `exchange_state(state)`: recover the full original exchange vector.
- `observe(state)`: expose the separate geometric, spin, mismatch and anchor readings.
- `retain`, `restore`, `advance_rung`: transport the complete execution interface.

Numerical inverse operations need not themselves be forward directed paths in
the original seed. Recovery retains the initial geometric attachment and the
word; it is not a source-selected physical reverse schedule.

## Rung contract

The old path rows are unchanged. A `RetainedExecution` wraps the original rung
path record with the initial preparation and lift-sign policy. Restoring the
word and replaying its operations recovers the execution exactly.

This additional wrapper is explicit: the original scalar rung aggregate never
contained arbitrary spin/exchange preparation. It must not be claimed to recover
information that was not encoded.

Both policies satisfy:

    restore(retain(execution)) = execution,
    restore(advance_rung(retain(execution), a)).final
        = step(execution.final, a).

The checker also verifies chronological composition at every split of each
tested word, spin norm preservation, exchange metric preservation, and agreement
with an independently evaluated full 22-dimensional exchange action. Foundational
source bindings and exact per-port exchange decomposition are freshly replayed.
The word census is finite; arbitrary-word composition follows from the recursive
execution definition and the per-port identities, not from claiming exhaustive
history enumeration.

Negative controls reject malformed endpoint continuations, electron exchange
requests, altered executions, foreign lift policies and an empty rung record.
Empty execution remains valid as an identity action outside that nonempty rung
adapter.

## Closed geometry does not imply an idle internal state

For every lift policy, two and four ABC traversals end at the same geometric
state and the same spin vector, while their mismatch vectors differ. Their
anchors agree. The supplied initial AB-record excitation is unchanged from the
prior model.

The consolidated interface thus preserves the key structural distinction:

    a completed geometric cycle can act nontrivially on retained internal state.

No projection silently erases that response, and no extra physical event is
counted merely because an execution is re-encoded at rung four.

## Boundary for the next comparison

A contact/mediator adapter can now be asked to preserve this actual `step` map,
not merely match endpoints or dimensions. Such a map is not yet supplied here.
Initial excitation, logical preparation, joint spin-frame choice, electron
exchange, relative-position dynamics and physical timing remain outside this
conditional interface.

## Reproduction

    OPENBLAS_NUM_THREADS=1 uv run --with sympy --with 'numpy>=2,<3' python research/nima/checkers/check_retained_proton_operation.py

The new checks are exact. The replayed older port adapter retains its separately
documented numerical comparison with the whitened fixture. No physical
calibration or new formal Agda theorem is claimed.
