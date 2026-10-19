"""Complete anchored C3 orbit is faithful; two averaging operations are not."""
from pathlib import Path
from fractions import Fraction as F
from copy import deepcopy
import contextlib,io,json,hashlib
with contextlib.redirect_stdout(io.StringIO()):
    import check_task_first_PN_conversion as t
    import check_anchored_sector_interface as a
R=t.R;Up,Un=t.r.Pthird[0],t.r.Nthird[0]
act=lambda p,n:(t.apply(Up,p),t.apply(Un,n))
token=lambda value:json.dumps(value,sort_keys=True,separators=(',',':'))
def field_token(pair):return token([[x.record() for x in v] for v in pair])
def encode(p,n):
    packets={}
    for _ in range(3):
        pkt=a.prepare(a.descriptor,a.to_ports(p,n));packets[token(pkt)]=pkt
        p,n=act(p,n)
    return [packets[k] for k in sorted(packets)]
def decode(orbit):
    assert len(orbit) in [1,3]
    assert len({token(p) for p in orbit})==len(orbit)
    recovered=[a.from_ports(a.recover(p,a.descriptor)) for p in orbit]
    expected=encode(*recovered[0])
    assert {token(p) for p in orbit}=={token(p) for p in expected},'incomplete or mixed orbit'
    return recovered
zero=[R()]*36
NP=t.r.Pop['N'];j=next(j for j in range(36) if (j,j) in NP)
p=[t.decode(NP.get((i,j),t.r.ZERO).record()) for i in range(36)]
norm=t.norm(p,t.pmetric);p=[x*t.sqrt(1/t.rational(norm)) for x in p]
n=t.convert(t.x);phase=t.sqrt(-1);nphase=[phase*x for x in n]
assert t.norm(p,t.pmetric)==t.norm(n,t.nmetric)==R(1) and t.apply(Up,p)==p
assert phase*phase*phase!=R(1)
assert all(t.apply(t.square.product(Un,Un) if g==2 else Un if g==1 else t.square.I,n)!=nphase for g in range(3))
fixtures=[('zero',zero,zero),('dense',a.denseP,a.denseN),('contrast',p,n),('relativePhase',p,nphase),('commonPhase',[phase*x for x in p],nphase)]
rows=[];orbits={}
for name,x,y in fixtures:
    orbit=encode(x,y);recovered=decode(orbit)
    expected=[];xx,yy=x,y
    for _ in range(3):expected.append(field_token((xx,yy)));xx,yy=act(xx,yy)
    assert {field_token(pair) for pair in recovered}==set(expected)
    assert encode(*act(x,y))==orbit
    assert {field_token(pair) for pair in decode(list(reversed(orbit)))}==set(expected)
    orbits[name]=orbit
    rows.append({'fixture':name,'orbitSize':len(orbit),'recoverUpToExactOrbit':True,'contextShiftInvariant':True})
assert len(orbits['zero'])==1 and len(orbits['contrast'])==3
assert orbits['contrast']!=orbits['relativePhase']!=orbits['commonPhase']
def mean_fields(x,y):
    xs=[];ys=[]
    for _ in range(3):xs.append(x);ys.append(y);x,y=act(x,y)
    return tuple([sum((v[i] for v in vs),R())*F(1,3) for i in range(36)] for vs in [xs,ys])
def mean_blocks(orbit):
    # Counterexample orbit has three elements; all have the same fixed P anchor.
    assert len(orbit)==3
    out=deepcopy(orbit[0]['blocks'])
    for target,row in out.items():
        for source,matrix in row.items():
            for i,line in enumerate(matrix):
                for j in range(len(line)):
                    line[j]=(sum((a.restore(pkt['blocks'][target][source][i][j]) for pkt in orbit),R())*F(1,3)).record()
    return out
assert mean_fields(p,n)==mean_fields(p,nphase)==(p,zero)
blocks=mean_blocks(orbits['contrast']);assert blocks==mean_blocks(orbits['relativePhase'])
anchors=[pkt['anchor'] for key in ['contrast','relativePhase'] for pkt in orbits[key]]
assert all(anchor==anchors[0] for anchor in anchors)
controls=[]
def rejected(name,fn):
    try:fn()
    except (AssertionError,ValueError,KeyError,IndexError,TypeError):controls.append(name)
    else:raise AssertionError('accepted hostile: '+name)
rejected('missing-orbit-member',lambda:decode(orbits['contrast'][:1]))
foreign=deepcopy(orbits['contrast']);foreign[0]=orbits['relativePhase'][0]
rejected('mixed-distinct-orbits',lambda:decode(foreign))
duplicate=deepcopy(orbits['contrast']);duplicate[1]=duplicate[0]
rejected('duplicated-orbit-member',lambda:decode(duplicate))
missing=deepcopy(orbits['contrast']);missing[0]['anchor']=None
rejected('missing-phase-anchor',lambda:decode(missing))
mean_packet=deepcopy(orbits['contrast'][0]);mean_packet['blocks']=blocks
rejected('quadratic-average-is-not-coherent-packet',lambda:a.recover(mean_packet,a.descriptor))
assert len(controls)==5
# Exact noncoherence witness: zero averaged P/N cross block and positive N
# self comparison are incompatible with recovery from the retained P anchor.
assert all(not entry for port in a.Nports for row in blocks[port['id']][anchors[0]['port']] for entry in row)
assert any(entry for port in a.Nports for row in blocks[port['id']][port['id']] for entry in row)
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/strominger/results'
result={'status':'pass','classification':'anchored-context-orbit-faithful-averages-merge-distinct-orbits',
        'domain':'all mathematical P/N field pairs admitted by the fixed descriptor; no equation n=S p and no physical independent-preparation claim',
        'equivalence':'simultaneous source geometric C3 action (p,n)->(U_P p,U_N n); no added phase quotient',
        'encoding':'unordered complete set of full anchored packets','recovery':'unordered field orbit, not a canonical field representative',
        'universalArgument':'Injective source prepare/recover and a genuine finite group action imply equality of complete packet orbits iff equality of field orbits; validator checks exact orbit closure.',
        'fixtures':rows,'differentPhaseOrbitsPreserved':True,
        'counterexample':{'inputs':'(p,n) and(p,i n), p unit return, n unit target relative field','sameMeanFields':True,'sameMeanComparisonBlocks':True,'sameRetainedPAnchor':True,'differentFullOrbits':True,'notContextEquivalent':'U_N^g n=i n would imply n=i^3 n after cubing, impossible for nonzero n.'},
        'averagedBlocksAcceptedAsCoherentPacket':False,'negativeControls':controls,
        'canonicalContextSelected':False,'physicalMixtureInterpretationEstablished':False,'PNFixedMapObstructionRepaired':False,'monsterGateActivated':False,
        'scope':'Exact quotient of declared comparison data, not physical phase equivalence, sewing or a canonical section. The full original task has not been weakened without naming the new quotient contract.',
        'nextObligation':'Specify task readouts on the orbit representation, retaining only the declared equivalence; if averaged second moments are needed, give them a separate positive-operator type rather than a coherent-packet inverse.'}
sources=[Path(__file__),Path(t.__file__),Path(a.__file__),ROOT/'research/strominger/context-orbit-readout-v1.md',BASE/'anchored-sector-interface/verification.json',BASE/'task-first-PN-conversion/verification.json']
result['sourceHashes']={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}
out=BASE/'context-orbit-readout';out.mkdir(exist_ok=True)
(out/'verification.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:result[k] for k in ['status','classification','fixtures','counterexample','averagedBlocksAcceptedAsCoherentPacket','negativeControls']}))
