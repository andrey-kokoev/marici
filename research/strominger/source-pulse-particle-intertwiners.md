# Source pulses versus current particle operations: exact intertwiner preflight

## Question tested

Can the existing six-port source exchange be mapped injectively into the current particle operation spaces while preserving every pulse and ordered source word?

This test does not invent new target generators. It compares the actual source exchange against three named existing targets: geometric source-action groups, literal L/G projection stages, and reflections formed from those complete L/G stages. It is not a classification of all primitive local or interaction operators elsewhere in the repository.

## Reconstruct the actual source action

The checker imports PACKETS from Nima's live six-arrow registry. It reconstructs the exchange formula from `check_seed_port_exchange_binding.py` exactly over the rationals, without importing that script's NumPy/SymPy replay pipeline.

For H=(10I+ones) tensor (10I+ones), each directed port has feature f_ab=e_ab/11. In the carrier-plus-six-record space,

    delta=r_i-f_i^T H y,
    y'=y+f_i delta, r_i'=r_i-delta.

Every resulting 22-dimensional E_i is a metric isometry and involution. The six columns B_i=(f_i,-e_i) span an invariant active space, with

    B^T M B=K=I+F^T H F,
    E_i B=B R_i,
    R_i=I-e_i K_i,:.

All six intertwiners and metric identities are checked exactly. The remaining 16-dimensional simultaneous fixed space is retained as a control, not mistaken for the active dynamics.

## The valid AB,BA source loop has infinite order

AB followed by BA is a composable closed source word, and repetitions remain valid histories. Its active operator is R_BA R_AB. Exact calculation gives

    trace(R_BA R_AB)=29283/14641,
    rotating-plane trace=-29281/14641.

The other four active directions are fixed. The loop's departure from identity has rank two, as does the AB/BA commutator.

A finite-order matrix has roots of unity as eigenvalues, so its trace is an algebraic integer. A rational algebraic integer must be an integer. The displayed trace is rational and nonintegral. Therefore this loop has **infinite order**, without a numerical angle estimate or finite-power search.

## Three current target comparisons

### Geometric source actions

Fresh exact vertex-action enumeration gives:

| Carrier | Generated geometric group order |
|---|---:|
| Proton | 12 |
| Neutron | 3 |
| Electron | 5 |

If an injective J obeyed J R_i=T_i J with every T_i in one of these finite target groups, the mapped AB,BA loop would have finite order. Injectivity would force the source loop to have that same finite order, contradicting the certificate above.

Thus no faithful pulse adapter into these geometric actions exists. This concerns the retained generator families, not the entire isometry group of a shape or an arbitrary new dynamics on its vertices.

### Literal coefficient stages

For an involution R and idempotent target T, J R=T J implies

    J=J R²=T² J=T J=J R.

An injective J would force R=I. Thus a nontrivial reversible source pulse cannot be identified with a literal projection stage by an injective linear map.

### Reflections of complete L/G stages

The current L and G commute. Consequently I-2L and I-2G generate an abelian group of order four for each native carrier, as checked from its nonempty joint sectors and current source-bound receipts.

Every word in those two target reflections commutes. The source AB/BA pulses do not. Therefore this alternative also admits no faithful all-pulse intertwiner.

## What the result means

The earlier canonical action is real reusable machinery, but it is not already the same dynamics as the geometric generator cycle or the coarse L/G stages. An energy attached to that action cannot be transferred merely because a return projector or carrier dimension agrees.

A successful next adapter must identify actual noncommuting target pulse operators, including dynamical records, that realize the source metric/action relations. Those might require a larger retained carrier, or might already be available among finer primitive operations; the present preflight does not decide that. Passive labels recording a history do not by themselves supply its missing linear action.

The test also preserves a positive control: the source's exact 22-to-active-6 reduction does intertwine every operation. The obstruction is not an incorrectly reconstructed source or an assertion that no intertwiners can exist anywhere.

## Verification

```sh
python research/strominger/checkers/check_source_pulse_particle_intertwiners.py
```

Nine checks passed. Complete active pulse matrices, metric, geometric permutations, target dispositions and file hashes:

`research/strominger/results/source-pulse-particle-intertwiners.json`.

The original Nima 267-control numerical replay was inspected but not freshly rerun; this checker independently verifies the exact source algebra used here. Common coefficient receipts and their bound source files were checked against current hashes. Shared scripts and stores were not modified.
