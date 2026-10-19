"""Exact simplicial homology and native two-axis commutator checks."""
from itertools import combinations
from fractions import Fraction as F
from pathlib import Path
import json,hashlib
from electron_packet_interface import E,I,gmm,adj,sm
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/strominger/results'
def complex_of(facets):
    cells={}
    for f in facets:
        for n in range(1,len(f)+1):cells.setdefault(n-1,set()).update(tuple(sorted(c)) for c in combinations(f,n))
    return {k:sorted(v) for k,v in cells.items()}
def rank(m):
    if not m:return 0
    a=[[F(x) for x in row] for row in m];r=0
    for j in range(len(a[0])):
        pivot=next((i for i in range(r,len(a)) if a[i][j]),None)
        if pivot is None:continue
        a[r],a[pivot]=a[pivot],a[r];x=a[r][j];a[r]=[v/x for v in a[r]]
        for i in range(r+1,len(a)):
            x=a[i][j]
            if x:a[i]=[v-x*w for v,w in zip(a[i],a[r])]
        r+=1
        if r==len(a):break
    return r
def homology(facets):
    cs=complex_of(facets);top=max(cs);ranks={0:0,top+1:0};boundaries={}
    for k in range(1,top+1):
        index={s:i for i,s in enumerate(cs[k-1])};m=[[0]*len(cs[k]) for _ in cs[k-1]]
        for j,s in enumerate(cs[k]):
            for i in range(k+1):m[index[s[:i]+s[i+1:]]][j]=(-1)**i
        boundaries[k]=m;ranks[k]=rank(m)
    for k in range(2,top+1):
        a,b=boundaries[k-1],boundaries[k]
        assert all(sum(a[i][j]*b[j][l] for j in range(len(b)))==0 for i in range(len(a)) for l in range(len(b[0])))
    return {'simplexCounts':[len(cs[k]) for k in range(top+1)],'boundaryRanks':[ranks[k] for k in range(top+1)],'betti':[len(cs[k])-ranks[k]-ranks[k+1] for k in range(top+1)]}
metricFile=BASE/'T-metric-gluing/verification.json';raw=metricFile.read_bytes();data=json.loads(raw);facets=list(data['facets'].values());allVertices=sorted(set().union(*map(set,facets)))
readerComplex=homology(facets);fullT=homology([allVertices]);boundaryT=homology(list(combinations(allVertices,4)))
core={'u','v'};linkFacets=[tuple(set(f)-core) for f in facets if core<=set(f)];readerLink=homology(linkFacets)
fullLink=homology([tuple(set(allVertices)-core)])
# Positive control: triangulated periodic 3x3 square has torus Betti numbers.
torus=[];v=lambda i,j:(i%3)*3+j%3
for i in range(3):
    for j in range(3):torus.extend([(v(i,j),v(i+1,j),v(i+1,j+1)),(v(i,j),v(i+1,j+1),v(i,j+1))])
torusResult=homology(torus)
# Explicit new closure prototype: close the longitudinal strip while reversing
# the link-circle coordinate, as the tested b/c reflection does on that link.
twisted=[]
w=lambda i,j: (i*3+j%3) if i<3 else ((-j)%3)
for i in range(3):
    for j in range(3):twisted.extend([(w(i,j),w(i+1,j),w(i+1,j+1)),(w(i,j),w(i+1,j+1),w(i,j+1))])
twistedResult=homology(twisted);assert twistedResult['betti']==[1,1,0]
for faces in [torus,twisted]:
    cs=complex_of(faces)
    assert all(sum(set(edge)<=set(face) for face in cs[2])==2 for edge in cs[1])
    for vertex, in cs[0]:
        link=[tuple(set(face)-{vertex}) for face in cs[2] if vertex in face];assert homology(link)['betti']==[1,1]
assert readerComplex['betti']==[1,0,0,0];assert fullT['betti']==[1,0,0,0,0];assert boundaryT['betti']==[1,0,0,1];assert readerLink['betti']==[1,1];assert fullLink['betti']==[1,0,0];assert torusResult['betti']==[1,2,1]
minusI=sm(F(-1),I);commutators=[]
for i,j in combinations(range(3),2):
    for si in [-1,1]:
        for sj in [-1,1]:
            a,b=sm(F(si),E[i]),sm(F(sj),E[j]);comm=gmm(gmm(gmm(a,b),adj(a)),adj(b));assert comm==minusI;assert gmm(gmm(a,a),gmm(a,a))==I
            commutators.append({'axes':[i,j],'signs':[si,sj],'commutator':'-I','projectiveCommutator':'identity'})
paths=[metricFile,ROOT/'research/strominger/checkers/electron_packet_interface.py',ROOT/'research/strominger/checkers/check_T_torus_hypothesis.py'];hashes={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
result={'status':'torus-hypothesis-tested-on-current-complex','readerFacetUnion':readerComplex,'fullSimplexT':fullT,'boundaryOfT':boundaryT,'readerCoreEdgeLink':readerLink,'fullTCoreEdgeLink':fullLink,'torusPositiveControl':torusResult,'reflectionTwistedClosurePrototype':twistedResult,'nativeTwoAxisCommutators':commutators,'sourceHashes':hashes,'scope':'Rational simplicial homology of explicitly supplied complexes; no periodic M/C identification assumed. Native electron spin-axis pair is a separate source operation task; it is not yet identified with geometric M/C. Its -I commutator excludes an ordinary flat full-spinor torus representation for those generators, but permits investigation of projective/twisted structures. No torus topology is inferred from phase equivalence. Production/viewer unchanged.'}
out=BASE/'T-torus-hypothesis';out.mkdir(exist_ok=True);(out/'verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:result[k] for k in ['readerFacetUnion','readerCoreEdgeLink','fullSimplexT','boundaryOfT','torusPositiveControl','reflectionTwistedClosurePrototype']},indent=2));print('12 native signed axis pairs: commutator -I.')
