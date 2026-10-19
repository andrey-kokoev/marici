# Retaining predecessor arcs repairs the endpoint kernel with a history-dependent counting metric

**New batch, iteration 7 of 10.**

**Strength:** executable lossless conditional event-history lift, positive weighted norm identities and source-API recovery tests. Not native control, physical normalization or odd preparation.

[Previous reachable carrier](LABELLED-REACHABLE-CARRIER.md) · [Checker](check_retained_event_arc_lift.py) · [Receipt](results/retained-event-arc-lift.v1.json)

## 1. Fresh obstruction and enlargement

The common labelled endpoint carrier has dimension fourteen and contains two directions killed by every event branch. No positive metric repairs that unchanged endpoint map without extra outputs.

This turn retains each allowed event arc as a distinct labelled record

    (predecessor controller state, primitive event, target controller state).

There are eighteen states and twenty-six allowed arcs. A local conditional arc registry uses the unchanged `RetainedSuccessorLedger` implementation to retain concatenated arc words and recover their parent prefixes.

This registry does not replace the original ten-primitive source registry. It explicitly assumes the existing segmented controller policy. The supplied dictionary, accepted/rejected primitive masks and original source history remain required; the test does not derive their operation from native dynamics.

## 2. Initial copy lift and decoder

Let d_s be the number of allowed controller arcs leaving state s; each d_s is one or two. Define

    (Lx)_arc = x_predecessor,
    (Dy)_s = mean of y over arcs leaving s.

Then DL=I on all eighteen controller coordinates. Give each arc weight 1/d_predecessor. The positive diagonal output metric H_arc satisfies

    L^t H_arc L = I.

The initial lift therefore preserves the ordinary input counting norm without changing coefficients. On the fourteen-dimensional reachable carrier it has rank fourteen. The previously lost predecessor difference has nonzero retained arc output and positive weighted norm, even though its labelled endpoint summary is zero.

Two checked summary squares distinguish retention from lossy observation:

    S_endpoint L=P,
    S_event_label L=V.

Thus the old aggregate and labelled maps are observers of the larger lift, not invertible replacements for it.

## 3. Repeatable retained extension with inherited weights

For each retained parent word, let d be the number of outgoing arcs from its final target. The owning ledger copies the parent coefficient into d children and uses a uniform fiber mean as decoder. Assign

    w_child=w_parent/d.

All weights remain strictly positive. Each copied parent contributes d*(w_parent/d)*x^2=w_parent*x^2. Induction proves exact norm preservation and recovery at every finite event depth, since no controller state is a sink.

Equivalently, a complete path carries the product of inverse branching counts along its history. These weights depend on the entire retained word, not just its final state.

The checker exercises:

| Event depth | Retained words | Lift rank on full states | Lift rank on reachable carrier |
|---|---:|---:|---:|
| 1 | 26 | 18 | 14 |
| 2 | 34 | 18 | 14 |
| 3 | 48 | 18 | 14 |
| 4 | 64 | 18 | 14 |

At every tested depth, the state decoder recovers all eighteen inputs and the aggregate endpoint observer equals P to that depth. The recorded depth counts controller events, not an independently derived physical clock.

## 4. Actual source mean/detail and reflection checks

For arbitrary child coefficients, the existing source `split_payload` returns parent means and detail. Under the inherited weights the two records obey

    ||child||^2_child = ||parent means||^2_parent + ||detail||^2_child.

The inherited copy and detail are weighted-orthogonal. Tests call the owning API, reconstruct every child coefficient and check this exact norm identity rather than fitting a new decoder.

Graph reflection maps complete arc words and preserves every branching count, so it preserves the inherited metric and intertwines the state lift. The construction can retain odd inputs, but it still does not prepare them from arbitrary inputs or discard their even records.

## 5. What was repaired—and what was not

The predecessor-preserving extension evades the earlier kernel obstruction by retaining information before endpoint summation. It provides a positive **history-dependent output counting metric**, not a common positive metric on the unchanged finite endpoint carrier. Therefore it does not contradict the previous impossibility result.

No inverse-square-root amplitude gain is implemented: coefficients are unchanged copies and the metric weights carry the normalization. Reinterpreting those weights as transition probabilities, physical energy or emission rates would require additional source justification.

Next compare this controlled arc history lift with unrestricted native primitive extension, retaining accepted and rejected control histories. Test whether conditioning commutes with inherited fiber normalization, or changes branch weights and requires an extra normalization operation. In particular, normalization relative to the allowed controller domain must not be silently identified with normalization relative to all native outgoing primitives.

The scientific root remains null; formal work-net and downstream contracts remain unchanged.

## Reproduce

```sh
python research/scattering/seed-composition/check_retained_event_arc_lift.py
python research/scattering/seed-composition/check_retained_event_arc_lift.py --check
python research/scattering/seed-composition/check_labelled_reachable_carrier.py --check
python research/scattering/seed-composition/check_seed_composition_net.py
python research/scattering/low-energy/check_low_energy_net_v3.py
```

All coefficients, weights, Gram identities and ranks are exact rational calculations. Prerequisites are recomputed; only the new checker's receipt is written, and `--check` is read-only.
