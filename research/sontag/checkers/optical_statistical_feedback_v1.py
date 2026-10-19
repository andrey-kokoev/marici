"""Exact posterior/moment and policy fixtures, not empirical photon counts."""
import json
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/strominger/checkers'))
import sympy as S
from energy_task_reduction import EnergyTaskState, gain_step
from energy_target_controller import target_gain

def posterior_current(k,rho,n,tau,eta):
    if k<=0 or rho<=0 or n<0 or int(n)!=n or not 0<tau<1 or not 0<eta<=1:
        raise ValueError('invalid prior, count or instrument')
    shape=k+n; rate=rho+eta*tau
    return ((1-tau)*shape/rate,(1-tau)**2*shape/rate**2)

checks={}; traces=[]
tau,eta=S.Rational(1,4),S.Rational(4,5)
for n1,n2 in ((0,0),(1,0),(0,2),(3,4)):
    m1,v1=posterior_current(S.Integer(2),S.Integer(1),n1,tau,eta)
    m2,v2=posterior_current(S.Integer(3),S.Integer(2),n2,tau,eta)
    state=EnergyTaskState(m1,m2,'gamma prior; recorded tap counts')
    h=(m1+m2)/2
    q=target_gain(state,h)
    final=gain_step(state,q).result
    variance=S.simplify(q**4*v1+q**8*v2)
    checks[f'posterior_mean_target_{n1}_{n2}']=S.simplify(final.energy-h)==0
    checks[f'nonzero_uncertainty_{n1}_{n2}']=bool(variance>0)
    traces.append({'counts':[n1,n2],'current_means':[str(m1),str(m2)],'target':str(h),
                   'gain':str(q),'conditional_variance':str(variance)})
a,b,t,e=S.symbols('a b t e',real=True)
checks['tap_resource_ledger']=S.expand((1-t)*(a+b)+e*t*(a+b)+(1-e)*t*(a+b)-a-b)==0
# Poisson likelihood updates gamma kernel x^(k-1) exp(-rho*x)
x=S.symbols('x',positive=True)
k,rho,c=S.symbols('k rho c',positive=True)
n=S.symbols('n',integer=True,nonnegative=True)
checks['gamma_poisson_kernel']=S.simplify((x**(k-1)*S.exp(-rho*x))*(x**n*S.exp(-c*x))/(x**(k+n-1)*S.exp(-(rho+c)*x)))==1
def count_likelihood(components, counts):
    return S.prod(S.exp(-eta*tau*z)*(eta*tau*z)**count/S.factorial(count)
                  for z,count in zip(components,counts))
left_likelihood=count_likelihood((8,0),(0,0))
right_likelihood=count_likelihood((0,8),(0,0))
checks['zero_counts_do_not_identify_equal_total_sectors']=(left_likelihood>0 and left_likelihood/(left_likelihood+right_likelihood)==S.Rational(1,2))
checks['channel_click_distinguishes_discrete_sectors']=(count_likelihood((8,0),(1,0))>0 and count_likelihood((0,8),(1,0))==0)
# Current mean must include tap attenuation; old exact target formula on the
# pre-tap state undershoots its intended post-control occupation.
pre=EnergyTaskState(S.Integer(3),S.Integer(5),'known hostile preparation')
h=S.Integer(4); wrong=target_gain(pre,h)
current=EnergyTaskState((1-tau)*pre.one_leg,(1-tau)*pre.two_leg,'actual tapped preparation')
checks['pre_tap_controller_undershoots']=S.simplify(gain_step(current,wrong).result.energy-(1-tau)*h)==0
checks['pre_tap_reset_rejected']=S.simplify(gain_step(current,wrong).result.energy-h)!=0
invalid=False
try: posterior_current(2,1,-1,tau,eta)
except ValueError: invalid=True
checks['invalid_count_rejected']=invalid
out={'schema':'marici.sontag.optical-statistical-feedback.v1','passed':all(checks.values()),
 'scope':'conditional coherent photon-count model and supplied gamma priors; fixtures are not measurements',
 'checks':{k:bool(v) for k,v in checks.items()},'traces':traces,
 'success_type':'conditional expected signal occupation, not samplewise exact energy'}
p=ROOT/'research/sontag/results/optical-statistical-feedback-v1.json'
p.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':out['passed'],'checks':len(checks),'traces':len(traces)},indent=2))
raise SystemExit(0 if out['passed'] else 1)
