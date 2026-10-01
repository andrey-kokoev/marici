"""State-derived preparation from retained incoming-family disagreement.

Adds a declared relaxation principle. The gain and interpretation of its
quadratic metric are not supplied by the carrier or witness algebra.
"""
from collections import defaultdict
from contextlib import redirect_stdout
from fractions import Fraction as F
from itertools import permutations, product
from pathlib import Path
import io
import json
import runpy

ROOT=Path(__file__).resolve().parents[3]
out=ROOT/'research/nima/results/family-disagreement-preparation.json'
out.unlink(missing_ok=True)
with redirect_stdout(io.StringIO()):
    model=runpy.run_path(str(Path(__file__).with_name('check_rung_transport_diagram.py')))
m=model['m']; add,scale,mul=(m[k] for k in ('add','scale','mul'))
I,Z=m['I'],m['Z']; E=model['E']; d=model['physical_reference'].value

def sub(a,b): return add(a,scale(-1,b))
def total(xs):
    result=Z
    for x in xs: result=add(result,x)
    return result

def avg(xs): return scale(F(1,len(xs)),total(xs))
def transpose(a): return tuple(zip(*a))
def inverse(a):
    det=a[0][0]*a[1][1]-a[0][1]*a[1][0]
    assert det
    return ((a[1][1]/det,-a[0][1]/det),(-a[1][0]/det,a[0][0]/det))
metric=((F(2),F(1)),(F(1),F(2)))
def inner(a,b):
    c=mul(mul(mul(inverse(metric),transpose(a)),metric),b)
    return c[0][0]+c[1][1]
def norm(a):
    value=inner(a,a)
    assert value>=0
    return value

def rho(h): return tuple(tuple(F((h[j]==i)-(h[3]==i)) for j in (1,2)) for i in (1,2))
def act(h,a): return mul(mul(rho(h),a),inverse(rho(h)))

legs={(tag,role,i):m['values'][f'{tag}{role}{i}']
      for tag,n in (('a',11),('s',4)) for role in ('x','y') for i in range(n)}
def group_key(key,edges=E):
    tag,role,i=key
    return tag,role,edges[i][1] if tag=='a' else i

def project(values,edges=E):
    groups=defaultdict(list)
    for key in values: groups[group_key(key,edges)].append(key)
    return {key:avg([values[k] for k in keys]) for keys in groups.values() for key in keys}

def relax(values,eta):
    p=project(values)
    kick={key:scale(eta,sub(p[key],value)) for key,value in values.items()}
    return {key:add(value,kick[key]) for key,value in values.items()},kick

def slots(values):
    return [mul(values[tag,'y',j],values[tag,'x',i])
            for tag,n in (('a',11),('s',4)) for i,j in product(range(n),repeat=2)]

p=project(legs); delta={key:sub(legs[key],p[key]) for key in legs}
assert project(p)==p
assert all(value==Z for value in project(delta).values())
energy=sum(norm(value) for value in delta.values())
assert energy>0
baseline=slots(legs); family_slot_means=slots(p)
linear=[]; quadratic=[]
for tag,n in (('a',11),('s',4)):
    for i,j in product(range(n),repeat=2):
        x,y=(tag,'x',i),(tag,'y',j)
        linear.append(add(mul(p[y],delta[x]),mul(delta[y],p[x])))
        quadratic.append(mul(delta[y],delta[x]))
assert all(sub(c,b)==add(l,q) for c,b,l,q in zip(baseline,family_slot_means,linear,quadratic))
assert sum(inner(l,q) for l,q in zip(linear,quadratic))==0
EL=sum(norm(l) for l in linear); EQ=sum(norm(q) for q in quadratic)
assert EL>0 and EQ>0
# This is the SAME32 target-family partition as the actual rung fixture.
indices=defaultdict(list)
for i,row in enumerate(model['source']): indices[row.target].append(i)
assert len(indices)==32
for members in indices.values():
    expected=avg([baseline[i] for i in members])
    assert all(family_slot_means[i]==expected for i in members)

for eta in (F(0),F(1,2),F(1),F(3,2)):
    updated,kick=relax(legs,eta); updated_slots=slots(updated); q=1-eta
    assert project(updated)==p
    assert all(sub(updated[key],kick[key])==legs[key] for key in legs)
    assert sum(norm(sub(updated[key],p[key])) for key in legs)==q*q*energy
    assert avg(updated_slots)==avg(baseline)
    assert avg([sub(c,d) for c in updated_slots])==avg([sub(c,d) for c in baseline])
    for members in indices.values():
        assert avg([updated_slots[i] for i in members])==avg([baseline[i] for i in members])
    assert all(c==add(b,add(scale(q,l),scale(q*q,z)))
               for c,b,l,z in zip(updated_slots,family_slot_means,linear,quadratic))
    assert sum(norm(sub(c,b)) for c,b in zip(updated_slots,family_slot_means))==q*q*EL+q**4*EQ
    if eta==1: assert updated_slots==family_slot_means and updated!=legs
# Composition is exact for a fixed retained partition, not a chosen time law.
for a,b in product((F(0),F(1,2),F(1),F(3,2)),repeat=2):
    first,_=relax(legs,a); second,_=relax(first,b)
    direct,_=relax(legs,a+b-a*b)
    assert second==direct

# The projector commutes with common witness action. A preparation after that
# action is B=eta*(P(T_h A)-T_h A); it is computed, not independently fitted.
for h in (g for g in permutations(range(4)) if g[0]==0):
    transported={key:act(h,value) for key,value in legs.items()}
    out_h,kick_h=relax(transported,F(1,2))
    out_plain,_=relax(legs,F(1,2))
    assert out_h=={key:act(h,value) for key,value in out_plain.items()}
    for value in legs.values(): assert norm(act(h,value))==norm(value)
    assert {key:act(tuple(h.index(i) for i in range(4)),sub(out_h[key],kick_h[key]))
            for key in legs}==legs
# Passive carrier relabelling moves the reference exclusion and grouping keys.
for relabel in permutations(range(4)):
    moved=[(relabel[i],relabel[j]) for i,j in E]
    assert project(legs,moved)==p
# No spontaneous preparation: a family-constant state receives no kick.
assert all(b==Z for b in relax(p,F(1,2))[1].values())

result={
 'status':'passed',
 'classification':'family_disagreement_feedback_computes_preparation_and_preserves_retained_response_means',
 'obligation':'declared source feedback, transport compatibility and retained reconstruction',
 'stratum':'Actual30 shared legs, incoming-family partition, equal member masses, common S3 action, explicit quadratic metric and relaxation gain',
 'checks':{'primitive_legs':30,'comparison_slots':137,'target_slot_families':32,
           'preparation_computed_from_current_records':True,'member_recovery_from_retained_kicks':True,
           'all_family_and_global_means_preserved':True,'fixed_reference_mean_preserved':True,
           'leg_energy_contraction':True,'slot_energy_quadratic_and_quartic_scaling':True,
           'gain_composition':True,'witness_action_compatibility':True,
           'passive_carrier_relabelling':True,'family_constant_states_receive_no_drive':True},
 'energies':{'leg_disagreement':str(energy),'slot_linear':str(EL),'slot_quadratic':str(EQ)},
 'unsupported':['physical justification of relaxation objective or gain',
                'physical energy identification','initial amplitude generation',
                'changing-partition gain law','independent per-leg witness actions'],
 'next_constructor':'Identify a source preparation/calibration operation implementing this family-disagreement feedback, or reject relaxation as the physical policy.'
}
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
