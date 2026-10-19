# The relevant control question: predicting energy, not steering every mode

## Relevance correction

The original goal was a Hamiltonian connection between rung presentations. Full independent control of every mode is NOT required for that connection. Investigating separate actuators was an optional stronger problem, not a necessary next rung-descent obligation.

For the already declared family-gain protocol, a more relevant question is: what must the retained rung4 data tell us to predict the next energy?

38 exact checks answer that question. Two nonnegative energy summaries suffice. No new actuator or independent mode control is introduced.

## Intuition from the two-leg records

Each comparison is Y_j X_i. Relative to its incoming-family averages, write

    X_i=Xbar+dx_i,
    Y_j=Ybar+dy_j.

Then

    Y_j X_i=Ybar Xbar+(Ybar dx_i+dy_j Xbar)+dy_j dx_i.

There are two kinds of disagreement:

- ONE-LEG: only one factor differs from its family average in that term;
- TWO-LEG: both factors differ.

The existing gain shrinks each primitive-leg disagreement by q=1-eta. One-leg response terms shrink by q; two-leg response terms shrink by q^2. Their quadratic energies therefore shrink by q^2 and q^4 respectively.

This also qualifies the earlier master-volume analogy: the knob acts on the primitive legs, not uniformly on every composite-response energy component.

## Two-statistic energy state

Call their declared coefficient energies a and b. Under the source drift they are separately conserved. Under the supplied family gain,

    (a,b) -> (q^2 a,q^4 b),
    observed total H=a+b.

Thus the retained data can be summarized by(a,b) for THIS energy-prediction task. The full source,137 leaves, kernel data and histories are still retained. This is not a claim that the physical state has only two coordinates.

For the supplied fixture,

    a=5746/675,
    b=1118/675,
    H=2288/225.

These use the existing declared coefficient-energy convention, not physical energy units or a fitted reference normalization.

## Exact construction through retained T9

Let P be the actual11-leg incoming-family averaging projector, Q=I-P. The native field projectors are

    P_mean=(P tensor P) direct-sum I16,
    P_one=(Q tensor P+P tensor Q) direct-sum0_16,
    P_two=(Q tensor Q) direct-sum0_16.

They are orthogonal, sum to I137 and commute with the declared interface-preserving native generator A. Their ranks are32,56,49; the energetic ranks are0,16,22 per response channel.

The summaries are

    a=||A P_one F||^2/4,
    b=||A P_two F||^2/4.

The source Hamiltonian is exactly a+b. There is no interference term between the two orthogonal sectors.

For the complete retained T9 target, decode the leaves with L and evaluate these functions on L F_target. The checker verifies identical summaries before/after the retained transport. The previous38-coordinate active reader also contains sufficient information to compute both summaries, without discarding its99-dimensional kernel record.

An exact field update

    F_next=(P_mean+q P_one+q^2 P_two)F

agrees with the ORIGINAL shared-leg gain operation. It is not a new response-cell-writing rule.

## Why current total energy is insufficient

The checker constructs two invertible shared-leg preparations with identical complete family means and identical positive total energy:

- one has only one-leg energetic disagreement;
- the other has only two-leg energetic disagreement.

After the same q=1/2 operation, their energies are respectively

    H/4 and H/16.

So current H, even together with all outer means, cannot predict the next H. Reading the two components resolves that ambiguity.

These are exact mathematical preparation hostiles within the factored-leg class. They are not claims that laboratory preparations with those values have been produced or have equal physical resource budgets.

## A precise predictive quotient

For the declared protocol consisting only of free drift and forward family gains, two preparations have the same energy behaviour for every future gain schedule exactly when their pairs(a,b) agree.

Sufficiency follows from the update law. Necessity follows from two readings: current H and H after a known nontrivial gain0<q<1. Their coefficient matrix is

    [[1,1],[q^2,q^4]],

whose determinant q^4-q^2 is nonzero. The supplied inference function recovers(a,b) and rejects negative/inconsistent inferred energies or the uninformative endpoint gains q=0,1.

This is behavioural sufficiency for the stated task, not a universal physical-state minimum. If the task includes other source operations, archival restoration, matrix responses, phase information or different interactions, more retained information may be relevant. In particular, histories are not discarded when the forward task state reaches(0,0).

Actual two-reading identification would require independently known gain, an energy detector, compatible preparation and measurement back-action/uncertainty control. None is admitted here.

## What to do—and not do—next

For this energy task, no separate mode knobs are needed. The existing conditional scalar-gain rule and the two-statistic reader give a complete mathematical prediction/update law.

For the ORIGINAL Hamiltonian-descent goal, the remaining gates are still source/control-law selection, physical metric/clock/energy/readout meaning, and an actual Postnikov/rung identification. Full ambient controllability is not a substitute for those gates and should not be presented as necessary to close them.

No new B=I input assumption, independent actuator, physical normalization or detector was introduced in this reduction.

## Verification

    uv run research/strominger/checkers/check_energy_task_reduction.py

38 exact checks pass. The29-check control audit,43-check observer and65-check classification/pinned numerical chains rerun as dependencies. No new compiler closure or physical experiment is claimed.

Artifacts:

- `research/strominger/checkers/energy_task_reduction.py`
- `research/strominger/checkers/check_energy_task_reduction.py`
- `research/strominger/results/energy-task-reduction.json`

Predecessor: `research/strominger/shared-leg-controllability-audit.md`.
