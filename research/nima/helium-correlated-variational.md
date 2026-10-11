# Explicit pair correlation improves the helium binding benchmark

## Question

Does allowing the two-electron state to depend explicitly on their separation reduce the error left by the product-orbital calculation? This is a successor conventional Coulomb benchmark, not a WG-derived Hamiltonian or an atomic-weight calculation.

## Claim boundary

Keep the fixed-nucleus, nonrelativistic Z=2 Coulomb Hamiltonian and hydrogen-only energy calibration from `helium-coulomb-variational.md`. Use a normalized symmetric spatial trial state proportional to

\[
\psi= e^{-\zeta(r_1+r_2)}(1+b\zeta r_{12}),
\]

times the antisymmetric spin singlet. The r12 factor introduces explicit correlation absent from the earlier product state.

Freeze b=j/1000 for j=0,...,1000. For each candidate compute exact integrals in nonnegative perimetric coordinates

\[
x=r_1+r_2-r_{12},\quad y=r_1-r_2+r_{12},\quad z=-r_1+r_2+r_{12}.
\]

In scaled coordinates the common exponential is exp(-2x-y-z); the integration moments are factorials divided by powers of two. Angular and Jacobian constants cancel in the Rayleigh quotient. The kinetic form uses the squared gradients of the full correlated wavefunction, including cross terms, not just the uncorrelated orbital kinetic energy.

Scale separation gives E(zeta,b)=zeta^2 T(b)+zeta V(b). Since T>0 and V<0 on every tested candidate, the exact minimizing scale is -V/(2T), with energy -V^2/(4T). Select the smallest energy on the frozen grid; this is not asserted to be the continuous optimum in b or the exact ground state. Reference helium binding enters only after that selection.

## Results

The selected b is 99/500 and zeta is 26275653/14204528, approximately 1.8504. The two-electron energy is approximately -2.8911 in the model's atomic unit.

| Calculation | Electronic binding, eV |
|---|---:|
| Earlier optimized uncorrelated product | 77.4471375 |
| Explicitly correlated trial | 78.6292309474 |
| Rounded reference | 79.0052 |

The calculated improvement is 1.1820934474 eV, leaving a shortfall of 0.3759690526 eV. No helium-specific parameter was fitted. The b=0 candidate exactly reproduces the previous energy -729/256 and exponent 27/16; exact complete-square checks certify scale minimization for the selected correlated state.

## Disposition

The coupled operator's prediction improves when its state retains a direct pair relation rather than being restricted to independent orbitals. This supports using a correlated-state benchmark for any proposed WG electronic realization, not identifying a geometric comparison with physical correlation without a map.

Remaining error includes the restricted variational family/grid and the previously declared fixed-nucleus, nonrelativistic and hydrogen-calibration limitations. It is not assigned entirely to one physical effect. No native electronic-sector identification, nuclear binding or isotope abundance was supplied.

Verification: `python research/nima/checkers/check_helium_correlated_variational.py` passed through execution `structured_command_execution:e_32876_1791225137395720000_27`. Exact rational integrals and optimization are stored in `results/helium-correlated-variational.json`; decimal values are display conversions. No commit or publication is claimed.
