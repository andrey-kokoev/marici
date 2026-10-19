# Nonorthogonal pointers admit an eraser, with pointer-dependent phase control

**Fourth batch, iteration 13 of 20.**

**Strength:** exact partial-pointer readout, phase feedback and heterogeneous-copy accounting. Not measured pointer parameters or physical control implementation.

[Previous basis classification](ERASER-BASIS-CALIBRATION.md) · [Checker](check_partial_pointer_eraser.py) · [Receipt](results/partial-pointer-eraser.v1.json)

## 1. Fresh pointer-relative readout

The partial-copy model has real pointer states

    e0=|0>, e1=gamma|0>+v|1>,
    gamma,v>=0, gamma²+v²=1.

An orthogonal-pointer X readout is generally biased for this actual pair: its flag-one amplitudes are (gamma±v)/sqrt(2), while flag zero gives 1/sqrt(2). Equal outcome probabilities occur only when gamma*v=0 in this real family.

Instead use the Y-basis readout rows

    (1,-i)/sqrt(2), (1,i)/sqrt(2).

Flag-one amplitudes relative to flag zero are gamma-i*v and gamma+i*v, each of unit modulus. Feed back their conjugates onto flag one. Each corrected label then gives exactly the same scalar amplitude on both flag branches; applying W* restores the prefilter input and arbitrary reference.

Both labels have probability one half, independent of input. They are not which-flag records. The checker verifies actual overlaps for gamma=0,3/5,4/5,1, including the failure of X unbiasedness for the interior cases. All quantities are exact, not numerically fitted phases.

## 2. Heterogeneous copies remain explicit

For several partial pointers, Y readout on each addressed copy contributes a uniform amplitude and a unit-modulus relative phase. The flag feedback is the conjugate product of those phases. Every addressed label string remains recorded with probability 2^(-m).

Unaddressed copies carry the tensor-product states e0,remaining and e1,remaining. Their overlap is

    Gamma=product gamma_j.

The checker constructs every remaining pointer-word amplitude explicitly and verifies normalization. After flag/polar undoing, their reduced disturbance is

    coherence=r²+(1-r²)Gamma,
    Bell fidelity=[1+r²+(1-r²)Gamma]/2,
    terminal flag-one effect=2r²(1-r²)(1-Gamma)Pi_high.

Mixed four-pointer and three-pointer families are checked for every access subset on both inverse-filter cases. Active, inactive, readout and terminal records are all accounted for.

Thus the number of remaining copies alone is not decisive. Identical-state pointers (gamma=1) carry no distinguishing information and are harmless even if unaddressed. Any remaining distinguishable pointer in this real family makes Gamma<1 and leaves disturbance. The earlier “one remaining copy obstructs” result was correctly scoped to orthogonal outcome copies.

## 3. Parameters and access are still inputs

The phase feedback uses the actual gamma and v. Supplying an exact Y basis does not by itself supply those pointer-dependent phases. Readout labels, apparatus access, a phase reference and feedback controls remain added resources, not native Hamiltonian dynamics.

This only restores the state entering the inverse-filter interaction. Earlier state-dependent successful-history measurements are not undone. Input-independent eraser labels remain distinct from a retained readable which-outcome record.

## 4. Next calibration-information gate

Use feedback computed from an incorrect pointer pair and calculate the actual residual channel. Determine whether the retained Y labels can identify gamma, or whether independent calibration probes or coherent inverse-copy access are needed. Keep calibration data and phase/control costs separate from unknown-state recovery.

Root outcome remains null. Shared sources, historical receipts, atlas and formal contracts are unchanged. No measured physical noise, preparation, spin, annihilation or photon output is admitted.

## Reproduce

```sh
python research/scattering/seed-composition/check_partial_pointer_eraser.py
python research/scattering/seed-composition/check_partial_pointer_eraser.py --check
python research/scattering/seed-composition/check_seed_composition_net.py
python research/scattering/low-energy/check_low_energy_net_v3.py
```

Predecessor basis tests are freshly recomputed. Exact root-mask arithmetic verifies the retained joint maps and reduced channels in the output spectral frame. General pointer-product and reference identities are explicitly scoped mathematical arguments, not new formal or physical admission.
