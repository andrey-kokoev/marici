"""C4 context extension; central sign is visible to fixed comparisons."""
from pathlib import Path
import sys,json,hashlib
from fractions import Fraction as F
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/voevodsky/checkers'))
from check_ramsey_moving_carrier_NE import restore,exchange,block,sharp,zero
from exact_multiradical import Radical as R,mm,adj,identity,serialize
V='research/voevodsky/';S='research/strominger/results/'
def load(p):return json.loads((ROOT/p).read_text())
def sha(p):return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
def neg(a):return [[-x for x in row] for row in a]

def main():
    paths={'lift':V+'results/ramsey-moving-carrier-NE-v1.json',
      'ne':S+'neutron-contrast-electron-transport/verification.json',
      'five':S+'full-five-channel-candidate/verification.json',
      'n':S+'common-three-carrier-protocol/neutron.json'}
    d={k:load(p) for k,p in paths.items()}
    for p,h in d['lift']['source_sha256'].items():assert sha(p)==h,'stale lift input '+p
    for label in ['ne','five']:
        for p,h in d[label]['sourceHashes'].items():assert sha(p)==h,'stale native input '+p
    metric=list(map(F,d['n']['source']['metric']));m44=metric+[F(1)]*8
    qe=restore(d['lift']['electronAction']);q=block(identity(36),qe)
    powers=[identity(44)];epowers=[identity(8)]
    for _ in range(3):powers.append(mm(q,powers[-1]));epowers.append(mm(qe,epowers[-1]))
    assert mm(q,powers[3])==identity(44)
    assert powers[2]==block(identity(36),neg(identity(8))) and powers[2]!=identity(44)
    k=restore(d['ne']['contrastFrame']);e=restore(d['ne']['electronFrame'])
    base=restore(d['five']['postNEJointEmbedding'])
    bindings=[mm(p,base) for p in powers]
    readouts=[sharp(b,m44) for b in bindings]
    exchanges=[exchange(k,mm(p,e),metric) for p in epowers]
    pair_count=triangle_count=0
    for a in range(4):
        assert mm(readouts[a],bindings[a])==identity(5)
        for b in range(4):
            c=powers[(b-a)%4]
            assert mm(exchanges[b],c)==mm(c,exchanges[a])
            assert mm(c,bindings[a])==bindings[b]
            assert mm(readouts[b],c)==readouts[a]
            pair_count+=1
            for t in range(4):
                assert mm(powers[(t-b)%4],c)==powers[(t-a)%4]
                triangle_count+=1
    assert (pair_count,triangle_count)==(16,64)
    z=powers[2]
    egram=mm(adj(base[36:]),base[36:])
    h=[[R(int(i==j))-2*egram[i][j] for j in range(5)] for i in range(5)]
    assert mm(readouts[0],mm(z,base))==h
    assert mm(z,base)==mm(base,h)  # central action stays in this full-five image
    assert mm(h,h)==identity(5) and h==adj(h)
    assert h!=identity(5) and h!=neg(identity(5))
    assert sum(h[i][i] for i in range(5))==R(1)  # three +, two -
    assert exchanges[2]!=exchanges[0]
    assert mm(readouts[2],mm(z,base))==identity(5)
    # Fixed coefficient detector supplies a concrete changed amplitude.
    i,j=next((i,j) for i in range(5) for j in range(5) if h[i][j]!=R(int(i==j)))
    column=[[row[j]] for row in base];central=mm(z,column)
    assert mm(sharp(column,m44),column)==[[R(1)]]
    assert mm(sharp(central,m44),central)==[[R(1)]]
    assert column!=central
    # Fourfold return restores both couplings and full readouts, not only norm.
    assert exchange(k,mm(mm(qe,epowers[3]),e),metric)==exchanges[0]
    files=list(paths.values())+[V+'contracts/ramsey-NE-lift-context-attempt.v1.json',
        V+'checkers/check_ramsey_NE_lift_context.py',V+'checkers/check_ramsey_moving_carrier_NE.py',
        'research/strominger/checkers/exact_multiradical.py']
    out={'schema':'marici.ramsey-NE-lift-context.verification.v1','status':'passed',
      'scope_id':'four-lift-contexts-joint-NE-composition-v1','contexts':4,'pairSquares':16,'compositionTriangles':64,
      'fullJointDimension':44,'preparedDimension':5,
      'centralPreparedAction':serialize(h),'centralPreparedSpectrum':{'plusOne':3,'minusOne':2},
      'centralActionPreservesPreparedImage':True,'centralActionChangesFixedCoupling':True,
      'centralActionDetectedByFixedReadout':True,'transportedReadoutAgrees':True,
      'fixedReadoutWitness':{'inputCoefficientBasis':j,'detectorCoordinate':i,
          'before':R(int(i==j)).record(),'after':h[i][j].record(),'normBefore':'1','normAfter':'1'},
      'fourfoldReturn':True,'ordinaryTwofoldQuotientPreservingFixedReadouts':False,
      'contextsAreTimeSteps':False,'nativeWGDerivationProved':False,'parentDescentResolved':False,
      'liftContextFamily':[{'context':t,'electronFrame':serialize(mm(epowers[t],e)),
        'fiveBinding':serialize(bindings[t]),'fiveReadout':serialize(readouts[t])} for t in range(4)],
      'source_sha256':{p:sha(p) for p in files}}
    (ROOT/(V+'results/ramsey-NE-lift-context-v1.json')).write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ['centralPreparedAction','liftContextFamily','source_sha256']},indent=2))
if __name__=='__main__':main()
