"""Exact norm-preserving transport of native geometric patch modes.
Uses a small real/complex multiradical ring; no numerical square roots.
"""
from pathlib import Path
from fractions import Fraction as F
from math import gcd
from collections import Counter
import sys,json,hashlib
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/'research/voevodsky/checkers'))
from check_belt_operator_inputs import mode,mean
from check_coupled_six_piece_belt import R
BASE=ROOT/'research/strominger/results';NATIVE=ROOT/'research/voevodsky/results'
class Radical:
    # key n denotes sqrt(n) for positive squarefree n, i sqrt(-n) otherwise.
    def __init__(self,d=0):self.d={k:F(v) for k,v in d.items() if v} if isinstance(d,dict) else ({1:F(d)} if d else {})
    def __add__(self,other):
        other=other if isinstance(other,Radical) else Radical(other);d=dict(self.d)
        for k,v in other.d.items():d[k]=d.get(k,F(0))+v
        return Radical(d)
    __radd__=__add__
    def __neg__(self):return Radical({k:-v for k,v in self.d.items()})
    def __sub__(self,o):return self+-o
    def __mul__(self,other):
        other=other if isinstance(other,Radical) else Radical(other);d={}
        for a,x in self.d.items():
            for b,y in other.d.items():
                g=gcd(abs(a),abs(b));key=(abs(a)//g)*(abs(b)//g)*(-1 if (a<0)!=(b<0) else 1);v=x*y*g*(-1 if a<0 and b<0 else 1);d[key]=d.get(key,F(0))+v
        return Radical(d)
    __rmul__=__mul__
    def conj(self):return Radical({k:v*(-1 if k<0 else 1) for k,v in self.d.items()})
    def __eq__(self,other):return self.d==(other.d if isinstance(other,Radical) else Radical(other).d)
    def record(self):return {str(k):str(v) for k,v in sorted(self.d.items())}
def sqrt(q):
    q=F(q)
    if not q:return Radical()
    sign=-1 if q<0 else 1;q=abs(q);n=q.numerator*q.denominator;outside=1;inside=1;p=2
    while p*p<=n:
        k=0
        while n%p==0:n//=p;k+=1
        outside*=p**(k//2)
        if k%2:inside*=p
        p+=1
    inside*=n
    return Radical({sign*inside:F(outside,q.denominator)})
def mm(a,b):return [[sum((a[i][k]*b[k][j] for k in range(len(b))),Radical()) for j in range(len(b[0]))] for i in range(len(a))]
def adj(a):return [[a[j][i].conj() for j in range(len(a))] for i in range(len(a[0]))]
def frame2(v):return [[v[0],-v[1].conj()],[v[1],v[0].conj()]]
def vector(v):return [[x] for x in v]
def projector(v):return mm(vector(v),adj(vector(v)))
def field_mode(a,b,beta):
    norm=beta+b*b/a+3*a
    return [b*sqrt(1/(a*norm))+sqrt(-3*a/norm),sqrt(beta/norm)]
def shape(a,b,beta):
    rr=beta+b*b/a;return ((rr-3*a)**2+12*b*b)/(rr+3*a)**2
I=[[Radical(1),Radical()],[Radical(),Radical(1)]]
# Test the exact arithmetic independently on nontrivial radicals/signs.
for q in [F(2),F(3),F(5),F(149,150),F(592,1341),F(-3),F(-7,9)]:assert sqrt(q)*sqrt(q)==q
assert sqrt(2)*sqrt(3)==sqrt(6);assert sqrt(-2)*sqrt(-3)==-sqrt(6)
# P reference patch (F_ABC,A,B) in its intrinsic orthogonal axes.
aP,bP,betaP=F(2),F(0),F(2,3);v=field_mode(aP,bP,betaP);assert mm(adj(vector(v)),vector(v))==[[Radical(1)]];rhoP=shape(aP,bP,betaP);assert rhoP==F(16,25)
geometry=json.loads((NATIVE/'four_six_center_cones.json').read_text());ambient=json.loads((NATIVE/'coupled_six_piece_belt_store.json').read_text())['record'];points={k:tuple(map(F,p)) for k,p in geometry['belt_scaled_coordinates'].items()}
for face in geometry['belt_faces']:points['F_'+'_'.join(sorted(face))]=mean([points[k] for k in face])
rows=[]
for index,triangle in enumerate(ambient['triangles']):
    rr,ss=mode(triangle,points);r,s=tuple(R(*x) for x in rr),tuple(R(*x) for x in ss);dot=lambda a,b:sum(x*y for x,y in zip(a,b));aa,bb=dot(s,s),dot(r,s);assert aa.b==bb.b==0;a,b=aa.a,bb.a;orth=tuple(x-(b/a)*y for x,y in zip(r,s));bet=dot(orth,orth);assert bet.b==0;beta=bet.a
    w=field_mode(a,b,beta);rhoN=shape(a,b,beta);assert rhoN!=rhoP
    assert mm(adj(vector(w)),vector(w))==[[Radical(1)]]
    U=mm(frame2(w),adj(frame2(v)));assert mm(adj(U),U)==I;assert U[0][0]*U[1][1]-U[0][1]*U[1][0]==1
    assert mm(U,vector(v))==vector(w);assert mm(mm(U,projector(v)),adj(U))==projector(w)
    # A real spatial isometry plus scalar phase preserves rho; all N patches
    # differ from P. This U instead mixes complex plane components internally.
    rows.append({'triangleIndex':index,'triangle':triangle,'planeDenominators':[str(a),str(beta)],'crossTerm':str(b),'neutronEllipticityInvariant':str(rhoN),'normalizedTarget':[x.record() for x in w],'transport':[[x.record() for x in row] for row in U]})
attachment=json.loads((BASE/'neutron-reader-field-interface/verification.json').read_text());store=json.loads((NATIVE/'belt_three_by_twelve_store.json').read_text());reference=attachment['charts'][0]['readerPatches'];incoming=[store['triangle_order'][i] for i,t in enumerate(reference) if t[0]=='F_buv'];assert len(incoming)==3
# The geometrically attached incoming face uses three actual belt patches.
# Direct sum of their U blocks is a unitary 6-component tangential interface.
assert len(set(incoming))==3
# Local patch unitaries alone cannot change the relative patch norms. Derive
# an additional real mixing from the actual native incoming-face weights.
norms=[];ws=[]
for i in incoming:
    a,beta=map(F,rows[i]['planeDenominators']);b=F(rows[i]['crossTerm']);norms.append(beta+b*b/a+3*a);ws.append(field_mode(a,b,beta))
prob=[x/sum(norms) for x in norms];assert prob[0]==prob[2] and prob[0]!=F(1,3)
ps,pm=sqrt(F(2,3)),sqrt(F(1,3));qs,qm=sqrt(2*prob[0]),sqrt(prob[1]);c,s=ps*qs+pm*qm,ps*qm-pm*qs
basis=[[sqrt(F(1,2)),Radical(),sqrt(F(1,2))],[Radical(),Radical(1),Radical()],[sqrt(F(1,2)),Radical(),-sqrt(F(1,2))]]
V=mm(mm(basis,[[c,-s,Radical()],[s,c,Radical()],[Radical(),Radical(),Radical(1)]]),adj(basis));I3=[[Radical(int(i==j)) for j in range(3)] for i in range(3)];assert mm(adj(V),V)==I3
assert mm(V,[[sqrt(F(1,3))] for _ in range(3)])==[[sqrt(p)] for p in prob]
block=lambda matrices:[[matrices[i//2][i%2][j%2] if i//2==j//2 else Radical() for j in range(6)] for i in range(6)]
V2=[[V[i//2][j//2] if i%2==j%2 else Radical() for j in range(6)] for i in range(6)]
faceU=mm(mm(block([frame2(w) for w in ws]),V2),block([adj(frame2(v))]*3));I6=[[Radical(int(i==j)) for j in range(6)] for i in range(6)];assert mm(adj(faceU),faceU)==I6
sourceFace=[sqrt(F(1,3))*x for _ in range(3) for x in v];targetFace=[sqrt(p)*x for p,w in zip(prob,ws) for x in w]
assert mm(faceU,vector(sourceFace))==vector(targetFace);assert mm(mm(faceU,projector(sourceFace)),adj(faceU))==projector(targetFace)
faceTransport={'nativeTargetPatchProbabilities':list(map(str,prob)),'sourcePatchProbabilities':['1/3']*3,'patchwiseTransportAloneSuffices':False,'additionalMixing':'real rotation in symmetric-outer/middle patch-amplitude plane; antisymmetric outer mode fixed','unitaryOnAllSixTangentialComponents':True,'nativeNormalizedFaceModesIntertwineExactly':True,'matrix':[[x.record() for x in row] for row in faceU]}
result={'status':'native-PN-patch-mode-transport-constructed','protonEllipticityInvariant':str(rhoP),'neutronInvariantCounts':dict(Counter(r['neutronEllipticityInvariant'] for r in rows)),'realSpatialIsometryPlusScalarPhasePossible':False,'complexTransportFormula':'U=F(w) F(v)*, F(z)=[[z0,-conj(z1)],[z1,conj(z0)]]; v,w are native normalized plane modes','unitaryDeterminantOneTransportsChecked':len(rows),'incomingReaderFaceTriangleIndices':incoming,'incomingTangentialInterfaceDimension':6,'incomingFaceTransport':faceTransport,'rows':rows,'scope':'Exact source-derived normalized patch-mode SU(2) transport, with explicit intrinsic axes and cyclic phases. Six-dimensional incoming-face unitary includes source-derived patch-weight mixing, not merely a direct sum of local maps. A minimal real mixing convention is explicit. Not a complete 36-dimensional PN operator and not NE. The real spatial-isometry obstruction concerns patch ellipticity. Full P face has nine ambient components: projecting to six tangential components loses three normal directions on general inputs. Native selected local modes are tangential, but global alignment/projector sewing across all patches remains unchecked. SU(2) here denotes internal complex two-component transport, not a derived physical spin or interaction law.'}
files=[Path(__file__).resolve(),NATIVE/'four_six_center_cones.json',NATIVE/'coupled_six_piece_belt_store.json',NATIVE/'belt_three_by_twelve_store.json',BASE/'neutron-reader-field-interface/verification.json'];result['sourceHashes']={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in files};out=BASE/'native-patch-mode-transport';out.mkdir(exist_ok=True);(out/'verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:result[k] for k in ['status','protonEllipticityInvariant','neutronInvariantCounts','unitaryDeterminantOneTransportsChecked','incomingTangentialInterfaceDimension']}))
