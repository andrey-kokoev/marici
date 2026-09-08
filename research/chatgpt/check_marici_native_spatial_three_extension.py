#!/usr/bin/env python3
"""Integral native-conductor comparison with the actual short-face link.

Standard library only. No ring variables are inverted. Face-ring maps are
checked modulo their actual coordinate ideals. Fine grading reduces every
polynomial matrix entry to one monomial times an integer. The note supplies
the unbounded-degree proofs and the distinction from full support-PC stalks.
"""
from __future__ import annotations
import argparse
from collections import Counter, defaultdict, deque
from itertools import combinations, product
import json
from pathlib import Path

N=6; ALL=(1<<N)-1; E=sum(1<<i for i in (0,2,4)); O=ALL^E
ZERO=(0,)*N
CHECKS=Counter()

def check(value: bool, name: str, detail=None):
    if not value: raise AssertionError((name,detail))
    CHECKS[name]+=1

def bits(mask): return tuple(i for i in range(N) if mask>>i&1)
def submasks(mask): return tuple(s for s in range(1<<N) if s&~mask==0)
def mono(mask): return tuple(int(bool(mask>>i&1)) for i in range(N))
def plus(a,b): return tuple(x+y for x,y in zip(a,b))
def sign(k): return -1 if k%2 else 1

def add(a,b,scale=1):
    result=dict(a)
    for k,v in b.items():
        result[k]=result.get(k,0)+scale*v
        if not result[k]: del result[k]
    return result

def scalar_term(key,coefficient=1,exponent=ZERO):
    return {(key,exponent):coefficient} if coefficient else {}

def allowed(exponent,face):
    return min(exponent)>=0 and all(v==0 or face>>i&1 for i,v in enumerate(exponent))

class Complex:
    def __init__(self,degrees,shifts=None,faces=None):
        self.degrees=dict(degrees)
        self.keys=tuple(degrees)
        self.shifts=dict(shifts or {k:ZERO for k in degrees})
        self.faces=dict(faces or {k:ALL for k in degrees})
        self.d={k:{} for k in degrees}
    def admitted(self,k,e):
        if hasattr(self,"families"):
            support=sum(1<<i for i,a in enumerate(e) if a)
            return min(e)>=0 and support in self.families[k]
        return allowed(e,self.faces[k])
    def multiply(self,v,exponent=ZERO,coefficient=1):
        out={}
        for (k,e),c in v.items():
            ee=plus(e,exponent)
            if self.admitted(k,ee): out=add(out,{(k,ee):coefficient*c})
        return out
    def differential(self,v):
        out={}
        for (k,e),c in v.items(): out=add(out,self.multiply(self.d[k],e,c))
        return out
    def audit(self,label):
        for k in self.keys:
            check(not self.differential(self.d[k]),label+'_d_squared',k)
            for (j,e),c in self.d[k].items():
                check(self.degrees[j]==self.degrees[k]+1,label+'_d_degree')
                check(plus(self.shifts[j],e)==self.shifts[k],label+'_fine_degree')
                check(allowed(e,self.faces[j]),label+'_legal_coefficient')
                # The coefficient map must kill every source module relation.
                for i in bits(ALL^self.faces[k]):
                    check(not self.multiply({(j,e):c},mono(1<<i)),label+'_module_relations')

def apply_map(F,v,target):
    out={}
    for (k,e),c in v.items(): out=add(out,target.multiply(F.get(k,{}),e,c))
    return out

def dmap(F,source,target,n):
    return {k:add(target.differential(F.get(k,{})),apply_map(F,source.d[k],target),-sign(n))
            for k in source.keys}

def koszul_co(seq,tag):
    degrees={(tag,h):h.bit_count()-6 for h in submasks(seq)}
    C=Complex(degrees,{k:mono(ALL^k[1]) for k in degrees})
    for k in C.keys:
        h=k[1]
        for i in bits(seq^h):
            C.d[k]=add(C.d[k],scalar_term((tag,h|(1<<i)),sign((h&((1<<i)-1)).bit_count()),mono(1<<i)))
    return C

def native_dual():
    pe=koszul_co(E,'+');po=koszul_co(O,'-');pc=koszul_co(ALL,'c')
    deg={**pe.degrees,**po.degrees,**{k:v-1 for k,v in pc.degrees.items()}}
    C=Complex(deg,{**pe.shifts,**po.shifts,**pc.shifts})
    C.d.update(pe.d);C.d.update(po.d)
    for k in pc.keys:
        h=k[1];v={t:-c for t,c in pc.d[k].items()}
        if h&~E==0:v=add(v,scalar_term(('+',h)))
        if h&~O==0:v=add(v,scalar_term(('-',h),-1))
        C.d[k]=v
    return C

def diag(i,j):return tuple(sorted((i%6,j%6)))
SHORT=tuple(diag(i,i+2) for i in range(6))
def crosses(a,b):
    x,y=a;u,v=b
    return x<u<y<v or u<x<v<y

def noncrossing(mask):
    return all(not crosses(SHORT[i],SHORT[j]) for i,j in combinations(bits(mask),2))

DELTA0=tuple(sorted(set(submasks(E))|set(submasks(O)),key=lambda m:(m.bit_count(),m)))
DELTA=tuple(m for m in range(64) if noncrossing(m))
BRIDGES=tuple(m for m in DELTA if m not in DELTA0)

def incidence_complex(delta):
    C=Complex({f:-f.bit_count() for f in delta},faces={f:f for f in delta})
    for f in C.keys:
        for pos,i in enumerate(bits(f)):
            C.d[f]=add(C.d[f],scalar_term(f^(1<<i),sign(pos)))
    return C

# Integer elimination, using only signed-unit pivots. No rational arithmetic.
class UnitSolver:
    def __init__(self,rows,columns,entries):
        self.rows=tuple(rows);self.cols=tuple(columns)
        ri={k:i for i,k in enumerate(rows)};ci={k:i for i,k in enumerate(columns)}
        a=[[0]*len(columns) for _ in rows]
        for c,v in entries.items():
            for r,x in v.items():a[ri[r]][ci[c]]=x
        self.ops=[];perm=list(range(len(columns)));k=0
        while k<min(len(rows),len(columns)):
            pivot=next(((i,j) for i in range(k,len(rows)) for j in range(k,len(columns)) if abs(a[i][j])==1),None)
            if pivot is None:break
            i,j=pivot
            if i!=k:a[i],a[k]=a[k],a[i];self.ops.append(('swap',i,k))
            if j!=k:
                for row in a:row[j],row[k]=row[k],row[j]
                perm[j],perm[k]=perm[k],perm[j]
            if a[k][k]<0:a[k]=[-x for x in a[k]];self.ops.append(('scale',k,-1))
            for i in range(len(rows)):
                if i!=k and a[i][k]:
                    c=a[i][k];a[i]=[x-c*y for x,y in zip(a[i],a[k])]
                    self.ops.append(('add',i,k,-c))
            k+=1
        self.rank=k;self.perm=perm;self.a=a
        check(all(x==0 for row in a[k:] for x in row),'integer_elimination_all_nonzero_factors_unit')
    def solve(self,rhs):
        b=[rhs.get(r,0) for r in self.rows]
        for op in self.ops:
            if op[0]=='swap':_,i,j=op;b[i],b[j]=b[j],b[i]
            elif op[0]=='scale':_,i,c=op;b[i]*=c
            else:_,i,j,c=op;b[i]+=c*b[j]
        if any(b[self.rank:]):return None
        x={self.cols[self.perm[i]]:b[i] for i in range(self.rank) if b[i]}
        return x

def degree_slice(C,alpha):
    available={k:tuple(a-b for a,b in zip(alpha,C.shifts[k])) for k in C.keys}
    available={k:e for k,e in available.items() if C.admitted(k,e)}
    deg={k:C.degrees[k] for k in available};d={k:{} for k in deg}
    for k,e in available.items():
        for (j,f),c in C.d[k].items():
            if j in available and plus(e,f)==available[j]:d[k][j]=d[k].get(j,0)+c
    return deg,d

def ranks_homology(deg,d):
    ranks={};bases={q:[k for k in deg if deg[k]==q] for q in set(deg.values())}
    for q in sorted(bases):
        rows=bases.get(q+1,[]);cols=bases[q]
        solver=UnitSolver(rows,cols,{k:d[k] for k in cols})
        ranks[q]=solver.rank
    return {q:len(v)-ranks.get(q,0)-ranks.get(q-1,0) for q,v in sorted(bases.items())
            if len(v)-ranks.get(q,0)-ranks.get(q-1,0)}

def homogeneous_map_basis(source,target,n):
    out=[]
    for s in source.keys:
        e=source.shifts[s]
        for t in target.keys:
            if target.degrees[t]-source.degrees[s]!=n or not allowed(e,target.faces[t]):continue
            # Every source is free in the native comparison.
            out.append((s,t))
    return tuple(out)

def vector_to_map(v,source,target):
    out={k:{} for k in source.keys}
    for (s,t),c in v.items():out[s]=add(out[s],scalar_term(t,c,source.shifts[s]))
    return out

def map_to_vector(F,source,target,n):
    out={}
    for s,v in F.items():
        for (t,e),c in v.items():
            check(target.degrees[t]-source.degrees[s]==n and e==source.shifts[s], 'homogeneous_map_encoding')
            out[(s,t)]=out.get((s,t),0)+c
    return {k:v for k,v in out.items() if v}

def hom_complex(source,target):
    degrees={};ds={};basis={}
    for q in (-2,-1,0,1):
        basis[q]=homogeneous_map_basis(source,target,q)
        degrees.update({k:q for k in basis[q]})
    for q in (-2,-1,0):
        for b in basis[q]:
            f=vector_to_map({b:1},source,target)
            df=dmap(f,source,target,q)
            ds[b]=map_to_vector(df,source,target,q+1)
    return basis,ds

def perm(i,g):
    r,s=g
    return (((1-i) if s else i)+2*r)%6

def perm_mask(h,g):return sum(1<<perm(i,g) for i in bits(h))
def wedge_sign(h,g):
    vals=[perm(i,g) for i in bits(h)]
    return sign(sum(vals[i]>vals[j] for i in range(len(vals)) for j in range(i+1,len(vals))))
def mul(g,h):return ((g[0]+sign(g[1])*h[0])%3,g[1]^h[1])
GROUP=tuple(product(range(3),range(2)))
def inverse(g):return next(h for h in GROUP if mul(g,h)==(0,0))

def source_action(k,g):
    tag,h=k;tt=tag
    if g[1] and tag in ('+','-'):tt='-' if tag=='+' else '+'
    a=wedge_sign(h,g)*wedge_sign(ALL,g)
    if tag=='c' and g[1]:a=-a
    return (tt,perm_mask(h,g)),a

def target_action(f,g):return perm_mask(f,g),wedge_sign(f,g)

def perm_exp(e,g):
    out=[0]*6
    for i,a in enumerate(e):out[perm(i,g)]=a
    return tuple(out)

def act_vector(v,g,action):
    out={}
    for (k,e),c in v.items():
        kk,s=action(k,g);out=add(out,scalar_term(kk,c*s,perm_exp(e,g)))
    return out

def act_hom(v,g):
    out={}
    for (s,t),c in v.items():
        ss,a=source_action(s,g);tt,b=target_action(t,g)
        out[(ss,tt)]=out.get((ss,tt),0)+a*b*c
    return {k:x for k,x in out.items() if x}

def apply_int(d,v):
    out={}
    for k,c in v.items():out=add(out,d.get(k,{}),c)
    return out


def construct_comparison(S,J):
    check(not homogeneous_map_basis(S,J,-3),'no_higher_negative_comparison_columns')
    basis,hd=hom_complex(S,J)
    known={(('+',E),O):1,(('-',O),E):-1}
    columns=[b for b in basis[0] if b[0][0]=='c']
    solver=UnitSolver(basis[1],columns,{b:hd[b] for b in columns})
    needed={k:-c for k,c in apply_int(hd,known).items()}
    h=solver.solve(needed)
    check(h is not None,'native_face_comparison_exists_integrally')
    F=add(known,h)
    check(not apply_int(hd,F),'native_face_comparison_full_chain_equation')
    maps=vector_to_map(F,S,J)
    # Nontrivial maps of BOTH branch cohomology and the conductor cohomology.
    check(maps[('+',E)]==scalar_term(O,1,mono(O)),'positive_branch_canonical_line')
    check(maps[('-',O)]==scalar_term(E,-1,mono(E)),'negative_branch_canonical_line')
    sigma=maps[('c',ALL)]
    check(not J.differential(sigma),'conductor_face_cycle')
    odd_sum=sum(c for (f,e),c in sigma.items() if f&O)
    even_sum=sum(c for (f,e),c in sigma.items() if f&E)
    check(abs(odd_sum)==1 and odd_sum==-even_sum,'primitive_conductor_difference')
    # Full Hom computation in negative degrees. Uniqueness is derived, not strict.
    s_minus2=UnitSolver(basis[-1],basis[-2],{b:hd[b] for b in basis[-2]})
    s_minus1=UnitSolver(basis[0],basis[-1],{b:hd[b] for b in basis[-1]})
    s_zero=UnitSolver(basis[1],basis[0],{b:hd[b] for b in basis[0]})
    check(s_minus2.rank==len(basis[-2]),'no_degree_minus_two_self_comparisons')
    check(len(basis[-1])==s_minus1.rank+s_minus2.rank,'no_degree_minus_one_self_comparisons')
    check(len(basis[0])-s_zero.rank-s_minus1.rank==1,'one_scalar_native_endomorphism_in_frame')
    a={};b={}
    for g in GROUP:
        diff=add(act_hom(F,g),F,-1)
        a[g]=s_minus1.solve(diff)
        check(a[g] is not None,'equivariant_comparison_one_cells',g)
        check(apply_int(hd,a[g])==diff,'one_cell_boundary_exact',g)
    for g,h in product(GROUP,repeat=2):
        defect=add(add(act_hom(a[h],g),a[mul(g,h)],-1),a[g])
        b[g,h]=s_minus2.solve(defect)
        check(b[g,h] is not None,'equivariant_comparison_two_cells',(g,h))
        check(apply_int(hd,b[g,h])==defect,'two_cell_boundary_exact',(g,h))
    for g,h,k in product(GROUP,repeat=3):
        defect=add(add(add(act_hom(b[h,k],g),b[mul(g,h),k],-1),b[g,mul(h,k)]),b[g,h],-1)
        check(not defect,'equivariant_comparison_all_triple_coherences',(g,h,k))
    return maps,sigma,{
        'comparison_nonzero_columns':len([v for v in maps.values() if v]),
        'comparison_nonzero_terms':sum(len(v) for v in maps.values()),
        'hom_dimensions':{str(q):len(basis[q]) for q in basis},
        'hom_differential_ranks':{'-2':s_minus2.rank,'-1':s_minus1.rank,'0':s_zero.rank},
        'group_one_cells':len(a),'group_two_cells':len(b),'group_triple_identities':216,
        'one_cell_nonzero_terms':{str(g):len(v) for g,v in a.items()},
        'two_cell_nonzero_terms':{str(g):len(v) for g,v in b.items()},
        'comparison':[{'source':[s[0],list(bits(s[1]))],
                       'target_face':list(bits(t)),'coefficient':c,
                       'monomial_exponents':list(e)}
                      for s,v in maps.items() for (t,e),c in v.items()],
        'conductor_cycle': [{'face':list(bits(f)),'coefficient':c} for (f,e),c in sigma.items()]
    }


def maps_on_every_support(S,J0,JS,F):
    records=[]
    for P in range(64):
        alpha=mono(P)
        ss,sd=degree_slice(S,alpha);jj,jd=degree_slice(J0,alpha);tt,td=degree_slice(JS,alpha)
        hs=ranks_homology(ss,sd);hj=ranks_homology(jj,jd);ht=ranks_homology(tt,td)
        check(hs==hj,'native_dual_face_model_all_polynomial_supports',P)
        # The cone of the actual map, not just matching source/target ranks.
        cone_deg={('t',k):q for k,q in jj.items()}
        cone_deg.update({('s',k):q-1 for k,q in ss.items()})
        cone_d={k:{} for k in cone_deg}
        for k in jj:
            cone_d[('t',k)]={('t',j):c for j,c in jd[k].items()}
        for k in ss:
            v={('s',j):-c for j,c in sd[k].items()}
            for (t,e),c in F[k].items():
                if t in jj:v=add(v,{('t',t):c})
            cone_d[('s',k)]=v
        check(not ranks_homology(cone_deg,cone_d),'native_comparison_cone_integrally_acyclic',P)
        expected={}
        if P==0:expected[-1]=1
        if P==E or P==O:expected[-3]=1
        check(hj==expected,'native_face_cohomology_closed_formula',P)
        # Positive exponents supported strictly within one branch are not enough
        # for a branch canonical form: all three must be positive.
        # Constant map coefficient on a nonzero source cohomology generator was
        # checked separately; the branch and conductor triangles prove the iso.
        expected_target={}
        if P==E or P==O:expected_target[-3]=1
        # Pair polynomial summands in degree -2, minus the one conductor value.
        edge_modes=sum(P&~p==0 for p in BRIDGES)
        if P==0:edge_modes-=1
        if edge_modes:expected_target[-2]=edge_modes
        check(ht==expected_target,'short_link_complete_cohomology_formula',P)
        records.append({'positive_support':list(bits(P)),'native_H':hs,'short_link_H':ht})
    return records


def boundary_chain(v,delta):
    out={}
    for f,c in v.items():
        for pos,i in enumerate(bits(f)):
            t=f^(1<<i)
            if t in delta:out=add(out,{t:sign(pos)*c})
    return out

def branch_path(start,finish,allowed_edges):
    adj=defaultdict(list)
    for f in allowed_edges:
        a,b=bits(f);adj[a].append((b,f));adj[b].append((a,f))
    queue=deque([start]);previous={start:None}
    while queue:
        a=queue.popleft()
        for b,f in adj[a]:
            if b not in previous:previous[b]=(a,f);queue.append(b)
    check(finish in previous,'spatial_branch_path_exists')
    current=finish;out={}
    while current!=start:
        a,f=previous[current];i,j=bits(f)
        out=add(out,{f:1 if (a,current)==(i,j) else -1});current=a
    check(boundary_chain(out,set(DELTA))=={1<<finish:1,1<<start:-1},'spatial_path_endpoint_identity')
    return out


def bridge_attachment(J0,JS,sigma):
    # Choose oriented bridges even -> odd, independent of lexicographic order.
    target_sigma={f:c for (f,e),c in sigma.items()}
    pos=[bits(f)[0] for f,c in target_sigma.items() if c==1]
    neg=[bits(f)[0] for f,c in target_sigma.items() if c==-1]
    # The algebraic solution may be a longer integral cycle. Compare it to the
    # fixed primitive odd-even cycle by filling separately on both simplices.
    ref={1<<1:1,1<<0:-1}
    odd=sum(c for f,c in target_sigma.items() if f&O)
    endpoint_solver=UnitSolver(tuple(f for f in DELTA0 if f.bit_count()==1),
        tuple(f for f in DELTA0 if f.bit_count()==2),
        {f:boundary_chain({f:1},set(DELTA0)) for f in DELTA0 if f.bit_count()==2})
    correction=endpoint_solver.solve(add(target_sigma,ref,-odd))
    check(correction is not None,'native_cycle_to_fixed_endpoint_identification')
    fillers=[]
    pure_edges=[f for f in DELTA0 if f.bit_count()==2]
    for p in BRIDGES:
        even=next(i for i in bits(p) if i%2==0);odd_vertex=next(i for i in bits(p) if i%2)
        path=branch_path(0,even,[f for f in pure_edges if f&~E==0]) if even!=0 else {}
        path=add(path,{p:1 if even<odd_vertex else -1})
        if odd_vertex!=1:path=add(path,branch_path(odd_vertex,1,[f for f in pure_edges if f&~O==0]))
        check(boundary_chain(path,set(DELTA))==ref,'each_actual_bridge_fills_conductor')
        full=add(correction,path,odd)
        check(boundary_chain(full,set(DELTA))==target_sigma,'native_conductor_image_is_explicit_boundary')
        fillers.append({'bridge':list(bits(p)),
            'filler':[{'edge':list(bits(f)),'coefficient':c} for f,c in full.items()]})
    # Kernel of the ring quotient is three genuine monomial ideals, not formal cells.
    for support in range(64):
        full=support in DELTA;native=support in DELTA0
        active=[p for p in BRIDGES if p&support==p and support&~p==0]
        check(int(full)==int(native)+len(active),'exact_face_ring_sequence_supports',support)
        for i in range(6):
            s=support|(1<<i)
            if active:
                check((s in DELTA)==(s&~active[0]==0),'bridge_kernel_annihilator', (support,i))
    # The connecting coefficient is evaluation at zero, NOT polynomial sum.
    for p in BRIDGES:
        for i,j in product(range(4),repeat=2):
            a,b=bits(p);ex=[0]*6;ex[a]=i;ex[b]=j
            v=scalar_term(p,1,tuple(ex));dv=JS.differential(v)
            if i==j==0:
                n=sum(c for (f,e),c in dv.items() if f&O)
                check(abs(n)==1,'primitive_bridge_constant_attachment')
            else:
                # Positive surviving singleton terms are exact in the native
                # face complex; all-subset homology computation already proves it.
                deg,d=degree_slice(J0,tuple(ex))
                check(not ranks_homology(deg,d),'positive_bridge_coefficients_no_conductor_value')
    return fillers


def symmetry(C,action,name):
    for g in GROUP:
        for k in C.keys:
            kk,s=action(k,g)
            check(kk in C.degrees,name+'_preserves_basis')
            check(act_vector(C.d[k],g,action)=={t:s*a for t,a in C.d[kk].items()},name+'_chain_equivariance')
            for h in GROUP:
                a,x=action(k,h);b,y=action(a,g);c,z=action(k,mul(g,h))
                check((b,x*y)==(c,z),name+'_all_group_laws')


# The three long vertices complete the actual noncrossing link to a 2-sphere.
# Long occurrence variables remain spectators: this is a coordinate-face
# occurrence model, not an alteration of the original normal-localized PC stalks.
ALL_DIAGS=SHORT+tuple(diag(i,i+3) for i in range(3))
def bits9(mask):return tuple(i for i in range(9) if mask>>i&1)
def compatible9(mask):
    return all(not crosses(ALL_DIAGS[i],ALL_DIAGS[j]) for i,j in combinations(bits9(mask),2))
FULL_FACES=tuple(m for m in range(512) if m.bit_count()<=3 and compatible9(m))
ROAD_ORDER=(7,6,8)   # D14,D03,D25, matching the inherited cyclic order.
BRIDGE_ORDER=tuple((1<<i)|(1<<(i+3)) for i in (1,0,2))

def cube_link_complex(faces):
    C=Complex({f:-f.bit_count() for f in faces},faces={f:f&ALL for f in faces})
    for f in C.keys:
        for p,i in enumerate(bits9(f)):
            if (f^(1<<i)) in C.degrees:
                C.d[f]=add(C.d[f],scalar_term(f^(1<<i),sign(p)))
    return C

def d9(v):
    out={}
    for f,c in v.items():
        for p,i in enumerate(bits9(f)):out=add(out,{f^(1<<i):sign(p)*c})
    return out

def beta_sign(p):
    a,b=bits(p)
    return 1 if a%2==0 else -1

def link_cycle(long_label):
    link=[f for f in DELTA if compatible9(f|(1<<long_label))]
    vertices=[bits(f)[0] for f in link if f.bit_count()==1]
    edges=[f for f in link if f.bit_count()==2]
    check((len(vertices),len(edges))==(4,4),'actual_long_facet_link_is_four_cycle')
    adjacency=defaultdict(list)
    for p in edges:
        a,b=bits(p);adjacency[a].append(b);adjacency[b].append(a)
    start=min(vertices);path=[start,min(adjacency[start])]
    while len(path)<4:
        options=[j for j in adjacency[path[-1]] if j!=path[-2]]
        check(len(options)==1,'actual_square_cycle_continuation')
        path.append(options[0])
    path.append(start);cycle={}
    for a,b in zip(path,path[1:]):
        p=(1<<a)|(1<<b);cycle[p]=1 if a<b else -1
    check(not d9(cycle),'actual_square_cycle_closed')
    own=BRIDGE_ORDER[ROAD_ORDER.index(long_label)]
    scale=cycle[own]*beta_sign(own)
    cycle={p:c*scale for p,c in cycle.items()}
    check(cycle[own]==beta_sign(own),'positive_labelled_long_facet_orientation')
    cone={p|(1<<long_label):c for p,c in cycle.items()}
    check(d9(cone)==cycle,'actual_long_star_boundary_not_fitted')
    return link,cycle,cone

def spatial_polynomial_resolution(J0):
    check(len(FULL_FACES)==45,'complete_non_crossing_link_face_count')
    full=cube_link_complex(FULL_FACES);full.audit('full_link_coordinate_faces')
    links={};cycles={};cones={}
    for ell in ROAD_ORDER:links[ell],cycles[ell],cones[ell]=link_cycle(ell)
    m=[[cycles[d].get(p,0)*beta_sign(p) for d in ROAD_ORDER] for p in BRIDGE_ORDER]
    expected=[[1,-1,0],[0,1,-1],[-1,0,1]] # 1-r^2 in the fixed road order
    check(m==expected,'labelled_middle_map_derived_as_one_minus_r_squared')
    r=[[0,0,1],[1,0,0],[0,1,0]]
    change=[[-x for x in row] for row in r]
    transformed=[[sum(m[i][k]*change[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
    check(transformed==[[1,0,-1],[-1,1,0],[0,-1,1]],'native_tag_dictionary_recovers_one_minus_r')
    sumcone={}
    for v in cones.values():sumcone=add(sumcone,v)
    needed={f:-c for f,c in d9(sumcone).items()}
    endpoint_solver=UnitSolver(tuple(f for f in DELTA0 if f.bit_count()==2),(E,O),
        {E:d9({E:1}),O:d9({O:1})})
    endpoint_correction=endpoint_solver.solve(needed)
    check(endpoint_correction is not None and set(endpoint_correction)=={E,O},'both_endpoint_triangles_required')
    check(all(abs(c)==1 for c in endpoint_correction.values()),'endpoint_corrections_integral_primitive')
    fundamental=add(sumcone,endpoint_correction)
    check(len(fundamental)==14 and all(abs(c)==1 for c in fundamental.values()),'full_fourteen_triangle_fundamental_chain')
    check(not d9(fundamental),'full_link_fundamental_chain_closed')
    check(bool(d9(sumcone)),'removing_endpoint_triangles_breaks_closure')
    # T: short-link face ring; G_d: four-cycle face rings; P_p: bridge face rings.
    deg={('T',0):-3}
    deg.update({('G',d):-2 for d in ROAD_ORDER});deg.update({('P',p):-1 for p in BRIDGE_ORDER})
    R=Complex(deg)
    R.families={('T',0):set(DELTA)}
    R.families.update({('G',d):set(links[d]) for d in ROAD_ORDER})
    R.families.update({('P',p):set(submasks(p)) for p in BRIDGE_ORDER})
    R.d[('T',0)]={((('G',d)),ZERO):1 for d in ROAD_ORDER}
    for j,d in enumerate(ROAD_ORDER):
        R.d[('G',d)]={((('P',p)),ZERO):m[i][j] for i,p in enumerate(BRIDGE_ORDER) if m[i][j]}
    # Map the ENTIRE seven-term spatial resolution to the native face dual.
    F={k:{} for k in R.keys}
    F[('T',0)]={(p,ZERO):c for p,c in endpoint_correction.items()}
    for d in ROAD_ORDER:
        F[('G',d)]={(p,ZERO):-c for p,c in cycles[d].items() if p in DELTA0}
    for p in BRIDGE_ORDER:
        F[('P',p)]={(f,ZERO):beta_sign(p)*c for f,c in d9({p:1}).items()}
    for k in R.keys:
        check(not R.differential(R.d[k]),'spatial_polynomial_resolution_d_squared',k)
        check(J0.differential(F[k])==apply_map(F,R.d[k],J0),'spatial_native_comparison_full_chain_equation',k)
        # Check every monomial support relation, not only missing variables.
        for bad in range(64):
            if bad in R.families[k]:continue
            check(not R.multiply(R.d[k],mono(bad)),'spatial_resolution_maps_descend_to_face_rings')
            check(not J0.multiply(F[k],mono(bad)),'spatial_native_map_descends_to_face_rings')
    # Complete all-polynomial quasi-isomorphism test, with the actual cone.
    for P in range(64):
        rr,rd=degree_slice(R,mono(P));jj,jd=degree_slice(J0,mono(P))
        check(ranks_homology(rr,rd)==ranks_homology(jj,jd),'seven_term_native_dual_all_coefficient_supports',P)
        degcone={('j',k):q for k,q in jj.items()};degcone.update({('r',k):q-1 for k,q in rr.items()})
        dc={k:{} for k in degcone}
        for k in jj:dc[('j',k)]={('j',t):a for t,a in jd[k].items()}
        for k in rr:
            v={('r',t):-a for t,a in rd[k].items()}
            for (t,e),a in F[k].items():
                if t in jj:v=add(v,{('j',t):a})
            dc[('r',k)]=v
        check(not ranks_homology(degcone,dc),'seven_term_spatial_native_cone_is_integrally_acyclic',P)
        # Independent whole-link resolution T[3] -> J_full.
        ff,fd=degree_slice(full,mono(P))
        expected={-3:1} if P in DELTA else {}
        check(ranks_homology(ff,fd)==expected,'full_link_resolves_short_face_ring',P)
        fv=full.multiply({(f,ZERO):c for f,c in fundamental.items()},mono(P))
        check(bool(fv)==(P in DELTA),'fundamental_class_has_exact_short_face_ring_annihilator',P)
        check(not full.differential(fv),'fundamental_class_all_polynomial_modes_closed')
    # Geometry fixes every D3 action in the seven-term model.
    def label_perm(i,g):
        if i<6:return perm(i,g)
        j=i-6;return 6+(((-j) if g[1] else j)+2*g[0])%3
    def face_action9(f,g):
        seq=[label_perm(i,g) for i in bits9(f)]
        return sum(1<<i for i in seq),sign(sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq))))
    def spatial_action(k,g):
        tag,v=k
        if tag=='T':return k,1
        if tag=='G':return ('G',label_perm(v,g)),1
        return ('P',perm_mask(v,g)),sign(g[1])
    for g in GROUP:
        image={}
        for f,c in fundamental.items():
            h,a=face_action9(f,g);image[h]=a*c
        check(image==fundamental,'link_fundamental_orientation_character')
        for k in R.keys:
            image,a=spatial_action(k,g)
            check({perm_mask(p,g) for p in R.families[k]}==R.families[image],
                  'spatial_D3_preserves_full_polynomial_coefficient_domains')
            check(act_vector(R.d[k],g,spatial_action)=={t:a*c for t,c in R.d[image].items()},'spatial_seven_term_D3_differential')
            check(act_vector(F[k],g,target_action)=={t:a*c for t,c in F[image].items()},'spatial_native_map_strict_D3_covariance')
            for h in GROUP:
                kk,a=spatial_action(k,h);tt,b=spatial_action(kk,g);zz,c=spatial_action(k,mul(g,h))
                check((tt,a*b)==(zz,c),'spatial_seven_term_all_group_laws')
    # Build the whole native three-extension, including both polynomial
    # endpoint ideals and the actual conductor augmentation.
    xdeg={('M',O):0,('M',E):0,('T',0):1,('C',0):4}
    xdeg.update({('G',d):2 for d in ROAD_ORDER})
    xdeg.update({('P',p):3 for p in BRIDGE_ORDER})
    shifts={k:(mono(k[1]) if k[0]=='M' else ZERO) for k in xdeg}
    X=Complex(xdeg,shifts)
    X.families=dict(R.families)
    X.families.update({('M',E):set(submasks(E)),('M',O):set(submasks(O)),('C',0):{0}})
    for f in (E,O):X.d[('M',f)]=scalar_term(('T',0),1,mono(f))
    for k in R.keys:X.d[k]=dict(R.d[k])
    for p in BRIDGE_ORDER:X.d[('P',p)]=scalar_term(('C',0))
    for k in X.keys:
        check(not X.differential(X.d[k]),'entire_native_three_extension_d_squared')
        for bad in range(64):
            if bad not in X.families[k]:
                check(not X.multiply(X.d[k],mono(bad)),'entire_three_extension_polynomial_module_relations')
    # Polynomial augmentation, including exact kernel and image on each support.
    for P in range(64):
        xx,xd=degree_slice(X,mono(P))
        check(not ranks_homology(xx,xd),'complete_native_three_extension_integrally_exact',P)
        dims=[int(P==E)+int(P==O),int(P in DELTA),
              sum(P in links[d] for d in ROAD_ORDER),sum(P&~p==0 for p in BRIDGE_ORDER),int(P==0)]
        check(sum(sign(i)*x for i,x in enumerate(dims))==0,'full_native_three_extension_euler_each_support')
    return {
       'full_link_face_counts':[1,9,21,14],
       'long_road_order':['D14','D03','D25'],
       'bridge_order':[list(bits(p)) for p in BRIDGE_ORDER],
       'middle_matrix':m,'signed_cyclic_tag_change':change,'one_minus_r_matrix':transformed,
       'endpoint_correction':{'even':endpoint_correction[E],'odd':endpoint_correction[O]},
       'fundamental_triangles':[{'face':list(bits9(f)),'coefficient':c} for f,c in fundamental.items()],
       'native_spatial_terms':{'-3':['T'], '-2':['G14','G03','G25'], '-1':['P14','P03','P25']},
       'cohomology':{'-3':'X1 X3 X5 B_plus direct_sum X0 X2 X4 B_minus','-1':'C with polarity'},
       'augmentation':'sum of the three bridge constant values',
       'extension':'0 -> M -> T -> direct_sum G_d -> direct_sum P_p -> C -> 0',
       'native_comparison':[{'source':str(s),'target_face':list(bits(t)),'coefficient':c}
                             for s,v in F.items() for (t,e),c in v.items()],
       'description':'Every term and differential comes from the actual noncrossing sphere, its two endpoint triangles, three long-facet cone links, and three mixed short bridges. The map to the native dual is a full polynomial quasi-isomorphism.'
    }


def main(output):
    check(len(DELTA0)==15 and len(DELTA)==18,'native_and_actual_short_face_counts')
    check({tuple(bits(p)) for p in BRIDGES}=={(0,3),(1,4),(2,5)},'three_bridges_from_actual_diagonal_crossing')
    S=native_dual();J0=incidence_complex(DELTA0);JS=incidence_complex(DELTA)
    check(len(S.keys)==80,'full_native_dual_eighty_columns')
    for C,label in [(S,'native_dual'),(J0,'native_face'),(JS,'short_link')]:C.audit(label)
    F,sigma,comparison=construct_comparison(S,J0)
    support=maps_on_every_support(S,J0,JS,F)
    fills=bridge_attachment(J0,JS,sigma)
    spatial=spatial_polynomial_resolution(J0)
    symmetry(S,source_action,'source_D3')
    symmetry(J0,target_action,'native_face_D3');symmetry(JS,target_action,'short_link_D3')
    # Inclusion of native face terms and projection onto three bridge terms.
    for f in J0.keys:check(J0.d[f]==JS.d[f],'native_spatial_inclusion_keeps_every_attachment')
    for p in BRIDGES:check(all(t in J0.degrees for (t,e) in JS.d[p]),'relative_bridges_have_zero_quotient_differential')
    # Negative occurrence modes vanish in these squarefree-dual face rings.
    for i in range(6):
        a=[0]*6;a[i]=-1
        check(not degree_slice(J0,tuple(a))[0] and not degree_slice(JS,tuple(a))[0],'negative_occurrence_modes_empty')
    # All 192 squarefree multiplications and 240 commuting squares retain the
    # actual face quotient. Integer unit pivots never localize an occurrence.
    arrows=0;squares=0
    for P in range(64):
        for i in bits(ALL^P):
            arrows+=1
            for C in (J0,JS):
                for f in C.keys:
                    present=P&~f==0
                    after=(P|(1<<i))&~f==0
                    if present:
                        img=C.multiply(scalar_term(f,1,mono(P)),mono(1<<i))
                        check(bool(img)==after,'face_multiplication_is_actual_quotient_map')
            for j in bits(ALL^P):
                if j<=i:continue
                squares+=1
                for C in (J0,JS):
                    for f in C.keys:
                        v=scalar_term(f,1,mono(P)) if P&~f==0 else {}
                        l=C.multiply(C.multiply(v,mono(1<<i)),mono(1<<j))
                        r=C.multiply(C.multiply(v,mono(1<<j)),mono(1<<i))
                        check(l==r,'coefficient_multiplication_squares')
    check((arrows,squares)==(192,240),'all_squarefree_coefficient_arrows_and_squares')
    result={
      'status':'proved_polynomial_spatial_realization_of_the_native_nonsplit_conductor_three_extension',
      'source_commit':'d1947b67a60d3e88ba77f4ca60ea02c2a306ee61',
      'source_blobs':{
        'normalization_conductor':'840258522d45e450e4f1e8bb927d9aae58c75566',
        'literal_non_crossing_target':'e972b69d0e2b1b0a0aee5e0a027c8216bcace3e8'},
      'native_face_count':15,'actual_short_face_count':18,
      'extra_faces':[list(bits(p)) for p in BRIDGES],
      'comparison':comparison,
      'all_64_homogeneous_supports':support,
      'three_explicit_spatial_fillers':fills,
      'seven_term_native_spatial_resolution':spatial,
      'relative_quotient':{'degree':-2,'terms':'direct sum of A/(coordinates outside each actual bridge)',
                           'differential':0},
      'conductor_connecting_map':'sum of the three zero-section evaluations, after even-to-odd edge orientation',
      'constant_grade_exact_sequence':{'ranks':[2,3,1],'augmentation':[1,1,1],'torsion':False},
      'native_conductor_image_in_absolute_short_link':0,
      'native_branch_duals_preserved':True,
      'source_identification_D3':'explicit coherent comparison: six one-cells, 36 two-cells, 216 triple identities',
      'ring_operations':'Polynomial maps of coordinate quotient modules; no occurrence inversion or coefficient extraction.',
      'scope':[
          'Face-ring/coordinate-strata model built from actual short-diagonal incidence.',
          'It is not a replacement of original PC stalks R[u_a^-1] by face rings.',
          'No identification with the complete ringed supported-Verdier PC functor is claimed.',
          'No physical reflection parity is selected.',
          'The native conductor maps to zero in the absolute connected link, but its two-branch attachment persists in the displayed relative triangle.',
          'Independent normal/Rees/excess parameters may be adjoined; a nonflat specialization of occurrence coordinates requires derived tensoring of this diagram.'
      ],
      'checks':dict(sorted(CHECKS.items())), 'exact_assertions':sum(CHECKS.values())}
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['status','native_face_count','actual_short_face_count','extra_faces','comparison','exact_assertions']},indent=2))

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output',type=Path,default=Path('marici_native_spatial_three_extension_certificate.json'))
    args=p.parse_args();main(args.output)
