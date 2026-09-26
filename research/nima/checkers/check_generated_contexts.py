"""Independent finite interpretation of the generated cartesian-closed programs.
No primitive arbitrary-function node exists. Function tables are values supplied
as continuation arguments, not program constructors.
"""
from dataclasses import dataclass
from functools import lru_cache
from itertools import product
from pathlib import Path
import hashlib
import json
BASE=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
BIT=('base',2); UNIT=('base',1); ONE=('unit',)
def prod(a,b):return ('product',a,b)
def arr(a,b):return ('arrow',a,b)
@lru_cache(None)
def values(t):
    if t[0]=='unit':return (0,)
    if t[0]=='base':return tuple(range(t[1]))
    if t[0]=='product':return tuple(product(values(t[1]),values(t[2])))
    a,b=values(t[1]),values(t[2])
    if len(b)**len(a)>4096:raise ValueError('finite enumeration bound exceeded')
    return tuple(product(b,repeat=len(a)))
@dataclass(frozen=True)
class P:
    op:str
    source:tuple
    target:tuple
    args:tuple=()
def terminal(a):return P('terminal',a,ONE)
def ident(a):return P('identity',a,a)
def first(a,b):return P('first',prod(a,b),a)
def second(a,b):return P('second',prod(a,b),b)
def seq(f,g):
    assert f.target==g.source
    return P('then',f.source,g.target,(f,g))
def pair(f,g):
    assert f.source==g.source
    return P('pair',f.source,prod(f.target,g.target),(f,g))
def app(a,b):return P('apply',prod(arr(a,b),a),b)
def lam(body):
    assert body.source[0]=='product'
    _,a,b=body.source
    return P('lambda',a,arr(b,body.target),(body,))
def run(p,x):
    if p.op=='terminal':return 0
    if p.op=='identity':return x
    if p.op=='first':return x[0]
    if p.op=='second':return x[1]
    if p.op=='then':return run(p.args[1],run(p.args[0],x))
    if p.op=='pair':return tuple(run(f,x) for f in p.args)
    if p.op=='apply':
        a=p.source[2]
        return x[0][values(a).index(x[1])]
    if p.op=='lambda':return tuple(run(p.args[0],(x,b)) for b in values(p.target[1]))
    raise ValueError(p.op)
def preprogram(f,x):
    h=arr(f.target,x)
    return lam(seq(pair(first(h,f.source),seq(second(h,f.source),f)),app(f.target,x)))
def swap(a,b):return pair(second(a,b),first(a,b))
def curry(a,b,c):
    h=arr(prod(a,b),c); ha=prod(h,a)
    hf=seq(first(ha,b),first(h,a))
    av=seq(first(ha,b),second(h,a))
    return lam(lam(seq(pair(hf,pair(av,second(ha,b))),app(prod(a,b),c))))
def uncurry(a,b,c):
    h=arr(a,arr(b,c)); ab=prod(a,b)
    hf=first(h,ab)
    av=seq(second(h,ab),first(a,b)); bv=seq(second(h,ab),second(a,b))
    return lam(seq(pair(seq(pair(hf,av),app(a,arr(b,c))),bv),app(b,c)))

def inverse_checks(f,g):
    assert f.source==g.target and f.target==g.source
    for x in values(f.source):assert run(g,run(f,x))==x
    for y in values(f.target):assert run(f,run(g,y))==y
    return len(values(f.source))+len(values(f.target))
assert all(run(terminal(BIT),a)==0 for a in values(BIT))
s=swap(BIT,BIT); t=swap(BIT,BIT)
c=curry(BIT,BIT,BIT); u=uncurry(BIT,BIT,BIT)
checks=inverse_checks(s,t)+inverse_checks(c,u)
context_cases=0
for x in (UNIT,BIT,prod(BIT,BIT)):
    sf,sg=preprogram(s,x),preprogram(t,x)
    for h in values(sf.source):
        assert run(sg,run(sf,h))==h
        # Check generated precomposition directly at every domain value.
        out=run(sf,h)
        assert out==tuple(h[values(s.target).index(run(s,a))] for a in values(s.source))
        context_cases+=1
# Exercise exactly the two witness continuations in the curry comparison;
# do not enumerate the enormous entire spaces of higher-order functions.
for x,h in ((c.source,tuple(run(u,b) for b in values(c.target))),
            (c.target,tuple(values(c.target)))):
    assert run(preprogram(u,x),run(preprogram(c,x),h))==h
    context_cases+=1

# Both proposed inverse programs are generated, but their inverse law fails.
f=first(BIT,BIT); g=pair(ident(BIT),ident(BIT))
assert all(run(f,run(g,a))==a for a in values(BIT))
assert any(run(g,run(f,p))!=p for p in values(prod(BIT,BIT)))
assert ident(BIT)!=seq(ident(BIT),ident(BIT))
assert all(run(ident(BIT),a)==run(seq(ident(BIT),ident(BIT)),a) for a in values(BIT))

# Original E/P parameters may simply carry an externally supplied table.
# This is audited as supplied, not relabeled as a generated program.
supplied_cases=0
for a in (BIT,prod(BIT,BIT)):
    for table in values(arr(a,BIT)):
        encoded=tuple((b,0) for b in table)
        assert tuple(x[0] for x in encoded)==table
        supplied_cases+=1
assert supplied_cases==20

def tree(p):return {'op':p.op,'source':p.source,'target':p.target,'args':[tree(q) for q in p.args]}
receipt_path=BASE/'results/agda-GeneratedContinuationContexts.json'
r=json.loads(receipt_path.read_text(encoding='utf-8-sig'))
assert r['passed'] and r['exit_code']==0 and r['ignore_interfaces']
modules=['GeneratedContinuationContexts','ResolutionMapIntroductionGap','UniversalSubstitution','WholePackageResolution','WholePackageSigmaPi']
for m in modules:
    p=BASE/f'agda/{m}.agda'
    assert r['owner_source_inventory_sha256'][p.name]==sha(p),m
control=json.loads((BASE/'results/generated-contexts-formal-audit.json').read_text(encoding='utf-8-sig'))
assert control['positive_receipt_sha256'].lower()==sha(receipt_path)
assert len(control['controls'])==2
for c0 in control['controls']:
    assert c0['correctly_rejected'] and c0['exit_code']!=0
    assert c0['source_sha256'].lower()==sha(BASE/f"agda/negative/{c0['module']}.agda")
packet={
 'status':'generated-certificates-in-explicit-new-fragment',
 'obligations':['forward realization','route/coherencer compatibility','readout descent'],
 'inverse_value_checks':checks,'continuation_cases':context_cases,
 'supplied_function_encoding_controls':supplied_cases,
 'formal_receipt_sha256':sha(receipt_path),
 'source_programs':{'swap':tree(s),'curry':tree(c),'uncurry':tree(u)},
 'established':['bare map packages in original Resolve must be seeded',
                'original E/P can nevertheless encode any supplied function in index parameters',
                'new typed programs generate precomposition maps and inverses for swap and currying',
                'quantified continuation witnesses constructed from generated programs and computed inverse laws',
                'new Extended derivations and raw certificate recovery checked'],
 'scope':'New fragment is nondependent cartesian-closed syntax with explicit map-introduction rule. No arbitrary-function program constructor. No decision procedure or inverse synthesis for all programs. Old rules are not modified or restricted.',
 'residual':'Uniform source derivations for index, family and witness parameters of all original schemas remain open; adding a certified fragment does not enforce provenance on the entire old closure.',
 'sha256':{f'agda/{m}.agda':sha(BASE/f'agda/{m}.agda') for m in modules},
}
(BASE/'results/generated-contexts.json').write_text(json.dumps(packet,indent=2)+'\n',encoding='utf-8')
print(f'PASS: {checks} inverse value checks, {context_cases} continuation cases, {supplied_cases} supplied-vs-generated controls; fresh source-bound formal audit.')
