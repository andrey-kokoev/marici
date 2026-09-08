#!/usr/bin/env python3
"""Mixed connector source-variation audit.

Includes the prior exact target comparison as a negative control.

Standard library only. All matrix identities are integral Laurent-polynomial
identities. The relation to stabilizer cochains is rational; no integral
E-infinity formality, full Artin equivalence, or physical readout is asserted.

Run: python check_mixed_normal_chern_comparison.py
The certificate is written beside this script.
"""
from __future__ import annotations
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path
import hashlib
import json

CHECKS = Counter()
ZERO = (0,) * 18

def check(ok, group, detail=''):
    CHECKS[group] += 1
    if not ok:
        raise AssertionError(f'{group}: {detail}')

def mon_at(powers):
    out = [0] * 18
    for i, n in powers.items():
        out[i] += n
    return tuple(out)

def madd(a, b):
    return tuple(x+y for x,y in zip(a,b))

def add(out, i, m, c):
    out[i,m] += c
    if out[i,m] == 0:
        del out[i,m]

def vec(i, m=ZERO, c=1):
    return {(i,m):c} if c else {}

def plus(*vectors):
    out = defaultdict(int)
    for v in vectors:
        for (i,m),c in v.items():
            add(out,i,m,c)
    return dict(out)

def scaled(v, c=1, m=ZERO):
    return {(i,madd(n,m)):c*a for (i,n),a in v.items() if c*a}

def apply(op, v):
    out = defaultdict(int)
    for (i,m),c in v.items():
        for (j,n),a in op(i).items():
            add(out,j,madd(m,n),c*a)
    return dict(out)

def subst_zero(v, coords):
    return {key:c for key,c in v.items() if all(key[1][k] == 0 for k in coords)}

def invert_q(v, coord):
    out = {}
    for (i,m),a in v.items():
        n=list(m); n[coord] = -n[coord]
        out[i,tuple(n)]=a
    return out

def tensor(v,w):
    out=defaultdict(int)
    for (i,m),a in v.items():
        for (j,n),b in w.items():
            add(out,(i,j),madd(m,n),a*b)
    return dict(out)

# Local graph cochains: vertices h,b; edges e_D,e_1.
# delta = [[-1,1],[-1,q]]. Minimal cochains: [R --q-1--> R].
def graph_ops(qcoord):
    q=mon_at({qcoord:1}); qi=mon_at({qcoord:-1})
    def dg(i):
        return plus(vec(2,c=-1),vec(3,c=-1)) if i==0 else plus(vec(2),vec(3,q)) if i==1 else {}
    def dk(i):
        return plus(vec(1,q),vec(1,c=-1)) if i==0 else {}
    def J(i): return plus(vec(0),vec(1)) if i==0 else vec(3)
    def P(i): return vec(0) if i==0 else vec(1,q,-1) if i==2 else vec(1) if i==3 else {}
    def H(i): return vec(1) if i==2 else {}
    def RG(i): return vec(0) if i==0 else vec(1,qi) if i==1 else vec(3) if i==2 else vec(2)
    def RK(i): return vec(0) if i==0 else vec(1,q,-1)
    def eta(i): return vec(1) if i==1 else {}
    return dg,dk,J,P,H,RG,RK,eta

def verify_local_graphs():
    for qcoord in (0,1):
        dg,dk,J,P,H,RG,RK,eta=graph_ops(qcoord)
        semig=lambda v:apply(RG,invert_q(v,qcoord))
        semik=lambda v:apply(RK,invert_q(v,qcoord))
        semieta=lambda v:apply(eta,invert_q(v,qcoord))
        for i in range(4):
            v=vec(i)
            check(apply(dg,apply(dg,v))=={},'twisted_graph')
            check(plus(apply(dg,apply(H,v)),apply(H,apply(dg,v)))==plus(v,scaled(apply(J,apply(P,v)),-1)), 'graph_contraction')
            check(apply(P,apply(dg,v))==apply(dk,apply(P,v)), 'graph_chain_maps')
            check(semig(semig(v))==v,'reflection_square')
            check(apply(dg,semig(v))==semig(apply(dg,v)), 'reflection_chain_maps')
        for i in range(2):
            v=vec(i)
            check(apply(P,apply(J,v))==v,'graph_retract')
            check(apply(dg,apply(J,v))==apply(J,apply(dk,v)),'graph_chain_maps')
            check(semik(semik(v))==v,'reflection_square')
            check(apply(dk,semik(v))==semik(apply(dk,v)),'reflection_chain_maps')
            lhs=plus(semig(apply(J,v)),scaled(apply(J,semik(v)),-1))
            rhs=plus(apply(dg,semieta(v)),semieta(apply(dk,v)))
            check(lhs==rhs,'reflection_homotopy')
            check(plus(semig(semieta(v)),semieta(semik(v)))=={},'reflection_higher_coherence')
    # Tensor both graph contractions, without truncating any of the 16 states.
    g1,k1,j1,p1,h1,*_=graph_ops(0)
    g2,k2,j2,p2,h2,*_=graph_ops(1)
    dgdeg=lambda i:0 if i<2 else 1
    dkdeg=lambda i:i
    def dG(pair):
        i,j=pair
        return plus(tensor(g1(i),vec(j)),scaled(tensor(vec(i),g2(j)),(-1)**dgdeg(i)))
    def dK(pair):
        i,j=pair
        return plus(tensor(k1(i),vec(j)),scaled(tensor(vec(i),k2(j)),(-1)**dkdeg(i)))
    def J(pair): return tensor(j1(pair[0]),j2(pair[1]))
    def P(pair): return tensor(p1(pair[0]),p2(pair[1]))
    def H(pair):
        i,j=pair
        jp=apply(j1,p1(i))
        return plus(tensor(h1(i),vec(j)),scaled(tensor(jp,h2(j)),(-1)**dgdeg(i)))
    for i in range(4):
        for j in range(4):
            v=vec((i,j))
            check(apply(dG,apply(dG,v))=={},'two_normal_graph')
            check(plus(apply(dG,apply(H,v)),apply(H,apply(dG,v)))==plus(v,scaled(apply(J,apply(P,v)),-1)), 'two_normal_contraction')
            check(apply(P,apply(dG,v))==apply(dK,apply(P,v)), 'two_normal_chain_maps')
    for i in range(2):
        for j in range(2):
            v=vec((i,j))
            check(apply(P,apply(J,v))==v,'two_normal_retract')
            check(apply(dG,apply(J,v))==apply(J,apply(dK,v)), 'two_normal_chain_maps')

# Koszul exterior operators. For this test c1,c2 use slots 2,3 and u1,u2 slots4,5.
def wedge(mask, i):
    if mask & (1<<i): return {}
    return vec(mask|(1<<i),c=(-1)**((mask & ((1<<i)-1)).bit_count()))

def contract(mask, i):
    if not mask & (1<<i): return {}
    return vec(mask & ~(1<<i),c=(-1)**((mask & ((1<<i)-1)).bit_count()))

def verify_koszul():
    c1=mon_at({2:1});c2=mon_at({3:1});u1=mon_at({4:1});u2=mon_at({5:1})
    dC=lambda m:plus(scaled(contract(m,0),m=c1),scaled(contract(m,1),m=c2))
    dU=lambda m:plus(scaled(wedge(m,0),m=u1),scaled(wedge(m,1),m=u2))
    N1=lambda m:scaled(wedge(m,0),m=c2)
    N2=lambda m:scaled(wedge(m,1),m=c1)
    T=lambda m:apply(lambda k:wedge(k,0),wedge(m,1))
    total=lambda m:plus(dC(m),dU(m))
    for m in range(4):
        v=vec(m)
        check(apply(dC,apply(dC,v))=={},'chern_Koszul')
        check(apply(dU,apply(dU,v))=={},'monodromy_Koszul')
        for Ni in (N1,N2):
            check(plus(apply(dC,apply(Ni,v)),apply(Ni,apply(dC,v)))==scaled(v,m=madd(c1,c2)),'chern_primary_nullhomotopies')
        check(plus(apply(N2,v),scaled(apply(N1,v),-1))==plus(apply(dC,apply(T,v)),scaled(apply(T,apply(dC,v)),-1)), 'chern_second_homotopy')
        check(plus(apply(dU,apply(T,v)),scaled(apply(T,apply(dU,v)),-1))=={},'monodromy_secondary_operator')
        curvature=plus(scaled(v,m=madd(c1,u1)),scaled(v,m=madd(c2,u2)))
        check(apply(total,apply(total,v))==curvature,'joint_differential_curvature')
        for i,ui in ((0,u1),(1,u2)):
            Ii=lambda x,i=i:contract(x,i)
            anticom=plus(apply(dU,apply(Ii,v)),apply(Ii,apply(dU,v)))
            check(anticom==scaled(v,m=ui),'supported_residue_obstruction')
            check(subst_zero(anticom,(4+i,))=={},'supported_residue')
        top_res=lambda x:vec(0) if x==3 else {}
        check(subst_zero(apply(top_res,apply(dU,v)),(4,5))=={},'double_supported_residue')
    check(T(0)==vec(3),'secondary_unit')
    check(subst_zero(N1(0),(2,3))=={} and subst_zero(N2(0),(2,3))=={},'augmented_primary_nullhomotopies')

# Actual finite and Cech K6 coefficient complex, copied structurally from the source.
D=tuple((a,b) for a in range(6) for b in range(a+1,6) if b-a!=1 and (a,b)!=(0,5))
DI={a:i for i,a in enumerate(D)}
A=(0,3); B=(1,3)
VP=frozenset(((1,3),(1,5),(3,5)))
VM=frozenset(((0,2),(0,4),(2,4)))
LONGS=frozenset(a for a in D if a[1]-a[0]==3)

def crosses(a,b):
    if set(a)&set(b):return False
    return (a[0]<b[0]<a[1]) != (a[0]<b[1]<a[1])

def subsets(s):
    s=sorted(s)
    return [frozenset(t) for n in range(len(s)+1) for t in combinations(s,n)]

FACES=[frozenset(t) for n in range(4) for t in combinations(D,n) if all(not crosses(a,b) for a,b in combinations(t,2))]
CELLS=[(s,h) for s in FACES for h in subsets(s)]
INDEX={x:i for i,x in enumerate(CELLS)}
VERTICES={i for i,(s,h) in enumerate(CELLS) if s in (VP,VM)}
QCELLS={i for i,(s,h) in enumerate(CELLS) if not s or len(s)==1 and s<=LONGS}
ADJ=defaultdict(list)
for i,(s,h) in enumerate(CELLS):
    for a in D:
        if a not in s and len(s)<3 and all(not crosses(a,b) for b in s):
            ADJ[i].append((INDEX[s|{a},h],a,'radial',(-1)**sum(b<a for b in s)))
    for p,a in enumerate(sorted(h)):
        ADJ[i].append((INDEX[s,h-{a}],a,'normal',(-1)**(3-len(s)+p)))

def local_mono(x=None, us=None):
    z={}
    if x is not None:z[DI[x]]=1
    for a,k in (us or {}).items():z[9+DI[a]]=k
    return mon_at(z)

def degree(i):
    s,h=CELLS[i]
    return 3-len(s)+len(h)

def boundary(i,cech=False,endpoint_relative=False):
    out={}
    for j,a,kind,sign in ADJ[i]:
        if endpoint_relative and j in VERTICES:continue
        m=local_mono(x=a,us={a:-1}) if cech and kind=='radial' else local_mono(x=a) if kind=='radial' else ZERO if cech else local_mono(us={a:1})
        out[j,m]=sign
    return out

def localization(i):
    s,h=CELLS[i]
    return local_mono(us={a:-1 for a in s-h})

def Lambda(i): return vec(i,localization(i))

def cap(i,a):
    s,h=CELLS[i]
    return vec(INDEX[s,h-{a}],c=(-1)**sum(b<a for b in h)) if a in h else {}

def T(i,cech):
    s,h=CELLS[i]
    if not {A,B}<=h:return {}
    out=apply(lambda j:cap(j,B),cap(i,A))
    return scaled(out,m=local_mono(us={A:-1,B:-1})) if cech else out

def H(i):
    s,h=CELLS[i]
    if A not in s-h or B not in h:return {}
    return scaled(cap(i,B),(-1)**(3-len(s)),local_mono(us={A:-1,B:-1}))

def radial_defect(i):
    s,h=CELLS[i]
    if A in s or B not in h or len(s)>=3 or any(crosses(A,b) for b in s):return {}
    sign=(-1)**(sum(b<A for b in s)+3-len(s)-1+sum(b<B for b in h))
    return vec(INDEX[s|{A},h-{B}],local_mono(x=A,us={A:-2,B:-1}),sign)

def kappa(i):
    return {key:c for key,c in boundary(i,True).items() if key[0] in VERTICES}

def legal(m,target):
    s,h=CELLS[target]
    return min(m[:9])>=0 and all(m[9+DI[a]]>=0 or a in s-h for a in D)

def verify_loaded():
    check(len(CELLS)==215 and len(VERTICES)==16 and len(QCELLS)==7,'source_census')
    check(sum(map(len,ADJ.values()))==522,'source_census')
    for i in range(215):
        for cech in (False,True):
            d=lambda j:boundary(j,cech)
            check(apply(d,d(i))=={},'loaded_d_squared')
            check(plus(apply(d,T(i,cech)),scaled(apply(lambda j:T(j,cech),d(i)),-1))=={},'secondary_chain_map')
        check(apply(lambda j:boundary(j,True),Lambda(i))==apply(Lambda,boundary(i,False)), 'finite_Cech_comparison')
        check(apply(Lambda,T(i,False))==apply(lambda j:T(j,True),Lambda(i)), 'secondary_comparison_naturality')
        lhs=plus(apply(lambda j:boundary(j,True),H(i)),apply(H,boundary(i,True)))
        check(lhs==plus(T(i,True),radial_defect(i)), 'global_radial_defect')
        for op in (lambda j:T(j,True),H,radial_defect):
            for (j,m),c in op(i).items():
                check(legal(m,j),'allowed_coefficients')
                check((CELLS[i][0]-CELLS[i][1]) <= (CELLS[j][0]-CELLS[j][1]), 'source_localization_linearity')
                check(j not in QCELLS and j not in VERTICES,'framed_outputs')
            check(apply(kappa,op(i))=={},'endpoint_connector_compatibility')
            if i in VERTICES|QCELLS:
                check(op(i)=={},'fixed_frame_inputs')
    star={i for i,(s,h) in enumerate(CELLS) if {A,B}<=s}
    check(len(star)==20,'mixed_star')
    for i in star:
        check(radial_defect(i)=={},'local_primitive')
        check(all(j in star for j,*_ in ADJ[i]),'star_subcomplex')
    counts=[sum(bool(op(i)) for i in range(215)) for op in (lambda j:T(j,True),H,radial_defect)]
    check(counts==[5,5,5],'operator_columns')
    return star,counts

# Genuine derived-Hom test: bounded-free finite E is the source;
# the endpoint-relative Cech complex is the target. Homogeneous weight is
# -epsilon_(u03)-epsilon_(u13). Source weight = -X_S + u_H;
# target weight = -X_S + u_S. Every homogeneous entry is one Laurent monomial.
def hom_basis(n):
    out=[]
    for i,(s,h) in enumerate(CELLS):
        if i in VERTICES:continue
        for j,(t,k) in enumerate(CELLS):
            if j in VERTICES or degree(j)-degree(i)!=-n:continue
            powers=[int(a in t)-int(a in s) for a in D]
            powers += [int(a in h)-int(a in t)-int(a in (A,B)) for a in D]
            powers=tuple(powers)
            if legal(powers,j):out.append((i,j,powers))
    return out

def zeros(m,n):return [[0]*n for _ in range(m)]
def imatmul(a,b):
    if not a:return []
    if not b:return zeros(len(a),0)
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]

def hom_matrix(n,ss,tt):
    rows={v:i for i,v in enumerate(tt)}
    out=zeros(len(tt),len(ss))
    for col,(source,target,m) in enumerate(ss):
        def op(i):return vec(target,m) if i==source else {}
        sources={source}|{i for i in range(215) if any(j==source for j,*_ in ADJ[i])}
        for i in sources-VERTICES:
            value=plus(apply(lambda j:boundary(j,True,True),op(i)),scaled(apply(op,boundary(i,False,True)),-(-1)**n))
            for (j,mo),c in value.items():
                check((i,j,mo) in rows,'Hom_homogeneity')
                out[rows[i,j,mo]][col]+=c
    return out

def unit_smith(matrix):
    """Unimodular row/column reduction; rejects any nonunit residual block."""
    a=[list(r) for r in matrix]
    m=len(a); n=len(a[0]) if m else 0; k=0
    while k<min(m,n):
        pivot=next(((i,j) for i in range(k,m) for j in range(k,n) if abs(a[i][j])==1),None)
        if pivot is None:
            check(all(a[i][j]==0 for i in range(k,m) for j in range(k,n)), 'Smith_unit_reduction')
            break
        i,j=pivot; a[k],a[i]=a[i],a[k]
        for row in a:row[k],row[j]=row[j],row[k]
        if a[k][k]<0:a[k]=[-x for x in a[k]]
        for i in range(m):
            if i==k:continue
            v=a[i][k]
            for j in range(n):a[i][j]-=v*a[k][j]
        for j in range(n):
            if j==k:continue
            v=a[k][j]
            for i in range(m):a[i][j]-=v*a[i][k]
        k+=1
    check(all(a[i][j]==int(i==j and i<k) for i in range(m) for j in range(n)), 'Smith_diagonal')
    return k

def encode_cell(i):
    s,h=CELLS[i]
    name=lambda a:''.join(map(str,a))
    return {'index':i,'face':[name(a) for a in sorted(s)],'marks':[name(a) for a in sorted(h)]}

def encode_mono(m):
    return {('X_' if j<9 else 'u_')+''.join(map(str,D[j%9])):p for j,p in enumerate(m) if p}

def encode_hom(key):
    i,j,m=key
    return {'source':encode_cell(i),'target':encode_cell(j),'monomial':encode_mono(m)}

def verify_derived_hom():
    bases=[hom_basis(n) for n in range(4)]
    check(list(map(len,bases))==[5,24,36,16],'Hom_dimensions')
    maps=[hom_matrix(n,bases[n],bases[n+1]) for n in range(3)]
    for left,right in zip(maps[1:],maps[:-1]):
        check(all(x==0 for row in imatmul(left,right) for x in row),'Hom_d_squared')
    ranks=[unit_smith(m) for m in maps]
    check(ranks==[5,19,16],'Hom_ranks')
    cohom=[len(bases[n])-(ranks[n-1] if n else 0)-(ranks[n] if n<3 else 0) for n in range(4)]
    check(cohom==[0,0,1,0],'Hom_integral_cohomology')
    rows={key:i for i,key in enumerate(bases[2])}
    t=[0]*len(bases[2])
    for i in range(215):
        if i in VERTICES:continue
        for (j,m),c in apply(lambda z:T(z,True),Lambda(i)).items():t[rows[i,j,m]]=c
    check(all(sum(x*y for x,y in zip(row,t))==0 for row in maps[2]),'secondary_derived_cycle')
    target=INDEX[frozenset((A,B)),frozenset()]
    srcs=[INDEX[frozenset(),frozenset()],INDEX[frozenset((A,)),frozenset((A,))],INDEX[frozenset((B,)),frozenset((B,))],INDEX[frozenset((A,B)),frozenset((A,B))]]
    ell=[0]*len(t)
    for sign,i in zip((-1,1,1,1),srcs):
        hits=[k for k,(s,j,m) in enumerate(bases[2]) if s==i and j==target]
        check(len(hits)==1,'obstruction_covector_support')
        ell[hits[0]]=sign
    check(all(sum(ell[i]*maps[1][i][j] for i in range(len(ell)))==0 for j in range(len(bases[1]))),'obstruction_kills_every_homotopy')
    check(sum(a*b for a,b in zip(ell,t))==1,'primitive_nonzero_derived_class')
    for n in (0,1,2,3):
        for i,j,m in bases[n]:
            check({A,B} <= CELLS[j][0] and not ({A,B}&CELLS[j][1]),'Hom_target_in_mixed_star')
    return {'dimensions':list(map(len,bases)),'differential_ranks':ranks,'all_nonzero_Smith_factors':1,'cohomology_ranks':cohom,'degree_two_free_rank':1,'obstruction_covector':[dict(encode_hom(bases[2][i]),coefficient=v) for i,v in enumerate(ell) if v],'covector_evaluation_on_T_Lambda':1,'hom_bases':[[encode_hom(v) for v in b] for b in bases],'differential_matrices':maps,'T_Lambda_coordinates':t}

# Further audit: coefficient connections, source normal variation, and blowdown.

def derivative(v, a):
    """Differentiate coefficients, not basis vectors; monodromy u_a coordinate."""
    k = 9 + DI[a]
    out = defaultdict(int)
    for (i, m), c in v.items():
        n = m[k]
        if n:
            mo = list(m); mo[k] -= 1
            add(out, i, tuple(mo), c*n)
    return dict(out)


def connection(v, a):
    """The coefficient connection on legal Cech modules.

    On a scalar monomial times [F,H], nabla_a acts with coefficient
    m_a + 1_{a in F-H}, and lowers the u_a exponent by one. It is a
    connection (Leibniz), not an R-linear endomorphism.
    """
    k = 9 + DI[a]
    out = defaultdict(int)
    for (i, m), c in v.items():
        f, h = CELLS[i]
        n = m[k] + int(a in f-h)
        if n:
            mo = list(m); mo[k] -= 1
            add(out, i, tuple(mo), c*n)
    return dict(out)


def Jnormal(i, a, cech=True):
    f, h = CELLS[i]
    m = local_mono(us={a:-1}) if cech else ZERO
    return scaled(cap(i, a), (-1)**(3-len(f)), m)


def rho(v):
    """Target restriction E -> Q direct-sum V[1], on nonendpoint inputs.

    Boundary indices are tagged ('q',cell) or ('v',cell). The sign of
    the shifted endpoint differential is handled in dboundary.
    """
    out=defaultdict(int)
    for (i,m),c in v.items():
        if i in QCELLS:
            add(out, ('q',i), m, c)
        for (j,n),b in boundary(i,True).items():
            if j in VERTICES:
                add(out, ('v',j), madd(m,n),c*b)
    return dict(out)


def dboundary(v):
    out=defaultdict(int)
    for ((kind,i),m),c in v.items():
        for (j,n),b in boundary(i,True).items():
            if (kind=='q' and j in QCELLS) or (kind=='v' and j in VERTICES):
                add(out,(kind,j),madd(m,n),c*b*(1 if kind=='q' else -1))
    return dict(out)


def connection_boundary(v,a):
    out=defaultdict(int)
    for ((kind,i),m),c in v.items():
        for (j,n),b in connection(vec(i,m,c),a).items():
            add(out,(kind,j),n,b)
    return dict(out)


def Jboundary(v,a):
    out=defaultdict(int)
    for ((kind,i),m),c in v.items():
        for (j,n),b in Jnormal(i,a).items():
            if (kind=='q' and j in QCELLS) or (kind=='v' and j in VERTICES):
                add(out,(kind,j),madd(m,n),c*b*(1 if kind=='q' else -1))
    return dict(out)


def verify_connections():
    de=lambda i:boundary(i,True,True)
    for i in range(215):
        for a in D:
            # Unit basis suffices for the R-linear connection commutator.
            v=vec(i)
            lhs=plus(connection(boundary(i,True),a),scaled(apply(lambda j:boundary(j,True),connection(v,a)),-1))
            check(lhs==Jnormal(i,a),'connection_commutator')
            check(plus(apply(lambda j:boundary(j,True),Jnormal(i,a)),apply(lambda j:Jnormal(j,a),boundary(i,True)))=={},'normal_variation_closed')
            check(connection(Lambda(i),a)=={},'horizontal_finite_Cech_basis')
            # Laurent and polynomial coefficients, including legal negative powers.
            f,h=CELLS[i]
            powers=(-3,-1,0,1,3) if a in f-h else (0,1,3)
            for power in powers:
                v=vec(i,local_mono(us={a:power}))
                check(all(legal(m,j) for (j,m) in connection(v,a)),'connection_coefficient_legality')
                base=connection(vec(i),a)
                rhs=plus(scaled(base,m=local_mono(us={a:power})),derivative(v,a))
                check(connection(v,a)==rhs,'connection_Leibniz')
            if i not in VERTICES:
                check(rho(de(i))==dboundary(rho(vec(i))),'boundary_chain_map')
                check(rho(connection(vec(i),a))==connection_boundary(rho(vec(i)),a),'boundary_connection_naturality')
                check(rho(Jnormal(i,a))==Jboundary(rho(vec(i)),a),'boundary_variation_naturality')
        check(apply(lambda j:Jnormal(j,B),Jnormal(i,A))==T(i,True),'mixed_operator_factorization')
        check(connection(connection(vec(i),A),B)==connection(connection(vec(i),B),A),'connection_flatness')
    # The short b-coordinate is absent throughout Q; long a absent at V.
    for i in QCELLS:
        check(Jnormal(i,B)=={},'Q_short_variation_zero')
    for i in VERTICES:
        check(A not in CELLS[i][0],'endpoint_long_coordinate_absent')
        check(connection(vec(i),A)=={},'endpoint_long_basis_horizontal')


# Complete integral Tate window; coefficients and external Cartier states
# are kept separate. This is the module in source Entry 417, not a
# reconstruction of the missing matrix of the spatial connector.
SBASE=(('z',0),)+tuple(('r',i) for i in range(3))+tuple(('t',i) for i in range(3))+(('o',0),)
SINDEX={x:i for i,x in enumerate(SBASE)}
SDEG=[0,1,1,1,2,2,2,3]


def ds(i):
    kind,k=SBASE[i]
    if kind=='r':return vec(SINDEX['z',0])
    if kind=='t':return plus(vec(SINDEX['r',k]),vec(SINDEX['r',(k+1)%3],c=-1))
    if kind=='o':return plus(*(vec(SINDEX['t',j]) for j in range(3)))
    return {}


def source_h(i):
    kind,k=SBASE[i]
    if kind=='z':return vec(SINDEX['r',0])
    if kind=='r' and k==1:return vec(SINDEX['t',0],c=-1)
    if kind=='r' and k==2:return plus(vec(SINDEX['t',0],c=-1),vec(SINDEX['t',1],c=-1))
    if kind=='t' and k==2:return vec(SINDEX['o',0])
    return {}


def verify_horizontal_source():
    for i in range(8):
        check(apply(ds,ds(i))=={},'Tate_d_squared')
        check(plus(apply(ds,source_h(i)),apply(source_h,ds(i)))==vec(i),'Tate_contraction_control')
        for a in (A,B):
            check(derivative(ds(i),a)=={},'Tate_normal_flatness')
    # Tensor all eight independent Cartier states, without using them as
    # target face-normal circles or adding exterior degree to chain degree.
    for i in range(8):
        for state in range(8):
            for a in (A,B):
                check(derivative(ds(i),a)=={},'all_Cartier_states_source_flatness')
            for j in range(3):
                before={(k,state):c for (k,m),c in ds(i).items()}
                check(all(st==state for k,st in before),'external_Cartier_level_unchanged')
    # Arbitrary chain maps from a contractible source are Hom boundaries.
    # Check each elementary degree -1 seed, with several polynomial and
    # legal Laurent coefficients. The theorem itself is a symbolic identity.
    de=lambda i:boundary(i,True,True)
    tested=0; endpoint_horizontal=0
    nonzero=0
    for si in range(8):
        for ti in range(215):
            if ti in VERTICES or degree(ti)!=SDEG[si]+1:
                continue
            f,h=CELLS[ti]
            mons=[ZERO,local_mono(us={A:1}),local_mono(us={A:2,B:1})]
            if A in f-h:
                mons.append(local_mono(us={A:-2}))
            for mon in mons:
                seed=lambda i,si=si,ti=ti,mon=mon:vec(ti,mon) if i==si else {}
                kap={i:plus(apply(de,seed(i)),apply(seed,ds(i))) for i in range(8)}
                aa={i:connection(kap[i],A) for i in range(8)}
                hom={i:apply(lambda j:Jnormal(j,B),aa[i]) for i in range(8)}
                endpoint_ok=all(not derivative({(j,m):c for ((kind,j),m),c in rho(kap[i]).items() if kind=='v'},A) for i in range(8))
                endpoint_horizontal+=int(endpoint_ok)
                tested+=1
                for i in range(8):
                    check(apply(de,kap[i])==apply(lambda j:kap[j],ds(i)),'sample_connector_chain_map')
                    check(plus(apply(de,aa[i]),scaled(apply(lambda j:aa[j],ds(i)),-1))==scaled(apply(lambda j:Jnormal(j,A),kap[i]),-1),'source_flat_variation_identity')
                    lhs=plus(apply(de,hom[i]),apply(lambda j:hom[j],ds(i)))
                    rhs=apply(lambda j:T(j,True),kap[i])
                    check(lhs==rhs,'horizontal_source_composite_nullhomotopy')
                    nonzero+=int(bool(rhs))
                    nr=rho(hom[i])
                    boundary_aa=connection_boundary(rho(kap[i]),A)
                    check(nr==Jboundary(boundary_aa,B),'composite_homotopy_boundary_formula')
                    if endpoint_ok:
                        check(nr=={},'horizontal_endpoint_frame_preserved')
                    for (j,m) in hom[i]:
                        check(legal(m,j),'composite_homotopy_coefficient_legality')
    return {'elementary_homotopy_seed_maps':tested,
            'seed_maps_with_long_horizontal_endpoint_values':endpoint_horizontal,
            'nonzero_composite_columns_nullified':nonzero,
            'scope':'all-degree proof for any R-linear connector with flat source; finite coefficient checks are not the missing spatial connector matrix'}


# Local toric blowdown comparison on the open two-normal torus.
# q_E=q_a*q_b, so u_E=u_a+u_b+u_a*u_b. Geometric normal coordinates,
# monodromy parameters, occurrence variables, and Chern classes are separate.
def vmul_poly(v, p):
    return plus(*(scaled(v,c,m) for m,c in p.items()))


def poly_var(a):return {local_mono(us={a:1}):1}
PONE={ZERO:1}
PA=poly_var(A);PB=poly_var(B)
PQA={ZERO:1,**PA};PQB={ZERO:1,**PB}
PE={**PA,**PB,local_mono(us={A:1,B:1}):1}


def normal_d(p0,p1):
    return lambda mask:plus(vmul_poly(contract(mask,0),p0),vmul_poly(contract(mask,1),p1))


def FA(mask):
    if mask==1:return plus(vec(1),vmul_poly(vec(2),PQA))
    return vec(mask)


def FAinv(mask):
    if mask==1:return plus(vec(1),scaled(vmul_poly(vec(2),PQA),-1))
    return vec(mask)


def FB(mask):
    if mask==2:return plus(vmul_poly(vec(1),PQB),vec(2))
    return vec(mask)


def FBinv(mask):
    if mask==2:return plus(scaled(vmul_poly(vec(1),PQB),-1),vec(2))
    return vec(mask)


def verify_blowdown_normal_packet():
    dt=normal_d(PA,PB)
    da=normal_d(PE,PB)
    db=normal_d(PA,PE)
    tt=lambda m:apply(lambda x:contract(x,1),contract(m,0))
    data={}
    for name,dsource,F,inv in [('E_b',da,FA,FAinv),('a_E',db,FB,FBinv)]:
        jaS=lambda m,dsource=dsource:derivative(dsource(m),A)
        jbS=lambda m,dsource=dsource:derivative(dsource(m),B)
        aa=lambda m,F=F:derivative(F(m),A)
        ab=lambda m,F=F:derivative(F(m),B)
        hh=lambda m:plus(apply(lambda x:contract(x,1),aa(m)),scaled(apply(ab,jaS(m)),-1))
        for mask in range(4):
            v=vec(mask)
            check(apply(dt,F(mask))==apply(F,dsource(mask)),'blowdown_normal_chain_map')
            check(apply(inv,F(mask))==v and apply(F,inv(mask))==v,'blowdown_normal_inverse')
            check(F(3)==vec(3),'blowdown_top_orientation')
            check(apply(tt,F(mask))==apply(F,tt(mask)),'geometric_double_normal_cap')
            lhs=plus(apply(dt,hh(mask)),apply(hh,dsource(mask)))
            rhs=plus(apply(tt,F(mask)),scaled(apply(F,apply(jbS,jaS(mask))),-1))
            check(lhs==rhs,'source_variation_double_naturality')
            # All three complexes specialize to zero differential at resonance.
            check(subst_zero(dsource(mask),(9+DI[A],9+DI[B]))=={},'blowdown_resonant_differential')
            check(subst_zero(dt(mask),(9+DI[A],9+DI[B]))=={},'blowdown_resonant_differential')
        check(subst_zero(apply(tt,F(3)),(9+DI[A],9+DI[B]))==vec(0),'nonzero_resonant_composite')
        data[name]={'top_map_coefficient':1,
                    'source_JbJa_top':[{**encode_mono(m),'coefficient':c} for (i,m),c in apply(jbS,jaS(3)).items()],
                    'homotopy_columns':{str(mask):[{'target_mask':i,'monomial':encode_mono(m),'coefficient':c} for (i,m),c in hh(mask).items()] for mask in range(4)}}
    change=lambda m:apply(FBinv,FA(m))
    for mask in range(4):
        check(apply(db,change(mask))==apply(change,da(mask)),'two_chart_transition_chain_map')
        check(apply(FB,change(mask))==FA(mask),'two_chart_overlap_agreement')
    # Refuting deletion of the physical source's a-dependence.
    check(derivative(da(1),A)==vmul_poly(vec(0),PQB),'actual_exceptional_source_derivative')
    check(derivative(da(1),A)!={},'exceptional_source_not_flat')
    return data


def normal_change_cell(i, chart):
    """Exterior extension of the normal chart matrices on a closed mixed star.

    The index a denotes the exceptional-normal slot in chart E_b; in chart
    a_E the b slot is exceptional. This is a local normal change of basis,
    not an assertion about the global support map of the connector.
    """
    face,marks=CELLS[i]
    if chart=='E_b':
        old,new,pol=A,B,PQA
    else:
        old,new,pol=B,A,PQB
    out=vec(i)
    if old in marks and new not in marks:
        others=marks-{old}
        sign=(-1)**sum(min(old,new)<c<max(old,new) for c in others)
        changed=INDEX[face,others|{new}]
        out=plus(out,scaled(vmul_poly(vec(changed),pol),sign))
    return out


def star_normal_d(i,chart):
    out={}
    for j,a,kind,sign in ADJ[i]:
        if kind=='radial':
            term=vec(j,local_mono(x=a),sign)
        else:
            exceptional=(a==A) if chart=='E_b' else (a==B)
            term=scaled(vmul_poly(vec(j),PE if exceptional else poly_var(a)),sign)
        out=plus(out,term)
    return out


def verify_closed_star_connector():
    star=[i for i,(f,h) in enumerate(CELLS) if {A,B}<=f]
    check(len(star)==20,'closed_star_census')
    out={}
    for chart in ('E_b','a_E'):
        change=lambda i,chart=chart:normal_change_cell(i,chart)
        source_d=lambda i,chart=chart:star_normal_d(i,chart)
        kc=lambda i:apply(Lambda,change(i))
        hc=lambda i:apply(H,kc(i))
        tc=lambda i:apply(lambda j:T(j,True),kc(i))
        for i in star:
            check(all(j in star for j,m in source_d(i)),'closed_star_source_support')
            check(apply(source_d,source_d(i))=={},'closed_star_source_d_squared')
            check(apply(lambda j:boundary(j,False),change(i))==apply(change,source_d(i)),'closed_star_normal_comparison')
            check(apply(lambda j:boundary(j,True),kc(i))==apply(kc,source_d(i)),'closed_star_Cech_comparison')
            check(plus(apply(lambda j:boundary(j,True),hc(i)),apply(hc,source_d(i)))==tc(i),'closed_star_composite_nullhomotopy')
            check(rho(hc(i))=={} and rho(tc(i))=={},'closed_star_complete_target_frame')
            check(apply(radial_defect,kc(i))=={},'closed_star_radial_defect_zero')
            for j,m in hc(i):
                check(legal(m,j),'closed_star_homotopy_legality')
        fs=frozenset((A,B))
        local={}
        for marks in subsets(fs):
            i=INDEX[fs,marks]
            local[str(encode_cell(i)['marks'])]={
                'comparison':[{**encode_cell(j),'monomial':encode_mono(m),'coefficient':c} for (j,m),c in kc(i).items()],
                'nullhomotopy':[{**encode_cell(j),'monomial':encode_mono(m),'coefficient':c} for (j,m),c in hc(i).items()],
                'composite':[{**encode_cell(j),'monomial':encode_mono(m),'coefficient':c} for (j,m),c in tc(i).items()]
            }
        out[chart]=local
    rows=[]
    for i in range(215):
        val=radial_defect(i)
        if val:
            rows.append({'input':encode_cell(i),'output':[{'cell':encode_cell(j),'monomial':encode_mono(m),'coefficient':c} for (j,m),c in val.items()]})
    check(len(rows)==5,'full_connector_five_row_reduction')
    return {'star_cells':20,'both_charts_composite':'nullhomotopic in the full closed mixed-face Cech complex',
            'endpoint_Q_homotopy':'identically zero','local_columns':out,'remaining_global_rows':rows}


def new_main():
    # Recheck the earlier target nonvanishing, not merely its rank assertion.
    verify_loaded()
    old_hom=verify_derived_hom()
    verify_connections()
    horizontal=verify_horizontal_source()
    blowdown=verify_blowdown_normal_packet()
    star_connector=verify_closed_star_connector()
    result={
      'schema':'marici.branchA.mixed_connector_normal_variation.v1',
      'source_commit':'d1947b67a60d3e88ba77f4ca60ea02c2a306ee61',
      'mixed_pair':['03','13'],
      'connection':'nabla_a(m e_FH)=(partial_ua m + 1_{a in F-H} m/u_a)e_FH',
      'normal_variation':'J_a=[nabla_a,d]=(-1)^(3-|F|) iota_a/u_a',
      'T':'J_13 J_03',
      'general_naturality':'delta(Jb_target A_a - A_b Ja_source)=T_target kappa-kappa T_source',
      'flat_source_result':'T_target kappa is explicitly nullhomotopic',
      'frame_condition':'zero Q homotopy; endpoint homotopy zero when full endpoint coefficients are independent of u03',
      'target_class_reverified':{'rank':old_hom['degree_two_free_rank'],'detector':old_hom['covector_evaluation_on_T_Lambda']},
      'horizontal_source_tests':horizontal,
      'exceptional_normal_monodromy':'qE=q03*q13; uE=u03+u13+u03*u13',
      'normal_blowdown':blowdown,
      'closed_star_connector':star_connector,
      'local_normal_self_Ext2':'R/(u03,u13), with ordered conormal determinant understood',
      'local_geometric_double_cap_coefficient':1,
      'full_physical_spatial_composite':'NOT IDENTIFIED: the actual loaded source-to-PC diagram map and connection-compatible Gysin transport have not been supplied by the inspected integration checker',
      'not_claimed':['normal-torus local map equals full connector','flat collapsed differential equals raw exceptional differential','nonzero normal-torus cap survives local Cech or global physical Gysin','integral Artin cochain formality'],
      'checks':dict(sorted(CHECKS.items())),
      'total_checks':sum(CHECKS.values()),
      'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    }
    path=Path(__file__).with_name('mixed_connector_normal_variation_certificate.json')
    path.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({key:result[key] for key in ('mixed_pair','total_checks','flat_source_result','local_geometric_double_cap_coefficient','full_physical_spatial_composite')},indent=2))
    print('certificate:',path)

if __name__=='__main__':new_main()
