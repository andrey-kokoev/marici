# An eraser can retain random labels, but unaddressed outcome copies still obstruct recovery

**Fourth batch, iteration 11 of 20.**

**Strength:** exact eraser readout/feedforward, input-independent labels, and explicit remaining-copy accounting. Not a physical readout implementation or undoing of earlier history measurements.

[Previous apparatus tradeoff](APPARATUS-RECORD-TRADEOFF.md) · [Checker](check_retained_quantum_eraser.py) · [Receipt](results/retained-quantum-eraser.v1.json)

## 1. Fresh eraser protocol

Take the orthogonal-pointer fixture and n coherent copies of the inverse flag. After the full inverse-filter unitary W and copying, the state is

    |0_flag> N|psi> |0...0> + |1_flag> F|psi> |1...1>.

Measure every pointer in the X basis {|+>,|->}, retaining all labels. Each label string z contributes amplitude 2^(-n/2), with a flag-one sign (-1)^(number of minus labels). Apply Z_flag if that parity is odd, then apply W*.

Every corrected branch is exactly

    2^(-n/2)|0_flag> tensor |psi>.

Thus all branches restore the input and any reference. Each retained label has probability 2^(-n), independent of input/reference. The output label channel factors as a uniform classical record times the restored input state.

The checker verifies the X-basis matrix and its overlaps, the parity correction and the resulting identity branch. It checks one through four copies on both witnessed inverse-filter cases; the same overlap product proves the general-n formula.

## 2. Which information is retained?

The eraser labels are actual recorded readout outcomes. They are not useful which-flag records: the original pointer words |0...0> and |1...1> give the same X-label distribution, so equal-prior guessing from those labels succeeds only with probability one half.

This is not a contradiction of the earlier information/disturbance obstruction. An input-independent random label can coexist with reference recovery; a readable record distinguishing logical inputs cannot. The protocol intentionally changes the pointer readout basis rather than silently dropping an already acquired which-outcome record.

The restored state is the input to the inverse-filter interaction. The earlier state-dependent successful-history measurement is not reversed by this test.

## 3. Every other copy must be counted

Now erase only m<n copies. Their labels are still uniformly random with probabilities 2^(-m), and the same parity feedback removes their phases. But an unaddressed register still carries orthogonal words |0...0> and |1...1>.

After undoing W, the reduced system retains coherence factor

    r²=lambda_min/lambda_max,

and the terminal flag-one effect remains

    2r²(1-r²)Pi_high.

The exact four retained system maps from the preceding orthogonal-pointer fixture are used, not a substitute channel. Their scaling by each eraser-label amplitude preserves completeness. Other remaining-copy words have zero amplitude; both active words and terminal flags remain accounted for.

All m=0..n configurations are checked for n=1..4 on both cases. In particular, uniform eraser labels alone are not evidence of successful recovery. Inaccessible environment copies can keep the disturbance even if every named pointer is read.

## 4. Control and access boundary

The protocol needs quantum X-basis apparatus access, a phase reference, flag-parity feedforward and inverse polar/flag controls. A classical memory already decohered into inaccessible environment copies does not supply those capabilities merely because its stored bit is known.

Coherent removal or eraser readout must address every useful outcome copy. The newly retained input-independent labels can themselves be copied without disturbing the restored input. None of this derives native Hamiltonian dynamics, a readout platform or control work costs.

## 5. Next readout-classification gate

Classify readout bases and feedforward phases that permit exact reference recovery. Test imbalanced amplitudes and phase miscalibration, checking branch effects as well as label statistics. Keep outstanding copies and physical phase/control assumptions explicit.

Root outcome remains null. Shared sources, historical receipts, atlas and formal contracts are unchanged. No physical preparation, spin, annihilation or photon output is admitted.

## Reproduce

```sh
python research/scattering/seed-composition/check_retained_quantum_eraser.py
python research/scattering/seed-composition/check_retained_quantum_eraser.py --check
python research/scattering/seed-composition/check_seed_composition_net.py
python research/scattering/low-energy/check_low_energy_net_v3.py
```

Predecessor apparatus maps are freshly recomputed. Exact root-mask arithmetic verifies branches, effects and remaining-copy channels. General copy-count and reference identities are explicitly scoped mathematical arguments, not new formal or physical admission.
