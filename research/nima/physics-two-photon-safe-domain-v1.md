# Maximal two-photon domain for the ordered three-bin route

## Scoped result

For the fixed nominal cavity rounds W0,W1,W2 and transmitted detector ports 2,5,8, the 55-dimensional initial two-photon optical sector has a **52-dimensional maximal safe subspace**. Every complete routed detector history is defined on this subspace without multiphoton truncation.

This is a conditional initial-state domain theorem for the declared three-round schedule. It is not an invariant domain for arbitrary passive operations, a physical preparation authorization, or physical sector admission. The previously accepted total-N<=1 overlap is unchanged.

Contract: `contracts/physics-two-photon-safe-domain.v1.json`.
Checker: `checkers/check_physics_two_photon_safe_domain.py`.

## Why only three linear constraints are needed

Let H2 be the total-two-photon sector in ten modes. Its occupation basis has dimension `10*11/2=55` and factorial metric. At detector port p, the only forbidden occupation in H2 is |2_p>; all other occupations have n_p<=1.

For each round k, evolve with Gamma(W_k). If the current detector absorbs a photon, total number becomes at most one and every later local detector event is automatically safe. Thus the only branch that can violate a later event is the branch retaining **both photons**.

In that branch, each earlier detector port had local vacuum. The optical operation is the projection `P_vac(p)`; for initial ready memory its no-click amplitude is one. For initial dead memory, the stay-dead no-click branch has nonzero amplitude 4/5, so this optical branch remains possible. Recovery branches change only the nonzero scalar and memory. Therefore the same optical constraints are necessary for either initial classical memory state.

Define linear coefficient rows on the initial H2:

```
c0 = <2_2| Gamma(W0)
c1 = <2_5| Gamma(W1) P_vac(2) Gamma(W0)
c2 = <2_8| Gamma(W2) P_vac(5) Gamma(W1) P_vac(2) Gamma(W0).
```

The common safe space is `ker(c0) intersect ker(c1) intersect ker(c2)`.

### Sufficiency

If all three rows vanish, the first event has no forbidden input. After it, any absorbed branch has at most one photon. The unabsorbed two-photon branch is precisely the projected-vacuum branch used in c1. It is safe by c1=0. Repeat for c2. Every outcome prefix and every separately labelled Kraus branch is consequently in the local n_port<=1 domain.

### Necessity and maximality

If any row is nonzero, take the earliest such row. Earlier detector events are valid, and the zero-absorption no-click branch survives with nonzero scalar amplitude for either R or D initial memory. At the failing bin, it has nonzero |2_p> coefficient and therefore strictly positive forbidden squared norm. The finite instrument cannot act there under its declared domain. A projection deleting that mass would be a different operation.

Thus the row intersection is the exact maximal initial optical subspace in H2 for this schedule, not merely a sufficient preparation family.

## Dimension and complex/density extension

Exact rational row reduction gives rank three, with pivot occupation coordinates 2_x, x+mode2 and x+mode5. The constraint rows and pivot coordinates are recorded in the receipt. The nullity is 55-3=52. Free-coordinate construction provides a rational nullspace basis.

The rows and evolution maps are complex-linear. Their exact rational rank is the same over C, so the statement covers arbitrary complex superpositions in the 52-dimensional safe space, not only the real executable probes.

Positive density operators supported there satisfy the same event-domain condition by spectral decomposition. Forbidden probability is nonnegative; mixing unsafe components cannot cancel it. With classical memory, apply this criterion to each populated memory block.

Since vacuum and total-N=1 were already safe, the direct sum through total N=2 has optical dimension `1+10+52=63`, compared with 66 for the unrestricted truncated sector. This is a schedule-specific conditional extension, not a modification of the accepted overlap catalog or an assertion that the coherent-state domain is now admitted.

## Domain guards and prior obstructions

The earlier input |1_x,1_u0> is not in this kernel: it violates c0 and creates transmitted two-photon probability 23328/390625. It remains rejected. The new safe subspace is not obtained by silently deleting that probability.

The checker constructs three separate earliest-failure vectors: the first violates c0; the second satisfies c0 but violates c1; the third satisfies c0,c1 but violates c2. Each is rejected at its actual failing detector. Hence a first-round-only support test is insufficient for later composition.

This refines the common-source assembly guard: check the full schedule constraint, not just total photon number or the first detector input. Native source-law, physical clock/preparation and reviewed sector assembly gates remain open.

## Verification

Fresh exact tests generate the 52-vector safe basis and 51 adjacent pair sums, preserving the factorial metric. They evaluate 1648 complete three-bin histories across R/D initialization without encountering the local multiphoton guard, and verify complete-outcome normalization against each input norm.

Row independence, nullspace membership and all three earliest-failure witnesses are checked exactly. The unrestricted validity/maximality statements follow from the branch-number and linearity arguments above; finite probes corroborate the implementation. Inputs are hash-checked before and after checking.

```
python research/nima/checkers/check_physics_two_photon_safe_domain.py
python research/aspect/scc/scc.py check physics-programme-v18
```

Measurement work remains parked.
