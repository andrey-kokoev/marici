# Task-relative selection is not guaranteed by task declaration

## Verdict

The strong conjecture—that an independently declared operational task necessarily selects a single nonempty contextual-equivalence class—is false.

A frozen reversible-memory task has multiple implementations satisfying all of its requirements. They disagree under an already authorized continuation, without adding a probe or changing the source. A second four-state task supplies an obstruction that survives arbitrary vertexwise state-frame comparisons.

This refutes a universal **selection** guarantee, not task-relative classification into multiple classes. It does not show that no more fully specified task can determine an implementation.

## 1. Freeze a useful task, not a desired answer

`contracts/task-relative-memory-selection.v1.json` specifies a reversible one-bit route memory on the unchanged six-arrow source:

- state is the current vertex plus one Boolean;
- initialization is (A,false);
- each edge uses a fixed Boolean permutation;
- observations read the current vertex and bit at every route boundary;
- every endpoint-correct finite continuation is authorized;
- updates preserve source-swap covariance, units and composition;
- all eight configurations must be reachable.

The task does not prescribe the response of a chosen edge or loop. It excludes inert or unreachable-state countermodels. It is a declared mathematical task, not a claimed blind empirical preregistration or a task uniquely selected by WG.

## 2. Complete one-bit classification

There are 64 Boolean-permutation assignments to the six edges. Exact enumeration finds eight source-covariant assignments and four satisfying full reachability. Complete paired-state exploration separates all four contextual classes under the frozen readout.

Two explicit policies are:

- **red:** flip at AB and BA; otherwise preserve the bit;
- **green:** flip at BC and AD; otherwise preserve the bit.

Both use source-swap orbits. Both are reversible, source-covariant and compositional, and both reach every vertex/bit configuration.

After the common prefix AB;BC;CA, both read (A,true). Apply the SAME continuation AB:

    red   -> (B,false)
    green -> (B,true).

No new observation was introduced to distinguish them. Equality of the present record does not select their next update law.

## 3. Original-rule binding and formal scope

`agda/TaskRelativeMemoryCounterexample.agda` defines both closed edge-equivalence factories and proves:

- source-swap covariance;
- all-word composition through the existing effect interpreter;
- agreement of each response with the actual original-rule geometric compiler;
- compiled witnesses reaching all eight configurations for each policy;
- equal present readings and unequal readings after the common continuation;
- nonexistence of contextual equality between the two implementations.

The native geometric compiler is shared. The two policies are distinct permitted interpretations of its retained path state into the same fixed bit-memory interface. They are not claimed to be two different universal free graph realizations.

The Python census classifies all 64 policies; the Agda proof handles arbitrary words for the two displayed survivors. These evidence scopes are separate.

## 4. Do not conceal the one-bit frame caveat

The four one-bit transition systems are related by vertex-dependent bit frames. Those frames change the observed bit at intermediate vertices and therefore are not equivalences of the frozen observation task. With a different task observing only returns at A, the distinction can disappear.

This is a real task-relative obstruction, but it is not an inequivalence of unobserved dynamics. To avoid resting the conclusion solely on fixed record labels, a separately declared four-state task was tested.

## 5. Four-state strengthening: an intrinsic return-loop mismatch

`contracts/task-relative-four-state-selection.v1.json` declares a reversible writable four-state memory on the same source. Its allowed updates are cyclic shifts modulo four, constant on each swapped edge pair. The task again requires source covariance, composition and reachability of every configuration, without prescribing an edge response.

There are 64 covariant shift policies; 32 reach all sixteen configurations. Compare:

- **P:** increment by one on every edge;
- **Q:** increment by one only on BC and AD, and by zero elsewhere.

Both satisfy the task. After (AB;BC;CA) repeated twice, both read (A,2). Apply the common RETURN continuation AB;BA:

    P -> (A,0)
    Q -> (A,2).

More importantly, the entire AB;BA action on the four memory states is

    P: [2,3,0,1]   (fixed-point-free shift by two)
    Q: [0,1,2,3]   (identity).

A vertexwise action intertwiner would have to conjugate these return permutations at A. That is impossible: identity cannot be conjugated to a nonidentity permutation. The exact checker also exhausts all 24 possible frames at A and finds none.

Thus this second failure is not removable by relabelling memory states, even after relaxing the fixed-readout requirement. It is a finite exact operational countermodel; a new Agda original-rule binding for this four-state instance was NOT performed.

## Verification

    python research/strominger/checkers/check_task_relative_memory_counterexample.py
    python research/strominger/checkers/check_task_relative_four_state_selection.py

The first command reruns the one-bit census and fresh safe Cubical/guarded closure with ignored interfaces and a stable conservative 2,445-file manifest. Both negative controls fail with the intended UnequalTerms diagnostics: false contextual equality and erasure of a bit-frame change while claiming fixed-readout preservation. Cubical warnings and the known unused import warning in TypedGeneratorLayers are recorded.

The second command performs the independent four-state exact census and return-action obstruction.

Receipts:

- `results/task-relative-memory-counterexample/verification.json`
- `results/task-relative-memory-selection/census.json`
- `results/task-relative-memory-selection/four-state.json`

## What remains viable

Declaring a task can yield a well-defined family with several operational classes. It need not select one. Even reversibility, source covariance, full finite reachability and composition do not guarantee selection.

A stronger task might prescribe a counting law, authorize an additional selector, or quotient observations differently. That is additional semantic authority, not a consequence of the requirements tested here. It must be justified independently rather than chosen after seeing which policy gives the desired answer.

The useful next question is which distinctions the intended application actually requires, and which source/task law constrains the remaining response freedom. There is no universal shortcut from “the task is declared” to “its response policy is determined.”

The completed local WG theorem, original-rule compiler and existing pins remain unchanged. No physical model or empirical prediction was validated or falsified here.
