"""Exact source Volterra/value-flux subproblem on the compact five-packet.
Weighted partial integrals on a packet's own seam cancel from its alternating
pairing; they are not approximated or silently declared zero.
"""
from pathlib import Path
from fractions import Fraction as F
import hashlib
import json
from exact_multiradical import Radical as R,mm,identity,serialize,sqrt,adj
from check_finite_observer_encoder import restore,perm,rational_inverse

ROOT=Path(__file__).resolve().parents[3]
BASE='research/strominger/results/'
PROFILE='research/strominger/contracts/finite-packet-green-trace.v1.json'
ENCODER=BASE+'finite-observer-encoder.json'
ENCODER_CHECK=BASE+'finite-observer-encoder-verification.json'
COMPARISON=BASE+'strict-native-comparison.json'
COMPARISON_CHECK=BASE+'strict-native-comparison-verification.json'
SEWING=BASE+'channel-assembled-field-sewing.json'


def transpose(a):return [list(row) for row in zip(*a)]
def add(a,b):return [[x+y for x,y in zip(row,col)] for row,col in zip(a,b)]
def scale(c,a):return [[c*x for x in row] for row in a]


def seam_matrix(k):
    """Build from the trace-law support cases, preserving partial-mass symbols.
    A J_sigma(p_j)=2^(sigma*k) delta_jk.
    M_sigma(p_j)=2^(sigma*j) for j<k, zero for j>k,
    and 2^(sigma*k)*theta_sigma for j=k. The latter cancels.
    """
    total=[[F(0) for _ in range(5)] for _ in range(5)]
    residual_symbol_coefficients=[]
    for sigma in [1,-1]:
        q=F(2)**sigma
        flux=[q**k if j==k else F(0) for j in range(5)]
        mass_constant=[q**j if j<k else F(0) for j in range(5)]
        mass_partial=[q**k if j==k else F(0) for j in range(5)]
        partial=[[mass_partial[i]*flux[j]-flux[i]*mass_partial[j] for j in range(5)] for i in range(5)]
        residual_symbol_coefficients.append(partial)
        for i in range(5):
            for j in range(5):total[i][j]+=mass_constant[i]*flux[j]-flux[i]*mass_constant[j]
    if any(x for a in residual_symbol_coefficients for row in a for x in row):
        raise AssertionError('uncomputed partial integral survives')
    return total


def main():
    profile=json.loads((ROOT/PROFILE).read_text());encoder=json.loads((ROOT/ENCODER).read_text())
    comparison=json.loads((ROOT/COMPARISON).read_text());sewing=json.loads((ROOT/SEWING).read_text());checks=[]
    def check(name,value):
        if not value:raise AssertionError(name)
        checks.append(name)
    for name,path in [('encoder',ENCODER_CHECK),('native comparison',COMPARISON_CHECK),('sewing',SEWING)]:
        data=json.loads((ROOT/path).read_text())
        check(name+' direct inputs current',all(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==sha for p,sha in data['sourceHashes'].items()))
    Wq=[seam_matrix(k) for k in range(5)]
    W=[[[R(x) for x in row] for row in a] for a in Wq]
    check('all125 seam entries evaluated with partial-mass symbols cancelled',len(W)==5 and all(len(a)==5 for a in W))
    check('all source seam forms retain their alternating orientation',all(transpose(a)==scale(-1,a) for a in W))
    check('first seam has no preceding packet with which to pair',W[0]==[[R(0)]*5 for _ in range(5)])
    check('actual source cross-entry at seam delta is5/2',W[1][0][1]==R(F(5,2)) and W[1][1][0]==R(F(-5,2)))
    Tq=[[F(x) for x in row] for row in encoder['analyticReadoutMatrix']];T=[[R(x) for x in row] for row in Tq]
    u=[[R(x)] for x in [2,-5,2,0,0]];v=[[R(x)] for x in [0,2,-5,2,0]]
    check('two distinct compact packets are invisible to both Mellin endpoints',mm(T[:2],u)==mm(T[:2],v)==[[R(0)],[R(0)]])
    value=mm(mm(transpose(v),W[1]),u)
    check('their actual calibrated seam comparison is nonzero minus10',value==[[R(-10)]])
    imaginary=sqrt(-1);iv=scale(imaginary,v)
    check('bilinear source law scales linearly in the second packet',mm(mm(transpose(iv),W[1]),u)==scale(imaginary,value))
    check('using adjoint instead of transpose would reverse that complex phase',mm(mm(adj(iv),W[1]),u)!=scale(imaginary,value))
    check('reversing value-flux orientation changes the detected value',mm(mm(transpose(v),scale(-1,W[1])),u)==[[R(10)]])
    # Two probe packet types and five readings across four fixed seam settings.
    # This is an observation protocol, not two arbitrary graph-node probes.
    observation=[Wq[1][1]]+[Wq[k][0] for k in range(1,5)]
    determinant,reconstruction=rational_inverse(observation)
    O=[[R(x) for x in row] for row in observation];Oinv=[[R(x) for x in row] for row in reconstruction]
    check('two fixed probe types with five declared seam readings reconstruct the packet',determinant!=0 and mm(Oinv,O)==identity(5))
    check('no faithful reconstruction claim is made for the two endpoint readings alone',len(T[:2])==2 and mm(T[:2],u)==[[R(0)],[R(0)]])
    H=restore(encoder['nativeFiveFrame']);_,Tiq=rational_inverse(Tq);Ti=[[R(x) for x in row] for row in Tiq]
    D={int(i):restore(a) for i,a in encoder['packetDecoders'].items()}
    packets={p['packet']:p for p in sewing['packetBindings']}
    L={i:mm(mm(restore(p['binding']),perm(p['nativePermutation'])),mm(adj(H),T)) for i,p in packets.items()}
    for i in packets:
        decoded=mm(D[i],L[i])
        for a in W:
            if mm(mm(transpose(decoded),a),decoded)!=a:raise AssertionError('native seam pullback mismatch')
    check('all70 native presentation/seam pairings pull back to the computed source matrices',len(packets)*len(W)==70)
    # Normalized D_i U_i must be one fixed5x44 source coefficient reader.
    normalized={i:mm(mm(mm(Ti,H),adj(perm(p['nativePermutation']))),restore(comparison['normalizedReadouts'][str(i)])) for i,p in packets.items()}
    common=next(iter(normalized.values()))
    check('native pairwise covariance holds on all44 inputs in factored form',all(a==common for a in normalized.values()))
    # PNE histories are still separate; these pairings do not collapse the ledger.
    check('both source primitive right endpoints are the declared Mellin weights',all(
        F(2)**(sigma*j)==Tq[0 if sigma==1 else 1][j] for sigma in [1,-1] for j in range(5)))
    artifact=BASE+'finite-packet-green-trace.json'
    result={'calibratedSeamMatrices':{str(k):serialize(a) for k,a in enumerate(W)},
            'physicalScaling':'Omega_k(g,h)=a_h^T W_k a_g / A, A positive and fixed by the packet profile',
            'partialMassTreatment':'theta_plus and theta_minus retained symbolically; coefficients cancel identically in the alternating form',
            'invisibleProbePair':{'u':[2,-5,2,0,0],'v':[0,2,-5,2,0],'endpointsBoth':[0,0],
                                  'seamIndex':1,'A_times_pairing':-10},
            'observationProtocol':[{'probePacket':1,'seamIndex':1}]+[{'probePacket':0,'seamIndex':k} for k in range(1,5)],
            'observationMatrix':[[str(x) for x in row] for row in observation],
            'reconstructionMatrix':[[str(x) for x in row] for row in reconstruction],
            'nativeBilinearReadout':'D_a^T W_k D_a / A; transpose, not adjoint',
            'sourceTraceSubproblemEvaluated':True,'fullPhysicalMixedPolarizationIdentified':False,
            'physicalCutoffResidualEvaluated':False,'analyticalFaceHomotopyEstablished':False,
            'physicalProbeProtocolEstablished':False}
    (ROOT/artifact).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    inputs=[PROFILE,profile['source'],ENCODER,ENCODER_CHECK,COMPARISON,COMPARISON_CHECK,SEWING,artifact,
            'research/strominger/checkers/exact_multiradical.py',
            'research/strominger/checkers/check_finite_observer_encoder.py',
            'research/strominger/checkers/check_finite_packet_green_trace.py']
    report={'status':'passed','check_count':len(checks),'checks':checks,'seamMatrices':5,'polarizedEntries':125,
            'nativePresentationSeamChecks':70,'endpointInvisiblePairing':-10,
            'sourceTraceSubproblemEvaluated':True,'fullPhysicalMixedPolarizationIdentified':False,
            'physicalCutoffResidualEvaluated':False,'analyticalFaceHomotopyEstablished':False,
            'physicalProbeProtocolEstablished':False,'full114ChannelEstablished':False,
            'sourceHashes':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in inputs},
            'scope':'Exact direct-sum Volterra/value-flux source subproblem for the explicitly chosen weighted compact inputs. Does not identify this lift with the full semilocal mixed polarization, add a bilinear form to a Hermitian form without a declared polarization, or evaluate the physical cutoff remainder.'}
    (ROOT/BASE/'finite-packet-green-trace-verification.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:report[k] for k in ['status','check_count','polarizedEntries','nativePresentationSeamChecks','endpointInvisiblePairing']}))


if __name__=='__main__':main()
