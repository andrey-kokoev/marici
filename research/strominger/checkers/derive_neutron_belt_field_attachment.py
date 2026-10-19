"""Derive native N weights/operators from belt geometry, not retained modes."""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import sys,json,hashlib
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/'research/voevodsky/checkers'))
from check_belt_operator_inputs import frame,action,mode,mean
from check_coupled_six_piece_belt import R,Z,norm,encoded
from assemble_metric_coefficient_protocol import A,ZERO,read_operator,product
BASE=ROOT/'research/strominger/results';NATIVE=ROOT/'research/voevodsky/results'
def lift(z):
    c=[F(0)]*16
    for k,v in zip([0,1,10,11],encoded(z)):c[k]=F(v)
    return A(tuple(c))
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def rational(x):assert x.b==0;return x.a
geometry=json.loads((NATIVE/'four_six_center_cones.json').read_text());ambient=json.loads((NATIVE/'coupled_six_piece_belt_store.json').read_text())['record'];retained=json.loads((NATIVE/'belt_three_by_twelve_store.json').read_text())
triangles=list(map(tuple,ambient['triangles']));faces=geometry['belt_faces'];owners=ambient['face_owners'];index={t:i for i,t in enumerate(triangles)}
points={k:tuple(map(F,v)) for k,v in geometry['belt_scaled_coordinates'].items()}
for f in faces:points['F_'+'_'.join(sorted(f))]=mean([points[k] for k in f])
coords={k:frame(v) for k,v in points.items()};inverse={v:k for k,v in coords.items()};rotation=((F(0),F(0),F(1)),(F(1),F(0),F(0)),(F(0),F(1),F(0)))
rename={k:inverse[action(rotation,v)] for k,v in coords.items()};perm=[index[tuple(rename[v] for v in t)] for t in triangles];facePerm=[next(j for j,f in enumerate(faces) if set(f)=={rename[v] for v in face}) for face in faces]
adjacent=[j for j in range(1,6) if len(set(faces[0])&set(faces[j]))==2];assert len(adjacent)==2
pair=(0,adjacent[0]);pairs=[]
for _ in range(3):pairs.append(pair);pair=tuple(facePerm[i] for i in pair)
assert sorted(i for pair in pairs for i in pair)==list(range(6))
reference=[i for i in range(18) if owners[i] in pairs[0]];order=reference+[perm[i] for i in reference]+[perm[perm[i]] for i in reference];assert order==retained['triangle_order']
planes=[]
for t in triangles:
    rr,ss=mode(t,points);r,s=tuple(R(*x) for x in rr),tuple(R(*x) for x in ss)
    a,b=rational(dot(s,s)),rational(dot(r,s));v=tuple(x-(b/a)*y for x,y in zip(r,s));beta=rational(dot(v,v));assert a>0 and beta>0 and dot(v,s)==0
    planes.append({'columns':(s,v),'d':(a,beta),'z':((R(b),R(a)),(R(beta),R()))})
for t in range(18):
    for axis in range(2):assert tuple(sum(rotation[a][b]*planes[t]['columns'][axis][b] for b in range(3)) for a in range(3))==planes[perm[t]]['columns'][axis]
d=[x for t in order for x in planes[t]['d']];z=[lift(x) for t in order for x in planes[t]['z']];assert d[:12]==d[12:24]==d[24:] and z[:12]==z[12:24]==z[24:]
source=json.loads((BASE/'common-three-carrier-protocol/neutron.json').read_text());assert list(map(F,source['source']['metric']))==[1/x for x in d]
assert source['source']['coordinates']==[f'triangle-{t}:axis-{axis}' for t in order for axis in range(2)]
sectorNorm=sum((z[i].flip(8)*z[i]/A(d[i]) for i in range(12)),ZERO)
L={(i,j):z[i]*z[j].flip(8)/(sectorNorm*A(d[j])) for i in range(36) for j in range(36) if i//12==j//12}
G={(i,j):A(F(1,3)) for i in range(36) for j in range(36) if i%12==j%12};N=product(G,L)
for name,m in [('L',L),('G',G),('N',N)]:assert m==read_operator(source['operators'][name],36)
gridData=json.loads((BASE/'baryon-tensor-grid/verification.json').read_text())['carriers']['neutron'];assert gridData['grid']==[[i,i+12,i+24] for i in range(12)]
weights=[z[i].flip(8)*z[i]/(A(d[i])*sectorNorm) for i in range(12)];assert [w.record() for w in weights]==gridData['rowProbabilities'];assert gridData['columnProbabilities']==[A(F(1,3)).record()]*3
bindings=[]
for i in range(12):
    slots=[i,i+12,i+24];ts=[order[k//2] for k in slots];assert ts==[ts[0],perm[ts[0]],perm[perm[ts[0]]]]
    bindings.append({'gridRow':i,'axis':i%2,'triangles':ts,'surfacePatches':[triangles[t] for t in ts],'probability':weights[i].record()})
# Native belt has two open triangular rims; not a tetrahedron's closed surface.
edges=Counter(tuple(sorted((f[i],f[(i+1)%3]))) for f in faces for i in range(3));vertices=set(v for f in faces for v in f);rim=[e for e,n in edges.items() if n==1];assert len(vertices)==6 and len(edges)==12 and len(faces)==6 and len(rim)==6
components=[];unseen=set(v for e in rim for v in e)
while unseen:
    found={min(unseen)};q=list(found)
    for v in q:
        for edge in rim:
            if v in edge:
                for w in edge:
                    if w not in found:found.add(w);q.append(w)
    unseen-=found;components.append(sorted(found))
assert sorted(map(len,components))==[3,3]
paths=[Path(__file__).resolve(),NATIVE/'four_six_center_cones.json',NATIVE/'coupled_six_piece_belt_store.json',NATIVE/'belt_three_by_twelve_store.json',BASE/'common-three-carrier-protocol/neutron.json',ROOT/'research/voevodsky/checkers/check_belt_operator_inputs.py']
result={'status':'native-neutron-geometric-weights-and-field-derived','surface':{'parentFaces':6,'smallTriangles':18,'intrinsicComponentsPerTriangle':2,'totalComponents':36,'rotatingSectors':3,'trianglesPerSector':6,'componentsPerSector':12,'adjacentFacePairs':pairs,'boundaryRims':components,'eulerCharacteristic':0},'nativeMetricReconstructed':True,'nativeFullOperatorsReconstructed':['L','G','N'],'allTensorWeightsDerivedFromGeometry':True,'gridGeometry':bindings,'TAttachmentGate':'Native field is attached to a six-face belt with two boundary rims, not to the closed four-face boundary of the single N reader tetrahedron. It can be retained as an internal geometric fiber, but a restriction/embedding/sewing map from this belt to T is additional input.','sourceHashes':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},'scope':'Reconstructs existing native N law from saved belt vertices, oriented corners, metric frame, cyclic character and adjacent-face grouping. No retained selected numerators used to build weights or operators. Neither arbitrary weights nor physical masses fitted. Underlying belt geometry and conventions remain supplied; no global PNE field derived. Production/viewer unchanged.'}
out=BASE/'neutron-belt-field-attachment';out.mkdir(exist_ok=True);(out/'verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:result[k] for k in ['status','surface','nativeMetricReconstructed','nativeFullOperatorsReconstructed','allTensorWeightsDerivedFromGeometry']}))
