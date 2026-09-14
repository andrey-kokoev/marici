# Positive kinematic mesh charges do not supply a positive charge Gram matrix

The scattering positive geometry imposes scalar inequalities

\[
C_{ij}>0
\]

on its discrete-wave source charges.

The zero-sum Weil reduction requires a stronger matrix statement:

\[
[C_{ij}]\succeq0.
\]

These are not equivalent. The exact charge matrix

\[
C=
\begin{pmatrix}
1&2\\
2&1
\end{pmatrix}
\]

has every entry positive but

\[
\det C=-3
\]

and

\[
(1,-1)C(1,-1)^T=-2.
\]

Thus positive source charges can carve out a nonempty associahedral region while failing to be Gram coordinates of primitive increments.

## Correction to the proposed bridge

The discrete-wave identity

\[
C_{ij}=\langle d_i,d_j\rangle
\]

holds if the channel field already has a common polarized realization. It cannot be inferred from entrywise positivity of the \(C_{ij}\).

Therefore the kinematic theorem supplies:

- positive scalar mesh sources;
- affine wave-equation incidence;
- positive channel regions.

It does not yet supply:

- Schwarz bounds \(|C_{ij}|^2\leq C_{ii}C_{jj}\);
- positive semidefiniteness of the complete charge matrix;
- the positive zero-sum Weil block.

The first comparison gate remains the common-carrier theorem for the primitive and prime-prime mesh observers. Only after that gate passes does the mass/zero-sum Schur complement become the final remaining condition.

## Verification

```text
python research/voevodsky/checkers/check_positive_mesh_charges_do_not_force_charge_Gram.py
```

Artifacts:

- `research/voevodsky/checkers/check_positive_mesh_charges_do_not_force_charge_Gram.py`
- `research/voevodsky/results/positive_mesh_charges_do_not_force_charge_Gram.json`
