"""Exact tests of operational reversal on the six-occurrence Marici seed.

The finite models are interpretations of the source, not source-derived operators.
The category-level assertions in the companion note have independent proofs.
Standard Python, no dependencies.
"""
from itertools import product
from fractions import Fraction
import json
from pathlib import Path

# Graph source and reflection: rho preserves direction after swapping vertices.
VERTICES = ('A', 'B', 'C', 'D')
EDGE = {
    'AB': ('A','B'), 'BC': ('B','C'), 'CA': ('C','A'),
    'AD': ('A','D'), 'DB': ('D','B'), 'BA': ('B','A'),
}
rho_v = {'A':'B', 'B':'A', 'C':'D', 'D':'C'}
rho_e = {'AB':'BA','BA':'AB','BC':'AD','AD':'BC','CA':'DB','DB':'CA'}
for e, (u,v) in EDGE.items():
    assert EDGE[rho_e[e]] == (rho_v[u],rho_v[v])
    assert rho_e[rho_e[e]] == e
assert ('AB',) != ('AD','DB') and ('BA',) != ('BC','CA')

# Quaternion group Q8, element=(sign, axis), axis=0=1,1=i,2=j,3=k.
QAX = {
    (0,0):(1,0), (0,1):(1,1), (0,2):(1,2), (0,3):(1,3),
    (1,0):(1,1), (1,1):(-1,0), (1,2):(1,3), (1,3):(-1,2),
    (2,0):(1,2), (2,1):(-1,3), (2,2):(-1,0), (2,3):(1,1),
    (3,0):(1,3), (3,1):(1,2), (3,2):(-1,1), (3,3):(-1,0),
}
def qmul(x,y):
    s,axis=QAX[(x[1],y[1])]
    return (x[0]*y[0]*s,axis)
def qinv(x):
    return (x[0] if x[1]==0 else -x[0], x[1])
Q=list(product((1,-1),range(4)))
QONE=(1,0)
QMINUS=(-1,0)
K=(1,3); QI=(1,1); QJ=(1,2)
def qtheta_id(x): return x
def qtheta_k(x): return qmul(qmul(K,x),qinv(K))

# Permutations: first argument applied after second (standard function composition).
S=list(__import__('itertools').permutations(range(3)))
SONE=(0,1,2)
def smul(x,y): return tuple(x[y[i]] for i in range(3))
def sinv(x): return tuple(x.index(i) for i in range(3))
T=(1,0,2)  # transposition (0 1)
def stheta_t(x): return smul(smul(T,x),sinv(T))

def all_tests(H,e,mul,inv,theta,central):
    out={'assignments':0,'green_strict':0,'central_nontrivial':0,'noncentral':0}
    records=[]
    for a,b in product(H, repeat=2):
        # All six source effects, with reflection pairing, and two face closures.
        c=mul(inv(b), inv(theta(a)))
        source={
          'AB':a,'BA':theta(a), 'AD':b,'BC':theta(b),
          'DB':c,'CA':theta(c)
        }
        prod=lambda *xs: __import__('functools').reduce(mul,xs,e)
        red=prod(source['AB'],source['BC'],source['CA'])
        blue=prod(source['AD'],source['DB'],source['BA'])
        g1=mul(source['AB'], inv(mul(source['AD'],source['DB'])))
        g2=mul(source['BA'], inv(mul(source['BC'],source['CA'])))
        residue=mul(a,theta(a))
        assert red==e and blue==e
        assert g1==residue and g2==mul(theta(a),a)
        assert (g1==e)==(g2==e)
        assert (residue==e)==(theta(a)==inv(a))
        out['assignments']+=1
        typ='green_strict' if g1==e else ('central_nontrivial' if central(g1) else 'noncentral')
        out[typ]+=1
        records.append((a,b,c,typ,g1))
    return out,records

def qcentral(x): return all(qmul(x,y)==qmul(y,x) for y in Q)
def scentral(x): return all(smul(x,y)==smul(y,x) for y in S)
q_id,q_id_records=all_tests(Q,QONE,qmul,qinv,qtheta_id,qcentral)
q_k,q_k_records=all_tests(Q,QONE,qmul,qinv,qtheta_k,qcentral)
s_t,s_t_records=all_tests(S,SONE,smul,sinv,stheta_t,scentral)

# Witnesses for all three outcomes.
assert any(a==QI and b==QJ and typ=='central_nontrivial' and g1==QMINUS
           for a,b,c,typ,g1 in q_id_records)
assert any(a==QI and b==QJ and typ=='green_strict'
           for a,b,c,typ,g1 in q_k_records)
A=(2,1,0) # permutation (0 2)
assert any(a==A and b==SONE and typ=='noncentral' for a,b,c,typ,g1 in s_t_records)

# Adjoint need not equal inverse: all scalar edges are invertible and self-adjoint.
a,b,c=Fraction(2),Fraction(1),Fraction(1,2)
assert a*b*c==1 and b*c*a==1
assert a*a==4 and a!=b*c  # green comparison fails, despite red/blue closure
assert a!=1/a
# Strict unitary (real scalar ±1) positive control.
for a in (Fraction(1),Fraction(-1)):
    c=1/a
    assert a*1*c==1 and a*a==1 and a==1/a

# One-sided section control: A=R, B=R^2, p=(1,0), q=(1,1), s(x,y)=x.
p=(Fraction(1),Fraction(0)); q=(Fraction(1),Fraction(1))
s=(Fraction(1),Fraction(0)); t=(Fraction(1),Fraction(1))
apply=lambda row,col: sum(x*y for x,y in zip(row,col))
assert p!=q and s!=t
assert apply(s,p)==apply(s,q)==apply(t,p)==1
# Strict one-sided return plus both red/blue faces do not imply either green equality.

# Independent operational inverses do not imply branch interchange.
X=((0,1),(1,0)); Z=((1,0),(0,-1)); I=((1,0),(0,1)); negI=((-1,0),(0,-1))
def matmul(A,B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in (0,1)) for j in (0,1)) for i in (0,1))
def trans(A): return tuple(tuple(A[j][i] for j in (0,1)) for i in (0,1))
assert matmul(trans(X),X)==I and matmul(trans(Z),Z)==I
assert matmul(matmul(X,Z),matmul(X,Z))==negI
assert matmul(X,Z)!=matmul(Z,X)

# Norm-class classification for extensions E --> C2, kernel A, action theta=id.
# C4: lifts 1,3 of odd class both have square 2; norms of A={0,2} are 0.
C4_lifts=(1,3)
assert {2*x%4 for x in C4_lifts}=={2}
assert {2*x%4 for x in (0,2)}=={0}
# Split C2 x C2: lifts (0,1),(1,1) both order 2.
C2xC2_lifts=((0,1),(1,1))
assert all(((2*x)%2,(2*y)%2)==(0,0) for x,y in C2xC2_lifts)
# Q8 -> C2×C2: preimages of coset [i] are ±i; both square to -1.
assert qmul(QI,QI)==QMINUS
assert qmul((-1,1),(-1,1))==QMINUS
# Actual source quotient extension (stage9): 2Z --> Z --> C2.
# Any odd lift 2k+1 squares to 4k+2, nonzero modulo 4Z.
assert all((2*(2*k+1))%4==2 for k in range(-200,201))

out={
    'source':{'directed_vertices':len(VERTICES),'directed_occurrences':len(EDGE),
              'reflected_occurrence_pairs':3,'retained_forward_histories_distinct':True},
    'finite_group_models':{
        'Q8_theta_identity':q_id,
        'Q8_theta_conjugation_by_k':q_k,
        'S3_theta_conjugation_by_transposition':s_t
    },
    'examples':{
        'Q8_strict':{'a':'i','b':'j','theta':'conjugation by k','G':'1'},
        'Q8_central_nontrivial':{'a':'i','b':'j','theta':'identity','G':'-1'},
        'S3_noncentral':{'a':'(0 2)','b':'identity','theta':'conjugation by (0 1)','G':'noncentral 3-cycle'},
        'dagger_nonunitary':{'a':'multiplication by 2','BA':'adjoint multiplication by 2','return':'multiplication by 4'},
        'one_sided_splitting':{'p':'x -> (x,0)','q':'x -> (x,x)','s':'(x,y) -> x','t':'(x,y) -> x+y'},
        'unitary_without_interchange':{'X':'swap','Z':'sign','commutator':'-I'}
    },
    'extension_classes':{
        'C4_over_C2':'nontrivial',
        'C2_times_C2_over_C2':'trivial',
        'Q8_coset_i_over_center':'nontrivial',
        'source_reflection_2Z_into_Z_to_C2':'nontrivial'
    },
    'note':'Exact finite computations. No new Agda proof or native Green constructor.'
}
path=Path(__file__).with_name('operational_reversal_results.json')
path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
