"""Actual electron spinor lift and reconstructed joint NE target exchange."""
from pathlib import Path
from fractions import Fraction as F
import sys,json,hashlib
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/strominger/checkers'))
from exact_multiradical import Radical as R,sqrt,mm,adj,identity,serialize
V='research/voevodsky/';S='research/strominger/results/'
def load(p):return json.loads((ROOT/p).read_text())
def sha(p):return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
def restore(a):return [[R({int(k):F(v) for k,v in x.items()}) for x in row] for row in a]
def spinor(v):return R(F(v[0][0]))+F(v[0][1])*sqrt(3)+F(v[1][0])*sqrt(-1)+F(v[1][1])*sqrt(-3)
def sub(a,b):return [[x-y for x,y in zip(r,s)] for r,s in zip(a,b)]
def neg(a):return [[-x for x in row] for row in a]
def zero(n,m):return [[R() for _ in range(m)] for _ in range(n)]
def block(a,b):return [row+[R() for _ in b] for row in a]+[[R() for _ in a]+row for row in b]
def sharp(a,metric):return [[x*metric[j] for j,x in enumerate(row)] for row in adj(a)]
def exchange(k,e,metric):
    ks=sharp(k,metric);s=mm(e,ks);ss=mm(k,adj(e))
    c=mm(k,ks);pe=mm(e,adj(e))
    return [a+b for a,b in zip(sub(identity(36),c),ss)]+[a+b for a,b in zip(s,sub(identity(8),pe))]

def main():
    paths={'spin':V+'results/electron_tetrahedral_spinor_store.json',
      'ne':S+'neutron-contrast-electron-transport/verification.json',
      'five':S+'full-five-channel-candidate/verification.json',
      'n':S+'common-three-carrier-protocol/neutron.json',
      'pn':V+'results/ramsey-moving-carrier-PN-v1.json'}
    d={k:load(p) for k,p in paths.items()}
    for name in ['ne','five']:
        for p,h in d[name]['sourceHashes'].items():assert sha(p)==h,'stale NE input '+p
    for p,h in d['pn']['source_sha256'].items():assert sha(p)==h,'stale moving PN input '+p
    projectors=[[[spinor(v) for v in row] for row in p] for p in d['spin']['face_projectors']]
    j=[[sqrt(F(1,2))*x for x in row] for p in projectors for row in p]
    u=[[R(),sqrt(-1)],[sqrt(-1),R()]]
    assert mm(adj(u),u)==identity(2) and mm(u,u)==neg(identity(2))
    permutation=[]
    for p in projectors:
        image=mm(mm(u,p),adj(u));permutation.append(projectors.index(image))
    assert permutation==[1,0,3,2]
    qe=[[u[i%2][j%2] if i//2==permutation[j//2] else R() for j in range(8)] for i in range(8)]
    assert mm(adj(qe),qe)==identity(8) and mm(qe,qe)==neg(identity(8))
    assert mm(qe,j)==mm(j,u)
    metric=list(map(F,d['n']['source']['metric']))
    k=restore(d['ne']['contrastFrame']);e=restore(d['ne']['electronFrame'])
    assert mm(sharp(k,metric),k)==identity(2) and mm(adj(e),e)==identity(2)
    alignment=mm(adj(j),e);assert mm(j,alignment)==e
    # Target alignment comes from the retained spin lift in logical coordinates.
    target_e=mm(j,mm(u,alignment));assert target_e==mm(qe,e)
    wa,wb=exchange(k,e,metric),exchange(k,target_e,metric)
    q44=block(identity(36),qe);metric44=metric+[F(1)]*8
    assert mm(wb,q44)==mm(q44,wa)
    assert mm(wb,wb)==identity(44)
    assert mm(sharp(wb,metric44),wb)==[[R(metric44[i]) if i==j else R() for j in range(44)] for i in range(44)]
    unchanged_left=mm(wa,q44);right=mm(q44,wa)
    failed=sum(x!=y for a,b in zip(unchanged_left,right) for x,y in zip(a,b));assert failed
    # Full-five output and input are the prior source-bound joint preparation.
    bn=restore(d['five']['neutronFiveEmbedding'])+zero(8,5)
    be=restore(d['five']['postNEJointEmbedding'])
    pi=d['ne']['fiveCoefficientTest']['nativePermutation']
    pimat=[[R(int(j==pi[i])) for j in range(5)] for i in range(5)]
    assert mm(wa,bn)==mm(be,pimat)
    target_be=mm(q44,be)
    assert mm(wb,mm(q44,bn))==mm(target_be,pimat)
    assert mm(sharp(target_be,metric44),target_be)==identity(5)
    egram=mm(adj(target_be[36:]),target_be[36:]);ngram=mm(sharp(target_be[:36],metric),target_be[:36])
    assert mm(egram,egram)==egram and mm(ngram,ngram)==ngram
    assert sum(egram[i][i] for i in range(5))==R(2)
    assert sum(ngram[i][i] for i in range(5))==R(3)
    # The other lift is admitted algebraically but not silently identified.
    alternate_e=neg(target_e);alternate_q=block(identity(36),neg(qe))
    alternate_w=exchange(k,alternate_e,metric)
    assert mm(alternate_w,alternate_q)==mm(alternate_q,wa)
    assert alternate_w!=wb
    square=mm(q44,q44);assert square==block(identity(36),neg(identity(8)))
    assert square!=identity(44)
    inputs=list(paths.values())+[V+'contracts/ramsey-moving-carrier-NE-attempt.v1.json',
       V+'checkers/check_ramsey_moving_carrier_NE.py','research/strominger/checkers/exact_multiradical.py',
       V+'checkers/check_electron_tetrahedral_spinor.py']
    out={'schema':'marici.ramsey-moving-carrier-NE.verification.v1','status':'passed',
       'scope_id':'complementary-spinor-frame-joint-NE-covariance-v1',
       'electronFacePermutation':permutation,'spinLift':serialize(u),'electronAction':serialize(qe),
       'targetElectronFrame':serialize(target_e),'targetJointExchange':serialize(wb),
       'targetFullFiveBinding':serialize(target_be),'fullFieldSquareEntries':1936,
       'jointMetricIsometry':True,'jointExchangeInvolution':True,
       'fiveCoefficientRecovery':True,'electronPreparedRank':2,'retainedBaryonPreparedRank':3,
       'unchangedTargetExchangeFailingEntries':failed,'alternativeLiftAlsoCovariant':True,
       'jointMarkingActionSquare':'diag(I36,-I8)','ordinaryC2ActionProved':False,
       'electronFaceToRamseyFacetBindingProved':False,'uniquePhysicalLiftSelected':False,
       'nativeWGRestrictionProved':False,'parentDescentResolved':False,
       'source_sha256':{p:sha(p) for p in inputs}}
    (ROOT/(V+'results/ramsey-moving-carrier-NE-v1.json')).write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ['spinLift','electronAction','targetElectronFrame','targetJointExchange','targetFullFiveBinding','source_sha256']},indent=2))
if __name__=='__main__':main()
