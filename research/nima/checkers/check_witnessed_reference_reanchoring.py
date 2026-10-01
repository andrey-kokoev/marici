"""Fixed-domain reference substitution using retained comparison witnesses.

All actual slot paths stay fixed. The selected comparison supplies kappa with
boundary d_new-d. Unit and triangle witnesses get new versions by one explicit
rule; immutable parent frames remain available. No edit metric is needed.
"""
from dataclasses import dataclass
from collections import defaultdict
from copy import deepcopy
from itertools import product
from fractions import Fraction as F
from pathlib import Path
import runpy

m=runpy.run_path(str(Path(__file__).with_name('check_shared_leg_dg_realization.py')))
plus,minus,word=m['plus'],m['minus'],m['word']
arrows,old_delta,_,_,routes=m['build']({'a':(0,0),'s':(0,0)})
boundaries={a:old_delta(word(a)) for a in arrows}
arrows=dict(arrows)
for obj in ('A','U','V','B'):
    arrows['id'+obj]=(obj,obj,0); boundaries['id'+obj]={}
arrows.update({'return':('B','A',0),'unitA':('A','A',1),
               'unitB':('B','B',1),'triangle':('A','B',2)})
boundaries.update({'return':{},
    'unitA':plus(word('d','return'),minus(word('idA'))),
    'unitB':plus(word('return','d'),minus(word('idB'))),
    'triangle':plus(word('unitA','d'),minus(word('d','unitB')))})


def degree(path): return sum(arrows[a][2] for a in path)
def signature(path):
    assert path and all(arrows[a][1]==arrows[b][0] for a,b in zip(path,path[1:]))
    return arrows[path[0]][0],arrows[path[-1]][1],degree(path)


def normal(path):
    s,t,k=signature(path)
    reduced=tuple(a for a in path if not a.startswith('id'))
    if not reduced:
        assert s==t and k==0
        return ('id'+s,)
    assert signature(reduced)==(s,t,k)
    return reduced


def accumulate(out,path,coefficient):
    out[path]=out.get(path,F(0))+coefficient
    if not out[path]: del out[path]


def canon(chain):
    out={}
    for p,c in chain.items(): accumulate(out,normal(p),c)
    return out


def mul(a,b):  # a after b
    out={}
    for pa,ca in a.items():
        for pb,cb in b.items():
            assert signature(pb)[1]==signature(pa)[0]
            accumulate(out,normal(pb+pa),ca*cb)
    return out


def prod(*chains):
    out=chains[0]
    for c in chains[1:]: out=mul(out,c)
    return out


def scale(c,chain): return {p:c*v for p,v in chain.items() if c*v}

def delta(chain):
    out={}
    for p,c in chain.items():
        for i,a in enumerate(p):
            for replacement,b in boundaries[a].items():
                term=p[:i]+replacement+p[i+1:]
                assert signature(term)==(signature(p)[0],signature(p)[1],degree(p)-1)
                accumulate(out,normal(term),c*b*((-1)**degree(p[i+1:])))
    return out


anchors={'reference':word('d')}; hs={'reference':{}}; slots=[]
primitive=[e for e in product(range(4),repeat=2) if e[0]!=e[1] and e!=(0,1)]
groups=defaultdict(list)
for tag,size in (('a',11),('s',4)):
    for i in range(size):
        for j in range(size):
            key=f'{tag}:{i}:{j}'; slots.append(key)
            anchors[key]=word(f'{tag}x{i}',f'{tag}y{j}')
            hs[key]=routes(tag,i,j)[0]
            target=(tag,primitive[i][1],primitive[j][1]) if tag=='a' else (tag,i,j)
            groups[target].append(key)
# Literal incoming-family promotion adds one retained weighted anchor per group.
families={}
for n,members in enumerate(groups.values()):
    label=f'family:{n}'; families[label]=tuple(members)
    mass=F(1,len(members))
    anchors[label]=plus(*(scale(mass,anchors[key]) for key in members))
    hs[label]=plus(*(scale(mass,hs[key]) for key in members))
assert len(slots)==137 and len(families)==32 and len(anchors)==170
assert sorted(key for members in families.values() for key in members)==sorted(slots)
# A retained total-family anchor transports original member masses.
anchors['total']=plus(*(scale(F(len(members),137),anchors[label]) for label,members in families.items()))
hs['total']=plus(*(scale(F(len(members),137),hs[label]) for label,members in families.items()))
assert hs['total']==plus(*(scale(F(1,137),hs[key]) for key in slots))


@dataclass(frozen=True)
class Frame:
    reference: dict
    unitA: dict
    unitB: dict
    triangle: dict
    witnesses: dict
    parents: tuple=()
    selected: str='reference'

    def verify(self):
        assert delta(self.unitA)==plus(mul(word('return'),self.reference),minus(word('idA')))
        assert delta(self.unitB)==plus(mul(self.reference,word('return')),minus(word('idB')))
        assert delta(self.triangle)==plus(mul(self.reference,self.unitA),minus(mul(self.unitB,self.reference)))
        assert set(self.witnesses)==set(anchors)
        assert all(delta(h)==plus(anchors[key],minus(self.reference)) for key,h in self.witnesses.items())


def reanchor(old,label):
    k=old.witnesses[label]; r=word('return')
    result=Frame(anchors[label],plus(old.unitA,mul(r,k)),plus(old.unitB,mul(k,r)),
                 plus(old.triangle,mul(k,old.unitA),mul(old.unitB,k),prod(k,r,k)),
                 {key:plus(h,minus(k)) for key,h in old.witnesses.items()},(old,),label)
    result.verify()
    return result


def payload(frame):
    return frame.reference,frame.unitA,frame.unitB,frame.triangle,frame.witnesses


initial=Frame(word('d'),word('unitA'),word('unitB'),word('triangle'),hs)
initial.verify()
snapshot=deepcopy(payload(initial))
first=reanchor(initial,'family:0')
second=reanchor(first,'family:1')
direct=reanchor(initial,'family:1')
assert payload(second)==payload(direct) and second.parents==(first,) and direct.parents==(initial,)
assert payload(reanchor(first,'reference'))==payload(initial)
assert payload(reanchor(first,'family:0'))==payload(first)
assert payload(initial)==snapshot
centered=reanchor(initial,'total')
assert not plus(*(scale(F(1,137),centered.witnesses[key]) for key in slots))
# Every retained slot and every promoted family is an admissible reference
# candidate because its comparison witness is already present.
for key in slots+list(families):
    k=initial.witnesses[key]
    assert delta(k)==plus(anchors[key],minus(initial.reference))

# Exact mean and rectangle behaviour under the same reference shift.
mean_initial=plus(*(scale(F(1,137),hs[key]) for key in slots))
mean_first=plus(*(scale(F(1,137),first.witnesses[key]) for key in slots))
assert mean_first==plus(mean_initial,minus(hs['family:0']))
for tag,size in (('a',11),('s',4)):
    for i in range(1,size):
        for j in range(1,size):
            keys=(f'{tag}:{i}:{j}',f'{tag}:{i}:0',f'{tag}:0:{j}',f'{tag}:0:0')
            def rectangle(frame):
                a,b,c,e=(frame.witnesses[key] for key in keys)
                return plus(a,minus(b),minus(c),e)
            assert rectangle(initial)==rectangle(first)==rectangle(second)==rectangle(centered)
# Weighted family witnesses remain the weighted retained member witnesses.
for frame in (initial,first,second):
    for label,members in families.items():
        assert frame.witnesses[label]==plus(*(scale(F(1,len(members)),frame.witnesses[key]) for key in members))

# Existing finite matrix response sees the reference change with actual maps
# held fixed. It needs no history-sensitive weighting or feedback law.
values=m['values']; eval0=lambda chain:m['evaluate'](chain,values)
actual_before=tuple(eval0(anchors[key]) for key in slots)
old_d,new_d=eval0(initial.reference),eval0(first.reference)
assert old_d!=new_d
rho_selected=m['add'](new_d,m['scale'](-1,old_d))
for C in actual_before:
    old_rho=m['add'](C,m['scale'](-1,old_d))
    new_rho=m['add'](C,m['scale'](-1,new_d))
    assert new_rho==m['add'](old_rho,m['scale'](-1,rho_selected))
assert tuple(eval0(anchors[key]) for key in slots)==actual_before
mean=eval0(anchors['total'])
norm2=lambda a:sum((v*v for row in a for v in row),F(0))/2
energy=sum((norm2(m['add'](C,m['scale'](-1,old_d))) for C in actual_before),F(0))/137
variance=sum((norm2(m['add'](C,m['scale'](-1,mean))) for C in actual_before),F(0))/137
mean_cost=norm2(m['add'](mean,m['scale'](-1,old_d)))
assert energy==variance+mean_cost and mean_cost>0
assert eval0(centered.reference)==mean
print('137 actual slots and32 freshly labelled retained-family anchors carry explicit reference-change witnesses.')
print('One reanchoring rule passes two successive changes, direct/staged equality, return to the old reference and idempotence.')
print('Unit and triangle versions update exactly while parent records and actual slot maps remain unchanged.')
print('All109 rectangle witnesses are unchanged; the mean residual shifts by the selected anchor residual.')
print('Choosing the retained total mean as reference makes the mean residual zero while preserving all mixed defects; the exact mean/variance norm split passes.')
print('The comparison domain is explicitly fixed. Choosing a new physical exclusion mask or a reference-selection schedule remains separate.')
