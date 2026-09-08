#!/usr/bin/env python3
"""Mixed D03/13 monodromy, Koszul, and framed coefficient comparison.

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

def main():
    verify_local_graphs();verify_koszul()
    star,counts=verify_loaded()
    hom=verify_derived_hom()
    operators={}
    for name,op in [('T',lambda i:T(i,True)),('H',H),('radial_defect',radial_defect)]:
        operators[name]=[dict(encode_hom((i,j,m)),coefficient=c) for i in range(215) for (j,m),c in op(i).items()]
    cert={'schema':'marici.branchA.mixed_normal_chern.v1','repository_commit':'d1947b67a60d3e88ba77f4ca60ea02c2a306ee61','mixed_pair':['03','13'],'loaded_cells':215,'generating_arrows':522,'mixed_star_cells':len(star),'operator_columns_T_H_R':counts,'normal_graph_contraction':'verified universally over Z[q03^+-1,q13^+-1]','joint_Chern_monodromy_curvature':'c03*u03+c13*u13','Chern_primary_action_after_augmentation':'zero','derived_secondary_class':'primitive nonzero degree-two class of finite-to-Cech coefficient complexes','physical_connector_readout':'not computed','Artin_stack_six_functor_equivalence':'not asserted','checks':dict(sorted(CHECKS.items())),'total_checks':sum(CHECKS.values()),'Hom':hom,'operators':operators,'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    path=Path(__file__).with_name('mixed_normal_chern_comparison_certificate.json')
    path.write_text(json.dumps(cert,indent=2)+'\n')
    print(json.dumps({k:cert[k] for k in ('loaded_cells','mixed_star_cells','operator_columns_T_H_R','total_checks','derived_secondary_class','physical_connector_readout')},indent=2))
    print('certificate:',path)

if __name__=='__main__':main()
