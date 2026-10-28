# Testing the proposed 36→1 collective mode and the missing ten

The current folded tiling was tested without supplying Pb-208 counts to the generator. All ranks below are computed by exact integer elimination. These are scalar site-incidence tests, not a derived particle Hamiltonian.

## Two genuine geometric observations

| Original-sheet sector | Surface-exposed sites | Interior sites | Total |
|---|---:|---:|---:|
| P (majority) | 71 | **10** | 81 |
| E (minority) | **1** | 35 | 36 |

The opposite sheet exchanges P/E on exactly the same sites.

Thus both the **one exposed minority site** and the **ten interior majority sites** occur independently in the construction. Ten was not obtained by subtracting 116 from 126.

## A candidate collective operation

Connect two minority sites when they share a whole neutral face-neighbour. This gives 36 sites, 121 distinct comparison links, and one connected component.

Let D take the difference across each link, and L=DᵀD. Both have rank 35, so the candidate coherence constraint

```
D x = 0
```

has one constant spatial mode. Positive link reweighting leaves this kernel unchanged.

There is also a boundary formulation. The minority sector has one exposed site and 35 interior sites. The interior Dirichlet block of L is invertible, with rank 35. Consequently, **under the declared unforced harmonic comparison law**, the single boundary value uniquely determines the interior extension. That extension is constant. This is a precise candidate for many internal comparisons being observed through one boundary value.

It is conditional: no native dynamics has yet selected this harmonic law, excluded interior forcing, or restricted all prepared states to this mode.

## Keep the internal information

One can record the collective mean and the 35 contrasts `xi−x0`. Together these reconstruct all 36 original values exactly. The checker verifies every basis vector.

Keeping all 81 majority readings and only one minority collective observation gives **82 observable coordinates**, but the retained charged-site data still have **117 coordinates**, including the 35 contrasts. That is an observation/retention distinction, not automatically 82 particles.

For an explicit local update, the checker tests

```
T = I − L/25,
```

where 25 is calculated as `2*maximumDegree+1`. It conserves the mean and contracts nonconstant values. T has full rank 36, however, so every finite iterate remains invertible. Fourteen or twenty-eight applications do not produce an exact rank-one collapse. The constant limit is asymptotic, unless an additional projection or admissibility constraint is supplied.

## A necessary selectivity control

The same unrestricted consensus rule on the 81-site majority sector also has one constant mode. Therefore **81+1** is not selected merely by finding a consensus kernel. One still needs a reason to retain all majority modes while observing only the minority collective mode.

Under a boundary-only observation, the majority has 71 boundary coordinates and ten hidden interior coordinates—not 81 independent boundary observables. Its interior Dirichlet block has rank ten.

## Neutron independence and the ten

The current polarity map fixes N coefficients and reverses their interface direction. Stacking the two N readings gives 116 displayed occurrences but rank **58**, not 116 independent site states.

The ten interior majority sites are dual-labelled P/E under polarity, but they already belong to the 81-site charged sector. They are not yet ten additional independent N modes. Promoting their comparisons to N states requires a typed, independence-preserving map; simply adding them would reuse existing coordinates.

As another check, the raw whole-face incidence network has:

- 56 distinct neutral P–E mediators;
- 560 two-leg P–N–E paths;
- rank 36 for the composed P/E incidence map;
- rank 56 for joint charged observation of the 58 neutral sites.

These simple interface operators do not select ten additional N modes. This does not exclude a different physically justified operator.

## Outcome

The collective/boundary interpretation has real structural support: **36 = 35 interior + one boundary**, and **81 = 71 boundary + ten interior**. It does not yet justify independent N doubling, reuse of the ten as extra N states, or Pb-208 counts.

Run:

```
node research/strominger/checkers/check_collective_pair_modes.mjs
```

**10 check groups pass**, including the controls against premature collapse, missing contrast information and polarity double-counting. Detailed graph, ranks and contraction trace: `results/collective-pair-modes-v1.json`.

The viewer and its particle-count labels are unchanged by this test.
