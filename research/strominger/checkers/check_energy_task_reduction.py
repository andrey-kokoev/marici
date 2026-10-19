# /// script
# dependencies = ["sympy"]
# ///
"""Energy-only sufficient state; existing common gain, no new actuator."""
from contextlib import redirect_stdout
from pathlib import Path
import hashlib
import io
import json
import runpy
import sympy as S
from sympy.polys.matrices import DomainMatrix
from energy_task_reduction import split_projectors,read_energy_task,gain_step,infer_components
from shared_leg_control_ports import response_field,vector_legs
from hamiltonian_descent_wg import zero

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
OUT=ROOT/'results/energy-task-reduction.json'
OUT.unlink(missing_ok=True)
with redirect_stdout(io.StringIO()):
    control=runpy.run_path(str(HERE/'check_shared_leg_controllability.py'))
model=control['model']
A=model['A']
F=control['F']
mean,one,two=split_projectors(control['P'])
checks=[]
def check(name,condition):
    if not condition: raise AssertionError(name)
    checks.append(name)
def rank(matrix): return DomainMatrix.from_Matrix(S.Matrix(matrix)).rank()

def energy(field): return S.simplify(((A*field).T*(A*field)).trace()/4)
check('prior29-control-audit-freshly-rerun',control['result']['verification_status']=='pass' and len(control['checks'])==29)
check('three-family-projectors-partition-source',mean+one+two==S.eye(137))
for name,P in (('mean',mean),('one-leg',one),('two-leg',two)):
    check('orthogonal-projector/'+name,P*P==P and P.T==P)
    check('source-drift-commutes/'+name,A*P==P*A)
check('projector-ranks32-56-49',tuple(rank(P) for P in (mean,one,two))==(32,56,49))
check('different-fluctuation-sectors-orthogonal',one*two==S.zeros(137))
check('mean-has-zero-declared-energy',A*mean==S.zeros(137))
check('active-fluctuation-ranks16-and22',rank(A*one)==16 and rank(A*two)==22)
state=read_energy_task(A,F,one,two,'supplied native fixture; declared coefficient Hamiltonian')
check('original-energy-two-term-decomposition',state.energy==energy(F)==control['prior']['initial'].energy)
check('matches-prior-gain-polynomial-coefficients',state.one_leg==control['a'] and state.two_leg==control['b'])
# Direct task readout through actual complete native T9; no changed J4.
check('retained-rung4-task-reader',read_energy_task(A,model['L']*model['T']*F,one,two,state.provenance)==state)
active_reconstructed=control['prior']['E']*control['prior']['initial'].active
check('existing-active-reader-already-sufficient',read_energy_task(A,active_reconstructed,one,two,state.provenance)==state)
check('free-drift-leaves-both-statistics-fixed',read_energy_task(A,model['U']*F,one,two,state.provenance)==state)
for q in (S.Rational(1,2),S.Rational(2,3),S.Integer(0),S.Integer(1)):
    field=(mean+q*one+q*q*two)*F
    task_step=gain_step(state,q)
    direct=read_energy_task(A,field,one,two,task_step.result.provenance)
    check('predicted-task-update/'+str(q),task_step.result==direct)
    exact_legs=vector_legs((control['Pleg']+q*control['Qleg'])*control['l0'],control['legs'])
    check('original-shared-leg-protocol-agrees/'+str(q),zero(response_field(exact_legs)-field))
check('gain-schedule-composition',gain_step(gain_step(state,S.Rational(2,3)).result,S.Rational(3,5)).result.one_leg
      ==gain_step(state,S.Rational(2,5)).result.one_leg and
      gain_step(gain_step(state,S.Rational(2,3)).result,S.Rational(3,5)).result.two_leg
      ==gain_step(state,S.Rational(2,5)).result.two_leg)
# Two energy readings recover the two statistics for any known nontrivial q.
after=gain_step(state,S.Rational(1,2)).result.energy
check('two-readings-recover-task-state',infer_components(state.energy,after,S.Rational(1,2))==(state.one_leg,state.two_leg))
q=S.symbols('q',real=True)
check('two-reading-determinant',S.Matrix([[1,1],[q*q,q**4]]).det()==q**4-q*q)

# Exact hostile with SAME complete family means and current energy, but
# one-leg versus two-leg disagreement. All primitive matrices invertible.
t=control['Q']*S.Matrix([i*i for i in range(11)])
check('nonzero-incoming-zero-mean-leg-pattern',all(v!=0 for v in t) and control['P']*t==S.zeros(11,1))
I=S.eye(2)
template=control['legs']
linear_legs=tuple((r,i,I if r=='ax' else t[i]*I if r=='ay' else M) for r,i,M in template)
bilinear_legs=tuple((r,i,t[i]*I if r in ('ax','ay') else M) for r,i,M in template)
FL=response_field(linear_legs)
FB=response_field(bilinear_legs)
aL=energy(FL)
bB=energy(FB)
scale=S.sqrt(aL/bB)
bilinear_legs=tuple((r,i,scale*M if r=='ax' else M) for r,i,M in bilinear_legs)
FB=response_field(bilinear_legs)
SL=read_energy_task(A,FL,one,two,'one-leg hostile')
SB=read_energy_task(A,FB,one,two,'two-leg hostile')
check('hostile-all-shared-legs-invertible',all(M.det()!=0 for _,_,M in linear_legs+bilinear_legs))
check('hostile-same-all-family-means',zero(model['means']*FL-model['means']*FB))
check('hostile-same-positive-current-energy',SL.energy==SB.energy and SL.energy>0)
check('hostile-distributes-energy-differently',SL.two_leg==0 and SB.one_leg==0)
nextL=gain_step(SL,S.Rational(1,2)).result.energy
nextB=gain_step(SB,S.Rational(1,2)).result.energy
check('current-energy-and-means-insufficient-for-next-energy',nextL==SL.energy/4 and nextB==SB.energy/16 and nextL!=nextB)
check('task-statistics-are-predictively-distinguishable',SL!=SB)
for qbad in (0,1):
    try: infer_components(state.energy,state.energy,qbad)
    except ValueError: check('uninformative-identification-gain-refused/'+str(qbad),True)
    else: raise AssertionError('uninformative identification gain')
try: gain_step(state,S.Integer(2))
except ValueError: check('extra-amplifier-not-introduced',True)
else: raise AssertionError('extra amplifier not introduced')
result={
 'schema':'marici.strominger.energy-task-reduction.v1','verification_status':'pass','checks':checks,
 'task':'predict the declared total coefficient energy under free drift and existing common family gain',
 'sufficient_statistics':{'one_leg':str(state.one_leg),'two_leg':str(state.two_leg)},
 'task_state_size':'two nonnegative scalar energies, summed across four response channels',
 'task_dynamics':'(a,b)->(q^2 a,q^4 b); free drift fixes(a,b); outputH=a+b',
 'current_energy_only_sufficient':False,'family_means_plus_current_energy_sufficient':False,
 'energy_task_full_mode_control_needed':False,'new_actuators_added':False,
 'identification':'currentH plus energy after known0<q<1 determine(a,b), conditional on actual calibrated energy/gain readings',
 'equal_energy_hostile':{'current':str(SL.energy),'next_one_leg':str(nextL),'next_two_leg':str(nextB),
                        'all_family_means_equal':True,'all_primitive_legs_invertible':True},
 'source_projector_ranks':{'mean':32,'one_leg_fluctuation':56,'two_leg_fluctuation':49},
 'active_projector_ranks':{'one_leg':16,'two_leg':22},
 'reduction_scope':'energy behaviour only; full137 leaves and histories retained, no physical state reset or detector minimality',
 'physical_selection_or_calibration':False,'Postnikov_identification':False,
 'input_sha256':{str(p.relative_to(ROOT.parent)).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest() for p in
                 (Path(__file__),HERE/'energy_task_reduction.py',HERE/'check_shared_leg_controllability.py')}
}
OUT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(f'PASS: {len(checks)} energy-task reduction checks')
print('Two energy components predict the existing gain protocol; current total energy and family means alone do not.')
print('No new independent mode controls are needed for this task. Physical calibration and source selection remain open.')
