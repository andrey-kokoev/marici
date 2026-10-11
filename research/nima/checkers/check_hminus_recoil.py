"""Finite-proton internal recoil plus a specified photon/recoil complement.

Not a model of the whole universe or a calculation of capture probability.
"""
from fractions import Fraction as F
from pathlib import Path
import json
from check_hminus_nested_orbitals import terms, energy
from check_helium_correlated_variational import ONE, add, scale, mul, integral

ROOT=Path(__file__).resolve().parents[1]


def main():
    previous=json.loads((ROOT/'results/hminus-nested-orbitals.json').read_text())
    inputs=json.loads((ROOT/'results/proton-hydrogen-helium-structure.json').read_text())['inputs']
    M=F(inputs['proton_me']);me_eV=F(inputs['electron_rest_energy_eV'])
    hydrogen=F(inputs['hydrogen_binding_eV'])
    mu=M/(M+1)
    a=F(previous['output']['compact_exponent']);b=F(previous['output']['diffuse_exponent'])
    old_E=F(previous['energy_hartree'])
    # The radial-only symmetrized s-orbital trial has no angular dependence.
    # Each term in grad1 psi dot grad2 psi is proportional to cos(theta),
    # whose exact angular mean is int_-1^1 t dt = 0. This is a property of
    # this restricted trial space, NOT permission to delete the operator.
    T,Vn,Vee,_=terms(mu*a,mu*b)
    finite_E=T/mu+Vn+Vee
    assert finite_E==mu*old_E
    hydrogen_E=-mu/2
    finite_affinity_au=hydrogen_E-finite_E
    assert finite_affinity_au>0
    fixed_unit=F(previous['hydrogen_calibrated_unit_eV'])
    fixed_unit_affinity=finite_affinity_au*fixed_unit
    # Prior unit was itself calibrated to H. Recalibrate consistently when
    # H's dimensionless energy changes, rather than double-counting recoil.
    recalibrated_unit=2*hydrogen/mu
    calibrated_affinity=finite_affinity_au*recalibrated_unit
    assert calibrated_affinity==F(previous['predicted_second_attachment_binding_eV'])
    assert fixed_unit_affinity==mu*calibrated_affinity

    # Correlated angular control: mass-polarization expectation need not vanish.
    x={(1,0,0):F(1)};y={(0,1,0):F(1)};z={(0,0,1):F(1)}
    r1=scale(add(x,y),F(1,2));r2=scale(add(x,z),F(1,2));u=scale(add(y,z),F(1,2))
    measure=mul(r1,r2,u)
    cos_weight=scale(mul(u,add(mul(r1,r1),mul(r2,r2),scale(mul(u,u),-1))),F(1,2))
    cross=scale(add(mul(r2,add(mul(r1,r1),scale(mul(r2,r2),-1),mul(u,u))),
                    mul(r1,add(mul(r2,r2),scale(mul(r1,r1),-1),mul(u,u)))),F(1,2))
    assert integral(cos_weight)==0
    c=F(1,5);factor=add(ONE,scale(u,c))
    polarization=integral(add(mul(cos_weight,factor,factor),scale(mul(cross,factor),c),
                              scale(measure,-c*c)))/integral(mul(measure,factor,factor))
    assert polarization!=0

    # Threshold H + free electron in their center-of-momentum frame. Q is
    # the computed rest-energy decrease. A chosen single-photon final channel
    # obeys exact two-body relativistic energy/momentum accounting (c=1).
    Q=calibrated_affinity
    initial_rest=(M+2)*me_eV-hydrogen
    final_rest=initial_rest-Q
    photon=(initial_rest**2-final_rest**2)/(2*initial_rest)
    recoil=Q-photon
    assert photon==Q-Q*Q/(2*initial_rest)
    assert recoil==Q*Q/(2*initial_rest)>0
    final_total=final_rest+recoil
    assert final_total+photon==initial_rest
    assert final_total**2-photon**2==final_rest**2
    momenta={'photon':photon,'ion':-photon}
    assert sum(momenta.values())==0
    # Omitting ion recoil while keeping photon energy Q violates its mass shell.
    wrong_mass_shell=final_rest**2-Q**2-final_rest**2
    assert wrong_mass_shell==-Q*Q!=0
    result=dict(schema='marici.nima.hminus-recoil.v1',status='pass',
                obligation='internal COM separation and closed two-body final-channel energy/momentum readout',
                source_inputs='rounded prior proton/electron mass ratio, electron rest energy and hydrogen binding; not precision audited',
                proton_mass_electron_units=str(M),reduced_mass=str(mu),
                internal_operator='H_int=(p1^2+p2^2)/(2*mu)+p1.dot(p2)/M -1/r1-1/r2+1/r12',
                restricted_trial_mass_polarization='zero by angular integration, not identically zero operator',
                correlated_control_p1_dot_p2=str(polarization),
                finite_mass_energy_au=str(finite_E),
                affinity_fixed_old_unit_eV=str(fixed_unit_affinity),
                fixed_old_unit_shift_decimal_eV=float(fixed_unit_affinity-calibrated_affinity),
                consistently_H_calibrated_affinity_eV=str(calibrated_affinity),
                calibration_disposition='Common reduced-mass scaling cancels in H-calibrated affinity for this restricted radial trial; richer angular correlations need not share this cancellation.',
                chosen_complement='one emitted photon plus recoiling H-minus ion, in initial center-of-momentum frame at capture threshold',
                attachment_Q_eV=str(Q),photon_energy_eV=str(photon),ion_recoil_energy_eV=str(recoil),
                Q_decimal_eV=float(Q),photon_decimal_eV=float(photon),recoil_decimal_eV=float(recoil),
                opposite_momenta_c_equals_one={k:str(v) for k,v in momenta.items()},
                residual='This adds finite-proton motion and a minimal specified radiative complement, not a universal environment. No capture matrix element, selection-rule admission, rate, WG recoil law or precision affinity prediction. Bound energies remain approximate nonrelativistic trial values; final-channel kinematics is exact conditional on them.')
    (ROOT/'results/hminus-recoil.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ('photon_energy_eV','ion_recoil_energy_eV','opposite_momenta_c_equals_one')},indent=2))


if __name__=='__main__':main()
