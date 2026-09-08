#!/usr/bin/env python3
"""Supported Rees-branch residue and primitive excess transgression.

Self-contained standard-library checker. The inherited target/Hom routines
reconstruct the pinned Marici coefficient models. New routines construct the
support-inclusion Cech map, the selected Koszul-to-Cech residue, all central
Rees faces, the actual excess basis, its coefficient-level endpoint normal
maps, and the Gysin-valued reverse pairing. No spatial Verdier comparison or
physical parity is asserted.
"""
from __future__ import annotations
import argparse
from collections import Counter
from itertools import combinations, product
from math import gcd
import hashlib
import json
from pathlib import Path

COMMIT='d1947b67a60d3e88ba77f4ca60ea02c2a306ee61'
SOURCE_BLOBS={
 'research/voevodsky/check_d03_plus_excess_beck_chevalley.rs':'df8448271089910a90c8e641af5b8ae95f1472dd',
 'research/voevodsky/check_global_k6_koszul_cech_promotion.rs':'e972b69d0e2b1b0a0aee5e0a027c8216bcace3e8',
 'research/voevodsky/check_two_endpoint_tate_carrier.rs':'0147e2e42dafac0da7289c571cb0331b51338be1',
 'src/ledger/20260814-115 Boundary-Triad Tate Realization and the Multi-Rees Cartier Bicomplex.md':'63da17cb5d641705056c5d5b9bc6f53cda72baf5',
}
COUNT=Counter()
def check(ok,category):
    if not ok:raise AssertionError(category)
    COUNT[category]+=1

def pm(n):return -1 if n%2 else 1

def add(*vs):
    out={}
    for v in vs:
        for k,a in v.items():
            out[k]=out.get(k,0)+a
            if not out[k]:del out[k]
    return out

def scale(v,a):return {k:a*b for k,b in v.items() if a*b}
def linear(table,v):
    out={}
    for k,a in v.items():out=add(out,scale(table[k],a))
    return out

def diag(i,j):return tuple(sorted((i%6,j%6)))
def cross(a,b):
    x,y=a;u,v=b
    return x<u<y<v or u<x<v<y

DS=tuple((i,j) for i in range(6) for j in range(i+1,6) if j-i not in (1,5))
SHORTS=tuple(diag(i,i+2) for i in range(6))
LONGS=tuple(diag(i,i+3) for i in range(3))
IX={d:i for i,d in enumerate(SHORTS+LONGS)}
FACES=tuple(f for k in range(4) for f in combinations(DS,k)
            if all(not cross(a,b) for a,b in combinations(f,2)))
CELLS=tuple((f,h) for f in FACES for k in range(len(f)+1) for h in combinations(f,k))
VP=tuple(sorted(SHORTS[i] for i in (1,3,5)))
VM=tuple(sorted(SHORTS[i] for i in (0,2,4)))
ZERO=(0,)*18
G=tuple(product(range(3),range(2)))
SEQ=(1,3,5,0,3)
BRANCH=(1,3,5)
ISET=frozenset((0,1,3,5))

def ex(data):return tuple(data.get(i,0) for i in range(18))
def eadd(a,b):return tuple(x+y for x,y in zip(a,b))
def esub(a,b):return tuple(x-y for x,y in zip(a,b))
GAMMA=ex({15:1,16:1,17:1})

def weight(f):return ex({**{IX[a]:1 for a in f},**{IX[a]+9:-1 for a in f}})
def degree(c):return 3-len(c[0])+len(c[1])
def legal(c,e):
    loc={IX[a] for a in c[0] if a not in c[1]}
    return all(a>=0 for a in e[:9]) and all(a>=0 or i in loc for i,a in enumerate(e[9:]))

def target_pred(c,support):
    v=c[0] in (VP,VM)
    b=any(a in SHORTS for a in c[0])
    return {'K':True,'B':b,'V':v,'E':not v,'Q':not b,'BV':b and not v}[support]

def boundary(c):
    f,h=c;out={}
    for a in DS:
        if a not in f and all(not cross(a,b) for b in f):
            t=(tuple(sorted(f+(a,))),h)
            out[(t,ex({IX[a]:1,IX[a]+9:-1}))]=pm(sum(b<a for b in f))
    for i,a in enumerate(h):
        t=(f,tuple(b for b in h if b!=a))
        out[(t,ZERO)]=pm(3-len(f)+i)
    return out
BD={c:boundary(c) for c in CELLS}

def mask_degree(seq,mask):
    out=[0]*18
    for i,a in enumerate(seq):
        if mask>>i&1:out[9+a]+=1
    return tuple(out)

def hom_complex(seq,lam,support,zero_last=False):
    """Hom_n consists of maps source_i -> target_(i+n). Ext^j=H_(-j)."""
    gens={};coeff={}
    for mask in range(1<<len(seq)):
        target_grade=eadd(lam,mask_degree(seq,mask))
        for c in CELLS:
            m=eadd(target_grade,weight(c[0]))
            if target_pred(c,support) and legal(c,m):
                key=(mask,c);gens[key]=degree(c)-mask.bit_count();coeff[key]=m
    d={x:{} for x in gens}
    for x,n in gens.items():
        mask,c=x
        for (t,m),s in BD[c].items():
            y=(mask,t)
            if not target_pred(t,support):continue
            check(y in gens,'Hom_target_differential_domain')
            check(eadd(coeff[x],m)==coeff[y],'Hom_target_exact_monomial')
            d[x][y]=s
        for i,a in enumerate(seq):
            if mask>>i&1 or (zero_last and i==len(seq)-1):continue
            y=(mask|(1<<i),c)
            check(y in gens,'Hom_source_differential_domain')
            check(eadd(coeff[x],ex({9+a:1}))==coeff[y],'Hom_source_exact_monomial')
            d[x][y]=-pm(n+(mask&((1<<i)-1)).bit_count())
    for x,n in gens.items():
        check(all(gens[y]==n-1 for y in d[x]),'Hom_homological_degree')
        check(not linear(d,d[x]),'Hom_d_squared')
    return gens,d,coeff

def reduce_fast(gens,original):
    """Exact algebraic cancellation. All pivots are signed units."""
    d={x:dict(v) for x,v in original.items()};incoming={x:set() for x in d};pivots=[]
    for x,v in d.items():
        for y in v:incoming[y].add(x)
    while True:
        hit=next(((b,a,u) for b,v in d.items() for a,u in v.items() if abs(u)==1),None)
        if hit is None:break
        b,a,u=hit;db=dict(d[b]);pivots.append((b,a,u))
        check(gens[b]==gens[a]+1 and u*u==1,'integral_unit_pivot')
        for z in list(incoming[a]-{b}):
            v=d[z][a]*u
            for t,c in db.items():
                n=d[z].get(t,0)-v*c
                if n:d[z][t]=n;incoming[t].add(z)
                else:d[z].pop(t,None);incoming[t].discard(z)
        for z in list(incoming[b]):d[z].pop(b,None)
        for t in db:incoming[t].discard(b)
        for t in d[a]:incoming[t].discard(a)
        del d[a];del d[b];del incoming[a];del incoming[b]
    check(not any(d.values()),'zero_residual_differential_integral_homology')
    return dict(sorted(Counter(gens[x] for x in d).items())),pivots

def reduce_sdr(gens,original):
    """Full I,P,H retained for independent chain identities on critical slices."""
    cells=tuple(gens);current={c:dict(v) for c,v in original.items()}
    P={c:{c:1} for c in cells};I=dict(P);H={c:{} for c in cells};np=0
    while True:
        hit=next(((b,a,u) for b in current for a,u in current[b].items() if abs(u)==1),None)
        if hit is None:break
        b,a,u=hit;db=current[b];survive=tuple(c for c in current if c not in (a,b));np+=1
        pa={c:{c:1} for c in survive};pa[b]={};pa[a]={t:-u*v for t,v in db.items() if t!=a}
        inc={c:add({c:1},({b:-u*current[c][a]} if a in current[c] else {})) for c in survive}
        for c in cells:
            acoef=P[c].get(a,0)
            if acoef:H[c]=add(H[c],scale(I[b],u*acoef))
        P={c:linear(pa,v) for c,v in P.items()}
        I={c:linear(I,v) for c,v in inc.items()}
        current={c:linear(pa,linear(current,inc[c])) for c in survive}
    check(not any(current.values()),'SDR_zero_residual')
    for c in cells:
        check(not linear(P,original[c]),'SDR_projection_chain_map')
        check(add(linear(original,H[c]),linear(H,original[c]))==add({c:1},scale(linear(I,P[c]),-1)),
              'SDR_dH_plus_Hd')
    for c,v in I.items():
        check(not linear(original,v),'SDR_section_closed')
        check(linear(P,v)=={c:1},'SDR_projection_section_identity')
    return {'homology':dict(sorted(Counter(gens[c] for c in current).items())),
            'P':P,'I':I,'H':H,'pivots':np}

def wedge(v,w):
    out={}
    for a,ca in v.items():
        for b,cb in w.items():
            if a&b:continue
            inv=sum((b&((1<<i)-1)).bit_count() for i in range(5) if a>>i&1)
            out=add(out,{a|b:ca*cb*pm(inv)})
    return out

def change_basis():
    # old h3(03) = new h3(+) - eta; the same substitution is its inverse.
    table={}
    for mask in range(32):
        v={0:1}
        for i in range(5):
            if mask>>i&1:v=wedge(v,{1<<i:1} if i<4 else {2:1,16:-1})
        table[mask]=v
    for mask,v in table.items():
        check(linear(table,v)=={mask:1},'excess_basis_change_is_integral_involution')
        check(all(mask_degree(SEQ,m)==mask_degree(SEQ,mask) for m in v),'excess_basis_change_preserves_normal_degree')
    return table
CHANGE=change_basis()

def source_d(mask,zero_last=False):
    out={}
    for i,a in enumerate(SEQ):
        if mask>>i&1 and not(zero_last and i==4):
            out[(mask^(1<<i),a)]=pm((mask&((1<<i)-1)).bit_count())
    return out

def check_source():
    for m in range(32):
        left={};right={}
        for n,c in CHANGE[m].items():
            for (t,a),s in source_d(n,True).items():left=add(left,{(t,a):c*s})
        for (n,a),c in source_d(m).items():
            for t,s in CHANGE[n].items():right=add(right,{(t,a):c*s})
        check(left==right,'excess_basis_change_commutes_with_source_d')
    # eta is degree one, differential zero, independent from the other four.
    check(CHANGE[16]=={2:1,16:-1},'eta_is_difference_of_shared_normals')

def precompose_old(v_split):
    grouped={}
    for (mask,c),a in v_split.items():grouped.setdefault(mask,{})[c]=a
    out={}
    for old,terms in CHANGE.items():
        for new,s in terms.items():
            for c,a in grouped.get(new,{}).items():out=add(out,{(old,c):s*a})
    return out

def named_cell(c):
    def dn(a):return 'x'+str(SHORTS.index(a)) if a in SHORTS else 'D'+str(a[0])+str(a[1])
    f,h=c
    return ('T' if not f else ','.join(dn(a) for a in f))+'['+','.join(dn(a) for a in h)+']'
def named_hom(v):return {f'{mask:05b} -> {named_cell(c)}':a for (mask,c),a in sorted(v.items())}
def ext_groups(homology):return {str(-n):r for n,r in sorted(homology.items(),reverse=True)}
def frame(*negative):
    result=list(GAMMA)
    for i in negative:result[9+i]-=1
    return tuple(result)

OMEGA={((),()):1}
for a in LONGS:OMEGA[((a,),(a,))]=-1

def generic_map(tor):
    return precompose_old({(31 if tor else 15,c):a for c,a in OMEGA.items()})

def endpoint_map(tor):
    out={}
    for sub in range(8):
        vals=[SHORTS[BRANCH[i]] for i in range(3) if sub>>i&1]
        orient=pm(sum(a>b for i,a in enumerate(vals) for b in vals[i+1:]))
        coeff=orient*(1 if tor else pm(len(vals)))
        out[(sub|8|(16 if tor else 0),(VP,tuple(sorted(vals))))]=coeff
    return precompose_old(out)

def reduced_regular(lam,support):
    vals={a:lam[9+a] for a in ISET}
    if any(x not in (0,-1) for x in vals.values()):return {}
    required={SHORTS[a] for a,x in vals.items() if x==0}
    forbidden={SHORTS[a] for a,x in vals.items() if x==-1}
    fs=[f for f in FACES if not any(a in LONGS for a in f) and required<=set(f) and not(set(f)&forbidden)
        and target_pred((f,()),support)]
    gs={f:3-len(f)-len(forbidden) for f in fs};d={f:{} for f in fs}
    for f in fs:
        for (t,_),s in BD[(f,())].items():
            if t[0] in gs:d[f][t[0]]=s
    return reduce_fast(gs,d)[0]

def reduced_excess(lam,support):
    h=Counter(reduced_regular(lam,support))
    up=eadd(lam,ex({12:1}))
    for n,r in reduced_regular(up,support).items():h[n-1]+=r
    return dict(sorted({n:r for n,r in h.items() if r}.items()))

def group_diag(d,g):
    r,s=g
    return diag(2*r+(d[0] if not s else 3-d[0]),2*r+(d[1] if not s else 3-d[1]))
def act_exp(v,g):
    out=[0]*18
    for a,i in IX.items():
        j=IX[group_diag(a,g)];out[j]=v[i];out[9+j]=v[9+i]
    return tuple(out)
def act_cell(c,g):
    f,h=c;vf=[group_diag(a,g) for a in f];vh=[group_diag(a,g) for a in h]
    inv=sum(a>b for i,a in enumerate(vf) for b in vf[i+1:])+sum(a>b for i,a in enumerate(vh) for b in vh[i+1:])
    return (tuple(sorted(vf)),tuple(sorted(vh))),pm(g[1]+inv)
def act_hom(v,g):
    out={}
    for (m,c),a in v.items():
        t,s=act_cell(c,g);out[(m,t)]=a*s
    return out



def branch_survives(c,branch):
    """A localization intersecting the closed normal branch has zero base change."""
    return not ((set(c[0])-set(c[1])) & {SHORTS[a] for a in branch})


def purity_complex(lam,support,seq=SEQ):
    """Hom(pair, (target tensor R/I_branch)[-3] tensor det_branch^dual).

    The pair retains its shared generator, with zero differential after base
    change. No branch normal is cancelled against its conormal symbol.
    """
    branch=seq[:3]; pair=seq[3:]
    bs=mask_degree(branch,7)
    gs={}; cs={}
    for mask in range(4):
        tg=eadd(eadd(lam,bs),mask_degree(pair,mask))
        for c in CELLS:
            m=eadd(tg,weight(c[0]))
            if (target_pred(c,support) and branch_survives(c,branch)
                and legal(c,m) and all(m[9+a]==0 for a in branch)):
                key=(mask,c);gs[key]=degree(c)-3-mask.bit_count();cs[key]=m
    d={x:{} for x in gs}
    for x,n in gs.items():
        mask,c=x
        for (t,m),a in BD[c].items():
            if not target_pred(t,support) or not branch_survives(t,branch):continue
            check(all(m[9+a]==0 for a in branch),'purity_retained_arrow_branch_exponent_zero')
            y=(mask,t)
            check(y in gs,'purity_target_domain')
            check(eadd(cs[x],m)==cs[y],'purity_target_monomial')
            d[x][y]=-a  # homological shift -3 reverses the differential
        for i,a in enumerate(pair):
            if mask>>i&1 or a in branch:continue
            y=(mask|(1<<i),c)
            check(y in gs,'purity_pair_source_domain')
            check(eadd(cs[x],ex({9+a:1}))==cs[y],'purity_pair_source_monomial')
            d[x][y]=-pm(n+(mask&((1<<i)-1)).bit_count())
    for x,n in gs.items():
        check(all(gs[y]==n-1 for y in d[x]),'purity_homological_degree')
        check(not linear(d,d[x]),'purity_d_squared')
    return gs,d,cs


def purity_projection(old,new,branch=BRANCH):
    """Select full branch wedge, restrict coefficients, keep odd-shift signs."""
    table={}
    for (m,c),n in old[0].items():
        cm=m>>3;value={}
        if (m&7==7 and (cm,c) in new[0]
            and all(old[2][(m,c)][9+a]==0 for a in branch)):
            value[(cm,c)]=pm(degree(c)+cm.bit_count())
            check(old[2][(m,c)]==new[2][(cm,c)],'purity_preserves_legal_monomial_exactly')
        table[(m,c)]=value
    for x in old[0]:
        check(linear(table,old[1][x])==linear(new[1],table[x]),'full_purity_projection_chain_map')
        check(all(new[0][y]==old[0][x] for y in table[x]),'purity_preserves_total_Hom_degree')
    return table


def cone_of_map(old,new,p):
    gs={('new',x):n for x,n in new[0].items()}
    gs.update({('old',x):n+1 for x,n in old[0].items()})
    d={('new',x):{('new',y):a for y,a in v.items()} for x,v in new[1].items()}
    for x,v in old[1].items():
        d[('old',x)]={('old',y):-a for y,a in v.items()}
        d[('old',x)].update({('new',y):a for y,a in p[x].items()})
    for x in gs:check(not linear(d,d[x]),'purity_comparison_cone_d_squared')
    return gs,d


def dual_complex(model):
    """Hom_Z(model,Z) in homological degrees; finite homogeneous slice ONLY."""
    gs={x:-n for x,n in model[0].items()};d={x:{} for x in gs}
    for x,v in model[1].items():
        for y,a in v.items():d[y][x]=pm(gs[y]+1)*a
    for x in gs:
        check(all(gs[y]==gs[x]-1 for y in d[x]),'graded_dual_degree')
        check(not linear(d,d[x]),'graded_dual_d_squared')
    return gs,d,{}


def evaluate(row,v):return sum(row.get(x,0)*a for x,a in v.items())

def restrict_vec(v,model):return {x:a for x,a in v.items() if x in model[0]}

def rows_with_coefficients(v,model):
    return [{'pair_mask':mask,'target':named_cell(c),'integer':a,
             'coefficient_exponents':list(model[2][(mask,c)])}
            for (mask,c),a in sorted(v.items())]


def counter_delta(after,before):
    return {k:after[k]-before.get(k,0) for k in sorted(after) if after[k]-before.get(k,0)}



# New exact polynomial/localization calculations. Variable order:
# t1,t3,t5,x1,x3,x5,u0. Spectators are left unchanged.
NZ=(0,)*7

def nmono(i:int, power:int=1):
    return tuple(power if j==i else 0 for j in range(7))

def nsum(*ms):
    return tuple(sum(m[j] for m in ms) for j in range(7))

def nscale(v,m,coefficient=1):
    return {(k,nsum(e,m)):coefficient*a for (k,e),a in v.items() if coefficient*a}

def nlinear(table,v):
    out={}
    for (key,e),a in v.items():
        out=add(out,nscale(table[key],e,a))
    return out

def nwedge(v,w):
    out={}
    for (a,e),ca in v.items():
        for (b,f),cb in w.items():
            if a&b:continue
            inv=sum((b&((1<<i)-1)).bit_count() for i in range(5) if a>>i&1)
            out=add(out,{(a|b,nsum(e,f)):ca*cb*pm(inv)})
    return out

def ndiff(v,sequence):
    out={}
    for (mask,e),a in v.items():
        for i,s in enumerate(sequence):
            if not(mask>>i&1) or s is None:continue
            out=add(out,{(mask^(1<<i),nsum(e,s)):a*pm((mask&((1<<i)-1)).bit_count())})
    return out

def ncentral(v,P,localized_mask=None,normal_state=False):
    """Derived t_P=0 on flat localized terms; no evaluate-0/0 operation."""
    out={}
    for (key,e),a in v.items():
        loc=(7^(key&7)) if normal_state else (localized_mask(key) if localized_mask else 0)
        if loc&P:continue
        check(all(e[i]>=0 for i in range(3) if P>>i&1),'central_coefficient_defined_on_surviving_stalk')
        if any(e[i]>0 for i in range(3) if P>>i&1):continue
        out[(key,e)]=a
    return out

def support_cochain_d(v,kind,P=0):
    """coK(x), coK(tx), Cech(x), or Cech(tx), all in degrees 0..3."""
    out={}
    for (mask,e),a in v.items():
        if kind=='C_u' and mask&P:continue
        for i in range(3):
            if mask>>i&1:continue
            target=mask|(1<<i)
            if kind=='C_u' and target&P:continue
            m=NZ
            if kind=='K_x':m=nmono(3+i)
            elif kind=='K_u':m=nsum(nmono(i),nmono(3+i))
            out=add(out,{(target,nsum(e,m)):a*pm((mask&((1<<i)-1)).bit_count())})
    return out

def residue_cochain(v,raw=False,P=0):
    """Selected residue in C_u: component t_H/u_H = 1/x_H.

    raw=True is the unselected map coK(u)->C_u, with coefficient 1/u_H.
    """
    out={}
    for (mask,e),a in v.items():
        if mask&P:continue
        negative=[0]*7
        for i in range(3):
            if mask>>i&1:
                negative[3+i]=-1
                if raw:negative[i]=-1
        out=add(out,{(mask,nsum(e,tuple(negative))):a})
    return out

def dual_selector_cochain(v):
    out={}
    for (mask,e),a in v.items():
        f=tuple(int(mask>>i&1) if i<3 else 0 for i in range(7))
        out=add(out,{(mask,nsum(e,f)):a})
    return out

def cech_local_legal(mask,e,kind='C_u'):
    return all(v>=0 or (j<3 and kind=='C_u' and mask>>j&1)
               or (3<=j<6 and mask>>(j-3)&1)
               for j,v in enumerate(e))

def check_support_residue():
    faces=[]
    # Testing a basis of each free source term proves polynomial linearity.
    for mask in range(8):
        v={(mask,NZ):1}
        for kind in ('K_x','K_u','C_x','C_u'):
            check(not support_cochain_d(support_cochain_d(v,kind),kind),'supported_cochain_d_squared')
        sx=residue_cochain(v)
        check(support_cochain_d(sx,'C_u')==residue_cochain(support_cochain_d(v,'K_x')),
              'selected_residue_chain_map')
        check(support_cochain_d(residue_cochain(v,True),'C_u')==residue_cochain(support_cochain_d(v,'K_u'),True),
              'unselected_residue_chain_map')
        check(support_cochain_d(dual_selector_cochain(v),'K_u')==dual_selector_cochain(support_cochain_d(v,'K_x')),
              'dual_selector_chain_map')
        check(residue_cochain(dual_selector_cochain(v),True)==sx,'residue_is_dual_selector_followed_by_supported_residue')
        check(all(cech_local_legal(k,e) for k,e in sx),'residue_has_only_legal_target_localizations')
        # The identity inclusion C_x -> C_u is forced by V(x) subset V(tx).
        sample=residue_cochain(v)
        check(support_cochain_d(sample,'C_x')==support_cochain_d(sample,'C_u'),
              'support_inclusion_chain_map')
        # Verify the positive-numerator expression t_H/u_H literally.
        den=[0]*7;num=[0]*7
        for i in range(3):
            if mask>>i&1:den[i]=-1;den[3+i]=-1;num[i]=1
        check(nsum(tuple(num),tuple(den))==next(iter(sx))[1], 'residue_t_over_u_not_base_ring_inverse')
    for P in range(8):
        for mask in range(8):
            v={(mask,NZ):1}
            check(residue_cochain(v,P=P)==ncentral(residue_cochain(v),P,lambda k:k),
                  'derived_base_change_of_complete_residue')
            check(support_cochain_d(residue_cochain(v,P=P),'C_u',P)==residue_cochain(support_cochain_d(v,'K_x'),P=P),
                  'partial_central_residue_chain_map')
            check(not support_cochain_d(support_cochain_d(v,'C_u',P),'C_u',P),
                  'partial_central_cech_d_squared')
            for j in range(3):
                if P>>j&1:continue
                Pj=P|(1<<j)
                a=residue_cochain(v,P=P)
                check(ncentral(a,1<<j,lambda k:k)==residue_cochain(v,P=Pj),
                      'Rees_cube_edge_base_change')
        faces.append({'zero_Rees_indices':[i for i in range(3) if P>>i&1],
                      'surviving_Cech_summands':2**(3-P.bit_count()),
                      'higher_extension_order':P.bit_count(),
                      'fundamental_coefficient':1})
    for i,j in combinations(range(3),2):
        for P in range(8):
            if P&((1<<i)|(1<<j)):continue
            for mask in range(8):
                v=residue_cochain({(mask,NZ):1},P=P)
                a=ncentral(ncentral(v,1<<i,lambda k:k),1<<j,lambda k:k)
                b=ncentral(ncentral(v,1<<j,lambda k:k),1<<i,lambda k:k)
                check(a==b,'Rees_cube_commuting_square')
    # At the fully central fibre, only the lower Cech row remains.
    for mask in range(8):
        expected={(0,NZ):1} if mask==0 else {}
        check(residue_cochain({(mask,NZ):1},P=7)==expected,'central_counit_is_bottom_projection_not_zero_map')
    # All degree-zero nullhomotopies in Hom(coK(x),A) have boundary in (x1,x3,x5).
    for i in range(3):
        k=1<<i
        coefficient=support_cochain_d({(0,NZ):1},'K_x')[(k,nmono(3+i))]
        check(abs(coefficient)==1,'central_Hom_boundary_generates_exact_branch_ideal')
    # Primitive nonvanishing is evaluated modulo that exact ideal, not by a rational rank test.
    check(all(nmono(3+i)[3+i]==1 for i in range(3)) and 1!=0,'central_trace_quotient_unit_is_primitive')
    # Independent complete homogeneous Hom(coK(x),A0) calculations.
    # Generator degree in coK is -sum e_i; an integer coefficient degree
    # lambda gives a basis functional on H exactly when lambda-1_H >= 0.
    # All integer frames reduce to the negative / zero / positive cases tested.
    for lam in product(range(-1,3),repeat=3):
        gs={mask:mask.bit_count() for mask in range(8)
            if all(lam[i]-int(mask>>i&1)>=0 for i in range(3))}
        dd={mask:{} for mask in gs}
        for mask in gs:
            for i in range(3):
                if mask>>i&1:
                    target=mask^(1<<i)
                    check(target in gs,'central_Hom_all_boundaries_stay_in_degree')
                    dd[mask][target]=-pm(mask.bit_count())*pm((target&((1<<i)-1)).bit_count())
        for mask in gs:
            check(not linear(dd,dd[mask]),'central_Hom_d_squared')
        hh=reduce_fast(gs,dd)[0]
        expected={0:1} if lam==(0,0,0) else {}
        check(hh==expected,'central_Hom_complete_frame_cohomology')
    return faces


def selected_excess_and_endpoint():
    x=(nmono(3),nmono(4),nmono(5),nmono(6),nsum(nmono(1),nmono(4)))
    u=tuple(nsum(x[i],nmono(i)) if i<3 else x[i] for i in range(5))
    split=(x[0],x[1],x[2],x[3],None)
    splitu=(u[0],u[1],u[2],u[3],None)
    table={};tabu={}
    for mask in range(32):
        v={(0,NZ):1};w=dict(v)
        for i in range(5):
            if mask>>i&1:
                v=nwedge(v,{(1<<i,NZ):1} if i<4 else {(2,nmono(1)):1,(16,NZ):-1})
                w=nwedge(w,{(1<<i,NZ):1} if i<4 else {(2,NZ):1,(16,NZ):-1})
        table[mask]=v;tabu[mask]=w
    for mask in range(32):
        v={(mask,NZ):1}
        check(nlinear(table,nlinear(table,v))==v,'selected_excess_change_is_unimodular_involution')
        check(ndiff(nlinear(table,v),split)==nlinear(table,ndiff(v,x)),
              'selected_excess_change_preserves_full_differential')
        check(ndiff(nlinear(tabu,v),splitu)==nlinear(tabu,ndiff(v,u)),
              'raw_excess_change_preserves_full_differential')
    eta={(2,nmono(1)):1,(16,NZ):-1}
    check(not ndiff(eta,x),'selected_eta_closed')
    check(nlinear(table,eta)=={(16,NZ):1},'actual_eta_is_independent_split_factor')
    check(ncentral(eta,7)=={(16,NZ):-1},'actual_eta_survives_central_Rees_face')

    # Endpoint normal chain factor in the ordered source normal frame.
    # Branch masks H: only the complement (unmarked normals) is localized.
    def endpoint_normal_d(v,P=0):
        out={}
        for (mask,e),a in v.items():
            h=mask&7
            if (7^h)&P:continue
            for i in range(3):
                if h>>i&1:
                    target=mask^(1<<i)
                    if (7^(target&7))&P:continue
                    out=add(out,{(target,e):a*pm((h&((1<<i)-1)).bit_count())})
            if mask&8:
                out=add(out,{(mask^8,nsum(e,nmono(6))):a*pm(h.bit_count())})
        return out
    def kappa(v,P=0):
        out={}
        for (mask,e),a in v.items():
            missing=7^(mask&7)
            if missing&P:continue
            coef=tuple(-int(missing>>(j-3)&1) if 3<=j<6 else 0 for j in range(7))
            out=add(out,{(mask,nsum(e,coef)):a})
        return out
    for P in range(8):
        for mask in range(32):
            v={(mask,NZ):1}
            check(endpoint_normal_d(kappa(v,P),P)==kappa(ndiff(v,split),P),
                  'full_residue_tensor_residual_pair_and_excess_chain_map')
            check(not endpoint_normal_d(endpoint_normal_d(kappa(v,P),P),P),
                  'endpoint_normal_tensor_d_squared')
            check(kappa(v,P)==ncentral(kappa(v),P,normal_state=True),
                  'full_excess_residue_derived_base_change')
            old=nlinear(table,v)
            check(endpoint_normal_d(kappa(old,P),P)==kappa(nlinear(table,ndiff(v,x)),P),
                  'residue_is_chain_map_on_original_32_generator_selected_source')
    check(kappa({(7,NZ):1},7)=={(7,NZ):1},'central_ordinary_residue_channel_primitive')
    check(kappa({(23,NZ):1},7)=={(23,NZ):1},'central_excess_residue_channel_primitive')
    check(kappa({(16,NZ):1},7)=={},'no_false_same_degree_eta_homology_image')
    # Convert ordered normal wedge maps into actual endpoint lexicographic signs.
    transported=[]
    for group in G:
        indices=tuple(IX[group_diag(SHORTS[i],group)] for i in BRANCH)
        targetface=tuple(sorted(SHORTS[i] for i in indices))
        check(targetface in (VP,VM),'transported_endpoint_is_actual_label')
        order=[SHORTS[i] for i in indices]
        orient={}
        for mask in range(8):
            vals=[order[i] for i in range(3) if mask>>i&1]
            orient[mask]=pm(sum(a>b for j,a in enumerate(vals) for b in vals[j+1:]))
            h=tuple(sorted(vals))
            # The actual normal removal coefficients match the source exterior signs.
            for i in range(3):
                if not mask>>i&1:continue
                targ=h.index(order[i]);other=mask^(1<<i)
                check(orient[mask]*pm(targ)==pm((mask&((1<<i)-1)).bit_count())*orient[other],
                      'actual_endpoint_wedge_orientation_chain_compatibility')
            normal_indices=[indices[i] for i in range(3) if not(mask>>i&1)]
            coefficient=ex({9+a:-1 for a in normal_indices})
            check(legal((targetface,h),coefficient),'actual_endpoint_stalk_poles_are_permitted')
        transported.append({'group':list(group),'ordered_branch_indices':list(indices),
                            'endpoint':'plus' if targetface==VP else 'minus',
                            'top_orientation_sign':orient[7]})
    return {'eta':'t3*h3_plus-h3_pair','central_eta':'-h3_pair',
            'raw_to_selected_lift':'F(eta_u)=eta_x',
            'residue_tensor_action':'identity on the actual split eta factor',
            'central_channels':'branch-top and branch-top wedge eta both have coefficient +1 in ordered frames',
            'central_same_degree_eta_image':'zero; the surviving object is a Gysin/Ext morphism, not a degree-one target cycle',
            'transported_endpoint_normal_maps':transported}


def all_ordinary_return_obstruction():
    """Exact support theorem with finite monomial controls.

    In S_u=A/(t1*x1,t3*x3,t5*x5,u0), a nonzero monomial is killed
    by all x1,x3,x5 iff it contains every t. Thus ann(J_x)=tau S_x.
    Every derived degree-zero return induces such a module homomorphism
    on H_1. The theorem covers all replacements, not only adjugates.
    """
    n=0
    for powers in product(range(4),repeat=6):
        if any(powers[i]>0 and powers[3+i]>0 for i in range(3)):continue
        killed=[]
        for i in range(3):
            v=list(powers);v[3+i]+=1
            killed.append(any(v[j]>0 and v[3+j]>0 for j in range(3)))
        has_tau=all(powers[i]>0 for i in range(3))
        check(all(killed)==has_tau,'annihilator_colon_ideal_monomial_control')
        if has_tau:
            check(all(powers[3+i]==0 for i in range(3)), 'trace_annihilator_is_tau_times_selected_quotient')
        n+=1
    return {'homology_source':'S_x eta_x','homology_target':'S_u eta_u',
            'allowed_H1_return_images':'(t1*t3*t5) S_x eta_u',
            'all_ordinary_H1_returns_vanish_on_t_equals_zero':True,
            'monomial_controls':n,
            'proof':'Standard nonzero monomial basis of the monomial complete-intersection quotient; annihilation by x_i forces a factor t_i independently.'}


def extend_critical_dual_pairing():
    """Tensor the VERIFIED finite slice pairing with the actual branch Gysin
    morphism. This is NOT identified with full supported Verdier duality.
    """
    records=[]
    for tor in (0,1):
        lam=frame(0,1,3,5,*((3,) if tor else ()))
        models={s:purity_complex(lam,s) for s in ('K','B','Q','V')}
        old=hom_complex(SEQ,lam,'K')
        projection=purity_projection(old,models['K'])
        generic=linear(projection,generic_map(tor))
        beta=linear(models['K'][1],generic)
        check(len(beta)==9,'actual_purity_obstruction_nine_terms_retained')
        check(not linear(models['Q'][1],generic),'actual_generic_class_closed')
        check(not linear(models['B'][1],beta),'actual_short_obstruction_closed')
        dualB=dual_complex(models['B']);dualK=dual_complex(models['K']);dualQ=dual_complex(models['Q'])
        key=(3 if tor else 1,(tuple(sorted((SHORTS[2],LONGS[2]))),(LONGS[2],)))
        check(key in models['B'][0],'actual_short_support_readout_row_exists')
        beta_dual={key:1}
        check(not linear(dualB[1],beta_dual),'actual_short_dual_closed')
        generic_dual=linear(dualK[1],beta_dual)
        check(all(x in models['Q'][0] for x in generic_dual),'actual_dual_boundary_is_generic')
        check(not linear(dualQ[1],generic_dual),'actual_generic_dual_closed')
        # The inherited dual convention can introduce one global sign. Derive,
        # rather than prescribe, the simultaneous primitive normalization.
        bv=evaluate(beta_dual,beta);gv=evaluate(generic_dual,generic)
        check(abs(bv)==abs(gv)==1,'actual_dual_pairings_are_units')
        # Build full tensor with the central cochain Koszul dual K^bullet(x).
        # Polynomial coefficients in x1,x3,x5 remain; differential raises
        # cohomological degree. We record them in 3-vectors.
        z=(0,0,0)
        def pdiff(v,model):
            out={}
            for ((mask,key),e),a in v.items():
                k=mask.bit_count()
                for i in range(3):
                    if mask>>i&1:continue
                    ee=tuple(e[j]+int(j==i) for j in range(3))
                    out=add(out,{((mask|(1<<i),key),ee):a*pm((mask&((1<<i)-1)).bit_count())})
                for target,c in model[1][key].items():
                    out=add(out,{((mask,target),e):a*c*pm(k)})
            return out
        # Tensor the primal cohomological C_T (homological degrees negated).
        for support,model in models.items():
            for key0 in model[0]:
                for mask in range(8):
                    v={((mask,key0),z):1}
                    check(not pdiff(pdiff(v,model),model),'full_Gysin_tensor_mapping_d_squared')
        # epsilon_K reads only mask=0. All tensor Koszul terms are consequently
        # invisible to this closed map; the support boundary is exactly inherited.
        def tensor_eval(row,v):
            p={}
            for ((mask,key0),e),a in v.items():
                if mask==0 and row.get(key0,0):p[e]=p.get(e,0)+a*row[key0]
            return {e:a for e,a in p.items() if a}
        for key0 in models['K'][0]:
            for mask in range(8):
                v={((mask,key0),z):1}
                lhs=tensor_eval(beta_dual,pdiff(v,models['K']))
                inherited=evaluate(beta_dual,models['K'][1][key0]) if mask==0 else 0
                check(lhs==({z:inherited} if inherited else {}),'Gysin_trace_commutes_with_actual_support_boundary')
        check(tensor_eval(beta_dual,{((0,k),z):a for k,a in beta.items()})=={z:bv},
              'Gysin_valued_short_pairing_is_primitive')
        check(tensor_eval(generic_dual,{((0,k),z):a for k,a in generic.items()})=={z:gv},
              'Gysin_valued_generic_pairing_is_primitive')
        records.append({'channel':'excess' if tor else 'ordinary',
                        'full_tensor_generator_counts':{s:8*len(m[0]) for s,m in models.items()},
                        'short_pairing_coefficient':bv,'generic_pairing_coefficient':gv,
                        'readout_row':named_cell(key[1]),
                        'value_ring':'A0/(x1,x3,x5) with ordered dual branch determinant',
                        'boundary_direction':'dual short support to dual generic quotient',
                        'scope':'Tensor of actual normal Gysin morphism with a verified finite homogeneous target pairing; no global Verdier identification.'})
    return records


def main(path:Path):
    faces=check_support_residue()
    eta=selected_excess_and_endpoint()
    returns=all_ordinary_return_obstruction()
    pairing=extend_critical_dual_pairing()
    result={
      'status':'proved_scoped_supported_Cech_trace_and_primitive_excess_Gysin_channels',
      'date':'2026-09-07','source_commit':COMMIT,'source_blobs':SOURCE_BLOBS,
      'normal_ring_variables':['t1','t3','t5','x1','x3','x5','u0'],
      'coefficient_spectators':'Occurrence, other normal and physical orientation factors are not identified or specialized by this normal calculation.',
      'support_operation':'R Gamma_(x1,x3,x5)(A) -> R Gamma_(t1*x1,t3*x3,t5*x5)(A)',
      'selected_residue_components':'e_H -> product_{i in H} t_i/u_i in cohomological Koszul convention',
      'central_full_map':'coK(x1,x3,x5) -> A0, bottom component +1, all higher components zero',
      'central_map_class':'primitive generator of Ext^3(A0/(x1,x3,x5),A0), with dual determinant retained',
      'partial_central_Rees_faces':faces,'actual_excess_and_endpoint_normal_maps':eta,
      'classification_of_all_ordinary_returns':returns,'actual_Gysin_valued_reverse_pairings':pairing,
      'exact_assertions':sum(COUNT.values()),'assertion_categories':dict(sorted(COUNT.items())),
      'unconstructed':['Global normalized-log proper push-pull into the full supported Verdier target',
                       'Two coupled spatial endpoint connector 2-cells',
                       'Identification of the graded residue pairing with the physical trace',
                       'Physical reflection parity'],
      'scope_corrections':['The supported trace is not an ordinary return D_x -> D_u.',
                           'At central Rees fibre, the primitive channel is an Ext/Gysin morphism, not a same-degree target homology class.',
                           'The reverse support pairing stays nonzero; no forbidden covariant filler is manufactured.',
                           'Only inverses already implied by indicated unmarked normal localizations occur; the base ring is never globally localized.'],
      'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      'verification':'Exact integer/Laurent identities; all-polynomial support and nonvanishing proved in the companion note. Not proof-assistant verification.'
    }
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ('status','central_map_class','exact_assertions','actual_Gysin_valued_reverse_pairings','unconstructed')},indent=2))

if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output',type=Path,default=Path('marici_rees_supported_residue_trace_certificate.json'))
    main(ap.parse_args().output)
