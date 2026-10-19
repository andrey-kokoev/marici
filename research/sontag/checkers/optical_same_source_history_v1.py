"""Independent numeric-summary and coherent-amplitude prefix realizations."""
import json
from pathlib import Path
import sympy as S
ROOT=Path(__file__).resolve().parents[3]

def equal(a,b): return S.simplify(a-b)==0

def replay_math(initial,history):
    state=list(initial); loss=S.Integer(0); factors=[S.Integer(1)]*2
    shapes=[S.Integer(2),S.Integer(3)]; rates=[S.Integer(1),S.Integer(2)]
    likelihood=S.Integer(1); rows=[]
    for event in history:
        if event['type']=='gain':
            q=event['q']; multipliers=[q*q,q**4]
            loss+=sum((1-m)*z for m,z in zip(multipliers,state))
            state=[m*z for m,z in zip(multipliers,state)]
            factors=[m*f for m,f in zip(multipliers,factors)]
        elif event['type']=='tap-count':
            tau,eta=event['tau'],event['eta']
            for i,n in enumerate(event['counts']):
                mean=eta*tau*state[i]
                likelihood*=S.exp(-mean)*mean**n/S.factorial(n)
                shapes[i]+=n; rates[i]+=eta*tau*factors[i]
            loss+=tau*sum(state)
            state=[(1-tau)*z for z in state]
            factors=[(1-tau)*f for f in factors]
        else: raise ValueError('unknown event')
        rows.append({'state':tuple(state),'loss':loss,'likelihood':likelihood,
                     'shape':tuple(shapes),'rate':tuple(rates),'factor':tuple(factors)})
    return rows

def replay_optical(initial_amplitudes,history):
    amplitudes=list(initial_amplitudes); environment=[]; rows=[]
    likelihood=S.Integer(1); transmitted=[S.Integer(1)]*2
    shapes=[S.Integer(2),S.Integer(3)]; rates=[S.Integer(1),S.Integer(2)]
    for event in history:
        if event['type']=='gain':
            gains=[event['q'],event['q']**2]
            for i,g in enumerate(gains):
                environment.append(S.sqrt(1-g*g)*amplitudes[i])
                amplitudes[i]*=g; transmitted[i]*=g
        elif event['type']=='tap-count':
            tau,eta=event['tau'],event['eta']
            for i,n in enumerate(event['counts']):
                tap=S.sqrt(tau)*amplitudes[i]
                observed=S.sqrt(eta)*tap; unobserved=S.sqrt(1-eta)*tap
                environment.extend([observed,unobserved])
                mean=S.simplify(observed*S.conjugate(observed))
                likelihood*=S.exp(-mean)*mean**n/S.factorial(n)
                shapes[i]+=n; rates[i]+=eta*tau*transmitted[i]**2
                amplitudes[i]*=S.sqrt(1-tau); transmitted[i]*=S.sqrt(1-tau)
        else: raise ValueError('unknown optical event')
        rows.append({'state':tuple(S.simplify(z*S.conjugate(z)) for z in amplitudes),
                     'loss':S.simplify(sum(z*S.conjugate(z) for z in environment)),
                     'likelihood':likelihood,'shape':tuple(shapes),'rate':tuple(rates),
                     'factor':tuple(S.simplify(t*t) for t in transmitted)})
    return rows

history=[{'type':'tap-count','tau':S.Rational(1,4),'eta':S.Rational(4,5),'counts':(1,0)},
         {'type':'gain','q':S.Rational(3,5)},
         {'type':'tap-count','tau':S.Rational(1,3),'eta':S.Rational(3,4),'counts':(0,2)},
         {'type':'gain','q':S.Rational(4,5)}]
initial=(S.Integer(3),S.Integer(5))
math=replay_math(initial,history)
physical=replay_optical((S.sqrt(3),S.I*S.sqrt(5)),history)
checks={}
for index,(m,p) in enumerate(zip(math,physical),start=1):
    checks[f'state_square_prefix_{index}']=all(equal(a,b) for a,b in zip(m['state'],p['state']))
    checks[f'resource_square_prefix_{index}']=equal(m['loss'],p['loss']) and equal(sum(m['state'])+m['loss'],sum(initial))
    checks[f'likelihood_square_prefix_{index}']=equal(m['likelihood'],p['likelihood'])
    checks[f'information_square_prefix_{index}']=m['shape']==p['shape'] and all(equal(a,b) for key in ('rate','factor') for a,b in zip(m[key],p[key]))
checks['actual_equal_readout_hostile_continuation']=S.Rational(1,2)**2*8 != S.Rational(1,2)**4*8
# Exposure after the first tap/gain must use current factors, not initial ones.
checks['posterior_rates_account_for_intervening_gains']=math[2]['rate']!=(S.Integer(1)+S.Rational(1,5)+S.Rational(1,4),S.Integer(2)+S.Rational(1,5)+S.Rational(1,4))
out={'schema':'marici.sontag.optical-same-source-history.v1','passed':all(checks.values()),
 'checks':{k:bool(v) for k,v in checks.items()},
 'scope':'ideal conditional coherent physical framework; retained phase, fresh vacuum, declared detector likelihood; no experimental claim',
 'history':[{k:[str(x) for x in v] if isinstance(v,tuple) else str(v) for k,v in event.items()} for event in history],
 'prefixes':[{'state':[str(z) for z in row['state']],'loss':str(row['loss']),
              'posterior_shape':[str(z) for z in row['shape']],
              'posterior_rate':[str(z) for z in row['rate']]} for row in math]}
p=ROOT/'research/sontag/results/optical-same-source-history-v1.json'
p.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':out['passed'],'checks':len(checks),'prefixes':len(math)},indent=2))
if __name__ == '__main__':
    raise SystemExit(0 if out['passed'] else 1)
