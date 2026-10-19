"""Actual anchored packet API versus lossless continuous sector coordinates."""
from pathlib import Path
from fractions import Fraction as F
from copy import deepcopy
import sys,json,gzip,hashlib
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/nima'))
from anchored_contact_comparisons import prepare,recover,restore,R
from exact_multiradical import decode_A,sqrt,serialize
from assemble_metric_coefficient_protocol import A,ONE,ZERO,read_operator,plus,scaled
BASE=ROOT/'research/strominger/results';OWNER=ROOT/'research/nima/results/anchored-PN-contact'
owner=json.loads((OWNER/'verification.json').read_text(encoding='utf8'))
assert owner['status']=='faithful-comparison-with-visible-rank-two-obstruction'
for path,digest in owner['sourceHashes'].items():assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==digest,'stale owner input: '+path
raw=(ROOT/owner['packetsPath']).read_bytes();assert hashlib.sha256(raw).hexdigest()==owner['packetsSha256']
archive=json.loads(gzip.decompress(raw));descriptor=archive['descriptor']
assert descriptor['sewingEqualityImposed'] is False
sources={name:json.loads((BASE/f'common-three-carrier-protocol/{name}.json').read_text()) for name in ['proton','neutron']}
operators={name:{k:read_operator(src['operators'][k],36) for k in ['L','G','N']} for name,src in sources.items()}
metric={name:list(map(F,src['source']['metric'])) for name,src in sources.items()}
I={(i,i):ONE for i in range(36)};sectors={}
for name,ops in operators.items():
    L,G,N=(ops[k] for k in ['L','G','N'])
    sectors[name]=[N,plus(L,scaled(A(-1),N)),plus(G,scaled(A(-1),N)),plus(I,scaled(A(-1),L),scaled(A(-1),G),N)]
    assert plus(*sectors[name])==I
# Convert once; subsequent vector operations stay in the actual packet scalar type.
rad=lambda op:{key:decode_A(value.record()) for key,value in op.items()}
sectors={name:list(map(rad,blocks)) for name,blocks in sectors.items()}
def apply(op,v):
    out=[R() for _ in range(36)]
    for (i,j),a in op.items():out[i]+=a*v[j]
    return out
def extract(name,v):return [apply(E,v) for E in sectors[name]]
def rebuild(name,blocks):
    assert len(blocks)==4 and all(isinstance(v,list) and len(v)==36 for v in blocks)
    assert all(apply(E,v)==v for E,v in zip(sectors[name],blocks)), 'wrong sector range'
    return [sum((v[i] for v in blocks),R()) for i in range(36)]
def norm(name,v):return sum((x.conj()*x*m for x,m in zip(v,metric[name])),R())
def weights(name,blocks):return [norm(name,v) for v in blocks]
Pports,Nports=[carrier['ports'] for carrier in descriptor['carriers']]
assert len(Pports)==12 and len(Nports)==18
plabels=sources['proton']['source']['coordinates'];nlabels=sources['neutron']['source']['coordinates']
assert [label for port in Nports for label in port['nativeLabels']]==nlabels
frames={port['id']:[[R(F(x)) for x in row] for row in port['sourcePatch']['rotation']] for port in Pports}
def mv(matrix,v):return [sum((a*b for a,b in zip(row,v)),R()) for row in matrix]
def to_ports(p,n):
    out={}
    for port in Pports:
        matrix=frames[port['id']];transpose=list(map(list,zip(*matrix)))
        out[port['id']]=mv(transpose,[p[plabels.index(label)] for label in port['nativeLabels']])
    for i,port in enumerate(Nports):out[port['id']]=n[2*i:2*i+2]
    return out
def from_ports(values):
    p=[R() for _ in range(36)];n=[]
    for port in Pports:
        vector=mv(frames[port['id']],values[port['id']])
        for label,x in zip(port['nativeLabels'],vector):p[plabels.index(label)]=x
    for port in Nports:n.extend(values[port['id']])
    return p,n
fixtures=[('dense',archive['dense']),('rotatedDense',archive['rotatedDense'])]
for j,route in enumerate(archive['relativeContrastRoutes']):
    for key in ['convertAfterSourceRotation','rotateAfterConversion']:fixtures.append((f'route{j}:{key}',route[key]))
denseP,denseN=from_ports(recover(archive['dense'],descriptor));zero=[R()]*36
phase=sqrt(-1)
fixtures.extend([('zero',prepare(descriptor,to_ports(zero,zero))),
                 ('commonPhase',prepare(descriptor,to_ports([phase*x for x in denseP],[phase*x for x in denseN]))),
                 ('relativePhase',prepare(descriptor,to_ports(denseP,[phase*x for x in denseN])))])
checked={}
for name,packet in fixtures:
    p,n=from_ports(recover(packet,descriptor))
    ps,ns=extract('proton',p),extract('neutron',n)
    rp,rn=rebuild('proton',ps),rebuild('neutron',ns)
    assert (rp,rn)==(p,n)
    direct=prepare(descriptor,to_ports(p,n))
    via_sectors=prepare(descriptor,to_ports(rp,rn))
    assert direct==via_sectors==packet
    recovered=from_ports(recover(via_sectors,descriptor))
    assert extract('proton',recovered[0])==ps and extract('neutron',recovered[1])==ns
    checked[name]=(p,n,ps,ns)
assert len(checked)==9
phase_packet=dict(fixtures)['commonPhase']
assert phase_packet['blocks']==archive['dense']['blocks'] and phase_packet['anchor']!=archive['dense']['anchor']
assert dict(fixtures)['relativePhase']['blocks']!=archive['dense']['blocks']
residuals=[];NN=rad(operators['neutron']['N'])
for j in range(2):
    before=checked[f'route{j}:convertAfterSourceRotation'];after=checked[f'route{j}:rotateAfterConversion']
    assert before[0]==after[0] and before[1]!=after[1]
    assert weights('neutron',before[3])==weights('neutron',after[3])
    assert before[3]!=after[3]
    e=[a-b for a,b in zip(after[1],before[1])]
    assert apply(NN,e)==zero
    residuals.append(e)
gram=[[sum((a.conj()*b*m for a,b,m in zip(x,y,metric['neutron'])),R()) for y in residuals] for x in residuals]
assert gram==[[R(3),R()],[R(),R(3)]]
controls=[]
def rejected(name,call):
    try:call()
    except (AssertionError,ValueError,KeyError,IndexError,TypeError):controls.append(name)
    else:raise AssertionError('hostile accepted: '+name)
blocks=deepcopy(checked['dense'][2]);assert any(blocks[2]);blocks[0]=blocks[2]
rejected('wrong-sector-vector',lambda:rebuild('proton',blocks))
rejected('weights-instead-of-vectors',lambda:rebuild('proton',weights('proton',checked['dense'][2])))
bad_anchor=deepcopy(archive['dense']);bad_anchor['anchor']=None
rejected('erased-common-phase-anchor',lambda:recover(bad_anchor,descriptor))
bad_cross=deepcopy(archive['dense']);bad_cross['blocks'][Nports[0]['id']].pop(Pports[0]['id'])
rejected('missing-rectangular-cross-block',lambda:recover(bad_cross,descriptor))
assert len(controls)==4
result={'status':'pass','classification':'anchored-PN-packet-and-continuous-sector-presentation-compatible',
        'ownerReceiptStatus':owner['status'],'ownerSourceHashesChecked':len(owner['sourceHashes']),
        'comparisonFixtures':list(checked),'completeBlocksPerFixture':900,
        'preparationSquareEqual':True,'recoverySquareEqual':True,
        'universalReconstructionBasis':'sum E_i=I plus sector range constraints and the actual exact anchored prepare/recover formula; finite fixtures are regression checks, not the universal proof.',
        'routeResidualGram':serialize(gram),'nativeReturnErasesResidual':True,'sectorWeightsBlindToRouteDifference':True,
        'fullSectorVectorsDistinguishRoutes':True,'anchorRetainsCommonPhase':True,'crossBlocksRetainRelativePhase':True,
        'negativeControls':controls,'PNGeometricSquareCommutes':False,'physicalSewingEstablished':False,
        'T9BindingEstablished':False,'monsterGateActivated':False,
        'scope':'Lossless coordinate/attachment-data comparison under the fixed descriptor and anchors. Does not identify P/N fibers or authorize motion, geometric seam equality or independent physical preparations.',
        'nextObligation':'Specify whether a proposed seam preserves strict geometric C3 or retains a typed relative defect; do not confuse recoverability with equality.'}
sources=[Path(__file__),ROOT/'research/strominger/anchored-sector-interface-v1.md',ROOT/'research/nima/anchored_contact_comparisons.py',OWNER/'verification.json',ROOT/owner['packetsPath'],BASE/'common-three-carrier-protocol/proton.json',BASE/'common-three-carrier-protocol/neutron.json',BASE/'decorated-sector-carrier/verification.json']
result['sourceHashes']={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}
assert all(hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==digest for path,digest in owner['sourceHashes'].items()),'owner input drift during comparison'
out=BASE/'anchored-sector-interface';out.mkdir(exist_ok=True)
(out/'verification.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:result[k] for k in ['status','classification','comparisonFixtures','preparationSquareEqual','recoverySquareEqual','routeResidualGram','negativeControls','PNGeometricSquareCommutes']}))
