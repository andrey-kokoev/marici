"""Filtered normal-symbol regressions. Exact arithmetic, no Rzk compilation."""
from fractions import Fraction
from math import factorial
from pathlib import Path
from datetime import datetime, timezone
import hashlib,json

# Integer polynomials in x,t,s; s is an unrelated spectator.
def add(a,b):
    out=dict(a)
    for k,v in b.items():
        out[k]=out.get(k,0)+v
        if not out[k]:del out[k]
    return out
def mul(a,b):
    out={}
    for ka,va in a.items():
        for kb,vb in b.items():out=add(out,{tuple(x+y for x,y in zip(ka,kb)):va*vb})
    return out
def restrict(a,axis):return {k:v for k,v in a.items() if k[axis]==0}
def divide_on_x_ideal(a):
    assert all(k[0]>=1 for k in a)
    return {(k[0]-1,k[1],k[2]):v for k,v in a.items()}
def first_t_symbol(a):
    # Output the coefficient of [t]; the conormal target is retained in spec.
    return {(k[0],0,k[2]):v for k,v in a.items() if k[1]==1}
x={(1,0,0):1};t={(0,1,0):1};s={(0,0,1):1};one={(0,0,0):1}
tx=mul(t,x)
a=add(add({(0,0,2):3},mul(t,s)),mul(x,add(one,s)))
beta=restrict(divide_on_x_ideal(mul(tx,a)),0)
assert beta==mul(t,restrict(a,0))
symbol=first_t_symbol(beta)
assert symbol==restrict(restrict(a,0),1)=={(0,0,2):3}
# Changing a fibre representative by t*b does not change the first symbol.
a_changed=add(a,mul(t,add(one,mul(s,s))))
assert first_t_symbol(restrict(divide_on_x_ideal(mul(tx,a_changed)),0))==symbol
assert restrict(tx,0)=={}  # Ordinary ambient restriction gives zero.
# K_x: d=x from degree 1 to 0; H=t from degree 0 to 1.
assert mul(x,t)==tx and mul(t,x)==tx  # dH in degree 0, Hd in degree 1
assert restrict(t,1)=={} and restrict(one,1)==one
# [tx] -> t[x] degenerates on t=0; cannot be a global unit change of frame.
assert restrict(t,1)!=one
for sign in (-1,1):assert sign*sign==1  # line and dual sign changes cancel

# Exterior contractions on a two-normal basis, in increasing label order.
def contraction(i,word):
    if i not in word:return {}
    pos=word.index(i)
    return {word[:pos]+word[pos+1:]: (-1)**pos}
def apply_contraction(i,v):
    out={}
    for word,c in v.items():
        for target,k in contraction(i,word).items():out=add(out,{target:c*k})
    return out
for word in ((),(0,),(1,),(0,1)):
    for i in (0,1):assert not apply_contraction(i,contraction(i,word))
    assert not add(apply_contraction(0,contraction(1,word)),apply_contraction(1,contraction(0,word)))

# Separate Q[[X]] fixture: U=(exp(X)-1)/X, U(0)=1; kappa=X^-1/U.
order=12
U=[Fraction(1,factorial(k+1)) for k in range(order+1)]
inv=[Fraction(1)]
for n in range(1,order+1):inv.append(-sum(U[k]*inv[n-k] for k in range(1,n+1)))
product=[sum(U[k]*inv[n-k] for k in range(n+1)) for n in range(order+1)]
assert product==[Fraction(1)]+[Fraction(0)]*order
kappa={n-1:c for n,c in enumerate(inv) if c}
f={0:Fraction(2),1:Fraction(3),2:Fraction(-1)}
def laurent_mul(a,b):
    out={}
    for i,c in a.items():
        for j,d in b.items():out[i+j]=out.get(i+j,Fraction(0))+c*d
    return {i:c for i,c in out.items() if c}
qminus={n:Fraction(1,factorial(n)) for n in range(1,order+2)}
normalized=laurent_mul(f,kappa)
cancelled=laurent_mul(qminus,normalized)
assert kappa[-1]==1 and normalized[-1]==f[0]
assert cancelled.get(-1,0)==0
assert all(cancelled.get(n,0)==f.get(n,0) for n in range(order+1))

spec=Path('research/nima/rzk-coefficient-interface-v4.md')
result={'status':'passed','checked_at':datetime.now(timezone.utc).isoformat(),
'spec_sha256':hashlib.sha256(spec.read_bytes()).hexdigest(),
'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
'integer_normal_fixture':{'connecting_symbol':'[t] tensor 3*s^2','framed_evaluation':'3*s^2','lift_independence_checked':True,'ambient_tx_fibre_value':0,'derived_ambient_tx_nullhomotopy':'H=t on K_x','conormal_change_degenerates_at_t_zero':True,'two_normal_koszul_signs':True},
'pole_fixture':{'coefficient_field':'Q','lambda':1,'series_order':order,'normalized_residue':str(normalized[-1]),'raw_factor_residue':str(cancelled.get(-1,0)),'pole_cancellation_verified':True},
'nonverification':['No Rzk terms compiled or full certificate validator implemented','No full localized source or spatial Gysin pipeline rerun','No global chart/overlap/endpoint/generic-Q naturality supplied','Finite series is a fixture, not a universal theorem by sampling']}
Path('research/nima/results/rzk_coefficient_interface_v4.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
