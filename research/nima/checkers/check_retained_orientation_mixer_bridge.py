"""Exact finite character bridge, not a physical-frame identification."""
from fractions import Fraction as F
from itertools import permutations, product
from pathlib import Path
import json
from check_four_packet_record_feedback import mm, transpose, rank
ROOT=Path(__file__).resolve().parents[1]


def matching(*pairs):return tuple(sorted(tuple(sorted(p)) for p in pairs))
MATCHINGS=(matching((0,1),(2,3)),matching((0,2),(1,3)),matching((0,3),(1,2)))

def sign(p):return (-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
def compose(p,q):return tuple(p[q[i]] for i in range(len(p)))
def det(a):return a[0][0]*a[1][1]-a[0][1]*a[1][0]
def contrast_action(p):
    induced=tuple(MATCHINGS.index(matching(*[(p[a],p[b]) for a,b in m])) for m in MATCHINGS)
    cols=[]
    for v in ((1,-1,0),(0,1,-1)):
        w=[0,0,0]
        for i in range(3):w[induced[i]]=v[i]
        assert sum(w)==0
        cols.append((F(w[0]),F(-w[2])))
    return transpose(tuple(cols))


def main():
    ps=tuple(permutations(range(4)));metric=((F(2),F(-1)),(F(-1),F(2)))
    actions={p:contrast_action(p) for p in ps}
    for p,a in actions.items():
        assert det(a)==sign(p)
        assert mm(mm(transpose(a),metric),a)==metric
    for p,q in product(ps,repeat=2):assert mm(actions[p],actions[q])==actions[compose(p,q)]
    # H2 of two primitive spheres transforms by (s,t). Needed attachment
    # transforms by st. A linear f(a,b)=u*a+v*b has no nonzero solution.
    linear=[]
    for s,t in product((-1,1),repeat=2):
        linear.append((F(s-s*t),F(t-s*t)))
    linear_rank=rank(tuple(linear))
    # Polynomial coefficient matching: each monomial is independent.
    quadratic_constraints=[]
    for s,t in product((-1,1),repeat=2):
        quadratic_constraints.extend(((F(1-s*t),0,0),(0,F(s*t-s*t),0),(0,0,F(1-s*t))))
    assert linear_rank==2 and rank(tuple(quadratic_constraints))==2
    for a,b,s,t in product((-2,-1,0,1,2),(-2,-1,0,1,2),(-1,1),(-1,1)):
        assert (s*a)*(t*b)==s*t*(a*b)
    # Filled tetrahedron: orientation survives as a retained 3-chain, not H2.
    vertices=range(4);edges=tuple((i,j) for i in vertices for j in vertices if i<j)
    faces=tuple(tuple(i for i in vertices if i!=k) for k in vertices)
    d2=[[F(0) for _ in faces] for _ in edges]
    for j,face in enumerate(faces):
        for k in range(3):d2[edges.index(tuple(x for i,x in enumerate(face) if i!=k))][j]=F((-1)**k)
    d3=tuple((F((-1)**k),) for k in range(4))
    assert mm(tuple(map(tuple,d2)),d3)==tuple((F(0),) for _ in edges)
    assert rank(tuple(map(tuple,d2)))==3 and rank(d3)==1
    # The seed's oriented ABC and ADB faces consistently select -boundary(ABCD).
    seed_boundary=tuple(-row[0] for row in d3)
    assert seed_boundary[faces.index((0,1,2))]==1
    assert seed_boundary[faces.index((0,1,3))]==-1
    # Actual adapter control: exchange Boolean basis at diagram vertex 1,
    # without permuting the four DIAGRAM vertices or their oriented faces.
    # Thus topological orientation records stay fixed while the mixer character
    # det(Q2)det(Q1) is -1. A function of those records alone cannot supply it.
    boolean_flip=((F(0),F(1)),(F(1),F(0)))
    topology_character=1
    actual_mixer_character=det(boolean_flip)
    assert topology_character==1 and actual_mixer_character==-1
    result=dict(status='pass',schema='marici.nima.retained-orientation-mixer-bridge.v1',
        permutation_actions=24,composition_checks=576,
        finite_character_bridge='S4 acts on its three pair partitions; their counting-metric contrast plane has determinant equal to the vertex-permutation sign.',
        actual_adapter_control={'diagram_orientation_character':topology_character,
                                'boolean_fiber_mixer_character':int(actual_mixer_character),
                                'conclusion':'Topological oriented-face records alone cannot provide the attachment under this actual independent fiber-frame change.'},
        linear_attachment_space_dimension=0,
        homogeneous_quadratic_attachment_space_dimension=1,
        bilinear_attachment='f(a,b)=kappa*a*b transforms by the required product character; equivariance alone does not fix kappa.',
        normalized_attachment='For two actual nonzero oriented records, sign(a*b) is covariant under the matched finite actions, after choosing the product-line identification. Zero records cannot supply a sign.',
        filled_tetrahedron={'rank_boundary2':3,'rank_boundary3':1,'H2_dimension':0,'orientation_chain_retained':True},
        seed_orientation='The directed ABC and ADB face orientations consistently extend to -boundary(ABCD); this selects an orientation only for a retained oriented-face input, not an unmarked tetrahedron.',
        unresolved=['No source identification yet binds this contrast plane to the existing Clifford edge fibers.',
                    'No two endpoint-indexed oriented records have yet been extracted from the actual evolving bank package.',
                    'Finite permutation covariance is not a proof of independently local O(2) physical covariance.',
                    'No physical geometry, matter coupling or gravitational normalization is selected.'])
    (ROOT/'results/retained-orientation-mixer-bridge.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
