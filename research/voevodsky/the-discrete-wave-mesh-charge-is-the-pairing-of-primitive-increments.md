# The discrete-wave mesh charge is the pairing of primitive increments

The source transcript defines

\[
C_{ij}
=
X_{ij}+X_{i+1,j+1}-X_{i,j+1}-X_{i+1,j}.
\]

Suppose the channel field is a polarized observation

\[
X_{ij}=\langle v_i,v_j\rangle
\]

in one common carrier. Define the primitive transition

\[
d_i=v_i-v_{i+1}.
\]

Then direct polarization gives

\[
\boxed{
C_{ij}=\langle d_i,d_j\rangle.
}
\]

Thus the discrete wave source is naturally the Gram matrix of primitive increments.

## Positivity consequence

On the diagonal,

\[
C_{ii}=\lVert d_i\rVert^2\geq0.
\]

For two transitions, rung-four positivity is

\[
\begin{pmatrix}
C_{ii}&C_{ij}\\
C_{ji}&C_{jj}
\end{pmatrix}
\succeq0,
\]

or

\[
|C_{ij}|^2\leq C_{ii}C_{jj}.
\]

This matches the proposed interpretation:

- the primitive observer records \(d_i\);
- the primitive-square observer records \(C_{ii}\);
- the prime-prime observer records \(C_{ij}\);
- the elementary wave-equation diamond is their rung-four incidence square.

## Exact source frontier

The implication is rigorous after the common-carrier hypothesis. What remains unproved is

\[
X_{ij}^{\mathrm{kinematic}}
=
\langle\Phi_i,\Phi_j\rangle_{\mathrm{Weil\ carrier}}.
\]

Scalar positivity of each kinematic mesh charge does not imply that the complete matrix \([C_{ij}]\) is positive semidefinite. Off-diagonal mesh charges may have either sign even in a positive carrier.

Therefore the correct comparison target is not `C13 = trace`. It is the polarized finite-difference identity

\[
\Delta_i\Delta_jX
=
\langle\Delta_i\Phi,\Delta_j\Phi\rangle.
\]

If the endpoint--gamma--prime source supplies this common polarized realization independently, all rung-four Schwarz inequalities follow at once.

## Verification

```text
python research/voevodsky/checkers/check_mesh_charge_as_increment_pairing.py
```

Artifacts:

- `research/voevodsky/checkers/check_mesh_charge_as_increment_pairing.py`
- `research/voevodsky/results/mesh_charge_as_increment_pairing.json`
