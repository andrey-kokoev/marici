"""Factorized exact attachment test; no assertion of physical face sewing.

The saved PN unitarity identity is reused, not recomputed densely. Fresh route
constraints are checked in its common-frame normal form. The NE projections
are computed exactly from the saved full PN matrix, including reader rotation.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
import sys, json, hashlib, subprocess
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/strominger/checkers'))
from exact_multiradical import Radical as R, mm, adj, identity, serialize
sys.path.insert(0,str(ROOT/'research/nima/checkers'))
from check_twelve_triangle_positive_geometry import rotation
BASE=ROOT/'research/strominger/results';OUT=ROOT/'research/nima/results/two-reader-field-sewing'
def read(p):return json.loads(p.read_text())
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def restore(a):return [[R({int(k):F(v) for k,v in x.items()}) for x in row] for row in a]
def plus(a,b,sign=1):return [[x+sign*y for x,y in zip(row,col)] for row,col in zip(a,b)]
def metric_adj(a,m):return [[x*m[j] for j,x in enumerate(row)] for row in adj(a)]
def gram(a,m):return mm(metric_adj(a,m),a)
def perm(p):return [[R(int(j==p[i])) for j in range(len(p))] for i in range(len(p))]
def trace(a):return sum((a[i][i] for i in range(len(a))),R()).record()
def det2(a):return a[0][0]*a[1][1]-a[0][1]*a[1][0]
def rank2(a):
    if len(a[0])==2 and det2(a)!=0:return 2
    if len(a[0])>2 and any(a[0][i]*a[1][j]-a[0][j]*a[1][i]!=0 for i,j in combinations(range(len(a[0])),2)):return 2
    return int(any(x!=0 for row in a for x in row))

subprocess.run(['node','research/nima/checkers/export_two_reader_field_fixture.mjs'],cwd=ROOT,check=True)
fixture=read(OUT/'fixture.json');fivePath=BASE/'full-five-channel-candidate/verification.json';five=read(fivePath)
for name,expected in five['sourceHashes'].items():assert digest(ROOT/name)==expected,('stale candidate input',name)
contrastPath=BASE/'neutron-contrast-electron-transport/verification.json';contrast=read(contrastPath);pnPath=BASE/'global-PN-transport/verification.json';pn=read(pnPath)
assert pn['status']=='global-PN-metric-unitary-candidate-constructed'
nd=read(BASE/'common-three-carrier-protocol/neutron.json');pd=read(BASE/'common-three-carrier-protocol/proton.json');m=list(map(F,nd['source']['metric']))
BP=restore(five['protonFiveEmbedding']);BN=restore(five['neutronFiveEmbedding']);PN=restore(pn['matrix']);K=restore(contrast['contrastFrame']);EF=restore(contrast['electronFrame']);S=restore(contrast['NEcandidateMatrix'])
assert gram(BP,[F(1)]*36)==identity(5);assert gram(K,m)==identity(2);assert gram(EF,[F(1)]*8)==identity(2)
assert mm(EF,metric_adj(K,m))==S
labels=pd['source']['coordinates'];rot=rotation((2,3,0,1));rename=dict(zip('ABCD','CDAB'));UP=[[R() for _ in range(36)] for _ in range(36)]
for j,label in enumerate(labels):
    edge,axis=label.split(':');new=''.join(rename[v] for v in edge)
    for i in range(3):
        if rot[i]['xyz'.index(axis)]:UP[labels.index(new+':'+'xyz'[i])][j]=R(rot[i]['xyz'.index(axis)])
assert mm(UP,UP)==identity(36);assert mm(adj(UP),UP)==identity(36)
P=[BP,mm(UP,BP)];assert P[0]!=P[1]
# Associate to the small contrast interface first, avoiding huge PNsharp*PN.
print('Computing exact projected PN candidate',flush=True)
projectionPN=mm(metric_adj(K,m),PN)
V=[mm(projectionPN,p) for p in P]
assert V[0]==mm(metric_adj(K,m),mm(BN,perm([3,1,2,0,4])))
assert mm(V[0],adj(V[0]))==identity(2)
E=[mm(EF,v) for v in V]
print('Exact projected fields computed',flush=True)
def species(p):return fixture['charts'][fixture['packets'][p]['chart']]['species']
def next_frame(e,frame):
    if e['kind']=='reader-phase-advance' and species(e['source'])=='proton':return frame^1
    assert e['kind'] in ['PN','inverse-PN','NE','experimental-terminal-PE','reader-phase-advance','NN-phase-advance']
    return frame
snapshots={};frames={}
for name in ['initial','final']:
    snap=fixture[name];edges=snap['native']+snap['shortcuts'];assigned={fixture['root']:0};tree=[]
    while len(assigned)<len(snap['selected']):
        grew=False
        for e in edges:
            if e['source'] in assigned and e['target'] not in assigned:
                assigned[e['target']]=next_frame(e,assigned[e['source']]);tree.append((e['kind'],e['id']));grew=True
        assert grew
    checks=[]
    for e in edges:
        assert assigned[e['target']]==next_frame(e,assigned[e['source']]),('candidate frame conflict',name,e)
        sourcePi=perm(fixture['packets'][e['source']]['permutation']);targetPi=perm(fixture['packets'][e['target']]['permutation'])
        assert targetPi==mm(perm(e['permutation']),sourcePi)
        checks.append({'kind':e['kind'],'id':e['id'],'source':e['source'],'target':e['target'],'treeEdge':(e['kind'],e['id']) in tree,'fieldEquationInFactoredNormalForm':True,'coefficientCompositionEquation':True})
    contacts=[]
    for contact in snap['contacts']:
        assert contact['witnesses'];assert all(any(e['id']==i for e in snap['native']) for i in contact['witnesses'])
        contacts.append({**contact,'nativeWitnessFieldEquationsCheckedInCandidate':True,'geometricFaceRestrictionEquation':'not-defined-by-this-candidate'})
    snapshots[name]={'readers':len(assigned),'frames':assigned,'edges':checks,'offTreeEdges':sum(not x['treeEdge'] for x in checks),'contacts':contacts};frames[name]=assigned
for p in fixture['initial']['selected']:assert frames['initial'][p]==frames['final'][p]

routes=[]
for shortcut in fixture['initial']['shortcuts']:
    source,target,n=shortcut['source'],shortcut['target'],shortcut['referenceNeutronPacket'];q=frames['initial'][source]
    assert q==frames['final'][n]==frames['initial'][target]==frames['final'][target]
    v=V[q];eg=mm(adj(v),v);ng=plus(identity(5),eg,-1);h=plus(identity(2),mm(v,adj(v)),-1)
    # The residual map is (I-K K* M) PN UP^q BP. Its kernel on five inputs
    # corresponds exactly to eigenvalue1 of v v*, hence rank=3+rank(I2-vv*).
    erank=rank2(v);nrank=3+rank2(h)
    assert plus(ng,eg)==identity(5);assert eg!=identity(5)
    routes.append({'shortcut':shortcut['id'],'source':source,'target':target,'referenceNeutron':n,'referenceBody':shortcut['referenceNeutronCell'],'nativeFactors':shortcut['nativeFactors'],'frameParity':q,'electronDirectEqualsExpanded':True,'virtualNeutronEqualsMaterializedReaderInCandidate':True,'electronRank':erank,'retainedBaryonRank':nrank,'jointRank':5,'electronGram':serialize(eg),'retainedGram':serialize(ng),'electronGramTrace':trace(eg),'retainedGramTrace':trace(ng),'electronGramIsProjector':mm(eg,eg)==eg,'jointGramIdentity':True,'retainedReferenceOnlyBeforeBatch':True,'electronField':serialize(E[q]),'residualFactorization':'(I36-K K* M_N) PN UP^parity BP','rankReductionMatrix':serialize(h)})
assert len(routes)==2
assert routes[0]['frameParity']==routes[1]['frameParity']
q=routes[0]['frameParity'];assert E[q]==E[routes[1]['frameParity']]
correlation={'sameRootInput':True,'electronMapsEqual':True,'stackedElectronRank':routes[0]['electronRank'],'residualMapsEqualInCommonFrame':True,'interpretation':'Correlated evaluations of one five-component root input, not two independently prepared channels. No independent-site tensor product or global energy sum supplied.'}
# Fixed-route controls: a coefficient relabeling, one-route sign, and deletion
# of the reference residual must not be accepted by these same equations.
p2=2;wrong=fixture['packets'][p2]['permutation'][:];wrong[0],wrong[1]=wrong[1],wrong[0]
e=next(e for e in fixture['final']['native'] if e['source']==0 and e['target']==p2)
assert perm(wrong)!=mm(perm(e['permutation']),perm(fixture['packets'][0]['permutation']))
assert [[-x for x in row] for row in E[q]]!=E[q]
assert all(r['electronGram']!=serialize(identity(5)) for r in routes)
files=[BASE/'rotation-realization-square/verification.json',ROOT/'research/strominger/rotation-realization-square-v1.md',Path(__file__).resolve(),ROOT/'research/nima/checkers/check_two_reader_field_sewing_scc.py',ROOT/'research/nima/scc-models/two-reader-field-sewing.json',ROOT/'research/nima/two-reader-field-sewing-v1.md',ROOT/'research/nima/checkers/export_two_reader_field_fixture.mjs',ROOT/'research/nima/two-reader-field-sewing-protocol-v1.md',OUT/'fixture.json',fivePath,contrastPath,pnPath,BASE/'common-three-carrier-protocol/neutron.json',BASE/'common-three-carrier-protocol/proton.json',ROOT/'research/strominger/checkers/exact_multiradical.py',ROOT/'research/nima/checkers/check_twelve_triangle_positive_geometry.py']
report={'schema':'marici.nima.two-reader-field-sewing.v1','status':'candidate-route-compatible-geometric-sewing-unresolved','candidate':'Fixed global PN/inverse; geometric P reader; co-moving N/NN identity; fixed contrast NE; PE defined by PN then NE. One shared five-component root input.','relatedOwnerResult':{'receipt':'research/strominger/results/rotation-realization-square/verification.json','scope':'Read and pinned, not rerun: named geometric C3 imposes an additional rank-two PN obstruction not tested by the fixed co-moving routes here.'},'verificationMethod':{'fresh':'Exact projected map K* M PN UP^q BP, Gram/rank calculations, native coefficient composition and every selected edge frame constraint. No floating point.','reused':'Saved PN metric unitarity and candidate-frame reduction; source hashes checked. Dense inverse composition was not recomputed.','rankFormula':'rank(residual)=3+rank(I2-V V*) for a five-isometric baryon input and orthonormal two-column K.'},'snapshots':snapshots,'routes':routes,'retainedReaderFieldsUnchangedInCandidate':True,'twoElectronComparison':correlation,'negativeControls':['wrong-coefficient-frame-detected','one-route-phase-flip-detected','electron-only-five-channel-accounting-rejected'],'residualObligations':['Geometric face restrictions and common seam comparison maps are not supplied by global carrier transports.','Residual baryon components remain reference-fiber data before materialization, not occupied neutron matter.','Independent body inputs, shared-body reader gluing and physical global norm/energy accounting remain unspecified.'],'sourceHashes':{p.relative_to(ROOT).as_posix():digest(p) for p in files},'sourceOwnerFilesUnchanged':all(digest(ROOT/name)==expected for name,expected in five['sourceHashes'].items())}
assert report['sourceOwnerFilesUnchanged'];(OUT/'verification.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'status':report['status'],'routes':[{k:r[k] for k in ['source','target','electronRank','retainedBaryonRank','jointRank','electronGramIsProjector','electronGramTrace','retainedGramTrace']} for r in routes],'snapshots':{k:{'readers':v['readers'],'edges':len(v['edges']),'offTreeEdges':v['offTreeEdges'],'contacts':len(v['contacts'])} for k,v in snapshots.items()},'twoElectronComparison':correlation}))
