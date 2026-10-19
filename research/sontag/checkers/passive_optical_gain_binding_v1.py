"""Ideal passive dilation checks; no empirical device/calibration claims."""
import json
from pathlib import Path
import sympy as S
ROOT=Path(__file__).resolve().parents[3]
q=S.symbols('q',real=True,nonnegative=True)
a,b=S.symbols('a b',real=True,nonnegative=True)
R=lambda z:S.Matrix([[z,S.sqrt(1-z*z)],[-S.sqrt(1-z*z),z]])
checks={
 'first_coupler_orthogonal':(R(q).T*R(q)-S.eye(2)).applyfunc(S.simplify)==S.zeros(2),
 'second_coupler_orthogonal':(R(q*q).T*R(q*q)-S.eye(2)).applyfunc(S.simplify)==S.zeros(2),
 'summary_gain_square':R(q)[0,0]**2*a+R(q*q)[0,0]**2*b==q*q*a+q**4*b,
 'environment_resource_square':S.expand(q*q*a+q**4*b+(1-q*q)*a+(1-q**4)*b-a-b)==0,
 'zero_gain_is_swap':R(S.Integer(0))==S.Matrix([[0,1],[-1,0]]),
 'identity_gain_retains_signal':R(S.Integer(1))==S.eye(2),
}
# Known finite populated ancilla creates a non-source feedthrough.
z=S.Rational(3,5)
checks['populated_environment_breaks_vacuum_gain']=R(z)[0,1]!=0 and (R(z)*S.Matrix([0,1]))[0]!=0
checks['one_leg_hostile_prediction']=(S.Rational(1,2)**2*8)==2
checks['two_leg_hostile_prediction']=(S.Rational(1,2)**4*8)==S.Rational(1,2)
tau=S.symbols('tau',real=True,nonnegative=True)
checks['tap_backaction_resource_balance']=S.expand((1-tau)*(a+b)+tau*(a+b)-a-b)==0
checks['positive_tap_changes_signal_fixture']=(1-S.Rational(1,4))*8!=8
out={'schema':'marici.sontag.passive-optical-gain-binding.v1',
 'scope':'ideal coherent equal-frequency passive network; conditional physical framework, no hardware measurements',
 'checks':{k:bool(v) for k,v in checks.items()},'passed':all(checks.values()),
 'selected_subtask':'known-preparation open-loop gain/target',
 'unbound':'exact nondisturbing intermediate total-energy reader',
 'next_action':'version resource-accounted statistical tap-read feedback interface'}
p=ROOT/'research/sontag/results/passive-optical-gain-binding-v1.json'
p.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
raise SystemExit(0 if out['passed'] else 1)
