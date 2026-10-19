# Physics programme: reviewed control contributions, iteration 1

## Decision

Accept four scoped contribution interfaces for the central physics programme:

| Contribution port | Source and preserved structure | Central use |
|---|---|---|
| `control.wg.fixed-composite-history` | Fixed refinements F,G; actual dependent history/edge witnesses; inverse and concatenation laws | Source/event identity and retained-history comparison |
| `control.energy.exact-feedback` | Nonnegative (a,b), admitted gains, exact mathematical readings and updated-state probing | Predictive quotient and feedback reference model |
| `control.context.capability` | Full authority/resource context; externally supplied grant/replenish events | Enabled-continuation and context policy interface |
| `control.optical.statistical-feedback` | Coherent two-mode source, fresh loss/tap ports, count histories and Gamma preparation information | Conditional physical-theory realization with explicit statistical observation and resource maps |

The machine-readable review is [physics-control-contribution-review.v1.json](contracts/physics-control-contribution-review.v1.json). It records source IDs, maps, consumers, assumptions and remaining comparison requirements. The central `review-control-contribution` task is complete at this scope. Child-net transition proposals remain separate records.

## Freshly inspected state

Sontag's optical successor now assembles its conditional statistical theory and defers `empirical-optical-realization` pending independent apparatus evidence. Its current frontier is empty. The earlier report naming calibration construction as the next task is superseded by this current contract.

The original exact-energy reader and the statistical tap/count reader have distinct event signatures. The optical successor records attenuation and conditional information updates. That distinction must survive the source register.

## Mathematical interface review

The common event dictionary has explicit initial context/task, admitted payloads, state update, observations and resource effects. WG generation, control choices and external context events have different roles.

For fixed F,G, the Agda module `RetainedHistoryTransport` maps the actual `TypedGeneratorLayers.Histories` constructors by `flatten-edge` and `unflatten-edge`. Its inverse and join proofs recurse on the history constructors, retaining intermediate states and actual witnesses. The `next-square` and `edge-square` use the fixed `Composite` definitions. Source tasks and observers transport at these specified types.

The energy quotient uses the admitted gain vocabulary. Gain composition acts on components by `(q r)^2 a, (q r)^4 b`; provenance keeps the distinct event traces. Full contexts distinguish grant/replenish continuations even where current enabled-action observations agree.

The marked relation-algebra attachment remains a separate source comparison. Its nonsplit module structure supplies a control against forgetting source action. The fixed Composite proof does not provide a map to that module.

## Optical primitive and history comparison

The optical source includes two equal-frequency coherent amplitudes, their phases, fresh ancillary inputs, preparation context and outcome history. Let `f_i` be current survival factors relative to the initial occupations.

- Gain q multiplies amplitudes by q and q², hence occupations by q² and q⁴. Each complementary loss port retains the missing occupation.
- A modewise tap sends fractions `1-tau`, `eta*tau`, `(1-eta)*tau` to surviving, counted and unobserved outputs. They sum to one.
- A count event contributes exposure `c_i=eta*tau*f_i` using the pre-tap factor. Gamma shape/rate update by the recorded count and this exposure. Current moments then use the updated survival factor.
- An adaptive gain determined by public history is fixed when conditioning on that history. Both realizations therefore apply the same primitive square.

These one-event state/resource/likelihood identities compose by finite-history induction. They supply the reviewed comparison vocabulary. The coupling Hamiltonian and physical-time context in Sontag's assembly are supplied optical framework data; the register must label them accordingly.

## Independent tests and a vocabulary-extension counterexample

A new Nima checker implements rational amplitude replay and occupation/information replay separately. Four event prefixes compare signal state, loss accounting and count means. It also checks accumulated pre-tap exposures, a public-count adaptive policy, gain composition, fresh-vacuum dependence and the equal-H continuation witness.

The phase-sensitive extension control is exact. Coherent amplitude pairs

`(1,1)` and `(1,-1)`

have the same occupation state `(1,1)`. A balanced mixing of the two signal modes gives occupation outputs `(2,0)` and `(0,2)`, respectively; both retain total occupation 2.

The reviewed vocabulary contains modewise loss/gain/tap operations. Adding inter-signal interference requires a phase-sensitive state or an explicitly restricted task quotient. This is a concrete acceptance test for any enlarged physical event dictionary.

The checker independently recomputes the interval certificate. For posterior shapes 100000, rates in `[99900,100100]`, surviving factors 1, target `h=5/16`, tolerance `h/4` and risk `1/20`, gain interval `[499/1000,501/1000]` certifies; `[2/5,3/5]` abstains. The systematic bias term is retained. Exact corner tests corroborate the monotone all-box inequalities used by the written theorem.

## Evidence review

Fresh verification completed:

- 27 independent rational checks;
- read-only verification of both source review-manifest hash maps;
- formal receipt/compiler/source freshness across 2193 declared inventory entries;
- six deliberately corrupted formal receipts rejected.

The compiler and Sontag's result-writing suites were not rerun. The review checker writes only `research/nima/results/physics-control-contribution-review-v1.json`. It records the source hashes and all exact control results.

Command:

```sh
python research/nima/checkers/check_physics_control_contribution_review.py
```

## Handoff to iterations 2 and 3

The source register should use four distinct IDs from the review contract. In particular, `energy.gain-exact-reader.v1` and `optical.coherent-gamma-tap.v1` are related by a versioned change of event vocabulary, not an identity of instruments. Classify Gamma preparation, coherent/Poisson laws, vacuum/frequency assumptions and calibration boxes by their actual provenance.

For target selection, the optical statistical candidate now has a concrete state/action/observation comparison and conditional error budget. It can be compared with the existing finite-memory detector and cavity models on specified observation and resource interfaces. Acquired apparatus records and preparation/calibration evidence remain named inputs to the empirical branch.
