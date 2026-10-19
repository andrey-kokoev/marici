"""Geometric P embeddings and a necessary PN projector-compatibility test."""
from pathlib import Path
from fractions import Fraction as F
import sys,json,hashlib
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/'research/nima/checkers'))
import check_twelve_triangle_positive_geometry as geo
from assemble_metric_coefficient_protocol import A,ONE,ZERO,read_operator,product
BASE=ROOT/'research/strominger/results'
def radical(mask,scale=1):return A(tuple(F(scale) if i==mask else F(0) for i in range(16)))
def lift(z):return A(tuple(F(z[0]) if i==0 else F(z[1]) if i==10 else F(0) for i in range(16)))
def adj(B,m):return {(j,i):v.flip(8)*A(m[i]) for (i,j),v in B.items()}
def compress(B,m,X):return product(product(adj(B,m),X),B)
def decode(d):return A(tuple(F(d.get(str(i),0)) for i in range(16)))
p=json.loads((BASE/'common-three-carrier-protocol/proton.json').read_text());n=json.loads((BASE/'common-three-carrier-protocol/neutron.json').read_text());labels=p['source']['coordinates'];P={k:read_operator(p['operators'][k],36) for k in ['L','G','N']};N={k:read_operator(n['operators'][k],36) for k in ['L','G','N']};mp=[F(1)]*36;mn=list(map(F,n['source']['metric']))
records=json.loads((BASE/'tetrahedral-field-attachment/verification.json').read_text())['gridGeometry'];patches={}
coeff=(geo.ONE,geo.OMEGA,geo.zmul(geo.OMEGA,geo.OMEGA));points=dict(geo.POINTS)
for rec in records:
    f,a,b=rec['surfaceTriangle'];points[f]=geo.mean([points[v] for v in f[2:]]);v=list(map(lift,geo.zmv(geo.transpose(tuple(points[k] for k in (f,a,b))),coeff)));patches[a+b]={'v':v,'R':[[F(x) for x in row] for row in rec['rotation']]}
v0=patches['AB']['v'];w=[v0[1].flip(8),-v0[0].flip(8),ZERO];assert sum((a.flip(8)*b for a,b in zip(v0,w)),ZERO)==ZERO
assert A(12)*sum((x.flip(8)*x for x in w),ZERO)==A(F(128,3));contextScale=radical(3,F(8,3));vertexScale=radical(4,2) # sqrt(20)
embeddings=[]
for endpoint in [0,1]:
    B={}
    for i,label in enumerate(labels):
        edge,axis=label.split(':');a='xyz'.index(axis);patch=patches[edge];B[i,'ABCD'.index(edge[endpoint])]=patch['v'][a]/vertexScale
        value=sum((A(patch['R'][a][j])*w[j] for j in range(3)),ZERO)/contextScale
        if value!=ZERO:B[i,4]=value
    assert product(adj(B,mp),B)=={(i,i):ONE for i in range(5)};embeddings.append(B)
assert embeddings[0]!=embeddings[1]
# Verify every proper tetrahedral rotation, not just one order-two advance.
group={(0,1,2,3)};q=list(group)
for g in q:
    for seed in [(1,2,0,3),(3,0,2,1)]:
        h=geo.compose(seed,g)
        if h not in group:group.add(h);q.append(h)
assert len(group)==12
for g in group:
    R=geo.rotation(g);U={};V={(g[j],j):ONE for j in range(4)};V[4,4]=ONE
    for j,label in enumerate(labels):
        edge,axis=label.split(':');new=''.join('ABCD'[g['ABCD'.index(v)]] for v in edge)
        for i in range(3):
            if R[i]['xyz'.index(axis)]:U[labels.index(new+':'+'xyz'[i]),j]=A(R[i]['xyz'.index(axis)])
    for B in embeddings:assert product(U,B)==product(B,V)
# Both geometric seeds induce the same operators on the five-dimensional input.
compressions=[{key:compress(B,mp,op) for key,op in P.items()} for B in embeddings];assert compressions[0]==compressions[1]
expectedL={(i,i):ONE for i in range(4)};expectedG={(i,j):A(F(1,4)) for i in range(4) for j in range(4)};expectedG[4,4]=ONE;expectedN={(i,j):A(F(1,4)) for i in range(4) for j in range(4)}
assert compressions[0]=={'L':expectedL,'G':expectedG,'N':expectedN}
for B in embeddings:
    for key in P:assert product(P[key],B)==product(B,compressions[0][key])
# A full metric-unitary PN S exchanging L/G would preserve these compressions:
# Bp*Mp Lp Bp = Pi* Bn*Mn Gn Bn Pi, etc. Reject prior arbitrary N seeds.
prior=json.loads((BASE/'five-coefficient-field-binding/verification.json').read_text());pi={(i,j):ONE for i,j in enumerate([3,1,2,0,4])};rejections=[]
for entries in prior['neutron']['constructedSeeds']:
    Bn={(e['field'],e['coefficient']):decode(e['value']) for e in entries};mismatch=[]
    for pk,nk in [('L','G'),('G','L'),('N','N')]:
        right=product(product(pi,compress(Bn,mn,N[nk])),pi)
        if right!=compressions[0][pk]:mismatch.append([pk,nk])
    assert mismatch;rejections.append(mismatch)
# A4 character count: field representation is three regular representations;
# domain is tetrahedral four-vertex permutation plus one scalar context.
intertwinerDimension=36*5//12;assert intertwinerDimension==15
serialize=lambda B:[{'row':i,'column':j,'value':v.record()} for (i,j),v in sorted(B.items())]
result={'status':'geometric-P-five-coefficient-bindings-derived-and-PN-filter-tested','geometricSeeds':[{'endpoint':name,'embedding':serialize(B)} for name,B in zip(['first outer corner','second outer corner'],embeddings)],'metricIsometric':True,'tetrahedralSymmetriesCheckedPerSeed':12,'exactReducingSubspace':True,'inducedFiveOperators':{k:serialize(v) for k,v in compressions[0].items()},'interpretation':{'L':'retain the four vertex coefficients; reject outside context','G':'average four vertex coefficients; retain outside context','return':'average four vertex coefficients; reject outside context'},'PNNecessaryCompatibility':{'priorNeutronSeedsRejected':len(rejections),'mismatchedOperatorPairs':rejections},'fullA4EquivariantLinearMapSpaceComplexDimension':intertwinerDimension,'scope':'Geometric P candidates use an ordered patch endpoint for scalar sampling and a chosen orthogonal transported context direction. Two choices survive all A4 rotations, metric and projector reduction, so not uniquely selected. Induced five-dimensional projectors are candidate constructions, not claimed to equal native active-window Fourier readouts. PN tests reject prior arbitrary N embeddings under a full metric-unitary role-exchanging field transport hypothesis; do not reject all PN field maps. No global PNE binding derived.'}
paths=[Path(__file__).resolve(),BASE/'common-three-carrier-protocol/proton.json',BASE/'common-three-carrier-protocol/neutron.json',BASE/'five-coefficient-field-binding/verification.json',BASE/'tetrahedral-field-attachment/verification.json'];result['sourceHashes']={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths};out=BASE/'geometric-coefficient-binding';out.mkdir(exist_ok=True);(out/'verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'status':result['status'],'geometricIsometricSeeds':2,'symmetriesPerSeed':12,'projectorReductionExact':True,'priorNeutronSeedsRejected':2}))
