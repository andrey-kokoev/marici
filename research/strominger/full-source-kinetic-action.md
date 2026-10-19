# Full-source occupied action: keep native dynamics and bound the energy

## Change from the return-only action

Do not restrict configuration space to im(N). Retain all 36 native proton coordinates, all 36 intrinsic neutron coordinates, and all eight tetrahedral electron coordinates, with their actual metrics and source-operation Hamiltonians K.

Apply one action and quantization:

    L = (1/2)||D_t z||² - <z,Kz>,   ||z||=1,
    H = -(1/2)Delta_S + <z,Kz>.

Use the common internal phase-charge sector +1 and the same separate empty state at energy zero. K is the prior native proton/belt operator in E*=pi*hbar/tau units; electron K=(I-L)+2(I-N) is its prior native stage-defect control. The tested normalization sets hbar=F²=1 and the common potential multiplier to one. No per-species offset or fitted coefficient is added.

This is the full-amplitude counterpart of the preceding declared sphere action. The source operators remain distinct inputs; one scalar action processes all three.

## Source checks

The checker loads actual matrices, not target eigenvalues. Exact metric-weighted complex elimination verifies K>=0 and its nullity. It checks KN=0, N²=N and metric self-adjointness.

| Carrier | Full complex dimension n | Native nullity | tr K |
|---|---:|---:|---:|
| Proton | 36 | 1 | 94 |
| Neutron | 36 | 1 | 1383011/14800 |
| Electron | 8 | 2 | 16 |

The source-bound neutron bridge and all of its recorded file hashes are checked before use. The electron projectors come from the native exact spinor store.

## Rigorous energy bounds

In internal charge +1, the full S^(2n-1) kinetic term has lowest energy (2n-1)/2. Since <z,Kz>>=0,

    E_ground >= (2n-1)/2.

For a normalized native zero vector v, take the first-harmonic wavefunction f(z)=<v,z>. The complex unit-sphere moments give

    <f,<z,Kz>f>/<f,f> = tr K/(n+1).

Hence

    E_ground <= (2n-1)/2 + tr K/(n+1).

This uses the trace as an exact variational expectation, not as a postulated rest-energy formula. The nonzero computed variance

    [(n+1)tr(K²)-(tr K)²]/[(n+1)²(n+2)]

also confirms that the trial is not an exact eigenstate. Higher harmonics have not been silently discarded.

## Results

| Carrier | Certified lower bound | Certified upper bound |
|---|---:|---:|
| Proton | 71/2 = 35.5 | 2815/74 = 38.0405405… |
| Neutron | 71/2 = 35.5 | 20822811/547600 = 38.0255861… |
| Electron | 15/2 = 7.5 | 167/18 = 9.2777778… |

Therefore

    639/167 <= E_proton/E_electron <= 563/111,
    3.826347… <= ratio <= 5.072072….

The hierarchy near 1836 is excluded at this common action normalization without solving the full sphere eigenproblem. Proton/neutron bounds overlap; no ordering between their actual ground energies follows from these bounds.

## What has and has not changed

The new action retains the native phase, alignment, seam and spinor excitation operators instead of reducing them to return rank. It still produces positive occupied sectors, and no vacuum-lowering contact is introduced. The full normalized-amplitude action nevertheless fails the hierarchy test.

This excludes this action at its stated common kinetic/potential normalization. It is not an all-coupling theorem and does not select a different kinetic scale. Changing the configuration variables or their physical inertia is an action change, not another algebraic presentation of this test.

## Verification

```sh
python research/strominger/checkers/check_full_source_kinetic_action.py
```

Ten checks passed. Exact matrices, traces, variances, bounds and provenance are retained in `results/full-source-kinetic-action.json`. No shared source/store was modified; the reference was opened only after the bounds were derived.
