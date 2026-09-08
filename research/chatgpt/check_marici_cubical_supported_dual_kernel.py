#!/usr/bin/env python3
"""Spatial cubical dual and cap kernel for Marici's complete coefficient target.

Reconstructs the 215-state target from its pinned rules, constructs actual
cubical interval cells [H,S], their flag triangulations and Serre diagonal,
and realizes the full support filtration contravariantly. Each coefficient
frame is an explicitly specified relative cubical cell complex. The critical
branch-purity Hom dual is realized in that geometry, not renamed without a
spatial map. Both carrier endpoint collar operators are retained.

This verifies a finite/graded incidence kernel. It does NOT assert equality
with an unspecified ringed supported-Verdier functor, supply all physical
source-sheet structure maps, or choose a physical reflection parity.

Python 3.10+, standard library only. Prior source/Hom helpers included below.
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
 'research/voevodsky/check_d03_normalized_blowdown_counit.py':'0fcbbf37a4f70dc0c2787ad7cb954287b9e97403',
 'src/ledger/20260814-136 Canonical AW-Cap Roof and the Endpoint-Connector Gap.md':'9afc5c63217bcf0240bd4837f342981eac680697',
 'src/ledger/20260815-184 Loaded AW Collar Principal-Line Repair and the Spatial Connector Gate.md':'68f960715e1c064411f3869daed7edaa2e6ee7cc',
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



def rees_branch_selection():
    """The actual repeated pair stays (u0,t3*x3); only the plus branch is selected.

    F: K(t1*x1,t3*x3,t5*x5,u0,t3*x3) ->
       K(x1,x3,x5,u0,t3*x3).
    G is the complementary-minor/adjugate return on the branch factor.
    """
    z=(0,)*7  # t1,t3,t5,x1,x3,x5,u0
    def mono(i):return tuple(int(j==i) for j in range(7))
    def plus(a,b):return tuple(x+y for x,y in zip(a,b))
    t=(mono(0),mono(1),mono(2),z,z)
    sel=(mono(3),mono(4),mono(5),mono(6),plus(mono(1),mono(4)))
    raw=tuple(plus(a,b) for a,b in zip(t,sel))
    total=tuple(sum(v[j] for v in t) for j in range(7))
    def factor(mask,complement=False):
        return tuple(sum(t[i][j] for i in range(5) if bool(mask>>i&1)!=complement)
                     for j in range(7))
    def d(v,seq):
        out={}
        for (mask,m),a in v.items():
            for i,u in enumerate(seq):
                if mask>>i&1:
                    key=(mask^(1<<i),plus(m,u))
                    out=add(out,{key:a*pm((mask&((1<<i)-1)).bit_count())})
        return out
    def op(v,complement=False):
        return {(mask,plus(m,factor(mask,complement))):a for (mask,m),a in v.items()}
    eta_raw={(2,z):1,(16,z):-1}
    eta_sel={(2,mono(1)):1,(16,z):-1}
    for mask in range(32):
        v={(mask,z):1}
        check(not d(d(v,raw),raw) and not d(d(v,sel),sel),'Rees_repeated_normal_d_squared')
        check(d(op(v),sel)==op(d(v,raw)),'Rees_branch_selection_F_chain_map')
        check(d(op(v,True),raw)==op(d(v,sel),True),'Rees_adjugate_G_chain_map')
        check(op(op(v),True)=={(mask,total):1},'Rees_GF_is_branch_determinant')
        check(op(op(v,True))=={(mask,total):1},'Rees_FG_is_branch_determinant')
    check(not d(eta_raw,raw) and not d(eta_sel,sel),'Rees_excess_generators_closed')
    check(op(eta_raw)==eta_sel,'Rees_selection_preserves_primitive_excess')
    multiplied={(mask,plus(m,total)):a for (mask,m),a in eta_raw.items()}
    check(op(eta_sel,True)==multiplied,'Rees_adjugate_return_multiplies_excess_by_branch_determinant')
    check(op({(31,z):1},True)=={(31,z):1},'Rees_adjugate_top_volume_coefficient_one')
    def central(v):return {k:a for k,a in v.items() if not any(k[1][:3])}
    check(central(eta_sel)=={(16,z):-1},'Rees_selected_excess_survives_central_face')
    check(central(op(eta_sel,True))=={},'Rees_adjugate_excess_dies_central_face')
    return {'raw_normal_sequence':['t1*x1','t3*x3','t5*x5','u0','t3*x3'],
            'branch_selected_sequence':['x1','x3','x5','u0','t3*x3'],
            'raw_eta':'h3_plus-h3_pair','selected_eta':'t3*h3_plus-h3_pair',
            'F_eta_coefficient':1,'G_eta_coefficient':'t1*t3*t5',
            'G_top_volume_coefficient':1,'FG_GF':'(t1*t3*t5) id',
            'central_selected_eta':'-h3_pair','central_G_eta':0,
            'scope':'Canonical maps of the actual repeated-normal Koszul sources under the declared product-Rees base change; not a map from them into the physical endpoint/Q target.'}


def cube_dimension(c):return len(c[0])-len(c[1])

def cube_boundary(c):
    """Oriented actual [0,1]^(S-H), all axes in the source diagonal order."""
    f,h=c;out={}
    for i,a in enumerate(x for x in f if x not in h):
        upper=(f,tuple(sorted(h+(a,))))
        lower=(tuple(x for x in f if x!=a),h)
        out[upper]=pm(i);out[lower]=-pm(i)
    return out
CUBED={c:cube_boundary(c) for c in CELLS}

def cube_gauge(c):
    f,h=c
    return pm(len(f)+len(h)*(3-len(f))+sum(f.index(a) for a in h))

def intervals_faces(c):
    """All faces, including the cell, of a cubical interval."""
    f,h=c;free=tuple(a for a in f if a not in h);out=[]
    for states in product(range(3),repeat=len(free)):
        # 0 fixed zero, 1 free, 2 fixed one.
        ff=tuple(sorted(h+tuple(a for a,s in zip(free,states) if s)))
        hh=tuple(sorted(h+tuple(a for a,s in zip(free,states) if s==2)))
        out.append((ff,hh))
    return out

from itertools import permutations

def triangulate_cube(c):
    f,h=c;free=tuple(a for a in f if a not in h);out={}
    for order in permutations(free):
        flag=[h];current=h
        for a in order:
            current=tuple(sorted(current+(a,)));flag.append(current)
        inv=sum(order[i]>order[j] for i in range(len(order)) for j in range(i+1,len(order)))
        out[tuple(flag)]=pm(inv)
    return out

TRI={c:triangulate_cube(c) for c in CELLS}

def flag_boundary(flag):
    if len(flag)==1:return {}
    return {flag[:i]+flag[i+1:]:pm(i) for i in range(len(flag))}

def apply_flag_d(v):
    out={}
    for flag,a in v.items():out=add(out,scale(flag_boundary(flag),a))
    return out


def cube_diagonal(c):
    """Tensor interval AW/Serre diagonal; no averaging or axis inversion."""
    f,h=c;free=tuple(a for a in f if a not in h);out={}
    for mask in range(1<<len(free)):
        left_free=tuple(a for i,a in enumerate(free) if mask>>i&1)
        middle=tuple(sorted(h+left_free))
        left=(middle,h);right=(f,middle)
        inv=sum(not(mask>>i&1) and bool(mask>>j&1)
                for i in range(len(free)) for j in range(i+1,len(free)))
        out[(left,right)]=pm(inv)
    return out
DIAGONAL={c:cube_diagonal(c) for c in CELLS}

def tensor_cube_d(v):
    out={}
    for (a,b),n in v.items():
        out=add(out,{(x,b):n*s for x,s in CUBED[a].items()},
                    {(a,y):n*pm(cube_dimension(a))*s for y,s in CUBED[b].items()})
    return out

def cube_action(c,g):
    f,h=c;free=tuple(a for a in f if a not in h)
    mapped=[group_diag(a,g) for a in free]
    inv=sum(a>b for i,a in enumerate(mapped) for b in mapped[i+1:])
    return ((tuple(sorted(group_diag(a,g) for a in f)),
             tuple(sorted(group_diag(a,g) for a in h))),pm(inv))

def act_cube(v,g):
    out={}
    for c,a in v.items():
        t,s=cube_action(c,g);out=add(out,{t:a*s})
    return out


def grade_allowed_geometry(c,alpha):
    """Independent coordinate-face description, not a call to legal()."""
    f,h=c;fs=set(f);hs=set(h)
    for a in DS:
        i=IX[a];x=alpha[i];u=alpha[9+i]
        if x < -1:return False
        if x == -1 and a not in fs:return False
        if u < 0 and (a not in fs or a in hs):return False
        if u == 0 and a in hs:return False
    return True

def graded_target(alpha,support):
    cells={c:degree(c) for c in CELLS
           if target_pred(c,support) and legal(c,eadd(alpha,weight(c[0])))}
    d={c:{} for c in cells}
    for c in cells:
        for (t,m),a in BD[c].items():
            if target_pred(t,support):
                check(t in cells,'homogeneous_target_actual_stalk_domain')
                d[c][t]=a
    return cells,d

def graded_cube(alpha,support):
    cells={c:cube_dimension(c) for c in CELLS
           if target_pred(c,support) and grade_allowed_geometry(c,alpha)}
    d={c:{t:a for t,a in CUBED[c].items() if t in cells} for c in cells}
    return cells,d


def realization_gauge(x):
    mask,c=x;k=cube_dimension(c);m=mask.bit_count()
    return pm(m+k*(k+1)//2)*cube_gauge(c)


def spatial_hom_d(x,available,pair=(0,3),branch=BRANCH):
    """Actual product incidence: residual normal interval, excess loop, cube.

    Coefficient face quotients decide when a boundary endpoint is relative.
    Source coordinates already in the selected branch have zero differential.
    """
    mask,c=x;out={};m=mask.bit_count()
    for i,a in enumerate(pair):
        if mask>>i&1 and a not in branch:
            y=(mask^(1<<i),c)
            if y in available:out[y]=pm((mask&((1<<i)-1)).bit_count())
    for t,s in CUBED[c].items():
        y=(mask,t)
        if y in available:out[y]=pm(m)*s
    return out


def geometric_purity_support(lam,seq=SEQ,support='K'):
    """Independent cubical face selection after branch purity."""
    branch=seq[:3];pair=seq[3:];bs=mask_degree(branch,7);out={}
    for mask in range(4):
        alpha=eadd(eadd(lam,bs),mask_degree(pair,mask))
        for c in CELLS:
            if not target_pred(c,support):continue
            f,h=c
            if not grade_allowed_geometry(c,alpha):continue
            valid=True
            for i in branch:
                a=SHORTS[i]
                # At a selected branch normal a free cube direction vanishes.
                # Its only remaining points are the correct fixed 0/1 face.
                if a in f and a not in h:valid=False;break
                bit=int(a in h)
                if alpha[9+i]!=bit:valid=False;break
            if valid:out[(mask,c)]=cube_dimension(c)+mask.bit_count()
    return out


def physical_cube_pair(available):
    """Realize the active CW rows as a relative subcomplex of W x I x S1.

    I has vertices 0 and 2 and edge 1, oriented d(edge)=v0-v2.
    The S1 factor has one vertex and its actual zero-boundary excess 1-cell.
    """
    chosen={(int(bool(m&1)),int(bool(m&2)),c) for m,c in available}
    closure=set()
    for i,j,c in chosen:
        for ii in ((0,1,2) if i==1 else (i,)):
            for jj in ((0,1) if j==1 else (0,)):
                closure.update((ii,jj,f) for f in intervals_faces(c))
    relative=closure-chosen
    for i,j,c in relative:
        for ii in ((0,1,2) if i==1 else (i,)):
            for jj in ((0,1) if j==1 else (0,)):
                for f in intervals_faces(c):
                    check((ii,jj,f) in relative,'discarded_product_cells_are_closed_subcomplex')
    return {'ambient_product_subcomplex_cells':len(closure),
            'relative_subcomplex_cells':len(relative),'active_cells':len(chosen)}


def transpose_plain(model):
    gs,dd=model;d={c:{} for c in gs}
    for x,v in dd.items():
        for y,a in v.items():d[y][x]=a
    return d


def cube_name(c):return '['+named_cell((c[1],()))+' <= '+named_cell((c[0],()))+']'

def export_cube_chain(v):return {cube_name(c):a for c,a in sorted(v.items())}


def endpoint_collars():
    """Transfer BOTH actual corridor homotopies, not arbitrary endpoint units.

    Work in the actual unmarked homogeneous unit lines. Vertex gauge is
    derived by d(edge)=terminal-initial along the connected flip graph.
    The operators on cube 2-cells are transposes of these actual path chains.
    """
    vertices=[f for f in FACES if len(f)==3];edges=[f for f in FACES if len(f)==2]
    raw={f:{t[0]:a for (t,_),a in BD[(f,())].items()} for f in edges}
    gauges={VP:1}
    while len(gauges)<len(vertices):
        before=len(gauges)
        for e in edges:
            (a,sa),(b,sb)=list(raw[e].items())
            if a in gauges and b not in gauges:gauges[b]=-sa*sb*gauges[a]
            elif b in gauges and a not in gauges:gauges[a]=-sa*sb*gauges[b]
        if len(gauges)==before:raise AssertionError('disconnected actual flip graph')
    check(gauges[VM] in (-1,1),'endpoint_orientation_gauge_derived')
    mid=tuple(sorted((LONGS[0],SHORTS[1],SHORTS[3])))
    c=tuple(sorted((LONGS[0],SHORTS[0],SHORTS[3])))
    v=tuple(sorted((LONGS[0],SHORTS[0],SHORTS[4])))
    def path(vs):
        out={}
        for left,right in zip(vs,vs[1:]):
            e=tuple(sorted(set(left)&set(right)))
            check(e in raw and set(raw[e])=={left,right},'actual_labelled_endpoint_collar_edge')
            a=gauges[right]*raw[e][right]
            check(a*raw[e][left]==-gauges[left],'endpoint_collar_incidence_sign')
            out[(e,())]=a
        return out
    hp=path([VP,mid]);hm=path([VM,v,c,mid])
    primal={c:{t:a for (t,m),a in BD[c].items()} for c in CELLS if not c[1]}
    for vtx,h in ((VP,hp),(VM,hm)):
        check(linear(primal,h)=={(mid,()):gauges[mid],(vtx,()):-gauges[vtx]},
              'both_carrier_endpoint_2cell_equations')
    gamma=add(hp,scale(hm,-1))
    check(linear(primal,gamma)=={(VM,()):gauges[VM],(VP,()):-gauges[VP]},
          'same_carrier_corridor_endpoint_difference')
    # On complementary cubes at grade zero, cap sends c* -> gauge(c) cube(c).
    # Thus the transported collar functional on cube(e) is gauge(e)*h(e).
    grade0=graded_cube(ZERO,'K')
    lp={c:cube_gauge(c)*a for c,a in hp.items()}
    lm={c:cube_gauge(c)*a for c,a in hm.items()}
    for vtx,row in ((VP,lp),(VM,lm)):
        for x in grade0[0]:
            value=evaluate(row,grade0[1][x])
            expected=cube_gauge(x)*(gauges[mid]*int(x==(mid,()))-gauges[vtx]*int(x==(vtx,())))
            check(value==expected,'cap_transfers_both_endpoint_homotopies_on_all_cells')
    # The two endpoint meridian 2-cycles are lower boundaries of actual 3-cubes.
    e_space=graded_cube(ZERO,'E');sigma={}
    for name,vtx in (('plus',VP),('minus',VM)):
        fullcube=(vtx,())
        chain={t:a for t,a in CUBED[fullcube].items() if t in e_space[0]}
        check(len(chain)==3,'endpoint_meridian_three_actual_square_faces')
        check(not linear(e_space[1],chain),'endpoint_meridian_is_closed_with_frame_fixed')
        sigma[name]=chain
    sdr=reduce_sdr(*e_space)
    coords={n:linear(sdr['P'],v) for n,v in sigma.items()}
    check(sdr['homology']=={2:1},'both_endpoint_dual_complex_has_one_meridian')
    check(all(len(v)==1 and abs(next(iter(v.values())))==1 for v in coords.values()),
          'both_endpoint_meridians_integrally_primitive')
    return {'midpoint':named_cell((mid,())),
            'plus_collar':export_cube_chain(lp),'minus_collar':export_cube_chain(lm),
            'endpoint_vertex_orientation_gauges':{'plus':gauges[VP],'minus':gauges[VM],'mid':gauges[mid]},
            'plus_meridian':export_cube_chain(sigma['plus']),
            'minus_meridian':export_cube_chain(sigma['minus']),
            'meridian_coordinates':{k:list(v.values())[0] for k,v in coords.items()},
            'scope':'The actual two labelled carrier homotopies after cap transfer in the unmarked unit frame; not the complete normalization-sheet connector in every Rees/Tor frame.'}


def tensor_flag_d(v):
    out={}
    for (a,b),n in v.items():
        out=add(out,{(x,b):n*t for x,t in flag_boundary(a).items()},
                    {(a,y):n*pm(len(a)-1)*t for y,t in flag_boundary(b).items()})
    return out

def simplicial_diagonal(flag):
    return {(flag[:j+1],flag[j:]):1 for j in range(len(flag))}

def flag_tensor_contraction(v,base):
    # Augmented simplex-cone contraction on the two actual cube triangulations.
    # Every flag in a cube [H,S] may be prefixed with the same least vertex H.
    out={}
    for (a,b),n in v.items():
        if a[0]!=base:out=add(out,{((base,)+a,b):n})
        if len(a)==1 and b[0]!=base:out=add(out,{((base,),(base,)+b):n})
    return out

def diagonal_subdivision_comparison():
    """Actual acyclic-carrier homotopy, with cube and endpoint support fixed."""
    h={};simp={};cub={}
    for c in sorted(CELLS,key=lambda c:(cube_dimension(c),c)):
        simp[c]=linear({f:simplicial_diagonal(f) for f in TRI[c]},TRI[c])
        cub[c]={}
        for (a,b),n in DIAGONAL[c].items():
            for x,u in TRI[a].items():
                for y,v in TRI[b].items():cub[c]=add(cub[c],{(x,y):n*u*v})
        check(simp[c]==cub[c],'simplicial_cubical_diagonals_agree_strictly_under_triangulation')
        z=add(simp[c],scale(cub[c],-1),scale(linear(h,CUBED[c]),-1))
        check(not tensor_flag_d(z),'subdivision_cap_difference_is_closed')
        h[c]=flag_tensor_contraction(z,c[1])
        check(add(tensor_flag_d(h[c]),linear(h,CUBED[c]))==add(simp[c],scale(cub[c],-1)),
              'full_simplicial_cubical_cap_comparison_homotopy')
        for (a,b),n in h[c].items():
            check(all(set(c[1])<=set(v)<=set(c[0]) for v in a+b),
                  'cap_comparison_homotopy_preserves_each_closed_cube_support')
    return {'strict_diagonal_compatibility':True,
            'nonzero_homotopy_columns':sum(bool(v) for v in h.values()),
            'total_homotopy_terms':sum(len(v) for v in h.values()),
            'uses_only_existing_flag_products':True,
            'relative_support_preserved':True}


def full_morse_dual_data(all_flags):
    """Actual complete source five-triangle identity in the same spatial ball.

    Each flag is in its original principal occurrence line. Its coefficient
    here is the coefficient after pairing with that line's dual frame, not a
    substitution of the occurrence variables by one.
    """
    o=();D=(LONGS[0],);ec=tuple(sorted((SHORTS[1],SHORTS[3])))
    er=tuple(sorted((LONGS[0],SHORTS[3])))
    mid=tuple(sorted((LONGS[0],SHORTS[1],SHORTS[3])))
    c=tuple(sorted((LONGS[0],SHORTS[0],SHORTS[3])))
    v=tuple(sorted((LONGS[0],SHORTS[0],SHORTS[4])))
    H={(o,ec,mid):-1,(o,ec,VP):1,
       (D,er,c):-1,(D,er,mid):1,(o,D,mid):1}
    q={(o,VP):-1,(o,D):1,(D,c):1}
    def path(a,b):
        e=tuple(sorted(set(a)&set(b)))
        check(len(e)==2,'Morse_collar_uses_actual_flip_face')
        return {(e,b):1,(e,a):-1}
    hp=path(VP,mid);hm=add(path(VM,v),path(v,c),path(c,mid))
    gamma=add(hp,scale(hm,-1));tail=add(path(c,v),path(v,VM));both=add(q,tail)
    check(len(H)==5 and len(both)==7 and len(gamma)==8,'complete_Morse_roof_collar_term_counts')
    for chain in (H,q,hp,hm,gamma,both):
        check(set(chain)<=all_flags,'all_Morse_and_endpoint_terms_are_in_same_flag_ball')
    check(apply_flag_d(H)==add(both,scale(gamma,-1)),'whole_Morse_identity_in_same_dual_cap_subdivision')
    check(apply_flag_d(hp)=={(mid,):1,(VP,):-1},'full_plus_endpoint_flag_homotopy')
    check(apply_flag_d(hm)=={(mid,):1,(VM,):-1},'full_minus_endpoint_flag_homotopy')
    # Keep the actual higher cochain operator; do not drop it in a generic subposet.
    for f in all_flags:
        if len(f)!=2:continue
        coboundary_on_H=sum(n*flag_boundary(t).get(f,0) for t,n in H.items())
        check(coboundary_on_H==both.get(f,0)-gamma.get(f,0),
              'Morse_higher_operator_dual_Stokes_on_every_edge_covector')
    def inB(f):return all(any(a in SHORTS for a in v) for v in f)
    qpart={f:n for f,n in both.items() if not inB(f)}
    dhpart={f:n for f,n in apply_flag_d(H).items() if not inB(f)}
    check(qpart==dhpart,'old_covariant_generic_nullhomotopy_is_not_falsely_revived')
    return {'Morse_triangles':5,'completed_roof_edges':7,'corridor_edges':8,
            'both_endpoint_operator_equations':True,'Morse_higher_operator_kept':True,
            'old_covariant_generic_map_stays_null':True}


def main(path):
    check(len(CELLS)==215,'exact_215_target_interval_cells')
    naked={c:degree(c) for c in CELLS},{c:{t:a for (t,m),a in BD[c].items()} for c in CELLS}
    tr=transpose_plain(naked)
    all_flags=set()
    for c in CELLS:
        check(not linear(CUBED,CUBED[c]),'geometric_cubical_boundary_squared')
        check(scale(CUBED[c],cube_gauge(c))=={t:a*cube_gauge(t) for t,a in tr[c].items()},
              'entire_target_transpose_is_signed_actual_cube_incidence')
        check(apply_flag_d(TRI[c])==linear(TRI,CUBED[c]),'triangulation_is_actual_flag_chain_map')
        for flag in TRI[c]:
            for k in range(1,len(flag)+1):all_flags.update(combinations(flag,k))
        check(tensor_cube_d(DIAGONAL[c])==linear(DIAGONAL,CUBED[c]),'actual_spatial_cap_diagonal_chain_map')
        left={};right={}
        for (a,b),n in DIAGONAL[c].items():
            for (x,y),m in DIAGONAL[a].items():left=add(left,{(x,y,b):m*n})
            for (x,y),m in DIAGONAL[b].items():right=add(right,{(a,x,y):m*n})
        check(left==right,'spatial_cap_diagonal_coassociative')
        # Both projections of the interval category have the required variances.
        for t in intervals_faces(c):
            check(set(c[1])<=set(t[1]) and set(t[0])<=set(c[0]),'interval_correspondence_opposite_variances')
        for g in G:
            image,s=cube_action(c,g)
            check(act_cube(CUBED[c],g)==scale(CUBED[image],s),'geometric_D3_cube_chain_covariance')
            # Preserve the physical global orientation character explicitly.
            (pc,ps)=act_cell(c,g)
            check(pc==image and ps*cube_gauge(pc)==pm(g[1])*cube_gauge(c)*s,
                  'duality_retains_ambient_orientation_character')
    check(len(all_flags)==509,'same_509_flag_spatial_carrier')
    check(Counter(len(f)-1 for f in all_flags)=={0:45,1:170,2:210,3:84},'exact_flag_census')
    wq={c for c in CELLS if target_pred(c,'Q')};we={c for c in CELLS if target_pred(c,'E')}
    check(wq<=we,'full_complementary_support_filtration')
    check((len(wq),len(we),len(CELLS))==(7,199,215),'dual_generic_endpoint_full_cell_counts')
    for subset in (wq,we):
        for c in subset:check(set(CUBED[c])<=subset,'complementary_support_is_closed_subcomplex')

    # Every boundary choice is from actual coefficient inequalities. A finite
    # threshold census and the printed formulas prove all exponent values.
    frames=[ZERO,GAMMA]
    for j in range(18):
        for n in (-2,-1,0,1,2):frames.append(ex({j:n}))
    for n in range(512):frames.append(ex({9+i:1 for i in range(9) if n>>i&1}))
    frames=list(dict.fromkeys(frames));frame_record=[]
    models={}
    for alpha in frames:
        actual=graded_target(alpha,'K');spatial=graded_cube(alpha,'K')
        check(set(actual[0])==set(spatial[0]),'coefficient_domains_equal_relative_cube_faces')
        dual=transpose_plain(actual)
        for c in spatial[0]:
            check(scale(spatial[1][c],cube_gauge(c))=={t:a*cube_gauge(t) for t,a in dual[c].items()},
                  'all_frame_spatial_duality_chain_isomorphism')
        # The excluded cells are a genuine closed subcomplex, not a fake projection.
        bad=set(CELLS)-set(spatial[0])
        for c in bad:check(set(CUBED[c])<=bad,'coefficient_forbidden_faces_are_closed')
        if alpha in (ZERO,GAMMA):
            supports={}
            for sup in ('K','B','V','E','Q','BV'):
                sc=graded_cube(alpha,sup);hh,_=reduce_fast(*sc)
                supports[sup]={'cells':len(sc[0]),'homology':hh}
            frame_record.append({'normal_grade':'unit' if alpha==ZERO else 'three_long_normals','supports':supports})
        models[alpha]=spatial
    multiplication_count=0
    for bits in range(512):
        alpha=ex({9+i:1 for i in range(9) if bits>>i&1});low=models[alpha]
        for j in range(9):
            if bits>>j&1:continue
            b=eadd(alpha,ex({9+j:1}));hi=models[b]
            table={c:({c:1} if c in low[0] else {}) for c in hi[0]}
            for c in hi[0]:
                check(linear(table,hi[1][c])==linear(low[1],table[c]),
                      'actual_coefficient_multiplication_dual_is_spatial_quotient')
            multiplication_count+=1
    check(multiplication_count==2304,'all_nine_normal_cube_multiplication_maps')

    cap_comparison=diagonal_subdivision_comparison()
    morse_data=full_morse_dual_data(all_flags)
    collars=endpoint_collars()
    critical=[]
    for tor in (False,True):
        lam=frame(0,1,3,5,*((3,) if tor else ()))
        old={s:hom_complex(SEQ,lam,s) for s in ('K','B','V','E','Q')}
        pure={s:purity_complex(lam,s) for s in old}
        proj={s:purity_projection(old[s],pure[s]) for s in old}
        q=linear(proj['Q'],generic_map(tor));beta=linear(pure['K'][1],q)
        check(len(beta)==9 and not linear(pure['B'][1],beta),'actual_nine_term_transgression_reused')
        spatial={};shapes={};hom={}
        for s in pure:
            dg=dual_complex(pure[s]);sg=geometric_purity_support(lam,support=s)
            check(sg==dg[0],'purity_Hom_dual_cells_equal_spatial_source_target_strata')
            sd={x:spatial_hom_d(x,sg) for x in sg}
            for x in sg:
                check(scale(sd[x],realization_gauge(x))=={y:a*realization_gauge(y) for y,a in dg[1][x].items()},
                      'purity_dual_equals_genuine_product_cellular_boundary')
            spatial[s]=(sg,sd);shapes[s]=physical_cube_pair(sg)
            hom[s]=reduce_fast(sg,sd)[0]
        record={'channel':'excess' if tor else 'ordinary','relative_CW_pairs':shapes,'homology':hom}
        if tor:
            special=(tuple(sorted((SHORTS[2],LONGS[2]))),(LONGS[2],))
            beta_row={(3,special):1};q_row={(3,((LONGS[2],),(LONGS[2],))):-1}
            sb={x:a*realization_gauge(x) for x,a in beta_row.items()}
            sq={x:a*realization_gauge(x) for x,a in q_row.items()}
            check(linear(spatial['K'][1],sb)==sq,'literal_relative_spatial_edge_realizes_reverse_connecting')
            check(not linear(spatial['B'][1],sb),'spatial_short_support_class_closed_rel_generic')
            check(evaluate(beta_row,beta)==1 and evaluate(q_row,q)==1,'spatial_reverse_pairing_unit_values')
            # The relative edge upper endpoint is killed by its x2 coefficient domain.
            upper=(special[0],special[0]);lower=((LONGS[2],),(LONGS[2],))
            check((3,upper) not in spatial['K'][0] and (3,lower) in spatial['Q'][0],
                  'relative_edge_has_exact_source_defined_upper_and_lower_endpoint')
            check(hom['B']=={3:1} and hom['Q']=={2:1} and hom['K']=={},'spatial_reverse_connecting_integral_isomorphism')
            # Retain all six transported frames, not just an abstract parity character.
            for g in G:
                seqg=tuple(IX[group_diag(SHORTS[a],g)] for a in SEQ);lg=act_exp(lam,g)
                for s in ('K','B','Q','V','E'):
                    pg=purity_complex(lg,s,seqg);dg=dual_complex(pg)
                    sg=geometric_purity_support(lg,seqg,s)
                    sd={x:spatial_hom_d(x,sg,seqg[3:],seqg[:3]) for x in sg}
                    check(sg==dg[0],'six_labelled_charts_same_geometric_strata_rule')
                    for x in sg:
                        check(scale(sd[x],realization_gauge(x))=={y:a*realization_gauge(y) for y,a in dg[1][x].items()},
                              'six_charts_complete_spatial_chain_realization')
                brr=act_hom(beta_row,g);qrr=act_hom(q_row,g)
                check(evaluate(brr,act_hom(beta,g))==1 and evaluate(qrr,act_hom(q,g))==1,
                      'six_charts_spatial_pairing_primitive')
            record.update({'dual_short_cell':cube_name(special),'dual_generic_cell':cube_name(lower),
              'pair_source_mask':3,'short_cell_geometric_coefficient':list(sb.values())[0],
              'generic_cell_geometric_coefficient':list(sq.values())[0],
              'evaluations':[1,1],'upper_endpoint_is_relative':True,
              'source_excess_retained_as_independent_one_cell':True})
        critical.append(record)

    # Endpoint residue channels remain explicit, in their actual DIFFERENT frames.
    endpoint_records=[]
    for tor in (False,True):
        le=frame(0,*((3,) if tor else ()));model=purity_complex(le,'V')
        geom=geometric_purity_support(le,support='V')
        mask=3 if tor else 1;x=(mask,(VP,VP))
        check(x in geom,'actual_endpoint_residue_is_same_space_labelled_vertex')
        # In these frames there is exactly one endpoint normal class.
        gd={y:spatial_hom_d(y,geom) for y in geom};hh,_=reduce_fast(geom,gd)
        check(hh.get(1+int(tor))==1,'spatial_endpoint_residue_class_primitive_in_actual_frame')
        endpoint_records.append({'channel':'excess' if tor else 'ordinary',
          'frame':list(le),'target_cube_vertex':cube_name((VP,VP)),
          'normal_cell_dimension':mask.bit_count(),'homology':hh})

    # Tensor the entire geometric differential with the supported residue.
    # Polynomial monomials use independent branch-section x1,x3,x5 coordinates;
    # the permitted localization is u_i=t_i*x_i, never the base coefficient ring.
    def mt_add(a,b):return tuple(x+y for x,y in zip(a,b))
    mz=(0,0,0)
    def mt_var(i):return tuple(int(j==i) for j in range(3))
    def td(v,kind,central):
        out={}
        for (h,x,e),a in v.items():
            if kind=='C' and h&central:continue
            for i in range(3):
                if h>>i&1:continue
                hh=h|(1<<i)
                if kind=='C' and hh&central:continue
                factor=mt_var(i) if kind=='K' else mz
                key=(hh,x,mt_add(e,factor))
                out=add(out,{key:a*pm((h&((1<<i)-1)).bit_count())})
            for y,c in spatial['K'][1][x].items():
                out=add(out,{(h,y,e):a*pm(h.bit_count())*c})
        return out
    def rho_tensor(v,central):
        out={}
        for (h,x,e),a in v.items():
            if h&central:continue
            factor=tuple(-int(h>>i&1) for i in range(3))
            out=add(out,{(h,x,mt_add(e,factor)):a})
        return out
    normal_columns=0
    for central in range(8):
        for h in range(8):
            for x in spatial['K'][0]:
                v={(h,x,mz):1};image=rho_tensor(v,central)
                check(td(image,'C',central)==rho_tensor(td(v,'K',central),central),
                      'full_supported_residue_times_spatial_kernel_chain_map')
                check(not td(td(v,'K',central),'K',central),
                      'supported_tensor_source_d_squared')
                check(not td(td(image,'C',central),'C',central),
                      'supported_tensor_target_d_squared')
                check(all(all(n>=0 or bool(hh>>i&1) for i,n in enumerate(e))
                          for hh,xx,e in image),
                      'supported_tensor_residue_only_in_permitted_Cech_summands')
                normal_columns+=1
    # All comparisons keep the independent residual source cells, including eta.
    check(normal_columns==8*8*len(spatial['K'][0]),'entire_supported_tensor_column_count')
    check(all(rho_tensor({(0,x,mz):1},7)=={(0,x,mz):1} for x in spatial['K'][0]),
          'central_Gysin_bottom_component_retained_on_whole_spatial_kernel')
    check(all(not rho_tensor({(h,x,mz):1},7) for h in range(1,8) for x in spatial['K'][0]),
          'central_localized_components_vanish_without_dropping_lower_component')
    rees=rees_branch_selection()
    result={'date':'2026-09-07','commit':COMMIT,'source_blobs':SOURCE_BLOBS,
      'status':'constructed_spatial_cubical_realization_of_graded_dual_and_cap',
      'cube_counts':dict(sorted(Counter(cube_dimension(c) for c in CELLS).items())),
      'flag_counts':dict(sorted(Counter(len(f)-1 for f in all_flags).items())),
      'dual_support_counts':{'Q_subcomplex':len(wq),'E_subcomplex':len(we),'K':len(CELLS)},
      'coefficient_frames_checked':len(frames),'multiplication_maps_checked':multiplication_count,
      'homogeneous_controls':frame_record,'both_endpoint_collar_operators':collars,
      'cap_subdivision_comparison':cap_comparison,'whole_Morse_endpoint_data':morse_data,
      'critical_source_target_spatial_models':critical,'endpoint_residue_frames':endpoint_records,
      'raw_source_excess_test':rees,'supported_tensor_columns':normal_columns,
      'assertions':dict(sorted(COUNT.items())),'total_exact_assertions':sum(COUNT.values()),
      'scope':[
        'The same labelled flag ball has an actual 215-cell cubical incidence structure; no physical filler has been adjoined.',
        'The complete signed target transpose, complementary support filtration, coefficient-face rules, and all normal multiplication maps are geometrically realized.',
        'After branch purity the critical derived-Hom dual is the cellular complex of explicit relative subcomplexes of W x I x S1.',
        'The nine-term obstruction and its generic row have unit pairing with an actual relative edge times the residual source normal/excess cells.',
        'The two known carrier endpoint homotopies are transferred through cap in their unit homogeneous frame, and both endpoint residue channels are retained in their own coefficient frames.',
        'These are not a proof that the different endpoint/generic frames admit one source-sheet mixed-variance morphism with all prescribed Rees transitions.',
        'No equality with the complete ringed support-Verdier functor or physical parity is asserted.'
      ],'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ('status','cube_counts','flag_counts','dual_support_counts','coefficient_frames_checked','multiplication_maps_checked','total_exact_assertions')},indent=2))
    print(json.dumps(critical,indent=2))

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output',type=Path,default=Path('marici_cubical_supported_dual_kernel_certificate.json'))
    args=p.parse_args();main(args.output)
