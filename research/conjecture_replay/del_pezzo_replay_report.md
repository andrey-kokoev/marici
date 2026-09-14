# Del Pezzo entrance replay: final report

## Question

Could a costed four-outcome conjecture-resolution machine, frozen when the global del Pezzo surface was first reconstructed, have selected the productive route toward the physical readout?

## Frozen origin and holdout

The origin is the hash-frozen `global_del_pezzo_double_cover.json`. Eight entrance-admissible conjectures were reconstructed from that result and four older packets. Forty-five later result packets form the holdout.

The historically realized programme was

\[
DP1^{++}\to DP2^{++}\to DP4^{++}\to DP5^{++}\to DP6^{++},
\]

namely: split-fiber pencil, source \(e_6\) placement, primitive closure, pairing geometry, and physical integral readout.

## Model 1: independent guarded action quiver

The first model retained 5,900 provenance-distinct simple policies and assigned uniform four-way outcome probabilities. Every cost/risk objective chose a direct `DP6` physical experiment. Historically `DP1` was first and ranked fifth under this model.

The failure is structural: the model treated raw executability as terminal interpretability. Earlier geometric work could only add cost because it could not change the meaning of a later physical observation.

## Model 2: hypothesis-conditioned interpretation state

The minimal reconstructed state has four interfaces:

\[
M=\text{global marking},\quad
E=\text{source }e_6\text{ placement},\quad
L=\text{integral normalization},\quad
P=\text{mod-two labels}.
\]

A raw favorable `DP6` observation reaches the declared readout only under

\[
M\land E\land L\land P.
\]

With success-first policy valuation, the balanced uniform expected policy and the robust credal policy both choose `DP1`, matching history. The optimistic policy chooses `DP2`; minimax correctly reports zero guaranteed success because unfavorable four-way outcomes can prevent readiness.

For the balanced scenario:

- expected policy: `DP1`, readout probability `0.001708984375`, expected action cost `30.044921875`;
- credal-worst policy: `DP1`, lower readout probability `6.09375e-7`;
- optimistic policy: `DP2`, a successful branch exists;
- minimax: no policy guarantees readout.

The tiny probabilities reflect the deliberately uninformative independent \(1/4\) outcome model, not empirical scientific odds.

## What the replay establishes

1. A provenance quiver can exactly preserve and enumerate the finite conjecture policy space.
2. Costs and probabilities alone do not value foundational discoveries.
3. Information has operational value only through a typed hypothesis/interface state that changes which later observations count as terminal answers.
4. Under the reconstructed interface, expected and robust selection recover the actual first move.
5. The historical route is better characterized as construction of an observation language than as a detour before measurement.

## Limits

The coupling was reconstructed after reading the holdout, so recovery of `DP1` is retrospective evidence, not prospective validation. The next valid test must freeze `M,E,L,P`-style interfaces in a new unexplored programme before outcomes are known. The snapshot uses filesystem order rather than a Git or ledger-head historical commit, costs are ordinal/static proxies, and unrecorded historical conjectures may be absent.

## Reproducibility

All executable stages and result packets live in `research/conjecture_replay/`. The closure certificate is `results/del_pezzo_final_audit.json`.
