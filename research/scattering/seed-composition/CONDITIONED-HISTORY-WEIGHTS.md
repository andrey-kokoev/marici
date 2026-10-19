# Conditioning native choices changes the history metric; controller-only normalization is additional

**New batch, iteration 8 of 10.**

**Strength:** exact source composition tests, six-horizon retained trial accounting and a rational survival transfer. Not a physical probability law or derived conditioning operation.

[Previous history lift](RETAINED-EVENT-ARC-LIFT.md) · [Checker](check_conditioned_history_weights.py) · [Receipt](results/conditioned-history-weights.v1.json)

## 1. Fresh comparison

The predecessor-preserving controller-arc lift is lossless with a positive fiber metric. Its weights were normalized over allowed controller arcs, not over all native primitive extensions. This turn compares those domains explicitly.

For each of the eighteen controller contexts, let m be its native outgoing primitive count and d the allowed controller-target count after executing the expected primitive. Four contexts have m=1; fourteen have m=2. Controller target counts are also one or two, but are not the same choice as native primitive selection.

The checker calls the actual native `RetainedSuccessorLedger` with the ten primitive registry. For every context, it composes an incoming path with neutral, accepted and rejected primitive payloads. Full, accepted and rejected families have identical retained word slots; accepted plus rejected coefficients recover full extension. The masks are still registered as **supplied**.

## 2. The two weight assignments differ

Native equal-copy extension divides a parent weight among m available primitives. Retaining the accepted primitive gives weight 1/m of the parent, while rejected primitives retain (m-1)/m. If the accepted coefficient is subsequently copied into d controller targets, each accepted arc has inherited weight

    native then conditioned: 1/(m*d).

The controller-only construction from the previous turn uses

    allowed controller domain: 1/d.

It therefore resets the accepted norm by a factor m at every step. Across an accepted history,

    w_controller / w_native = product of m(context).

The coefficients need not change: this is a change of metric. If one holds the native metric fixed instead, matching the controller norm would require amplitude gain sqrt(product m). Neither that gain nor metric reset is source-derived.

The controller-target split itself remains supplied dictionary/control structure. It must not be counted as a second native primitive choice.

## 3. Retain first-reject histories

For each initial controller state, the checker enumerates accepted event histories through six depths. On the first rejected primitive, it retains the full accepted arc prefix, rejected primitive word and context, then stops that control trial.

These stopped prefixes represent first rejection; the test does not enumerate every subsequent unrestricted rejected continuation. Their retained primitive words can still be continued in the native ledger. No rejected coefficient is silently reassigned to the accepted branch.

At every tested depth:

    accepted inherited weight + all first-reject weight = 1,
    controller-only accepted weight = 1.

Accepted history counts are 26, 34, 48, 64, 88, 120. Cumulative first-reject record counts are 14, 36, 64, 104, 156, 228. Every accepted primitive word is checked endpoint-sewn, and the history-weight ratio is checked individually.

These are rational counting weights, not derived probabilities. For a coefficient x at an initial state, the corresponding weighted norm contributions scale by x squared.

## 4. Conditioning is generally not one scalar on the selected plane

Let q_n(s) be the accepted inherited weight at depth n from initial context s. On the boundary-initialized synchronized frame E, the accepted input pullback is

    G_n = E^t diag(q_n) E.

Its input counting Gram is G_0=[[9,1],[1,1]]. At depth one,

    G_1=[[19/4,3/4],[3/4,3/4]],

which is not a scalar multiple of G_0. The same nonproportionality holds at tested depths two, four, five and six. Thus a single scalar normalization cannot generally restore the initial plane's metric; it changes relative mode-direction weights.

There is an important exact exception at depth three:

    G_3=(7/32)G_0.

The checker pins this exception rather than asserting failure at every horizon. This finite exception is not an all-depth normalization theorem or a physical three-step return.

## 5. Exact survival recurrence

The finite enumeration is independently checked against the rational backward transfer

    q_0=1,
    q_(n+1)(s) = sum_target q_n(target)/(m(s)*d(s)).

The receipt contains its eighteen-by-eighteen matrix K. Reflection preserves m and d, hence q_n is reflection-invariant. Symmetry preserves odd parity under diagonal survival weighting, but does not force that weighting to be scalar on the selected plane.

Forced native contexts can have survival one for more than a single step. The checker does not assume immediate strict contraction everywhere; long-horizon decay requires an actual transfer analysis.

## 6. Result and next gate

Selecting first and renormalizing over allowed controller histories differs from extending over all native choices and retaining accepted/rejected records. The difference is an explicit context- and history-dependent reset, not an invertible coordinate change or a derived physical gain.

Next analyze K exactly: certify long-horizon survival decay and any conditioned limiting profile, distinguishing a reweighted control law from physical clock or scalar normalization. The full retained record remains available alongside that observer analysis.

The scientific root remains null. Physical normalization, prepared odd inputs and controller authorization are not derived; pinned work-net and downstream contracts remain unchanged.

## Reproduce

```sh
python research/scattering/seed-composition/check_conditioned_history_weights.py
python research/scattering/seed-composition/check_conditioned_history_weights.py --check
python research/scattering/seed-composition/check_retained_event_arc_lift.py --check
python research/scattering/seed-composition/check_seed_composition_net.py
python research/scattering/low-energy/check_low_energy_net_v3.py
```

All coefficients, history weights, matrices and identities use exact rational arithmetic. Prerequisites are recomputed; only the new receipt is written. `--check` compares read-only.
