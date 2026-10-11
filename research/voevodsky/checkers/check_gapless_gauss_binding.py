"""Gapless transverse-field bounds and a conditional full-field binding witness.
Analytic inequalities in the note establish the infinite-volume claims. This
checker binds exact rational certificates and tests finite-mode diagnostics;
it never replaces the gapless field by a positive lowest photon frequency.
"""
from fractions import Fraction as F
from itertools import product
from math import cos, pi, sqrt, factorial, prod
from pathlib import Path
from hashlib import sha256
import json
from check_gauss_dressed_hopping import exp_negative

BASE=Path(__file__).resolve().parents[1]
ROOT=BASE.parents[1]


def verify_sources(path):
    result=json.loads(path.read_text(encoding='utf-8'))
    assert result['verification_passed']
    for name,digest in result['source_hashes'].items():
        assert sha256((ROOT/name).read_bytes()).hexdigest()==digest
    return result


def coherent_controls():
    energies=(F(1),F(2),F(3));intensities=(F(1,8),F(1,16),F(1,32))
    a=sum(intensities);b=sum(x/w for x,w in zip(intensities,energies))
    c=sum(x/w**2 for x,w in zip(intensities,energies))
    exp_lo,exp_hi=exp_negative(a)
    sums={1:F(0),2:F(0)};cutoff=10
    for n in product(range(cutoff+1),repeat=3):
        if not 0<sum(n)<=cutoff:continue
        weight=prod(x**k/F(factorial(k)) for x,k in zip(intensities,n))
        energy=sum(w*k for w,k in zip(energies,n))
        for power in sums:sums[power]+=weight/energy**power
    # Tail bounded with omega_min=1 only for this finite fixture. Infinite-volume
    # bounds use b and c integrals, not this fixture's gap.
    tail=a**(cutoff+1)/F(factorial(cutoff+1))/(1-a/F(cutoff+2))
    assert exp_hi*sums[1]+tail < b
    assert exp_hi*sums[2]+tail < c
    assert (1-exp_lo)*b/a<=b
    return dict(norm_intensity=str(a),inverse_energy_bound=str(b),inverse_energy_squared_bound=str(c),
        exact_truncated_plus_tail_controls=True)


def mode_diagnostics(n):
    # Nonzero momentum quadrature of the infinite field, NOT an invariant
    # zero-harmonic-mode sector of a physical periodic gauge lattice.
    symbols=[2-2*cos(2*pi*j/n) for j in range(n)]
    j_integral=g_integral=charged_c=neutral_c=0.0
    for ix,iy,iz in product(range(n),repeat=3):
        lam=symbols[ix]+symbols[iy]+symbols[iz]
        if lam==0:continue
        transverse=1-symbols[ix]/lam
        j_integral+=1/sqrt(lam);g_integral+=1/lam
        charged_c+=0.5*transverse/lam**1.5
        neutral_c+=0.5*transverse*symbols[ix]/lam**1.5
    volume=n**3
    return dict(n=n,J=j_integral/volume,G=g_integral/volume,
        charged_inverse_energy_squared=charged_c/volume,
        unit_dipole_inverse_energy_squared=neutral_c/volume)


def main():
    static_path=BASE/'results/gauss_spatial_binding.json'
    hopping_path=BASE/'results/gauss_dressed_hopping.json'
    static=verify_sources(static_path);hopping=verify_sources(hopping_path)
    assert static['negative_level_certified'] and not hopping['local_hopping_preserves_transverse_vacuum']
    witness=ROOT/static['certificate']['file']
    assert sha256(witness.read_bytes()).hexdigest()==static['certificate']['sha256']
    replay=json.loads((BASE/'results/gauss_spatial_binding_replay.json').read_text(encoding='utf-8'))
    assert replay['exact_replay_passed'] and replay['negative_trial']
    assert replay['witness_sha256']==static['certificate']['sha256']
    assert replay['checker_sha256']==sha256((BASE/'checkers/check_gauss_spatial_binding.py').read_bytes()).hexdigest()
    binding=-F(static['best_trial']['energy_upper']);assert binding>0

    # Integer-shell bound: lambda(k)>=16|m|^2/n^2 and the max-norm shell
    # has 24m^2+2 points. The proof uses sum 1/m^2<=2 for every cutoff.
    for n in range(2,257):
        radius=n//2
        shell_bound=(24*F(radius)+2*sum(F(1,m*m) for m in range(1,radius+1)))/(16*n)
        coarse=F(3,4)+F(1,4*n)
        assert shell_bound<=coarse<=F(7,8)
    # Infinite lattice: the previous ball integral bound and Cauchy-Schwarz.
    assert F(7,4)**2>3
    green_infinite_upper=F(7,4)*F(22,7)/8
    assert green_infinite_upper==F(11,16)<1
    # Thus J=integral lambda^-1/2 <= sqrt(G)<1. With beta=q=1,
    # a<=1/(3sqrt(kappa)), b<=7/(24kappa), uniformly without a gap.
    diagnostics=[mode_diagnostics(n) for n in (8,16,32,64)]
    for row in diagnostics:
        assert 0<row['G']<float(F(7,8)) and row['J']<1
        assert row['unit_dipole_inverse_energy_squared']<float(F(1,3))
    assert diagnostics[-1]['charged_inverse_energy_squared']>diagnostics[0]['charged_inverse_energy_squared']

    # Reuse exactly the certified relative tent wavefunction and its potential
    # bound. Only the full-field stiffness is varied as an EXPLICIT parameter.
    # The conservative error is 6(1-Z)<=3a<=1/sqrt(kappa), for t_p+t_e=1.
    # A normalized common-position box of side L adds <=6/L for any t_p<=1.
    cases=[]
    com_side=2**16
    for root_kappa in (1,4,16,4096):
        a_upper=F(1,3*root_kappa)
        b_upper=F(7,24*root_kappa**2)
        vacuum_cost=3*a_upper
        finite_com_cost=F(6,com_side)
        total=-binding+vacuum_cost+finite_com_cost
        cases.append(dict(kappa=str(root_kappa**2),root_kappa=root_kappa,
            link_coherent_intensity_upper=str(a_upper),gapless_inverse_energy_upper=str(b_upper),
            vacuum_kinetic_cost_upper=str(vacuum_cost),com_side=com_side,
            finite_com_cost_upper=str(finite_com_cost),full_trial_energy_upper=str(total),
            decimal_upper=float(total),binding_certified=total<0))
    assert not cases[0]['binding_certified'] and cases[-1]['binding_certified']
    assert F(cases[-1]['full_trial_energy_upper'])<F(-1,10000)
    # Different positive mass partitions with the same relative t do not change
    # the phase-vacuum overhead; this does not determine either physical mass.
    for tp in (F(1,2),F(1,3),F(1,7)):
        te=1-tp;assert tp>0 and te>0 and 6*(tp+te)==6
        assert 6*tp/com_side<=F(6,com_side)
    result=dict(verification_passed=True,model='infinite cubic lattice, two conserved opposite charges, noncompact transverse harmonic Fock field',
        coefficients=dict(beta='1',q='1',relative_kinetic_sum='t_p+t_e=1'),
        no_positive_photon_gap_assumed=True,green_infinite_upper=str(green_infinite_upper),
        nonzero_mode_quadrature_green_uniform_upper='7/8',
        coherent_discrete_controls=coherent_controls(),mode_diagnostics=diagnostics,
        charged_hop_inverse_energy_norm_finite=True,
        charged_hop_inverse_energy_squared_norm_diverges=True,
        bounded_dipole_inverse_energy_squared_norm_finite=True,
        neutrality_control_scope='coherent rigid pair translation at fixed separation; not arbitrary independent hops or breakup',
        common_field_breakup_lower_bound='0 after one common vacuum normalization and the retained static self-energy subtraction',
        prior_static_binding_lower_bound=str(binding),stiffness_cases=cases,
        unit_stiffness_binding_settled=False,conditional_large_stiffness_binding_certified=True,
        isolated_full_hamiltonian_eigenstate_proved=False,
        physical_stiffness_mass_charge_or_length_selected=False,
        scope='Energetic binding below the same full-field separation threshold in an explicit parameter regime, not physical hydrogen or a gap-based reduction theorem.',
        source_hashes={str(p.relative_to(ROOT)).replace('\\','/'):sha256(p.read_bytes()).hexdigest() for p in
            [Path(__file__),BASE/'checkers/check_gauss_dressed_hopping.py',static_path,hopping_path,
             BASE/'results/gauss_spatial_binding_replay.json']})
    (BASE/'results/gapless_gauss_binding.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
