"""Finite parity instrument, calibration, and inaccessible-record hostile."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json

routes = [(0,1,2,3),(0,1,3,2),(1,0,2,3),(1,0,3,2)]
parity = (1,-1,-1,1)
def source_parity(word):
    if len(word) != 4 or set(word[:2]) != {0,1} or set(word[2:]) != {2,3}:
        raise ValueError('Outside the declared ordered-pair block')
    return (1 if word[0]<word[1] else -1)*(1 if word[2]<word[3] else -1)
assert tuple(map(source_parity,routes)) == parity

def calibrated_mean(probabilities, flips):
    if len(probabilities)!=4 or sum(probabilities)!=1 or min(probabilities)<0:
        raise ValueError('Expected four route probabilities')
    if len(flips)!=2 or any(not F(0)<=q<F(1,2) for q in flips):
        raise ValueError('Unidentifiable or invalid marker error')
    return (1-2*flips[0])*(1-2*flips[1])*sum(p*s for p,s in zip(probabilities,parity))

positive = (F(1,2),F(0),F(0),F(1,2))
negative = (F(0),F(1,2),F(1,2),F(0))
q=(F(1,10),F(1,5))
gain=(1-2*q[0])*(1-2*q[1])
assert gain==F(12,25)
assert calibrated_mean(positive,q)==gain
assert calibrated_mean(negative,q)==-gain
# Enumerate independent marker flips explicitly.
for route, truth in zip(routes,parity):
    expectation=F(0)
    for f0,f1 in product((0,1),repeat=2):
        weight=(q[0] if f0 else 1-q[0])*(q[1] if f1 else 1-q[1])
        expectation+=weight*truth*(-1)**(f0+f1)
    assert expectation==gain*truth
# q0=q1=1/4 but perfectly correlated flips: parity gain 1, not 1/4.
correlated_gain = F(3,4)*1+F(1,4)*1
assert correlated_gain==1 and (1-2*F(1,4))**2!=correlated_gain
# Both mixtures have identical complete edge marginals.
def edge_weights(probabilities):
    out={}
    for p,word in zip(probabilities,routes):
        mask=0
        for j in word:
            e=(mask,mask | 1<<j,j)
            out[e]=out.get(e,F(0))+p
            mask=e[1]
    return {k:v for k,v in out.items() if v}
assert edge_weights(positive)==edge_weights(negative)
# Coherent sign kickback: marker |-> and controlled flip yield s_p|p>|->.
minus=(F(1),F(-1))  # common 1/sqrt(2) factor omitted
for sign in parity:
    actual=minus if sign==1 else minus[::-1]
    assert actual==tuple(sign*x for x in minus)
# Intensity is not the signed linear amplitude readout.
x=(F(1,2),)*4
z=tuple(F(s,2) for s in parity)
assert tuple(v*v for v in x)==tuple(v*v for v in z)
assert sum(s*v for s,v in zip(parity,x))==0
assert sum(s*v for s,v in zip(parity,z))==2
# Hoeffding: N >= (2/g^2) log(2/alpha); log(40)<4 at alpha=.05.
assert sum(F(4)**k/__import__('math').factorial(k) for k in range(10))>40
N=36
assert F(N)*gain*gain/2 >= 4
result={'schema':'marici.grothendieck.route-parity-instrument.v1','passed':True,
        'classical_gain':str(gain),'means':[str(gain),str(-gain)],
        'sufficient_trials_for_error_below_0.05_on_extremal_pair':N,
        'checks':{'source_parity':True,'independent_flip_enumeration':True,
                  'correlated_noise_hostile':True,'equal_edge_marginals':True,
                  'coherent_sign_kickback':True,'intensity_not_amplitude':True},
        'authority':'Conditional finite instrument only. No arithmetic source adapter or measured calibration supplied.'}
p=Path(__file__).resolve().parents[1]/'results/route-parity-instrument.json'
p.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
