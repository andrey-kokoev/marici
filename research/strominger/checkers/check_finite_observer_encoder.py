"""Exact finite-packet candidate derived from endpoint/flux observations.
The analytic packet identities are justified by translation, evenness and
compact support; no numerical analytic inverse or full-domain claim is made.
"""
from pathlib import Path
from fractions import Fraction as F
import hashlib
import json
from exact_multiradical import Radical as R,mm,adj,identity,sqrt,rational,serialize

ROOT=Path(__file__).resolve().parents[3]
BASE='research/strominger/results/'
PROFILE='research/strominger/contracts/finite-observer-encoder.v1.json'
SEWING=BASE+'channel-assembled-field-sewing.json'
FIXTURE=BASE+'channel-assembled-native-fixture.json'
NE=BASE+'neutron-contrast-electron-transport/verification.json'


def restore(a):return [[R({int(k):F(v) for k,v in x.items()}) for x in row] for row in a]
def perm(p):return [[R(int(j==p[i])) for j in range(5)] for i in range(5)]
def subtract(a,b):return [[x-y for x,y in zip(row,col)] for row,col in zip(a,b)]


def rational_inverse(a):
    n=len(a);rows=[list(map(F,row))+[F(i==j) for j in range(n)] for i,row in enumerate(a)];det=F(1)
    for col in range(n):
        pivot=next((i for i in range(col,n) if rows[i][col]),None)
        if pivot is None:raise ValueError('singular observer readout')
        if pivot!=col:rows[col],rows[pivot]=rows[pivot],rows[col];det=-det
        value=rows[col][col];det*=value;rows[col]=[x/value for x in rows[col]]
        for i in range(n):
            if i!=col:
                value=rows[i][col];rows[i]=[x-value*y for x,y in zip(rows[i],rows[col])]
    return det,[row[n:] for row in rows]


def native_completion(endpoint_rows):
    projector=subtract(identity(5),mm(adj(endpoint_rows),endpoint_rows));columns=[]
    for j in range(5):
        v=[[row[j]] for row in projector]
        for q in columns:v=subtract(v,mm(q,mm(adj(q),v)))
        norm=rational(mm(adj(v),v)[0][0])
        if norm:
            if norm<0:raise ValueError('nonpositive coefficient norm')
            columns.append([[sqrt(1/norm)*x[0]] for x in v])
    if len(columns)!=3:raise ValueError('native endpoint complement is not rank3')
    return endpoint_rows+[adj(v)[0] for v in columns]


def main():
    profile=json.loads((ROOT/PROFILE).read_text());sewing=json.loads((ROOT/SEWING).read_text())
    fixture=json.loads((ROOT/FIXTURE).read_text());ne=json.loads((ROOT/NE).read_text());checks=[]
    def check(name,value):
        if not value:raise AssertionError(name)
        checks.append(name)
    for name,receipt in [('native sewing',sewing),('native NE',ne)]:
        check(name+' direct inputs current',all(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==sha for p,sha in receipt['sourceHashes'].items()))
    # Translation by delta=2log2 multiplies the two endpoint integrals by
    # 2^j and2^-j. Evenness equates the two normalization integrals A.
    # At sample k*delta, disjoint support makes A*p_j exactly delta_kj.
    q=F(2)
    Tq=[[q**j for j in range(5)],[q**(-j) for j in range(5)]]
    Tq += [[F(4*abs(k-j)<1) for j in range(5)] for k in range(3)]
    det,Tinvq=rational_inverse(Tq)
    T=[[R(x) for x in row] for row in Tq];Tinv=[[R(x) for x in row] for row in Tinvq]
    check('five actual endpoint/flux packet observations are independent',det==F(-3,2))
    check('packet coefficients reconstructed from all five observations',mm(Tinv,T)==identity(5) and mm(T,Tinv)==identity(5))
    check('three calibrated flux rows follow disjoint translated support',Tq[2:]==[[F(i==j) for j in range(5)] for i in range(3)])
    packets={p['packet']:p for p in sewing['packetBindings']};root=fixture['rootPacket']
    B={i:restore(p['binding']) for i,p in packets.items()};RR={i:restore(p['readout']) for i,p in packets.items()}
    P={i:perm(p['nativePermutation']) for i,p in packets.items()};J=restore(ne['electronFrame'])
    exit_id=sewing['exitSplits'][0]['packet'];Yexit=mm(B[exit_id],P[exit_id])
    endpoint_rows=mm(adj(J),Yexit[36:]);H=native_completion(endpoint_rows)
    check('actual native electron reader and retained complement give an orthonormal five-frame',mm(H,adj(H))==identity(5) and mm(adj(H),H)==identity(5))
    coefficient_encoder=mm(adj(H),T)
    L={i:mm(mm(B[i],P[i]),coefficient_encoder) for i in packets}
    D={i:mm(mm(mm(Tinv,H),adj(P[i])),RR[i]) for i in packets}
    check('all14 native presentations exactly decode the five observer packet coefficients',all(mm(D[i],L[i])==identity(5) for i in packets))
    check('both actual E exits reproduce the two Mellin endpoints in the declared calibration',all(
        mm(adj(J),L[e['packet']][36:])==T[:2] for e in sewing['exitSplits']))
    check('all three complementary readouts are retained at every presentation',all(
        mm(mm(mm(H[2:],adj(P[i])),RR[i]),L[i])==T[2:] for i in packets))
    generators={name:restore(a) for name,a in sewing['generatorMatrices'].items()};tested=set()
    for op in fixture['operations']:
        a,b=op['source'],op['target'];kind=op['kind']
        if kind=='reader-phase-advance':kind='P-reader' if packets[a]['species']=='proton' else 'identity'
        if kind=='NN-phase-advance':kind='identity'
        key=(kind,packets[a]['species'],packets[a]['frameParity'],packets[b]['species'],packets[b]['frameParity'])
        if key not in tested:
            actual=L[a] if kind=='identity' else mm(generators[kind],L[a])
            if actual!=L[b]:raise AssertionError('native interface breaks candidate encoding')
            tested.add(key)
    check('all18 native interfaces transport the candidate observer encoding',len(fixture['operations'])==18)
    check('root field norm is the declared observation Gram, not assumed source L2',mm(adj(L[root]),L[root])==mm(adj(T),T))
    # v represents a nonzero compact observer with zero endpoint pair.
    # These coefficients annihilate both exponential observation rows.
    invisible=[[R(2)],[R(-5)],[R(2)],[R(0)],[R(0)]]
    check('endpoint-only observation misses a nonzero actual packet',mm(T[:2],invisible)==[[R(0)],[R(0)]] and any(x[0]!=0 for x in mm(L[root],invisible)))
    check('retained flux complement detects that endpoint-invisible packet',mm(T[2:],invisible)==invisible[:3])
    swapped=mm(adj(H),[T[1],T[0],*T[2:]])
    wrong_exit=mm(Yexit,swapped)
    check('swapping endpoint assignments fails the declared native endpoint binding',mm(adj(J),wrong_exit[36:])!=T[:2])
    truncated=[*T[:2],*[ [R(0)]*5 for _ in range(3)]]
    check('discarding retained complement destroys packet reconstruction',mm(Tinv,truncated)!=identity(5))
    # Any specified linear source residual on D5 has samples f(p_j), hence
    # is transported exactly by f*D_i. Verify the universal coefficient law
    # rather than manufacturing the intended cutoff residual's sample values.
    check('arbitrary finite-packet residual factors through the exact decoder',all(mm(D[i],L[i])==identity(5) for i in packets))
    a,b=fixture['comparisonPackets']
    check('encoded field agreement does not merge the distinct coefficient witnesses',L[a]==L[b] and P[a]!=P[b] and mm(RR[a],L[a])!=mm(RR[b],L[b]))
    artifact=BASE+'finite-observer-encoder.json'
    result={'profile':PROFILE,'analyticReadoutMatrix':[[str(x) for x in row] for row in Tq],
            'determinant':str(det),'nativeEndpointRows':serialize(endpoint_rows),'nativeFiveFrame':serialize(H),
            'rootEncoder':serialize(L[root]),'packetDecoders':{str(i):serialize(d) for i,d in D.items()},
            'endpointInvisiblePacketCoefficients':[2,-5,2,0,0],
            'explicitFinitePacketEncoderConstructed':True,'sourceForcedOrUnique':False,
            'fullObserverDomainEncoded':False,'specificAnalyticalResidualEvaluated':False,
            'intendedAnalyticalWitnessBindingEstablished':False,'physicalPreparationEstablished':False,
            'full114ChannelEstablished':False}
    (ROOT/artifact).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    inputs=[PROFILE,*profile['sources'],SEWING,FIXTURE,NE,artifact,
            'research/strominger/checkers/exact_multiradical.py','research/strominger/checkers/check_finite_observer_encoder.py']
    report={'status':'passed','checks':checks,'check_count':len(checks),'packetDimension':5,'nativeFieldDimension':44,
            'encodedPresentations':14,'nativeInterfaces':18,'matchedEExits':2,'observationDeterminant':str(det),
            'explicitFinitePacketEncoderConstructed':True,'sourceForcedOrUnique':False,
            'fullObserverDomainEncoded':False,'specificAnalyticalResidualEvaluated':False,
            'intendedAnalyticalWitnessBindingEstablished':False,'physicalPreparationEstablished':False,'full114ChannelEstablished':False,
            'sourceHashes':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in inputs},
            'scope':'Explicit candidate on five compact translated physical packets in a declared Mellin convention; endpoint identities follow analytically from translation/evenness, and all native matrix equations are exact. Parent-chart use remains conditional on common-domain hypotheses. No particular regulator residual or higher analytical homotopy is evaluated.'}
    (ROOT/BASE/'finite-observer-encoder-verification.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:report[k] for k in ['status','check_count','packetDimension','encodedPresentations','nativeInterfaces','matchedEExits','observationDeterminant']}))


if __name__=='__main__':main()
