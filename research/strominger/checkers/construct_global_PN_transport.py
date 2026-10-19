"""Exact global metric-unitary PN candidate from tensor factors and gauges."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib
from exact_multiradical import Radical as R,sqrt,mm,adj,identity,decode_A,rational,serialize
from assemble_metric_coefficient_protocol import read_operator
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/strominger/results'
def toward_first(prob):
    n=len(prob);Q=identity(n);mass=prob[0]
    for i in range(1,n):
        total=mass+prob[i];c,s=sqrt(mass/total),sqrt(prob[i]/total);G=identity(n);G[0][0]=G[i][i]=c;G[0][i]=s;G[i][0]=-s;Q=mm(G,Q);mass=total
    assert mass==1;assert mm(Q,[[sqrt(x)] for x in prob])==[[R(int(i==0))] for i in range(n)];assert mm(adj(Q),Q)==identity(n)
    return Q
def projector(prob):return [[sqrt(x*y) for y in prob] for x in prob]
fixture=BASE/'baryon-tensor-grid/verification.json';data=json.loads(fixture.read_text())['carriers'];sources={s:json.loads((BASE/f'common-three-carrier-protocol/{s}.json').read_text()) for s in ['proton','neutron']};frames={}
for species in sources:
    row=data[species];metric=list(map(F,sources[species]['source']['metric']));z=[decode_A(x) for x in row['sourceReturnColumn']];phase=[]
    for x in z:
        norm=rational(x.conj()*x);assert norm>0;phase.append(x*sqrt(1/norm));assert phase[-1].conj()*phase[-1]==1
    probs=[[rational(decode_A(x)) for x in row[key]] for key in ['rowProbabilities','columnProbabilities']];grid=sum(row['grid'],[]);fine='L' if species=='proton' else 'G';coarse='G' if species=='proton' else 'L'
    normalized={}
    for key in ['L','G','N']:
        native=read_operator(sources[species]['operators'][key],36);matrix=[]
        for a,i in enumerate(grid):
            line=[]
            for b,j in enumerate(grid):
                value=decode_A(native[i,j].record()) if (i,j) in native else R();line.append(sqrt(metric[i]/metric[j])*phase[i].conj()*value*phase[j])
            matrix.append(line)
        normalized[key]=matrix
    p12,p3=map(projector,probs)
    expectedFine=[[p3[i%3][j%3] if i//3==j//3 else R() for j in range(36)] for i in range(36)];expectedCoarse=[[p12[i//3][j//3] if i%3==j%3 else R() for j in range(36)] for i in range(36)];expectedReturn=[[p12[i//3][j//3]*p3[i%3][j%3] for j in range(36)] for i in range(36)]
    assert normalized[fine]==expectedFine;assert normalized[coarse]==expectedCoarse;assert normalized['N']==expectedReturn
    frames[species]={'metric':metric,'phase':phase,'grid':grid,'probabilities':probs}
p,n=frames['proton'],frames['neutron'];O=[]
for axis in range(2):
    left,right=p['probabilities'][axis],n['probabilities'][axis];o=mm(adj(toward_first(right)),toward_first(left));assert mm(adj(o),o)==identity(len(left));assert mm(o,[[sqrt(x)] for x in left])==[[sqrt(x)] for x in right];assert mm(o,projector(left))==mm(projector(right),o);O.append(o)
S=[[R() for _ in range(36)] for _ in range(36)]
for a,i in enumerate(n['grid']):
    for b,j in enumerate(p['grid']):S[i][j]=n['phase'][i]*sqrt(p['metric'][j]/n['metric'][i])*O[0][a//3][b//3]*O[1][a%3][b%3]*p['phase'][j].conj()
# All source entries were checked against the two tensor factors above.
# Their exact orthogonality/intertwining plus metric/phase changes prove the
# full 36-dimensional identities, without large redundant dense products.
result={'status':'global-PN-metric-unitary-candidate-constructed','dimension':36,'identities':['S* M_N S=M_P','S L_P=G_N S','S G_P=L_N S','S N_P=N_N S'],'method':'native grid/phase/metric normalization; two real factor rotations; undo target normalization','factorDimensions':[12,3],'factorRotations':[serialize(o) for o in O],'matrix':serialize(S),'scope':'All 36 native operator coefficients checked in normalized tensor frames, with exact factor orthogonality and intertwining. This gives a global algebraic PN candidate, not a face-supported map. Ordered Givens rotations choose one of many possible complements. It is not yet tied to the native five-coefficient PN permutation or path holonomy, and does not extend the prior six-component face map as a closed block. No physical transport law or production change asserted.'}
paths=[Path(__file__).resolve(),Path(__file__).with_name('exact_multiradical.py'),fixture,*[BASE/f'common-three-carrier-protocol/{s}.json' for s in sources]];result['sourceHashes']={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths};out=BASE/'global-PN-transport';out.mkdir(exist_ok=True);(out/'verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'status':result['status'],'dimension':36,'identities':result['identities']}))
