"""Actual physical pullback matrices: integer homology and compatible detector image."""
from pathlib import Path
import ast,hashlib,itertools,json
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
source=ROOT/'research/voevodsky/check_physical_derived_pullback_after_transform.py'
paths=[Path(__file__),HERE/'readout-contract-realized-pullback.md',source,ROOT/'src/ledger/20260817-435 The Global Mixed-Variance Transform Lands on the Unique Framed Connector.md',ROOT/'src/ledger/20260817-436 The Physical Derived Pullback Is One Primitive Integral Line.md',ROOT/'research/nima/rzk-coefficient-interface-v213.md',ROOT/'research/nima/rzk-coefficient-interface-v216.md']
def hashes():return {p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
def mv(A,v):return tuple(sum(a*b for a,b in zip(row,v)) for row in A)
def mm(A,B):return [list(mv(A,col)) for col in zip(*B)]
before=hashes();data={}
main=next(n for n in ast.parse(source.read_text(encoding='utf-8')).body if isinstance(n,ast.FunctionDef) and n.name=='main')
for node in main.body:
 if isinstance(node,ast.Assign) and len(node.targets)==1 and isinstance(node.targets[0],ast.Name) and node.targets[0].id in ('d1','d2','d3','primitive'):
  data[node.targets[0].id]=ast.literal_eval(node.value)
d1,d2,d3,z=[data[k] for k in ('d1','d2','d3','primitive')]
r=(0,0,1,1,1);c=(1,-1,0,0,0);detectors=[r,c,r]
assert tuple(c[i]-r[i] for i in range(5))==tuple(d1[0])
assert all(not any(col) for col in mm(d1,d2))
assert all(not any(col) for col in mm(d2,d3))
assert all(not any(col) for col in mm(detectors,d2))
assert mv(d1,z)==(0,) and mv(detectors,z)==(1,1,1)
count=0
for x1,x2,x3,x4 in itertools.product(range(-2,3),repeat=4):
 x=(x1+x2+x3+x4,x1,x2,x3,x4);n=x2+x3+x4
 boundary=mv(d2,(x1,-x3-x4,-x4,0))
 assert tuple(n*z[i]+boundary[i] for i in range(5))==x
 assert mv(detectors,x)==(n,n,n)
 count+=1
for w in itertools.product(range(-2,3),repeat=4):
 if mv(d2,w)==(0,)*5:assert w==mv(d3,(w[1],))
assert mv(d1,(1,0,0,0,0))==(1,)
for n in range(-12,13):
 image=(n,n,n)
 assert (image[0]-image[1],image[1]-image[2])==(0,0)
 assert (-sum(image))%3==0
 assert tuple(a%3 for a in image)==(n%3,)*3
# H is onto: (a,b) lifted by (a+b,b,0).
for a,b in itertools.product(range(-3,4),repeat=2):
 image=(a+b,b,0)
 assert (image[0]-image[1],image[1]-image[2])==(a,b)
assert before==hashes()
report={'passed':True,'source_unchanged':True,'source_sha256':before,'integer_cycle_witness_controls':count,'primitive_detector_image':[1,1,1],'compatible_output':'diagonal Z in Z^3','arbitrary_ambient_triples_realized':False,'scalar_trace_mod3_preserves_primitive_class':False,'retained_packet_mod3_preserves_primitive_class':True,'scope':'Existing chain and detector realization, not a new proof of global fs/Kato geometry or unrestricted physical amplitude identification.'}
(HERE/'readout-contract-realized-pullback.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,indent=2))
