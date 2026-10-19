# /// script
# dependencies = ["sympy"]
# ///
"""Target-reaching certificate with probe cost and exact interval bounds."""
from contextlib import redirect_stdout
from pathlib import Path
import hashlib
import io
import json
import runpy
import sympy as S
from energy_task_reduction import EnergyTaskState,gain_step
from energy_target_controller import target_gain,safe_probe,finish_after_probe

HERE=Path(__file__).resolve().parent
OUT=HERE.parent/'results/energy-target-controller.json'
OUT.unlink(missing_ok=True)
with redirect_stdout(io.StringIO()):
    prior=runpy.run_path(str(HERE/'check_energy_task_reduction.py'))
checks=[]
def check(name,condition):
    if not condition: raise AssertionError(name)
    checks.append(name)
def rejects(name,call):
    try: call()
    except ValueError: check(name,True)
    else: raise AssertionError(name)
check('prior38-check-task-reduction-freshly-rerun',prior['result']['verification_status']=='pass' and len(prior['checks'])==38)
for a,b in ((0,0),(3,0),(0,5),(2,7),(S.Rational(1,3),S.Rational(7,5))):
    state=EnergyTaskState(S.sympify(a),S.sympify(b),'declared boundary control')
    for fraction in (0,S.Rational(1,4),S.Rational(1,2),1):
        target=fraction*state.energy
        q=target_gain(state,target)
        check(f'direct-target/{a}/{b}/{fraction}',S.simplify(gain_step(state,q).result.energy-target)==0)
# Universal algebraic certificate: a,b>=0 and q in[0,1].
a,b,q=S.symbols('a b q',nonnegative=True)
H=a+b
Hq=a*q*q+b*q**4
check('probe-lower-bound-identity',S.expand(Hq-q**4*H-a*q*q*(1-q*q))==0)
check('probe-upper-bound-identity',S.expand(q*q*H-Hq-b*q*q*(1-q*q))==0)
r=S.symbols('r',nonnegative=True)
check('safe-probe-target-margin',S.expand(((1+r)/2)**2-r-(1-r)**2/4)==0)
fixture=prior['state']
target=fixture.energy/2
probe=safe_probe(fixture.energy,target)
after=gain_step(fixture,probe).result.energy
probed,final=finish_after_probe(fixture.energy,after,probe,target,'exact model energy readings')
check('inference-recovers-original-components',probed.parent.one_leg==fixture.one_leg and probed.parent.two_leg==fixture.two_leg)
check('identification-pulse-is-not-free',after<fixture.energy and after>=target)
check('second-step-uses-probed-state',final.parent==probed.result)
check('target-reached-after-accounted-probe',S.simplify(final.result.energy-target)==0)
check('composite-gain-reaches-same-target',S.simplify(gain_step(fixture,probe*final.q).result.energy-target)==0)
# An arbitrary strong probe loses the ability to reach the former target.
bad_probe=S.Rational(1,2)
bad_after=gain_step(fixture,bad_probe).result.energy
check('strong-probe-undershoots-half-energy',bad_after<target)
rejects('free-reset-not-assumed',lambda:finish_after_probe(fixture.energy,bad_after,bad_probe,target,'hostile over-probe'))
rejects('amplification-refused',lambda:target_gain(fixture,2*fixture.energy))
rejects('negative-target-refused',lambda:target_gain(fixture,-1))
rejects('zero-state-cannot-create-energy',lambda:target_gain(EnergyTaskState(S.Integer(0),S.Integer(0),'zero'),1))
rejects('probe-for-no-change-is-unnecessary',lambda:safe_probe(fixture.energy,fixture.energy))
rejects('missing-protocol-provenance-refused',lambda:finish_after_probe(fixture.energy,after,probe,target,''))
# Identification conditioning: atq²=s, determinant=s(s-1), greatest
# absolute magnitude1/4 ats=1/2. This gain need not be safe for every target.
s=S.symbols('s',real=True)
check('maximal-two-reading-determinant-certificate',S.expand(S.Rational(1,4)-s*(1-s)-(s-S.Rational(1,2))**2)==0)
check('safe-probe-near-no-change-is-ill-conditioned',S.simplify(((1+r)/2)**2-(1+r)/2-(r*r-1)/4)==0)
result={
 'schema':'marici.strominger.energy-target-controller.v1','verification_status':'pass','checks':checks,
 'task':'reach lower declared model energy with existing common family gain',
 'direct_observer_controller':True,'probe_then_control':True,'new_actuators':False,
 'fixture':{'initial_energy':str(fixture.energy),'target':str(target),'probe_q':str(probe),
            'energy_after_probe':str(after),'final_q':str(final.q)},
 'safe_probe':'q²=(1+h/H)/2 for0<h<H; energy_after>=q⁴H>=h',
 'zero_target':'discrete q=0 allowed with retained history; continuous finite integrated gain reaches zero only as limit',
 'measurement_caveat':'exact model energies/gains; no back-action, noise, calibration or hardware admitted',
 'conditioning':'safe probe determinant=(r²-1)/4 tends to0 as target/initial r tends to1; no uniform noisy identification claim',
 'input_sha256':{str(p.relative_to(HERE.parent.parent)).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest() for p in
                (Path(__file__),HERE/'energy_target_controller.py',HERE/'energy_task_reduction.py',HERE/'check_energy_task_reduction.py')}
}
OUT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(f'PASS: {len(checks)} energy-target controller checks')
print('Exact lower-energy targeting with known components or accounted safe identification probe.')
print('No reset, amplifier, new actuator or physical calibration inferred.')
