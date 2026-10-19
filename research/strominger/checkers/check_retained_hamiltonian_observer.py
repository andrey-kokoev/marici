# /// script
# dependencies = ["sympy"]
# ///
"""Active energy readout through complete native T9; full kernel retained."""
from contextlib import redirect_stdout
from pathlib import Path
import hashlib
import io
import json
import runpy
import sympy as S
from sympy.polys.matrices import DomainMatrix
from retained_hamiltonian_observer import construct_observer
from hamiltonian_descent_wg import zero, positive_metric

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
OUT=ROOT/'results/retained-hamiltonian-observer.json'
OUT.unlink(missing_ok=True)
with redirect_stdout(io.StringIO()):
    previous=runpy.run_path(str(HERE/'check_interface_preserving_carrier_dynamics.py'))
A=previous['A']
F=previous['F']
Fhostile=previous['Fhostile']
T,L=previous['T'],previous['L']
means=previous['means']
U=previous['U']
observer=construct_observer(A)
w=observer.witness
C,E,N=w.P,w.E,w.N
checks=[]
def check(name,condition):
    if not condition: raise AssertionError(name)
    checks.append(name)
def rank(matrix):
    return DomainMatrix.from_Matrix(S.Matrix(matrix)).rank()

check('exact-rational-positive-metric',positive_metric(S.Matrix([[2,1],[1,2]])))
check('positive-diagonal-does-not-hide-indefinite-metric',not positive_metric(S.Matrix([[1,2],[2,1]])))
check('semidefinite-metric-refused',not positive_metric(S.ones(2)))
check('nonsymmetric-metric-refused',not positive_metric(S.Matrix([[2,1],[0,2]])))
check('prior65-check-classification-freshly-rerun',previous['result']['verification_status']=='pass' and len(previous['checks'])==65)
check('linear-active-observer38-coordinates',C.shape==(38,137) and rank(C)==38)
check('all99-kernel-directions-retained',rank(N)==99 and zero(A*N))
check('active-observer-left-inverse',C*E==S.eye(38))
check('active-Hamiltonian-nondegenerate',rank(w.target.Omega)==38 and rank(w.target.K)==38)
check('active-generator-intertwines',zero(C*A-w.target.D*C))
check('Hamiltonian-factorization',zero(w.source.K-C.T*w.target.K*C))
check('source-energy-rank38-linear-lower-bound',rank(w.source.K)==38)
check('family-means-alone-remain-insufficient',means*A==S.zeros(64,137))
check('joint-active-family-readout-rank70',rank(S.Matrix.vstack(means[:32,:],C))==70)
check('67-extra-static-directions-remain-beyond-joint-readout',137-rank(S.Matrix.vstack(means[:32,:],C))==67)

for name,field in (('fixture',F),('factored-hostile',Fhostile),('after-exact-step',U*F)):
    observed=observer.observe(field,'declared '+name+' coefficient sample')
    check('full-state-reconstruction/'+name,observer.reconstruct(observed)==field)
    check('energy-readout-exact/'+name,observed.energy==S.simplify(((A*field).T*(A*field)).trace()/4))
    target_field=T*field
    target_observed=observer.observe_retained(target_field,T,L,'retained '+name+' chart')
    check('complete-T9-target-reader/'+name,target_observed==observer.observe(field,'retained '+name+' chart'))
    check('full-kernel-reconstruction-from-retained-T9/'+name,N*L*target_field==observed.retained_kernel)

initial=observer.observe(F,'original supplied fixture')
rival=observer.observe(Fhostile,'invertible factored-leg hostile')
check('same-outer-means-different-active-energy',means*F==means*Fhostile and initial.energy!=rival.energy)
check('exact-step-active-dynamics',C*U*F==(C*U*E)*initial.active)
check('exact-step-kernel-stationary',N*U*F==initial.retained_kernel)
check('exact-step-energy-preserved',observer.energy_from_active(C*U*F)==initial.energy)
# Retained target generator B=T A L cannot require another inferred input.
check('active-observer-commutes-with-retained-generator',C*L*previous['B']==w.target.D*C*L)

# Spectral bands are exactly0,32,128 for -A^2. These are declared squared
# angular frequencies, not excitation energies or physical masses.
Z=-A*A
low=S.simplify(Z*(128*S.eye(137)-Z)/3072)
high=S.simplify(Z*(Z-32*S.eye(137))/12288)
stationary=S.eye(137)-low-high
check('exact-spectral-polynomial',A*(A*A+32*S.eye(137))*(A*A+128*S.eye(137))==S.zeros(137))
check('low-band-rank36',rank(low)==36 and low*low==low)
check('high-band-rank2',rank(high)==2 and high*high==high)
check('stationary-band-rank99',rank(stationary)==99 and stationary==N)
check('spectral-bands-orthogonal',low*high==S.zeros(137) and low.T==low and high.T==high)
check('squared-frequency-action',Z*low==32*low and Z*high==128*high)
check('energy-from-exact-band-amplitudes',initial.energy==8*((low*F).T*(low*F)).trace()+32*((high*F).T*(high*F)).trace())
# A kernel vector is energetically invisible in THIS fixed dynamics but must
# remain retained. Another model/context need not give it zero energy.
k=next(N[:,j] for j in range(137) if N[:,j]!=S.zeros(137,1))
changed=F.copy()
changed[:,0]+=k
kernel_hostile=observer.observe(changed,'retained kernel perturbation')
check('equal-active-reader-does-not-identify-whole-state',kernel_hostile.active==initial.active and kernel_hostile.source!=initial.source)
check('energy-equality-does-not-discard-kernel',kernel_hostile.energy==initial.energy and observer.reconstruct(kernel_hostile)==changed)
try: observer.observe(F,'')
except ValueError: check('missing-observer-provenance-refused',True)
else: raise AssertionError('missing-observer-provenance-refused')
bad_target=T*F
bad_target[137,0]+=1
try: observer.observe_retained(bad_target,T,L,'hostile family mean')
except ValueError: check('inconsistent-family-value-chart-refused',True)
else: raise AssertionError('inconsistent-family-value-chart-refused')
result={
 'schema':'marici.strominger.retained-hamiltonian-observer.v1','verification_status':'pass','checks':checks,
 'source':'declared interface-preserving S4 skew-action combination; original candidate law not changed',
 'active_linear_coordinates_per_response_channel':38,'retained_kernel_coordinates_per_response_channel':99,
 'native_response_channels':4,'active_family_readout_rank':70,'residual_static_directions_beyond_joint_reader':67,
 'minimality_scope':'38 is minimal for exact quadratic-energy factorization through linear amplitude readers on the full137D coefficient space; not scalar detector count or minimal factored preparation',
 'source_fixture_energy':str(initial.energy),'factored_equal_mean_rival_energy':str(rival.energy),
 'squared_angular_frequency_bands':{'32':36,'128':2,'0':99},
 'active_reader':[[str(v) for v in C.row(i)] for i in range(38)],
 'active_energy_hessian':[[str(v) for v in w.target.K.row(i)] for i in range(38)],
 'energy_formula':'H4=(z^T K_active z)/2 summed over four response channels; z=C L target_retained',
 'original_J4_changed':False,'physical_detector_admitted':False,'physical_energy_or_clock_calibration':False,'Postnikov_identification':False,
 'full_state_retained':True,'input_sha256':{str(p.relative_to(ROOT.parent)).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest() for p in
                 (Path(__file__),HERE/'retained_hamiltonian_observer.py',HERE/'hamiltonian_descent_wg.py',HERE/'check_interface_preserving_carrier_dynamics.py')}
}
OUT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(f'PASS: {len(checks)} retained Hamiltonian observer checks')
print('Exact38-coordinate active reader determines declared energy; all99 kernel directions retained.')
print('Readout through complete native T9 works; originalJ4 stays unchanged. Physical detector/units and Postnikov gates remain open.')
