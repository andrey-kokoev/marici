"""Bounded regressions for reference syntax; no general theorem claimed."""
from pathlib import Path
import hashlib,json
from reference import Package, Admission, Rule, Seed, Step, unit, map_seeds, flatten
p=Package('P',('retained payload',));q=Package('Q')
u=Rule('u',(p,),p,'u-witness-1');u2=Rule('u',(p,),p,'u-witness-2');v=Rule('v',(p,p),p,'v-witness')
s=unit(Admission(p,'seed-proof'))
def grow(seeds):
 return seeds+[Step(r,(x,)) for r in (u,u2) for x in seeds]+[Step(v,(x,y)) for x in seeds for y in seeds]
base=grow(grow([s]));nested=grow([unit(x) for x in base[:4]]);triple=grow([unit(x) for x in nested[:4]])
for d in base:
 assert flatten(unit(d))==d
 assert flatten(map_seeds(unit,d))==d
 assert map_seeds(lambda x:x,d)==d
 f=lambda x:Admission(x.package,x.witness+'f')
 g=lambda x:Admission(x.package,x.witness+'g')
 assert map_seeds(g,map_seeds(f,d))==map_seeds(lambda x:g(f(x)),d)
for d in nested:assert flatten(d).level==0 and flatten(d).package==d.package
for d in triple:assert flatten(flatten(d))==flatten(map_seeds(flatten,d))
inside=unit(Step(u,(s,)));outside=Step(u,(unit(s),))
assert inside!=outside and flatten(inside)==flatten(outside)
assert Step(u,(s,))!=Step(u2,(s,))
a=Step(u,(s,));b=Step(u2,(s,));assert Step(v,(a,b))!=Step(v,(b,a))
rejections=0
for action in (lambda:flatten(s),lambda:Seed(q,s),lambda:Step(u,()),lambda:Step(v,(s,unit(s))),lambda:Step(u,(unit(Admission(q,'q')),)),lambda:Rule('bad',(),p,'no-nullary-rules')):
 try:action()
 except (ValueError,TypeError):rejections+=1
 else:raise AssertionError('invalid syntax accepted')
root=Path(__file__).parent
report={'passed':True,'base_histories':len(base),'nested_histories':len(nested),'triple_histories':len(triple),'negative_tests':rejections,'unit_and_map_laws':True,'associativity_cases':len(triple),'distinct_layerings_same_flattening':True,'witness_and_premise_order_retained':True,'source_sha256':{name:hashlib.sha256((root/name).read_bytes()).hexdigest() for name in ('reference.py','check_reference.py')},'scope':'Finite immutable Python reference syntax and bounded executable regressions. Not arbitrary dependent types, a local interaction net, or new Agda certification.'}
(root/'results').mkdir(exist_ok=True);(root/'results/reference.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
