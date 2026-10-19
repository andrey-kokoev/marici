"""Adaptive same-source trace and preparation-uncertainty accuracy audit."""
import importlib.util
import json
import sys
from pathlib import Path
import sympy as S
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/strominger/checkers'))
from energy_task_reduction import EnergyTaskState
from energy_target_controller import target_gain
spec=importlib.util.spec_from_file_location('comparison',ROOT/'research/sontag/checkers/optical_same_source_history_v1.py')
c=importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)  # reruns and records the independent-prefix dependency

def decision(info,target):
    # ONLY public prior/count-derived information, not info['state'].
    means=[S.simplify(f*k/r) for f,k,r in zip(info['factor'],info['shape'],info['rate'])]
    return target_gain(EnergyTaskState(*means,'public posterior transcript'),target)

checks={}; rows=[]
for n in (0,2):
    history=[{'type':'tap-count','tau':S.Rational(1,4),'eta':S.Rational(4,5),'counts':(n,0)}]
    initial=(S.Integer(3),S.Integer(5))
    info=c.replay_math(initial,history)[-1]
    h=S.Rational(1,2)
    q=decision(info,h)
    # Independent amplitude replay uses a numeric gain to avoid expensive
    # conjugate/radical normalization; comparison tolerance is explicit.
    history.append({'type':'gain','q':S.Float(str(S.N(q,17)))})
    m=c.replay_math(initial,history)
    p=c.replay_optical((S.sqrt(3),S.I*S.sqrt(5)),history)
    for j,(u,v) in enumerate(zip(m,p)):
        checks[f'adaptive_state_square_{n}_{j}']=all(abs(float(S.N(a-b)))<1e-12 for a,b in zip(u['state'],v['state']))
        checks[f'adaptive_resource_square_{n}_{j}']=abs(float(S.N(u['loss']-v['loss'])))<1e-12
    final=m[-1]
    means=[S.simplify(f*k/r) for f,k,r in zip(final['factor'],final['shape'],final['rate'])]
    variances=[S.simplify(f*f*k/(r*r)) for f,k,r in zip(final['factor'],final['shape'],final['rate'])]
    variance=S.simplify(sum(variances)); K=sum(final['shape'])
    checks[f'conditional_mean_target_{n}']=abs(float(S.N(sum(means)-h)))<1e-12
    checks[f'variance_floor_{n}']=bool(S.N(variance-h*h/K)>-1e-12)
    # Evaluate the sufficient Chebyshev certificate at 25% relative error,
    # failure probability 5%. Failure is not proof of the actual tail value.
    eps=h/4; delta=S.Rational(1,20)
    checks[f'strict_accuracy_certificate_rejected_{n}']=bool(S.N(variance/(eps*eps))>delta)
    spoof=dict(info,state=(S.Integer(999),S.Integer(999)))
    checks[f'hidden_state_not_used_{n}']=c.equal(decision(spoof,h),q)
    rows.append({'first_count':n,'gain':str(q),'target':str(h),
                 'conditional_variance':str(variance),'posterior_shape_sum':str(K),
                 'chebyshev_bound':str(min(S.Integer(1),variance/(eps*eps))),
                 'requested_failure_probability':str(delta),'certificate_passes':False})
checks['feedback_changes_with_observed_count']=rows[0]['gain']!=rows[1]['gain']
# Cauchy-Schwarz identity proves variance >= (m1+m2)^2/(k1+k2).
m1,m2,k1,k2=S.symbols('m1 m2 k1 k2',positive=True)
checks['variance_floor_identity']=S.simplify(m1*m1/k1+m2*m2/k2-(m1+m2)**2/(k1+k2)-(k2*m1-k1*m2)**2/(k1*k2*(k1+k2)))==0
out={'schema':'marici.sontag.optical-adaptive-feedback-accuracy.v1','passed':all(checks.values()),
 'checks':{k:bool(v) for k,v in checks.items()},'traces':rows,
 'scope':'conditional ideal coherent/Gamma-prior model; numeric adaptive replay tolerance 1e-12, symbolic variance identity; fixture counts, no measurements',
 'rejected':'5% failure certificate at 25% relative preparation-mean error for these posterior contexts',
 'not_claimed':'actual tail probability failure, photon-number precision, or physical calibration'}
pth=ROOT/'research/sontag/results/optical-adaptive-feedback-accuracy-v1.json'
pth.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':out['passed'],'checks':len(checks),'traces':len(rows)},indent=2))
raise SystemExit(0 if out['passed'] else 1)
