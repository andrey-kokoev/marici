"""Hydrogen-calibrated helium variational benchmark, with no helium fitting.

Standard nonrelativistic fixed-nucleus Coulomb Hamiltonian is supplied input,
not derived from WG. Rational arithmetic is exact conditional on rounded data.
"""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[1]


def coulomb_integral(zeta):
    # Product normalized 1s densities; angular integration yields 1/max(r,s).
    # J=32*zeta^6 int_0^inf dr r exp(-a*r) int_0^r ds s^2 exp(-a*s).
    # Reverse integration order and use int s^k exp(-b*s) ds=k!/b^(k+1).
    a=2*zeta
    return 32*zeta**6*(F(factorial(3),1)/(a*(2*a)**4)
                       +F(factorial(2),1)/(a*a*(2*a)**3))


def main():
    inputs=json.loads((ROOT/'results/proton-hydrogen-helium-structure.json').read_text())['inputs']
    hydrogen=F(inputs['hydrogen_binding_eV'])
    helium_reference=F(inputs['helium_electronic_binding_eV'])
    hartree=2*hydrogen  # Hydrogen calibration, not independently measured Eh.
    z=F(2)
    def energy(zeta):return zeta*zeta-2*z*zeta+coulomb_integral(zeta)
    for zeta in (F(1,4),F(1),F(27,16),F(2),F(3)):
        assert coulomb_integral(zeta)==F(5,8)*zeta
    optimum=z-F(5,16)
    assert optimum==F(27,16)
    minimum=-optimum**2
    assert energy(optimum)==minimum
    assert 2*optimum-2*z+F(5,8)==0
    # Completion of square proves the global minimum for this ansatz.
    for zeta in (F(1,4),F(1),optimum,F(2),F(3)):
        assert energy(zeta)-minimum==(zeta-optimum)**2
    independent=-z*z
    fixed=energy(z)
    binding=-minimum*hartree
    assert binding==F('77.4471375')
    error=binding-helium_reference
    assert error==F('-1.5580625')
    connected=(minimum-independent)*hartree
    fixed_repulsion=coulomb_integral(z)*hartree
    relaxation=(fixed-minimum)*hartree
    assert connected==fixed_repulsion-relaxation==F('31.3400625')
    repulsion_optimum=coulomb_integral(optimum)*hartree
    orbital_penalty=(optimum-z)**2*hartree
    assert connected==repulsion_optimum+orbital_penalty
    # Controls: remove interaction => independent hydrogenic energy.
    assert z*z-2*z*z==independent
    # Reversing the repulsion sign instead yields spurious enhanced binding.
    wrong_optimum=z+F(5,16)
    wrong_binding=wrong_optimum**2*hartree
    assert wrong_binding > -independent*hartree > binding
    assert energy(z)>energy(optimum)
    result=dict(schema='marici.nima.helium-coulomb-variational.v1',status='pass',
                obligation='conditional physical readout with explicitly supplied Coulomb Hamiltonian; no native WG identification',
                hamiltonian='H=sum_i[-(1/2) Laplacian_i-Z/r_i]+1/r12 in atomic units, fixed nucleus Z=2',
                ansatz='normalized equal-exponent 1s spatial product times antisymmetric spin singlet',
                coulomb_integral='5*zeta/8 hartree, obtained from radial integration',
                energy='zeta^2-2Z*zeta+5*zeta/8',
                optimum_zeta=str(optimum),minimum_energy_hartree=str(minimum),
                calibration_hartree_eV=str(hartree),input_hydrogen_binding_eV=str(hydrogen),
                predicted_helium_binding_eV=str(binding),rounded_reference_eV=str(helium_reference),
                prediction_minus_reference_eV=str(error),
                independent_binding_eV=str(-independent*hartree),
                connected_energy_eV=str(connected),
                fixed_orbital_repulsion_eV=str(fixed_repulsion),
                relaxation_gain_eV=str(relaxation),
                optimized_repulsion_eV=str(repulsion_optimum),
                orbital_deformation_cost_eV=str(orbital_penalty),
                required_connected_energy_from_reference_eV=str(-independent*hartree-helium_reference),
                disposition='Repulsive interaction plus variational orbital relaxation computes a connected term without a helium-fitted coefficient; approximate binding underestimates the reference.',
                residual='Restricted uncorrelated spatial ansatz; fixed nucleus and nonrelativistic Hamiltonian; hydrogen-based unit calibration and rounded data. Residual is not isolated electron correlation. No WG derivation, nuclear binding, isotope or abundance prediction.')
    (ROOT/'results/helium-coulomb-variational.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
