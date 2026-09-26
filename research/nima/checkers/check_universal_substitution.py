"""Finite universal-property hostiles, independently source-bound to Agda proof."""
from itertools import product
from pathlib import Path
import hashlib
import json
BASE=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def functions(a,b):return list(product(range(b),repeat=a))
def pre(a,b,f,x):
    domain=functions(b,x); codomain=functions(a,x)
    images=[tuple(h[f[i]] for i in range(a)) for h in domain]
    return {'domain':len(domain),'codomain':len(codomain),
            'surjective':set(images)==set(codomain),
            'injective':len(set(images))==len(images)}
def equiv(t):return t['surjective'] and t['injective']
count=0
for a,b in product(range(4),repeat=2):
    for f in functions(a,b):
        actual=len(set(f))==a and set(f)==set(range(b))
        all_targets=all(equiv(pre(a,b,f,x)) for x in range(4))
        two=equiv(pre(a,b,f,a)) and equiv(pre(a,b,f,b))
        assert all_targets==two==actual
        graph=tuple((i,f[i]) for i in range(a))
        assert len(set(graph))==a and tuple(v[0] for v in graph)==tuple(range(a))
        count+=1
assert count==60
# Endpoint inhabitation and all proposition-valued continuations miss collapse.
collapse_prop=[pre(2,1,(0,0),x) for x in (0,1)]
assert all(equiv(t) for t in collapse_prop)
collapse_bool=pre(2,1,(0,0),2)
assert not collapse_bool['surjective'] and collapse_bool['injective']
# Canonical sum of two unit branches, a collapsed candidate, and an extra point.
sums={'canonical':pre(2,2,(0,1),2),'collapse':pre(2,1,(0,0),2),'extra_point':pre(2,3,(0,1),2)}
assert equiv(sums['canonical'])
assert not sums['collapse']['surjective']
assert sums['extra_point']['surjective'] and not sums['extra_point']['injective']
# Product universality at Unit already detects lost or surplus tuple data.
def product_unit_test(bundle):
    return {'domain':len(bundle),'codomain':4,
            'surjective':set(bundle)==set(range(4)),
            'injective':len(set(bundle))==len(bundle)}
products={'canonical':product_unit_test((0,1,2,3)),
          'missing_tuples':product_unit_test((0,)),
          'extra_bit':product_unit_test((0,0,1,1,2,2,3,3))}
assert equiv(products['canonical'])
assert not products['missing_tuples']['surjective']
assert products['extra_bit']['surjective'] and not products['extra_bit']['injective']
# Distinct retained labels, identical singleton value types.
assert all(equiv(pre(1,1,(0,),x)) for x in range(4))
retained_tags={'unit':'atom','square':'E'}
assert retained_tags['unit']!=retained_tags['square']
receipt_path=BASE/'results/agda-UniversalSubstitution.json'
r=json.loads(receipt_path.read_text(encoding='utf-8-sig'))
assert r['passed'] and r['exit_code']==0 and r['ignore_interfaces']
modules=['UniversalSubstitution','BoundaryGeneratedQuestions','WholePackageSigmaPi']
for m in modules:
    p=BASE/f'agda/{m}.agda'
    assert r['owner_source_inventory_sha256'][p.name]==sha(p),m
control=json.loads((BASE/'results/universal-substitution-formal-audit.json').read_text(encoding='utf-8-sig'))
assert control['positive_receipt_sha256'].lower()==sha(receipt_path)
assert control['correctly_rejected'] and control['negative_exit_code']!=0
assert control['negative_source_sha256'].lower()==sha(BASE/'agda/negative/SubstitutionBadTruthTest.agda')
packet={
 'status':'relative-universal-selection-not-context-free-rule-origin',
 'obligations':['forward realization','route/coherencer compatibility','readout descent'],
 'all_map_cases_cardinalities_0_through_3':count,
 'collapse_proposition_tests':collapse_prop,'collapse_bool_test':collapse_bool,
 'sum_candidates':sums,'product_candidates':products,
 'unit_square':{'all_value_tests_pass':True,'retained_constructor_tags':retained_tags},
 'collapse_graph':{'input_size':2,'output_size':1,'retained_graph_size':2,'source_recovered':True},
 'formal_receipt_sha256':sha(receipt_path),
 'scope':'Agda proves quantified equivalence and universal characterizations; enumeration is a finite hostile suite, not the general proof.',
 'residual':'The context language and completeness-of-admission requirement are specified. A rule rejecting some reversible maps is excluded only if admission must include every universally reversible map. No complete synthesis of the original twelve schemas is proved.',
 'sha256':{f'agda/{m}.agda':sha(BASE/f'agda/{m}.agda') for m in modules},
}
(BASE/'results/universal-substitution.json').write_text(json.dumps(packet,indent=2)+'\n',encoding='utf-8')
print('PASS: universal substitution characterizations, 60 finite maps, sum/product universality hostiles, and value-versus-retained context separation.')
