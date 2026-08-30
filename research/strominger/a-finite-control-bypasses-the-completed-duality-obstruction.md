# A Finite Control Bypasses the Completed Duality Obstruction

## Controlled-sign circuit

Let \(H\) be the completed endpoint Hilbert space and let \(z=-I_H\) be the
metaplectic central sign. Adjoin a two-dimensional control \(Q\) and define

\[
C_z
=
|0\rangle\langle0|\otimes I_H
+
|1\rangle\langle1|\otimes z.
\]

For every normalized \(\psi\in H\),

\[
C_z(|+\rangle\otimes\psi)=| -\rangle\otimes\psi.
\]

Consequently, a Pauli-\(X\) observation on the control changes from \(+1\) to
\(-1\). The endpoint ray and endpoint density state remain unchanged.

This circuit uses neither an endpoint dual nor a maximally mixed or thermal
endpoint reference. It survives infinite-dimensional Hilbert completion.

## Correction to the reference hierarchy

There are two genuinely different readout constructions:

```text
closed categorical trace
  needs endpoint dualizability
  fails under Hilbert completion
  can be repaired by a trace-class weight

controlled relative-phase readout
  needs only a finite control and a normal endpoint state
  survives Hilbert completion
  requires controlled application of the central operation
```

Thus nuclear weighting is not the universal next rung. It repairs one
presentation of the sign experiment. The smaller operational constructor is
conditionalization.

## Authority boundary

The bounded operator \(C_z\) exists mathematically once \(Q\otimes H\) is
admitted. But existence of \(z\), tensoring, and a control system does not imply
authority to implement \(C_z\). Conditional execution is strictly stronger
than diagonal metaplectic execution: it must preserve branch coherence while
applying different endpoint operations on the two branches.

The endpoint source has not supplied this controlled-action constructor.
Therefore the sign is mathematically measurable in the completed theory, but
not yet executable in the magnetic system.

## Higher-tower interpretation

The next closure tower controls conditionalization of lower-level operations.
Its rungs do not add new endpoint transformations. They certify that an
existing transformation can be selected coherently relative to another
system. This is the precise bridge from invariant closure to executable
closure in the present example.

## Evidence replay

```powershell
C:\Users\andrey\.local\bin\python.exe research/strominger/checkers/controlled_metaplectic_sign_readout_checks.py
```

The exact checker verifies the control flip for several endpoint dimensions
without using duality or a trace-class ensemble.
