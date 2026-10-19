"""Recoverable full-field PN comparisons with a visible native C3 residual."""
from pathlib import Path
from fractions import Fraction as F
from copy import deepcopy
import sys,json,hashlib,gzip
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/nima'))
from anchored_contact_comparisons import prepare,recover,inverse,restore,R
sys.path.insert(0,str(ROOT/'research/strominger/checkers'))
from exact_multiradical import mm,adj,identity,serialize,decode_A,sqrt
from assemble_metric_coefficient_protocol import read_operator
sys.path.insert(0,str(ROOT/'research/nima/checkers'))
from check_twelve_triangle_positive_geometry import rotation
BASE=ROOT/'research/strominger/results';NATIVE=ROOT/'research/voevodsky/results';OUT=ROOT/'research/nima/results/anchored-PN-contact';OUT.mkdir(exist_ok=True)
inputHashes={}
def read(p):
    data=p.read_bytes();inputHashes[p]=hashlib.sha256(data).hexdigest();return json.loads(data)
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def mat(records):return [[restore(x) for x in row] for row in records]
def column(a,j):return [row[j] for row in a]
def mv(a,v):return column(mm(a,[[x] for x in v]),0)
def sharp(a,m):return [[x*m[j] for j,x in enumerate(row)] for row in adj(a)]
def gram(a,m):return mm(sharp(a,m),a)
def minus(a,b):return [[x-y for x,y in zip(r,s)] for r,s in zip(a,b)]
def native(d,key):
    sparse=read_operator(d['operators'][key],36)
    return [[decode_A(sparse[i,j].record()) if (i,j) in sparse else R() for j in range(36)] for i in range(36)]

pd=read(BASE/'common-three-carrier-protocol/proton.json');nd=read(BASE/'common-three-carrier-protocol/neutron.json');labels=pd['source']['coordinates'];metric=list(map(F,nd['source']['metric']))
patches=read(BASE/'tetrahedral-field-attachment/verification.json')['gridGeometry'];reader=read(BASE/'neutron-reader-field-interface/verification.json');belt=read(BASE/'neutron-belt-field-attachment/verification.json')
fixture=read(ROOT/'research/nima/results/two-reader-field-sewing/fixture.json');contact=next(c for c in fixture['final']['contacts'] if sorted(c['cells'])==[0,2]);assert 6 in contact['witnesses']
frames={p['outerArrow']:[[R(F(v)) for v in row] for row in p['rotation']] for p in patches}
Pports=[{'id':'P:'+p['outerArrow'],'dimension':3,'metric':['1']*3,'nativeLabels':[p['outerArrow']+':'+a for a in 'xyz'],'sourcePatch':p} for p in patches]
Nports=[{'id':f'N:s{i//6}:p{i%6}','dimension':2,'metric':[str(x) for x in metric[2*i:2*i+2]],'nativeLabels':nd['source']['coordinates'][2*i:2*i+2],'sector':i//6,'patchWithinSector':i%6} for i in range(18)]
descriptor={'schema':'marici.nima.PN-contact-coordinate-types.v1','contact':contact,'markedReaders':[{**fixture['packets'][p],'chartData':fixture['charts'][fixture['packets'][p]['chart']]} for p in [2,6]],'carriers':[{'id':'P','coordinateConvention':'native spatial amplitudes transformed by each retained R_patch transpose','ports':Pports},{'id':'N','coordinateConvention':'native internal plane components, all sectors; not target Euclidean tangent vectors','ports':Nports,'charts':reader['charts'],'chartTransitions':reader['sharedVertexTransitionCompletions'],'loopMonodromy':reader['properPermutationLoop'],'sourceReaderMetric':reader['fieldMaps']['readerMetric'],'affineNotSimilarity':reader['similarityToSavedNFacetMetrics'],'beltSurface':belt['surface']}],'sewingEqualityImposed':False}

def values(p,n):
    out={}
    for port in Pports:
        edge=port['id'][2:];out[port['id']]=mv(adj(frames[edge]),[p[labels.index(edge+':'+a)] for a in 'xyz'])
    for i,port in enumerate(Nports):out[port['id']]=n[2*i:2*i+2]
    return out

def fields(q):
    p=[R() for _ in range(36)];n=[]
    for port in Pports:
        edge=port['id'][2:];v=mv(frames[edge],q[port['id']])
        for a,x in zip('xyz',v):p[labels.index(edge+':'+a)]=x
    for port in Nports:n.extend(q[port['id']])
    return p,n

def packet(p,n):return prepare(descriptor,values(p,n))
def replay(pkt,p,n):assert fields(recover(pkt,descriptor))==(p,n)
# Exact inverse also handles non-rational anchor norms, without approximations.
for x in [R(3),sqrt(-1),sqrt(2)+sqrt(3),R(1)+sqrt(-2)+sqrt(5),sqrt(7)+sqrt(-3)]:assert x*inverse(x)==R(1)
zero=[R() for _ in range(36)];denseP=[R(i+1)+sqrt(-1)*(i%3-1) for i in range(36)];denseN=[R(2-i)+sqrt(-1)*(i%5) for i in range(36)];phase=sqrt(-1)
fixtures=[('zero',zero,zero),('P-only',denseP,zero),('N-only',zero,denseN),('dense',denseP,denseN),('global-phase',[phase*x for x in denseP],[phase*x for x in denseN]),('relative-phase',denseP,[phase*x for x in denseN])]
saved={}
for name,p,n in fixtures:saved[name]=packet(p,n);replay(saved[name],p,n)
assert saved['dense']['blocks']==saved['global-phase']['blocks'];assert saved['dense']['anchor']!=saved['global-phase']['anchor'];assert saved['dense']['blocks']!=saved['relative-phase']['blocks']
for ports in [Pports,Nports]:
    for a in ports:
        for b in ports:assert saved['dense']['blocks'][a['id']][b['id']]==saved['relative-phase']['blocks'][a['id']][b['id']]
# Source geometric actions, constructed from saved actual geometry, not fitted.
g=(1,2,0,3);rot=rotation(g);renameP=lambda e:''.join('ABCD'[g['ABCD'.index(a)]] for a in e);UP=[[R() for _ in range(36)] for _ in range(36)]
for j,label in enumerate(labels):
    e,a=label.split(':')
    for i in range(3):UP[labels.index(renameP(e)+':'+'xyz'[i])][j]=R(rot[i]['xyz'.index(a)])
rigidity=read(BASE/'field-rotation-rigidity/verification.json');nrow=next(r for r in rigidity['neutron']['isometries'] if r['orientation']==1 and r['order']==3);renameN=nrow['vertices']
triangles=list(map(tuple,read(NATIVE/'coupled_six_piece_belt_store.json')['record']['triangles']));order=read(NATIVE/'belt_three_by_twelve_store.json')['triangle_order'];positions={t:i for i,t in enumerate(order)};triIndex={t:i for i,t in enumerate(triangles)};UN=[[R() for _ in range(36)] for _ in range(36)];portMap={p['id']:'P:'+renameP(p['id'][2:]) for p in Pports}
for t,(f,a,b) in enumerate(triangles):
    new=('F_'+'_'.join(sorted(renameN[k] for k in f[2:].split('_'))),renameN[a],renameN[b]);nt=triIndex[new];i,j=positions[nt],positions[t];portMap[Nports[j]['id']]=Nports[i]['id']
    for axis in range(2):UN[2*i+axis][2*j+axis]=R(1)
assert mm(mm(UP,UP),UP)==identity(36);assert mm(mm(UN,UN),UN)==identity(36);assert gram(UN,metric)==[[R(metric[i] if i==j else 0) for j in range(36)] for i in range(36)]
rotated=packet(mv(UP,denseP),mv(UN,denseN));replay(rotated,mv(UP,denseP),mv(UN,denseN))
for a,row in saved['dense']['blocks'].items():
    for b,block in row.items():assert rotated['blocks'][portMap[a]][portMap[b]]==block
print('Full recovery, phase controls and all900 rotation-covariance blocks pass',flush=True)
# Pull back the actual native contrast frame using the retained PN unitary.
contrastPath=BASE/'neutron-contrast-electron-transport/verification.json';contrast=read(contrastPath);pnPath=BASE/'global-PN-transport/verification.json';pn=read(pnPath);K=mat(contrast['contrastFrame']);PN=mat(pn['matrix']);Q=adj(mm(sharp(K,metric),PN))
assert gram(K,metric)==identity(2);assert gram(Q,[F(1)]*36)==identity(2)
GP=native(pd,'G');NN=native(nd,'N');assert mm(GP,Q)==Q;assert mm(UP,Q)==Q
rotatedK=mm(UN,K);D=minus(rotatedK,K);assert gram(D,metric)==[[R(3 if i==j else 0) for j in range(2)] for i in range(2)];assert mm(NN,D)==[[R(),R()] for _ in range(36)]
assert all(sum((D[i+12*s][j] for s in range(3)),R())==0 for i in range(12) for j in range(2))
assert mm(NN,K)==mm(NN,rotatedK)==[[R(),R()] for _ in range(36)]
assert all(sum((a[i+12*s][j] for s in range(3)),R())==0 for a in [K,rotatedK] for i in range(12) for j in range(2))
assert gram(rotatedK,metric)==identity(2)
# PN Q=K uses the saved PN unitarity identity. All subsequent target action,
# source fixedness, recovery, Gram and readout calculations are fresh.
assert pn['status']=='global-PN-metric-unitary-candidate-constructed';routePackets=[];recoveredD=[]
for j in range(2):
    p=column(Q,j);y=column(K,j);z=column(rotatedK,j);before=packet(p,y);after=packet(p,z);replay(before,p,y);replay(after,p,z);assert before['blocks']!=after['blocks']
    py,ny=fields(recover(before,descriptor));pz,nz=fields(recover(after,descriptor));assert py==pz==p;recoveredD.append([a-b for a,b in zip(nz,ny)])
    routePackets.append({'contrastInput':j,'convertAfterSourceRotation':before,'rotateAfterConversion':after})
recoveredMatrix=[[recoveredD[j][i] for j in range(2)] for i in range(36)];assert recoveredMatrix==D;assert gram(recoveredMatrix,metric)==[[R(3 if i==j else 0) for j in range(2)] for i in range(2)]
# Rejection tests modify exact data/typing, not interpretation after the result.
controls=[]
def rejects(name,mutate):
    x=deepcopy(saved['dense']);mutate(x)
    try:recover(x,descriptor)
    except (AssertionError,ValueError,KeyError,IndexError):controls.append(name)
    else:raise AssertionError('Hostile accepted: '+name)
rejects('missing-N-sector',lambda x:[x['blocks'].pop(p['id']) for p in Nports if p['sector']==2])
rejects('missing-cross-block',lambda x:x['blocks'][Nports[0]['id']].pop(Pports[0]['id']))
rejects('wrong-anchor-magnitude',lambda x:x['anchor'].update(value=(restore(x['anchor']['value'])*2).record()))
rejects('wrong-metric',lambda x:x['descriptor']['carriers'][1]['ports'][0]['metric'].__setitem__(0,'999'))
rejects('erased-N-chart-transition',lambda x:x['descriptor']['carriers'][1].pop('chartTransitions'))
rejects('truncated-2-by-3-cross-map',lambda x:x['blocks'][Nports[0]['id']][Pports[0]['id']][0].pop())
rejects('false-zero-stratum',lambda x:x.update(anchor=None))
rejects('forged-non-anchor-block',lambda x:x['blocks'][Nports[-1]['id']][Nports[-1]['id']][0].__setitem__(0,{}))
archive={'descriptor':descriptor,'dense':saved['dense'],'rotatedDense':rotated,'relativeContrastRoutes':routePackets};data=gzip.compress((json.dumps(archive,separators=(',',':'))+'\n').encode(),mtime=0);(OUT/'packets.json.gz').write_bytes(data)
assert all(digest(p)==h for p,h in inputHashes.items()),'Source input changed during experiment'
assert len(json.loads(gzip.decompress(data))['relativeContrastRoutes'])==2
files=[ROOT/'research/nima/anchored-PN-contact-v1.md',ROOT/'research/nima/scc-models/anchored-PN-contact.json',Path(__file__).resolve(),ROOT/'research/nima/anchored_contact_comparisons.py',ROOT/'research/nima/anchored-PN-contact-protocol-v1.md',ROOT/'research/nima/results/two-reader-field-sewing/fixture.json',BASE/'common-three-carrier-protocol/proton.json',BASE/'common-three-carrier-protocol/neutron.json',BASE/'tetrahedral-field-attachment/verification.json',BASE/'neutron-belt-field-attachment/verification.json',BASE/'neutron-reader-field-interface/verification.json',BASE/'field-rotation-rigidity/verification.json',BASE/'rotation-realization-square/verification.json',BASE/'field-comparison-preparation/verification.json',contrastPath,pnPath,NATIVE/'coupled_six_piece_belt_store.json',NATIVE/'belt_three_by_twelve_store.json',ROOT/'research/strominger/checkers/exact_multiradical.py']
report={'schema':'marici.nima.anchored-PN-contact.v1','status':'faithful-comparison-with-visible-rank-two-obstruction','portTypes':{'P':[12,3],'N':[18,2],'neutronSectors':3},'blocks':{'PP':144,'NN':324,'NP':216,'PN':216,'total':900},'fixtureRecoveries':len(fixtures)+1+4,'rotationCovarianceBlocks':900,'commonPhaseNeedsAnchor':True,'relativePhaseDetectedByCrossBlocks':True,'obstruction':{'rank':2,'recoveredGram':serialize(gram(recoveredMatrix,metric)),'neutronReturnZero':True,'threeSectorAverageZero':True,'sourceGeometricC3FixesBothInputs':True,'routePacketsDiffer':True},'reuse':'PN Q=K follows from saved metric unitarity. Q, its Gram/source-G membership and C3 fixedness, target rotation, discrepancy, full packet recovery and readout blindness freshly calculated. This is not a new proof of existence of a geometric PN intertwiner.','negativeControls':controls,'packetsPath':'research/nima/results/anchored-PN-contact/packets.json.gz','packetsSha256':hashlib.sha256(data).hexdigest(),'sourceHashes':{p.relative_to(ROOT).as_posix():digest(p) for p in files},'scope':'Typed recoverable internal-coordinate comparisons at a marked contact, not physical seam equality, tangent-field identification, independent input preparation or legacy T9 encoding.'}
(OUT/'verification.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:v for k,v in report.items() if k!='sourceHashes'}))
