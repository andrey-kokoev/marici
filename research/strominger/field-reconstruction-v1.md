# Conditional reconstruction within the 137 comparison labels

## Prior research and the actual new question

This is not the first field-reconstruction construction in this programme.

- [`field-comparison-preparation-v1.md`](field-comparison-preparation-v1.md) already retains all 144 operator-valued arrow blocks: 121 counted blocks and 23 reference-touching blocks. They determine the field up to common phase; an amplitude anchor restores the full field. Its checker covers zero and reference-only fields as well as generic fields. Its co-moving coordinates use spatial rotations, not an assumed identification with the present corner coordinates.
- [`rung-symmetry-atlas-v3.json`](rung-symmetry-atlas-v3.json) and `check_rung_automorphism_classification.py` already establish the scalar complex commutant of the actual named projector P and corner cycle C. Metric preservation reduces its nonzero scalars to U(1). This is an operator-symmetry statement, not by itself a reconstruction theorem.
- [`../kitaev/target-domination-is-weaker-than-full-state-observability.md`](../kitaev/target-domination-is-weaker-than-full-state-observability.md) distinguishes reconstruction of a target from reconstruction of a whole state. Here we deliberately ask for the whole field modulo phase; a narrower target may require less information.
- [`../kitaev/scrambling-is-collapse-of-a-restricted-reconstruction-margin.md`](../kitaev/scrambling-is-collapse-of-a-restricted-reconstruction-margin.md) requires frozen source/tester norms and distinguishes exact rank from a uniformly stable inverse. Its linear singular-value theorem is not silently applied globally to this quadratic map; below we give a direct pair-of-fields instability witness.
- [`../nima/accessible-readout-algebra-gate.md`](../nima/accessible-readout-algebra-gate.md) distinguishes a separating mathematical readout from an implemented instrument. No instrument is supplied here.
- [`../nima/carrier-probe-adapter-and-state-reference.md`](../nima/carrier-probe-adapter-and-state-reference.md) already shows that 137 record slots need not mean 137 independent observations and that the state branch cannot automatically be inferred from an arrow-only probe model.
- [`../kitaev/coherence-probe-redundancy-is-edge-connectivity-not-probe-count.md`](../kitaev/coherence-probe-redundancy-is-edge-connectivity-not-probe-count.md) provides a related phase-synchronization lesson: disconnected probe access can conceal relative phases. Its additive graph-error theorem is not asserted for the present quadratic comparisons.

**New question:** can scalar channels within the existing 121+16 labels recover the field conditionally, with the four-state branch supplying the excluded arrow information instead of explicitly retaining all 23 reference-touching operator blocks?

## Declared comparison and three channels

Use the previous experiment's actual corner coordinates c_e = B_e^{-1} x_e, positive metric K3, excluded arrow r=(a,t), and destination-labelled state vectors z_a. Their t-th triple is c_(a,t), with a zero self-arrow triple.

For E in {P, Q=I-P, C}, retain

```
arrow_E[i,j] = c_j* K3 E c_i,          i,j != r;
state_E[a,b] = z_b* (I4 tensor K3 E) z_a.
```

P and Q recover the prior projector-resolved comparisons. Their sum is the unrefined Gram. The C channel uses the actual named cycle, which is **not K3-unitary** and does not commute with P. It is not a positive Gram channel and is not silently substituted with a Hermitian or orthogonal cycle.

There are **137 labels, three complex scalar channels per label, 411 complex values**. These values have many dependencies. Neither minimality nor 137 scalar values is claimed.

## Conditional uniqueness theorem

Assume:

1. The eleven selected arrow triples span C3.
2. For the two sources b outside {a,t}, the rows
   `c_(b,t)* K3 P` and `c_(b,t)* K3 Q`, stacked together, have rank three.
3. The supplied P, Q, C and metric are the verified source operations. In particular the complex simultaneous commutant of P and C consists only of scalars.

Then equal three-channel data determine the entire twelve-arrow field **up to one common unit-modulus scalar**.

### Selected arrows

Equal P+Q Gram data on a spanning family imply that the selected triples are related by one K3-unitary T. Equal P data imply T commutes with P. Equal C data imply T commutes with C: since the selected columns span, equality of all their matrix elements is equality of the underlying operators. The source commutant calculation forces T to be scalar, and metric preservation makes that scalar a phase.

### Excluded arrow

Align that common phase, so all selected triples coincide. Write v for the difference between the two excluded triples. For b outside {a,t}, subtracting the known terms from state_E[a,b] gives

```
c_(b,t)* K3 E v = 0,     E=P,Q.
```

The rank-three condition forces v=0. Because the P and Q row spaces are complementary, an equivalent sufficient gate is P-probe rank one and Q-probe rank two.

This proof classifies all collisions **within the stated domain**, not just sampled transformations. The span/rank hypotheses are substantive: the checker supplies a counterexample outside them.

## Exact decoder, not only a uniqueness argument

`field_reconstruction.py` consumes the measurements and the source operations, not the original field:

1. Select three independent measured arrow anchors and obtain their Gram M.
2. Solve for the matrices of P and C in that measured anchor basis.
3. Solve the two intertwining equations against the actual source P and C. Their common solution is a one-dimensional line of invertible 3x3 frames S.
4. Compute rho from `S* K3 S = rho M`, certifying its positive sign in the chosen algebraic real embedding with rational interval bounds.
5. Recover every selected triple in this representative frame.
6. Recover the excluded triple from the four linear state equations above.
7. Regenerate and check **all 411 measurements**, including those not needed in the solves.

The output is a field representative y and positive rho. The field `y/sqrt(rho)` is the original field up to common phase. This exact representation avoids introducing an arbitrary floating-point phase anchor or extending the algebraic field merely to display a square root.

Missing channels, mismatched provenance, an inconsistent unused cycle measurement and negative Gram data are rejected. This is an exact algebraic decoder on its gated domain, not a noise-tolerant least-squares implementation.

## Verified connection to the earlier operator packet

The checker converts both the original corner field and decoded representative through their actual native frames into the older co-moving preparation. Every one of its **144 operator blocks** is reproduced, multiplied by rho. Normalizing removes rho, and the remaining common phase cancels in the operator blocks.

Thus, on the reconstruction domain, the new scalar packet determines the earlier complete unanchored operator packet. The earlier anchored recovery is freshly replayed. This is not a claim that the two coordinate systems or their metrics were identical by notation.

The full operator packet remains the robust structural fallback outside this domain, including zero and reference-only fields. The new decoder does not replace that previously available coverage.

## Why the cycle channel matters

A nontrivial sector phase `T = phase P + Q` leaves all P and Q comparisons unchanged. The checker verifies that it changes the C channel and that both original and transformed fields reconstruct correctly from their own three-channel packets.

A common phase leaves all three channels unchanged. Decoding that packet gives the identical normalized projective representative. No absolute phase is recovered without additional reference data.

## Exact failure stratum

Start with the spanning fixture and zero the two selected arrows `(b,t)` for b outside {a,t}. The remaining selected arrows still span C3. Now multiply only the excluded arrow by a nontrivial phase.

All 411 values remain equal:

- the excluded arrow is absent from the arrow block;
- state off-diagonal comparisons have no surviving incoming probe at its destination;
- its state diagonal quadratic forms are phase invariant, including the C form.

The two fields are not related by one common phase: nonzero selected arrows are unchanged. The decoder rejects the missing-reference rank failure. Thus even cycle-sensitive data are **not universally injective**.

## Near the failure stratum: exact instability witness

Scale those same two incoming probe arrows by epsilon instead of zero. For epsilon = 1, 1/10 and 1/100, all reconstruction gates pass and decoding is exact.

Freeze the source norm as `sum_e c_e* K3 c_e`. For this diagnostic only, freeze the tester norm as the unweighted squared-modulus sum of the 411 complex output coordinates. This is a declared diagnostic metric, not a derived instrument cost or a conserved energy.

Compare each field with the one differing only by the fixed excluded-arrow phase. The anchored source difference is independent of epsilon, while the output difference is exactly linear in epsilon: its squared norm is epsilon^2 times the baseline value. At epsilon=0 the distinct phase classes collide. The unchanged nonzero selected arrows prevent the two source classes from approaching the same common-phase orbit.

Consequently there is no uniform inverse Lipschitz bound near this stratum, even modulo common phase. Raising the gain on weak probes would change the tester normalization rather than eliminate the obstruction for free. We do not claim an optimal singular-value bound or optimal anchor selection.

## Synthesis disposition

The structural chain now has a conditional theorem:

```
retained field
 -> 137 labels carrying P/Q/C comparisons
 -> full unanchored operator packet, on the spanning/probe domain
 -> field modulo common phase.
```

The state branch can recover excluded-arrow data under a precise probe condition. It does not universally replace retained reference records. Cycle-sensitive observation removes the projector-preserving ambiguity generically, but not a disconnected reference phase.

Still open: operational realization of these complex comparisons, source selection of the coframe policy and tester costs, noise-aware reconstruction, and identification with the pinned 2x2 numerical/DG carrier. The new channel does not silently extend the previous rectangular DG trial or determine its supplied direct reference d.

## Reproduction

```
python research/strominger/checkers/check_field_reconstruction.py
```

Receipt: `research/strominger/results/field-reconstruction/verification.json`. The checker freshly replays the preceding metric/DG experiment, the source symmetry classification and the earlier operator-comparison preparation. No production or viewer code is changed.
