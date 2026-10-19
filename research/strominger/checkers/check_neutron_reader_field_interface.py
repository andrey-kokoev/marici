"""Three co-moving belt charts onto a two-face N reader, with exact field maps."""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations, permutations, product as choices
import sys,json,hashlib
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/'research/voevodsky/checkers'))
from check_belt_operator_inputs import frame,action
from check_coupled_six_piece_belt import R
from assemble_metric_coefficient_protocol import A,ONE,read_operator,product
BASE=ROOT/'research/strominger/results';NATIVE=ROOT/'research/voevodsky/results'
geo=json.loads((NATIVE/'four_six_center_cones.json').read_text());ambient=json.loads((NATIVE/'coupled_six_piece_belt_store.json').read_text())['record'];store=json.loads((NATIVE/'belt_three_by_twelve_store.json').read_text());attachment=json.loads((BASE/'neutron-belt-field-attachment/verification.json').read_text())
faces=geo['belt_faces'];pairs=attachment['surface']['adjacentFacePairs'];triangles=list(map(tuple,ambient['triangles']));order=store['triangle_order'];points={k:tuple(map(F,v)) for k,v in geo['belt_scaled_coordinates'].items()};coords={k:frame(v) for k,v in points.items()};inverse={v:k for k,v in coords.items()};rot=((F(0),F(0),F(1)),(F(1),F(0),F(0)),(F(0),F(1),F(0)));rename={k:inverse[action(rot,v)] for k,v in coords.items()}
f0,f1=[set(faces[i]) for i in pairs[0]];shared=sorted(f0&f1);assert len(shared)==2
q0={shared[0]:'u',shared[1]:'v',next(iter(f0-f1)):'b',next(iter(f1-f0)):'c'}
charts=[]
for s in range(3):
    mapping=dict(q0)
    for _ in range(s):mapping={rename[k]:v for k,v in mapping.items()}
    assert set(mapping)==set().union(*(set(faces[i]) for i in pairs[s]))
    placed=[]
    for t in order[6*s:6*s+6]:
        centroid,a,b=triangles[t];face=centroid[2:].split('_');assert set(face)<=set(mapping)
        placed.append(('F_'+''.join(sorted(mapping[v] for v in face)),mapping[a],mapping[b]))
    assert len(set(placed))==6
    if charts:assert placed==charts[0]['readerPatches']
    charts.append({'sector':s,'facePair':pairs[s],'vertexMap':mapping,'readerPatches':placed})
# Gluing the whole belt directly into one fixed marked reader is stronger than
# three chart maps. Report actual disagreements rather than hiding them.
disagreements=[]
for i,j in combinations(range(3),2):
    a,b=charts[i]['vertexMap'],charts[j]['vertexMap']
    for v in sorted(set(a)&set(b)):
        if a[v]!=b[v]:disagreements.append({'charts':[i,j],'beltVertex':v,'readerImages':[a[v],b[v]]})
assert disagreements
# Exhaust all extensions of the shared-vertex identifications to tetrahedral
# vertex permutations. Two completions per overlap; none closes trivially.
labels=['b','c','u','v'];options=[]
for i,j in [(0,1),(1,2),(2,0)]:
    a,b=charts[i]['vertexMap'],charts[j]['vertexMap'];allowed=[]
    for p in permutations(labels):
        t=dict(zip(labels,p))
        if all(t[a[v]]==b[v] for v in set(a)&set(b)):
            parity=sum(labels.index(p[k])>labels.index(p[l]) for k in range(4) for l in range(k+1,4))%2
            allowed.append({'map':t,'parity':parity})
    assert len(allowed)==2;options.append(allowed)
holonomies=[]
for ts in choices(*options):
    h={v:ts[2]['map'][ts[1]['map'][ts[0]['map'][v]]] for v in labels};assert any(h[v]!=v for v in labels)
    holonomies.append({'transitionParities':[t['parity'] for t in ts],'vertexMonodromy':h})
proper=next(h for h in holonomies if h['transitionParities']==[0,0,0]);assert all(proper['vertexMonodromy'][proper['vertexMonodromy'][v]]==v for v in labels)
native=json.loads((BASE/'common-three-carrier-protocol/neutron.json').read_text());L=read_operator(native['operators']['L'],36);G=read_operator(native['operators']['G'],36);N=read_operator(native['operators']['N'],36)
restriction={(i,i+12*s):A(F(1,3)) for i in range(12) for s in range(3)};lift={(i+12*s,i):ONE for i in range(12) for s in range(3)};I={(i,i):ONE for i in range(12)};P={(i,j):v for (i,j),v in L.items() if i<12 and j<12}
assert product(restriction,lift)==I;assert product(lift,restriction)==G
assert product(P,P)==P;assert product(product(lift,P),restriction)==N
assert product(restriction,L)==product(P,restriction);assert product(L,lift)==product(lift,P)
metric=list(map(F,native['source']['metric']));readerMetric=[3*m for m in metric[:12]]
adjoint={(j,i):a.flip(8)*A(readerMetric[i]/metric[j]) for (i,j),a in restriction.items()};assert adjoint==lift
# Affine chart attachment, not a silent claim of Euclidean isometry.
sourceEdges={}
for a,b in combinations(q0,2):
    va,vb=[tuple(R(*x) for x in coords[k]) for k in (a,b)];d=sum((x-y)*(x-y) for x,y in zip(va,vb));assert d.b==0;sourceEdges['|'.join(sorted([q0[a],q0[b]]))]=d.a
T=json.loads((BASE/'T-metric-gluing/verification.json').read_text());isometric=[]
for row in T['rows']:
    ratios={sourceEdges[e]/F(row['metric'][e]) for e in sourceEdges}
    isometric.append(len(ratios)==1)
assert not any(isometric)
paths=[Path(__file__).resolve(),NATIVE/'four_six_center_cones.json',NATIVE/'coupled_six_piece_belt_store.json',NATIVE/'belt_three_by_twelve_store.json',BASE/'common-three-carrier-protocol/neutron.json',BASE/'neutron-belt-field-attachment/verification.json',BASE/'T-metric-gluing/verification.json']
result={'status':'local-reader-interface-and-native-field-descent-constructed','readerFaces':[['b','u','v'],['c','u','v']],'readerCoordinates':12,'charts':charts,'fieldMaps':{'restriction':'A(y)_i=(y_i+y_(i+12)+y_(i+24))/3','lift':'J(x)=(x,x,x)','readerMetric':list(map(str,readerMetric)),'readerProjector':'first 12x12 block of native L','identities':['AJ=I_12','JA=G','A*=J in retained source/induced reader metrics','AL=P_reader A','LJ=J P_reader','N=J P_reader A'],'lostDimension':24,'retainedDimension':12,'jointSurvivingDimension':1},'globalVertexGluingDisagreements':disagreements,'sharedVertexTransitionCompletions':options,'allEightLoopMonodromies':holonomies,'properPermutationLoop':proper,'referencePairSquaredDistances':{k:str(v) for k,v in sourceEdges.items()},'similarityToSavedNFacetMetrics':isometric,'sourceHashes':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},'scope':'Three explicit marked affine/barycentric chart maps of native adjacent-face pairs onto the N reader incoming/outgoing faces. Native co-moving component axes are carried as internal field-frame labels with their metric, not identified with Euclidean tangent axes of the target facet. Exact native projector descent proved. Restriction is lossy on general states; kernel remains in original 36-coordinate field. Charts disagree on shared belt vertices as maps to one fixed reader, and are not metric similarities. No globally glued metric field on T or full PNE sewing asserted. Production/viewer unchanged.'}
out=BASE/'neutron-reader-field-interface';out.mkdir(exist_ok=True);(out/'verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'status':result['status'],'readerCoordinates':12,'charts':3,'exactFieldIdentities':True,'globalVertexDisagreements':len(disagreements),'metricSimilarities':sum(isometric)}))
