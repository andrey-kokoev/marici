"""Literal record-endpoint composition, distinguished from matrix bridging."""
from collections import defaultdict
from contextlib import redirect_stdout
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import io
import json
import runpy

ROOT=Path(__file__).resolve().parents[3]
out=ROOT/'research/nima/results/endpoint-composition-gate.json'
out.unlink(missing_ok=True)
with redirect_stdout(io.StringIO()):
    m=runpy.run_path(str(Path(__file__).with_name('check_rung_transport_diagram.py')))
rows=m['source']
r=m['scale'](F(1,2),m['I'])
assert m['mul'](m['physical_reference'].value,r)==m['I']


def ports(records,masses):
    incoming=defaultdict(F); outgoing=defaultdict(F)
    for row,mass in zip(records,masses):
        incoming[row.target]+=mass; outgoing[row.source]+=mass
    return dict(incoming),dict(outgoing)


def matching(records):
    # Chronological left operand followed by right operand.
    return [(j,i) for j,right in enumerate(records) for i,left in enumerate(records)
            if left.target==right.source]


pairs=matching(rows)
assert len(pairs)==916
incoming,outgoing=ports(rows,[F(1)]*137)
assert incoming[('a',0,0)]==9 and outgoing[('a',0,0)]==4
assert incoming!=outgoing
# Every supported pair at v consumes exactly one incoming and one outgoing
# marginal. Unequal vertex totals therefore rule out ANY coupling with the
# original uniform marginals, regardless of how supported pairs are weighted.
imbalances={str(v):str(incoming.get(v,0)-outgoing.get(v,0))
            for v in incoming.keys()|outgoing.keys()
            if incoming.get(v,0)!=outgoing.get(v,0)}
assert imbalances

promoted={}
for policy in ('inherited','common'):
    first=m['incoming_promotion'](rows,1,policy)
    second=m['incoming_promotion'](first,2,policy)
    for stage in (first,second):
        assert not ({x.source for x in stage}&{x.target for x in stage})
        assert matching(stage)==[]
    promoted[policy]={'first_families':len(first),'second_families':len(second),
                      'literal_composable_pairs_at_either_stage':0}

# A declared per-record reference d_i:s_i->t_i and return r_i:t_i->s_i
# instead permits right*r_right*left precisely when their targets agree.
# This is an added typed lift, not an inverse of the actual record map.
def return_pairs(records):
    return [(j,i) for j,b in enumerate(records) for i,a in enumerate(records) if a.target==b.target]

def typed_word(edges):
    assert all(a[1]==b[0] for a,b in zip(edges,edges[1:]))
    return edges[0][0],edges[-1][1]

for j,i in return_pairs(rows):
    a,b=rows[i],rows[j]
    assert typed_word(((a.source,a.target),(b.target,b.source),(b.source,b.target)))==(a.source,a.target)
assert len(return_pairs(rows))==977
# The composite keeps the first operand's source and reference. Both triple
# bracketings flatten to c*r_c*b*r_b*a, with that same retained reference.
for family in m['indexed'](rows,'target').values():
    a,b,c=family[0],family[len(family)//2],family[-1]
    path=((a.source,a.target),(b.target,b.source),(b.source,b.target),
          (c.target,c.source),(c.source,c.target))
    assert typed_word(path)==(a.source,a.target)
    av,bv,cv=a.value,b.value,c.value
    assert m['mul'](m['mul'](cv,r),m['mul'](m['mul'](bv,r),av))==m['mul'](m['mul'](m['mul'](m['mul'](cv,r),bv),r),av)

# Expand the reference-return join at the first promoted stage. Its target
# incidence reproduces the two previously derived final-family leaf laws.
return_profiles={}
for policy in ('inherited','common'):
    first=m['incoming_promotion'](rows,1,policy)
    final=m['incoming_promotion'](first,2,policy)
    target_mass=defaultdict(F)
    for f in first: target_mass[f.target]+=f.mass
    lifted=defaultdict(F)
    for j,i in return_pairs(first):
        a,b=first[i],first[j]
        pair_mass=F(a.mass*b.mass,137*target_mass[a.target])
        for right in m['leaves']((b,)):
            for left in m['leaves']((a,)):
                lifted[right.label,left.label]+=pair_mass*F(right.mass,b.mass)*F(left.mass,a.mass)
    direct={}
    for f in final:
        for right in m['leaves']((f,)):
            for left in m['leaves']((f,)):
                direct[right.label,left.label]=F(right.mass*left.mass,137*f.mass)
    assert dict(lifted)==direct and sum(lifted.values())==1
    return_profiles[policy]={'first_stage_return_pairs':len(return_pairs(first)),
                             'expanded_leaf_pairs':len(lifted)}
assert return_profiles=={'inherited':{'first_stage_return_pairs':32,'expanded_leaf_pairs':977},
                         'common':{'first_stage_return_pairs':1024,'expanded_leaf_pairs':18769}}

# Control1: keeping all directed edges restores balance, but changes the record
# set from137 to160. This is NOT silently substituted for the intended carrier.
Eall=[e for e in product(range(4),repeat=2) if e[0]!=e[1]]
Row=m['Row']; full=[]
for i,e in enumerate(Eall):
    for j,f in enumerate(Eall):
        full.append(Row(('control',i,j),('a',e[0],f[0]),('a',e[1],f[1]),m['I']))
full.extend(row for row in rows if row.source[0]=='s')
assert len(full)==160
assert ports(full,[F(1)]*160)[0]==ports(full,[F(1)]*160)[1]
assert len(matching(full))==1312

# Control2: the existing137 labels admit positive circulation weights. These
# change the observation law. Add one unit along0->2->1 to balance the missing
# edge0->1; take products on arrow-pair slots, unit masses on the state slots.
E=m['E']; edge_mass={e:F(2 if e in ((0,2),(2,1)) else 1) for e in E}
weighted=[edge_mass[e]*edge_mass[f] for e in E for f in E]+[F(1)]*16
assert len(weighted)==137 and sum(weighted)==185
wi,wo=ports(rows,weighted)
assert wi==wo
M=sum(weighted)
pi={(j,i):weighted[j]*weighted[i]/(M*wi[rows[i].target]) for j,i in pairs}
assert sum(pi.values())==1
left=defaultdict(F); right=defaultdict(F)
for (j,i),p in pi.items(): left[i]+=p; right[j]+=p
expected={i:w/M for i,w in enumerate(weighted)}
assert dict(left)==dict(right)==expected
# The balanced join is a Markov context extension. Marginalizing the last port
# of a triple returns the preceding pair; this supplies a finite consistency
# check without claiming that these changed weights are source-selected.
next_ports=defaultdict(list)
for k,j in pairs: next_ports[j].append(k)
for (j,i),p in pi.items():
    assert sum((p*weighted[k]/wo[rows[j].target] for k in next_ports[j]),F(0))==p

result={
 'status':'passed',
 'classification':'literal_endpoint_obstruction_with_conditional_target_fiber_return_lift',
 'obligation':'source port typing before composition/readout transport',
 'stratum':'Actual137-slot endpoint fixture; literal target-to-source matching is a tested candidate, not assumed tower semantics',
 'uniform_leaf_gate':{'supported_pairs':916,'stationary_uniform_coupling':False,
                     'witness_vertex':'a,0,0','incoming_mass':9,'outgoing_mass':4},
 'promoted_gate':promoted,
 'conditional_reference_return_lift':return_profiles,
 'controls':{'restored_edge_records':160,'restored_edge_pairs':1312,
             'reweighted_existing_records':137,'reweighted_total_mass':185,
             'positive_balanced_coupling_verified':True,'triple_marginal_verified':True},
 'unsupported':['selection of literal endpoint composition as tower operation',
                'authority to restore excluded records or change weights',
                'source authority for the per-record reference-return attachment'], 
 'next_constructor':'Select or derive the per-record reference attachments and next-level endpoint policy; the conditional target-fiber return lift now has an explicit typed realization.'
}
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
