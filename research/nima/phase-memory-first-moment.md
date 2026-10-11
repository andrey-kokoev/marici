# Opposite-phase first moments return through retained memory

## Experiment and admission boundary

Freshly read the prior projection-to-record exchange construction. Apply that same discarded-coordinate swap mechanism to the existing twelve-mode collective projector P, with the AB/BA contrast and cone-centroid intensity reader from the preceding experiment.

This is a conditional conservative extension of the established projector. The record bank, initialized empty, and its reuse schedule are explicitly chosen for the test. Neither a physical interaction nor this extension's unique source selection is claimed. The old source projector is not overwritten.

Let Q=I-P. The update is

    x_next=P x+Q r,
    r_next=Q x+P r.

On the natural zero-mean record sector Pr=0, it swaps the discarded contrast into the record and returns the previously stored contrast to the active carrier. An empty record reproduces the original projected active output exactly.

## Exact identities

The full block matrix [[P,Q],[Q,P]] is orthogonal and squares to identity. It preserves both the total quadratic budget and x+r. These are checked as operator identities, not inferred from a few trajectories.

The discarded subspace has dimension eleven. The implementation stores twelve coefficients constrained by sum(r)=0; no arbitrary contrast basis is needed. Only one contrast direction is excited in this experiment, but eleven are needed to recover arbitrary inputs in this twelve-mode sector. This is different from the earlier one-dimensional exterior aggregate needed merely to predict the projected interface observation.

## Two preparations

Use the existing global mode u and the interface contrast d, supported with coefficients +1 on AB and -1 on BA. Prepare x=u+d or x=u-d, with r=0. Both total budgets are 280/3 under the previous local-vector normalization.

The active intensity centers are:

| Advance | Preparation u+d | Preparation u-d |
|---|---|---|
| 0 | (1/12, 1/42,-1/42) | (1/12,-1/42, 1/42) |
| 1 | (0,0,0) | (0,0,0) |
| 2 | (1/12, 1/42,-1/42) | (1/12,-1/42, 1/42) |
| 3 | (0,0,0) | (0,0,0) |

After the first advance x=u and r=+d or -d. Active budget is 80; record budget is 40/3. After the second advance the record empties and the initial active state returns. Only three advances were executed; the period-two statement follows from the exact operator identity.

This is a genuine memory-mediated return of a phase-sensitive active readout. It is not a bound electron, asymptotic stability, or an attractive force.

## Stronger observer obstruction

At advance one the two runs have identical active intensities AND identical record intensities at every block. Their budgets, separate intensity centers and all functions of those intensities agree. Nevertheless their next active first moments differ.

Therefore even retaining the full lists of current intensities is insufficient to predict this update. The relative phase between carrier and record is operationally relevant. Replacing the records by magnitudes would not be an observation-preserving quotient for the admitted continuation.

Erasing the bank is also not cost-free: it removes budget 40/3 and prevents the return. The remaining active u is fixed by the original projector.

## Where the first moment went

Assigning the bank the same block positions is a declared diagnostic convention. The sum of separate carrier and record intensity first moments need not be conserved, despite conservation of their total norm.

For a diagonal position reader X, the coherent sum has first moment

    (x+r)^dagger X (x+r)
      = x^dagger X x + r^dagger X r + 2 Re(x^dagger X r).

At advance one, the cross first moment is (0,+20/9,-20/9) or (0,-20/9,+20/9). This is exactly the transverse distinction missing from separate intensity readouts. Because x+r is invariant under this swap, its complete coherent first moment is constant.

This conserved joint readout is not automatically physical center of mass: independently stored degrees of freedom need a specified spatial density and measurement/recombination coupling. It does show explicitly that the missing signal is in a relation between retained sectors, rather than in their scalar budgets alone.

## What this gains and what it does not

The previous projection-only experiment removed the displacement from the active readout. A prior conservative record mechanism now returns it without a fitted gain. That closes a bounded response test which had not been performed for the barycenter observer.

The result depends on retaining and reusing phase-bearing records. It does not derive why nature supplies that bank or schedule, why the mode has electric charge, or how its positions/intensities acquire a mass interpretation. The prepared sign change is not charge conjugation. No recoil trajectory, momentum conservation law, particle mass or lifetime is calculated.

## Verification

`python research/nima/checkers/check_phase_memory_first_moment.py` passes exact rational orthogonality, involution, rank, budget, phase-blind counterexample and first-moment identities. Full three-advance histories are in `results/phase-memory-first-moment.json`. Existing geometry and dynamics implementations were not changed. No new Agda proof, ledger entry or physical selection claim is made.
