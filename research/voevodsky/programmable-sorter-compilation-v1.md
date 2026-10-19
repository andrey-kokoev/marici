# Exact abstract gate compilation of the first native scalar sorter

Scope: mathematical quantum-circuit compilation only. Experiments and calibration remain parked.
Checker: `research/voevodsky/checkers/check_programmable_sorter_compilation.py`.
Receipt/circuit: `research/voevodsky/results/programmable-sorter-compilation-v1.json`.
Run: `uv run research/voevodsky/checkers/check_programmable_sorter_compilation.py`.

## Frozen input and gate set

Use chirality +1, doublet option 0 from the actual native adapter. Reconstruct v=J(1,0,0,1)/sqrt(2), pad to 128 matter states, and retain the previous Householder U=I-ww†/alpha, w=e0-v, alpha=1-v0. This case has exactly 50 nonzero real amplitudes sqrt(2)/10; that sparsity is checked rather than assumed from dimension.

The abstract gate set is six-controlled X, six-controlled arbitrary real one-qubit rotations (both positive and negative control literals allowed), and a computational-state phase flip. These are specified unitary macros, not elementary fault-tolerant hardware gates. Lowering them further to a finite universal gate alphabet requires a separate synthesis/error budget. No physical native capability or calibration is claimed.

## Exact two-level elimination

For each nonzero w_j, j>0, combine current pivot a at index 0 and b=w_j by

    G_j=[[a/r,b/r],[-b/r,a/r]], r=sqrt(a²+b²)>0.

It maps (a,b) to (r,0). Applying the recorded sequence A to w gives sqrt(2 alpha)e0, so

    U=A† Z_0 A,
    Z_0=I-2|0><0|.

The finite sequence exactly implements the source-bound reflection, including its action on the full orthogonal complement, not just on the prepared scalar input. Vacuum and padding remain fixed because none of the elimination pairs involves them and Z_0 fixes them.

To implement G_j on seven qubits, use a Gray path from 0 to j by flipping its set bits in ascending order. Move index 0 to the penultimate path vertex with adjacent transposition gates, apply the one-bit-adjacent rotation on the final edge, and undo the transpositions in reverse order. Each adjacent transposition or rotation has six specified control bits and one target bit. The checker exhausts all 128 indices for each lowering, including spectators. This detects residual permutations rather than validating only the desired pair.

Emit the full chronological sorter circuit as lowered A, Z_0, reversed inverse lowered A. Reversible flag computation from the previous interface follows this sorter; no matter measurement or complement deletion is introduced. Although Gray routing can temporarily traverse other states, all spectators are restored by each conjugated rotation.

## Resources and approximation

The receipt records the number of elimination rotations, lowered gates and logical controls, plus exact algebraic entries for every rotation. The compile is exact in the abstract arbitrary-angle gate set. For a unitary implementation of L gates, each approximated with operator-norm error at most delta, telescoping gives ||U_approx-U||<=L delta. This assumes unitary approximants; uncontrolled noise/leakage is not described by that bound.

For pure input states, trace-distance error is at most the resulting state-vector norm error, so every normalized effect probability differs by at most L delta. If the surrounding control uses both sorter and inverse sorter plus a record gate, add their individual norm-error budgets; the exact predicate macros also require their own implementation bound if approximated.

Constructed: a concrete source-specific abstract gate word with exact lowering and a conditional deterministic error budget. Not constructed: hardware gate compilation/calibration, a native physical 100-state encoder, K simulation, optical controlled interface or empirical rule selection. Other three native cases remain verified matrix interfaces; this circuit is not asserted to apply to their different vectors.
