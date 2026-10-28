"""Frozen finite-packet representation of the retained external C0 coefficient."""
import hashlib,json
from pathlib import Path
from fractions import Fraction as F
from exact_multiradical import Radical as R,mm,adj,identity,serialize
from check_finite_observer_encoder import restore,perm,rational_inverse
ROOT=Path(__file__).resolve().parents[3]
BASE='research/strominger/'
CONTRACT=BASE+'contracts/external-c0-finite-trace-attempt.v1.json'
SNAPSHOT=BASE+'contracts/persistent-seam-pe-conjecture-net.snapshot.rev36.json'
OUT=BASE+'results/external-c0-finite-trace/'
def load(p):return json.loads((ROOT/p).read_text())
def main():
    spec=load(CONTRACT);pre=load(SNAPSHOT);sewing=load(spec['sourceSewing']);encoder=load(spec['sourceEncoder'])
    relative_path=BASE+'results/screw-esd7-relative-attachment/attachment.json'
    relative=load(relative_path)
    receipt_paths=[spec['sourceAttachment'],spec['sourceSewing'],BASE+'results/finite-observer-encoder-verification.json']
    inputs={CONTRACT,SNAPSHOT,spec['sourceEncoder'],relative_path,spec['sourceTrace'],BASE+'checkers/check_external_c0_finite_trace.py',BASE+'checkers/check_finite_observer_encoder.py',BASE+'checkers/exact_multiradical.py',BASE+'external-c0-finite-trace-result-v1.md'}
    checks=[];failures=[]
    (ROOT/OUT).mkdir(parents=True,exist_ok=True)
    def check(name,value):
        if not value:
            failures.append({'equation':name})
            (ROOT/OUT/'failure.json').write_text(json.dumps({'status':'failed','contract':CONTRACT,'failures':failures},indent=2)+'\n')
            raise AssertionError(name)
        checks.append(name)
    for p in receipt_paths:
        receipt=load(p);inputs.add(p)
        check('live receipt closure: '+p,all(hashlib.sha256((ROOT/q).read_bytes()).hexdigest()==sha for q,sha in receipt['sourceHashes'].items()))
        inputs.update(receipt['sourceHashes'])
    node=next(n for n in pre['conjectures'] if n['id']=='external-c0-finite-trace-attempt')
    check('finite trace test registered before execution',node['status']=='open' and node['registration_before_execution'])
    native={p['id']:p for p in relative['packets']};charts={c['nativeChart']:c for c in relative['chartBindings']}
    s,t=spec['nativeInterface']['source'],spec['nativeInterface']['target']
    op=next(o for o in relative['operations'] if o['id']==spec['nativeInterface']['operation'])
    check('actual NE interface and external C0 owners match the relative attachment',op['source']==s and op['target']==t and op['kind']=='NE' and op['permutation'][0]==0 and all(charts[native[i]['chart']]['aliases']['C0']=='-3,1,3,0' for i in [s,t]))
    Tq=[[F(x) for x in row] for row in encoder['analyticReadoutMatrix']]
    det,Tiq=rational_inverse(Tq);T=[[R(x) for x in row] for row in Tq];Ti=[[R(x) for x in row] for row in Tiq]
    H=restore(encoder['nativeFiveFrame']);C=mm(adj(H),T)
    bindings={p['packet']:p for p in sewing['packetBindings']}
    B={i:restore(p['binding']) for i,p in bindings.items()};RR={i:restore(p['readout']) for i,p in bindings.items()};P={i:perm(p['nativePermutation']) for i,p in bindings.items()}
    L={i:mm(mm(B[i],P[i]),C) for i in bindings};D={i:mm(mm(mm(Ti,H),adj(P[i])),RR[i]) for i in bindings}
    check('frozen encoder is unchanged at the root',L[0]==restore(encoder['rootEncoder']) and det==F(-3,2))
    check('all66 native presentations exactly recover the original compact packet',set(bindings)==set(native) and len(bindings)==66 and all(mm(D[i],L[i])==identity(5) for i in bindings))
    generators={k:restore(v) for k,v in sewing['generatorMatrices'].items()};cache={}
    for edge in relative['operations']:
        a,b=edge['source'],edge['target'];kind=edge['kind']
        if kind=='reader-phase-advance':kind='P-reader' if bindings[a]['species']=='proton' else 'identity'
        if kind=='NN-phase-advance':kind='identity'
        key=(kind,json.dumps(serialize(L[a]),sort_keys=True))
        if key not in cache:cache[key]=L[a] if kind=='identity' else mm(generators[kind],L[a])
        check('frozen encoder transport on native interface '+str(edge['id']),cache[key]==L[b])
    rows={i:[mm(RR[i],L[i])[0]] for i in [s,t]}
    check('external C0 coefficient agrees exactly across NE5->15',rows[s]==rows[t] and any(x!=0 for x in rows[s][0]))
    observation_row=mm(rows[s],Ti)
    check('C0 is reconstructed from the existing endpoint and flux observations',mm(observation_row,T)==rows[s])
    matching_flux=[k for k in range(3) if rows[s]==[T[k+2]]]
    kernel=[[2,-5,2,0,0],[0,2,-5,2,0],[0,0,2,-5,2]]
    witnesses=[]
    for a in kernel:
        column=[[R(x)] for x in a];end=mm(T[:2],column);value=mm(rows[s],column)
        check('fixed endpoint-kernel control '+str(a),end==[[R(0)],[R(0)]])
        if value!=[[R(0)]]:witnesses.append({'packetCoefficients':a,'endpointPair':serialize(end),'externalC0':serialize(value)})
    check('deleting the C0 readout changes an actual finite packet observation',any(x!=0 for x in rows[s][0]))
    ne_path=BASE+'results/neutron-contrast-electron-transport/verification.json';ne=load(ne_path);inputs.add(ne_path);J=restore(ne['electronFrame'])
    check('all four actual E histories still match the declared Mellin endpoints',len(sewing['exitSplits'])==4 and all(mm(adj(J),L[e['packet']][36:])==T[:2] for e in sewing['exitSplits']))
    artifact={'contract':CONTRACT,'nativeInterface':spec['nativeInterface'],'domain':spec['domain'],
        'C0PacketRows':{str(i):serialize(row) for i,row in rows.items()},'C0ObservationRow':serialize(observation_row),
        'matchingCalibratedFluxIndices':matching_flux,'endpointOnlySufficient':not bool(witnesses),'endpointInvisibleWitnesses':witnesses,
        'finiteC0TraceBindingEstablished':True,'encoderRefitted':False,'spatialCoordinateIdentifiedWithAnalyticalCoordinate':False,
        'analyticalDomainExtensionEstablished':False,'actualF006BindingEstablished':False,'fullPbConstructionEstablished':False,
        'interpretation':'A native coefficient functional on the already admitted compact five-packet domain. A matching flux index k means C0=A*2^k*B_f(4^k), not that the spatial reference vertex is the analytical point4^k.',
        'scope':spec['scope']}
    artifact_path=OUT+'trace.json';(ROOT/artifact_path).write_text(json.dumps(artifact,indent=2)+'\n');inputs.add(artifact_path)
    report={'status':'passed','check_count':len(checks),'checks':checks,'encodedPresentations':len(bindings),'nativeInterfaces':len(relative['operations']),
        'finiteC0TraceBindingEstablished':True,'matchingCalibratedFluxIndices':matching_flux,'endpointOnlySufficient':not bool(witnesses),
        'endpointInvisibleWitnessCount':len(witnesses),'encoderRefitted':False,'analyticalDomainExtensionEstablished':False,'actualF006BindingEstablished':False,'fullPbConstructionEstablished':False,
        'sourceHashes':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in sorted(inputs)}}
    (ROOT/OUT/'verification.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k not in ['checks','sourceHashes']}))
if __name__=='__main__':main()
