# Pulse-area errors and doublet coupling have different retry consequences

**Fourth batch, iteration 5 of 20.**

**Strength:** exact history-averaged calibration channel, coherent doublet-coupling fixture and uniform retry bound. Not a physical noise measurement or lossless arbitrary-input preparation.

[Previous continuous control](SELECTOR-CONTINUOUS-CONTROL.md) · [Checker](check_selector_pulse_errors.py) · [Receipt](results/selector-pulse-errors.v1.json)

## 1. Fresh area-error calculation

Assume the same pulse-area error delta on the sixteen noncentral feedback branches, leaving the two identity branches unchanged. The residual rotation on each active plus branch is exp(-i delta J_g). The exact axis identities are

    mean J_g=0,
    mean J_g X_plus J_g=(2 tr(X_plus)P_plus-X_plus)/3.

Using the actual branch weights yields

    Phi_delta(X_plus)
      =[16/25-(304/375)sin²(delta)]X_plus
       +(152/375)sin²(delta)tr(X_plus)P_plus.

The normalized failure channel has Bloch factor 1-(19/15)sin²(delta). Sector weights and eventual success probability remain unchanged: retries select only the initial plus weight.

Pooling eventual successes gives the reduced plus Bloch factor

    L(delta)=135/[135+304 sin²(delta)].

For pure plus input the pooled fidelity is (1+L)/2, with infidelity (152/135)delta²+O(delta^4). Three rational cosine/sine fixtures verify the channel directly on an operator basis, alongside the exact symbolic axis identities. This common-area model is not an assertion about arbitrary correlated, axis or gauge-breaking errors.

A reduced channel ignores controller histories for statistics; it does not delete them. Known branch rotations can still be corrected with further controls.

## 2. Full corrected failure channel, including cross-sector coherence

To compare a sector-mixing perturbation, the checker reconstructs the corrected Kraus branches on both doublets. Their complete channel is verified on sixteen matrix units:

    plus block:  (16/25)X_plus,
    minus block: (1/5)X_minus+(2/5)tr(X_minus)P_minus,
    cross block: [(2-sqrt(19))/25]X_cross.

The cross factor matters. Replacing this channel with a classical two-sector Markov process would silently insert a sector dephasing operation. None is inserted here.

## 3. Explicit ground-doublet coupling

Exact orthonormal frames U_plus and U_minus define

    B=U_plus U_minus*+U_minus U_plus*.

This Hermitian unitary obeys B²=I and BQ+QB=0. After every corrected failure apply the additional unitary

    V_epsilon=cos(epsilon)I-i sin(epsilon)B,
    cos(epsilon)=99/101, sin(epsilon)=20/101.

This couples the two doublets **inside the four-dimensional ground**. It is not leakage into the twelve-dimensional excited complement, nor a native interaction. A ground-unitary extension can preserve Gauss by acting as identity on all other physical states and gauge sectors; that existence argument is not device synthesis.

One-step failure effects stay unchanged because V is unitary. Later retry effects do change. Initially minus input has second-attempt success probability (9/25)sin²(epsilon). Full coherent finite-depth effects, not only sector populations, are retained in the receipt.

## 4. Uniform bound establishes eventual success, not lossless encoding

Write c=99/101, s=20/101 and t=(2-sqrt(19))/25. The checker verifies the two-step success effect

    S_2=(9/25)[(1+16c²/25)P_plus+s²P_minus
               +i c s t(BP_plus-P_plus B)].

The Hermitian off-diagonal operator i(BP_plus-P_plus B) has norm one. Since |t|<1/10,

    S_2 >= kappa I,
    kappa=(9/25)(s²-cs/10)=1818/255025>0.

Therefore all-failure effects after 2n attempts are bounded above by (1-kappa)^n I. The eventual-success effect is identity for this declared fixture. Histories and unsuccessful finite-time branches remain records throughout.

This is a changed control protocol, not a repair derived from the original Hamiltonian. Unit eventual success into a rank-two output does not establish preservation of arbitrary rank-four input information. The reduced logical channel, reference correlations and retained history must be examined next.

## 5. Next information-retention test

Compute the input-to-success channel of the declared recycling fixture, including a reference-system witness. Determine whether it preserves encoded information or is a lossy reduced preparation, and identify the distinguishing input information in the joint output/history. Do not equate unit success probability with a reversible state transfer.

Root outcome remains null. Shared sources, historical receipts, atlas and formal contracts are unchanged. No measured noise, physical spin, annihilation or photon output is admitted.

## Reproduce

```sh
python research/scattering/seed-composition/check_selector_pulse_errors.py
python research/scattering/seed-composition/check_selector_pulse_errors.py --check
python research/scattering/seed-composition/check_seed_composition_net.py
python research/scattering/low-energy/check_low_energy_net_v3.py
```

The prerequisite control construction is freshly recomputed. Exact arithmetic verifies axis moments, direct channels and coherent finite-depth effects. Geometric limits, the operator bound and the gauge extension are stated mathematical arguments, not new machine-formal or physical admission.
