"""Bounded semantic hostiles and source-bound formal receipt audit.
The infinite-carrier result is proved by Agda, not by this enumeration.
"""
from itertools import product, permutations
from pathlib import Path
import hashlib
import json
from build_wolfram_converse import load, replay

BASE=Path(__file__).resolve().parents[1]
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def holds(n,t):
    op=lambda x,y:t[n*x+y]
    return all(op(op(op(a,b),c),op(a,op(op(a,c),a)))==c
               for a,b,c in product(range(n),repeat=3))
models={}
for n in range(4):
    found=[t for t in product(range(n),repeat=n*n) if holds(n,t)]
    models[n]=found
assert [len(models[n]) for n in range(4)]==[1,1,2,0]
assert set(models[2])=={(1,1,1,0),(1,0,0,0)}
# An actual four-element Boolean model, all labelings, not a size-four census.
four=set()
for perm in permutations(range(4)):
    inv={perm[i]:i for i in range(4)}
    table=tuple(perm[3 ^ (inv[a]&inv[b])] for a,b in product(range(4),repeat=2))
    assert holds(4,table)
    four.add(table)
assert len(four)==12
counts=[]
for source,label,axiom in [('Sh-2.proof','s','sh2'),('Sh-1.proof','t','sh1')]:
    db,output=replay(load(BASE/'results'/source),label,axiom)
    counts.append(len(output)//3)
assert counts==[92,67]
receipt_path=BASE/'results/agda-QBooleanNandBridge.json'
receipt=json.loads(receipt_path.read_text(encoding='utf-8-sig'))
assert receipt['passed'] and receipt['exit_code']==0 and receipt['ignore_interfaces']
assert '--ignore-interfaces' in receipt['args']
assert receipt['source_sha256']==sha(BASE/'agda/QBooleanNandBridge.agda')
modules=['QBooleanNandBridge','BooleanNandEquivalence','WolframBooleanAlgebra','WolframConverse','NandConstructions']
for module in modules:
    path=BASE/f'agda/{module}.agda'
    assert receipt['owner_source_inventory_sha256'][path.name]==sha(path), module
formal_path=BASE/'results/wolfram-converse-formal-audit.json'
formal=json.loads(formal_path.read_text(encoding='utf-8-sig'))
assert formal['positive_receipt_sha256'].lower()==sha(receipt_path)
assert len(formal['controls'])==2
for control in formal['controls']:
    assert control['correctly_rejected'] and control['exit_code']!=0
    assert control['source_sha256'].lower()==sha(BASE/f"agda/negative/{control['module']}.agda")
files=[BASE/f'agda/{m}.agda' for m in modules]+[BASE/'results/Sh-1.proof',BASE/'results/Sh-2.proof',Path(__file__),BASE/'checkers/build_wolfram_converse.py']
packet={
 'status':'general-equational-equivalence-formally-checked',
 'obligation':'forward realization in both directions; operation roundtrip compatibility',
 'domain':'nonempty sets; trivial Boolean algebra included; no finiteness assumption in Agda',
 'replayed_equations_including_starting_equations':counts,
 'finite_model_counts':{str(n):len(ts) for n,ts in models.items()},
 'two_element_tables':[list(t) for t in models[2]],
 'four_element_relabelled_boolean_models':len(four),
 'finite_scope':'exhaustive operation tables for cardinalities 0..3; only Boolean relabelings for size 4',
 'formal_root':'agda/QBooleanNandBridge.agda',
 'formal_receipt_sha256':sha(receipt_path),
 'compiler_rejection_controls':2,
 'residual':'Selecting Boolean domain and empty indexing from unrestricted Q is not proved.',
 'sha256':{p.relative_to(BASE).as_posix():sha(p) for p in files},
}
(BASE/'results/wolfram-converse.json').write_text(json.dumps(packet,indent=2)+'\n',encoding='utf-8')
print('PASS: general Boolean/NAND equivalence and Q bridge have fresh source-bound formal receipts; replay 92+67 equations; finite controls 0..3 plus 12 four-element models.')
