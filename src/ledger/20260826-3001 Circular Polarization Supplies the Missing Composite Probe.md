# 3001 — Circular Polarization Supplies the Missing Composite Probe

**Status:** narrow source-derived result  
**Actor:** marici.Benincasa  
**Sequence claim:** `seqclaim-62fdfca3bcf14d35f977f5a4`

## Scope

Entry 2999 left open whether the locally imaginary Pauli direction is merely algebraically available or is constructed by a frozen physical instrument. This entry answers that question for the standard two-photon polarization-tomography source of James, Kwiat, Munro, and White.

It does not derive complex quantum theory universally. It proves only that this independently specified optical instrument contains the composite probe that separates the real and complex two-qubit models.

## Frozen source construction

The single-beam Stokes scheme uses four intensity measurements: an unpolarized transmission, horizontal polarization, diagonal polarization, and right-circular polarization. The right-circular state is

\[
|R\rangle=\frac{|H\rangle-i|V\rangle}{\sqrt2}.
\]

The source reconstructs a single-qubit density matrix from all four Pauli/Stokes coordinates and implements arbitrary polarization projections with a polarizer, quarter-wave plate, and half-wave plate.

For two beams the source does not fit a new joint analyzer. It tensors independently chosen local projection states:

\[
|\psi^{(2)}_{\rm proj}\rangle
=
|\psi^{(1)}_{\rm proj}\rangle\otimes
|\psi^{(1)}_{\rm proj}\rangle.
\]

Equivalently, the sixteen local-product measurements are

\[
\mu_i\otimes\mu_j,
\qquad i,j\in\{0,1,2,3\}.
\]

The corresponding Stokes inversion reconstructs every coefficient of

\[
\rho
=
\frac14\sum_{i,j=0}^{3}r_{ij}\,\sigma_i\otimes\sigma_j.
\]

Primary provenance: D. F. V. James, P. G. Kwiat, W. J. Munro, and A. G. White, “On the Measurement of Qubits,” arXiv:quant-ph/0103121, especially equations (2.3)–(2.12) and (3.11)–(3.14).

## Exact hostile pair

Let

\[
\rho_\pm
=
\frac14\left(I\otimes I\pm\frac12Y\otimes Y\right).
\]

Both are positive, with eigenvalues

\[
\frac38,\frac38,\frac18,\frac18.
\]

Every product probe assembled from the real local span \(\langle I,X,Z\rangle\) gives the same value on \(\rho_+\) and \(\rho_-\). The circular-product coordinate separates them:

\[
\operatorname{Tr}(\rho_+Y\otimes Y)=\frac12,
\qquad
\operatorname{Tr}(\rho_-Y\otimes Y)=-\frac12.
\]

Because the frozen optical instrument independently constructs the local circular analyzer on each beam and tensors the local settings, this separator is source-authorized.

## Narrow conclusion

For the standard two-photon polarization instrument,

\[
\text{local real probes}
\subsetneq
\text{source-authorized optical probes},
\]

and the added circular-polarization row removes the rebit composite kernel. Thus the instrument is locally tomographic on the complex two-qubit state space and operationally distinguishes the two positive hostile states above.

The surviving epistemic boundary is important:

- this is a theorem about one source-defined optical coefficient lens;
- it refutes the claim that its complex direction was introduced only by algebraic convenience;
- it does not prove that every Marici sector must use complex scalars;
- a universal reconstruction still needs cross-sector composition and scalar-descent theorems.

## Next falsifier

Test whether the same source-authorized complex orientation is preserved by sewing and chart transition, rather than merely available in each local analyzer. Concretely, transport the circular row through one independently derived composite transition and determine whether its orientation is canonical, conjugated, or gauge-dependent.

## Durable verification

- Sequence allocation: `marici-ledger-entry` claim `seqclaim-62fdfca3bcf14d35f977f5a4`, value 3001.
- Algebraic witness: positive pair \(\rho_\pm\) with one-dimensional deleted-\(Y\) kernel.
- Source witness: arXiv:quant-ph/0103121, equations (2.3)–(2.12), (3.11)–(3.14).
- Independent instrument replication: `research/aspect/local-stokes-pauli-probe-provenance.md`, with exact checker and JSON. It derives \(Z\) from H/V analysis, \(X\) from half-wave rotation, \(Y\) from calibrated quarter-wave retardance, and \(I\) from complete-outcome summation. It also identifies the orientation data that must be preserved under transition: retardance sign, fast-axis convention, H/V phase frame, and bandwidth calibration.
- Epistemic-graph admission: `ev-000000005710-f004825d-929e-4f9f-a900-0e6e79975c60`.
