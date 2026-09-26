"""Retained pointed finite constructions, actual filler enumeration, and signature hostile."""
from itertools import product, permutations
from pathlib import Path
import hashlib
import json
BASE=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
unit=('unit',)
objects={'unit':unit,'square':tuple(product(unit,unit)),
         'choice':tuple(product((0,1),unit)),'four':tuple(product((0,1),repeat=2))}
# Each complete object retains its name, full value family, and chosen first value.
objects={name:{'values':values,'point':values[0]} for name,values in objects.items()}
def fillers(a,b,policy):
    A,B=objects[a]['values'],objects[b]['values']
    if policy=='identities':
        return [tuple(range(len(A)))] if a==b else []
    if len(A)!=len(B):return []
    return [p for p in permutations(range(len(B))) if B[p[0]]==objects[b]['point']]
def compose(f,g):return tuple(g[i] for i in f)
def inverse(f):return tuple(f.index(i) for i in range(len(f)))
reports={}
for policy in ('pointed-bijections','identities'):
    hom={(a,b):fillers(a,b,policy) for a,b in product(objects,repeat=2)}
    for a in objects:
        identity=tuple(range(len(objects[a]['values'])))
        assert identity in hom[a,a]
    for (a,b),fs in hom.items():
        for f in fs:
            assert inverse(f) in hom[b,a]
            assert compose(f,inverse(f))==tuple(range(len(f)))
            assert compose(tuple(range(len(f))),f)==f
            assert compose(f,tuple(range(len(f))))==f
    for a,b,c in product(objects,repeat=3):
        for f,g in product(hom[a,b],hom[b,c]):assert compose(f,g) in hom[a,c]
    for a,b,c,d in product(objects,repeat=4):
        for f,g,h in product(hom[a,b],hom[b,c],hom[c,d]):
            assert compose(compose(f,g),h)==compose(f,compose(g,h))
    reports[policy]={'filler_counts':{f'{a}->{b}':len(fs) for (a,b),fs in hom.items()}}
rich=reports['pointed-bijections']['filler_counts']
strict=reports['identities']['filler_counts']
assert rich['unit->square']==1 and rich['unit->choice']==0
assert rich['four->four']==6 and strict['four->four']==1
assert strict['unit->square']==0
assert (0,1,2,3)!=(0,2,1,3)
assert (0,2,1,3) in fillers('four','four','pointed-bijections')
receipt_path=BASE/'results/agda-BoundaryGeneratedQuestions.json'
r=json.loads(receipt_path.read_text(encoding='utf-8-sig'))
assert r['passed'] and r['exit_code']==0 and r['ignore_interfaces']
modules=['BoundaryGeneratedQuestions','QBooleanity','WholePackageResolution','WholePackageSigmaPi']
for m in modules:
    p=BASE/f'agda/{m}.agda'
    assert r['owner_source_inventory_sha256'][p.name]==sha(p),m
control=json.loads((BASE/'results/boundary-questions-formal-audit.json').read_text(encoding='utf-8-sig'))
assert control['positive_receipt_sha256'].lower()==sha(receipt_path)
assert control['correctly_rejected'] and control['negative_exit_code']!=0
assert control['negative_source_sha256'].lower()==sha(BASE/'agda/negative/BoundaryBadWitnessCollapse.agda')
packet={
 'status':'operation-and-question-share-a-rule-relative-boundary',
 'obligations':['forward realization','route/coherencer compatibility','readout descent'],
 'policies':reports,
 'formal_receipt_sha256':sha(receipt_path),
 'results':['actual comparison-rule application consumes a filler and premise derivations',
            'complete Q pairs give both inhabited and empty generated comparison questions',
            'two retained four-point fillers are distinct while their Boolean reflections agree',
            'supplied endpoint comparisons transport the question and give equivalent truth types'],
 'signature_hostile':'Same retained finite objects admit both coherent policies, with different unit->square truth. The identities-only policy is an alternative signature, not the existing compare-rule.',
 'residual':'A common boundary-filling interface does not select the admitted rule schemas or generate every higher filler.',
 'sha256':{f'agda/{m}.agda':sha(BASE/f'agda/{m}.agda') for m in modules},
}
(BASE/'results/boundary-questions.json').write_text(json.dumps(packet,indent=2)+'\n',encoding='utf-8')
print('PASS: boundary-derived questions, source-bound formal closure, retained-filler distinction, and alternative-signature hostile.')
