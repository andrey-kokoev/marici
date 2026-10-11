# A coupled electronic benchmark computes the helium connected term

## Question

Can the connected electronic energy isolated in `binding-composition-coherence.md` be calculated rather than fitted? Use a separately supplied standard Coulomb Hamiltonian to establish an executable benchmark. This changes the evidence type: it is a conventional quantum-mechanical calculation, not a derivation of an electronic operator from WG.

## Claim boundary

Supply the nonrelativistic, fixed-nucleus Hamiltonian in atomic units:

\[
H=\sum_{i=1}^2\left(-\frac12\nabla_i^2-\frac{Z}{r_i}\right)+\frac1{r_{12}},\qquad Z=2.
\]

Use the normalized spatial product of two identical orbitals

\[
\phi_\zeta(r)=\left(\frac{\zeta^3}{\pi}\right)^{1/2}e^{-\zeta r},
\]

with the antisymmetric spin singlet. The exponent is determined by energy minimization, not by helium data. This is a restricted variational ansatz; it has no explicit inter-electron spatial correlation.

Angular integration of the two spherical densities yields 1/max(r,s). Thus, with a=2zeta,

\[
\langle r_{12}^{-1}\rangle
=32\zeta^6\int_0^\infty r e^{-ar}\int_0^r s^2e^{-as}\,ds\,dr
=\frac58\zeta.
\]

Reversing integration order reduces this to elementary factorial moments. The checker evaluates that expression exactly. Together with the kinetic and nuclear terms,

\[
E(\zeta)=\zeta^2-2Z\zeta+\frac58\zeta
=\left(\zeta-Z+\frac5{16}\right)^2-\left(Z-\frac5{16}\right)^2.
\]

Hence zeta=27/16 and E=-729/256 for helium. The complete-square identity establishes the minimum within this ansatz, not the exact two-electron ground state.

## Hydrogen-only calibration and held-out helium

For continuity with the earlier trial, use the rounded hydrogen binding a_H=13.5984 eV to set the energy unit to 2a_H=27.1968 eV. This is a declared calibration, not an independently measured Hartree constant. In particular, finite proton mass in physical hydrogen is not a feature of the fixed-nucleus Hamiltonian. No helium value enters either the Hamiltonian or the minimizing exponent.

| Quantity | eV |
|---|---:|
| Independent hydrogenic helium binding | 108.7872 |
| Coupled variational helium binding | 77.4471375 |
| Rounded reference | 79.0052 |
| Prediction minus reference | -1.5580625 |
| Calculated connected energy relative to two independent Z=2 electrons | 31.3400625 |
| Connected energy required by the reference in that same baseline | 29.7820 |

The connected term decomposes in two equivalent ways:

- fixed-orbital repulsion 33.9960 minus orbital-relaxation gain 2.6559375;
- optimized repulsion 28.684125 plus orbital-deformation cost 2.6559375.

This shows why the connected correction is not simply a count of electron pairs or a bare repulsion expectation. Allowing the state to respond to the interaction changes both attraction/kinetic energy and repulsion. The remaining difference is not isolated correlation energy: the approximation, fixed-nucleus/nonrelativistic assumptions, unit calibration and rounded inputs all delimit that interpretation.

## Disposition and verification

The interaction calculation improves the earlier independent-electron trial without fitting a helium-specific coefficient. It does not reproduce the reference exactly and supplies no nuclear binding, isotope abundance or atomic-weight prediction. The native WG electronic-sector and Hamiltonian-selection problem remains open; this benchmark gives it a concrete calculation to reproduce rather than replacing that missing derivation.

`python research/nima/checkers/check_helium_coulomb_variational.py` passed, execution `structured_command_execution:e_32876_1791224974600068300_26`. Exact checks cover the radial integral, stationary point, complete-square minimum, connected-energy accounting, zero-interaction control and incorrect repulsion-sign control. Results: `results/helium-coulomb-variational.json`. No commit or publication is claimed.
