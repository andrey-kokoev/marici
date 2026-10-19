"""Independent exact homology and lift checks for the proposed chart base."""
from pathlib import Path
from fractions import Fraction
from itertools import combinations
import json,hashlib
ROOT=Path(__file__).resolve().parents[3];out=ROOT/'research/strominger/results/realization-periodic-cover';data=(out/'verification.json').read_bytes();d=json.loads(data)
def rank(m):
    a=[[Fraction(x) for x in row] for row in m];r=0
    for j in range(len(a[0])):
        k=next((i for i in range(r,len(a)) if a[i][j]),None)
        if k is None:continue
        a[k],a[r]=a[r],a[k];p=a[r][j];a[r]=[x/p for x in a[r]]
        for i in range(r+1,len(a)):
            p=a[i][j]
            if p:a[i]=[x-p*y for x,y in zip(a[i],a[r])]
        r+=1
        if r==len(a):break
    return r
faces=sorted({tuple(sorted(f)) for f in d['proposedBaseTriangles']});edges=sorted({e for f in faces for e in combinations(f,2)});vertices=sorted({v for e in edges for v in e});b1=[[0]*len(edges) for v in vertices];b2=[[0]*len(faces) for e in edges]
for j,(a,b) in enumerate(edges):b1[vertices.index(a)][j]=-1;b1[vertices.index(b)][j]=1
for j,f in enumerate(faces):
    for i in range(3):b2[edges.index(f[:i]+f[i+1:])][j]=(-1)**i
assert all(sum(b1[i][j]*b2[j][k] for j in range(len(edges)))==0 for i in range(len(vertices)) for k in range(len(faces)))
r1,r2=rank(b1),rank(b2);betti=[len(vertices)-r1,len(edges)-r1-r2,len(faces)-r2];assert betti==[1,2,1]
assert all(sum(set(e)<=set(f) for f in faces)==2 for e in edges)
for case in d['rows']:
    for rec in case['records']:
        assert 2*rec['winding']+rec['phase']==rec['origin'];assert len(rec['history'])==rec['origin']
        for name,o in rec['occurrences'].items():assert o['index']==rec['origin']+int(name[1:])
    for rec in case['records'][:-2]:
        later=case['records'][rec['origin']+2];assert rec['phase']==later['phase'];assert later['winding']==rec['winding']+1;assert rec['chartKey']==later['chartKey'];assert rec['history']!=later['history']
result={'status':'periodic-base-and-lift-verified','simplexCounts':[len(vertices),len(edges),len(faces)],'rationalBettiNumbers':betti,'markings':len(d['rows']),'nativeOriginRecoveredExactly':True,'fullHistoryRetained':True,'phaseOnlyIdentificationRejected':True,'inputSha256':hashlib.sha256(data).hexdigest(),'checkerSha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Torus topology of constructed base, independent consistency of saved integer lifts. This is not topology of the full native packet space or an identification of the two circles with M and C.'}
(out/'topology-verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
