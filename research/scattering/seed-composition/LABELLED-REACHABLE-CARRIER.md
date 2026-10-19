# Labelled closure reaches lost history directions: endpoint completeness fails in every positive metric

**New batch, iteration 6 of 10.**

**Strength:** exact minimal reachable carriers and a metric-independent kernel obstruction. Not a no-go for enlarged history-preserving maps or modified controls.

[Previous metric test](EVENT-BRANCH-METRIC.md) · [Checker](check_labelled_reachable_carrier.py) · [Receipt](results/labelled-reachable-carrier.v1.json)

## 1. Fresh continuation question

The previous turn found a positive metric normalizing the initial selected plane for one labelled step, but that particular metric failed at the next aggregate frame. This turn tests repeatability on the actual common labelled carrier instead of extrapolating a one-step fit.

Start with the synchronized boundary mode frame at z=1 and six zero internal rows. Repeatedly add its images under every full event-label matrix T_l, pruning by exact rational rank. Every retained basis vector is an actual finite event-word image of a seed column. The final basis is checked invariant under every T_l, proving it is the smallest common invariant carrier containing the seed.

## 2. Labels change the reachable carrier

Dimensions by closure round, including the seed and the final unchanged round:

    labelled:  2 -> 13 -> 14 -> 14,
    aggregate: 2 -> 3 -> 4 -> 5 -> 6 -> 6.

The fourteen-dimensional labelled carrier has seven even and seven odd reflection directions. The six-dimensional aggregate carrier is entirely odd and is contained in the labelled carrier.

The receipt includes both exact bases and their generation histories. Retaining event labels prevents the cancellations used by aggregate propagation. Thus aggregate closure is not a faithful replacement for closure under conditional event branches.

## 3. The endpoint kernel is actually reachable

The two known predecessor differences are

    v1=e_1-e_14,
    v2=e_10-e_16.

Both belong to the labelled carrier; the checker solves their coordinates in its generated basis and verifies the reconstruction. Neither belongs to the aggregate carrier. Every full event matrix kills each vector:

    T_l v1 = T_l v2 = 0 for all l.

On the fourteen-dimensional carrier the stacked event-labelled endpoint map has rank twelve, so these two independent witnesses span its entire kernel. Appending the two retained difference rows restores rank fourteen.

This is a reachability result, not just an obstruction somewhere in the ambient eighteen-state controller. Linear combinations of actual event-word images produce the witnesses, so a common invariant linear carrier containing the selected plane must account for them.

## 4. No positive metric can restore endpoint completeness on this carrier

Let A_l denote T_l restricted to the common labelled carrier. A proposed repeatable completeness equation is

    sum_l A_l^t G A_l = G, G positive definite.

Evaluate it on either nonzero kernel witness. Every term on the left vanishes, while the right is strictly positive. Contradiction.

The same argument allows different positive output metrics for different branches: zero branch outputs still have zero norm. Coordinate changes or scalar reweighting of these branches cannot remove a common kernel.

The obstruction concerns **unchanged labelled endpoint maps without additional history/residual outputs**. It does not rule out general instruments, predecessor-preserving extensions, modified controls, step-dependent metrics on enlarged outputs or independently supplied preparation. It supplies no physical probability or clock law.

The one-step metric from the preceding turn remains a valid conditional calculation on its initial plane. Its failure to extend is now explained by the unavoidable reachable kernel of the full labelled closure, not merely by an unsuccessful fitted metric.

## 5. Next executable construction

Construct an event-arc lift retaining predecessor state, event label and target state. Copy coefficients into each allowed arc rather than summing different predecessors into one endpoint. Give the output a positive fiber-weighted counting metric and check an exact decoder and the endpoint-summary square.

This will determine whether history retention repairs the mathematical normalization obstruction, and expose any extra weights needed to interpret it physically. Keep existing rejected-control and source-history records; do not call a larger accounting map a derived preparation.

The scientific root remains null; formal work-net and low-energy contracts are unchanged.

## Reproduce

```sh
python research/scattering/seed-composition/check_labelled_reachable_carrier.py
python research/scattering/seed-composition/check_labelled_reachable_carrier.py --check
python research/scattering/seed-composition/check_event_branch_metric.py --check
python research/scattering/seed-composition/check_seed_composition_net.py
python research/scattering/low-energy/check_low_energy_net_v3.py
```

Exact rational rank and elimination certify closure, invariance and kernel membership. The checker recomputes prerequisites and writes only its own receipt; `--check` is read-only.
