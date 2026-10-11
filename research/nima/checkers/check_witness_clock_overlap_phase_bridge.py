"""Separate witnessed rotation from overlap curvature; reuse prior dynamics.

No new force, initial preparation or fitted coefficient is introduced.
Reusing the old model with t=T is an explicit dimensionless parameter
attachment, not a derivation of its Hamiltonian from the witnessing source.
"""
from contextlib import redirect_stdout
from pathlib import Path
import io
import json
import hashlib
import runpy
import numpy as np
import sympy as S

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
with redirect_stdout(io.StringIO()):
    witness=runpy.run_path(str(HERE/'check_full_turn_witness_rung_attachment.py'))
    exchange=runpy.run_path(str(HERE/'check_seed_port_exchange_binding.py'))
    backreaction=runpy.run_path(str(HERE/'check_137_phase_backreaction.py'))
checks=[]
def check(name,condition):
    if not condition:raise AssertionError(name)
    checks.append(name)

# The SAME six bound state/tensor ports, at phi=0, in the curved model.
phi=S.symbols('phi',real=True)
GA=10*S.eye(4)+S.ones(4)
GB=GA.copy()
GA[0,1]=S.exp(S.I*phi);GA[1,0]=S.exp(-S.I*phi)
curved_metric=S.kronecker_product(S.conjugate(GA),GB)
features=exchange['features']; labels=exchange['labels']
port_gram=features.T*curved_metric*features
check('same-source-port-metric-at-zero',curved_metric.subs(phi,0)==exchange['H'])
check('same-six-normalized-features',all(S.simplify(port_gram[i,i]-1)==0 for i in range(6)))
# A Bargmann triangle product is invariant under any common isometric
# transport and independent rephasing of the three normalized directions.
a,b,c=(labels.index(label) for label in ('AB','BC','CA'))
triangle=S.simplify(port_gram[a,b]*port_gram[b,c]*port_gram[c,a])
check('actual-triangle-holonomy',S.simplify(triangle-S.exp(-S.I*phi)/121**3)==0)
fixed_triangle=triangle.subs(phi,0)
angles=witness['witness'].angles_over_pi
check('uses-actual-six-step-full-turn',angles[0]==0 and angles[-1]==2 and len(angles)==7)
for n,angle in enumerate(angles):
    substituted=S.simplify(triangle.subs(phi,S.pi*angle))
    if n in (0,6):
        check('endpoint-holonomy-coincidence/'+str(n),substituted==fixed_triangle)
    else:
        check('phase-identification-fails-between-endpoints/'+str(n),S.simplify(substituted-fixed_triangle)!=0)

# Prior directions use a positive square-root frame. Verify its state ports
# reproduce exactly this raw-coordinate overlap data numerically.
def state_port(label):
    source,target=exchange['registry'][label]
    return 121+4*'ABCD'.index(source)+'ABCD'.index(target)
ports=[state_port(label) for label in labels]
for value in (0.,.4,np.pi/3):
    U=backreaction['directions'](value)[ports]
    numeric=U.conj()@U.T
    expected=np.array(port_gram.subs(phi,value),dtype=complex)
    check('same-old-positive-frame/'+str(value),np.max(np.abs(numeric-expected))<1e-12)

# Retain the two typed roles: T is the accumulated witness clock; phi and p
# are old dynamical field coordinates. The old equation is dphi/dt=beta*p,
# not phi=t and not dphi/dt=1. No reset at a witnessing return.
y0=backreaction['y0'].copy()
check('old-phase-is-not-clock-rate',abs(backreaction['rhs'](y0)[153].real-.07)<1e-14)
check('old-phase-is-not-initial-clock',y0[153].real==.4 and angles[0]==0)


def run_cycle(substeps):
    y=y0.copy()
    H0=backreaction['energy'](y)
    Q0=float(np.vdot(y[:153],y[:153]).real)
    h_error=q_error=0.
    snapshots=[]
    for n,angle in enumerate(angles):
        if n:
            dt=float(S.pi*(angle-angles[n-1]))/substeps
            for _ in range(substeps):
                y=backreaction['step'](y,dt)
                h_error=max(h_error,abs(backreaction['energy'](y)-H0))
                q_error=max(q_error,abs(float(np.vdot(y[:153],y[:153]).real)-Q0))
        snapshots.append({'tick':n,'witness_T_over_pi':str(angle),
            'overlap_phase':float(y[153].real),'phase_momentum':float(y[154].real),
            'comparison_force':float(backreaction['rhs'](y,parts=True)[0]),
            'record_norm':float(np.linalg.norm(y[16:153]))})
    return y,h_error,q_error,snapshots

coarse=run_cycle(64);fine=run_cycle(128)
check('full-witness-cycle-energy-control',fine[1]<5e-7)
check('full-witness-cycle-global-phase-charge-control',fine[2]<5e-7)
check('energy-refinement',fine[1]<coarse[1]/3)
check('charge-refinement',fine[2]<coarse[2]/3)
check('trajectory-refinement',np.linalg.norm(fine[0]-coarse[0])<1e-6)
check('returned-witness-does-not-reset-interaction',np.linalg.norm(fine[0]-y0)>1e-3)
check('overlap-phase-not-forced-to-full-turn',abs(fine[0][153].real-2*np.pi)>1.)

result={
    'schema':'marici.nima.witness-clock-overlap-phase-bridge.v1','status':'pass','checks':checks,
    'same_port_triangle':['AB','BC','CA'],
    'exact_holonomy':'exp(-i*phi)/121^3; fixed-port witness realization has constant 1/121^3',
    'phase_verdict':'witness angle and overlap curvature phase are not the same source operation; matching at 0 and 2pi hides intermediate mismatch',
    'parameter_attachment':'reuse the old dimensionless evolution parameter as T, with dT/dparameter=1; no identification phi=T and no seconds calibration',
    'unchanged_model_parameters':{name:backreaction[name] for name in ('kappa','beta','mu')},
    'clocked_old_trajectory':fine[3],
    'errors':{'coarse_energy':coarse[1],'fine_energy':fine[1],
              'coarse_global_norm':coarse[2],'fine_global_norm':fine[2],
              'state_refinement_difference':float(np.linalg.norm(fine[0]-coarse[0]))},
    'positive_result':'the prior collective backreaction runs through one completed witnessing-clock cycle with nonzero field/state change and controlled energy/global-norm errors',
    'remaining':'identifying the prior curved metric/action with a source-generated interaction is not supplied by this parameter attachment',
    'scope':'exact port/phase obstruction plus numerical reuse of the old trial action; not the old ordered-exchange schedule and not a derived electric charge or mechanical mass',
    'input_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in
        [Path(__file__),HERE/'check_137_phase_backreaction.py',HERE/'check_seed_port_exchange_binding.py']},
}
(ROOT/'results/witness-clock-overlap-phase-bridge.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(f'PASS: {len(checks)} phase/clock attachment checks')
print('Exact: the actual port triangle separates fixed-frame witness rotation from overlap curvature.')
print('Existing collective action reused with T as dimensionless time; phi remains an independent dynamical coordinate.')
print('End of full witness turn:',fine[3][-1])
print('Energy/global-norm errors:',fine[1],fine[2])
