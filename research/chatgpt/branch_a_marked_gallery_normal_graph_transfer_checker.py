#!/usr/bin/env python3
"""Exact normal-graph support transfer on the marked hexagon gallery.

Standalone: Python standard library only, no cached certificates or network.
The universal native coefficient is L_d*X_d. The beta family is L_d=beta.
All 430 states and the separate occurrence-35 factor are reconstructed.
Negative exponents are permitted only in the slope variables, and are removed
in the displayed two-slope regularized map. They never occur in X variables.
"""
from __future__ import annotations
import argparse
from collections import Counter
from hashlib import sha256
from itertools import combinations
from math import gcd
from pathlib import Path
import json

DIAGS=('02','03','04','13','14','15','24','25','35')
PLUS=frozenset(('13','15','35'))
MINUS=frozenset(('02','04','24'))
SHORT=PLUS|MINUS
SHORT_ORDER=tuple(sorted(SHORT))
VARS=tuple('X'+d for d in DIAGS)+tuple('L'+d for d in DIAGS)+('beta',)
ZERO=(0,)*len(VARS)
COUNTS=Counter()
COMMIT='d1947b67a60d3e88ba77f4ca60ea02c2a306ee61'

def check(condition,label,detail=None):
    if not condition: raise AssertionError((label,detail))
    COUNTS[label]+=1

def put(v,k,c):
    if c:
        v[k]=v.get(k,0)+c
        if not v[k]:del v[k]

def add(a,b,s=1):
    v=dict(a)
    for k,c in b.items():put(v,k,s*c)
    return v

def mono(*names):
    p=[0]*len(VARS)
    for name in names:p[VARS.index(name)]+=1
    return tuple(p)

def survives(p):
    return not (any(p[DIAGS.index(a)]>0 for a in PLUS)
                and any(p[DIAGS.index(a)]>0 for a in MINUS))

def mul(v,p,s=1):
    out={}
    for (j,q),c in v.items():
        z=tuple(x+y for x,y in zip(p,q))
        if survives(z):put(out,(j,z),s*c)
    return out

def apply(M,v):
    out={}
    for (j,p),c in v.items():
        for (i,q),z in M.get(j,{}).items():
            pq=tuple(x+y for x,y in zip(p,q))
            if survives(pq):put(out,(i,pq),c*z)
    return out

def unit(j):return {(j,ZERO):1}
def restrict(v,ids):return {(j,p):c for (j,p),c in v.items() if j in ids}
def cond_order(p):return sum(p[DIAGS.index(a)] for a in SHORT)

def beta_sub(v):
    out={}
    for (j,p),c in v.items():
        q=list(p[:9])+[0]*9+[sum(p[9:18])+p[18]]
        put(out,(j,tuple(q)),c)
    return out

def set_zero(v,names):
    ids=[VARS.index(a) for a in names]
    check(all(all(p[k]>=0 for k in ids) for j,p in v),'specialization_has_no_pole',names)
    return {(j,p):c for (j,p),c in v.items() if all(p[k]==0 for k in ids)}

def crosses(a,b):
    i,j=map(int,a);k,l=map(int,b)
    return i<k<j<l or k<i<l<j

def parity(seq):
    return (-1)**sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))

def perm_diag(a,rot=0,ref=False):
    f=lambda v: ((2-v if ref else v)+2*rot)%6
    return ''.join(map(str,sorted((f(int(a[0])),f(int(a[1]))))))

class Model:
    def __init__(self,occ='35'):
        self.occ=occ
        self.faces=[F for n in range(4) for F in combinations(DIAGS,n)
                    if all(not crosses(a,b) for a,b in combinations(F,2))]
        self.states=[(F,H,e) for F in self.faces for n in range(len(F)+1)
                     for H in combinations(F,n) for e in (0,1)]
        self.idx={v:j for j,v in enumerate(self.states)}
        self.deg={j:3-len(F)+len(H)+e for j,(F,H,e) in enumerate(self.states)}
        self.V={j for j,(F,H,e) in enumerate(self.states) if frozenset(F) in (PLUS,MINUS)}
        self.Vminus={j for j,(F,H,e) in enumerate(self.states) if frozenset(F)==MINUS}
        self.Q={j for j,(F,H,e) in enumerate(self.states) if not set(F)&SHORT}
        self.d={j:{} for j in self.idx.values()}
        fs=set(self.faces)
        for j,(F,H,e) in enumerate(self.states):
            for a in DIAGS:
                FF=tuple(sorted(F+(a,)))
                if a not in F and FF in fs:
                    put(self.d[j],(self.idx[FF,H,e],mono('X'+a)),(-1)**sum(b<a for b in F))
            for k,a in enumerate(H):
                put(self.d[j],(self.idx[F,H[:k]+H[k+1:],e],mono('L'+a,'X'+a)),
                    (-1)**(3-len(F)+k))
            if e:
                put(self.d[j],(self.idx[F,H,0],mono('X'+occ)),(-1)**(3-len(F)+len(H)))
        self.db={j:beta_sub(v) for j,v in self.d.items()}
        self.dv={j:{(i,p):c for (i,p),c in v.items() if self.states[i][0]==self.states[j][0]}
                 for j,v in self.d.items()}
        check((len(self.states),len(self.V),len(self.Q))==(430,32,14),'complete_state_census')
        check(Counter(map(len,self.faces))=={0:1,1:9,2:21,3:14},'face_census')
        for j,col in self.d.items():
            check(not apply(self.d,col),'graph_d_squared',j)
            check(not apply(self.dv,self.dv[j]),'vertical_d_squared',j)
            check(all(self.deg[i]==self.deg[j]-1 for i,p in col),'homological_degrees',j)
        self.T={j:self.shear(j,False) for j in self.idx.values()}
        self.Ti={j:self.shear(j,True) for j in self.idx.values()}
        for j in self.idx.values():
            check(apply(self.T,self.Ti[j])==unit(j),'shear_inverse_left',j)
            check(apply(self.Ti,self.T[j])==unit(j),'shear_inverse_right',j)
            check(apply(self.d,self.T[j])==apply(self.T,self.dv[j]),'normal_shear_chain_equation',j)
            for (i,p),c in self.T[j].items():
                check(self.deg[i]==self.deg[j],'shear_degree_zero',j)
                check(set(self.states[j][0])<=set(self.states[i][0]),'shear_adds_only_cofaces',j)
                check(all(q==0 for q in p[:9]),'shear_never_inverts_occurrence',j)
                f,h,e=self.states[j];ff,hh,ee=self.states[i]
                src=[-int(a in f)+int(a in h)+e*int(a==occ) for a in DIAGS]
                dst=[-int(a in ff)+int(a in hh)+ee*int(a==occ)+p[k] for k,a in enumerate(DIAGS)]
                check(src==dst,'shear_preserves_occurrence_weights',j)
                check(all(int(a in h)==int(a in hh)+p[9+k] for k,a in enumerate(DIAGS)),
                      'shear_preserves_each_slope_normal_weight',j)

    def shear(self,j,inverse):
        F,H,e=self.states[j];out={}
        for A in self.faces:
            if set(A)&set(F):continue
            FF=tuple(sorted(F+A));HH=tuple(sorted(H+A))
            if (FF,HH,e) not in self.idx:continue
            k=len(A)
            n=k*(3-len(F))-k*(k-1)//2+sum(sum(f<a for f in F)+sum(h<a for h in H) for a in A)
            p=[0]*len(VARS)
            for a in A:p[9+DIAGS.index(a)]-=1
            put(out,(self.idx[FF,HH,e],tuple(p)),(-1)**(n+k*inverse))
        return out

    def retract(self,allowed):
        check(all(i in allowed for j in allowed for i,p in self.d[j]),'carrier_is_subcomplex')
        R={j:apply(self.T,restrict(self.Ti[j],allowed)) for j in self.idx.values()}
        for j,col in R.items():
            check(all(i in allowed for i,p in col),'transfer_has_required_support',j)
            check(apply(self.d,col)==apply(R,self.d[j]),'transfer_chain_equation',j)
            if j in allowed:check(col==unit(j),'transfer_fixes_carrier',j)
            check(apply(R,col)==col,'transfer_idempotent',j)
        return R

    def action(self,v,rot=0,ref=False):
        out={}
        for (j,p),c in v.items():
            F,H,e=self.states[j];FF=[perm_diag(a,rot,ref) for a in F];HH=[perm_diag(a,rot,ref) for a in H]
            i=self.idx[tuple(sorted(FF)),tuple(sorted(HH)),e]
            q=[0]*len(VARS)
            for k,a in enumerate(DIAGS):
                dst=DIAGS.index(perm_diag(a,rot,ref));q[dst]=p[k];q[9+dst]=p[9+k]
            q[18]=p[18]
            put(out,(i,tuple(q)),c*((-1) if ref else 1)*parity(FF)*parity(HH))
        return out

def homogeneous_kernel(columns,label):
    """Saturated integral kernel using signed-unit pivots after row gcd reduction."""
    variables=sorted(columns)
    rows={}
    for j,col in columns.items():
        for k,c in col.items():put(rows.setdefault(k,{}),j,c)
    def primitive(row):
        g=0
        for c in row.values():g=gcd(g,abs(c))
        return {j:c//g for j,c in row.items()} if g else {}
    rows={k:primitive(v) for k,v in rows.items() if v}
    original={k:dict(v) for k,v in rows.items()};piv=[]
    while rows:
        degree=Counter(j for v in rows.values() for j in v)
        options=[(len(v)*degree[j],repr(k),j,k) for k,v in rows.items() for j,c in v.items() if abs(c)==1]
        check(bool(options),'integral_unit_kernel_pivot',label)
        _,_,j,k=min(options)
        v=rows.pop(k);sg=v[j];v={q:c*sg for q,c in v.items()};piv.append((j,v))
        for kk,row in list(rows.items()):
            if j in row:
                row=primitive(add(row,v,-row[j]))
                if row:rows[kk]=row
                else:del rows[kk]
    free=[j for j in variables if j not in {p for p,v in piv}]
    basis=[]
    for j in free:
        v={j:1}
        for p,row in reversed(piv):put(v,p,-sum(c*v.get(q,0) for q,c in row.items() if q!=p))
        for row in original.values():check(sum(c*v.get(q,0) for q,c in row.items())==0,'kernel_satisfies_every_row',label)
        basis.append(v)
    return {'basis':basis,'free':free,'rank':len(piv),'pivots':piv}

def combine(vs,co):
    v={}
    for j,c in co.items():v=add(v,vs[j],c)
    return v

def source_resolution():
    ids={a:i for i,a in enumerate(SHORT_ORDER)};rel=[]
    for sh in (sorted(PLUS),sorted(MINUS)):
        for a,b in combinations(sh,2):
            rel.append((('K',a,b),{((0,ids[b]),mono('X'+a)):1,((0,ids[a]),mono('X'+b)):-1}))
        for n in sorted(SHORT-set(sh)):
            for a in sh:rel.append((('M',n,a),{((0,ids[a]),mono('X'+n)):1}))
    ri={name:j for j,(name,v) in enumerate(rel)};sy=[]
    for sh in (sorted(PLUS),sorted(MINUS)):
        opp=sorted(SHORT-set(sh));a,b,c=sh
        sy.append({((1,ri['K',b,c]),mono('X'+a)):1,((1,ri['K',a,c]),mono('X'+b)):-1,
                   ((1,ri['K',a,b]),mono('X'+c)):1})
        for n in opp:
            for a,b in combinations(sh,2):sy.append({((1,ri['K',a,b]),mono('X'+n)):1})
        for p in sh:
            for n in opp:
                for a in sh:sy.append({((1,ri['M',n,p]),mono('X'+a)):1})
            for n,m in combinations(opp,2):
                sy.append({((1,ri['M',m,p]),mono('X'+n)):1,((1,ri['M',n,p]),mono('X'+m)):-1})
    src={(0,i):{} for i in range(6)}
    src.update({(1,j):v for j,(name,v) in enumerate(rel)})
    src.update({(2,j):v for j,v in enumerate(sy)})
    check((len(rel),len(sy))==(24,92),'source_relation_counts')
    augmentation={(0,i):{(0,mono('X'+a)):1} for i,a in enumerate(SHORT_ORDER)}
    for j,(name,col) in enumerate(rel):
        check(not apply(augmentation,col),'ideal_augmentation_respects_each_relation',name)
    for j,v in src.items():check(not apply(src,v),'source_relations_square_zero',j)
    return src,rel

def map_delta(src,dt,mp,degree):
    out={}
    for sid,col in src.items():
        v=apply(dt,mp.get(sid,{}))
        for (s,p),c in col.items():v=add(v,mul(mp.get(s,{}),p,-((-1)**degree)*c))
        if v:out[sid]=v
    return out

def serial_chain(v,M):
    return [{'state_index':j,'face':list(M.states[j][0]),'native_marks':list(M.states[j][1]),
             'occurrence_partner':M.states[j][2],'coefficient':c,'exponents':list(p)}
            for (j,p),c in sorted(v.items())]

def serial_matrix(mat,M):return [{'source':j,'image':serial_chain(v,M)} for j,v in sorted(mat.items()) if v]

def execute(path):
    M=Model();ids=set(M.d)
    gallery_faces={('13','35'),('03','35'),('13','15','35'),('03','13','35'),('02','03','35')}
    G={j for j,(F,H,e) in enumerate(M.states) if F in gallery_faces}
    F35={j for j,(F,H,e) in enumerate(M.states) if '35' in F}
    GB=G|M.Vminus;DB=F35|M.Vminus
    check((len(G),len(F35),len(GB),len(DB))==(64,124,80,140),'gallery_facet_endpoint_counts')
    Rg=M.retract(G);Rboth=M.retract(GB)
    Rlocal={j:Rg[j] for j in F35};RlocalB={j:Rboth[j] for j in DB}
    # A complete closed formula for the 64 by 124 matrix.
    for j in F35:
        F,H,e=M.states[j];expected={}
        def mark_image(face,added,denominators,sign):
            pp=[0]*len(VARS)
            for a in denominators:pp[VARS.index('L'+a)]-=1
            return {(M.idx[tuple(face),tuple(sorted(set(H)|set(added))),e],tuple(pp)):sign}
        if j in G:expected=unit(j)
        elif F==('35',):
            expected=add(mark_image(('03','35'),('03',),('03',),-1),
                         mark_image(('13','35'),('13',),('13',),-1))
            expected=add(expected,mark_image(('03','13','35'),('03','13'),('03','13'),1))
        elif F==('02','35'):
            expected=mark_image(('02','03','35'),('03',),('03',),(-1)**(1+int('02' in H)))
        elif F==('15','35'):
            expected=mark_image(('13','15','35'),('13',),('13',),1)
        check(Rlocal[j]==expected,'all_local_transfer_case_formulas',j)
    allowed_negative={VARS.index('L03'),VARS.index('L13')}
    for j,col in Rlocal.items():
        for (i,p),c in col.items():
            check(all(x>=0 or k in allowed_negative for k,x in enumerate(p)),'only_two_slope_denominators',(j,i))
            check(all(p[k]>=-1 for k in allowed_negative),'only_simple_separate_slope_poles',(j,i))
    regular={j:mul(v,mono('L03','L13')) for j,v in Rlocal.items()}
    for j,col in regular.items():
        check(all(min(p)>=0 for i,p in col),'regularized_transfer_is_polynomial',j)
        check(apply(M.d,col)==apply(regular,M.d[j]),'regularized_chain_equation',j)
        if j in G:check(col==mul(unit(j),mono('L03','L13')),'regularized_restriction_is_two_slope_factor',j)
    symbol={j:set_zero(v,('L03','L13')) for j,v in regular.items()}
    dz={j:set_zero(v,('L03','L13')) for j,v in M.d.items()}
    nonzero={j:v for j,v in symbol.items() if v}
    check(len(nonzero)==4,'four_state_double_normal_symbol')
    for H in ((),('35',)):
        for e in (0,1):
            j=M.idx[('35',),H,e];i=M.idx[('03','13','35'),tuple(sorted(('03','13')+H)),e]
            check(symbol[j]==unit(i),'primitive_ordered_double_normal_insertion',(H,e))
    for j,col in symbol.items():
        check(apply(dz,col)==apply(symbol,dz[j]),'central_symbol_chain_equation',j)
        check(not restrict(col,M.V) and not restrict(col,M.Q),'central_symbol_has_zero_endpoint_and_Q',j)

    # Actual two endpoint triangles. Graded projection v is NOT assumed to be a chain map.
    quotient_src=DB-M.V;quotient_tgt=GB-M.V
    dES={j:restrict(M.d[j],quotient_src) for j in quotient_src}
    dET={j:restrict(M.d[j],quotient_tgt) for j in quotient_tgt}
    dV={j:restrict(M.d[j],M.V) for j in M.V}
    cS={j:restrict(M.d[j],M.V) for j in quotient_src}
    cT={j:restrict(M.d[j],M.V) for j in quotient_tgt}
    RE={j:restrict(RlocalB[j],quotient_tgt) for j in quotient_src}
    A={j:restrict(RlocalB[j],M.V) for j in quotient_src}
    for j in quotient_src:
        check(apply(dET,RE[j])==apply(RE,dES[j]),'endpoint_quotient_chain_map',j)
        lhs=add(apply(cT,RE[j]),cS[j],-1)
        rhs=add(apply(A,dES[j]),apply(dV,A[j]),-1)
        check(lhs==rhs,'complete_endpoint_connector_comparison_cell',j)
    for j in M.V:check(RlocalB[j]==unit(j),'both_endpoint_packets_fixed_pointwise',j)

    # Relabelling covariance, including the moved occurrence label.
    for rot in range(3):
        for ref in (False,True):
            Mt=M if not (rot or ref) else Model(perm_diag('35',rot,ref))
            destG={Mt.idx[(tuple(sorted(perm_diag(a,rot,ref) for a in F)),
                          tuple(sorted(perm_diag(a,rot,ref) for a in H)),e)]
                   for j,(F,H,e) in enumerate(M.states) if j in GB}
            rt=Mt.retract(destG)
            for j in ids:
                check(apply(Mt.d,M.action(unit(j),rot,ref))==M.action(M.d[j],rot,ref),
                      'dihedral_differential_covariance',(rot,ref,j))
                check(M.action(Rboth[j],rot,ref)==apply(rt,M.action(unit(j),rot,ref)),
                      'support_transfer_transports_marked_gallery',(rot,ref,j))

    rb={j:beta_sub(v) for j,v in Rboth.items()}
    rlocal={j:beta_sub(v) for j,v in RlocalB.items()}
    def E(F):F=tuple(F);return unit(M.idx[F,F,1])
    Ua=add(add(E(('02','03','35')),E(('02','25','35'))),mul(E(('02','35')),mono('beta')),-1)
    Ub=add(mul(E(('35',)),mono('beta','beta')),mul(add(E(('03','35')),E(('25','35'))),mono('beta')))
    L03=add(E(('03','13','35')),mul(E(('13','35')),mono('beta')),-1)
    check(not apply(rlocal,Ua),'first_facet_comparison_transfers_to_zero')
    check(apply(rlocal,Ub)==L03,'second_facet_comparison_has_two_term_local_image')
    bad=restrict(apply(M.db,L03),M.V)
    badstate=M.idx[('13','15','35'),('13','35'),1]
    check(bad=={(badstate,mono('beta','X15')):1},'local_incoming_endpoint_defect_is_primitive')
    check(not restrict(L03,M.V),'local_homotopy_has_zero_endpoint_value')
    # The actual off-diagonal comparison reproduces rather than suppresses the defect.
    Ab={j:beta_sub(v) for j,v in A.items()}
    check(not apply(Ab,Ub),'offdiagonal_comparison_on_Ub_zero')
    check(apply(Ab,apply(M.db,Ub))==bad,'offdiagonal_comparison_accounts_for_incoming_defect')

    # Reconstruct all nine previously allowed extension homotopies from exact coefficient equations.
    hslots=[]
    for F in M.faces:
        j=M.idx[F,F,1]
        if j in M.V or j in M.Q:continue
        hslots.append(mul(unit(j),mono(*(['beta']*(3-len(F))))))
    eq={}
    for k,U in enumerate(hslots):
        dU=apply(M.db,U)
        eq[k]={('incoming_endpoint',j,p):c for (j,p),c in dU.items() if j in M.V}
        eq[k].update({('nonconductor',j,p):c for (j,p),c in dU.items() if not cond_order(p)})
    hk=homogeneous_kernel(eq,'all_coherent_homotopies')
    U9=[combine(hslots,c) for c in hk['basis']]
    check(len(U9)==9,'nine_global_comparisons_reconstructed')
    src,relations=source_resolution();sid35=(0,SHORT_ORDER.index('35'))
    fmaps=[];rhmaps=[];rfmaps=[]
    for k,U in enumerate(U9):
        h={sid35:U};f=map_delta(src,M.db,h,1)
        check(not map_delta(src,M.db,f,0),'all_source_relation_equations_before_transfer',k)
        for col in h.values():
            check(not restrict(col,M.V) and not restrict(col,M.Q) and not restrict(apply(M.db,col),M.V),
                  'input_homotopy_frame',k)
        for col in f.values():
            check(all(cond_order(p)>0 for j,p in col),'input_ideal_map_conductor_values',k)
            check(not restrict(col,M.V) and not restrict(col,M.Q) and not restrict(apply(M.db,col),M.V),
                  'input_ideal_map_full_frame',k)
        rh={s:apply(rb,v) for s,v in h.items() if apply(rb,v)}
        rf={s:apply(rb,v) for s,v in f.items() if apply(rb,v)}
        check(map_delta(src,M.db,rh,1)==rf,'transferred_restriction_homotopy_and_all_relations',k)
        check(not map_delta(src,M.db,rf,0),'transferred_ideal_map_chain_equation',k)
        check(all(min(p)>=0 for v in list(rh.values())+list(rf.values()) for j,p in v),
              'transferred_nine_maps_remain_polynomial',k)
        fmaps.append(f);rhmaps.append(rh);rfmaps.append(rf)
    Uim=[apply(rb,U) for U in U9]
    imker=homogeneous_kernel(dict(enumerate(Uim)),'localized_global_image')
    check(imker['rank']==3,'nine_to_three_image_rank')
    epminus=E(tuple(sorted(MINUS)));epplus=E(tuple(sorted(PLUS)))
    im_basis=[L03,epminus,epplus]
    for k,V in enumerate(Uim):
        co={0:V.get((M.idx[('03','13','35'),('03','13','35'),1],ZERO),0),
            1:V.get(next(iter(epminus)),0),2:V.get(next(iter(epplus)),0)}
        check(combine(im_basis,co)==V,'local_image_three_explicit_coordinates',k)
    fd={}
    for k,V in enumerate(Uim):
        col={('value',j,p):c for (j,p),c in restrict(V,M.V).items()}
        col.update({('boundary',j,p):c for (j,p),c in restrict(apply(M.db,V),M.V).items()})
        fd[k]=col
    fker=homogeneous_kernel(fd,'preserve_original_full_endpoint_frame_after_transfer')
    check(len(fker['basis'])==6,'frame_kernel_six_inputs')
    check(all(not combine(Uim,c) for c in fker['basis']), 'no_nonzero_transferred_image_retains_zero_frame')
    # Three endpoint readouts give a unimodular detector on the three image generators.
    detector=[]
    for V in im_basis:
        detector.append([V.get(next(iter(epminus)),0),V.get(next(iter(epplus)),0),
                         apply(M.db,V).get((badstate,mono('beta','X15')),0)])
    check(detector==[[0,0,1],[1,0,0],[0,1,-1]],'three_endpoint_detectors_are_unimodular')

    # Strict reflection invariants computed in the original face basis, not by averaging.
    rawcoords={next(iter(U))[0]:k for k,U in enumerate(hslots)}; invslots=[];seen=set()
    for k,U in enumerate(hslots):
        j=next(iter(U))[0]
        if j in seen:continue
        sU=M.action(U,0,True);j2=next(iter(sU))[0]
        seen.update((j,j2))
        if j==j2:
            check(sU==add({},U,-1),'fixed_face_is_reflection_odd')
        else:
            V=add(U,sU)
            check(M.action(V,0,True)==V,'integral_reflection_pair')
            invslots.append(V)
    ieq={}
    for k,U in enumerate(invslots):
        dU=apply(M.db,U);v={('incoming',j,p):c for (j,p),c in dU.items() if j in M.V}
        v.update({('constant',j,p):c for (j,p),c in dU.items() if not cond_order(p)})
        ieq[k]=v
    ik=homogeneous_kernel(ieq,'invariant_input_comparisons')
    Uinv=[combine(invslots,c) for c in ik['basis']]
    check(len(Uinv)==3,'three_invariant_inputs')
    rims=[apply(rb,U) for U in Uinv]
    check(homogeneous_kernel(dict(enumerate(rims)),'invariant_local_image')['rank']==1,
          'three_invariant_families_to_one_local_direction')
    localgen=add(L03,epplus)
    for j,V in enumerate(rims):
        coefficient=V.get(next(iter(epplus)),0)
        check(V==add({},localgen,coefficient),'invariant_local_generator_is_L03_plus_endpoint',j)

    # Explicit failure of a polynomial, coface-only retraction at each slope divisor.
    j=M.idx[('02','35'),(),0]
    check(Rlocal[j]=={(M.idx[('02','03','35'),('03',),0],tuple(-1 if k==VARS.index('L03') else 0 for k in range(len(VARS)))):-1},
          'first_slope_pole_witness')
    j2=M.idx[('15','35'),(),0]
    check(any(p[VARS.index('L13')]==-1 for i,p in Rlocal[j2]),'second_slope_pole_witness')
    # Modulo L03=X02=X35=0, a coface-only degree-one image at {02,03,35}
    # has zero differential, whereas the source boundary has surviving X03.
    for H,e in [(('02',),0),(('03',),0),(('35',),0),((),1)]:
        v=M.d[M.idx[('02','03','35'),H,e]]
        check(not set_zero(v,('L03','X02','X35')),'first_divisor_no_polynomial_retraction_test',(H,e))
    check(bool(set_zero({(M.idx[('02','03','35'),(),0],mono('X03')):1},('L03','X02','X35'))),
          'first_divisor_source_incidence_survives')
    for H,e in [(('13',),0),(('15',),0),(('35',),0),((),1)]:
        v=M.d[M.idx[('13','15','35'),H,e]]
        check(not set_zero(v,('L13','X15','X35')),'second_divisor_no_polynomial_retraction_test',(H,e))
    check(bool(set_zero({(M.idx[('13','15','35'),(),0],mono('X13')):1},('L13','X15','X35'))),
          'second_divisor_source_incidence_survives')

    local_beta={j:beta_sub(v) for j,v in Rlocal.items()}
    check(min(p[18] for v in local_beta.values() for j,p in v)==-2,'common_regulator_pole_order_exactly_two')
    lower_degree={k:sum(1 for j in F35 if M.deg[j]==k) for k in range(5)}
    target_degree={k:sum(1 for j in G if M.deg[j]==k) for k in range(5)}
    data={
      'schema':'marici.branchA.marked_gallery_normal_graph_transfer.v1',
      'scope':{
        'coefficient_ring':'Z[X_d,L_d,beta]/(X_minus X_plus)',
        'universal_graph':'u_d=L_d X_d; slopes L_d are graph parameters, not identified with channel coordinates',
        'physical_graph':'L_d=beta v_d(X_d), v_d(0)=1, after scalar extraction; beta!=0 for the retraction',
        'beta_family':'L_d=beta after the invertible v_d frame changes',
        'source_occurrence_partner':'35, retained separately from native normal 35',
        'physical_Delta_identified':False,
        'six_functor_Gysin_identified':False,
        'regularized_symbol_not_assumed_to_select_physical_map':True},
      'variables':list(VARS),
      'native_target_states':430,
      'state_basis':[{'index':j,'face':list(F),'marks':list(H),'occurrence':e,'degree':M.deg[j]}
                      for j,(F,H,e) in enumerate(M.states)],
      'graph_differential':serial_matrix(M.d,M),
      'vertical_differential':serial_matrix(M.dv,M),
      'shear':serial_matrix(M.T,M),'inverse_shear':serial_matrix(M.Ti,M),
      'carrier_counts':{'facet':len(F35),'gallery':len(G),'facet_with_negative_endpoint':len(DB),
                        'gallery_with_negative_endpoint':len(GB)},
      'local_degree_counts':{'source':lower_degree,'target':target_degree},
      'local_transfer':serial_matrix(Rlocal,M),
      'local_transfer_entries':sum(map(len,Rlocal.values())),
      'local_transfer_with_both_endpoints_entries':sum(map(len,RlocalB.values())),
      'global_transfer_entries':sum(map(len,Rboth.values())),
      'endpoint_comparison_cell_entries':sum(map(len,A.values())),
      'local_transfer_with_both_endpoints':serial_matrix(RlocalB,M),
      'global_transfer_with_both_endpoints':serial_matrix(Rboth,M),
      'regularized_transfer':serial_matrix(regular,M),
      'ordered_double_slope_symbol':serial_matrix(nonzero,M),
      'exact_slope_poles':['L03','L13'],
      'common_beta_pole_order':2,
      'endpoint_quotient_map':serial_matrix(RE,M),
      'endpoint_comparison_cell':serial_matrix(A,M),
      'endpoint_connector_source':serial_matrix(cS,M),
      'endpoint_connector_target':serial_matrix(cT,M),
      'two_facet_homotopies':{'Ua':serial_chain(Ua,M),'Ub':serial_chain(Ub,M)},
      'two_facet_images':{'Ua':[],'Ub':serial_chain(L03,M)},
      'Ub_incoming_endpoint_term':serial_chain(bad,M),
      'nine_input_homotopies':[serial_chain(v,M) for v in U9],
      'nine_transferred_homotopies':[serial_chain(v,M) for v in Uim],
      'nine_transferred_source_maps':[
        [{'source':list(s),'image':serial_chain(v,M)} for s,v in sorted(mp.items())] for mp in rfmaps],
      'global_image_rank':3,'global_image_basis':[serial_chain(v,M) for v in im_basis],
      'zero_endpoint_frame_input_kernel_rank':6,'nonzero_frame_preserving_transferred_image_rank':0,
      'endpoint_detector_columns':detector,
      'invariant_input_homotopies':[serial_chain(v,M) for v in Uinv],
      'invariant_images':[serial_chain(v,M) for v in rims],
      'invariant_image_rank':1,'invariant_local_generator':serial_chain(localgen,M),
      'sources':[
       {'path':'research/voevodsky/check_absolute_unlocalized_support_pc.rs','commit':COMMIT,
        'blob':'b967151cb0ee822e2361b9334a4ab26082c12682'},
       {'path':'src/ledger/20260814-106 Marked Log Gallery Secondary Class and the Global Yoneda Gap.md',
        'commit':COMMIT,'blob':'d9ac9420e7360013ff6acde34df51a4941b34101'},
       {'path':'research/voevodsky/check_d03_formal_support_purity.rs','commit':COMMIT,
        'blob':'acaabf367b24029d9dbfa371ee1983d392b393fa'}]
    }
    digest=sha256(json.dumps(data,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    data['mathematical_data_sha256']=digest
    data['checks_by_family']=dict(sorted(COUNTS.items()));data['exact_checks']=sum(COUNTS.values())
    data['checker_sha256']=sha256(Path(__file__).read_bytes()).hexdigest()
    path.write_text(json.dumps(data,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'certificate':str(path),'checks':data['exact_checks'],'mathematical_data_sha256':digest,
                      'local_matrix':[64,124],'local_entries':data['local_transfer_entries'],
                      'global_transfer_image_rank':3,'invariant_image_rank':1,
                      'fixed_frame_nonzero_image_rank':0},sort_keys=True))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,
       default=Path(__file__).with_name('branch_a_marked_gallery_normal_graph_transfer_certificate.json'))
    execute(p.parse_args().output)
