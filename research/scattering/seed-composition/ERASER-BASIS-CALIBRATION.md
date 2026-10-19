# Eraser basis and phase calibration are separate recovery requirements

**Fourth batch, iteration 12 of 20.**

**Strength:** projective-qubit readout classification and exact calibration-error channels. Not a physical phase reference, measured noise model or arbitrary-POVM no-go.

[Previous retained eraser](RETAINED-QUANTUM-ERASER.md) · [Checker](check_eraser_basis_calibration.py) · [Receipt](results/eraser-basis-calibration.v1.json)

## 1. Fresh classification

Assume a single orthogonal pointer with all other outcome copies addressed. Up to row phases and outcome relabelling, its projective readout has rows

    (a,b p), (b,-a p),
    a,b>=0, a²+b²=1, |p|=1.

Apply flag-one feedback phases f and -f. The corrected flag-zero/flag-one amplitudes in each label are

    label 0: (u,w)=(a,b e),
    label 1: (u,w)=(b,a e), e=p f.

After W*, that label has terminal flag maps

    flag 0: u Pi_low+(u r²+w(1-r²))Pi_high,
    flag 1: r sqrt(1-r²)(w-u)Pi_high.

Since 0<r²<1, exact reference recovery with flag returned to zero requires w=u on each label. Thus the readout must be unbiased, a=b=1/sqrt(2), and its relative phase matched, e=1. Arbitrary equatorial basis phase is allowed if supplied feedback compensates it.

The classification is for projective readout plus flag-phase feedback and W*, not every POVM or additional coherent recovery operation. Outcome-specific phase errors can be considered separately; the tested fixtures use a common residual phase after the nominal sign correction.

## 2. Label independence is weaker than recovery

The label effect is

    |u|² Pi_low+[|u|²r²+|w|²(1-r²)]Pi_high.

It is scalar precisely when a²=b², irrespective of residual phase. An imbalanced readout therefore reveals logical-input information and cannot be repaired by phase-only feedback. A balanced readout can retain uniform labels yet fail to restore the input/reference because its feedback phase is wrong.

Eight fixtures on each witnessed filter test compensated real, imaginary and rational-complex phases, amplitude imbalance, isolated phase faults, combined faults and the which-outcome basis. All label effects, terminal flags and completeness are checked exactly.

## 3. Actual reduced error channel

Let

    z=2ab conjugate(e),
    kappa=r²+(1-r²)z.

The reduced channel preserves spectral populations and multiplies low/high coherence by kappa. Its Bell undo fidelity and terminal flag-one effect are

    F=1-(1-r²)(1-Re(z))/2,
    E_flag1=2r²(1-r²)(1-Re(z))Pi_high.

The maximum visibility with matched phase is 2ab. The readout distributions of the original flag values have distinguishability |a²-b²|, and

    (2ab)²+|a²-b²|²=1.

Amplitude imbalance and phase error therefore have distinct signatures: the first leaks into label probabilities; the second can disturb reference coherence without that statistical warning. Known phase error can be corrected by changing the control; uniform labels alone do not establish that the actual control did so.

Ignoring labels/flags for reduced statistics is not physical deletion. Their joint maps remain retained. The test concerns only the inverse-filter interaction, not earlier state-dependent history measurements.

## 4. Control scope and next pointer extension

Readout basis, phase reference and flag feedback remain added inputs, not native Hamiltonian dynamics. Outstanding outcome copies invalidate the single-pointer classification's recovery conclusion even with a calibrated basis, as the previous turn established.

Next construct an eraser for the partially overlapping pointer pair e0=|0>, e1=gamma|0>+sqrt(1-gamma²)|1>. Choose a readout unbiased relative to those actual states, not merely the orthogonal-pointer X basis. Test exact branch/reference recovery and retained label independence, including the required pointer-dependent phase feedback.

Root outcome remains null. Shared sources, historical receipts, atlas and formal contracts are unchanged. No physical feedback, preparation, spin, annihilation or photon output is admitted.

## Reproduce

```sh
python research/scattering/seed-composition/check_eraser_basis_calibration.py
python research/scattering/seed-composition/check_eraser_basis_calibration.py --check
python research/scattering/seed-composition/check_seed_composition_net.py
python research/scattering/low-energy/check_low_energy_net_v3.py
```

Predecessor erasers are freshly recomputed. Exact root-mask arithmetic checks basis unitarity, actual branches and reduced channels on an operator basis. The classification is explicitly scoped mathematics, not new machine-formal or physical admission.
