#!/usr/bin/env python3
"""Source-oriented 2-round incidence closure and its conditional comparison homology."""
import json
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

V='ABCD'
N=['AB','BC','CA','AD','DB','BA']
short={'AC':('AB','BC'), 'BD':('BA','AD'), 'CB':('CA','AB'), 'DA':('DB','BA')}
# The two missing opposite-support arcs appear only on the second round
# of same-chirality composition.
short['CD']=('CB','BD')
short['DC']=('DA','AC')
words={u:(u,) for u in N}
for u in ('AC','BD','CB','DA','CD','DC'):
    a,b=short[u]
    assert a in words and b in words
    words[u]=words[a]+words[b]
assert words['CD']==('CA','AB','BA','AD')
assert words['DC']==('DB','BA','AB','BC')
assert words['CD'][0]=='CA' and words['DC'][0]=='DB'

def chain(path):
    return sp.Matrix([path.count(e) for e in N])
T1=chain(('AB','BC','CA'))
T2=chain(('AD','DB','BA'))
H=chain(('AB','BA'))
# Chiral routes differ from the original 2-step routes by the seam chain.
assert chain(words['CD'])-chain(('CA','AD')) == H
assert chain(words['DC'])-chain(('DB','BC')) == H

old_relations={}
for tri in ('ADB','BCA','ACD','BDC','CDA','DCB'):
    u,v,w=tri
    relation=chain(words[u+v])+chain(words[v+w])-chain(words[u+w])
    old_relations[tri]=relation
expected={'ADB':T2-H, 'BCA':T1-H, 'ACD':T1+H,
          'BDC':T2+H,'CDA':T2+H,'DCB':T1+H}
assert all(old_relations[t]==v for t,v in expected.items())

stages=[
  ('S0_original_six_occurrences',N,()),
  ('S1_compare_two_existing_parallel_paths',N,('ADB','BCA')),
  ('S2_promote_four_reverse_support_arcs',N+['AC','BD','CB','DA'],('ADB','BCA','ABC','BAD','CAB','DBA')),
  ('S3_promote_CD_DC_through_the_reverses',N+list(short),('ADB','BCA','ABC','BAD','CAB','DBA','CBD','DAC')),
  ('S4_close_all_seed_chiral_comparisons',N+list(short),('ADB','BCA','ABC','BAD','CAB','DBA','CBD','DAC','ACD','BDC','CDA','DCB')),
  ('S5_compare_CD_to_its_original_shortcut',N+list(short),('ADB','BCA','ABC','BAD','CAB','DBA','CBD','DAC','ACD','BDC','CDA','DCB','CAD')),
]

def compute(name,edges,faces):
    d1=sp.zeros(4,len(edges))
    for j,e in enumerate(edges):
        d1[V.index(e[0]),j]=-1
        d1[V.index(e[1]),j]=1
    d2=sp.zeros(len(edges),len(faces))
    for j,(u,v,w) in enumerate(faces):
        for e,val in (((u,v),1),((v,w),1),((u,w),-1)):
            eid=''.join(e)
            assert eid in edges, (name,faces[j],eid)
            d2[edges.index(eid),j]+=val
    assert d1*d2==sp.zeros(4,len(faces))
    snf=smith_normal_form(d2,domain=ZZ)
    invariant=[abs(int(snf[i,i])) for i in range(min(snf.shape)) if snf[i,i]]
    r2=len(invariant)
    return {'edges':len(edges),'faces':len(faces),'rank_d1':3,'rank_d2':r2,
      'H1_free_rank':len(edges)-3-r2,'H1_torsion':[x for x in invariant if x>1],
      'H2_free_rank':len(faces)-r2,'SNF_d2':invariant}

result={'status':'passed','scope':'Conditional 2-comparison admission, not a proof of native generation',
  'induced_words':{k:list(v) for k,v in words.items() if k not in N},
  'composite_CD_minus_native_CD_equals_seam':True,
  'composite_DC_minus_native_DC_equals_seam':True,
  'existing_target_relation_in_H1_basis':{
      'ADB':'t2-h','BCA':'t1-h','ACD':'t1+h',
      'BDC':'t2+h','CDA':'t2+h','DCB':'t1+h'},
  'stages':{name:compute(name,edges,faces) for name,edges,faces in stages}}
assert [(q['H1_free_rank'],q['H1_torsion']) for q in result['stages'].values()]==[(3,[]),(1,[]),(1,[]),(1,[]),(0,[2]),(0,[])]
with open('/mnt/data/marici_chiral_growth_stages_results.json','w') as f:
    json.dump(result,f,indent=2);f.write('\n')
print(json.dumps(result,indent=2))
