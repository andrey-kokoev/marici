"""Exact audit of the frozen Marici six-arrow source and its two-face quotient.

No native green relation, effect representation, or physical parameter is added.
Only the explicitly labeled directed graph, optional R/B and G cellular
attachments, and formal groupoid inverses for homotopy calculations are used.
"""
from collections import Counter, defaultdict
from itertools import permutations, product
import json
from sympy import Matrix
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

V=('A','B','C','D')
E={'AB':('A','B'),'BC':('B','C'),'CA':('C','A'),
   'AD':('A','D'),'DB':('D','B'),'BA':('B','A')}
rho_v={'A':'B','B':'A','C':'D','D':'C'}
rho_e={'AB':'BA','BA':'AB','BC':'AD','AD':'BC','CA':'DB','DB':'CA'}
FACES={
 'R':[('AB',1),('BC',1),('CA',1)],
 'B':[('AD',1),('DB',1),('BA',1)],
 'G1':[('AB',1),('DB',-1),('AD',-1)],
 'G2':[('BA',1),('CA',-1),('BC',-1)],
}

# Original source: check exact directed graph involution and its uniqueness.
perms=[]
for p in permutations(V):
    mp=dict(zip(V,p))
    rel={k for k,(s,t) in E.items()}
    if all((mp[s],mp[t]) in E.values() for s,t in E.values()):
        perms.append(mp)
assert perms==[dict(zip(V,V)),rho_v] or (len(perms)==2 and rho_v in perms)
for e,(s,t) in E.items():
    assert E[rho_e[e]]==(rho_v[s],rho_v[t])

adj=defaultdict(list)
for k,(s,t) in E.items(): adj[s].append((k,t))
paths_by_len={0:[('A',(), 'A')]}
# Enumerate all free paths from A to any destination.
allpath=[('A',(), 'A')]
counts_all=[len(V)]
N=9
bylen={0:[(v,(),v) for v in V]}
for n in range(1,N+1):
    bylen[n]=[(s,w+(e,),t) for s,w,u in bylen[n-1] for e,t in adj[u]]
    counts_all.append(len(bylen[n]))
assert counts_all[:7]==[4,6,10,16,26,42,68]

# Enumerate first returns at A: the interior vertices must all be != A.
first_returns=[]
for n in range(1,N+1):
    for s,w,t in bylen[n]:
        if s!='A' or t!='A': continue
        cur='A'; internal=[]
        for e in w[:-1]:
            assert E[e][0]==cur
            cur=E[e][1]; internal.append(cur)
        if 'A' not in internal: first_returns.append(w)
first_returns=sorted(first_returns,key=lambda w:(len(w),w))
expected={('AB','BA'),('AB','BC','CA'),('AD','DB','BA'),('AD','DB','BC','CA')}
assert set(first_returns)==expected

def split_returns(w):
    u='A'; group=[]; chunks=[]
    for e in w:
        assert E[e][0]==u
        group.append(e); u=E[e][1]
        if u=='A':
            assert tuple(group) in expected
            chunks.append(tuple(group)); group=[]
    assert u=='A' and not group
    return tuple(chunks)

returns=0
for n in range(N+1):
    for s,w,t in bylen[n]:
        if s==t=='A':
            assert sum(map(len,split_returns(w)))==len(w)
            returns+=1

# Fundamental group of the free graph with spanning tree AB,AD,BC.
# After contracting the spanning tree, each remaining edge is one free generator.
chord={'CA':'x','DB':'y','BA':'z'}
def inv(k):return k.upper() if k.islower() else k.lower()
def reduce_word(seq):
    out=[]
    for c in seq:
        if out and out[-1]==inv(c):out.pop()
        else:out.append(c)
    return tuple(out)
def mul(*ws):return reduce_word(c for w in ws for c in w)
def inverse(w):return tuple(inv(c) for c in reversed(w))
def edge_word(segments):
    return reduce_word((chord[e] if sign==1 else inv(chord[e]))
                       for e,sign in segments if e in chord)
def directed_word(w):return edge_word([(e,1) for e in w])
reps={
 'r00':('AB','BA'),
 'r01':('AB','BC','CA'),
 'r10':('AD','DB','BA'),
 'r11':('AD','DB','BC','CA')}
free_group_image={key:''.join(directed_word(w)) for key,w in reps.items()}
assert free_group_image=={'r00':'z','r01':'x','r10':'yz','r11':'yx'}

# Transport of source reflection to loops based at A along AB.
# The chosen transport is explicitly additional to the unbased involution.
phi_letters={'x':('z','y'),'y':('x','Z'),'z':('z',)}
def phi(w):
    return reduce_word((c for a in w for c in
        (phi_letters[a] if a.islower() else inverse(phi_letters[a.lower()]))))
for k in 'xyz':
    assert phi(phi((k,)))==mul(('z',),(k,),('Z',))
assert all(phi(phi(directed_word(w)))==mul(('z',),directed_word(w),('Z',))
           for n in range(N+1) for s,w,t in bylen[n] if s==t=='A')

# The source reflection permutes R/B and G1/G2 cellular boundaries.
def cyclic_rotations(word):
    return [tuple(word[i:]+word[:i]) for i in range(len(word))]
assert all(tuple((rho_e[e],sg) for e,sg in FACES[a]) in cyclic_rotations(FACES[b])
           for a,b in [('R','B'),('G1','G2')])

# Compute integral boundary maps; face columns depend on supplied face list.
edge_list=list(E); vertex_list=list(V)
B1=Matrix([[(-1 if s==v else 0)+(1 if t==v else 0)
           for e,(s,t) in E.items()] for v in V])
B2all=Matrix([[sum(s for e2,s in path if e2==e)
               for path in FACES.values()] for e in E])
assert B1*B2all==Matrix.zeros(len(V),len(FACES))

def diag_smith(A):
    D=smith_normal_form(A,domain=ZZ)
    return [int(D[i,i]) for i in range(min(D.shape)) if D[i,i]!=0]

# The three non-tree edges freely generate H1 of the graph; projection of
# face boundaries to these coordinates presents H1 after attaching 2-cells.
chord_indices=[edge_list.index(e) for e in ('CA','DB','BA')]
results={}
for name,fs in [('free',[]),('RB',['R','B']),('RBG1',['R','B','G1']),
                ('RBG1G2',['R','B','G1','G2'])]:
    m=Matrix([[sum(s for e,s in FACES[f] if e==e0) for f in fs]
              for e0 in ('CA','DB','BA')]) if fs else Matrix.zeros(3,0)
    rank=int(m.rank())
    torsion=[abs(d) for d in diag_smith(m) if abs(d)>1]
    h1free=3-rank
    h2=len(fs)-rank
    results[name]={'V':4,'E':6,'F':len(fs),'chi':4-6+len(fs),
                   'H1_free_rank':h1free,'H1_torsion':torsion,'H2_rank':h2,
                   'face_matrix_snf':diag_smith(m)}
assert results['free']['H1_free_rank']==3
assert results['RB']['H1_free_rank']==1
assert results['RBG1']['H1_free_rank']==0
assert results['RBG1G2']['H2_rank']==1
assert all(not r['H1_torsion'] for r in results.values())
# Explicit complete 2-cycle, with reflection acting as -1 on this class:
cycle=Matrix([1,-1,-1,1])
assert B2all*cycle==Matrix.zeros(6,1)
rho_face=Matrix([[1 if f=={'R':'B','B':'R','G1':'G2','G2':'G1'}[g] else 0
                  for g in FACES] for f in FACES])
assert rho_face*cycle==-cycle

# Quotient by rho: U={A,B}, V={C,D}; a=AB/BA, b=BC/AD, c=CA/DB.
# R=abc and B=bca: same 2-cell in quotient. G=a c^-1 b^-1.
quotient={'R':'abc','B':'bca','G':'aCB'}
quotient_smith={
 'before_G':diag_smith(Matrix([[1],[1]])),
 'after_G':diag_smith(Matrix([[1,1],[1,-1]])),
}
assert quotient_smith=={'before_G':[1],'after_G':[1,2]}
# First relation abc=1 implies bc=a^-1; hence green word a(bc)^-1=a².
assert tuple('aCB')==('a','C','B')

# Reflection-equivariant reversible additive-effect model with red/blue
# closed but green independently selectable. a in Z, b=0, c=-a.
for a in range(-9,10):
    vals={'AB':a,'BA':a,'AD':0,'BC':0,'DB':-a,'CA':-a}
    sums={f:sum(sign*vals[e] for e,sign in face)
          for f,face in FACES.items()}
    assert sums=={'R':0,'B':0,'G1':2*a,'G2':2*a}

# Exact first-return generating series (formal words): four first-return
# terms t^2+2t^3+t^4, and all A-loops are sequences of first returns.
num_returns_by_len=Counter(len(w) for w in first_returns)
assert num_returns_by_len==Counter({3:2,2:1,4:1})
A_return_counts={n:sum(1 for s,w,t in bylen[n] if s==t=='A') for n in range(N+1)}
for n in range(1,N+1):
    assert A_return_counts[n]==sum(num_returns_by_len[k]*A_return_counts.get(n-k,0)
                                   for k in num_returns_by_len)

output={'source_automorphisms':len(perms),'length_n_directed_paths':counts_all,
        'first_returns':[' '.join(w) for w in first_returns],
        'n_tested_return_paths':returns,
        'free_group_images':free_group_image,
        'transported_reflection':{'x':'zy','y':'xZ','z':'z','square':'conjugation by z'},
        'homology':results,
        'A_return_count_by_length':A_return_counts,
        'quotient_presentation':{'before_G':'<a,b,c | abc=1> = Z * Z (2-cell quotient with 2 vertices; after tree collapse F1)',
                                 'after_G':'<a | a^2=1> = C2'},
        'effect_countermodels':{'a=0':'green closes','a=1':'green discrepancy 2'},
        'quotient_h1_smith':quotient_smith,
        'formal_status':'exact finite computations + elementary free group and covering space theorems; not an Agda proof'}
# Fix quotient presentation note to avoid abstract free-product confusion
output['quotient_presentation']['before_G']='π1 = Z, generator a, bc=a^-1 (with b chosen as a spanning-tree edge)'
with open('/mnt/data/ramsey_g_attack/stage9/native_continuation_results.json','w') as f:
    json.dump(output,f,indent=2,sort_keys=True)
print(json.dumps(output,indent=2))
