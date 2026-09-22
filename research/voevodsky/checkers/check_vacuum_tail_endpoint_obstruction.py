"""Exact endpoint audit of the actual saved vacuum-tail restriction square.

Standard library only. Finite actual forgotten-path sources suffice to rule
out an equivariant quotient, regardless of any infinite-tail completion.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import product,combinations
import hashlib,json
ROOT=Path(__file__).resolve().parents[3]
path=ROOT/'research/nima/results/tail-refinement-square.json'
square=json.loads(path.read_text(encoding='utf-8'))
backgrounds=(3,4,5,6);primes=(2,3,5,7,11,13);terminal_factor=30030

def cubic(A):
    out={}
    for flips in product((0,1),repeat=3):
        word=[]
        for pair,flip in zip(((2,3),(5,7),(11,13)),flips):word.extend(pair[::-1] if flip else pair)
        out[tuple(word)]=(-1)**sum(flips)
    assert len(out)==8 and sum(out.values())==0
    # Each factor is the forgotten two-path relation, hence lies in I.
    return out

def private_vacuum(A,B,col):
    if A!=B:return 0 # The outer initial label is part of the row.
    seams=((B,2*B),(6*B,30*B),(210*B,2310*B));value=0
    for word,coefficient in col.items():
        states=[A]
        for p in word:states.append(states[-1]*p)
        assert states[-1]==terminal_factor*A
        for cuts in combinations(range(6),3):
            if tuple((states[j],states[j+1]) for j in cuts)==seams:value+=coefficient
    return value
for A in backgrounds:
    assert [private_vacuum(A,B,cubic(A)) for B in backgrounds]==[int(A==B) for B in backgrounds]

def mat(groups,n):return [[F(int(j in group)) for j in range(n)] for group in groups]
def mul(a,b):return [[sum((x*y for x,y in zip(row,col)),F(0)) for col in zip(*b)] for row in a]
def vec(xs):return [[F(x)] for x in xs]
def encode(x):return [[str(v) for v in row] for row in x]
# Restrict the infinite background family to four genuine labelled sources.
P={'00':mat([[0,1,2,3]],4),'10':mat([[0],[1,2,3]],4),
   '01':mat([[0,1],[2,3]],4),'11':mat([[0],[1],[2,3]],4)}
edge_maps={}
for name,edge in square['edges'].items():
    old,new=name.split('->');n=len(square['nodes'][new]['rows'])
    assert sorted(j for group in edge['groups'] for j in group)==list(range(n))
    R=mat(edge['groups'],n)
    assert mul(R,P[new])==P[old]
    edge_maps[name]=R
route1=mul(edge_maps['00->10'],edge_maps['10->11'])
route2=mul(edge_maps['00->01'],edge_maps['01->11'])
assert route1==route2==[[F(1),F(1),F(1)]]
# Any equivariant quotient must have a kernel stable under every vertex
# idempotent. Show an explicit violation at every node.
merged={'00':(0,1),'10':(1,2),'01':(0,1),'11':(2,3)}
obstructions={}
for name,(i,j) in merged.items():
    h=vec([int(k==i)-int(k==j) for k in range(4)])
    ei=[[F(int(a==b==i)) for b in range(4)] for a in range(4)]
    before=mul(P[name],h);after=mul(P[name],mul(ei,h))
    assert all(v==[0] for v in before) and any(v!=[0] for v in after)
    obstructions[name]={'source_backgrounds':[backgrounds[i],backgrounds[j]],
      'kernel_vector':encode(h),'left_vertex_idempotent':backgrounds[i],
      'aggregate_before_projection':encode(before),'aggregate_after_projection':encode(after)}
# Endpoint saturation of every displayed partition exposes all four labels.
for observation in P.values():
    projected=set()
    for row in observation:
        for j in range(4):
            if row[j]:projected.add(tuple(row[k] if k==j else F(0) for k in range(4)))
    assert projected=={tuple(F(int(k==j)) for k in range(4)) for j in range(4)}
# Actual finite sources, not just unrestricted formal vectors, fit the same
# declared moment prior and the returned final data.
weights=[8*(F(A,2)**12) for A in backgrounds]
x=vec([F(3,2000),F(1,20000),0,0])
y=vec([F(77,50000),F(1,100000),0,0])
z=vec([F(3,2000),F(1,20000),F(1,10**9),-F(1,10**9)])
final=square['nodes']['11'];costs=[]
for source in (x,y,z):
    cost=sum(w*abs(c[0]) for w,c in zip(weights,source));assert cost<=F(final['budget']);costs.append(str(cost))
    observed=mul(P['11'],source)
    for row,val in zip(final['rows'],observed):
        assert row['calibration']==['1','1']
        lo,hi=map(F,row['data']);assert lo<=val[0]<=hi
    assert sum(F(t)*v[0] for t,v in zip(final['target']['coefficients'],observed))>F(final['target']['threshold'])
assert mul(P['00'],x)==mul(P['00'],y)
assert mul(P['11'],x)!=mul(P['11'],y)
assert mul(P['11'],x)==mul(P['11'],z)
result={'passed':True,'input_square_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
 'actual_source_corners':[[A,terminal_factor*A] for A in backgrounds],
 'private_vacuum_matrix':'4 by 4 identity from the actual eight-term paths',
 'scalar_routes_commute':True,'endpoint_kernel_obstructions':obstructions,
 'minimum_endpoint_saturated_dimension_on_this_support':4,
 'feasible_source_pair_same_coarse_sum':[encode(x),encode(y)],
 'feasible_source_pair_same_final_coordinates':[encode(x),encode(z)],
 'true_finite_source_costs':costs,
 'conclusion':'The scalar aggregate maps cannot be source-equivariant quotient maps for the fixed labelled algebra, under any choice of action on their scalar targets.',
 'scope':'Finite endpoint obstruction; does not negate scalar task certificates or construct an infinite saturated observer.'}
(ROOT/'research/voevodsky/results/vacuum-tail-endpoint-obstruction.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
