# Optimal heralded history inverses retain a rank-one failure

**Fourth batch, iteration 8 of 20.**

**Strength:** exact inverse Kraus construction, completeness, optimal probability and reference recovery for the witnessed branches. Not physical implementation or deterministic recovery.

[Previous classical-history gate](CLASSICAL-HISTORY-RECOVERY.md) · [Checker](check_heralded_history_inverse.py) · [Receipt](results/heralded-history-inverse.v1.json)

## 1. Fresh witnessed inverse

Use the preceding positive-probability third-attempt history, separately on a known plus or known minus logical code. Its invertible successful map is K, with

    G=K* K=lambda_min Pi_input,low+lambda_max Pi_input,high,
    0<lambda_min<lambda_max.

The optimal uniformly exact inverse-success operator is

    N=sqrt(lambda_min) K^{-1}.

The checker reconstructs K, verifies its two-sided inverse exactly and checks

    NK=sqrt(lambda_min)I2.

Thus accepted recovery restores every unknown state on the known logical code, including all correlations with an arbitrary reference. Knowing the code is an input; its physical frame embedding and associated controls are not inferred from this two-dimensional logical inverse.

## 2. Complete filter with retained failure

Let Pi_output,high=K Pi_input,high K*/lambda_max. Define

    F=sqrt(1-lambda_min/lambda_max) Pi_output,high.

The exact effects are

    N* N=Pi_output,low+(lambda_min/lambda_max)Pi_output,high,
    F* F=(1-lambda_min/lambda_max)Pi_output,high,
    N* N+F* F=I2.

Composing with the original successful history retains both new outcomes:

    (NK)*(NK)=lambda_min I2,
    (FK)*(FK)=(lambda_max-lambda_min)Pi_input,high.

Their sum is G, not identity: this is recovery within one original history leaf. Other original histories and their terminal failures are not silently discarded.

The receipt stores both filter Kraus matrices with positive factored scalar-root prefactors and exact prefactor squares. All inverse, projector and effect identities are checked over the prior exact field extended by sqrt(19), without fitting numerical roots or suppressing new radical inputs.

## 3. Probability and reference cost

Contraction N* N≤I forces uniform original-input acceptance at most lambda_min; the construction saturates this bound. Acceptance conditional on the original history is state dependent:

- low-eigenstate input: inverse success probability one;
- high-eigenstate input: lambda_min/lambda_max;
- Bell input: 2lambda_min/(lambda_min+lambda_max).

On inverse success the Bell state is restored exactly. On inverse failure it has Schmidt rank one, with original-input failure probability (lambda_max-lambda_min)/2. This rank-one conditional output cannot recover an arbitrary entangled input using only local operations and classical failure history. Retrying such a collapsed branch does not undo the collapse.

This is not loss of information in a fully coherent apparatus description. It is a limitation of the stated classical-flag access model; coherent records/environment must be included for the larger reversible dilation.

## 4. Coherent undoing is a different operation

The full original success/history dilation remains isometric and has a mathematical left inverse on its range. Accessing that inverse requires the joint system, coherent histories, measurement apparatus/environment and inverse controls. A finite-depth circuit undoing must also retain its terminal failure branch; an eventual-success limit is not a finite pulse sequence.

The existence of such an inverse is not evidence that a device can access it. Classical recorded labels are not equivalent to those coherent degrees of freedom.

## 5. Next flag-dilation gate

Construct an explicit two-outcome ancilla dilation of the optimal filter. Factor its attenuation into a controlled flag rotation and its success unitary into polar undoing. Check gauge-compatible extensions and compare coherent uncomputation with measuring the flag, retaining both outcomes and control obligations.

Root outcome remains null. Shared sources, historical receipts, atlas and formal contracts are unchanged. No physical preparation, spin, annihilation or photon output is admitted.

## Reproduce

```sh
python research/scattering/seed-composition/check_heralded_history_inverse.py
python research/scattering/seed-composition/check_heralded_history_inverse.py --check
python research/scattering/seed-composition/check_seed_composition_net.py
python research/scattering/low-energy/check_low_energy_net_v3.py
```

Predecessor channels are freshly recomputed. Exact square identities verify positive-root Kraus prefactors and reference recovery. Optimality and coherent-access statements are explicitly scoped mathematical arguments, not new machine-formal or physical admission.
