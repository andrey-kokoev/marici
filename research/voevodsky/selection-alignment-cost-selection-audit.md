# Can retained operations select the selection/alignment cost difference?

## Answer and new constraint

We recovered the prior gap-symmetry, sector-protection, index-protection, autonomous-execution and source-interchange work before adding another energy mechanism.

The resulting test does **not** select Delta_L > Delta_G. It does select a narrower conclusion:

> If the cost of every forward source traversal depends only on whether its departure comparison slot maps to L, G or N, and independent-operation interchange must preserve additive cost, then c_L=c_G=c_N.

This is an exact result on all 52,488 admitted interchange faces of the operation-resolved source graph, not an appeal to a generic symmetry slogan. It rules out deriving the previous unequal stage costs from that simple traversal-cost interpretation.

More general coherent positive costs are possible. We construct them with exact reservoir accounting and with either ordering of the stored stage gaps. Thus the missing selection cannot be supplied merely by positivity, charge-preserving relabelling or independent-operation coherence.

## 1. What prior research already supplies

All paths in this table are under `research/nima/`.

| Prior construction | Positive result | Remaining choice relevant here |
|---|---|---|
| `mass-gap-symmetry-and-protected-kernel.md` | Exact rooted slot orbits and a charge-sector offset argument | Rooted symmetry leaves independent energy coefficients; even positive-square constraints do not force a nonempty protected kernel |
| `mass-local-sector-protection.md` | Exact Gauss constraints plus restricted tensor-factor locality can prevent conversion between collective and elementary sectors | A one-site diagonal energy perturbation still changes their gap; transition protection is not energy-value protection |
| `mass-index-protected-energy-bound.md` | An explicitly supplied graded complex protects saturation of a chosen bound | Its central-charge weights and grading are not supplied by the actual source complex |
| `mass-autonomous-history-execution.md` | A time-independent Hamiltonian executes the reversible locking programme with retained records and reservoirs | It supplies neither the charging law nor a terminal latch; completion is not a stationary state |
| `mass-source-interchange-coherence.md` | Explicit independent-operation squares/cubes retain genuine traversal cycles | The operation-resolved complex has H1 rank 228; no physical energy pairing is selected |

These results mean that building another controller, clock, index example or symmetric family would repeat an already identified boundary. The useful test is whether the actual source operations impose a new relation on our proposed stage costs.

## 2. Reuse the new record bridge on the old source graph

The previous geometry bridge labels each of the 1836 comparison slots:

- state-comparison slot -> L;
- arrow-comparison slot whose right inner arrow is outgoing from the shared reference -> G;
- other arrow-comparison slot -> N.

This gives 108 L slots, 432 G slots and 1296 N slots, agreeing with the actual proton transfer supports.

The source operation graph acts on these slots through four kinds of operation:

1. append an outer path;
2. append a left inner path;
3. append a right inner path;
4. read endpoints into a state-comparison record, retaining the parent history.

There are 17,820 directed operation edges. The admitted coherence faces interchange an outer operation with an independent inner operation, or left and right inner appends. Their product construction supplies 52,488 squares.

These edges are **operations on comparison records**. They are not the 1836 coefficient arrows to which those records map. This distinction is essential: a cost of visiting or changing a record is not automatically the energy of an occupied coefficient-channel register.

## 3. Departure-stage-only traversal cost is forced to be uniform

Try

    r(e) = c_stage(source(e)).

For each interchange square, compare the two two-step routes. Their cost difference is a linear expression in c_L,c_G,c_N. The checker constructs every such expression and computes their exact rank.

The constraint matrix has rank two, and its kernel is precisely the constant vector:

    c_L = c_G = c_N.

Two kinds of square already explain the result:

- An outer append commutes with an endpoint readout. One route pays the outer-append cost before the change from an arrow slot to an L slot; the other pays it afterward. Since the outer operation's own retained action is unchanged, the departure-stage-only rule must equate those costs.
- An outer append similarly commutes with a right-inner append that changes an outgoing-reference G slot into an N slot. This equates the remaining pair.

The result uses the declared independence/coherence contract. A coupled implementation could assign different work to the two paths, but then it must supply that coupling and its work reservoir rather than claim these are the same independent-operation interchange with the same resource.

This equality is NOT a theorem that stored channel gaps Delta_L,Delta_G,Delta_N are equal. It restricts the stated traversal-cost ansatz. Identifying those gaps with this traversal cost would give no intrinsic splitting in 324(Delta_L-Delta_G), so that particular identification cannot explain a nonzero difference.

## 4. Positive coherent resource survives without selecting stored gaps

A constant cost for each actual operation kind,

    kappa_outer, kappa_left, kappa_right, kappa_endpoint,

respects every admitted square: both routes contain the same count of each kind. The four coefficients need not be equal.

Returning appends remain genuine resource-consuming operations. An outer append followed by a fresh returning append costs 2 kappa_outer, despite returning to the same active label. It is not the inverse operation on the full history.

A more general explicit family is

    r(e) = kappa_kind(e) + V(target(e)) - V(source(e)).

The potential difference telescopes around each square, while the operation-kind costs cancel between its two routes. Hence r descends through all admitted interchanges for any V.

Take V(slot)=Delta_stage(slot) and kappa=(2,3,5,7). The checker tests both

    (Delta_L,Delta_G,Delta_N) = (2,1,1)
    (Delta_L,Delta_G,Delta_N) = (1,2,1).

Every one of the 17,820 forward operations has strictly positive r in both cases. An explicit ledger balances each edge:

    stored-energy change = V(target)-V(source),
    resource-sink increase = kappa_kind,
    battery change = -r.

Their sum is zero. The source history is retained; the sink is an accounting register, not a derived thermodynamic bath. A fresh returning append consumes positive resource and transfers it to the sink, while the active-state potential returns to its original value.

Both choices therefore admit coherent positive traversal accounting. Their associated fully occupied stage-gap totals give opposite intrinsic proton–belt differences, +324 and -324. Equal gaps give zero. These are explicit model controls, not physical energy predictions. They show that coherence and reservoir balance do not by themselves choose the ordering of V or of the stored gaps.

The same gap assignments are invariant under all 216 independent rooted S3 relabellings of the three comparison roles. All 396,576 slot/action cases are checked. This generous symmetry preserves the stage classes; consequently it cannot distinguish the two gap orderings. No claim is made that every member of this enlarged slot symmetry is a physical symmetry of the coefficient geometry.

## 5. What the source actually distinguishes

The graph distinguishes enabled operations as follows:

| Departure-slot label | Outer appends | Left appends | Right appends | Endpoint readouts | Mean enabled outgoing operations per slot |
|---|---:|---:|---:|---:|---:|
| L | 324 | 0 | 0 | 0 | 3 |
| G | 1296 | 1296 | 1296 | 324 | 39/4 |
| N | 3888 | 3888 | 3888 | 1620 | 41/4 |

These are exact incidence differences. They do not say that all alternatives must execute, that each must remain physically occupied, or that their costs should be summed into a rest energy. The L rows are active state-readout labels in this finite operation graph; absence of inner appends there does not assert that the retained parent histories have been erased.

Thus the source does distinguish operation availability, but it does not support the immediate inference 'selection requires more work than alignment.' To use this table for energy one must specify occupation, execution rates or retained physical resources.

## 6. Preparation effort is another distinct quantity

We also test a minimal measurement implementation of the already checked commuting L/G projectors. Supply a fresh maximally mixed 36-dimensional input for every trial, measure one constraint, abort immediately on failure, then measure the other. The common-success probability per fresh trial is 1/36 for either order and either carrier.

Expected unit-cost measurement attempts until success are:

| Schedule | Proton | Belt |
|---|---:|---:|
| L then G, early abort | 48 | 39 |
| G then L, early abort | 39 | 48 |
| Always attempt both | 72 | 72 |

For example, under L-first the first measurement is attempted 36 times on average; the second is attempted rank(L) times, giving 36+12 or 36+3. The reverse order replaces rank(L) by rank(G).

These formulas are exact. But reset states, measurements, scheduling and unit attempt costs are supplied. G-first is a competing commuting-projector implementation, not an assertion that the original typed three-stage protocol admits a free interchange. Its equality as a final projector does not make its full recorded history identical.

The control demonstrates why preparation effort cannot be identified with persistent particle mass just because it uses the same projectors. Additional accounting for the original return stage, reservoirs and repeated input preparation must remain explicit.

## 7. Revised synthesis frontier

We now know more precisely what not to conflate:

- **Source traversal resource:** a positive additive pairing on retained operation histories.
- **Stored channel energy:** an occupation Hamiltonian on persistent record degrees of freedom.
- **Constraint penalty:** departure from the selected carrier state.
- **Preparation effort:** a protocol-dependent resource budget.
- **Rest energy:** the energy of a protected particle sector relative to a common vacuum.

The source's existing interchange cells genuinely constrain the first quantity: the naive departure-stage-only assignment becomes uniform. They leave explicit room for either ordering of the second. The third and fourth have already been independently constructed and do not close that gap.

The next productive task is not another arbitrary Hamiltonian. It is to specify which **physical record change** the retained source demands, how much conserved resource that change exchanges, and how the corresponding records remain occupied in a particle sector. The existing local-sector protection can then be reused, rather than rediscovered. The resulting resource functional must respect the actual history interchanges while distinguishing persistent occupations from bookkeeping labels.

If no such physical record interpretation is selected by the present source, the synthesis must explicitly add one and test its extra observable consequences. The mathematical structure has now localized that necessary input instead of leaving it hidden in Delta_L and Delta_G.

## Verification

    python research/voevodsky/checkers/check_selection_alignment_cost_selection.py

This freshly reconstructs the prior source operation graph and its dependencies; it does not merely read an old result summary. All 52,488 square checks, the rank-two departure-cost constraints, 396,576 rooted symmetry cases, edgewise positive-cost reservoir controls, and preparation formulas use exact integer/rational arithmetic.

Result: `research/voevodsky/results/selection_alignment_cost_selection.json`, including explicit square witnesses.

The broader prior sector/index/autonomous-execution conclusions above were recovered from their research notes; they are not claimed as newly rerun by this checker.
