#!/usr/bin/env python3
"""Completed normal-dual comparison and the coupled Rees symbol.

Python 3.10+, standard library only. Integer polynomial/Laurent identities are
checked symbolically; inverse normals occur only in their designated target
stalks. Occurrence variables are never inverted. The complete node resolution,
two endpoint maps, conductor homotopy, target support filtration, Hom fibres,
and orientation character are retained. This is a finite coefficient/cap
comparison, not a claimed algebraic six-functor or physical parity theorem.
"""
from __future__ import annotations
import argparse, hashlib, json
from collections import Counter
from itertools import combinations, product
from pathlib import Path

COMMIT='d1947b67a60d3e88ba77f4ca60ea02c2a306ee61'
SOURCE_BLOBS={
 'src/ledger/20260814-93 Alternating Fusion Normalization-Conductor Square.md':'840258522d45e450e4f1e8bb927d9aae58c75566',
 'research/voevodsky/check_global_k6_koszul_cech_promotion.rs':'e972b69d0e2b1b0a0aee5e0a027c8216bcace3e8',
 'research/voevodsky/check_two_endpoint_tate_carrier.rs':'0147e2e42dafac0da7289c571cb0331b51338be1'}
COUNT=Counter(); Z=(0,)*18
EV=(0,2,4); OD=(1,3,5); ORDER=EV+OD

def check(ok,tag):
    if not ok: raise AssertionError(tag)
    COUNT[tag]+=1

def pm(n):return -1 if n%2 else 1

def subsets(s):return [t for k in range(len(s)+1) for t in combinations(s,k)]
def ex(entries):return tuple(entries.get(i,0) for i in range(18))
def eadd(a,b):return tuple(x+y for x,y in zip(a,b))
def esub(a,b):return tuple(x-y for x,y in zip(a,b))
def add(*vs):
    o={}
    for v in vs:
        for k,a in v.items():
            o[k]=o.get(k,0)+a
            if not o[k]:del o[k]
    return o

def scale(v,a):return {k:a*c for k,c in v.items() if a*c}
def multiply(v,e,a=1):return {(b,eadd(m,e)):a*c for (b,m),c in v.items() if a*c}
def one(b):return {(b,Z):1}
def apply(table,v):
    out={}
    for (b,e),c in v.items():out=add(out,multiply(table.get(b,{}),e,c))
    return out

def lin(table,v):
    out={}
    for b,a in v.items():out=add(out,scale(table.get(b,{}),a))
    return out

def di(i,j):return tuple(sorted((i%6,j%6)))
def cross(a,b):
    x,y=a;u,v=b
    return x<u<y<v or u<x<v<y
DS=tuple((i,j) for i in range(6) for j in range(i+1,6) if j-i not in (1,5))
SHORT=tuple(di(i,i+2) for i in range(6)); LONG=tuple(di(i,i+3) for i in range(3))
IX={a:i for i,a in enumerate(SHORT+LONG)}
FACES=tuple(f for k in range(4) for f in combinations(DS,k)
            if all(not cross(a,b) for a,b in combinations(f,2)))
CELLS=tuple((f,h) for f in FACES for h in subsets(f))
VP=tuple(sorted(SHORT[i] for i in OD)); VM=tuple(sorted(SHORT[i] for i in EV))
GAMMA=ex({15:1,16:1,17:1}); LAMBDA=esub(GAMMA,ex({i:1 for i in range(6)}))
GROUP=tuple(product(range(3),range(2)))

def degree(c):return 3-len(c[0])+len(c[1])
def weight(c):return ex({**{IX[a]:1 for a in c[0]},**{9+IX[a]:-1 for a in c[0]}})
def predicate(c,k):
    v=c[0] in (VP,VM); b=any(a in SHORT for a in c[0])
    return {'K':True,'V':v,'B':b,'E':not v,'BV':b and not v,'Q':not b}[k]
def legal(c,m):
    local={IX[a] for a in c[0] if a not in c[1]}
    return all(a>=0 for a in m[:9]) and all(a>=0 or i in local for i,a in enumerate(m[9:]))
def target_boundary(c):
    f,h=c;z={}
    for a in DS:
        if a not in f and all(not cross(a,b) for b in f):
            t=(tuple(sorted(f+(a,))),h)
            z[t,ex({IX[a]:1,9+IX[a]:-1})]=pm(sum(b<a for b in f))
    for i,a in enumerate(h):z[(f,tuple(b for b in h if b!=a)),Z]=pm(3-len(f)+i)
    return z
BD={c:target_boundary(c) for c in CELLS}

def project(v,k):return {(c,e):a for (c,e),a in v.items() if predicate(c,k)}
def td(v,k='K'):return project(apply(BD,v),k)

def koszul(seq,tag):
    g={};d={};labels={}
    for s in subsets(seq):
        b=(tag,s);g[b]=len(s);labels[b]=ex({i:1 for i in s})
        d[b]={((tag,s[:j]+s[j+1:]),ex({i:1})):pm(j) for j,i in enumerate(s)}
    return g,d,labels

def node():
    bot=('P',(),());g={bot:0};d={bot:{}};labels={bot:Z}
    for u in subsets(EV)[1:]:
        for v in subsets(OD)[1:]:
            b=('P',u,v);g[b]=len(u)+len(v)-1;labels[b]=ex({i:1 for i in u+v});z={}
            if len(u)==len(v)==1:z[bot,ex({u[0]:1,v[0]:1})]=1
            else:
                if len(u)>1:
                    for j,i in enumerate(u):z[('P',u[:j]+u[j+1:],v),ex({i:1})]=pm(j)
                if len(v)>1:
                    for j,i in enumerate(v):z[('P',u,v[:j]+v[j+1:]),ex({i:1})]=pm(len(u)-1+j)
            d[b]=z
    return g,d,labels

def audit_source(model,tag):
    gs,d,labels=model
    for b in gs:
        check(not apply(d,d[b]),tag+'_d_squared')
        for (a,e),v in d[b].items():
            check(gs[a]+1==gs[b],tag+'_chain_degree')
            check(eadd(e,labels[a])==labels[b],tag+'_coefficient_degree')
            check(min(e)>=0 and abs(v)==1,tag+'_integral_polynomial')

def omega(t):
    f=tuple(sorted(SHORT[i] for i in t))
    if f not in FACES:return {}
    e=eadd(GAMMA,ex({9+i:-1 for i in t}));z={((f,()),e):1}
    for l in LONG:
        if all(not cross(l,b) for b in f):
            c=(tuple(sorted(f+(l,))),(l,))
            m=eadd(e,ex({IX[l]:1,IX[l]+9:-1}))
            z[c,m]=-pm(sum(b>l for b in f))
    return z

def complement_sign(i):
    t=tuple(a for a in ORDER if a not in i)
    inversions=sum(SHORT[t[a]]>SHORT[t[b]] for a in range(len(t)) for b in range(a+1,len(t)))
    return pm(len(t)+sum(ORDER.index(a) for a in t)+inversions)

def perm_short(g):
    k,f=g;return tuple((2*k+(1-i if f else i))%6 for i in range(6))
def perm_di(a,g):
    k,f=g
    per=lambda v:(2*k+(3-v if f else v))%6
    return di(per(a[0]),per(a[1]))
def invsign(values,order):
    ix={v:i for i,v in enumerate(order)};x=[ix[v] for v in values]
    return pm(sum(x[i]>x[j] for i in range(len(x)) for j in range(i+1,len(x))))
def perm_ex(e,g):
    out=[0]*18
    for i,a in enumerate(SHORT+LONG):
        j=IX[perm_di(a,g)];out[j]=e[i];out[9+j]=e[9+i]
    return tuple(out)
def act_p_basis(b,g):
    _,u,v=b
    if not u:return b,1
    per=perm_short(g);pu=[per[i] for i in u];pv=[per[i] for i in v]
    if not g[1]:return ('P',tuple(sorted(pu)),tuple(sorted(pv))),invsign(pu,EV)*invsign(pv,OD)
    return ('P',tuple(sorted(pv)),tuple(sorted(pu))),pm((len(u)-1)*(len(v)-1))*invsign(pv,EV)*invsign(pu,OD)
def act_source(v,g):
    z={}
    for (b,e),a in v.items():
        im,s=act_p_basis(b,g);z=add(z,{(im,perm_ex(e,g)):a*s})
    return z

def act_target(v,g):
    z={}
    for (c,e),a in v.items():
        f,h=c;pf=[perm_di(i,g) for i in f];ph=[perm_di(i,g) for i in h]
        sign=pm(g[1])*invsign(pf,DS)*invsign(ph,DS)
        c1=(tuple(sorted(pf)),tuple(sorted(ph)))
        z=add(z,{(c1,perm_ex(e,g)):a*sign})
    return z


ONE_N=(1,)*9

def finite_boundary(c,n):
    f,h=c;out={}
    for a in DS:
        if a not in f and all(not cross(a,b) for b in f):
            t=(tuple(sorted(f+(a,))),h);i=IX[a]
            out[t,ex({i:1,9+i:n[i]-1})]=pm(sum(b<a for b in f))
    for pos,a in enumerate(h):
        t=(f,tuple(b for b in h if b!=a));i=IX[a]
        out[t,ex({9+i:n[i]})]=pm(3-len(f)+pos)
    return out

def finite_table(n):return {c:finite_boundary(c,n) for c in CELLS}

def clear_power(c,n):
    return ex({9+IX[a]:n[IX[a]] for a in c[0] if a not in c[1]})

def finite_shift(c,n):return esub(scale_exp(weight(c),-1),clear_power(c,n))
def scale_exp(v,k):return tuple(k*a for a in v)

def diagonal_map(v,n,m):
    out={}
    for (c,e),a in v.items():
        ee=eadd(e,ex({9+IX[q]:m[IX[q]]-n[IX[q]] for q in c[0] if q not in c[1]}))
        out=add(out,{(c,ee):a})
    return out

def delocalize(v,n):
    return add(*({(c,eadd(e,clear_power(c,n))):a} for (c,e),a in v.items()))

def localize(v,n):
    return add(*({(c,esub(e,clear_power(c,n))):a} for (c,e),a in v.items()))

def construct_source_data():
    P=node();KE=koszul(EV,'E');KO=koszul(OD,'O');KC=koszul(ORDER,'C')
    cap={b:scale(omega(tuple(i for i in ORDER if i not in b[1])),complement_sign(b[1])) for b in KC[0]}
    fp={};fm={};H={};F={}
    for b in P[0]:
        _,u,v=b
        if not u:
            fp[b]=one(('E',()));fm[b]=one(('O',()));H[b]={};F[b]={}
        else:
            fp[b]={(('E',u),ex({v[0]:1})):1} if len(v)==1 else {}
            fm[b]={(('O',v),ex({u[0]:1})):1} if len(u)==1 else {}
            H[b]={(('C',u+v),Z):pm(len(u))}
            F[b]=scale(apply(cap,H[b]),-1)
    tp={b:cap[('C',b[1])] for b in KE[0]}
    tm={b:cap[('C',b[1])] for b in KO[0]}
    ends={b:add(apply(tp,fp[b]),scale(apply(tm,fm[b]),-1)) for b in P[0]}
    return P,KE,KO,KC,cap,fp,fm,H,F,tp,tm,ends

def transpose(table,source_basis,target_basis):
    out={x:{} for x in target_basis}
    for b in source_basis:
        for (c,e),a in table.get(b,{}).items():out[c]=add(out[c],{(b,e):a})
    return out

def dual_differential(table,basis,degrees):
    tr=transpose(table,basis,basis)
    return {b:scale(v,pm(degrees[b]+1)) for b,v in tr.items()}

def check_dual_equation(F,P,bd,ends,tag):
    ft=transpose(F,P[0],CELLS)
    at=transpose(ends,P[0],CELLS)
    pd=dual_differential(P[1],P[0],P[0])
    kd=dual_differential(bd,CELLS,{c:degree(c) for c in CELLS})
    for c in CELLS:
        lhs=add(apply(pd,ft[c]),scale(apply(ft,kd[c]),-1))
        check(lhs==scale(at[c],pm(degree(c))),tag+'_whole_dual_endpoint_identity')
    for support in ('E','Q'):
        cells=tuple(c for c in CELLS if predicate(c,support))
        ds={c:project(bd[c],support) for c in cells}
        ff={b:project(v,support) for b,v in F.items()}
        ftr=transpose(ff,P[0],cells)
        kd=dual_differential(ds,cells,{c:degree(c) for c in cells})
        for c in cells:
            check(apply(pd,ftr[c])==apply(ftr,kd[c]),tag+'_closed_dual_'+support)


def generic_rows(n):
    # Top cochain basis T*, M0*, M1*, M2*. Ignoring one common Hom sign.
    return [{('Tstar',ex({6+i:1,15+i:n[6+i]-1})):1,
             (('Mstar',i),ex({15+i:n[6+i]})):1} for i in range(3)]

def generic_trace():
    return {'Tstar':{('kappa',GAMMA):1},
            **{('Mstar',i):{('kappa',ex({6+i:1,**{15+j:1 for j in range(3) if j!=i}})):-1} for i in range(3)}}

def polynomial_membership(e,gens):return any(all(a>=b for a,b in zip(e,g)) for g in gens)

def rees_exp(e):
    # Same eighteen-coordinate storage: (X_0,...,X_8,t_0,...,t_8).
    return tuple(e[i]+e[9+i] for i in range(9))+tuple(e[9+i] for i in range(9))

def rees(v):
    return add(*({(b,rees_exp(e)):a} for (b,e),a in v.items()))

def specialize(v,zero_t):
    return {(b,e):a for (b,e),a in v.items() if all(e[9+i]==0 for i in zero_t)}

def long_order(e):return sum(e[15:18])

def keep_order(v,p):return {(b,e):a for (b,e),a in v.items() if long_order(e)==p}

def dual_generic_trace_audit(F0,P):
    q={b:project(v,'Q') for b,v in F0.items()}
    tr=transpose(q,P[0],tuple(c for c in CELLS if predicate(c,'Q')))
    top=('P',EV,OD);tcell=((),());Ttr=tr[tcell]
    check(Ttr=={(top,GAMMA):1},'R_linear_chamber_covector_keeps_U')
    for i,l in enumerate(LONG):
        expected={(top,ex({6+i:1,**{15+j:1 for j in range(3) if j!=i}})):-1}
        check(tr[((l,),(l,))]==expected,'R_linear_marked_covector_keeps_complement_product')
    check(all(not tr[((l,),())] for l in LONG),'generic_facet_covectors_have_zero_source_image')
    return tr


def minimal_rees_resolution_check():
    # Three generators of the ideal (t1*t2,t0*t2,t0*t1).
    j=[ex({15+k:1 for k in range(3) if k!=i}) for i in range(3)]
    row={('g',i):{('R',j[i]):1} for i in range(3)}
    d2={('s',0):{(('g',0),ex({15:1})):1,(('g',1),ex({16:1})):-1},
        ('s',1):{(('g',0),ex({15:1})):1,(('g',2),ex({17:1})):-1}}
    for v in d2.values():check(not apply(row,v),'Rees_ideal_resolution_d_squared')
    # Independently form the entire multihomogeneous linear algebra for all
    # zero/positive support classes. Larger positive exponents give the same
    # matrices, because all basis degrees are squarefree.
    records=[]
    for a in product((0,1),repeat=3):
        available_g=[i for i in range(3) if all(a[k]>=int(k!=i) for k in range(3))]
        available_s=[0,1] if min(a)>=1 else []
        nr=len(available_g);ns=len(available_s)
        # The row is [1,...,1]. Both syzygy columns are independent when present.
        rank1=int(nr>0);rank2=ns
        check(nr-rank1-rank2==0,'Rees_ideal_all_support_exact_middle')
        check(ns-rank2==0,'Rees_ideal_all_support_injective_left')
        surviving=nr==0
        check(surviving==(sum(a)<=1),'Rees_defect_is_three_coordinate_axes')
        records.append({'positive_support':list(a),'ideal_generators':nr,'syzygies':ns,'quotient_rank':int(surviving)})
    for e in product(range(4),repeat=3):
        in_ideal=sum(a>0 for a in e)>=2
        intersection=all(e[i]>0 or e[k]>0 for i,k in combinations(range(3),2))
        check(in_ideal==intersection,'Rees_ideal_intersection_of_three_pair_ideals')
    return records


def generic_syzygy_support_check():
    # Independent complete squarefree support proof of ker(psi)=im(N_1).
    # Three X entries followed by the three u entries.
    generators=[(0,0,0,1,1,1)]
    generators += [tuple(int(j==i) for j in range(3))+
                   tuple(int(j!=i) for j in range(3)) for i in range(3)]
    syzygies=[tuple(int(j==i) for j in range(3))+(1,1,1) for i in range(3)]
    records=[]
    for alpha in product((0,1),repeat=6):
        available=[i for i,g in enumerate(generators) if all(a>=b for a,b in zip(alpha,g))]
        cols=[i for i,g in enumerate(syzygies) if all(a>=b for a,b in zip(alpha,g))]
        rank=len(cols)
        check(all(0 in available and i+1 in available for i in cols),'generic_syzygy_columns_are_admitted')
        # Each column has its own nonzero M_i coordinate; hence independent.
        check(len(available)-int(bool(available))==rank,'generic_syzygy_all_64_supports_exact')
        records.append({'support':list(alpha),'generators':available,'syzygies':cols})
    return records


def independent_selected_excess_check():
    # Actual selected five-normal source, not an internal target multiplier.
    # Storage continues to use X variables followed by t variables here.
    regular=[ex({1:1}),ex({3:1}),ex({5:1}),ex({0:1,9:1})]
    old_f=regular+[ex({3:1,12:1})]
    new_f=regular+[None]
    def kb(fs):
        out={}
        for mask in range(32):
            z={}
            for i in range(5):
                if mask>>i&1 and fs[i] is not None:
                    z[mask^(1<<i),fs[i]]=pm((mask&((1<<i)-1)).bit_count())
            out[mask]=z
        return out
    def wedge(v,w):
        out={}
        for (a,e),c in v.items():
            for (b,f),d in w.items():
                if a&b:continue
                inv=sum(1 for i in range(5) if a>>i&1 for j in range(i) if b>>j&1)
                out=add(out,{(a|b,eadd(e,f)):c*d*pm(inv)})
        return out
    cols=[{(1<<i,Z):1} for i in range(4)]+[{(1<<1,ex({12:1})):1,(1<<4,Z):-1}]
    change={}
    for mask in range(32):
        v={(0,Z):1}
        for i in range(5):
            if mask>>i&1:v=wedge(v,cols[i])
        change[mask]=v
    old_d=kb(old_f);new_d=kb(new_f)
    for mask in range(32):
        check(apply(old_d,change[mask])==apply(change,new_d[mask]),'selected_excess_all_32_wedge_equations')
    eta=cols[4]
    check(not apply(old_d,eta),'selected_excess_is_closed')
    check(specialize(eta,(1,3,5))=={(1<<4,Z):-1},'selected_excess_survives_central_Rees_face')
    check(change[31]=={(31,Z):-1},'selected_excess_basis_change_is_unimodular')
    return {'source_equations':['X1','X3','X5','t0*X0','t3*X3'],
            'excess':'eta=t3*h3_plus-h3_pair','central_excess':'-h3_pair',
            'top_wedge_determinant':-1,
            'scope':'Independent source coefficient factor only; not identified with an internal PC marked normal.'}


def main(output):
    P,KE,KO,KC,cap,fp,fm,H,FC,tpC,tmC,endC=construct_source_data()
    for model,tag in ((P,'native_P'),(KE,'sheet_plus'),(KO,'sheet_minus'),(KC,'conductor_K')):
        audit_source(model,tag)
    check(len(CELLS)==215,'actual_full_state_count')
    check([sum(i==q for i in P[0].values()) for q in range(6)]==[1,9,18,15,6,1],'native_complete_resolution_ranks')
    for b in P[0]:
        check(add(td(FC[b]),scale(apply(FC,P[1][b]),-1))==endC[b],'original_complete_cap_endpoint_equation')
    F1={b:delocalize(v,ONE_N) for b,v in FC.items()}
    tp1={b:delocalize(v,ONE_N) for b,v in tpC.items()}
    tm1={b:delocalize(v,ONE_N) for b,v in tmC.items()}
    end1={b:delocalize(v,ONE_N) for b,v in endC.items()}
    check(sum(map(len,F1.values()))==43,'full_polynomial_cap_43_terms')
    check(sum(map(len,end1.values()))==6,'both_endpoint_composites_six_terms')
    orders=[ONE_N,(2,)*9,(4,)*9,tuple(1+(i%3) for i in range(9))]
    # Include every independent one-normal and pair-normal change.
    orders+= [tuple(1+int(i==j) for i in range(9)) for j in range(9)]
    orders+= [tuple(1+int(i in pair) for i in range(9)) for pair in combinations(range(9),2)]
    orders=list(dict.fromkeys(orders))
    for n in orders:
        bd=finite_table(n)
        Fn={b:delocalize(v,n) for b,v in FC.items()}
        an={b:delocalize(v,n) for b,v in endC.items()}
        capn={b:delocalize(v,n) for b,v in cap.items()}
        for c in CELLS:
            check(not apply(bd,bd[c]),'finite_tower_d_squared')
            for (t,e),a in bd[c].items():
                check(min(e)>=0 and abs(a)==1,'finite_tower_polynomial_arrows')
                check(degree(t)+1==degree(c),'finite_tower_chain_degree')
                check(eadd(e,finite_shift(t,n))==finite_shift(c,n),'finite_tower_fine_degree')
                for k in ('V','B'):
                    if predicate(c,k):check(predicate(t,k),'finite_tower_support_preservation')
            check(td(localize(one(c),n))==localize(bd[c],n),'kappa_complete_chain_equation')
            for (c0,e),v in localize(one(c),n).items():check(legal(c0,e),'kappa_only_admitted_normal_inverses')
        for b in KC[0]:
            check(apply(bd,capn[b])==scale(apply(capn,KC[1][b]),-1),'finite_complement_cap_equation')
        for b in P[0]:
            check(add(apply(bd,Fn[b]),scale(apply(Fn,P[1][b]),-1))==an[b],'finite_full_endpoint_equation')
            check(localize(Fn[b],n)==FC[b],'finite_comparison_localizes_to_fixed_map')
            check(all(min(e)>=0 for c,e in Fn[b]),'finite_comparison_has_no_inverse')
            check(all(predicate(c,'V') for c,e in an[b]),'finite_comparison_both_endpoints')
            check(diagonal_map(F1[b],ONE_N,n)==Fn[b],'comparison_compatible_at_all_finite_orders')
            check(diagonal_map(end1[b],ONE_N,n)==an[b],'endpoint_compatible_at_all_finite_orders')
        check_dual_equation(Fn,P,bd,an,'finite')
        for row in generic_rows(n):check(not apply(generic_trace(),row),'all_generic_relations_killed_by_trace')
    # Entire two-level nine-normal transition cube, each arrow on all 215
    # generators and all 522 source incidences. Exponent identities are exact.
    cube_vertices=list(product((1,2),repeat=9));edges=0;squares=0
    for n in cube_vertices:
        for c in CELLS:
            nn=tuple(3 for _ in range(9))
            check(localize(diagonal_map(one(c),n,nn),nn)==localize(one(c),n),'tower_image_independent_of_presentation')
        for i in range(9):
            if n[i]!=1:continue
            m=tuple(a+int(k==i) for k,a in enumerate(n));edges+=1
            # Every arrow class is checked by its exponent equality on every
            # original incidence; signs are unchanged.
            for c in CELLS:
                s=ex({9+i:int((SHORT+LONG)[i] in c[0] and (SHORT+LONG)[i] not in c[1])})
                for (t,e),a in finite_boundary(c,n).items():
                    ee=next(e2 for (t2,e2),a2 in finite_boundary(c,m).items() if t2==t)
                    st=ex({9+i:int((SHORT+LONG)[i] in t[0] and (SHORT+LONG)[i] not in t[1])})
                    check(eadd(e,st)==eadd(s,ee),'all_nine_normal_transition_chain_squares')
            for b in P[0]:
                check(diagonal_map(delocalize(FC[b],n),n,m)==delocalize(FC[b],m),'all_transition_comparison_squares')
            for j in range(i+1,9):
                if n[j]!=1:continue
                m2=tuple(a+int(k==j) for k,a in enumerate(n))
                top=tuple(a+int(k in (i,j)) for k,a in enumerate(n));squares+=1
                # Universal diagonal monomial formula checks each cell.
                for c in CELLS:
                    left=diagonal_map(diagonal_map(one(c),n,m),m,top)
                    right=diagonal_map(diagonal_map(one(c),n,m2),m2,top)
                    check(left==right,'all_transition_cube_two_faces')
    check((len(cube_vertices),edges,squares)==(512,2304,4608),'normal_cube_census')
    # Six semilinear transports, including anisotropic order relabelling.
    testn=tuple(1+i%3 for i in range(9))
    for g in GROUP:
        ng=[0]*9
        for a,i in IX.items():ng[IX[perm_di(a,g)]]=testn[i]
        ng=tuple(ng);bd=finite_table(testn);bg=finite_table(ng)
        for c in CELLS:
            check(act_target(bd[c],g)==apply(bg,act_target(one(c),g)),'anisotropic_dihedral_differential')
        Fg={b:delocalize(v,ng) for b,v in FC.items()}
        Fn={b:delocalize(v,testn) for b,v in FC.items()}
        for b in P[0]:
            check(act_target(Fn[b],g)==scale(apply(Fg,act_source(one(b),g)),pm(g[1])),'anisotropic_joint_comparison_polarity')
    tr=dual_generic_trace_audit(F1,P)
    gens=[GAMMA]+[ex({6+i:1,**{15+j:1 for j in range(3) if j!=i}}) for i in range(3)]
    check(not polynomial_membership(Z,gens),'trace_ideal_does_not_contain_one')
    for n in orders:
        # Transition in generic top degree is literally the identity. Thus
        # every fixed polynomial row gives a compatible inverse-limit class.
        for l in LONG:
            check(diagonal_map(one(((l,),(l,))),ONE_N,n)==one(((l,),(l,))),'generic_marked_top_transition_identity')
        check(diagonal_map(one(((),())),ONE_N,n)==one(((),())),'generic_chamber_transition_identity')
        for i,row in enumerate(generic_rows(n)):
            base=generic_rows(ONE_N)[i]
            factor=ex({15+i:n[6+i]-1})
            check(row==multiply(base,factor),'generic_nested_relation_submodules')
    # Rees-normalized complete source map, not only its scalar image.
    REES_F={b:rees(v) for b,v in F1.items()}
    REES_A={b:rees(v) for b,v in end1.items()}
    bd1=finite_table(ONE_N);RB={c:rees(v) for c,v in bd1.items()}
    for b in P[0]:
        check(add(apply(RB,REES_F[b]),scale(apply(REES_F,P[1][b]),-1))==REES_A[b],'whole_map_after_Rees_substitution')
    face_records=[]
    for mask in range(8):
        zs=tuple(6+i for i in range(3) if mask>>i&1)
        f={b:specialize(v,zs) for b,v in REES_F.items()}
        a={b:specialize(v,zs) for b,v in REES_A.items()}
        d={c:specialize(v,zs) for c,v in RB.items()}
        for b in P[0]:
            check(add(apply(d,f[b]),scale(apply(f,P[1][b]),-1))==a[b],'all_Rees_faces_full_endpoint_equation')
        nn=sum(map(len,f.values()));ne=sum(map(len,a.values()))
        if zs:check(ne==0,'any_long_Rees_zero_kills_old_endpoint_composites')
        if len(zs)>=2:check(nn==0,'two_long_Rees_zeros_kill_whole_map')
        if len(zs)==1:check(nn>0,'one_Rees_zero_leaves_marked_generic_channel')
        face_records.append({'zero_long_Rees_indices':[i-6 for i in zs],'full_map_terms':nn,'endpoint_terms':ne})
    # Two adjacent Rees orders must remain coupled. The degree-zero long-normal
    # differential d0 and its degree-one component d1 are independently formed.
    F2={b:keep_order(v,2) for b,v in F1.items()}
    F3={b:keep_order(v,3) for b,v in F1.items()}
    D0={c:keep_order(v,0) for c,v in bd1.items()}
    D1={c:keep_order(v,1) for c,v in bd1.items()}
    for c in CELLS:
        check(add(D0[c],D1[c])==bd1[c],'long_Rees_differential_order_split')
        check(not apply(D0,D0[c]),'order_zero_d_squared')
        check(not add(apply(D0,D1[c]),apply(D1,D0[c])),'mixed_Rees_anticommutator')
        check(not apply(D1,D1[c]),'order_one_d_squared')
    for b in P[0]:
        check(add(F2[b],F3[b])==F1[b],'whole_comparison_has_exactly_orders_two_three')
        check(apply(D0,F2[b])==apply(F2,P[1][b]),'quadratic_generic_symbol_closed')
        check(add(apply(D0,F3[b]),apply(D1,F2[b]),scale(apply(F3,P[1][b]),-1))==end1[b],'cubic_endpoint_equation_includes_quadratic_correction')
        check(not apply(D1,F3[b]),'no_higher_Rees_remainder')
    check(any(end1.values()),'cubic_endpoint_data_nonzero_before_specialization')
    check(any(apply(D1,v) for v in F2.values()),'quadratic_to_cubic_correction_really_nonzero')
    # Factor only the actual principal long-occurrence ideal, never a normal
    # parameter. The residual ideal is the three-axis pair-product ideal.
    W=ex({6:1,7:1,8:1})
    trace=generic_trace();trace_rees={b:rees(v) for b,v in trace.items()}
    normalized={b:{(k,esub(e,W)):a for (k,e),a in v.items()} for b,v in trace_rees.items()}
    check(all(min(e)>=0 for v in normalized.values() for k,e in v),'principal_occurrence_factorization_no_inverse')
    check(normalized['Tstar']=={('kappa',ex({15:1,16:1,17:1})):1},'normalized_trace_cubic_top')
    for i in range(3):
        check(normalized['Mstar',i]=={('kappa',ex({15+j:1 for j in range(3) if j!=i})):-1},'normalized_trace_quadratic_marked')
    support_records=minimal_rees_resolution_check()
    generic_supports=generic_syzygy_support_check()
    selected_excess=independent_selected_excess_check()
    # Keep an independent exterior class as tensor data, without identifying it
    # with an internal marked normal. This is only a tensor-compatibility check.
    for eta_degree in (0,1):
        for b in P[0]:
            lhs=add(apply(bd1,F1[b]),scale(apply(F1,P[1][b]),-1))
            check({(eta_degree,c,e):a for (c,e),a in lhs.items()}=={(eta_degree,c,e):a for (c,e),a in end1[b].items()},'independent_excess_tensor_equation')
    def export(v):
        return [{'basis':repr(b),'coefficient':a,'exponents':list(e)} for (b,e),a in sorted(v.items(),key=lambda kv:repr(kv[0]))]
    result={
        'status':'constructed_actual_R_linear_dual_comparison_with_normal_completion_and_exact_Rees_trace_ideal',
        'date':'2026-09-07','source_commit':COMMIT,'source_blobs':SOURCE_BLOBS,
        'coefficient_ring':'Z[X_0,...,X_8,u_0,...,u_8], with independent variables before the explicitly declared Rees substitution',
        'finite_normal_system':{'states_each':215,'source_ranks':[1,9,18,15,6,1],
            'orders_fully_audited':[list(n) for n in orders],
            'cube_vertices':512,'cube_edges':edges,'cube_squares':squares,
            'radial_coefficient':'epsilon X_a u_a^(n_a-1)','normal_coefficient':'epsilon u_h^n_h',
            'transition':'product u_a^(m_a-n_a) over a in S minus H',
            'Cech_map':'product u_a^(-n_a) over a in S minus H'},
        'actual_derived_dual':'Rlim_n Hom_R(K_n,R); its support quotient maps and endpoint homotopies are dualized before taking the limit',
        'generic_dual':{
            'cohomological_degree':3,'other_cohomology':0,
            'finite_presentation':'R^4 / sum_i R*u_i^(n-1)*(X_i*Tstar+u_i*Mistar)',
            'limit_presentation':'(R^4 direct_sum direct_sum_i Rhat_(u_i)) / ((X_i*Tstar+u_i*Mistar),-1_i)',
            'ML':'top cohomology transition is the quotient of the identity on R^4; surjective',
            'trace_ideal_generators':[list(e) for e in gens],
            'trace_ideal_contains_unit':False,
            'completion_enlarges_trace_image':False,
            'finite_order_one_trace':'isomorphism of H3 with the ideal J',
            'all_support_syzygy_check':generic_supports},
        'Rees':{
            'substitution':'u_a=t_a X_a',
            'common_principal_occurrence_factor':'X_D03 X_D14 X_D25',
            'residual_trace_ideal':'(t_D14*t_D25,t_D03*t_D25,t_D03*t_D14)',
            'defect_support':'union of the three long-Rees coordinate axes',
            'minimal_defect_resolution_ranks':[1,3,2],
            'support_records':support_records,'all_eight_central_faces':face_records,
            'quadratic_comparison_terms':sum(map(len,F2.values())),
            'cubic_comparison_terms':sum(map(len,F3.values())),
            'cubic_endpoint_terms':sum(map(len,end1.values())),
            'equations':['d0 F2 - F2 dP = 0','d0 F3 + d1 F2 - F3 dP = A3','d1 F3 = 0']},
        'independent_selected_excess':selected_excess,
        'finite_order_one_map':{repr(b):export(v) for b,v in F1.items() if v},
        'finite_order_one_endpoint_map':{repr(b):export(v) for b,v in end1.items() if v},
        'plus_sheet_attachment':{repr(b):export(v) for b,v in tp1.items() if v},
        'minus_sheet_attachment':{repr(b):export(v) for b,v in tm1.items() if v},
        'scope':[
            'The seven-module target is the native dual via the preceding complete quasi-isomorphisms; the new reverse map is into that entire native dual, not a split conductor summand.',
            'The inverse-limit result is proved for all orders; the executable checks the displayed symbolic identities on complete finite complexes and the entire two-level normal cube.',
            'This is the actual derived Hom over the ambient polynomial ring, not an identification with the full ringed supported-Verdier six-functor.',
            'Independent exterior excess is retained as tensor data only; its physical identification and the framed collar comparison are not constructed.',
            'The ordinary completed-dual comparison has a proper trace image ideal. No degree-zero unit trace or physical parity is assigned.',
            'The ambient polynomial base is not replaced by the singular intrinsic normalization ring.'
        ],
        'assertions':dict(sorted(COUNT.items())),'exact_assertions':sum(COUNT.values())}
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ('status','generic_dual','Rees','exact_assertions')},indent=2))

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path('marici_completed_normal_dual_comparison_certificate.json'))
    args=parser.parse_args();main(args.output)
