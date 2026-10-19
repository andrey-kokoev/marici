# A sharp compiler conjecture: routing and phase alone do not suffice

Net: `research/conjecture_net/contracts/routing-only-projector-control-conjecture.v1.json`.
Checker: `research/voevodsky/checkers/check_routing_only_projector_control.py`.
Receipt: `research/voevodsky/results/routing-only-projector-control-obstruction-v1.json`.
Run: `python research/voevodsky/checkers/check_routing_only_projector_control.py`.

## Frozen conjecture

For each actual native scalar v in the fixed seven-qubit computational encoding, a finite circuit consisting only of matter permutations, diagonal matter phases and matter-label-conditioned record/work unitaries implements

    C_Pi=(I-Pi) tensor I+Pi tensor X, Pi=vv†,

on every input, with clean work ancillas. No matter amplitude mixing, matter-basis oracle, measurement or record-controlled matter operation is permitted. Arbitrary gate angles and arbitrary circuit depth ARE permitted. This is a testable restricted compiler hypothesis, not a characterization of every operation available from native geometry.

## Class-wide invariant (written proof)

Each permitted operation preserves the property: an input with one definite matter label has exactly one definite matter label at output, even when its record/work state changes. More generally every finite word has the block-monomial form

    sum_j |sigma(j)><j| tensor V_j,

where sigma is a permutation and each V_j is unitary on record/work. For composition, the permutation becomes tau o sigma and the blocks become W_(sigma(j)) V_j. Diagonal matter phases are scalar factors in those blocks. This proves closure by induction for arbitrary finite depth.

Independent clean work ancillas do not weaken this invariant. Before or after their uncomputation, the matter factor remains the single label sigma(j). Thus every output from a definite matter-label input has support on exactly one matter coordinate. This is a coherent unitary statement, not a sampling or dimension-count argument.

## Source-bound falsifier

Prepare the computational input |0>_matter tensor |0>_record, NOT the prepared scalar v. The target gives

    (e0-v conjugate(v0)) tensor |0> + v conjugate(v0) tensor |1>.

In all four source cases, v0=sqrt(2)/10, |v0|²=1/50, and there is a nonzero vj with j!=0. Therefore the output has both matter label 0 (record-0 amplitude 49/50) and matter label j (record-1 amplitude vj conjugate(v0)). A routing-only circuit cannot produce that output.

The total matter probability outside label 0 is

    2 |v0|²(1-|v0|²)=49/1250.

The label-0 probability is 1201/1250. Consequently for any normalized routing-only output, its squared overlap with the target output is at most 1201/1250. The pure-state trace distance is at least sqrt(49/1250), about 0.198. This is a positive approximation obstruction, not merely failure of exact equality. Work ancillas are compared under the frozen clean-return requirement.

The checker reconstructs all four native vectors, verifies the exact two-label witnesses and probabilities, and checks the controlled flip's unitarity through Pi²=Pi and X²=I. A computational coordinate projector is a positive control: its controlled flip belongs to the allowed class. Thus the obstruction concerns the coherent source projector, not all controlled records.

## Verdict and consequences

Proposed reject-attempt outcome: -+ for this frozen compiler conjecture. This note supplies a class-wide mathematical obstruction and exact source checks; it does not independently admit a shared graph outcome.

The prior sorter uses precisely the excluded resource: coherent matter amplitude mixing. Routing, arbitrary phase precision, longer words and extra record-only clean workspace cannot substitute for it. This is a genuine resource distinction, not a physical experiment.

It does NOT prove that coherent amplitude mixing is unavailable physically, uniquely select the frozen Hamiltonian, prohibit record-controlled matter gates, or refute an alternative encoding. Those would change the scope and require separate conjectures. Experiments and calibration remain parked.
