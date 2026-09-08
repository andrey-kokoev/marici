#!/usr/bin/env python3
"""Exact five-row mixed-action audit over integral Laurent polynomials.

The source matrices are extracted from Marici at commit
  d1947b67a60d3e88ba77f4ca60ea02c2a306ee61.
The universal statements are proved in five_row_physical_action.md.
This program does not construct the missing raw spatial connector.
Python 3.10+, standard library only.
"""
from __future__ import annotations
from collections import Counter, defaultdict, deque
from itertools import combinations
from pathlib import Path
import hashlib
import json

COUNTS=Counter()
def check(p, label):
    COUNTS[label]+=1
    if not p:
        raise AssertionError(label)

D=tuple((i,j) for i in range(6) for j in range(i+1,6)
        if j-i!=1 and (i,j)!=(0,5))
DI={a:i for i,a in enumerate(D)}
Z=(0,)*18
A=(0,3); B=(1,3); C=(0,4); D35=(3,5)
VP=frozenset(((1,3),(3,5),(1,5)))
VM=frozenset(((0,2),(2,4),(0,4)))
LONGS=frozenset(a for a in D if a[1]-a[0]==3)

def crosses(a,b):
    return not(set(a)&set(b)) and ((a[0]<b[0]<a[1]) != (a[0]<b[1]<a[1]))
def subsets(f):
    f=sorted(f)
    return [frozenset(t) for n in range(len(f)+1) for t in combinations(f,n)]
FACES=[frozenset(t) for n in range(4) for t in combinations(D,n)
       if all(not crosses(a,b) for a,b in combinations(t,2))]
CELLS=[(f,h) for f in FACES for h in subsets(f)]
IX={v:i for i,v in enumerate(CELLS)}
V={i for i,(f,h) in enumerate(CELLS) if f in (VP,VM)}
Q={i for i,(f,h) in enumerate(CELLS) if not f or (len(f)==1 and f<=LONGS)}
E=tuple(i for i in range(len(CELLS)) if i not in V)

def degree(i):
    f,h=CELLS[i]
    return 3-len(f)+len(h)
def mono(xs=None, us=None):
    a=[0]*18
    for k,v in (xs or {}).items(): a[DI[k]]+=v
    for k,v in (us or {}).items(): a[9+DI[k]]+=v
    return tuple(a)
def mm(a,b): return tuple(x+y for x,y in zip(a,b))
def vec(i,m=Z,c=1): return {(i,m):c} if c else {}
def plus(*vs):
    o=defaultdict(int)
    for v in vs:
        for k,c in v.items(): o[k]+=c
    return {k:c for k,c in o.items() if c}
def scale(v,c=1,m=Z):
    return {(i,mm(n,m)):c*b for (i,n),b in v.items() if c*b}
def apply(op,v):
    o={}
    for (i,m),c in v.items():o=plus(o,scale(op(i),c,m))
    return o

def boundary(i,cech=True,relative=True):
    f,h=CELLS[i]; o={}
    for a in D:
        if a in f or len(f)==3 or any(crosses(a,b) for b in f):continue
        j=IX[f|{a},h]
        if relative and j in V:continue
        m=mono(xs={a:1},us={a:-1}) if cech else mono(xs={a:1})
        o=plus(o,vec(j,m,(-1)**sum(b<a for b in f)))
    for k,a in enumerate(sorted(h)):
        j=IX[f,h-{a}]
        if relative and j in V:continue
        o=plus(o,vec(j,Z if cech else mono(us={a:1}),(-1)**(3-len(f)+k)))
    return o

def lam(i):
    f,h=CELLS[i]
    return vec(i,mono(us={a:-1 for a in f-h}))
def cap(i,a):
    f,h=CELLS[i]
    if a not in h:return {}
    return vec(IX[f,h-{a}],c=(-1)**sum(b<a for b in h))
def T(i,a=A,b=B):
    return scale(apply(lambda j:cap(j,b),cap(i,a)),m=mono(us={a:-1,b:-1}))
def Hlocal(i):
    f,h=CELLS[i]
    if A not in f-h or B not in h:return {}
    return scale(cap(i,B),(-1)**(3-len(f)),mono(us={A:-1,B:-1}))
def defect(i):
    f,h=CELLS[i]
    if A in f or B not in h or len(f)==3 or any(crosses(A,x) for x in f):return {}
    sign=(-1)**(sum(x<A for x in f)+2-len(f)+sum(x<B for x in h))
    return vec(IX[f|{A},h-{B}],mono(xs={A:1},us={A:-2,B:-1}),sign)
def rho(v):
    o={}
    for (i,m),c in v.items():
        if i in Q:o=plus(o,vec(('Q',i),m,c))
        for (j,n),s in boundary(i,relative=False).items():
            if j in V:o=plus(o,vec(('V',j),mm(m,n),c*s))
    return o

def legal(m,i):
    f,h=CELLS[i]
    return min(m[:9])>=0 and all(m[9+DI[a]]>=0 or a in f-h for a in D)
def cellstr(i):
    f,h=CELLS[i]
    fmt=lambda t:''.join(map(str,t))
    return {'face':[fmt(t) for t in sorted(f)],'marks':[fmt(t) for t in sorted(h)]}

# Source extraction. Degrees are homological.
PHYS_DEG=[0]+[1]*5+[2]*4+[3]
# Global source indices 0;1..5;6..9;10.
P1=((1,-1,-1,-1,-1),)
P2=((1,0,0,0),(1,0,0,0),(0,1,0,-1),(0,-1,1,0),(0,0,-1,1))
P3=((0,),(1,),(1,),(1,))

def phys_d(i):
    if i==0:return {}
    if i<=5:return vec(0,c=P1[0][i-1])
    if i<=9:return plus(*(vec(1+j,c=P2[j][i-6]) for j in range(5)))
    return plus(*(vec(6+j,c=P3[j][0]) for j in range(4)))
def phys_h(i):
    if i==0:return vec(1)
    if i==2:return vec(6)
    if i==4:return vec(7,c=-1)
    if i==5:return plus(vec(7,c=-1),vec(8,c=-1))
    if i==9:return vec(10)
    return {}
def phys_ip(i):
    if i in (3,4,5):return plus(vec(1),vec(3))
    return {}

def phys_read(i):return 1 if i in (3,4,5) else 0

TATE_DEG=[0,1,1,1,2,2,2,3]
def tate_d(i):
    if i==0:return {}
    if i<=3:return vec(0)
    if i<=6:
        k=i-4
        return plus(vec(1+k),vec(1+(k+1)%3,c=-1))
    return plus(vec(4),vec(5),vec(6))
def tate_h(i):
    return {0:vec(1),2:vec(4,c=-1),3:plus(vec(4,c=-1),vec(5,c=-1)),6:vec(7)}.get(i,{})


def verify_five_rows():
    check(len(CELLS)==215 and len(V)==16 and len(Q)==7,'target_census')
    W=tuple(i for i in E if defect(i))
    check(len(W)==5,'five_state_quotient')
    wset=set(W)
    project=lambda i:vec(i) if i in wset else {}
    dw=lambda i:{k:v for k,v in boundary(i).items() if k[0] in wset}
    for i in E:
        check(apply(boundary,boundary(i))=={},'target_d_squared')
        check(apply(project,boundary(i))==apply(dw,project(i)),'actual_quotient_chain_map')
        check(plus(apply(boundary,Hlocal(i)),apply(Hlocal,boundary(i)))==plus(T(i),defect(i)), 'target_radial_identity')
        check(apply(boundary,defect(i))==apply(defect,boundary(i)),'five_row_defect_closed')
        check(rho(T(i))=={},'T_endpoint_Q_zero')
        check(rho(Hlocal(i))=={},'local_homotopy_endpoint_Q_zero')
        check(rho(defect(i))=={},'defect_endpoint_Q_zero')
        for op in (T,Hlocal,defect):
            for (j,m),c in op(i).items():
                check(legal(m,j),'operator_coefficient_legal')
                f,h=CELLS[i]; ff,hh=CELLS[j]
                check(f-h<=ff-hh,'operator_preserves_existing_localizations')
        if degree(i)<2:check(T(i)=={},'T_low_degree_zero')
    # Ordered basis w0,wc0,wc1,wd0,wd1.
    ids=[IX[frozenset({B}),frozenset({B})],
         IX[frozenset({B,C}),frozenset({B})],
         IX[frozenset({B,C}),frozenset({B,C})],
         IX[frozenset({B,D35}),frozenset({B})],
         IX[frozenset({B,D35}),frozenset({B,D35})]]
    check(set(ids)==wset,'five_row_exact_support')
    w0,wc0,wc1,wd0,wd1=ids
    check(dw(w0)==plus(vec(wc0,mono(xs={C:1},us={C:-1})),vec(wd0,mono(xs={D35:1},us={D35:-1}),-1)), 'quotient_top_column')
    check(dw(wc1)==vec(wc0,c=-1),'quotient_first_normal_column')
    check(dw(wd1)==vec(wd0),'quotient_second_normal_column')
    theta=plus(vec(w0,mono(us={C:1,D35:1})),
               vec(wc1,mono(xs={C:1},us={D35:1})),
               vec(wd1,mono(xs={D35:1},us={C:1})))
    check(apply(dw,theta)=={},'quotient_top_cycle')
    return ids


def verify_retracts():
    for name,degs,ds,hs,ip in [('physical',PHYS_DEG,phys_d,phys_h,phys_ip),
                               ('Tate',TATE_DEG,tate_d,tate_h,lambda i:{})]:
        for i in range(len(degs)):
            check(apply(ds,ds(i))=={},name+'_d_squared')
            check(plus(apply(ds,hs(i)),apply(hs,ds(i)))==plus(vec(i),scale(ip(i),-1)),name+'_integral_retract')
            check(apply(hs,hs(i))=={},name+'_h_squared')
            for state in range(8):
                check(all(degs[j]==degs[i]+1 for j,m in hs(i)),name+'_Cartier_filtration_unaltered')
    z=plus(vec(1),vec(3))
    check(apply(phys_d,z)=={},'physical_primitive_cycle')
    check(sum(c*phys_read(i) for (i,m),c in z.items())==1,'physical_readout_unit')


def corridor_cycle():
    # Actual unmarked edge path between the two endpoint triangulations.
    vertices=[f for f in FACES if len(f)==3]
    prev={VP:None}; todo=deque([VP])
    while todo:
        f=todo.popleft()
        if f==VM:break
        for g in vertices:
            if g not in prev and len(f&g)==2:prev[g]=f;todo.append(g)
    path=[]; f=VM
    while f is not None:path.append(f);f=prev[f]
    path.reverse()
    out={}; sign=1; left_sign=None
    for left,right in zip(path,path[1:]):
        face=left&right; cell=IX[face,frozenset()]
        dc=boundary(cell,cech=False,relative=False)
        signs={CELLS[j][0]:c for (j,m),c in dc.items()}
        if left_sign is not None:sign=-left_sign*signs[left]
        left_sign=sign*signs[right]
        out=plus(out,vec(cell,mono(xs={a:1 for a in face},us={a:-1 for a in face}),sign))
    check(apply(boundary,out)=={},'actual_endpoint_corridor_cycle')
    check(bool(rho(out)),'corridor_retains_endpoint_connectors')
    check(apply(T,out)=={},'corridor_mixed_operation_zero')
    return out,[[''.join(map(str,a)) for a in sorted(f)] for f in path]


def test_source_maps(name,degs,ds,hs,read,cycle,all_checks=True):
    map_count=0; active_rows=0; nonzero=0
    # Every elementary degree +1 (homological) seed produces a closed map.
    # For the physical source add a genuine relative corridor cycle times
    # the supplied primitive readout; this need not be an exact target map.
    for si in range(len(degs)):
        for ti in E:
            if degree(ti)!=degs[si]+1:continue
            f,h=CELLS[ti]
            coeffs=[Z,mono(us={A:2,B:1})]
            if A in f-h:coeffs.append(mono(us={A:-2}))
            for mon in coeffs:
                seed=lambda i:vec(ti,mon) if i==si else {}
                kap={i:plus(apply(boundary,seed(i)),apply(seed,ds(i)),scale(cycle,read(i))) for i in range(len(degs))}
                tk={i:apply(T,kap[i]) for i in range(len(degs))}
                g={i:apply(lambda j:tk[j],hs(i)) for i in range(len(degs))}
                rad={i:apply(defect,kap[i]) for i in range(len(degs))}
                rprim={i:plus(apply(Hlocal,kap[i]),scale(g[i],-1)) for i in range(len(degs))}
                map_count+=1
                active_rows+=sum(bool(rad[i]) for i in kap)
                nonzero+=sum(bool(tk[i]) for i in kap)
                for i in kap:
                    check(apply(boundary,kap[i])==apply(lambda j:kap[j],ds(i)),name+'_sample_chain_map')
                    check(plus(apply(boundary,g[i]),apply(lambda j:g[j],ds(i)))==tk[i],name+'_framed_nullhomotopy')
                    check(plus(apply(boundary,rprim[i]),apply(lambda j:rprim[j],ds(i)))==rad[i],name+'_five_row_primitive')
                    check(rho(g[i])=={},name+'_all_endpoint_Q_homotopies_zero')
                    check(rho(rprim[i])=={},name+'_radial_primitive_frame_zero')
                    for (j,m) in g[i]:check(legal(m,j),name+'_primitive_coefficient_legality')
    return {'tested_chain_maps':map_count,'nonzero_T_columns':nonzero,'nonzero_five_row_columns':active_rows,
            'maps_are':'algebraic controls, not asserted to be the physical connector'}


def verify_ordered_pair_orbit():
    def perm(d,k,s):return tuple(sorted(((s*d[0]+2*k)%6,(s*d[1]+2*k)%6)))
    orbit={(perm(A,k,s),perm(B,k,s)) for k in range(3) for s in (1,-1)}
    check(len(orbit)==6,'D3_ordered_pair_free_orbit')
    for a,b in orbit:
        check(not crosses(a,b),'orbit_pairs_compatible')
        check(a in LONGS and b not in LONGS,'orbit_long_short_type')
        for i in E:
            check(rho(T(i,a,b))=={},'orbit_endpoint_Q_zero')
            check(apply(boundary,T(i,a,b))==apply(lambda j:T(j,a,b),boundary(i)), 'orbit_secondary_map_closed')
    return [[list(a),list(b)] for a,b in sorted(orbit)]



def negative_control():
    # Bounded-free source E_fin, Cech target E; no source contraction is assumed.
    # Fine degree -eps(u03)-eps(u13). Each admissible matrix entry is one monomial.
    def hb(n):
        out=[]
        for i in E:
            f,h=CELLS[i]
            for j in E:
                g,k=CELLS[j]
                if degree(i)-degree(j)!=n:continue
                powers=tuple(int(a in g)-int(a in f) for a in D)+tuple(
                    int(a in h)-int(a in g)-int(a in (A,B)) for a in D)
                if legal(powers,j):out.append((i,j,powers))
        return out
    bases=[hb(n) for n in range(4)]
    check(list(map(len,bases))==[5,24,36,16],'nontrivial_control_Hom_dimensions')
    incoming=defaultdict(set)
    for i in E:
        for (j,m),c in boundary(i,cech=False).items():incoming[j].add(i)
    mats=[]
    for n in range(3):
        rows={v:i for i,v in enumerate(bases[n+1])}
        mat=[[0]*len(bases[n]) for _ in rows]
        for col,(src,tgt,mon) in enumerate(bases[n]):
            op=lambda i:vec(tgt,mon) if i==src else {}
            for i in {src}|incoming[src]:
                v=plus(apply(boundary,op(i)),scale(apply(op,boundary(i,cech=False)),-(-1)**n))
                for (j,m),c in v.items():
                    check((i,j,m) in rows,'nontrivial_control_Hom_homogeneous')
                    mat[rows[i,j,m]][col]+=c
        mats.append(mat)
    row={key:i for i,key in enumerate(bases[2])}; t=[0]*len(row)
    for i in E:
        for (j,m),c in apply(T,lam(i)).items():t[row[i,j,m]]=c
    target=IX[frozenset((A,B)),frozenset()]
    srcs=[IX[frozenset(),frozenset()],IX[frozenset((A,)),frozenset((A,))],
          IX[frozenset((B,)),frozenset((B,))],IX[frozenset((A,B)),frozenset((A,B))]]
    ell=[0]*len(t)
    for sign,i in zip((-1,1,1,1),srcs):
        hits=[k for k,(src,tgt,mon) in enumerate(bases[2]) if src==i and tgt==target]
        check(len(hits)==1,'nontrivial_control_detector_support')
        ell[hits[0]]=sign
    check(all(sum(ell[i]*mats[1][i][j] for i in range(len(ell)))==0
              for j in range(len(bases[1]))),'nontrivial_control_detector_kills_boundaries')
    check(sum(a*b for a,b in zip(ell,t))==1,'nontrivial_control_detector_value_one')
    return {'source':'E_fin, not either finite physical source','dimensions':list(map(len,bases)),
            'integral_detector_on_T_Lambda':1,'detector_annihilates_every_homotopy_boundary':True}


def main():
    ids=verify_five_rows();verify_retracts()
    cycle,path=corridor_cycle()
    tests={
      'physical':test_source_maps('physical',PHYS_DEG,phys_d,phys_h,phys_read,cycle),
      'Tate':test_source_maps('Tate',TATE_DEG,tate_d,tate_h,lambda i:0,{})
    }
    orbit=verify_ordered_pair_orbit()
    negative=negative_control()
    rows=[]
    for i in ids:
        for (j,m),c in defect(i).items():rows.append({'input':cellstr(i),'output':cellstr(j),'sign':c,'coefficient_exponents':list(m)})
    result={'schema':'marici.branchA.five_row_physical_action.v1',
       'source_commit':'d1947b67a60d3e88ba77f4ca60ea02c2a306ee61',
       'five_row_quotient':{'homological_ranks':{'2':2,'3':3},'d3':[['X04/u04',-1,0],['-X35/u35',0,1]],'rows':rows},
       'physical_source_matrices':{'d1':P1,'d2':P2,'d3':P3},
       'physical_retract':'d h+h d=id-i epsilon; i(1)=(1,0,1,0,0); epsilon=road sum',
       'Tate_retract':'d h+h d=id',
       'universal_nullhomotopy':'G=T kappa h; dG+Gd=T kappa; rho G=0',
       'five_row_primitive':'L=Hlocal kappa-T kappa h; dL+Ld=R kappa; rho L=0',
       'conclusion':'degree-two mixed action is zero in the specified target-boundary-framed coefficient mapping fibre for every map from either extracted finite source',
       'whole_source_diagram_admissibility':'NOT ESTABLISHED: source-support, Rees and comparison-arrow restrictions require their actual maps',
       'actual_normalization_connector_rows':'NOT EXTRACTED: inspected integration code exports a signature, not these source-to-target columns',
       'negative_control':negative,'control_maps':tests,'corridor_path':path,'D3_ordered_pair_orbit':orbit,
       'checks':dict(sorted(COUNTS.items())),'total_checks':sum(COUNTS.values()),
       'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    target=Path(__file__).with_name('five_row_physical_action_certificate.json')
    target.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ('conclusion','control_maps','total_checks','whole_source_diagram_admissibility')},indent=2))
    print(target)

if __name__=='__main__':main()
