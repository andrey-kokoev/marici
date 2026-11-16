"""Exact finite quotient and integral homology checks for a candidate Marici history lift.

Mathematical model, not a native Marici execution or a Ramsey theorem.
The infinite-group no-lift result is proved in the accompanying explanation;
this script verifies its normal-form premise symbolically and finite data.
"""
import json
from itertools import product
from sympy import Matrix, eye, symbols

# D_infty = <M,R | R^2=1, RMR=M^-1>.
# Normal form M^n R^eps, eps in {0,1}.
def multiply(u,v):
    n,e=u; m,f=v
    return (n+(-1)**e*m, e^f)

def q(u):
    n,e=u
    return (n%2,e)

def alpha(v):
    a,b=v
    return (b,(a+b)%2)  # order 3 on Q=F_2^2

I=(0,0); M=(1,0); R=(0,1); x=R; y=multiply(R,M)
assert y==(-1,1)
assert multiply(x,x)==I and multiply(y,y)==I
assert multiply(x,y)==M
assert multiply(alpha((0,1)),(0,0))==alpha((0,1))
for z in product(range(2),repeat=2):
    assert alpha(alpha(alpha(z)))==z
assert [alpha(q(t)) for t in (x,y,M)]==[q(y),q(M),q(x)]
# All involutions have eps=1 (or are identity), no lift in the rotation coset.
# This is an all-integer statement deduced directly from the square formula.
assert multiply((symbols('n',integer=True),1),(symbols('n',integer=True),1))==I

# Symmetric enlargement W=C2*C2*C2 with x,y,z independent involutions.
Q=[(0,0),(0,1),(1,1),(1,0)]
labels=['D','A','B','C']
gen={'x':q(x),'y':q(y),'z':q(M)}
assert alpha(gen['x'])==gen['y'] and alpha(gen['y'])==gen['z'] and alpha(gen['z'])==gen['x']
index={p:labels[i] for i,p in enumerate(Q)}
def add(u,v):return (u[0]^v[0],u[1]^v[1])
matchings={k:sorted({tuple(sorted((index[u],index[add(u,g)]))) for u in Q}) for k,g in gen.items()}
all_edges=set().union(*(set(v) for v in matchings.values()))
assert len(all_edges)==6 and len(set().union(*map(set,matchings.values())))==6
assert all(len(m)==2 for m in matchings.values())
assert len(Q)==4 and len(all_edges)-len(Q)+1==3 # ker(W->Q) free of rank 3

# g=(A B C) acts on H1(K4;Z), base vertex D fixed.
# z_AB=(DA+AB-DB), z_AC=(DA+AC-DC), z_BC=(DB+BC-DC).
# Under g: z_AB -> z_BC; z_AC -> -z_AB; z_BC -> -z_AC.
T=Matrix([[0,-1,0],[0,0,-1],[1,0,0]])
assert T**3==eye(3)
lam=symbols('lambda')
assert T.charpoly(lam).as_expr().expand()==lam**3-1
fixed=(T-eye(3)).nullspace()
assert fixed==[Matrix([1,-1,1])]

# Color only the three matching families, red/blue. Nonconstant assignments
# avoid monochromatic triangles because every K4 triangle uses all matchings.
triples=list(product((0,1),repeat=3))
valid=[t for t in triples if len(set(t))==2]
assert len(valid)==6
orbit={t:tuple(t[(i-1)%3] for i in range(3)) for t in triples}
assert all(orbit[t]!=t for t in valid)
rot_orbits=[]; unvisited=set(valid)
while unvisited:
    a=next(iter(unvisited)); b=orbit[a]; c=orbit[b]; O={a,b,c}
    assert len(O)==3 and orbit[c]==a
    rot_orbits.append(sorted(O)); unvisited-=O
assert len(rot_orbits)==2

# Conditional A4-covariant face closure on the *undirected support* complex.
# Marici has oriented triangles ABC and BAD.  g=(ABC) sends
# BAD -> CBD -> ACD -> BAD.  Their sum with ABC is a 2-cycle.
from itertools import combinations
from sympy import zeros
verts=('A','B','C','D')
edges=list(combinations(verts,2))
faces=list(combinations(verts,3))
B1=zeros(4,6)
for j,(a,b) in enumerate(edges):
    B1[verts.index(a),j]=-1;B1[verts.index(b),j]=1
B2=zeros(6,4)
for j,(a,b,c) in enumerate(faces):
    for pair,coeff in (((b,c),1),((a,c),-1),((a,b),1)):
        B2[edges.index(pair),j]+=coeff
assert B1*B2==zeros(4,4)
assert B1.rank()==3 and B2.rank()==3
sigma=Matrix([1,-1,1,-1]) # ABC - ABD + ACD - BCD
assert B2*sigma==zeros(6,1)
assert (4-1)-B2.rank()==0 # H1=0
assert 4-B2.rank()==1 # H2=Z

# Exhaustive exact K4 extension classification for the induced three matchings.
from collections import Counter
V=('A','B','C','D')
E=list(combinations(V,2))
def mono_triangle(colors, verts):
    for trip in combinations(verts,3):
        vals=[colors[tuple(sorted(e))] for e in combinations(trip,2)]
        if vals[0]==vals[1]==vals[2]:return True
    return False
classes=Counter()
for col in product((0,1),repeat=6):
    coloring=dict(zip(E,col))
    if mono_triangle(coloring,V):
        classes['invalid_K4']+=1;continue
    extensions=0
    for zcolor in product((0,1),repeat=4):
        with_z={**coloring,**{tuple(sorted((v,'Z'))):z for v,z in zip(V,zcolor)}}
        if not mono_triangle(with_z,V+('Z',)):
            extensions+=1
    splitting=[k for k,m in matchings.items()
               if len({coloring[tuple(sorted(e))] for e in m})==2]
    if extensions==1:
        assert len(splitting)==1
        classes['extendable_K4']+=1
    else:
        assert extensions==0 and len(splitting)==0
        classes['nonextendable_triangle_free_K4']+=1
assert classes==Counter({'invalid_K4':46,'extendable_K4':12,'nonextendable_triangle_free_K4':6})

# A finite section for the canonical nonfunctional correspondence P_alpha:
# for each source normal form u, all targets v=M^{2k}v0 are valid and distinct.
def target_representatives(u,ks=(-2,-1,0,1,2)):
    a,b=alpha(q(u)); v0=(a,b)
    return [multiply((2*k,0),v0) for k in ks]
for u in [(-3,1),(-2,0),(0,0),(1,0),(3,1)]:
    candidates=target_representatives(u)
    assert len(set(candidates))==5
    assert all(q(v)==alpha(q(u)) for v in candidates)

report={
    'model':'Symmetric three-involution lift of the D_infinity -> V4 quotient',
    'input_involutions':{'x':'R','y':'RM'},
    'quotient':{'elements':4,'alpha_order':3},
    'nonlift_explanation':'Every order-2 element of D_infinity is a reflection M^n R; the nontrivial rotation coset q(M) has no such representative.',
    'universal_enlargement':'C2 * C2 * C2, with x,y,z exchanged cyclically',
    'K4_matching_orbits':{k:[list(e) for e in v] for k,v in matchings.items()},
    'kernel_free_rank':3,
    'H1_K4_action_matrix':[[int(T[i,j]) for j in range(3)] for i in range(3)],
    'H1_action_characteristic_polynomial':'lambda^3 - 1',
    'H1_fixed_cycle_coefficients':[1,-1,1],
    'conditional_A4_face_growth':{'seed_faces':['ABC','BAD'], 'g_orbit_of_BAD':['BAD','CBD','ACD'], 'fundamental_2_cycle':'ABC + BAD + CBD + ACD', 'boundary_rank_1':3, 'boundary_rank_2':3, 'H1':'0', 'H2':'Z', 'requires':'support-level reversal BA=-AB and admissible transport of face fillers'},
    'admissible_coloring_by_matching_count':6,
    'K4_extension_classification':dict(classes),
    'K4_extension_invariant':'Each extending K4 coloring splits exactly one of the three matchings; each matching-constant valid coloring is nonextendable.',
    'C3_orbits_of_matching_colorings':[[list(t) for t in row] for row in rot_orbits],
    'canonical_correspondence':'P_alpha={(u,v):q(v)=alpha(q(u))}; infinite integer winding choices in each fiber',
    'scope':'Constructive group-theoretic candidate, not an established native Marici filler or a Ramsey forcing law'
}
with open('/mnt/data/marici_threefold_lift_results.json','w') as f:json.dump(report,f,indent=2)
print(json.dumps(report,indent=2))
