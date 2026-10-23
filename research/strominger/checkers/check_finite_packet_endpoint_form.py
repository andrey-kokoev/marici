"""Evaluate the source signed endpoint term on the declared compact packet.
This is not the full regulated H234 residual or an analytical filler.
"""
from pathlib import Path
from fractions import Fraction as F
import hashlib
import json
from exact_multiradical import Radical as R,mm,adj,identity,serialize,sqrt
from check_finite_observer_encoder import restore,perm,rational_inverse

ROOT=Path(__file__).resolve().parents[3]
BASE='research/strominger/results/'
ENCODER=BASE+'finite-observer-encoder.json'
RECEIPT=BASE+'finite-observer-encoder-verification.json'
SEWING=BASE+'channel-assembled-field-sewing.json'
NE=BASE+'neutron-contrast-electron-transport/verification.json'
SOURCE='research/voevodsky/the-full-analytical-system-is-the-joint-graph-realization-of-the-regular-and-endpoint-channels.md'


def main():
    encoder=json.loads((ROOT/ENCODER).read_text());receipt=json.loads((ROOT/RECEIPT).read_text())
    sewing=json.loads((ROOT/SEWING).read_text());ne=json.loads((ROOT/NE).read_text());checks=[]
    def check(name,value):
        if not value:raise AssertionError(name)
        checks.append(name)
    for name,r in [('encoder',receipt),('native sewing',sewing),('native NE',ne)]:
        check(name+' receipt direct inputs current',all(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==sha for p,sha in r['sourceHashes'].items()))
    Tq=[[F(x) for x in row] for row in encoder['analyticReadoutMatrix']]
    T=[[R(x) for x in row] for row in Tq];beta=T[:2];sigma=[[R(0),R(1)],[R(1),R(0)]]
    G=mm(mm(adj(beta),sigma),beta)
    formula=[[R(F(2)**(i-j)+F(2)**(j-i)) for j in range(5)] for i in range(5)]
    check('all25 polarized source endpoint entries evaluated exactly',G==formula)
    check('endpoint form is Hermitian in the declared linear-first pairing convention',G==adj(G))
    # E(g,h)=beta(h)^* sigma beta(g), so a_h^* G a_g is the
    # source convention, rather than silently changing linearity convention.
    plus=[[R(Tq[0][j]+16*Tq[1][j])] for j in range(5)]
    minus=[[R(Tq[0][j]-16*Tq[1][j])] for j in range(5)]
    eigenvalues=[F(421,16),F(-261,16)]
    check('two nonzero eigenvalues of the actual packet form',
          mm(G,plus)==[[eigenvalues[0]*x[0]] for x in plus] and mm(G,minus)==[[eigenvalues[1]*x[0]] for x in minus])
    kernels=[]
    for shift in range(3):
        v=[F(0)]*5;v[shift:shift+3]=[F(2),F(-5),F(2)];kernels.append(v)
    check('three independent endpoint-invisible packet directions remain in the kernel',all(
        mm(G,[[R(x)] for x in v])==[[R(0)] for _ in range(5)] for v in kernels))
    eigenbasis=[[Tq[0][j]+16*Tq[1][j] for j in range(5)],
                [Tq[0][j]-16*Tq[1][j] for j in range(5)],*kernels]
    determinant,_=rational_inverse(eigenbasis)
    check('signature is exactly one positive one negative and three zero directions',determinant!=0)
    negative=[[R(3)],[R(-2)],[R(0)],[R(0)],[R(0)]]
    neg_endpoint=mm(beta,negative);neg_form=mm(mm(adj(negative),G),negative)[0][0]
    check('an actual compact packet has endpoint values minus1 and2 and signed value minus4',neg_endpoint==[[R(-1)],[R(2)]] and neg_form==R(-4))
    positive_gram=mm(adj(beta),beta)
    check('positive endpoint norm is not the source signed pairing',positive_gram!=G and
          mm(mm(adj(negative),positive_gram),negative)==[[R(5)]])
    check('endpoint form alone cannot distinguish a simultaneous exchange of endpoint labels',
          mm(mm(adj(beta[::-1]),sigma),beta[::-1])==G and beta[::-1]!=beta)
    packets={p['packet']:p for p in sewing['packetBindings']}
    H=restore(encoder['nativeFiveFrame']);coefficient_encoder=mm(adj(H),T)
    L={i:mm(mm(restore(p['binding']),perm(p['nativePermutation'])),coefficient_encoder) for i,p in packets.items()}
    D={int(i):restore(a) for i,a in encoder['packetDecoders'].items()}
    readers={i:mm(beta,D[i]) for i in packets}
    check('all14 native packet readers reproduce the actual endpoint coordinates',all(mm(readers[i],L[i])==beta for i in packets))
    check('all14 transported signed endpoint forms pull back to the evaluated source form',all(
        mm(mm(adj(mm(readers[i],L[i])),sigma),mm(readers[i],L[i]))==G for i in packets))
    J=restore(ne['electronFrame']);physical_reader=[[R(0) for _ in range(36)]+row for row in adj(J)]
    check('both E readers match the existing native contrast reader on all44 coordinates',all(
        readers[e['packet']]==physical_reader for e in sewing['exitSplits']))
    Qe=mm(mm(adj(J),J),sigma) # auxiliary check uses the source contrast isometry
    check('native contrast has two orthonormal directions without forcing a positive analytical form',Qe==sigma)
    hadamard=[[sqrt(F(1,2)),sqrt(F(1,2))],[sqrt(F(1,2)),-sqrt(F(1,2))]]
    signed_powers=[[R(1),R(0)],[R(0),R(-1)]]
    check('ideal balanced mixing followed by signed power difference realizes the endpoint form',
          mm(mm(adj(hadamard),signed_powers),hadamard)==sigma)
    native_signed_readout=mm(mm(J,sigma),adj(J))
    for e in sewing['exitSplits']:
        electron=L[e['packet']][36:]
        if mm(mm(adj(electron),native_signed_readout),electron)!=G:raise AssertionError('signed E readout mismatch')
    check('the explicit native8x8 signed readout gives the entire25-entry source endpoint form',True)
    check('discarding one endpoint destroys its cross pairing',
          mm(mm(adj([beta[0],[R(0)]*5]),sigma),[beta[0],[R(0)]*5])!=G)
    artifact=BASE+'finite-packet-endpoint-form.json'
    result={'packetEndpointForm':serialize(G),'nativeElectronSignedReadout':serialize(native_signed_readout),
            'nativeEndpointReaders':{str(i):serialize(a) for i,a in readers.items()},
            'idealEndpointMixer':serialize(hadamard),'detectorConvention':'difference of the two mixed-mode powers; ideal identity only, no calibrated apparatus',
            'pairingConvention':'E(g,h)=beta(h)^* sigma_x beta(g)=a_h^* G a_g (linear in g)',
            'formula':'G_ij=2^(i-j)+2^(j-i), indices0..4',
            'nonzeroEigenvalues':[str(x) for x in eigenvalues],'signature':[1,1,3],
            'kernelBasis':[[str(x) for x in row] for row in kernels],
            'negativePacket':{'coefficients':[3,-2,0,0,0],'endpoints':[-1,2],'signedPairing':-4,'positiveEndpointNormSquared':5},
            'specificEndpointTermEvaluated':True,'fullRegulatedResidualEvaluated':False,
            'analyticalFaceHomotopyEstablished':False,'positivityEstablished':False,'physicalReadoutEstablished':False}
    (ROOT/artifact).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    inputs=[ENCODER,RECEIPT,SEWING,NE,SOURCE,artifact,
            'research/strominger/checkers/exact_multiradical.py',
            'research/strominger/checkers/check_finite_observer_encoder.py',
            'research/strominger/checkers/check_finite_packet_endpoint_form.py']
    report={'status':'passed','checks':checks,'check_count':len(checks),'polarizedEntries':25,
            'transportedPresentations':14,'matchedFull44EReaders':2,'signature':[1,1,3],
            'specificEndpointTermEvaluated':True,'fullRegulatedResidualEvaluated':False,
            'analyticalFaceHomotopyEstablished':False,'positivityEstablished':False,'physicalReadoutEstablished':False,
            'full114ChannelEstablished':False,
            'sourceHashes':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in inputs},
            'scope':'Actual source endpoint Green pairing evaluated on the declared five-packet candidate in its fixed Mellin convention. Native signed-readout equality is exact. This is one analytical term, not the regular/mixed/cutoff remainder or a positive analytical filler.'}
    (ROOT/BASE/'finite-packet-endpoint-form-verification.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:report[k] for k in ['status','check_count','polarizedEntries','transportedPresentations','matchedFull44EReaders','signature']}))


if __name__=='__main__':main()
