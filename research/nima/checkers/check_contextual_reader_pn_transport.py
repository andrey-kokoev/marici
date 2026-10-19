"""Actual four-reader contexts, coefficient images, NN maps and PN diagnostic."""
from pathlib import Path
from fractions import Fraction as F
from copy import deepcopy
import sys,json,gzip,hashlib,itertools
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/'research/nima'))
from anchored_contact_comparisons import R,restore,recover,prepare
from reader_chart_transport import encode,decode,transition,mix,validate
from exact_multiradical import decode_A,serialize
OUT=ROOT/'research/nima/results/contextual-reader-PN-transport';OUT.mkdir(exist_ok=True)
inputs={}
def load(path,gz=False):
    raw=path.read_bytes();inputs[path]=hashlib.sha256(raw).hexdigest()
    return json.loads(gzip.decompress(raw) if gz else raw)
base=ROOT/'research/strominger/results'
chart=load(base/'eight-sector-interface/verification.json');readers=load(base/'eight-sector-readers/verification.json');bindings=load(base/'five-coefficient-field-binding/verification.json')
for receipt in [chart,readers,bindings]:
    for name,h in receipt['sourceHashes'].items():
        p=ROOT/name;assert hashlib.sha256(p.read_bytes()).hexdigest()==h,('stale receipt',name);inputs[p]=h
contexts={k:readers[k] for k in ['rootReader','readers','operations','witnesses']}
rows=chart['nativeReaderRows'];native=chart['nativeAxis'];names=list(chart['unnormalizedCharts'])
T={(r['target'],r['source']):r['matrix'] for r in chart['transitions']}
nd=load(base/'common-three-carrier-protocol/neutron.json');metric=list(map(F,nd['source']['metric']))
def mv(matrix,v):return [sum((a*b for a,b in zip(row,v) if a!=0 and b!=0),R()) for row in matrix]
def adjM(matrix):return [list(row) for row in zip(*[[x.conj() for x in row] for row in matrix])]
def gram(columns):return [[sum((a.conj()*b*metric[k%36] for k,(a,b) in enumerate(zip(u,v))),R()) for v in columns] for u in columns]
def coeffnorm(v):return sum((x.conj()*x for x in v),R())
def fieldnorm(fields):return sum((x.conj()*x*metric[j] for field in fields for j,x in enumerate(field)),R())
def zero():return [R() for _ in range(36)]
def matmul(a,b):return [[sum((F(x)*F(y) for x,y in zip(row,col)),F()) for col in zip(*b)] for row in a]
# Geometric assignment is rederived from source FCC face sectors, not copied
# only from the slot list. Pair sector triangles whose vertices are in each
# actual selected reader's source component.
def fcc(v):return (v[1]+v[2],v[1]+v[3],v[2]+v[3])
signs=chart['sectorSigns'];pairs=chart['pairings'][native]
for reader,row in zip(contexts['readers'],rows):
    owner=reader['cell']['owner'];verts=[fcc(v) for v in owner['vertices']]
    center=tuple(sum(v[k] for v in verts)/F(len(verts)) for k in range(3))
    component={fcc(tuple(map(int,v.split(',')))) for v in reader['cell']['vertices']}
    incident=[]
    for s,sigma in enumerate(signs):
        face={tuple(center[k]+(sigma[axis] if k==axis else 0) for k in range(3)) for axis in range(3)}
        if face<=component:incident.append(s)
    assert set(incident)==set(pairs[row])
# Build both saved noncanonical seeds with exact source algebra decoding.
seeds=[]
for records in bindings['neutron']['constructedSeeds']:
    B=[[R() for _ in range(5)] for _ in range(36)]
    for r in records:B[r['field']][r['coefficient']]=decode_A(r['value'])
    seeds.append(B)
perm=bindings['nativePermutations']['neutron']
Pi=[[R(int(j==perm[i])) for j in range(5)] for i in range(5)]
embeddings=[]
for seed in seeds:
    bs=[]
    for rec in contexts['readers']:
        B=deepcopy(seed)
        for _ in range(rec['packet']['origin']):
            B=[[sum((row[k]*Pi[k][j] for k in range(5)),R()) for j in range(5)] for row in B]
        cols=[list(c) for c in zip(*B)];assert gram(cols)==[[R(int(i==j)) for j in range(5)] for i in range(5)]
        bs.append(B)
    for i in range(3):
        op=contexts['operations'][i+1]
        assert op['kind']=='NN-phase-advance' and op['permutation']==perm
        assert op['source']==contexts['readers'][i]['packet']['id'] and op['target']==contexts['readers'][i+1]['packet']['id']
        assert op['phaseDelta']==1 and contexts['readers'][i+1]['packet']['origin']==contexts['readers'][i]['packet']['origin']+1
        assert [[sum((row[k]*Pi[k][j] for k in range(5)),R()) for j in range(5)] for row in bs[i+1]]==bs[i]
    embeddings.append(bs)
counts={'coefficientBasisRecoveries':0,'coherentChainRecoveries':0,'NNChartSquares':0,'PNPacketRecoveries':0,'residualGrams':0,'chartCompositionTriangles':0}
fixtures=[]
for seedIndex,bs in enumerate(embeddings):
    # Twenty independent coefficient directions: independent records, not one
    # simultaneous reachable native state. Decode all five coefficients.
    for i,j in itertools.product(range(4),range(5)):
        coeffs=[[R(int(r==i and k==j)) for k in range(5)] for r in range(4)]
        fields=[mv(B,v) for B,v in zip(bs,coeffs)]
        for target in names:
            p=encode(fields,contexts,rows,native,target,T);decoded=decode(p,contexts,rows,native,T)
            assert decoded==fields
            for B,field,expected in zip(bs,decoded,coeffs):
                dual=[[x*metric[k] for k,x in enumerate(row)] for row in adjM(B)]
                assert mv(dual,field)==expected
            assert fieldnorm([[restore(x) for x in row] for row in p['values']])==sum((coeffnorm(v) for v in coeffs),R())
            counts['coefficientBasisRecoveries']+=1
    root=[R(i+1) for i in range(5)]
    coeffs=[[root[j] for j in rec['packet']['permutation']] for rec in contexts['readers']]
    for i in range(3):assert mv(Pi,coeffs[i])==coeffs[i+1]
    fields=[mv(B,v) for B,v in zip(bs,coeffs)]
    assert all(f==fields[0] for f in fields)
    for target in names:
        p=encode(fields,contexts,rows,native,target,T);assert decode(p,contexts,rows,native,T)==fields
        assert all(not restore(x).d for row in p['values'][4:] for x in row)
        counts['coherentChainRecoveries']+=1
    # Actual NN partial channels on the coefficient image, for every source
    # basis coefficient and every chart. Not whole-space unitary evolution.
    for i in range(3):
        support=[[F() for _ in range(8)] for _ in range(8)];support[rows[i+1]][rows[i]]=F(1)
        for target in names:
            transported=matmul(matmul(T[target,native],support),T[native,target])
            incoming=sorted({j%4 for row in transported for j,x in enumerate(row) if x})
            outgoing=sorted({j%4 for j,row in enumerate(transported) if any(row)})
            expected=next(r for r in chart['nativeNNUpdateSupport'] if r['sourceOrigin']==i and r['chart']==target)
            assert incoming==expected['inputPairs'] and outgoing==expected['outputPairs']
            for j in range(5):
                c=[R(int(k==j)) for k in range(5)]
                before=[zero() for _ in range(8)];before[rows[i]]=mv(bs[i],c)
                after=[zero() for _ in range(8)];after[rows[i+1]]=mv(bs[i+1],mv(Pi,c))
                assert mix(transported,mix(T[target,native],before))==mix(T[target,native],after)
                counts['NNChartSquares']+=1
    fixtures.append(p)
# PN obstruction remains a FULL-FIELD diagnostic. Check, rather than assume,
# whether its residual lies in the actual five-coefficient image.
archive=load(ROOT/'research/nima/results/anchored-PN-contact/packets.json.gz',True)
desc=archive['descriptor'];nports=[p for c in desc['carriers'] if c['id']=='N' for p in c['ports']]
routeFields=[];differences=[]
for route in archive['relativeContrastRoutes']:
    lv=recover(route['convertAfterSourceRotation'],desc);rv=recover(route['rotateAfterConversion'],desc)
    n=lambda v:[x for p in nports for x in v[p['id']]]
    routeFields.append((route,lv,rv,n(lv),n(rv)));differences.append([a-b for a,b in zip(n(rv),n(lv))])
assert gram(differences)==[[R(3),R()],[R(),R(3)]]
projection=[]
for s,bs in enumerate(embeddings):
    for i,B in enumerate(bs):
        dual=[[x*metric[k] for k,x in enumerate(row)] for row in adjM(B)]
        projected=[mv(B,mv(dual,d)) for d in differences]
        remainder=[[a-b for a,b in zip(d,p)] for d,p in zip(differences,projected)]
        assert any(x!=0 for col in remainder for x in col),'Unexpectedly complete coefficient image'
        gp=gram(projected);gr=gram(remainder)
        assert [[gp[a][b]+gr[a][b] for b in range(2)] for a in range(2)]==gram(differences)
        assert gp[0][0]*gp[1][1]-gp[0][1]*gp[1][0]==R(F(109350,89401))
        assert gr[0][0]*gr[1][1]-gr[0][1]*gr[1][0]==R(F(308484,89401))
        projection.append({'seed':s,'origin':i,'residualInCoefficientImage':False,'projectedRank':2,'discardedRank':2,'projectedGram':serialize(gp),'discardedGram':serialize(gr)})
for readerIndex in range(4):
    for target in names:
        columns=[]
        for route,lv,rv,left,right in routeFields:
            restored=[]
            for vector,oracle in [(left,lv),(right,rv)]:
                fields=[zero() for _ in range(4)];fields[readerIndex]=vector
                p=encode(fields,contexts,rows,native,target,T)
                out=decode(p,contexts,rows,native,T);assert out==fields
                # Rebuild the ORIGINAL PN oracle, not a newly claimed contact
                # between the old P and these different actual N contexts.
                vals=deepcopy(oracle)
                for k,port in enumerate(nports):vals[port['id']]=out[readerIndex][2*k:2*k+2]
                rebuilt=prepare(desc,vals)
                original=route['convertAfterSourceRotation'] if vector is left else route['rotateAfterConversion']
                assert rebuilt==original;counts['PNPacketRecoveries']+=1
                restored.append([[restore(x) for x in row] for row in p['values']])
            columns.append([a-b for rr,ll in zip(restored[1],restored[0]) for a,b in zip(rr,ll)])
        assert gram(columns)==[[R(3),R()],[R(),R(3)]];counts['residualGrams']+=1
# Composition on an independent dense full-field assignment, not just one slot.
fields=[[R((i+1)*(j+1)) for j in range(36)] for i in range(4)]
start=encode(fields,contexts,rows,native,native,T)
for a,b,c in itertools.product(names,repeat=3):
    pa=transition(start,a,contexts,rows,native,T)
    composite=transition(transition(pa,b,contexts,rows,native,T),c,contexts,rows,native,T)
    assert composite==transition(pa,c,contexts,rows,native,T);counts['chartCompositionTriangles']+=1
controls=[]
def reject(name,change):
    p=deepcopy(start);change(p)
    try:validate(p,contexts,rows,native,T)
    except (AssertionError,KeyError,ValueError,IndexError):controls.append(name)
    else:raise AssertionError('accepted '+name)
reject('origin-folding',lambda p:[r['packet'].update(origin=r['packet']['origin']%2) for r in p['contexts']['readers']])
reject('reader-row-swap',lambda p:p['readerRows'].__setitem__(slice(0,2),list(reversed(p['readerRows'][:2]))))
reject('new-native-detail-mode',lambda p:p['values'][4].__setitem__(0,{'1':'1'}))
reject('wrong-NN-factor',lambda p:p['contexts']['operations'][1].update(permutation=list(range(5))))
reject('missing-reader',lambda p:p['contexts']['readers'].pop())
# Averaging a target with nonzero detail fails to recover independent records.
bad=transition(start,'0',contexts,rows,native,T)
assert any(restore(x)!=0 for row in bad['values'][4:] for x in row)
bad['values'][4:]=[[{} for _ in range(36)] for _ in range(4)]
try:
    changed=decode(bad,contexts,rows,native,T)
except AssertionError:controls.append('drop-required-differences')
else:
    assert changed!=fields;controls.append('drop-required-differences-detected-by-oracle')
assert all(hashlib.sha256(p.read_bytes()).hexdigest()==h for p,h in inputs.items())
for p in [Path(__file__).resolve(),ROOT/'research/nima/reader_chart_transport.py',ROOT/'research/nima/contextual-reader-PN-transport-v1.md']:
    inputs[p]=hashlib.sha256(p.read_bytes()).hexdigest()
report={'schema':'marici.nima.contextual-reader-PN-transport.v1','status':'pass','counts':counts,'readerRows':rows,'origins':[r['packet']['origin'] for r in contexts['readers']],
        'projectionAudit':projection,'negativeControls':controls,
        'result':'Actual contexts, both coefficient bindings and three native NN partial maps transport faithfully. Full-field PN diagnostic retains Gram 3I2 in every slot/chart. Its residual is outside every tested five-coefficient binding image; coefficient-only promotion would lose data.',
        'scope':'Read-only source-context assignment. Independent fields are not one coherent native history; PN oracle recovery does not identify its original contact with these reader cells. No geometric PN lift, new native operation or physical preparation derived.',
        'sourceHashes':{p.relative_to(ROOT).as_posix():h for p,h in inputs.items()}}
(OUT/'verification.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'status':'pass','counts':counts,'coefficientImageGate':'residual outside all 8 tested images','negativeControls':controls}))
