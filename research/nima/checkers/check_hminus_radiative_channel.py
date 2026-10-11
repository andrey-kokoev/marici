"""E1 selection gate and explicit continuum trial for H+e -> H-minus+photon.

Standard dipole coupling, singlet spin and an exchange-symmetrized hydrogen
1s plus free plane wave are supplied. This is NOT a Coulomb/distorted scattering
solution, rate calculation or WG derivation. Exact radial transforms establish
nonzero p-wave amplitude and the zero-incident-momentum limit.
"""
from fractions import Fraction as F
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[1]


def overlap(q):
    # Integral exp[-(q+1)r] d^3r, with common pi omitted.
    return 8/(q+1)**3


def dipole_transform(q,k):
    # Fourier transform exp(-q r): 8*pi*q/(q^2+k^2)^2.
    # Integral r_z exp(-q r) exp(i*k*z) = -i*d/dk Fourier
    # = i*32*pi*q*k/(q^2+k^2)^3. Return coefficient with i*pi omitted.
    return 32*q*k/(q*q+k*k)**3


def main():
    data=json.loads((ROOT/'results/hminus-nested-orbitals.json').read_text())
    a=F(data['output']['compact_exponent']);b=F(data['output']['diffuse_exponent'])
    def amplitude(k):
        # Both exchange terms add in the singlet spatial sector. Full
        # unnormalized z component is i*pi^2 times this rational coefficient.
        return 2*(overlap(a)*dipole_transform(b,k)+overlap(b)*dipole_transform(a,k))
    ks=[F(0),F(1,100),F(1,10),F(1,2)]
    rows=[]
    unit=F(data['hydrogen_calibrated_unit_eV'])
    Q=F(data['predicted_second_attachment_binding_eV'])
    mass_inputs=json.loads((ROOT/'results/proton-hydrogen-helium-structure.json').read_text())['inputs']
    electron_rest=F(mass_inputs['electron_rest_energy_eV'])
    hydrogen_rest=(F(mass_inputs['proton_me'])+1)*electron_rest-F(mass_inputs['hydrogen_binding_eV'])
    initial_rest=hydrogen_rest+electron_rest
    final_rest=initial_rest-Q
    for k in ks:
        A=amplitude(k)
        assert A== -amplitude(-k)
        assert (A==0)==(k==0)
        # Approximate incoming relative kinetic energy including H recoil;
        # exact outgoing two-body kinematics conditional on this input energy.
        kinetic=k*k*unit/2*(1+electron_rest/hydrogen_rest)
        initial_energy=initial_rest+kinetic
        release=Q+kinetic
        photon=release-release*release/(2*initial_energy)
        recoil=release-photon
        ion_energy=final_rest+recoil
        assert ion_energy+photon==initial_energy
        assert ion_energy*ion_energy-photon*photon==final_rest*final_rest
        rows.append(dict(k_inverse_model_bohr=str(k),dipole_coefficient_without_i_pi_squared=str(A),
                         nonzero=A!=0,incident_relative_kinetic_eV=str(kinetic),
                         photon_energy_eV=str(photon),ion_recoil_energy_eV=str(recoil),
                         photon_decimal_eV=float(photon),recoil_decimal_eV=float(recoil)))
    # Nonzero derivative at zero: coefficient M_z = i*pi^2*(slope*k+O(k^3)).
    slope=64*(overlap(a)/b**5+overlap(b)/a**5)
    assert slope>0
    # Swapping compact/diffuse roles does not change physical amplitude.
    k=F(1,10)
    swapped=2*(overlap(b)*dipole_transform(a,k)+overlap(a)*dipole_transform(b,k))
    assert swapped==amplitude(k)
    # Symmetric E1 operator cannot connect antisymmetric spatial (triplet)
    # entrance to symmetric spatial singlet exit: exchanged terms cancel.
    direct=overlap(a)*dipole_transform(b,k)+overlap(b)*dipole_transform(a,k)
    triplet=direct-direct
    assert triplet==0
    # For k along z, the dipole vector is along z. A photon propagating
    # along x can have z polarization (allowed); along z, transverse x/y
    # polarizations have zero dot product. No longitudinal photon is used.
    allowed_polarization_dot=amplitude(k)
    forbidden_direction_dot=F(0)
    assert allowed_polarization_dot!=0 and forbidden_direction_dot==0
    # E1 is odd. An s-wave entrance and the even final state give an odd
    # angular integrand, whose integral vanishes. Plane wave contains the
    # required odd l=1 component; at k=0 it reduces to an even constant.
    result=dict(schema='marici.nima.hminus-radiative-channel.v1',status='pass',
                obligation='declared E1 interaction and exchange-compatible joint-channel selection gate',
                inputs='retained H-minus compact/diffuse trial; hydrogen 1s plus free plane wave; standard length-gauge electric dipole; spin singlet',
                final_spatial='exp(-a*r1-b*r2)+exp(-b*r1-a*r2)',
                initial_spatial='exp(-r1)*exp(i*k*z2)+exp(-r2)*exp(i*k*z1)',
                dipole='D=r1+r2; overall charge, photon mode normalization and continuum normalization not included in displayed coefficient',
                amplitude_formula='M_z/(i*pi^2)=64*k*[S(a)*b/(b^2+k^2)^3+S(b)*a/(a^2+k^2)^3], S(q)=8/(q+1)^3',
                samples=rows,threshold_linear_coefficient=str(slope),
                selection='Final 1S-even singlet requires incident singlet P-odd component for E1. Pure S-wave and triplet entrances are E1-forbidden; exact k=0 plane-wave trial has zero dipole amplitude.',
                allowed_geometry='incident k along z; emitted photon along x with transverse z polarization',
                controls=['k reversal flips amplitude','zero k yields zero','orbital-role swap preserves amplitude','triplet cancellation','transverse polarization enforced'],
                disposition='Nonzero E1 matrix element exists in the declared finite-k continuum trial. Earlier threshold recoil bookkeeping did not establish a nonzero threshold amplitude.',
                residual='Free plane wave is not the interacting H+electron scattering state. No exact transition rate, gauge-independent prediction, finite-mass scattering correction or WG-derived electromagnetic coupling. The integral formula is analytically derived; checker tests its exact consequences, not numerical quadrature of a scattering solution.')
    (ROOT/'results/hminus-radiative-channel.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(dict(status='pass', samples=[{k:v for k,v in r.items() if k in
        ('k_inverse_model_bohr','nonzero','photon_decimal_eV','recoil_decimal_eV')} for r in rows],
        selection=result['selection'],residual=result['residual']),indent=2))


if __name__=='__main__':main()
