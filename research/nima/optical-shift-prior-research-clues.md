# Prior clues beyond the fixed-marker involution obstruction

## Question and disposition

Which prior constructions admit repeated nonreturning actions, rather than only the fixed marker flip excluded by `interval-marker-involution-gate.md`?

The strongest inspected implementation clue is Aspect's existing two-mode optical mesh compiler; the strongest independent process source is Aspect's delayed cavity plant. Cyclic-permutation packets supply a separate finite-order algebraic example. None of the inspected sources supplies the interval encoding, guarded action dictionary and physical causal interpretation together.

This is a bounded source search, not execution of the imported checkers or a new bridge construction. The source files below were read; only the initial cyclic-shift construction was needed from Kitaev's longer packet. SCC classification for a future test remains forward realization and operation compatibility before readout interpretation.

## 1. Existing mesh compiler exposes a richer control library

`research/aspect/comparison-loop-optical-mesh.md` lowers connected 20-mode routes into two-mode real Givens rotations and terminal phases. Its emitted instructions retain mode pairs, rotation coefficients, arm, phase and reset labels. Hardware calibration is explicitly separate.

Inspection of `research/aspect/checkers/check_comparison_loop_optical_mesh.py` finds a dimension-parameterized `decompose(u)` routine performing adjacent-row Givens elimination and reconstructing the supplied matrix. It uses floating-point arithmetic; the published route check uses Frobenius tolerance 1e-10, not an exact symbolic proof.

Important distinction: its published target routes are Householder matrices, themselves involutions. Reusing one whole Householder as an interval shift would reproduce the old obstruction. The reusable clue is the underlying library of tunable two-mode rotations and their ordered products, not those particular compiled routes. Such products need not square to identity. No interval shift was found already compiled here.

This is an implementation route for a separately justified finite optical model, not a mechanism selecting the interval model from optics. Supplying a target shift matrix to a compiler would establish simulation capability only. The source's status is `compiled_not_programmed` / `physical_status: not_run`.

## 2. An independently specified repeated physical process exists

`research/aspect/reciprocal-lossy-cavity-plant.md` supplies ordered mirror, propagation, delay and loss operations before writing a state-space recurrence. Its round-trip parameter T is a declared physical delay; sample k indexes that actual stroboscopic process, not an arbitrarily renamed interval coordinate.

The packet retains a four-port orthogonal dilation including the unused exterior and environment inputs. The compressed recurrence is generally not unitary. Repeated cavity round trips therefore provide a source of repeated actions independent of the desired interval grammar, but a compressed return is not an authorized inverse. Any reverse claim must name access/control over all required ports and their temporal slices. A controller and interval dictionary remain absent.

This is the better source-first candidate if the aim is physical derivation rather than programmable simulation. It does not yet justify identifying its round-trip index, stored amplitude or port coordinates with either interval endpoint.

## 3. Cyclic permutations avoid order two, not all periodicity

`research/aspect/bargmann-cocycle-two-compiler-gate.md` constructs a three-copy cyclic shift from two whole-copy transpositions. `research/kitaev/a-four-copy-cyclic-shift-measures-the-associator-loop-exactly.md` constructs a four-copy shift from three swaps. Their ordered products have longer cycles even though individual swaps are involutions.

Both explicitly distinguish a circuit identity from an admitted controlled-permutation implementation. A shift of copy slots also is not an endpoint shift. Moreover a finite cyclic register wraps around: if its action has period N, a faithful intertwiner cannot represent a legal interval execution of N repeated shifts whose source endpoints differ. A bounded encoding must declare its no-wrap domain or retain the boundary transition; it cannot silently totalize a partial shift by wrapping.

## 4. Existing controls constrain the encoding and resource claim

`research/aspect/interaction-net-executable-context-obstruction.md` already constructs range-limited optical mode-sorter readouts for integer coordinates. Faithfulness holds on a fixed declared truncation, while two coordinates beyond the range saturate to the same record. Increasing the apparatus with each cutoff does not establish one fixed faithful instrument on the unbounded source.

`research/aspect/minimal-two-path-interferometer.md` supplies a physically typed phase/splitter library and exhibits their noncommutativity. This further shows that the old fixed-flip test was not a test of Aspect's entire optical library.

`research/aspect/controlled-clifford-phase-interferometer.md` shows that identical conjugation actions can conceal a phase exposed by a coherent reference. An encoding must freeze whether that reference is admitted before choosing its operational equivalences; matching isolated density-state channels need not preserve controlled-route observations.

## Selection consequence

Keep two goals separate:

- **Source-first physical bridge:** inspect the declared cavity's actual transition and ports for a justified interval interpretation. Its existing process law and physical delay are usable source data; its reverse authority is not established.
- **Finite simulator:** reuse the mesh library after an explicit bounded encoding and domain are justified. Test true inverse domains, repeated shifts, boundary/no-wrap behavior, complete decoded records, and route history separately. Do not infer physical geometry from compilation.

The fixed-marker no-go remains intact, but it is not a reason to stop examining Aspect's noninvolutive control families. No new physical conjecture is closed, and no new hardware experiment is claimed by this review.
