"""Bounded independent controls for inductive-tree and scoped-template proofs."""
from pathlib import Path
from itertools import product
import hashlib,json
BASE=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def leaf(a):return ('leaf',a)
def node(l,r):return ('node',l,r)
def fold(t,atoms,branch):
    if t[0]=='leaf':return atoms(t[1])
    return branch(fold(t[1],atoms,branch),fold(t[2],atoms,branch))
def plug(t,env):return fold(t,env,node)
def trees(labels,depth):
    leaves=tuple(leaf(a) for a in labels)
    if depth==0:return leaves
    smaller=trees(labels,depth-1)
    return leaves+tuple(node(l,r) for l in smaller for r in smaller)
small=trees((0,1),1)
for t in trees((0,1),2):assert plug(t,leaf)==t
assoc=0
for t,sigma,tau in product(small,product(small,repeat=2),product(small,repeat=2)):
    assert plug(plug(t,sigma.__getitem__),tau.__getitem__)==plug(t,lambda a:plug(sigma[a],tau.__getitem__))
    assoc+=1

def free(a):return ('free',a)
def slot(i):return ('slot',i)
def embed(t):return plug(t,lambda a:leaf(free(a)))
def instantiate(t,args):
    return plug(t,lambda v:leaf(v[1]) if v[0]=='free' else args[v[1]])
def partial(t,arg):
    def at(v):
        if v[0]=='free':return leaf(v)
        if v[1]==0:return embed(arg)
        return leaf(slot(v[1]-1))
    return plug(t,at)
def run(t,args):
    for a in args:t=partial(t,a)
    return instantiate(t,())
scoped=0
for n in (1,2,3):
    labels=(free(0),free(1))+tuple(slot(i) for i in range(n))
    for body,args in product(trees(labels,1),product(small,repeat=n)):
        assert instantiate(partial(body,args[0]),args[1:])==instantiate(body,args)
        assert run(body,args)==instantiate(body,args)
        scoped+=1
K=leaf(slot(0))
S=node(node(leaf(slot(0)),leaf(slot(2))),node(leaf(slot(1)),leaf(slot(2))))
for x,y in product(small,repeat=2):assert run(K,(x,y))==x
for f,g,x in product(small,repeat=3):assert run(S,(f,g,x))==node(node(f,x),node(g,x))
# Scope hostile: the second slot survives the first application.
assert partial(leaf(slot(1)),leaf(0))==leaf(slot(0))
assert partial(leaf(slot(1)),leaf(0))!=embed(leaf(0))
# Duplication hostile: omitting the second use of x changes the result.
badS=node(node(leaf(slot(0)),leaf(slot(2))),leaf(slot(1)))
assert run(badS,(leaf(0),leaf(1),leaf(0)))!=run(S,(leaf(0),leaf(1),leaf(0)))
# One-hole contexts cannot flip leaf labels. Formal proof is unbounded.
nonfull=0
for t in trees((free(0),free(1),slot(0)),2):
    assert any(instantiate(t,(leaf(b),))!=leaf(1-b) for b in (0,1))
    nonfull+=1
nested=trees(small,1)
images={plug(t,lambda x:x) for t in nested}
assert len(nested)==42 and len(images)==38
example=node(leaf(0),leaf(1))
assert fold(example,lambda x:x,lambda l,r:l)!=fold(example,lambda x:x,lambda l,r:r)
# Retaining a complete application does not discard unused arguments.
x,y=small[0],small[-1]
frame={'source':partial(K,x),'argument':y,'residual':partial(partial(K,x),y)}
assert frame['argument']==y and instantiate(frame['residual'],())==x

rp=BASE/'results/agda-ECurriedTemplates.json'
r=json.loads(rp.read_text(encoding='utf-8-sig'))
assert r['passed'] and r['exit_code']==0 and r['ignore_interfaces']
modules=('ETreeSubstitution','ECurriedTemplates','WholePackageSigmaPi')
for m in modules:
    assert r['owner_source_inventory_sha256'][m+'.agda']==sha(BASE/f'agda/{m}.agda')
c=json.loads((BASE/'results/e-tree-templates-formal-audit.json').read_text(encoding='utf-8-sig'))
assert c['positive_receipt_sha256'].lower()==sha(rp)
assert len(c['controls'])==2
for control in c['controls']:
    assert control['correctly_rejected'] and control['exit_code']!=0
    assert control['source_sha256'].lower()==sha(BASE/f"agda/negative/{control['module']}.agda")
packet={
 'status':'inductive-template-substitution-checked',
 'obligations':['forward realization','route/coherencer compatibility','readout descent'],
 'associativity_controls':assoc,'scoped_application_controls':scoped,
 'K_controls':36,'S_controls':216,'nonfull_function_space_controls':nonfull,
 'flattening':{'inputs':len(nested),'distinct_outputs':len(images)},
 'formal_receipt_sha256':sha(rp),
 'scope':'Finite inductive E-trees with declared leaf/node labels, arities and recursion. Template instantiation and residualization, not execution of arbitrary function-valued inputs or a full dependent P.',
 'residuals':['source derivation of the inductive eliminator',
              'internal typed execution semantics for application nodes',
              'full dependent abstraction and any function-space completeness theorem'],
 'source_sha256':{m:sha(BASE/f'agda/{m}.agda') for m in modules},
 'checker_sha256':sha(Path(__file__).resolve()),
}
(BASE/'results/e-tree-templates.json').write_text(json.dumps(packet,indent=2)+'\n',encoding='utf-8')
print(f'PASS: {assoc} substitution associativity, {scoped} scoped application, 252 K/S and {nonfull} function-space controls; fresh formal closure.')
