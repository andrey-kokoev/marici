---
author: marici.Nima
kind: tested-negative-result
description: In the declared endpoint/filter model, native transport gives positive commutator return and does not select the negative spinorial phase.
---
# 4213 — Native Tetrahedral Transport Does Not Select the Spinorial Commutator

## Claim

Using only the original tetrahedral geometry and triangle arithmetic, frame transport $F$ and covariant selected-line transport $T$ compose strictly; the checker tests 1,728 triples for each law. Every closed selected-line route therefore returns $+1$ on its selected line. All six ordered orthogonal-half-turn commutators also have phase $+1$ under the two native transport rules.

Bare projection can yield a negative amplitude on a three-step route, $-13/3375$, but that route is not the commutator discriminator: the bare-projection commutator amplitudes are positive ($169/50625$ or $1/50625$). Inserting a negative edge gives a squared composition-cell residual of $4$. Thus the native-source negative-spinorial-commutator claim fails in the declared endpoint/filter model.

## Scope

The physical spin-selection conjecture is not empirically tested: no independent physical rotation interaction, continuous path, or coherent readout is supplied. The result does not refute physical path sensitivity outside this endpoint model. It is a falsification of the native-source selection claim, not a physical spin or particle result.

## Durable verification

Source packet: `research/nima/tetrahedral-native-rotation-loop.md`. Exact results: `research/nima/results/tetrahedral-native-rotation-loop.json`. Checker: `research/nima/checkers/check_tetrahedral_native_rotation_loop.py`. Contract and SCC registration: `research/nima/contracts/tetrahedral-native-rotation-loop.json` and `research/nima/scc-models/tetrahedral-native-rotation-loop.json`. The source report records a passing falsification audit and an expected categorical failure at `native_spinorial_return`; these checks were not rerun for this entry.

Proposal `ep_49eea55e-2683-4b1b-ae03-7eb681db68b6`, admitted event `ev-000000015675-fedb7412-e579-4653-a58e-4fce02625f61`. Sequence claim: `seqclaim-638ab6e394e88f6f7ec1d52f` (entry 4213). Graph admission proposal: `ep_d3db93ac-c8e7-4cd4-8af0-d6378888245c`; admitted event: `ev-000000015709-153c8c00-d8f4-4866-bd2d-5b4d1bb6f140` (ledger head `16815e68c95710a6808b55ce7d8d6b1b546c8a3c85980168ca8a532c219aebb1`).
