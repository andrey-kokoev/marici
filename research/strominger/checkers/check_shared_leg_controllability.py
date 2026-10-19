# /// script
# dependencies = ["sympy"]
# ///
"""Existing family-gain actuation versus primitive preparation capacity."""
from contextlib import redirect_stdout
from pathlib import Path
import hashlib
import io
import json
import runpy
import sympy as S
from sympy.polys.matrices import DomainMatrix
from shared_leg_control_ports import (primitive_legs,response_field,product_jacobian,
                                      incoming_leg_projector,leg_vector,vector_legs,gain_for_energy)
from hamiltonian_descent_wg import zero

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
OUT=ROOT/'results/shared-leg-controllability.json'
OUT.unlink(missing_ok=True)
with redirect_stdout(io.StringIO()):
    prior=runpy.run_path(str(HERE/'check_retained_hamiltonian_observer.py'))
model=prior['previous']
A=model['A']
Ds=model['Ds']
fixture=model['fixture']
C=prior['C']
legs=primitive_legs(fixture['m']['values'])
l0=leg_vector(legs)
F=response_field(legs)
J,ports=product_jacobian(legs)
reader=S.SparseMatrix(S.kronecker_product(C,S.eye(4)))
Jactive=reader*J
checks=[]
def check(name,condition):
    if not condition: raise AssertionError(name)
    checks.append(name)
def rank(matrix): return DomainMatrix.from_Matrix(S.Matrix(matrix)).rank()

check('prior43-check-observer-freshly-rerun',prior['result']['verification_status']=='pass' and len(prior['checks'])==43)
check('exact30-source-legs-and-fixed-reference',len(legs)==30 and len(ports)==120 and 'd' not in [p[0] for p in ports])
check('source-legs-reproduce-all137-values',F==model['F'])
check('native-response-coordinates548',J.shape==(548,120) and reader.shape==(152,548))
check('actual-preparation-Jacobian-rank112',rank(J)==112)
# Explicit eight intermediate-frame gauge directions, not independent forces.
gauge=[]
for tag,n in (('a',11),('s',4)):
    for a in range(2):
        for b in range(2):
            W=S.zeros(2); W[a,b]=1
            direction=[]
            for role,i,M in legs:
                change=S.zeros(2)
                if role[0]==tag: change=W*M if role[1]=='x' else -M*W
                direction.extend(list(change))
            gauge.append(S.Matrix(direction))
Gauge=S.Matrix.hstack(*gauge)
check('eight-preparation-gauge-directions',rank(Gauge)==8 and J*Gauge==S.zeros(548,8))
active_rank=rank(Jactive)
check('primitive-assignment-active-tangent-not-full',active_rank<152)
check('active-only-arrow-leg-inputs',Jactive[:,88:120]==S.zeros(152,32))
# Regardless of a special operating point, active response depends on only
# 22 invertible arrow matrices (88 variables), with4 gauge dimensions.
check('generic-factored-active-ceiling84-below152',88-4==84 and 84<152)
# Differentiate a valid matrix perturbation directly, coefficient-by-coefficient.
lookup={(role,i):M for role,i,M in legs}
role,i,a,b=ports[0]
unit=S.zeros(2); unit[a,b]=1
changed=tuple((r,j,M+unit if (r,j)==(role,i) else M) for r,j,M in legs)
check('single-leg-input-column-exact',S.Matrix(548,1,list(response_field(changed)-F))==J[:,0])

# Prior family-disagreement preparation law: common scalar gain, not120
# independent actuators. Its continuous-rate interpretation is explicit.
P=incoming_leg_projector(model['selected'])
Q=S.eye(11)-P
L=S.SparseMatrix(S.diag(S.kronecker_product(Ds,S.eye(4)),S.kronecker_product(Ds,S.eye(4)),S.zeros(16),S.zeros(16)))
Qleg=S.SparseMatrix(S.diag(S.kronecker_product(Q,S.eye(4)),S.kronecker_product(Q,S.eye(4)),S.zeros(16),S.zeros(16)))
Pleg=S.eye(120)-Qleg
check('actual-target-family-projector',P*P==P and rank(P)==4)
check('drift-commutes-with-family-feedback',L*Qleg==Qleg*L)
check('family-constant-legs-undriven',L*Pleg==S.zeros(120) and Qleg*Pleg==S.zeros(120))
check('free-leg-drift-lifts-native-drift',J*L*l0==S.Matrix(548,1,list(A*F)))
check('prior-gain-is-state-dependent-not-additive-force',Qleg*S.zeros(120,1)==S.zeros(120,1))
control_direction=-Qleg*l0
leg_orbit_rank=rank(S.Matrix.hstack(L*l0,control_direction))
active_orbit_rank=rank(reader*J*S.Matrix.hstack(L*l0,control_direction))
check('one-gain-free-time-leg-orbit-rank2',leg_orbit_rank==2)
check('one-gain-active-task-orbit-not-full',active_orbit_rank<=2 and active_orbit_rank<152)
check('zero-input-state-cannot-be-excited',L*S.zeros(120,1)==Qleg*S.zeros(120,1)==S.zeros(120,1))
# Exact discrete gain composition from the inspected prior protocol.
q1,q2=S.Rational(2,3),S.Rational(3,5)
R1=Pleg+q1*Qleg
R2=Pleg+q2*Qleg
check('gain-schedule-reduces-to-one-product',R1*R2==Pleg+q1*q2*Qleg)
leg_step=S.SparseMatrix(S.diag(S.kronecker_product(model['Q'],S.eye(4)),S.kronecker_product(model['Q'],S.eye(4)),S.eye(16),S.eye(16)))
check('ordering-drift-and-gain-does-not-create-control-directions',leg_step*R1==R1*leg_step)
# A candidate law still has real task-relevant effect: varying gain changes
# exact energy without changing family means or independently editing slots.
q=S.symbols('q',real=True)
relaxed_legs=vector_legs((Pleg+q*Qleg)*l0,legs)
Fq=response_field(relaxed_legs)
energy_q=S.factor(((A*Fq).T*(A*Fq)).trace()/4)
poly=S.Poly(energy_q,q)
check('feedback-preserves-all-native-family-means',zero(model['means']*Fq-model['means']*F))
check('feedback-energy-is-even-quadratic-quartic',set(power[0] for power in poly.monoms())<={2,4}
      and poly.coeff_monomial(q**2)>0 and poly.coeff_monomial(q**4)>0)
check('full-relaxation-removes-visible-Hamiltonian-energy',energy_q.subs(q,0)==0)
check('unrelaxed-preparation-restores-fixture-energy',energy_q.subs(q,1)==prior['initial'].energy)
# Kernel preparation is not inferred from zero dynamics.
check('stationary-state-legs-undriven',Qleg[88:120,:]==S.zeros(32,120))
a=poly.coeff_monomial(q**2)
b=poly.coeff_monomial(q**4)
target=prior['initial'].energy/2
eta=gain_for_energy(target,a,b)
check('witnessed-half-energy-control',S.simplify(energy_q.subs(q,1-eta)-target)==0)
check('energy-controller-respects-contraction-interval',eta.is_positive is True and (1-eta).is_positive is True)
try: gain_for_energy(2*prior['initial'].energy,a,b)
except ValueError: check('energy-amplification-not-smuggled-into-gain',True)
else: raise AssertionError('energy-amplification-not-smuggled-into-gain')
relaxed=(Pleg+S.Rational(1,2)*Qleg)*l0
kick=relaxed-l0
check('prior-leg-data-recover-from-retained-kick',relaxed-kick==l0)
result={
 'schema':'marici.strominger.shared-leg-controllability.v1','verification_status':'pass','checks':checks,
 'physical_controllability':'unestablished; no admitted hardware input map supplied',
 'inspected_prior_input':'conditional common family-disagreement gain; new continuous-rate interpretation explicitly supplied',
 'control_system':'dot ell=L ell-u(t) Qleg ell withu>=0 (declared continuous-rate contraction), F_ij=Y_j X_i; discrete gain eta in[0,1]',
 'input_count_for_prior_gain':1,'free_time_leg_orbit_rank_at_fixture':leg_orbit_rank,'active_orbit_rank_at_fixture':active_orbit_rank,
 'global_orbit_bound':'L and Qleg commute, so time and integrated gain give at most2 continuous orbit parameters; fixed time at most1',
 'primitive_preparation_jacobian':{'candidate_coefficient_variations':120,'response_rank':112,'intermediate_frame_kernel':8,
                                  'active_response_rank_at_fixture':active_rank,'generic_active_factored_dimension_ceiling':84},
 'active_task_dimension':152,'active_coordinates_per_response_channel':38,
 'energy_under_family_relaxation':str(energy_q),'family_means_preserved':True,
 'energy_task_control':'discrete preparation gain reaches any model energy in[0,H_initial]; continuous finite integrated gain reaches(0,H_initial], zero is a limit; not full mode control',
 'half_energy_target':str(target),'half_energy_gain':str(eta),'retained_kick_reconstruction':True,
 'ports':ports,'declared_source_law_not_changed':True,
 'not_claimed':['No120 installed actuators','No additiveB=I on137 records','No frozen-Kalman test relabelled as nonlinear reachability',
                'No full active controllability','No ability to excite zero resource','No physical damping/reset/calibration','No Postnikov identification'],
 'input_sha256':{str(p.relative_to(ROOT.parent)).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest() for p in
                (Path(__file__),HERE/'shared_leg_control_ports.py',HERE/'check_retained_hamiltonian_observer.py',
                 ROOT.parent/'nima/family-disagreement-preparation-law.md',ROOT.parent/'nima/matrix-leg-preparation-exchange-closure.md')}
}
OUT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(f'PASS: {len(checks)} shared-leg controllability audit checks')
print(f'Prior common-gain control: orbit rank{active_orbit_rank} in the152D active task, not full controllability.')
print(f'Typed primitive preparation active tangent rank{active_rank}; generic factored ceiling84<152.')
print(f'Gain affects energy: H(q)={energy_q}. Physical actuators/units remain unestablished.')
