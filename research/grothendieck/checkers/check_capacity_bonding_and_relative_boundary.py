"""Inverse capacity bonding, direct defect, and relative normalization square."""
from pathlib import Path
from itertools import product
from math import factorial
import sympy as s
import json
ROOT=Path(__file__).resolve().parents[3]
tau=2

def words(n):return tuple(w for k in range(n+1) for w in product(('a','b'),repeat=k))
def weight(w):return (-1)**w.count('b')*tau**(2*len(w))
def projection(low,high):
    rows={w:i for i,w in enumerate(low)}
    return s.SparseMatrix(len(low),len(high),{(rows[w],j):1 for j,w in enumerate(high) if w in rows})
def seam(n):
    ws=words(n)
    minus=tuple((u,k,v) for u in ws for k in ('omega','a','b') for v in ws)
    zero=tuple((vertex,u,v) for vertex in (0,1) for u in ws for v in ws)
    row={a:i for i,a in enumerate(zero)};entries={}
    for j,(u,k,v) in enumerate(minus):
        letter=() if k=='omega' else (k,)
        if len(u+letter)<=n:entries[row[1,u+letter,v],j]=1
        if len(letter+v)<=n:entries[row[0,u,letter+v],j]=-1
    d=s.SparseMatrix(len(zero),len(minus),entries)
    gm=s.diag(*(weight(u)*weight(v)*(-1 if k=='b' else 1) for u,k,v in minus))
    gz=s.diag(*(weight(u)*weight(v) for vertex,u,v in zero))
    for i,j in entries:
        _,u,v=zero[i];uu,k,vv=minus[j]
        assert len(u)+len(v)==len(uu)+len(vv)+(k!='omega')
    return minus,zero,d,gm,gz
lo=seam(1);hi=seam(2)
pm,pz=projection(lo[0],hi[0]),projection(lo[1],hi[1])
im,iz=pm.T,pz.T
assert pz*hi[2]==lo[2]*pm
boundary=hi[2]*im-iz*lo[2]
assert boundary.rank()==16 and pz*boundary==s.zeros(len(lo[1]),len(lo[0]))
assert boundary==(s.eye(len(hi[1]))-iz*pz)*hi[2]*im
assert hi[3]*im==pm.H*lo[3] and hi[4]*iz==pz.H*lo[4]
# Adjoint inclusion is a chain map on the Green-dual complexes, not the primal ones.
dh_lo=lo[3].inv()*lo[2].H*lo[4]
dh_hi=hi[3].inv()*hi[2].H*hi[4]
assert dh_hi*iz==im*dh_lo

# The untruncated fixed-depth seam differential has a uniform cut-l1 bound.
# Here r=1, tau=2, and the seam feature weight is one: bound 2*max(1,tau)=4.
for model in (lo,hi):
    column_sums=[]
    for j in range(model[2].cols):
        value=sum(abs(c)*s.sqrt(abs(model[4][i,i])) for (i,k),c in model[2].todok().items() if k==j)/s.sqrt(abs(model[3][j,j]))
        column_sums.append(value)
    assert max(column_sums)==2*tau
# Finite beta isomorphisms must not be promoted to cut-l1 self-duality.
# A coarse vacuum observer pulls back to m unit observations: l-infinity norm1,
# but l1 norm m. This is the exact growing-multiplicity hostile.
for multiplicity in range(1,17):
    observer=[1]*multiplicity
    assert max(map(abs,observer))==1 and sum(map(abs,observer))==multiplicity

# Multiplication at one coefficient interface, with independently generated current.
def normalization(n):
    ws=words(n);raw=tuple(product(ws,repeat=2));idx={w:i for i,w in enumerate(ws)}
    fibers={w:[] for w in ws};entries={};t_entries={}
    gr=s.diag(*(weight(u)*weight(v) for u,v in raw));gy=s.diag(*(weight(w) for w in ws))
    for j,(u,v) in enumerate(raw):
        if len(u+v)>n:t_entries[j,j]=-weight(u)*weight(v)
        else:entries[idx[u+v],j]=1;fibers[u+v].append(j)
    for w,js in fibers.items():
        for i,j in product(js,repeat=2):
            if len(raw[i][0])!=len(raw[j][0]):t_entries[i,j]=weight(w)
    m=s.SparseMatrix(len(ws),len(raw),entries)
    current=s.SparseMatrix(len(raw),len(raw),t_entries)
    assert gr+current==m.H*gy*m
    return ws,raw,m,current,gr,gy
nl,nh=normalization(1),normalization(2)
py,pu=projection(nl[0],nh[0]),projection(nl[1],nh[1])
assert py*nh[2]==nl[2]*pu
# Capacity current is negative of the discarded orthogonal degree blocks.
def loss(proj,gram):
    kept={j for i,j in proj.todok()}
    return s.SparseMatrix(gram.rows,gram.cols,{(j,j):-gram[j,j] for j in range(gram.rows) if j not in kept})
lu,ly=loss(pu,nh[4]),loss(py,nh[5])
assert pu.H*nl[4]*pu==nh[4]+lu
assert py.H*nl[5]*py==nh[5]+ly
assert lu+pu.H*nl[3]*pu==nh[3]+nh[2].H*ly*nh[2]
# Fixed total grades stabilize once every buffer fits that grade.
for degree in range(3):
    for component in (0,1):
        def grade(key):
            if component==0:
                u,k,v=key;return len(u)+len(v)+(k!='omega')
            _,u,v=key;return len(u)+len(v)
        small=seam(degree)[component];large=seam(degree+1)[component]
        assert {k for k in small if grade(k)==degree}=={k for k in large if grade(k)==degree}
# Compatible formal inputs need not have finite weighted Hilbert norm.
for n in range(7):
    coeff={k:factorial(k) for k in range(n+1)}
    next_coeff={k:factorial(k) for k in range(n+2)}
    assert coeff=={k:v for k,v in next_coeff.items() if k<=n}
k=s.symbols('k',integer=True,nonnegative=True);alpha=s.symbols('alpha',positive=True)
assert s.simplify(s.factorial(k+1)*alpha**(k+1)/(s.factorial(k)*alpha**k))==(k+1)*alpha
result={'schema':'marici.grothendieck.capacity-bonding-relative-boundary.v1','passed':True,
        'capacity_pair':[1,2],'direct_inclusion_defect_rank':16,
        'checks':{'inverse_projection_is_chain_map':True,'direct_inclusion_has_top_degree_defect':True,
                  'defect_lands_in_capacity_kernel':True,'green_dual_inclusion_is_chain_map':True,
                  'normalization_commutes_with_truncation':True,
                  'collision_loss_currents_satisfy_capacity_square':True,
                  'fixed_total_grade_stabilizes':True,
                  'fixed_depth_cut_l1_differential_bound':True,
                  'cut_l1_dual_requires_cut_l_infinity':True,
                  'formal_compatibility_does_not_imply_analytic_summability':True},
        'scope':'Exact finite word/seam fixtures. General formal completion and topology statements are proved in the companion note. No infinite-packet or norm-convergent completion is inferred.'}
p=ROOT/'research/grothendieck/results/capacity-bonding-relative-boundary.json'
p.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
