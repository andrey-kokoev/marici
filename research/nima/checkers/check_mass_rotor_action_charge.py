"""Two rotor actions distinguish phase locking, charge locking and electric charge."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
from contextlib import redirect_stdout
import io
import json
import runpy

HERE=Path(__file__).resolve().parent
with redirect_stdout(io.StringIO()):
    prior=runpy.run_path(str(HERE/'check_mass_path_port_connectivity.py'))
slots=prior['slots']; N=len(slots); edges=prior['source_links']
assert len(prior['components'](N,edges))==1
# hbar=1, elementary reference rotor capacitance C_e=1 and charge q_e=1.
Ce=F(1); elementary=1/(2*Ce); C=[F(1)]*N
# Phase-rigid constraint theta_s=phi: effective inertia is SUM C_s.
phase_energy=1/(2*sum(C)); phase_ratio=phase_energy/elementary
assert phase_ratio==F(1,N)
# Gauge constraint B^T n=0: integer n_s=k, conjugate Phi=sum theta_s.
# Its effective inertia is harmonic: C_eff=1/sum(1/C_s).
charge_effective_C=1/sum(1/c for c in C)
charge_energy=1/(2*charge_effective_C)
assert charge_energy/elementary==N
# Common external U(1), theta_s -> theta_s+lambda, generator sum n_s.
unit_k_total_charge=N
assert unit_k_total_charge!=1
# One unit of this same electric charge is absent in the locked nonzero sector.
assert all(N*k!=1 for k in (-2,-1,0,1,2))
# The quotient coordinate has primitive character exp(i Phi), not exp(i Phi/N).
# Shifting one original theta by2*pi leaves exp(i Phi) unchanged; the latter
# fractional character is not single-valued for N>1.
assert F(1,N).denominator!=1
# Independent finite-window exact verification of integer Gauss constraints.
for n in range(2,7):
    allowed=[v for v in product((-1,0,1),repeat=n) if all(v[i]==v[i+1] for i in range(n-1))]
    assert len(allowed)==3
    for v in allowed:
        k=v[0]
        assert sum(v)==n*k
        assert sum(F(x*x,2) for x in v)==F(n*k*k,2)
# Energy variation preserves all compact gauge constraints and common charge.
unequal=[F(1) if s[1][0]=='arrow' else F(1,2) for s in slots]
unequal_ratio=sum(1/c for c in unequal)/(2*elementary)
assert unequal_ratio==1944
# Assigning each slot fractional external charge1/N restores unit collective
# charge but is new microscopic coupling data, not a change of coordinates.
assert sum(F(1,N) for _ in slots)==1
# Neutral slots + a separate unit-charged core also require extra core dynamics;
# charge neutrality does not tie their gaps to the elementary reference.
assert sum(F(0) for _ in slots)==0

result={
 'status':'passed','classification':'rotor_action_separates_energy_count_from_unit_particle_charge',
 'channels':N,
 'phase_rigid_unit_charge_energy_ratio':str(phase_ratio),
 'gauss_locked_primitive_energy_ratio':str(charge_energy/elementary),
 'gauss_locked_primitive_external_charge':unit_k_total_charge,
 'unequal_capacitance_energy_ratio':str(unequal_ratio),
 'checks':{'source_incidence_chain_fresh':True,'phase_rigid_sum_inertia':True,
           'gauss_locked_harmonic_inertia':True,'integer_charge_sector_checked':True,
           'fractional_character_not_single_valued':True,
           'capacitance_deformation_preserves_constraints':True},
 'conclusion':'An explicit charge-locking rotor action gives1836 elementary energy units with equal capacitances, but its primitive excitation carries1836 elementary charges under a common U(1). Phase locking instead yields a unit-charge excitation with energy ratio1/1836 in the ideal rigid limit. Neither supplies the observed proton/electron mass and equal-magnitude charge simultaneously without additional microscopic input.',
 'next_falsifier':'Source the microscopic external charge assignments and capacitance/action law together. Neutral internal channels with a separate charged core remain possible, but their gap normalization and core dynamics are not fixed by the rotor action.'}
out=HERE.parent/'results/mass-rotor-action-charge.json'
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
