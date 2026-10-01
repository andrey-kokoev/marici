"""Finite realization of the supplied pointed comparison constructor.

Keep the actual permutation, not a flat section of the endpoint relation.
Composition payloads form an action groupoid; parent histories remain retained.
"""
from dataclasses import dataclass
from itertools import permutations, combinations
from pathlib import Path
import hashlib
import json

ROOT=Path(__file__).resolve().parents[3]
out=ROOT/'research/nima/results/retained-pointed-comparison-groupoid.json'
out.unlink(missing_ok=True)
paths=[ROOT/'research/nima/agda'/name for name in
       ('WholePackageSigmaPi.agda','WholePackageResolution.agda','BoundaryGeneratedQuestions.agda')]
texts=[p.read_text(encoding='utf-8') for p in paths]
assert 'pack (comparison (retained a) (retained b) e) (value a , value b , p)' in texts[0]
assert 'remember (comparison-package a b e p)' in texts[0]
assert '(comparison-package a c (compEquiv e f)' in texts[0]
assert 'output (compare-rule a b e p) = comparison-package a b e p' in texts[1]
assert '(λ e → equivFun e (value a) ≡ value b)' in texts[2]
V=tuple(range(4)); G=tuple(permutations(V)); unit=V

def mul(b,a): return tuple(b[a[i]] for i in V)
def inv(a): return tuple(a.index(i) for i in V)
def swap(i,j): return tuple(j if k==i else i if k==j else k for k in V)

@dataclass(frozen=True)
class Arrow:
    source: int
    target: int
    witness: tuple
    parents: tuple=()
    def __post_init__(self):
        assert self.witness in G and self.witness[self.source]==self.target
    def payload(self): return self.source,self.target,self.witness

def compose(b,a):
    assert a.target==b.source
    return Arrow(a.source,b.target,mul(b.witness,a.witness),(a,b))

def leafword(a):
    return tuple(p for child in a.parents for p in leafword(child)) if a.parents else (a.payload(),)

arrows=tuple(Arrow(i,g[i],g) for i in V for g in G)
assert len(arrows)==96
hom={(i,j):tuple(a for a in arrows if (a.source,a.target)==(i,j)) for i in V for j in V}
assert all(len(v)==6 for v in hom.values())
assert sum(a.source!=a.target for a in arrows)==72
H=tuple(g for g in G if g[0]==0)
assert len(H)==6
# A root-frame choice is a coordinate section; it does not discard witnesses.
tau={i:unit if i==0 else swap(0,i) for i in V}
def residual(a,frames): return mul(inv(frames[a.target]),mul(a.witness,frames[a.source]))
for a in arrows:
    h=residual(a,tau)
    assert h in H
    assert mul(tau[a.target],mul(h,inv(tau[a.source])))==a.witness
    assert compose(Arrow(a.target,a.source,inv(a.witness)),a).witness==unit
    assert compose(Arrow(a.target,a.target,unit),a).payload()==a.payload()
    for b in arrows:
        if b.source!=a.target: continue
        ab=compose(b,a)
        assert residual(ab,tau)==mul(residual(b,tau),h)

# Independently change each local frame through every permitted root stabilizer.
# The isotropy coordinate changes by endpoint gauge factors, not deletion.
for port in V:
    for u in H:
        changes={i:u if i==port else unit for i in V}
        frames={i:mul(tau[i],changes[i]) for i in V}
        for a in arrows:
            old=residual(a,tau); new=residual(a,frames)
            assert new==mul(inv(changes[a.target]),mul(old,changes[a.source]))
            assert mul(frames[a.target],mul(new,inv(frames[a.source])))==a.witness

# Three source-admissible boundary-changing comparisons have a nontrivial loop.
a=Arrow(0,1,swap(0,1)); b=Arrow(1,2,swap(1,2)); c=Arrow(2,0,swap(2,0))
left=compose(c,compose(b,a)); right=compose(compose(c,b),a)
assert left.payload()==right.payload() and left!=right
assert leafword(left)==leafword(right)==(a.payload(),b.payload(),c.payload())
assert left.witness==swap(1,2)!=unit and left.witness[0]==0
# Full permutation-code observations separate every pair forgotten by endpoints.
for bucket in hom.values():
    for x,y in combinations(bucket,2):
        assert x.source==y.source and x.target==y.target
        assert any(x.witness[k]!=y.witness[k] for k in V if k!=x.source)
# Setting every isotropy residual to identity is a special flat section, not
# a coordinate change of a nonidentity based loop.
for u in H: assert mul(inv(u),mul(left.witness,u))!=unit

result={
 'status':'passed',
 'classification':'source_comparison_retains_groupoid_witness_instead_of_selecting_flat_section',
 'obligation':'source constructor realization with retained boundary and equivalence',
 'stratum':'Four differently pointed copies of one four-element carrier; finite shadow of existing supplied-equivalence constructors',
 'checks':{'objects':4,'comparison_payloads':96,'off_diagonal_payloads':72,
           'witnesses_per_endpoint_pair':6,'root_isotropy_size':6,
           'composition_and_inverse':True,'frame_coordinate_reconstruction':True,
           'all_local_frame_changes':True,'parent_histories_retained':True,
           'endpoint_quotient_not_faithful':True},
 'source_hashes':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
 'verdict':'The source supplies an actual equivalence as input and retains it. Keep its six-valued isotropy coordinate (or the full permutation); flatness is a property of selected routes, not a replacement for the witness.',
 'unsupported':['identification of the137 matrix slots with this finite source sector',
                'selection of a particular filler for every carrier edge',
                'physical gauge interpretation or metric','fresh Agda compilation'],
 'next_constructor':'Map the supplied comparison witnesses and their endpoint types into the137-slot response model without discarding isotropy or parent histories.'
}
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
