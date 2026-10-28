"""Frozen candidate: the four-mode complement of the stored N return.
Read-only candidate sources. No assertion that the signed wire selects it.
"""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
import json
import sys
from exact_multiradical import Radical as R, sqrt, mm, adj, identity, serialize

ROOT=Path(__file__).resolve().parents[3]
BASE=ROOT/'research/strominger/results'

def restore(a):
    return [[R({int(k):F(v) for k,v in x.items()}) for x in row] for row in a]

def perm(p):
    return [[R(int(j==p[i])) for j in range(len(p))] for i in range(len(p))]

def subtract(a,b):
    return [[x-y for x,y in zip(row,other)] for row,other in zip(a,b)]

def run():
    path=BASE/'full-five-channel-candidate/verification.json'
    before=sha256(path.read_bytes()).hexdigest()
    data=json.loads(path.read_text())
    N=restore(data['inducedNeutronFiveProjectors']['N'])
    L=restore(data['inducedNeutronFiveProjectors']['L'])
    G=restore(data['inducedNeutronFiveProjectors']['G'])
    assert mm(N,N)==N and adj(N)==N
    mean=[[R()],[sqrt(F(1,3))],[sqrt(F(1,3))],[sqrt(F(1,3))],[R()]]
    assert N==mm(mean,adj(mean))
    # Freeze the prior contrast basis plus the two source context slots.
    E=[[R(),R(),R(1),R()],
       [sqrt(F(1,2)),sqrt(F(1,6)),R(),R()],
       [-sqrt(F(1,2)),sqrt(F(1,6)),R(),R()],
       [R(),-sqrt(F(2,3)),R(),R()],
       [R(),R(),R(),R(1)]]
    assert mm(adj(E),E)==identity(4)
    assert mm(E,adj(E))==subtract(identity(5),N)
    H=subtract(subtract([[2*x for x in row] for row in identity(5)],L),G)
    assert H==subtract(identity(5),N) and mm(H,E)==E
    assert mm(N,mean)==mean and mm(adj(E),mean)==[[R()] for _ in range(4)]
    assert mm(adj(mean),mean)==[[R(1)]]
    # P-root seed pulled back by the actual declared PN coefficient map.
    PN=perm([3,1,2,0,4]);root=mm(PN,E)
    assert mm(adj(root),root)==identity(4)
    endpoints=[]
    for item in data['pathPair']['paths']:
        p=perm(item['coefficientPermutation']);binding=restore(item['binding'])
        encoded=mm(p,root)
        assert mm(adj(encoded),encoded)==identity(4)
        transported_projector=mm(mm(p,mm(root,adj(root))),adj(p))
        assert mm(encoded,adj(encoded))==transported_projector
        endpoints.append({'word':item['word'],'encoded':encoded,'physical':mm(binding,encoded)})
    assert len(endpoints)==2
    assert endpoints[0]['encoded']!=endpoints[1]['encoded']
    assert endpoints[0]['physical']==endpoints[1]['physical']
    # Independent failure if the current local active-mean constraint is
    # reapplied instead of transported. The outside slot enters the mean.
    NN=perm([0,3,4,1,2]);outside=[[R()],[R()],[R()],[R()],[R(1)]]
    assert mm(N,outside)==[[R()] for _ in range(5)]
    after=mm(NN,outside);leak=mm(N,after)
    assert mm(adj(leak),leak)==[[R(F(1,3))]]
    assert sha256(path.read_bytes()).hexdigest()==before
    evidence={str(path.relative_to(ROOT)):before}
    for p in [Path(__file__),Path(__file__).with_name('exact_multiradical.py'),ROOT/'research/strominger/history-dependent-four-mode-codec-v1.md']:
        evidence[str(p.relative_to(ROOT))]=sha256(p.read_bytes()).hexdigest()
    return {'schema':'history-dependent-four-mode-codec.v1','constructionAdmitted':False,
      'signedPairBindingAdmitted':False,'broadExistentialConjectureFalsified':False,
      'frozenCandidate':'kernel of collective N return; transported by retained native coefficient permutation',
      'sectorEncoding':serialize(E),'initialProtonEncoding':serialize(root),
      'conditionalSectorTransport':'passes exact isometry and existing two-path field comparison',
      'fullFiveSlotFaithfulness':'fails: mean and zero have the same four-mode decode',
      'lostMean':serialize(mean),'lostMeanNormSquared':1,'meanSurvivesNativeReturn':True,
      'fixedCurrentSectorInvariance':'fails under NN','NNmeanLeakNormSquared':'1/3',
      'pathComparisons':[{'word':x['word'],'encoding':serialize(x['encoded'])} for x in endpoints],
      'scope':'Reuses a stored conditional field-binding candidate, not a fresh proof of source selection. Kernel restriction omits a genuine retained native mode. It is valid only if an independent wire-source law excludes that mode and supplies the history-dependent coupling. No such law is supplied here.',
      'sourceHashes':evidence}

if __name__=='__main__':
    report=run()
    if '--record' in sys.argv:
        out=BASE/'history-dependent-four-mode-codec-v1/verification.json'
        out.parent.mkdir(parents=True,exist_ok=True)
        out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:report[k] for k in ['conditionalSectorTransport','fullFiveSlotFaithfulness','fixedCurrentSectorInvariance','NNmeanLeakNormSquared','signedPairBindingAdmitted','broadExistentialConjectureFalsified']},indent=2))
