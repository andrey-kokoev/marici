"""Test whether response-equivalent histories remain equivalent in context.

Fixed-frame composition descends to actual-map data. Protected reference-frame
updates can still distinguish histories through admission or recorded cost.
"""
from pathlib import Path
from fractions import Fraction as F
import runpy

scope=runpy.run_path(str(Path(__file__).with_name('check_return_observability_metric_gate.py')))
policy=scope['policy']; model=policy['m']
Map,add,mul,delta=policy['Map'],policy['add'],policy['mul'],policy['delta']
d,r=scope['d'],scope['r']
fixed=policy['fixed']; bases=(scope['ub'],scope['vb'],scope['wb'])
nu,nv,nw=map(len,bases)


def prod(*maps):
    out=maps[0]
    for item in maps[1:]: out=mul(out,item)
    return out


def composition(left,right,u):
    C1,h1=left; C2,h2=right
    C=prod(C2,r,C1)
    h=add(add(prod(h2,r,C1),prod(d,r,h1)),mul(d,u))
    assert delta(h)==add(C,d,-1)
    return C,h


def bracketings(records,u):
    a,b,c,e=records
    f=lambda left,right: composition(left,right,u)
    return [f(f(a,b),f(c,e)),f(f(f(a,b),c),e),f(f(a,f(b,c)),e),
            f(a,f(f(b,c),e)),f(a,f(b,f(c,e)))]


def observation(record):
    C,h=record
    return C,add(C,d,-1),delta(h)


original=[(record.actual,record.witness) for record in model['records']]
baseline=bracketings(original,fixed.u)
changed_histories=0; trials=0
for tangent in scope['hidden']:
    for coefficient in (F(1),F(-2)):
        vector=[coefficient*v for v in tangent]
        du=policy['reconstruct'](fixed.u,bases[0],vector[:nu])
        dv=policy['reconstruct'](fixed.v,bases[1],vector[nu:nu+nv])
        dw=policy['reconstruct'](fixed.triangle,bases[2],vector[nu+nv:])
        u=add(fixed.u,du); v=add(fixed.v,dv); W=add(fixed.triangle,dw)
        assert delta(u)==delta(fixed.u) and delta(v)==delta(fixed.v)
        assert delta(W)==add(mul(d,u),mul(v,d),-1)
        z=delta(dw)
        assert not delta(z).entries
        alternate=[(C,add(h,z)) for C,h in original]
        outcomes=bracketings(alternate,u)
        assert all(observation(x)==observation(y) for x,y in zip(outcomes,baseline))
        changed_histories+=any(x[1]!=y[1] for x,y in zip(outcomes,baseline))
        # A common further comparison still cannot turn a closed history
        # difference into an actual-map response difference.
        for x,y in zip(outcomes,baseline):
            assert observation(composition(x,original[0],u))==observation(composition(y,original[0],fixed.u))
        trials+=1
assert trials==28 and changed_histories>0

# A change of endpoint bases transports complete histories and therefore keeps
# equivalence. It is distinct from an active edit with unit histories locked.
G=Map('B','B',0,{(i,i):F(2 if i in (1,2,3,4) else 1) for i in range(9)})
assert not delta(G).entries
assert mul(G,baseline[0][0])==mul(G,baseline[-1][0])

# Operational counterexample: two coherent histories in a zero-differential
# X->Y frame. Their actual/reference/return maps and current responses agree.
policy['spaces']['Y']=(0,1); model['diffs']['Y']={}
id_values={(0,0):F(1),(1,1):F(1)}
d0=Map('X','Y',0,id_values); r0=Map('Y','X',0,dict(id_values))
u0=Map('X','X',1,{}); v0=Map('Y','Y',1,{})
u1=Map('X','X',1,{(1,0):F(1)}); v1=Map('Y','Y',1,{(1,0):F(1)})
state0=policy['select'](d0,r0,u0,v0)
state1=policy['select'](d0,r0,u1,v1)
assert state0 is not None and state1 is not None
assert delta(state0.u)==delta(state1.u) and delta(state0.v)==delta(state1.v)
# Install the same new agreement frame C'=d'=g, r'=g^-1, retaining both unit
# histories. This is an active protected edit, not a passive basis change.
d1=Map('X','Y',0,{(0,0):F(1),(1,1):F(2)})
r1=Map('Y','X',0,{(0,0):F(1),(1,1):F(1,2)})
assert mul(r1,d1)==model['identity']('X') and mul(d1,r1)==model['identity']('Y')
new_actual=d1
assert add(new_actual,d1,-1).entries=={}  # same agreement response in both cases
locked0=policy['select'](d1,r1,state0.u,state0.v,old_triangle=state0.triangle)
locked1=policy['select'](d1,r1,state1.u,state1.v,old_triangle=state1.triangle)
assert locked0 is not None and locked1 is None
assert add(mul(d1,u1),mul(v1,d1),-1).entries=={(1,0):F(1)}
# Permission to edit makes both requests feasible, but their declared costs differ.
editable0=policy['select'](d1,r1,u0,v0,protect=())
editable1=policy['select'](d1,r1,u1,v1,protect=())
assert editable0.edit_cost==0 and editable1.edit_cost==F(1,5)
assert editable1.u.entries=={(1,0):F(3,5)}
assert editable1.v.entries=={(1,0):F(6,5)}
# A genuine passive B-basis change transports v as well and has no obstruction.
g=Map('Y','Y',0,d1.entries); gi=Map('Y','Y',0,r1.entries)
v_transported=prod(g,v1,gi)
assert v_transported.entries=={(1,0):F(2)}
transported=policy['select'](d1,r1,u1,v_transported)
assert transported is not None and transported.edit_cost==0
print(f'Fixed-frame composition: all{trials} hidden-direction trials preserve actual/residual observations across five bracketings and a further comparison.')
print('Closed witness differences remain closed algebraically, so this response projection descends through every finite comparison word.')
print('Protected active frame edit: two initially coherent, response-equivalent histories give accept versus reject.')
print('With edits permitted both succeed, at declared costs0 and1/5; a fully transported passive basis change succeeds without an edit.')
print('Response equivalence is valid for fixed-frame composition, but not for the full protected-update protocol. No physical signal or coupling has been inferred from admission/cost.')
