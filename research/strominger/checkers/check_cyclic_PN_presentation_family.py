"""Exact full-matrix C3 comparison orbit, averaging loss and anchored recovery."""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
import contextlib,io,json,hashlib
with contextlib.redirect_stdout(io.StringIO()):
    import check_task_first_PN_conversion as t
    import check_anchored_sector_interface as packet
R=t.R;s=t.square;r=s.r
Up,Un=r.Pthird[0],r.Nthird[0]
I=s.I
pp=[I,Up,s.product(Up,Up)];nn=[I,Un,s.product(Un,Un)]
assert s.product(pp[2],Up)==s.product(nn[2],Un)==I
for U,ops,metric in [(Up,r.Pop,t.pmetric),(Un,r.Nop,t.nmetric)]:
    assert s.product(r.sharp(U,metric),U)==I
    assert all(s.product(U,P)==s.product(P,U) for P in ops.values())
def left(U,M):
    out=[[R() for _ in range(36)] for _ in range(36)]
    for (i,k),a in U.items():
        value=t.decode(a.record())
        for j in range(36):out[i][j]+=value*M[k][j]
    return out
def right(M,U):
    out=[[R() for _ in range(36)] for _ in range(36)]
    for (k,j),a in U.items():
        value=t.decode(a.record())
        for i in range(36):out[i][j]+=M[i][k]*value
    return out
def mv(M,x):return [sum((a*b for a,b in zip(row,x)),R()) for row in M]
family=[left(nn[g],right(t.pn.S,pp[(-g)%3])) for g in range(3)]
assert family[0]==t.pn.S
for g in range(3):assert left(Un,family[g])==right(family[(g+1)%3],Up)
for g in range(3):
    for h in range(3):assert left(nn[g],right(family[h],pp[(-g)%3]))==family[(g+h)%3]
assert left(Un,right(family[2],pp[2]))==family[0]
assert all(family[g]!=family[h] for g,h in combinations(range(3),2))
# Actual source-derived orthonormal basis of the entire rank3 alignment space.
inner=lambda x,y:sum((a.conj()*b*m for a,b,m in zip(x,y,t.pmetric)),R())
def normalized(x):
    size=t.rational(inner(x,x));assert size>0
    return [a*t.sqrt(1/size) for a in x]
NP,GP=r.Pop['N'],r.Pop['G'];Q=t.relative
col=lambda M,j:[t.decode(M.get((i,j),r.ZERO).record()) for i in range(36)]
u=normalized(col(NP,next(j for j in range(36) if (j,j) in NP)))
v=t.x
w=None
for j in range(36):
    raw=col(Q,j);coefficient=inner(v,raw);candidate=[a-coefficient*b for a,b in zip(raw,v)]
    if inner(candidate,candidate)!=R():w=normalized(candidate);break
assert w is not None
basis=[u,v,w]
assert r.trace(GP)==r.A(3)
for i,x in enumerate(basis):
    assert t.apply(GP,x)==x and t.apply(Up,x)==x
    for j,y in enumerate(basis):assert inner(x,y)==R(int(i==j))
assert t.apply(NP,v)==t.apply(NP,w)==[R()]*36
average=[[sum((family[g][i][j] for g in range(3)),R())*F(1,3) for j in range(36)] for i in range(36)]
for x in basis:assert mv(average,x)==t.convert(t.apply(NP,x))
assert mv(average,v)==mv(average,w)==[R()]*36
assert t.norm(mv(average,u),t.nmetric)==R(1)
outputs=[[mv(M,x) for x in [v,w]] for M in family]
def gram(columns):
    return [[sum((a.conj()*b*m for a,b,m in zip(x,y,t.nmetric)),R()) for y in columns] for x in columns]
for out in outputs:assert gram(out)==[[R(1),R()],[R(),R(1)]]
pairwise=[]
for g,h in combinations(range(3),2):
    difference=[[a-b for a,b in zip(outputs[h][i],outputs[g][i])] for i in range(2)]
    assert gram(difference)==[[R(3),R()],[R(),R(3)]]
    pairwise.append({'contexts':[g,h],'residualGram':t.pn.serialize(gram(difference))})
for i in range(2):
    steps=[[outputs[(g+1)%3][i][j]-outputs[g][i][j] for j in range(36)] for g in range(3)]
    assert [sum((step[j] for step in steps),R()) for j in range(36)]==[R()]*36
# Real packet API, same frozen descriptor/reference conventions.
packets=[]
for g,out in enumerate(outputs):
    pkt=packet.prepare(packet.descriptor,packet.to_ports(v,out[0]))
    assert packet.from_ports(packet.recover(pkt,packet.descriptor))==(v,out[0])
    packets.append({'context':g,'packet':pkt})
assert all(packets[g]['packet']['blocks']!=packets[h]['packet']['blocks'] for g,h in combinations(range(3),2))
mean_output=[sum((out[0][i] for out in outputs),R())*F(1,3) for i in range(36)]
assert mean_output==[R()]*36
mean_field_packet=packet.prepare(packet.descriptor,packet.to_ports(v,mean_output))
# Compare an actual N diagonal self-block entry: positive averaged intensity
# survives while preparation of the zero mean output gives zero.
witness=None
for port in packet.Nports:
    key=port['id']
    for i in range(port['dimension']):
        intensity=sum((packet.restore(row['packet']['blocks'][key][key][i][i]) for row in packets),R())*F(1,3)
        if intensity!=R():
            assert packet.restore(mean_field_packet['blocks'][key][key][i][i])==R()
            witness={'port':key,'coordinate':i,'averagedSelfComparison':intensity.record(),'selfComparisonOfMeanField':{}}
            break
    if witness:break
assert witness
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/strominger/results'
result={'status':'pass','classification':'three-context-equivariant-PN-family-retained-averaging-loses-relative-modes',
        'family':'S_g=U_N^g S U_P^(-g), g in Z/3','distinctFullMatrices':3,
        'cyclicReturn':True,'transportSquares':3,'groupActionCompositions':9,
        'metricAndProjectorPreservationCertificate':'Fresh coarse S factor identities plus native metric-unitary C3 actions commuting with named projectors; preserved under composition. No dense36-by36 inverse products claimed.',
        'alignmentBasisDimension':3,'averagedAlignmentRank':1,'annihilatedRelativeDimension':2,
        'averagingIdentity':'Sbar G_P=S N_P','fullAveragedRankComputed':False,
        'pairwiseResiduals':pairwise,'consecutiveResidualsSumZero':True,
        'anchoredContextPacketsRecovered':3,'comparisonAveragingDiffersFromFieldAveraging':witness,
        'fixedEquivariantMapConstructed':False,'contextCanonicalChoiceDerived':False,
        'physicalSewingEstablished':False,'monsterGateActivated':False,
        'scope':'Orbit of a supplied coarse comparison with retained context. Closed cyclic transport does not imply equality of its three maps. No physical context, native move, canonical complement or statistical-mixture type is inferred.',
        'nextObligation':'Classify which task data/readouts descend after forgetting context, distinguishing invariant scalar diagnostics, full fields, and averages of quadratic comparisons.'}
sources=[Path(__file__),Path(t.__file__),Path(packet.__file__),ROOT/'research/strominger/cyclic-PN-presentation-family-v1.md',BASE/'task-first-PN-conversion/verification.json',BASE/'anchored-sector-interface/verification.json',BASE/'global-PN-transport/verification.json']
result['sourceHashes']={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}
out=BASE/'cyclic-PN-presentation-family';out.mkdir(exist_ok=True)
(out/'verification.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:result[k] for k in ['status','classification','distinctFullMatrices','cyclicReturn','groupActionCompositions','averagedAlignmentRank','annihilatedRelativeDimension','anchoredContextPacketsRecovered','fixedEquivariantMapConstructed']}))
