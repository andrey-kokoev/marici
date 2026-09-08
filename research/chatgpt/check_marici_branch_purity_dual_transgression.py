#!/usr/bin/env python3
"""Exact branch-supported purity and dual-transgression computation.

Self-contained standard-library script. Source/target combinatorics and
integer reduction helpers are retained from the preceding obstruction checker.
New maps compute regular closed-immersion purity on the actual stalk modules,
retain the excess normal, verify all homogeneous comparison cones, and form
the finite graded dual of the resulting mapping triangle.

The graded dual below is NOT identified with a full ringed Verdier kernel.
No physical parity or normalization-sheet push-pull map is asserted.
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

def main(path):
    baseline=dict(COUNT)
    check(len(CELLS)==215,'target_215_stalks')
    check_source()
    survivors={sup:sum(branch_survives(c,BRANCH) and target_pred(c,sup) for c in CELLS)
               for sup in ('K','B','V','E','Q','BV')}
    check(survivors=={'K':136,'B':129,'V':9,'E':127,'Q':7,'BV':120},'purity_stalk_census')
    check(sum(branch_survives(c,BRANCH) and c[0]==VP for c in CELLS)==1,'plus_endpoint_retains_fully_marked_state')
    check(sum(branch_survives(c,BRANCH) and c[0]==VM for c in CELLS)==8,'minus_endpoint_retains_all_normal_states')
    # Local one-normal duality: Koszul->dual top projection is reduction modulo
    # the normal. On a localization where that normal is invertible, both the
    # base-changed object and the local Koszul cohomology vanish. The universal
    # regular-sequence proof in the note establishes all exponents.
    records=[]
    for ns in product((0,-1),repeat=3):
        for n3 in (0,-1,-2):
            lam=list(GAMMA)
            for a,n in zip((0,1,5),ns):lam[9+a]=n
            lam[12]=n3;lam=tuple(lam)
            rec={'frame':{'u0':ns[0],'u1':ns[1],'u3':n3,'u5':ns[2]},'targets':{}}
            olds={};news={};maps={}
            for sup in ('V','E','Q','B','K','BV'):
                old=hom_complex(SEQ,lam,sup);new=purity_complex(lam,sup);p=purity_projection(old,new)
                cg,cd=cone_of_map(old,new,p)
                hc,pc=reduce_fast(cg,cd)
                check(not hc,'entire_purity_comparison_cone_integrally_acyclic')
                hn,_=reduce_fast(new[0],new[1])
                ho,_=reduce_fast(old[0],old[1])
                check(hn==ho,'purity_preserves_full_derived_Hom_groups')
                check(hn==reduced_excess(lam,sup),'independent_surviving_face_model_agrees')
                rec['targets'][sup]={'old_generators':len(old[0]),'purity_generators':len(new[0]),
                    'Ext':ext_groups(hn),'comparison_cone_unit_pivots':len(pc),'comparison_cone_homology':{}}
                olds[sup]=old;news[sup]=new;maps[sup]=p
            # Every actual off-diagonal support boundary is retained. Check the
            # connecting cochain to endpoints and from Q into the short boundary.
            for dom,cod in (('E','V'),('Q','B'),('BV','V')):
                for x in olds[dom][0]:
                    olddelta=restrict_vec(olds['K'][1][x],olds[cod])
                    left=linear(maps[cod],olddelta)
                    right=restrict_vec(linear(news['K'][1],maps[dom][x]),news[cod])
                    check(left==right,'purity_commutes_with_actual_support_connecting_components')
            records.append(rec)
    critical=[]; endpoints=[]
    for tor in (False,True):
        lam=frame(0,1,3,5,*((3,) if tor else ()))
        old={sup:hom_complex(SEQ,lam,sup) for sup in ('K','B','V','E','Q')}
        new={sup:purity_complex(lam,sup) for sup in old}
        pp={sup:purity_projection(old[sup],new[sup]) for sup in old}
        qold=generic_map(tor);q=linear(pp['Q'],qold)
        betaold=linear(old['K'][1],qold);beta=linear(new['K'][1],q)
        check(linear(pp['B'],betaold)==beta,'purity_transgression_of_actual_generic_class')
        check(len(beta)==9,'eighteen_to_nine_short_support_terms')
        check(not linear(new['B'][1],beta),'purified_short_transgression_closed')
        sdr={sup:reduce_sdr(new[sup][0],new[sup][1]) for sup in new}
        qc=linear(sdr['Q']['P'],q);bc=linear(sdr['B']['P'],beta)
        check(qc and gcd(*[abs(a) for a in qc.values()])==1,'purified_generic_is_primitive')
        check(bc and gcd(*[abs(a) for a in bc.values()])==1,'purified_obstruction_is_primitive')
        j=1+int(tor)
        check(sdr['E']['homology'].get(-j,0)==0,'branch_purity_does_not_create_forbidden_lift')
        entry={'channel':'Tor1' if tor else 'Tor0','map_frame':list(lam),
               'pure_groups':{sup:ext_groups(sdr[sup]['homology']) for sup in new},
               'generic':rows_with_coefficients(q,new['Q']),
               'boundary':rows_with_coefficients(beta,new['B'])}
        if tor:
            check(sdr['K']['homology']=={} and sdr['V']['homology']=={},'pure_Tor1_total_and_endpoint_acyclic')
            check(len(bc)==1 and abs(next(iter(bc.values())))==1,'pure_Tor1_boundary_line_primitive')
            survivor,eps=next(iter(bc.items()))
            beta_dual={x:eps*v[survivor] for x,v in sdr['B']['P'].items() if survivor in v}
            # Oriented trace functional on the exact finite graded mapping slice.
            check(evaluate(beta_dual,beta)==1,'dual_boundary_primitive_pairing')
            dB=dual_complex(new['B']);dK=dual_complex(new['K']);dQ=dual_complex(new['Q'])
            check(not linear(dB[1],beta_dual),'dual_boundary_functional_closed')
            generic_dual=linear(dK[1],beta_dual)
            check(all(x in dQ[0] for x in generic_dual),'dual_connecting_map_supported_in_Q')
            check(not linear(dQ[1],generic_dual),'dual_generic_functional_closed')
            check(evaluate(generic_dual,q)==1,'dual_connecting_primitive_pairing')
            # Explicit literal rows in source labels, not a scalar signature.
            special=(tuple(sorted((SHORTS[2],LONGS[2]))),(LONGS[2],))
            check(beta_dual=={(3,special):1},'dual_boundary_literal_row_x2_D25')
            check(generic_dual=={(3,((LONGS[2],),(LONGS[2],))):-1},'dual_generic_literal_row_minus_M25')
            # Compare every dual group to the integral original retraction.
            for sup in new:
                dual=dual_complex(new[sup]);dh,_=reduce_fast(dual[0],dual[1])
                check(dh=={-n:r for n,r in sdr[sup]['homology'].items()},'finite_dual_preserves_entire_free_homology')
            # All six branch/pair transports preserve the normal determinant frame,
            # physical cell sign, the actual maps, and both pairing values.
            for g in G:
                seqg=tuple(IX[group_diag(SHORTS[a],g)] for a in SEQ)
                lg=act_exp(lam,g)
                transformed={sup:purity_complex(lg,sup,seqg) for sup in ('Q','B','K')}
                for sup in transformed:
                    for x in new[sup][0]:
                        ax=act_hom({x:1},g)
                        check(all(y in transformed[sup][0] for y in ax),'pure_dual_transport_actual_support')
                        check(act_hom(new[sup][1][x],g)==linear(transformed[sup][1],ax),'pure_dual_transport_full_differential')
                qt=act_hom(q,g);bt=act_hom(beta,g)
                bd=act_hom(beta_dual,g);qd=act_hom(generic_dual,g)
                check(evaluate(bd,bt)==1 and evaluate(qd,qt)==1,'six_charts_dual_pairings_primitive')
                dk=dual_complex(transformed['K'])
                check(linear(dk[1],bd)==qd,'six_charts_dual_boundary_compatibility')
                original_g=hom_complex(seqg,lg,'K')
                projection_g=purity_projection(original_g,transformed['K'],seqg[:3])
                for x in old['K'][0]:
                    check(act_hom(pp['K'][x],g)==linear(projection_g,act_hom({x:1},g)),
                          'six_charts_purity_naturality')
            entry.update({'dual_boundary_row':named_hom(beta_dual),
                          'dual_generic_row':named_hom(generic_dual),
                          'duality_pairings':[1,1],
                          'graded_dual_scope':'Hom_Z of the finite homogeneous derived-Hom slice; not identified with the ringed supported Verdier kernel'})
        critical.append(entry)
        le=frame(0,*((3,) if tor else ()))
        eo=hom_complex(SEQ,le,'V');en=purity_complex(le,'V');ep=purity_projection(eo,en)
        ev=linear(ep,endpoint_map(tor));esdr=reduce_sdr(en[0],en[1]);evc=linear(esdr['P'],ev)
        check(len(evc)==1 and abs(next(iter(evc.values())))==1,'purity_preserves_primitive_endpoint_class')
        expected={(3 if tor else 1,(VP,VP)):(-1 if tor else 1)}
        check(ev==expected,'endpoint_residue_after_purity_is_fully_marked_unit')
        endpoints.append({'channel':'Tor1' if tor else 'Tor0','frame':list(le),
                          'class':rows_with_coefficients(ev,en),'Ext':ext_groups(esdr['homology'])})
    # Counterexample to using unshifted restriction on cohomology first:
    # the endpoint pole representative becomes zero after localizing then
    # restricting, but its whole Koszul->Cech map has a nonzero top-dual image.
    bottom=(VP,())
    check(not branch_survives(bottom,BRANCH),'raw_endpoint_pole_term_has_zero_ordinary_branch_base_change')
    check(branch_survives((VP,VP),BRANCH),'fully_marked_endpoint_survives_correct_purity')
    rees=rees_branch_selection()
    result={'date':'2026-09-07','source_commit':COMMIT,'source_blobs':SOURCE_BLOBS,
      'status':'proved_branch_regular_purity_and_graded_dual_transgression',
      'branch_ideal':['u1','u3','u5'],'retained_pair_after_branch_purity':['u0',0],
      'purity_det_degree':list(ex({10:-1,12:-1,14:-1})),
      'purity_homological_shift':-3,'purity_target_stalk_counts':survivors,
      'all_normal_frames':records,'critical_classes':critical,'endpoint_classes':endpoints,'product_Rees_branch_selection':rees,
      'assertions':dict(sorted(COUNT.items())),'total_exact_assertions':sum(COUNT.values()),
      'new_assertion_categories':counter_delta(COUNT,baseline),
      'scope':[
        'Regular closed-immersion purity is computed for the actual independent normal branch ideal, not substituted for a scalar branch selector in a reducible Rees fibre.',
        'The excess generator is retained through K_R/I(u0,0); no short normal or occurrence variable is inverted.',
        'All 144 homogeneous purity comparison cones are integrally acyclic; the all-polynomial theorem follows from Koszul purity on flat target stalks.',
        'The finite graded dual reverses the actual mapping-complex support triangle and has a primitive boundary pairing.',
        'No identification of this graded dual with a complete ringed support-Verdier dual, logarithmic normalized blowdown, or physical period functor is asserted.',
        'Primitive generic data stay obstructed as covariant lifts. Purity and the dual boundary formula do not assign physical parity or construct the normalization-sheet endpoint butterfly.'
      ],'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'checks':result['total_exact_assertions'],
        'stalks':survivors,'comparison_cones':len(records)*6,
        'critical':[{'channel':c['channel'],'groups':c['pure_groups'],
                     'generic_terms':len(c['generic']),'boundary_terms':len(c['boundary'])} for c in critical],
        'dual_boundary_row':critical[1]['dual_boundary_row'],'dual_generic_row':critical[1]['dual_generic_row']},indent=2))

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path('marici_branch_purity_dual_transgression_certificate.json'))
    args=parser.parse_args(); main(args.output)
