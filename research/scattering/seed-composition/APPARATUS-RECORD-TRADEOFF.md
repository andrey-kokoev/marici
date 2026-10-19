# Apparatus distinguishability trades against local undo fidelity

**Fourth batch, iteration 10 of 20.**

**Strength:** explicit unitary pointer copying, retained joint maps, reduced-channel and record-information tests. Not a physical apparatus or arbitrary readout recovery no-go.

[Previous flag dilation](INVERSE-FLAG-DILATION.md) · [Checker](check_apparatus_record_tradeoff.py) · [Receipt](results/apparatus-record-tradeoff.v1.json)

## 1. Fresh pointer model

Supply a neutral two-state apparatus initially |0>. Flag zero leaves it in e0=|0>; flag one applies the unitary

    [[gamma,-v],[v,gamma]],
    e1=gamma|0>+v|1>, v=sqrt(1-gamma²).

Use real 0≤gamma≤1, or compensate a known relative pointer phase. This is copying an orthogonal flag basis through a controlled unitary, not cloning an arbitrary unknown state.

Apply the inverse-filter dilation W, copy the flag, then apply W*. Its success-controlled polar factors commute with the copy and cancel. Write H=Pi_output,high, L=I-H, r²=lambda_min/lambda_max and s²=1-r². The retained joint system maps, ordered by terminal flag and apparatus coordinate, are

    (0,0): L+(r²+gamma s²)H,
    (0,1): v s² H,
    (1,0): rs(gamma-1)H,
    (1,1): rs v H.

Their squared amplitudes sum to identity. The apparatus and terminal flag remain joint records; reduction for statistics is not their physical erasure. Exact tests cover gamma=0,3/5,4/5,1 on both witnessed codes.

## 2. Quantitative undo/record tradeoff

The reduced local-undo channel preserves eigenstate populations and multiplies low/high coherence by

    lambda=r²+(1-r²)gamma.

A Bell input/reference probe therefore has fidelity F=(1+lambda)/2. The retained terminal flag-one effect is 2r²(1-r²)(1-gamma)H.

For the two pure conditional pointer states, equal-prior distinguishability is

    D=sqrt(1-gamma²),
    optimal guessing probability=(1+D)/2.

Thus, with the stated phase convention,

    F=1-(1-r²)[1-sqrt(1-D²)]/2.

Identical pointers permit perfect local undo but carry no which-flag information. Orthogonal pointers give the previous fully measured-flag disturbance. These statements concern the inverse-filter interaction, not reversal of earlier history measurements.

## 3. The record contains logical-input information

The checker explicitly traces the retained joint map. Low logical input leaves the apparatus in |e0><e0|; high input gives

    r²|e0><e0|+(1-r²)|e1><e1|.

Their trace distance is (1-r²)D. A pointer-coordinate readout has outcome-one effect

    (1-r²)v² H,

which is non-scalar for gamma<1. Consequently that classical record cannot support deterministic exact recovery of an arbitrary unknown logical state/reference. More generally, perfect reference-preserving recovery cannot leave an environment record that distinguishes those logical inputs.

Coherently undoing the copy before undoing W changes the access model and can restore the input, but removes the useful which-outcome correlation from the pointer. No coherent apparatus access or physical pulse implementation is inferred.

## 4. Not all retained labels are which-outcome records

This does not prohibit every classical label. A quantum-eraser readout can have an input-independent random label, with phase feedback correcting its branch. Such a label is not a retained readable record of the original flag outcome. That distinction must be tested explicitly rather than calling all readout “erasure” or all classical records irreversible.

Next construct an eraser-basis readout for the orthogonal-pointer fixture and verify exact reference recovery, input-independent label probabilities and the loss of original which-outcome accessibility. Include any additional copies of the outcome when assessing apparatus access.

Root outcome remains null. Shared sources, historical receipts, atlas and formal contracts are unchanged. No measured noise, physical preparation, spin, annihilation or photon output is admitted.

## Reproduce

```sh
python research/scattering/seed-composition/check_apparatus_record_tradeoff.py
python research/scattering/seed-composition/check_apparatus_record_tradeoff.py --check
python research/scattering/seed-composition/check_seed_composition_net.py
python research/scattering/low-energy/check_low_energy_net_v3.py
```

Predecessor dilations are freshly recomputed. Exact root-mask arithmetic verifies the retained maps and apparatus marginals. General tradeoff formulas, distinguishability and the information-without-disturbance argument are explicitly scoped mathematics, not new formal or physical admission.
