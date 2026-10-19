"""Frozen assembly-independent transport and ordinary graded-candidate screen.
Exact affine coefficients prove identities for arbitrary real displacements;
finite degree counts reject only the explicitly declared Sym(V) candidate.
"""
from pathlib import Path
from fractions import Fraction as F
from math import comb
from collections import defaultdict
import hashlib,json

ROOT=Path(__file__).resolve().parents[3]
BASE=ROOT/'research/strominger/results'
PROTOCOL=ROOT/'research/strominger/graded-parent-transport-protocol-v1.md'
# Independent formal variables p(3),u(3),v(3),q(3), not sampled points.
zero=(0,)*12
basis=lambda i:tuple(int(i==j) for j in range(12))
add=lambda a,b:tuple(x+y for x,y in zip(a,b))
neg=lambda a:tuple(-x for x in a)
plus=lambda a,b:tuple(add(x,y) for x,y in zip(a,b))
minus=lambda a,b:plus(a,tuple(map(neg,b)))
p,u,v,q=[tuple(basis(i+j) for j in range(3)) for i in [0,3,6,9]]
identity=(zero,)*3
transport=plus
assert transport(p,identity)==p
assert transport(transport(p,v),u)==transport(p,plus(u,v))
assert transport(transport(p,v),tuple(map(neg,v)))==p
assert minus(transport(p,v),transport(q,v))==minus(p,q)
def squared_norm(vector):
    coefficients=defaultdict(int)
    for coordinate in vector:
        for i,a in enumerate(coordinate):
            for j,b in enumerate(coordinate):coefficients[tuple(sorted((i,j)))]+=a*b
    return {k:v for k,v in coefficients.items() if v}
assert squared_norm(minus(transport(p,v),transport(q,v)))==squared_norm(minus(p,q))
# The fiber leg is explicitly identity. It commutes with every fixed linear
# operator and leaves the metric/readout unchanged in this chosen trivialization.
# No such trivialization is claimed derived from the native reader interface.
assert transport(p,u)!=transport(p,plus(u,v))  # dropped displacement control
bad=lambda point,shift:plus(plus(point,point),shift)
assert squared_norm(minus(bad(p,v),bad(q,v)))!=squared_norm(minus(p,q))
def in_bcc(point):
    return any(all((x-offset)/4==int((x-offset)/4) for x in point) for offset in [0,2])
assert in_bcc((F(0),)*3)
assert not in_bcc((F(1,2),F(0),F(0)))

count_path=BASE/'native-36-count-screen/verification.json'
alignment_path=BASE/'field-comparison-preparation/verification.json'
count=json.loads(count_path.read_text(encoding='utf8'))
alignment=json.loads(alignment_path.read_text(encoding='utf8'))
checked=0
for evidence in [count,alignment]:
    for path,digest in evidence['sourceHashes'].items():
        assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==digest, 'stale input: '+path
        checked+=1
assert count['rawDimensions']['proton']==36
assert alignment['alignmentGeometry']['complexRank']==3
# Explicit ordinary polynomial grading: each generator has degree one.
def symmetric_dimensions(d,degree):
    coefficients=[1]+[0]*degree
    for _ in range(d):
        coefficients=[sum(coefficients[:n+1]) for n in range(degree+1)]
    assert coefficients==[comb(d+n-1,n) for n in range(degree+1)]
    return coefficients
moonshine=[1,0,196884,21493760]  # comparison target, not derived from native fields
candidates=[]
for label,d in [('alignment',3),('baryon',36)]:
    dims=symmetric_dimensions(d,3)
    mismatch=next(i for i,(a,b) in enumerate(zip(dims,moonshine)) if a!=b)
    assert mismatch==1
    candidates.append({'input':label,'dimension':d,'candidate':'ordinary Sym(C^d)',
                       'degrees':[0,1,2,3],'dimensions':dims,'firstMismatchDegree':mismatch,
                       'verdict':'rejected-as-grading-preserving-moonshine-realization',
                       'sourceCanonicalParent':False})
assert candidates[0]['dimensions']==[1,3,6,10]
assert candidates[1]['dimensions']==[1,36,666,8436]
# Any nonzero d has degree-one dimension d, unlike the moonshine target.
# This general formula rejects the whole stated degree-one-generator family,
# not enriched, differently graded, quotient or vertex-algebra constructions.
result={
    'status':'pass',
    'classification':'conditional-free-transport-constructed-naive-graded-candidates-rejected-parent-open',
    'conditionalTransport':{'ambient':'Euclidean R3','bundle':'trivial R3 x V',
        'formula':'T_v(p,z)=(p+v,z)','exactSymbolicIdentities':['identity','composition','inverse','pairwise-difference','squared-distance'],
        'scope':'All real displacements and arbitrary subsets in this declared comparison model. Fiber identity preserves fixed fiber operators, metrics and readouts. No native connection or sewing law is derived.'},
    'fixedLatticeControl':{'lattice':'(4Z)^3 union ((2,2,2)+(4Z)^3)',
        'originInLattice':True,'displacement':['1/2','0','0'],'translatedOriginInLattice':False},
    'gradedCandidates':candidates,'moonshineComparisonDimensions':moonshine,
    'gradingPolicy':'ordinary polynomial degree, generators degree1; no shifts or fitted generators',
    'missingInputs':['canonical graded parent and source-defined grading/product',
                     'native arbitrary-displacement transition/connection with full interface compatibility',
                     'canonical sector realization and readout maps',
                     'source-derived modular trace law, central-charge structure or other ledger996 witness and independent replication',
                     'actual automorphism-group identification; for Baby Monster an appropriate action and involution/centralizer construction'],
    'nativeArbitraryTransportDerived':False,'canonicalParentConstructed':False,
    'monsterGateActivated':False,'babyMonsterActionConstructed':False,
    'wholeCellAssemblyRequired':False,'physicalValidation':False,'formalOutcome':None,
    'reusedDirectInputHashesChecked':checked,'freshNativeFieldReplay':False,
    'negativeControls':['dropped displacement detected','nonisometric spatial dilation detected','continuous translation need not preserve fixed lattice','naive degree1 sector fails moonshine target']}
ledger=ROOT/'src/ledger'
sources=[Path(__file__),PROTOCOL,count_path,alignment_path]+[
    ledger/'20260819-985 Weak Calculus Universality and the Strong Parent-Object Hypothesis.md',
    ledger/'20260819-990 The Parent May Co-Generate Lenses and Readouts.md',
    ledger/'20260819-996 Monster Symmetry Is a Gated Graded-Parent Research Direction.md',
    ledger/'20260824-2002 The Post-Admission Operations Table (Cross-Sector Synthesis II, WP47).md']
result['sourceHashes']={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}
out=BASE/'graded-parent-transport';out.mkdir(exist_ok=True)
(out/'verification.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:result[k] for k in ['status','classification','gradedCandidates','monsterGateActivated','nativeArbitraryTransportDerived']}))
