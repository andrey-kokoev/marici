# Neutron comparison memory: derive its spectrum from the stored task

## Result

A reversible memory encoder and energy operator are now derived from the neutron's **21 actual seam residuals**, not from an assigned equal register gap. There are 15 independent residual directions; all 21 occurrence slots remain retained, including six dependent/zero-energy directions.

The memory excitation spectrum, in the existing collective-source unit, is:

| Eigenvalue | Multiplicity |
|---|---:|
| 0 | 6 |
| 0.172938631059362... | 3 |
| 4485/3292 = 1.362393681652491... | 3 |
| 1.433959780712725... | 3 |
| 5391/3292 = 1.637606318347509... | 3 |
| 2.393101588227912... | 3 |

The three irrational values are the roots of the previously recovered odd-channel cubic. Their appearance here follows from the actual comparison operator, not a numerical fit.

## Exact storage task and residual map

The declared task is to remove all 21 live seam comparisons from the native energy while preserving their information and energy in memory. This is not yet a physical neutron breakup or detector protocol.

Use the current 24-coordinate neutron/bank space and its metric M. For a seam joining triangle coefficients a,b, take the raw residual row

    B_e z=z_a-z_b,
    gamma_e=1/(1/M_aa+1/M_bb).

Let Gamma=diag(gamma_e). Each existing seam projector is reproduced exactly by

    P_e=M^-1 B_e^T gamma_e B_e.

Thus the source seam energy is B^T Gamma B in quadratic-form coordinates. After whitening native and memory metrics, define D=Gamma^(1/2) B M^(-1/2), with the actual Cholesky isometry used in the implementation.

The memory operator is

    H_memory=D D†.

No independent epsilon, J or g is introduced. In rational, unwhitened memory coordinates its matrix is B M^-1 B^T Gamma. Each seven-occurrence sector block has characteristic polynomial z times the corresponding six-mode seam operator's characteristic polynomial. This exactly certifies the spectrum and six zero directions before numerical diagonalization.

The spectrum is task-derived within the already supplied seam-energy rule. It does not uniquely select that physical rule or its energy unit.

## Reversible encoding without duplicating norm

Because D has rank 15 rather than 21, use its polar partial isometry W and keep the memory kernel explicitly:

    Q=W†W, N=I24-Q,
    Qm=WW†, Nm=I21-Qm,
    U=[[N,W†],[W,Nm]].

Then U†=U and U²=I45. For ready memory the encoding is

    z -> Jz=(Nz,Wz).

It preserves norm, and z is recovered by N(Nz)+W†(Wz). The original residual is recovered from H_memory^(1/2)Wz=Dz. Memory amplitudes are polar coordinates for the stored residual, not an extra copy of it.

The six dependent memory directions are retained as identity spectators under U. They are not discarded or arbitrarily charged.

These 21 complex memory coordinates are **not** the earlier 21 tensor-product neutral qubits. The original six active source-bank coordinates remain inside the native 24-coordinate block; they are not identified with the new seam memory.

## Full energy accounting

Write the existing core as

    K=A0+D†D,
    A0=H_native/4.

After storage, use A0 on the native block and H_memory on memory. The seam energy moves exactly:

    W† H_memory W=D†D.

For a generic input the other native energy changes by

    N A0 N-A0.

Exact calculation finds rank 10, nonzero eigenvalue -3/4, and fourteen zero eigenvalues. Therefore the encoder is NOT universally energy-conserving merely because residual storage is exact.

For the actual autonomous two-rim scattering preparation, however, the entire five-dimensional bright core lies in ker(A0). This is checked exactly over the rationals. On that invariant sector,

    H_after J=J K.

The full core energy therefore is preserved for the current scattering experiment, not just its residual contribution.

## The contact must retain access to memory

Transport the original lead/core coupling C along with the state:

    C_after=J C.

Its columns remain normalized, and C_after†Jz=C†z. Keeping only the native component after storage would change the readout and the interaction.

A negative control detects an approximately 1.2676 maximal native-only readout discrepancy on the retained scan. With the correct native-plus-memory contact, all **201 scattering matrices** agree before and after encoding. Maximum S-matrix discrepancy is about 2.31e-14; energy and recovery residuals are similarly small.

This is a lossless task-specific re-encoding of the accessible dynamics. It is not evidence for an independently realized physical memory-writing gate, a new outgoing particle, or an instantaneous free operation on arbitrary excited states.

## What this does and does not give for rest energy

The memory spectrum is now tied to what is stored. This replaces an arbitrary equal-gap assignment for this particular residual-storage task.

The coherent neutron has zero seam residual, so ready memory stores zero energy for that state. A mismatch-memory spectrum is not the satisfied-interface charging spectrum needed for a positive neutron rest gap. Physical time/action normalization is also still separate.

## Verification

```sh
uv run --offline --with numpy --with scipy python research/strominger/checkers/check_neutron_comparison_memory.py
```

Eight checks passed, including exact reconstruction of all projectors, rank and characteristic-polynomial certificates, reversible memory-kernel retention, full native energy accounting, and the 201-case scattering comparison.

Results under `research/strominger/results/`:

- `neutron-comparison-memory.json`: exact residuals, metric, rational memory operator, spectra and checks;
- `neutron-comparison-memory.npz`: whitened operator, full reversible encoder, transported contact and post-storage native/memory Hamiltonian.

No source/scattering backend was overwritten.
