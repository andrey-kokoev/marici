"""Exact finite Heyting controls plus source-bound Agda receipt validation."""
from pathlib import Path
from itertools import product
import hashlib
import json
BASE=Path(__file__).resolve().parents[1]
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
frames={
 'chain':({0,1},lambda x,y:x<=y),
 'fork':({0,1,2},lambda x,y:x==y or x==0),
 'diamond':({0,1,2,3},lambda x,y:x==y or x==0 or y==3),
}
reports={}
for name,(points,le) in frames.items():
    U=frozenset(points)
    opens=[frozenset(i for i in U if mask & (1<<i)) for mask in range(1<<len(U))]
    opens=[a for a in opens if all(not(x in a and le(x,y)) or y in a for x,y in product(U,repeat=2))]
    neg=lambda a:frozenset(x for x in U if not any(le(x,y) and y in a for y in U))
    d=lambda a:neg(neg(a))
    n=lambda a,b:neg(a&b)
    w=lambda a,b,c:n(n(n(a,b),c),n(a,n(n(a,c),a)))
    regular=[a for a in opens if d(a)==a]
    assert all(w(a,b,c)==d(c) for a,b,c in product(opens,repeat=3))
    assert all(d(d(a))==d(a) and a<=d(a) for a in opens)
    assert all(n(a,b) in regular for a,b in product(opens,repeat=2))
    assert all(w(a,b,c)==c for a,b,c in product(regular,repeat=3))
    assert all(n(n(a,a),n(b,b))==d(a|b) for a,b in product(opens,repeat=2))
    reports[name]={'opens':len(opens),'regular':len(regular),'wolfram_double_cases':len(opens)**3}
    if name=='chain':
        c=frozenset({1})
        assert w(frozenset(),frozenset(),c)==U and c!=U
        reports[name]['raw_wolfram_counterexample']={'a':[],'b':[],'c':[1],'actual':[0,1]}
    if name=='fork':
        a,b=frozenset({1}),frozenset({2})
        assert a in regular and b in regular and a|b not in regular
        assert n(n(a,a),n(b,b))==U
        assert a|neg(a)!=U  # Stable does not imply decidable in the raw logic.
        reports[name]['join_changes']={'raw_union':[1,2],'boolean_join':[0,1,2]}

receipt_path=BASE/'results/agda-QBooleanity.json'
r=json.loads(receipt_path.read_text(encoding='utf-8-sig'))
assert r['passed'] and r['exit_code']==0 and r['ignore_interfaces']
modules=['QBooleanity','BooleanNandEquivalence','WolframBooleanAlgebra','WolframConverse','WholePackageSigmaPi']
for m in modules:
    p=BASE/f'agda/{m}.agda'
    assert r['owner_source_inventory_sha256'][p.name]==sha(p),m
control_path=BASE/'results/q-booleanity-formal-audit.json'
control=json.loads(control_path.read_text(encoding='utf-8-sig'))
assert control['positive_receipt_sha256'].lower()==sha(receipt_path)
assert control['correctly_rejected'] and control['negative_exit_code']!=0
assert control['negative_source_sha256'].lower()==sha(BASE/'agda/negative/QBooleanityBadInverse.agda')
packet={
 'status':'boolean-reflection-derived-not-unrestricted-Q-booleanity',
 'obligations':['forward realization','readout descent'],
 'formal_root':'agda/QBooleanity.agda',
 'formal_receipt_sha256':sha(receipt_path),
 'frames':reports,
 'theorems':['W(A,B,C) equivalent to double negation C',
             'W equivalent to C precisely when C is a stable proposition',
             'double negation is an idempotent reflection into stable propositions',
             'stable propositions form a Boolean algebra under constructed NAND',
             'Boolean join is double negation of the tagged sum',
             'Bool is not equivalent to its double negation',
             'inhabitation reflection of every complete Q is contractible'],
 'residual':'Retained Q is not preserved by truth reflection; nontrivial truth of a complete Q needs a specified predicate or compatibility fibre. Empty target remains required.',
 'sha256':{f'agda/{m}.agda':sha(BASE/f'agda/{m}.agda') for m in modules},
}
(BASE/'results/q-booleanity.json').write_text(json.dumps(packet,indent=2)+'\n',encoding='utf-8')
print('PASS: stable-truth Boolean algebra, exact Wolfram/double-negation comparison, reflection and loss proofs; finite Heyting hostiles retained.')
