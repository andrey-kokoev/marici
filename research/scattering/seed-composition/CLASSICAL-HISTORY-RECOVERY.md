# Classical success histories do not guarantee deterministic logical recovery

**Fourth batch, iteration 7 of 20.**

**Strength:** exact classically flagged recovery condition, complete early-history enumeration and positive-probability reference witness. Not implemented recovery or a no-go for coherent apparatus access.

[Previous information channel](RECYCLING-INFORMATION-CHANNEL.md) · [Checker](check_classical_history_recovery.py) · [Receipt](results/classical-history-recovery.v1.json)

## 1. Fresh recovery criterion

Consider a known plus or known minus logical doublet, an otherwise unknown logical state and a classical successful-history label h. The flagged channel is

    sum_h |h><h| tensor K_h X K_h*.

Exact deterministic code recovery requires

    P_code K_h* K_h P_code=lambda_h P_code

for every history. This is the classically flagged Knill–Laflamme condition: different flags have orthogonal outputs. In the present two-dimensional code/output setting, each nonzero scalar effect also gives a history-conditioned unitary inverse. A zero effect means that history cannot occur on the code.

Knowing a branch label does not undo a state-dependent branch probability. This condition tests deterministic recovery without a prior logical-state promise, including preservation of an entangled reference.

## 2. Early successes and the first obstruction

The fixture retains cos(epsilon)=99/101 and sin(epsilon)=20/101. In aligned logical frames, each corrected failure branch has plus scalar k_g and minus unitary S_g,minus, before its controller-preparation amplitude:

    k_central=2/5,
    k_half=sqrt(19)/5.

Immediate success has scalar effect on plus and zero effect on minus. All eighteen second-attempt successful histories have scalar effects on both codes.

For failures g then h followed by success at attempt three, the unscaled logical maps are

    plus:  k_g[c² k_h I-s² S_h,minus],
    minus: -i c s[k_h I+S_h,minus] S_g,minus.

Their effects include the positive controller/success factor (9/25)p_g p_h. The checker enumerates all 324 histories:

- 36 have scalar effects on both codes: the second failure h is central;
- 288 have non-scalar effects on each code: h is a half-quaternion branch.

For a half branch the Hermitian S_h,minus+S_h,minus* has eigenvalues 1 and -2, not a scalar. Both maps above therefore distinguish logical states. This is not an assertion that every early success is uncorrectable; the obstruction starts at the third attempt in this tested tree.

## 3. Positive-probability logical and reference witness

Choose a central first failure and a half-quaternion second failure. The receipt stores the chronological labels, both code effects, exact rank-one eigenprojectors and their distinct positive branch probabilities.

For a Bell-entangled code/reference input, the normalized successful branch has Schmidt weights

    lambda_min/(lambda_min+lambda_max),
    lambda_max/(lambda_min+lambda_max),

which are unequal. Its squared concurrence is 4 lambda_min lambda_max/(lambda_min+lambda_max)²<1. A unitary on the output cannot repair these Schmidt weights. More generally the flagged recovery criterion excludes deterministic exact recovery of the full unknown code from classical history access.

The selected witness is invertible on each code. This leaves a possible heralded inverse filter, but not a probability-one inverse.

## 4. Probability cost cannot be hidden in the remaining histories

For a successful branch effect G_h, a branchwise uniform exact inverse can accept at most lambda_min(G_h) of the original input probability. Code completeness gives

    sum_h tr(G_h)/2=1.

The exhibited leaf has lambda_max>lambda_min. Hence even optimizing every other branch gives a strict global upper bound

    uniform branchwise inverse success
      <=1-[lambda_max(G_witness)-lambda_min(G_witness)]/2<1.

The receipt records this bound on each doublet. It applies to the stated classical branchwise heralded exact-inverse class, not to arbitrary coherent control of the full dilation.

## 5. Coherent dilation remains a different access model

The preceding coherent output/history dilation is still an isometry. The new obstruction concerns histories made classical, with the measurement environment unavailable. Classical flags can reveal logical-state information without giving reversible access to the coherences that retain it globally.

It does not follow that a laboratory can access or invert the full coherent apparatus. Nor does retaining classical files supply that capability. Both a coherent undoing and heralded filters require explicitly declared controls and records.

## 6. Next retained inverse-filter test

Construct optimal heralded inverse filters for this witness, keeping their own failure Kraus operators and Bell-reference outputs. Verify completeness and the probability cost. Compare that conditional inverse with a coherent undoing of the dilation without claiming physical implementation.

Root outcome remains null. Shared sources, historical receipts, atlas and formal contracts are unchanged. No physical preparation, spin, annihilation or photon output is admitted.

## Reproduce

```sh
python research/scattering/seed-composition/check_classical_history_recovery.py
python research/scattering/seed-composition/check_classical_history_recovery.py --check
python research/scattering/seed-composition/check_seed_composition_net.py
python research/scattering/low-energy/check_low_energy_net_v3.py
```

Predecessor channels and native actions are freshly recomputed. Exact quadratic-extension arithmetic checks every early successful-history effect and the reference witness. The flagged recovery theorem and infinite-history bound are explicitly scoped mathematical arguments, not new machine-formal or physical admission.
