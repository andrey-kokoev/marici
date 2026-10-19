# Extension turn3: uncertainty on a joint retained WG ensemble

## Fresh objective and admitted uncertainty

The mutable net has56 nodes and two open extensions. This turn addresses `uncertainty-budget-binding` on the actual checked common-witness assembly. It does not invent uncertain physical acquisitions or identify ideal depth with uncertainty.

The caller supplies three possible gain histories with equal probabilities1/3:

- x: gains2/3 then3/5;
- y: gain2/5;
- z: gain3/4.

Each alternative contains a complete validated Assembly: relation source/cuts/action, energy field, context, policy/reference, comparison filler and predecessor history. This ensemble expresses uncertainty about which admitted history occurred. It is NOT uncertainty about arbitrary unknown marked sources; the source fixture remains fixed. The labels and prior are supplied statistical assumptions, not inferred frequencies.

The same alternative label determines ALL packet fields. No independent marginal re-boxing of energy, relation and context is allowed. Shared subsequent drift/gain commands act on each complete alternative and retain its predecessor.

## Exact task-relative balance law

For two independent draws from the supplied finite prior p_s, define

    B = Pr(alternative labels differ) = 1 - sum_s p_s²,
    D = Pr(observer readouts differ) = 1 - sum_y p_y²,
    R = Pr(labels differ but readouts agree) = sum_y p_y² - sum_s p_s².

Here p_y is the total probability of each actual observer fiber. Thus B=D+R, R>=0. R measures unresolved ambiguity relative to that observer; D measures observable distinctions. These are collision-pair quantities, not Shannon entropy, radius or physical variance.

For deterministic transport with fixed prior and retained alternative identities, B is unchanged and deltaD=-deltaR. This is an exact partition/bookkeeping identity, NOT an independently discovered physical conservation principle. Conditioning, merging alternatives, or stochastic dynamics would change the assumptions and require a new law.

The task observer retains the four separate prior assembly readouts as a tuple: energy, comparison residual, relation matrix and formal source detector. A separate history observer reports the retained command word. They are not conflated.

| Case | B | D | R |
|---|---:|---:|---:|
| initial task observer | 2/3 | 4/9 | 2/9 |
| initial history observer | 2/3 | 2/3 | 0 |
| after shared drift, half gain and zero gain; task observer | 2/3 | 0 | 2/3 |
| same final ensemble; history observer | 2/3 | 2/3 | 0 |
| initial prior conditioned on{x,y}; task observer | 1/2 | 0 | 1/2 |

The zero-gain readout collapse does not erase any possible retained history. Every source cut/action and context filler remains checked inside each alternative. Equal x/y task readouts are not permission to replace one complete history with the other. No claim is made that these task-equivalent histories become distinguishable by a later command under the same task family; they remain distinguishable by the declared history task.

## Scalar-square compatibility and changed assumptions

The checker instantiates the owner's exact scalar source/observer square with source scales(2,3), observer scales(5,7), tighter source budget and narrower readings. The portable verifier accepts both routes. An individually valid but noncommuting edge is rejected. This preserves the owner's restricted theorem rather than asserting it automatically transports all source-algebra attachments.

A positive rescaling of the energy observer leaves its ensemble partition unchanged. An interval radius epsilon scaled by b pulls back as(b epsilon)/b=epsilon. Changing units is not free precision.

Explicit conditioning retains the old ensemble and evidence labels, normalizes the chosen probabilities, and changes B. Empty evidence returns no feasible ensemble, not a fictitious zero-uncertainty state. Refinement is therefore distinct from fixed-prior transport.

## Validation and negative controls

Ensemble validation reconstructs each actual complete state from the admitted initial history and shared commands. It checks all attachment equations and parent/probability/evidence relations. Unchanged state validations are cached only with exact repr snapshots including mutable maps, not merely object identity.

Five package/ensemble hostiles fail: independent energy/relation re-boxing, erased cut attachment, equal-readout history substitution, conditioned probabilities without evidence, and stale/missing comparison filler after transport. The separately rerun scalar test also rejects its noncommuting square.

## Verification and disclosed execution repairs

    uv run --with sympy python research/strominger/checkers/check_wg_uncertainty_budget.py

Six checks and five ensemble hostiles pass. Receipt: `research/strominger/results/wg-uncertainty-budget-v1.json`.

The initial attempt to run the owner's full scalar suite failed because its saved physical-model input `research/nima/results/diagonal-task-example-problem.json` is absent from this checkout. The final checker instantiates the available synthetic finite square using the unchanged owning functions and verifier; it does NOT claim the absent physical-source case ran. A subsequent run timed out from repeated full-history recomputation; exact unchanged-state snapshots and cached deterministic reconstruction reduced redundant work, and the final complete run passed. No owner implementation changed, no fresh Agda theorem claimed.

## Disposition

`uncertainty-budget-binding` is constructed at this finite task-relative joint-history scope. The law explicitly retains conditional dependence, residual ambiguity and supplied prior assumptions while checking actual WG attachments. It does not establish universal uncertainty conservation, uncertain calibration/dynamics, continuous set-volume conservation, arbitrary source-ideal filtration transport or physical repeated-acquisition statistics.

One extension remains: whole-package half-step. The four-extension objective is not yet complete.
