# Individual branch isometries fail by rank; combined initial normalization remains possible

**New batch, iteration 5 of 10.**

**Strength:** exact metric-independent branch-rank obstruction and a conditional positive-metric completeness witness. Not a no-go for general instruments, nor a derived physical metric.

[Previous event register](EVENT-REGISTER-PARITY.md) · [Checker](check_event_branch_metric.py) · [Receipt](results/event-branch-metric.v1.json)

## 1. Fresh scope: the boundary-initialized selected plane

Use the existing synchronized two-column boundary mode frame at z=1, extended by six zero internal-state rows. Call this eighteen-by-two frame E. It is an initial selected plane, not an invariant plane of the primitive-step automaton.

For each full event label l=(pair,primitive,completion), compute B_l=T_l E. Among sixteen labels, twelve have rank one and four vanish on this initial plane. These ranks are checked before choosing a metric.

## 2. Rank rules out scalar-weighted branch isometries

For any positive input metric G and positive output metric H_l, the pullback B_l^t H_l B_l has the same rank as B_l. A nonzero rank-one branch therefore cannot satisfy

    B_l^t H_l B_l = p_l G

for a state-independent nonnegative scalar p_l: the right side has rank two if p_l>0 and is zero if p_l=0. This obstruction allows even a different positive output metric for each branch. The receipt gives each branch's exact pullback and a nonzero kernel vector in the two mode parameters.

Zero branches are harmless with weight zero. The nonzero rank-one branches can still be measurement-like, state-dependent maps; general instruments do not require each branch to be a scaled isometry. Accordingly this result must not be renamed an obstruction to every physical instrument.

## 3. A common positive metric does normalize the combined initial map

There is a useful positive counterpoint. In the existing zero-based context order, let H be diagonal with weight three at states 4 and 7 and weight one elsewhere. H is positive and reflection-invariant. Direct exact calculation gives

    G=E^t H E = [[10,2],[2,2]], det(G)=16,
    sum_l B_l^t H B_l = G.

Thus the complete label-bearing one-step map preserves norm on this initial plane in an explicit common metric, although its individual branches do not preserve it up to constant scalar weights.

The branch quadratic forms sum to G. Their relative weights depend on the input direction; no physical probability interpretation is admitted. H is a conditional mathematical choice, not a source-derived metric or a uniqueness result.

The witness also does not preserve the reference macro-step invariant form: its induced G is not invariant under the reference two-dimensional macro step. Different notions of metric compatibility should not be identified merely because each involves the selected initial frame.

## 4. One-step fitting is not repeatable completeness

Let P=sum_l T_l be the aggregate primitive-step operator. Apply the same metric test to the next aggregate frame PE:

    sum_l (T_l PE)^t H (T_l PE) != (PE)^t H (PE).

The exact matrices are in the receipt. The constructed H therefore fails even this next aggregate-frame test. This is only the failure of one witness, not a proof that every positive metric fails on a larger repeatable carrier.

For the entire eighteen-state controller, any positive-metric isometry of the labelled endpoint map is impossible without extra residual outputs: all T_l kill the nonzero predecessor difference e_1-e_14. Its input norm in every positive metric is strictly positive. Original retained history and the two provenance-difference records must remain accounted for.

## 5. Next executable gate

Compute the smallest carrier containing E and closed under **every labelled transition**, not merely P. Branch-specific closure can be larger than aggregate closure because cancellations across event labels are absent.

Then solve or obstruct common positive-metric completeness on that whole carrier. Include provenance residuals explicitly when testing lossless operations. This distinguishes a repeatable instrument candidate from a one-step fit on a noninvariant plane, without mistaking rank-one measurement branches for scaled unitary dynamics.

The scientific root remains null. No physical metric, branch probability, emission, coherent erasure or preparation authority is derived. Existing pinned formal contracts remain unchanged.

## Reproduce

```sh
python research/scattering/seed-composition/check_event_branch_metric.py
python research/scattering/seed-composition/check_event_branch_metric.py --check
python research/scattering/seed-composition/check_event_register_parity.py --check
python research/scattering/seed-composition/check_seed_composition_net.py
python research/scattering/low-energy/check_low_energy_net_v3.py
```

The checker recomputes prerequisites, uses exact rational matrices and writes only its own receipt. `--check` compares read-only.
