# Minimal context for the two-tour vertex observation

## Declared system

Reuse the two existing six-slot successors. The finite state is (tour alternative, current occurrence slot), giving twelve states. The observation returns the current slot's source vertex. The successor follows that same tour; switching between tours is NOT part of this system. Repeated cycling is a combinatorial model, not a derived physical schedule or clock.

`check_seed_typed_execution.py` now computes the coarsest successor-stable refinement of this observation partition. At each round, a state is classified by its current block and its successor's block. This is the standard finite predictive-equivalence refinement; no cost, metric or phase is supplied.

## Exact result

The numbers of blocks are

    4 -> 6 -> 10 -> 12.

The initial four classes are the vertex readings. One refinement records the next vertex too, identifying the six primitive directed edges but not necessarily the tour. The final partition is discrete: every (tour,slot) state has a distinct future observation sequence.

For a FIXED tour, current and next vertex already identify all six slots. Hence its smallest deterministic refinement preserving the vertex observation has six states. On the disjoint union of BOTH tours, that minimum is twelve. Any deterministic observation-preserving quotient must respect every refinement round; since the stable partition is discrete, no distinct states can be merged.

This minimality is specific to this deterministic finite system and its labelled vertex reader. It is not a minimal physical state count or a result for nondeterministic presentations.

## Finite observation window

Four consecutive vertex readings distinguish all twelve states; three distinguish only ten classes and are insufficient in the worst case. Because the slot successor is invertible, the corresponding past-window test also gives twelve classes for four readings and ten for three.

Thus an observer need not be supplied a tour label after enough history has accumulated: the actual labelled trajectory identifies both tour and slot. This is an inference from an observed execution, not a symmetry-breaking rule selecting which tour to execute. The names of vertices are part of the reader; relabelling them transports the observation history.

Past windows assume the declared cyclic successor has been followed for the requisite steps. At initialization, or under unmodelled switching between alternatives, this inference is not licensed. No pre-execution future oracle is inferred.

## Structural synthesis

The missing memory is now quantified rather than guessed. Vertex-only observation is non-Markovian for the full-support cycle; retaining sufficient occurrence/history context restores deterministic prediction. This does not require choosing another physical carrier or identifying the six-cycle with the earlier triangle half-phase.

The two-tour retained family can stay unselected until execution evidence or an independently justified preparation marking is supplied. A physical rung4 reader remains a separate calibration/admission question.

## Working observer and rung4 bridge

`check_seed_history_observer.py` now implements the observation interface over the SAME declared successor. Its initial state is the set of all twelve possibilities. The first reading filters that set without advancing time. Later readings update by

    candidates' = { next(s) | s in candidates, observation(next(s)) = reading }.

Prediction returns the SET of possible next vertices, not a guessed tour or probability. An impossible history returns the empty set. Empty, one-, two-, three- and four-reading histories give 1+4+6+10+12=33 distinct admissible window records. Three-reading startup can remain ambiguous; four readings identify the current state.

Tests follow all twelve initial states for thirteen updates each. At every step, incremental filtering equals full-history reconstruction and reconstruction from the last four readings. The actual state remains in the candidate set and its next reading is predicted. Once synchronized, the prediction is singleton. These tests do not authorize switching tours or adding observation noise.

The thirty-three records are carried through both existing rung transports. Each stores only its history and a diagnostic candidate count, not a hidden selected state or tour. At rung4 the reader recomputes candidates and predictions from decoded histories. Both diagram routes preserve these results, and every possible next vertex is checked against direct extended-history reconstruction. The numerical means used internally by transport do not define this history reader.

This is the requested history -> predictive state -> next observation bridge, with explicit startup uncertainty. It is not the independently calibrated physical rung4 observation and does not equate combinatorial updates with elapsed physical time.

## Verification

    python research/nima/checkers/check_seed_typed_execution.py

Fresh exact enumeration passes for all twelve states, refinement to stability, per-tour six-slot distinction, and both future and past minimal-window controls. Existing seed path, spectral-window, symmetry and successor checks also pass. No new native formal proof or physical evolution law is claimed.
