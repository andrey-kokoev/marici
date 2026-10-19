"""Symbolic energy squares; tuple illustration is not an Agda check."""
import json
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/strominger/checkers'))
import sympy as S
from energy_task_reduction import EnergyTaskState, gain_step
from energy_target_controller import target_gain, safe_probe

def phi(a,b): return (a+b,a)
def psi(H,A): return (A,H-A)
def chart_step(H,A,q): return (q**4*H+(q**2-q**4)*A,q**2*A)
def eq(x,y): return all(S.simplify(a-b)==0 for a,b in zip(x,y))
a,b,H,A,q,r = S.symbols('a b H A q r', real=True)
checks = {
    'component_chart_inverse':eq(psi(*phi(a,b)),(a,b)),
    'energy_chart_inverse':eq(phi(*psi(H,A)),(H,A)),
    'transition_square':eq(phi(q**2*a,q**4*b),chart_step(*phi(a,b),q)),
    'composition_square':eq(chart_step(*chart_step(H,A,q),r),chart_step(H,A,r*q)),
    'observation_square':S.simplify(phi(a,b)[0]-(a+b))==0,
    'visible_resource_square':S.simplify(chart_step(*phi(a,b),q)[0]-(a+b)-(q**2*a+q**4*b-a-b))==0,
}
policy_checks=[]
for x,y in ((3,5),(0,8),(8,0)):
    state=EnergyTaskState(S.Integer(x),S.Integer(y),'retained fixture')
    h=state.energy/2
    probe=safe_probe(state.energy,h)
    current=gain_step(state,probe).result
    chart=chart_step(*phi(S.Integer(x),S.Integer(y)),probe)
    recovered=EnergyTaskState(*psi(*chart),'chart retained fixture')
    decision=target_gain(current,h)
    transported=target_gain(recovered,h)
    policy_checks.append(S.simplify(decision-transported)==0)
    policy_checks.append(eq(phi(current.one_leg,current.two_leg),chart))
checks['probe_and_policy_transport_fixtures']=all(policy_checks)
checks['H_only_chart_hostile']=phi(8,0)[0]==phi(0,8)[0] and chart_step(*phi(8,0),S.Rational(1,2))[0]!=chart_step(*phi(0,8),S.Rational(1,2))[0]
# Paired data only: illustrates reshaping without deleting witness payload.
s,p,z='base','admission-F','admission-G'
w,e,f='base-witness','extra-F',('depends-on','extra-F')
flatten_state=lambda t:(t[0][0],t[0][1],t[1])
unflatten_state=lambda t:((t[0],t[1]),t[2])
checks['WG_tuple_roundtrip_illustration']=unflatten_state(flatten_state(((s,p),z)))==((s,p),z)
checks['WG_payload_roundtrip_illustration']=unflatten_state(flatten_state(((w,e),f)))==((w,e),f)
out={'schema':'marici.sontag.presentation-naturality.v1',
     'scope':'symbolic energy chart and policy fixtures; WG tuple illustration only, dependent maps inspected separately',
     'checks':{k:bool(v) for k,v in checks.items()},'passed':all(checks.values())}
pth=ROOT/'research/sontag/results/presentation-naturality-v1.json'
pth.parent.mkdir(parents=True,exist_ok=True)
pth.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
raise SystemExit(0 if out['passed'] else 1)
