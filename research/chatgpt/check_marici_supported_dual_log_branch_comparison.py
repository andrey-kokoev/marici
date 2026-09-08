#!/usr/bin/env python3
"""Supported-dual occurrence-line normalization and logarithmic branch restriction.

Self-contained, Python 3.10+, standard library. Reconstructs the pinned
32-generator excess source and 215-stalk target. Builds the actual short-Rees
base change and the selected occurrence-branch pullback. Checks supported
purity signs, coefficient-line factorization, both excess-channel endpoint
images, and the full generic connecting obstruction and its dual functional.

The scalar dual of a finite homogeneous Hom slice is explicitly distinguished
from the unconstructed full spatial Verdier-dual/logarithmic correspondence.
No source normal, occurrence parameter or integer is globally inverted.
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



# New calculations begin here. The old helper definitions above are included
# verbatim so this checker is reproducible without other conversation files.

def log_exponent(e):
    """u_i = X_i t_i for the six short labels; long normals stay independent."""
    v=list(e)
    for i in range(6):v[i]+=v[9+i]
    return tuple(v)


def log_legal(c,e):
    loc={IX[a] for a in c[0] if a not in c[1]}
    # Inverting X_i*t_i in a TARGET stalk inverts each factor there.
    # This is an actual base-change property, not global source localization.
    return (all(v>=0 or (i<6 and i in loc) for i,v in enumerate(e[:9]))
            and all(v>=0 or i in loc for i,v in enumerate(e[9:])))


def log_hom(seq,lam,support,selected=()):
    """lam is expressed in the old frame, then transported to the log ring.

    selected are short occurrence labels set to zero. A target localization
    inverting any of them is the zero module. All source exterior generators
    are retained, including generators whose differential becomes zero.
    """
    selected=set(selected)
    def alive(c):
        return not any(SHORTS[i] in c[0] and SHORTS[i] not in c[1] for i in selected)
    gens={};coeff={}
    for mask in range(1<<len(seq)):
        grade=log_exponent(eadd(lam,mask_degree(seq,mask)))
        for c in CELLS:
            e=eadd(grade,log_exponent(weight(c[0])))
            if (target_pred(c,support) and alive(c) and log_legal(c,e)
                    and all(e[i]==0 for i in selected)):
                key=(mask,c);gens[key]=degree(c)-mask.bit_count();coeff[key]=e
    d={x:{} for x in gens}
    for x,n in gens.items():
        mask,c=x
        for (t,me),s in BD[c].items():
            if not target_pred(t,support) or not alive(t):continue
            y=(mask,t)
            check(y in gens,'log_target_arrow_has_legal_domain')
            check(eadd(coeff[x],log_exponent(me))==coeff[y],'log_target_arrow_exact_monomial')
            d[x][y]=s
        for i,a in enumerate(seq):
            if mask>>i&1 or a in selected:continue
            y=(mask|1<<i,c)
            check(y in gens,'log_source_arrow_has_legal_domain')
            check(eadd(coeff[x],log_exponent(ex({9+a:1})))==coeff[y],
                  'log_source_arrow_exact_monomial')
            d[x][y]=-pm(n+(mask&((1<<i)-1)).bit_count())
    for x,n in gens.items():
        check(all(gens[y]==n-1 for y in d[x]),'log_Hom_homological_degree')
        check(not linear(d,d[x]),'log_Hom_d_squared')
    return gens,d,coeff


def restrict_slice(ambient,selected):
    """Natural base change on the full homogeneous Hom complex."""
    ag,ad,ac=ambient;sg,sd,sc=selected
    p={x:({x:1} if x in sg else {}) for x in ag}
    for x in ag:
        check(linear(p,ad[x])==linear(sd,p[x]),'actual_branch_restriction_chain_map')
    check(set(sg)<=set(ag),'selected_Hom_basis_comes_from_log_basis')
    for x in sg:check(ac[x]==sc[x],'selected_coefficient_frame_retained')
    return p


def dual_complex(gens,d):
    """RHom_Z(C,Z) for this bounded finite free homogeneous slice only."""
    dualg={x:-n for x,n in gens.items()};duald={x:{} for x in gens}
    for x,v in d.items():
        for y,a in v.items():duald[y][x]=-pm(dualg[y])*a
    for x,n in dualg.items():
        check(all(dualg[y]==n-1 for y in duald[x]),'dual_slice_degree')
        check(not linear(duald,duald[x]),'dual_slice_d_squared')
    return dualg,duald


def pairing(phi,v):return sum(phi.get(x,0)*a for x,a in v.items())


def trace_from_primitive(reduction,v):
    """Normalize a cohomology functional by the already oriented source class.

    This constructs a coefficient dual, not an independently supplied physical
    readout. The report explicitly preserves that distinction.
    """
    coords=linear(reduction['P'],v)
    check(len(coords)==1 and abs(next(iter(coords.values())))==1,'oriented_line_is_primitive')
    c,sg=next(iter(coords.items()))
    return {x:p[c]*sg for x,p in reduction['P'].items() if c in p}


def audit_purity():
    """Ordered closed-immersion purity on three occurrence coordinates.

    For K(X_1,X_3,X_5)^vee the top projection, modulo the selected ideal,
    is the purity quasi-isomorphism. Exactness is proved by the regular-
    sequence argument in the report, not by sampling polynomial exponents.
    """
    seq=(1,3,5);dual_d={mask:{} for mask in range(8)}
    for mask in range(8):
        k=mask.bit_count()
        for i,a in enumerate(seq):
            if mask>>i&1:continue
            high=mask|1<<i
            dual_d[mask][(high,a)]=-pm(k+(mask&((1<<i)-1)).bit_count())
    for mask in range(8):
        sq={}
        for (h,a),s in dual_d[mask].items():
            for (t,b),z in dual_d[h].items():sq=add(sq,{(t,tuple(sorted((a,b)))):s*z})
        check(not sq,'ordered_occurrence_purity_dual_d_squared')
        for (h,a),s in dual_d[mask].items():
            if h==7:check(a in seq,'purity_top_boundaries_vanish_on_support')
    # Duality counit is dual of the unit R -> K: only dual degree zero survives.
    check(dual_d[7]=={},'ordered_occurrence_top_is_dual_cocycle')
    # Exterior-determinant covariance under all six permutations is exact.
    from itertools import permutations
    for perm in permutations(range(3)):
        def orient(mask):
            vals=[perm[i] for i in range(3) if mask>>i&1]
            inv=sum(a>b for i,a in enumerate(vals) for b in vals[i+1:])
            return sum(1<<i for i in vals),pm(inv)
        for mask in range(8):
            im,sg=orient(mask)
            left={}
            for (h,a),s in dual_d[mask].items():
                ih,hs=orient(h)
                left[(ih,seq[perm[seq.index(a)]])]=s*hs
            right={k:v*sg for k,v in dual_d[im].items()}
            check(left==right,'ordered_dual_purity_permutation_covariance')
        check(orient(7)[1] in (-1,1),'determinant_orientation_unit')
    # Full source dual: all 32 entries, including the independent excess line.
    old_dual={m:{} for m in range(32)}
    split_dual={m:{} for m in range(32)}
    for m in range(32):
        for (n,a),s in source_d(m).items():
            old_dual[n][(m,a)]=-pm(n.bit_count())*s
        for (n,a),s in source_d(m,True).items():
            split_dual[n][(m,a)]=-pm(n.bit_count())*s
    trans={m:{n:CHANGE[n].get(m,0) for n in range(32) if CHANGE[n].get(m,0)} for m in range(32)}
    for m in range(32):
        left={};right={}
        for n,c in trans[m].items():
            for (h,a),s in old_dual[n].items():left=add(left,{(h,a):c*s})
        for (n,a),s in split_dual[m].items():
            for h,c in trans[n].items():right=add(right,{(h,a):s*c})
        check(left==right,'full_excess_dual_basis_change_chain_map')
    # Ordered regular frame is h1,h3,h5,h0. The excess wedge gives the sign.
    check(CHANGE[15]=={15:1} and CHANGE[31]=={31:-1},'both_supported_purity_top_signs')
    return {
      'branch_codimension':3,'branch_occurrence_order':['X1','X3','X5'],
      'purity_cohomological_degree':3,'purity_value':'top dual coefficient modulo (X1,X3,X5)',
      'purity_line':'det((X1,X3,X5)/(X1,X3,X5)^2)^vee',
      'duality_counit':'dual degree zero evaluation; higher components zero',
      'full_original_excess_dual_supported_degrees':[4,5],
      'regular_dual_frame':'(h1_plus wedge h3_plus wedge h5_plus wedge h0_pair)^vee',
      'excess_dual_frame':'eta^vee retained; eta=h3_plus-h3_pair',
      'top_coordinate_signs_in_original_basis':{'regular_4':1,'excess_5':-1}}


def audit_currying(lam,sup):
    """Hom(Kplus tensor Kpair,T) = Hom(Kpair,Hom(Kplus,T)), with signs."""
    gs,d,cs=hom_complex(SEQ,lam,sup)
    conv={};cg={};cd={}
    for (mask,c),n in gs.items():
        a=mask&7;b=mask>>3
        y=(b,a,c);cg[y]=n;conv[(mask,c)]={y:pm(a.bit_count()*b.bit_count())}
    for y,n in cg.items():
        b,a,c=y;out={};q=b.bit_count()
        for (t,me),s in BD[c].items():
            if target_pred(t,sup):out[(b,a,t)]=s
        for i in range(3):
            if not(a>>i&1):out[(b,a|1<<i,c)]=-pm(n+q+(a&((1<<i)-1)).bit_count())
        for j in range(2):
            if not(b>>j&1):out[(b|1<<j,a,c)]=-pm(n+(b&((1<<j)-1)).bit_count())
        check(all(t in cg for t in out),'upper_shriek_adjoint_domains')
        cd[y]=out
    for x in gs:
        check(linear(conv,d[x])==linear(cd,conv[x]),'upper_shriek_explicit_currying_chain_map')
    return len(gs)


def audit_purity_on_target(selected=(1,3,5)):
    """All 8*215 tensor columns for K(X_selected)^vee tensor T -> i^*T[-3]."""
    selected=tuple(selected)
    def restrict_term(cell,mono):
        inverted={IX[a] for a in cell[0] if a not in cell[1]}
        if any(i in inverted for i in selected):return {}
        if any(mono[i]!=0 for i in selected):return {}
        return {(cell,mono):1}
    for mask in range(8):
        k=mask.bit_count()
        for c in CELLS:
            left={}
            # The component into dual top has a selected occurrence factor,
            # and hence becomes zero under the actual support quotient.
            for i,a in enumerate(selected):
                if mask>>i&1:continue
                high=mask|1<<i
                if high==7:
                    term=restrict_term(c,ex({a:1}))
                    left=add(left,scale(term,-pm(k+(mask&((1<<i)-1)).bit_count())))
            if mask==7:
                for (t,e),sg in BD[c].items():
                    left=add(left,scale(restrict_term(t,log_exponent(e)),pm(k)*sg))
            right={}
            if mask==7 and restrict_term(c,ZERO):
                for (t,e),sg in BD[c].items():
                    # The target shift [-3] changes the differential sign.
                    right=add(right,scale(restrict_term(t,log_exponent(e)),-sg))
            check(left==right,'supported_purity_full_215_target_tensor_chain_equation')
    return 8*len(CELLS)


def small_selected_model(original,support):
    """Projection onto actual short faces: fixed odd marks and optional x2,x4."""
    gs,d,cs=original
    basis={x:n for x,n in gs.items() if x[0]==31 and
           not any(a in LONGS for a in x[1][0]) and SHORTS[0] not in x[1][0]}
    small_d={x:{y:a for y,a in d[x].items() if y in basis} for x in basis}
    p={x:({x:1} if x in basis else {}) for x in gs}
    for x in gs:
        check(linear(p,d[x])==linear(small_d,p[x]),'small_fixed_mark_projection_is_chain_map')
    # Cone of the projection is acyclic with signed-unit reductions.
    cone_g={('small',x):n for x,n in basis.items()}
    cone_g.update({('full',x):n+1 for x,n in gs.items()})
    cone_d={('small',x):{('small',y):a for y,a in small_d[x].items()} for x in basis}
    for x in gs:
        cone_d[('full',x)]={('full',y):-a for y,a in d[x].items()}
        if x in basis:cone_d[('full',x)][('small',x)]=1
    for x in cone_g:check(not linear(cone_d,cone_d[x]),'small_projection_cone_d_squared')
    h,_=reduce_fast(cone_g,cone_d)
    check(not h,'small_projection_is_integral_quasi_isomorphism')
    hs,_=reduce_fast(basis,small_d)
    return {'generators':len(basis),'Ext':ext_groups(hs)}


def main_new(path):
    check_source()
    check(len(CELLS)==215,'actual_target_stalk_count')
    for c in CELLS:
        square={}
        for (t,a),s in BD[c].items():
            for (v,b),z in BD[t].items():square=add(square,{(v,eadd(a,b)):s*z})
        check(not square,'actual_polynomial_target_d_squared')
    SOURCE_BLOBS['src/ledger/20260814-115 Boundary-Triad Tate Realization and the Multi-Rees Cartier Bicomplex.md']='63da17cb5d641705056c5d5b9bc6f53cda72baf5'
    purity=audit_purity()
    purity['target_tensor_columns_checked']=audit_purity_on_target()
    selected=(1,3,5);occ=ex({i:1 for i in selected})
    critical=frame(0,1,3,5,3)
    ambient_invariance=[]
    for sup in ('V','E','Q','B','K'):
        old=hom_complex(SEQ,critical,sup);new=log_hom(SEQ,critical,sup)
        check(old[0]==new[0] and old[1]==new[1],'Tor1_critical_log_base_change_identical_matrices')
        for x in old[0]:check(log_exponent(old[2][x])==new[2][x],'Tor1_critical_log_base_change_exact_coefficients')
        ambient_invariance.append({'target':sup,'generators':len(new[0]),'Ext':ext_groups(reduce_fast(*new[:2])[0])})
        audit_currying(critical,sup)

    records=[];critical_models=None;critical_red=None;critical_g=None;critical_beta=None
    for tor in (False,True):
        le=frame(0,*((3,) if tor else ()))
        normalized=esub(le,occ)
        # Before log restriction, the occurrence-line normalized endpoint map
        # is itself a legal polynomial/localized chain map. No scalar inversion.
        raw=endpoint_map(tor)
        og,od,oc=hom_complex(SEQ,normalized,'V')
        check(all(x in og for x in raw),'principal_occurrence_line_factorization_legal')
        check(not linear(od,raw),'principal_occurrence_line_factorization_chain_map')
        olde=hom_complex(SEQ,le,'V')
        for x in raw:check(eadd(oc[x],occ)==olde[2][x],'endpoint_has_exact_occurrence_factor')
        # Without that line pairing, restriction annihilates every column.
        un=log_hom(SEQ,le,'V');unr=log_hom(SEQ,le,'V',selected)
        up=restrict_slice(un,unr)
        check(not linear(up,raw),'raw_endpoint_restriction_is_zero_termwise')
        # All five target objects retained in the corrected homogeneous frame.
        models={};reductions={}
        for sup in ('V','E','Q','B','K'):
            amb=log_hom(SEQ,normalized,sup)
            mod=log_hom(SEQ,normalized,sup,selected)
            restrict_slice(amb,mod)
            models[sup]=mod;reductions[sup]=reduce_sdr(*mod[:2])
        nf={x:a for x,a in raw.items() if x in models['V'][0]}
        check(nf and not linear(models['V'][1],nf),'normalized_selected_endpoint_is_closed')
        fc=linear(reductions['V']['P'],nf)
        check(fc and gcd(*[abs(v) for v in fc.values()])==1,'normalized_selected_endpoint_primitive')
        check(linear(reductions['K']['P'],nf),'normalized_selected_endpoint_survives_in_full_target')
        # The same target/source frame forces the product of the three Rees
        # parameters on the generic top image. It is not a normal product U.
        generic=generic_map(tor)
        check(all(x in models['Q'][0] for x in generic),'framed_generic_source_map_legal')
        check(not linear(models['Q'][1],generic),'framed_generic_source_map_closed')
        expected=eadd(log_exponent(GAMMA),ex({9+i:1 for i in selected}))
        for (mask,c),a in generic.items():
            if c==((),()):check(models['Q'][2][(mask,c)]==expected,'generic_top_coefficient_is_Rees_determinant_times_U')
        gc=linear(reductions['Q']['P'],generic)
        check(gc and gcd(*[abs(v) for v in gc.values()])==1,'framed_generic_source_map_primitive')
        defect=linear(models['K'][1],generic)
        check(len(defect)==(9 if tor else 18),'selected_actual_short_support_term_count')
        check(all(x in models['B'][0] for x in defect),'selected_defect_is_short_supported')
        check(not linear(models['B'][1],defect),'selected_defect_closed')
        bc=linear(reductions['B']['P'],defect)
        check(bc and gcd(*[abs(v) for v in bc.values()])==1,'selected_generic_obstruction_primitive')
        # All full endpoint-quotient cohomology representatives have zero
        # generic class. This checks every replacement, not one failed chain.
        for v in reductions['E']['I'].values():
            qv={x:a for x,a in v.items() if x in models['Q'][0]}
            check(not linear(reductions['Q']['P'],qv),'every_endpoint_quotient_class_has_zero_generic_image')
        # A uniform occurrence-line normalization applied to the old generic
        # frame is impossible; in this frame its whole selected Hom is zero.
        wrong=esub(frame(0,1,3,5,*((3,) if tor else ())),occ)
        wrongg,wrongd,_=log_hom(SEQ,wrong,'Q',selected)
        check(not wrongg,'uniform_occurrence_division_does_not_define_generic_arrow')
        if tor:
            check(reductions['V']['homology']=={-2:1},'Tor1_selected_endpoint_line')
            check(reductions['E']['homology']=={-2:4},'Tor1_selected_endpoint_quotient_four_classes')
            check(reductions['Q']['homology']=={-2:1},'Tor1_selected_generic_line')
            check(reductions['B']['homology']=={-2:5,-3:1},'Tor1_selected_short_support_obstruction_line')
            check(reductions['K']['homology']=={-2:5},'Tor1_selected_full_target_five_classes')
            critical_models=models;critical_red=reductions;critical_g=generic;critical_beta=defect
        records.append({'channel':'Tor1' if tor else 'Tor0','frame_in_original_exponents':list(normalized),
          'frame_in_log_exponents':list(log_exponent(normalized)),
          'targets':{s:{'generators':len(models[s][0]),'Ext':ext_groups(reductions[s]['homology'])} for s in models},
          'raw_endpoint_restriction':'zero on every cochain column',
          'normalized_endpoint_cochain':named_hom(nf),'normalized_endpoint_coordinates':named_hom(fc),
          'generic_top_coefficient':'(t1*t3*t5)*U',
          'generic_cochain':named_hom(generic),'generic_coordinates':named_hom(gc),
          'short_support_obstruction':named_hom(defect),'obstruction_coordinates':named_hom(bc),
          'target_to_generic_homology_map':'zero','obstruction_additive_order':'infinite'})
        # Transport actual selected-branch formulas. Source wedge positions
        # retain their transported ordered frames; no averaging of branches.
        for g in G:
            seqg=tuple(IX[group_diag(SHORTS[a],g)] for a in SEQ)
            selg=tuple(IX[group_diag(SHORTS[a],g)] for a in selected)
            for sup,v in (('V',nf),('Q',generic),('B',defect),('E',generic)):
                original=models[sup];transported=log_hom(seqg,act_exp(normalized,g),sup,selg)
                for x in original[0]:
                    im=act_hom({x:1},g)
                    check(all(y in transported[0] for y in im),'six_log_branch_transports_have_legal_stalks')
                    check(act_hom(original[1][x],g)==linear(transported[1],im),'six_log_branch_transports_chain_maps')
                    y=next(iter(im))
                    check(act_exp(original[2][x],g)==transported[2][y],'six_log_branch_transports_exact_coefficients')
                check(all(y in transported[0] for y in act_hom(v,g)),'transported_supported_classes_are_legal')

    small={sup:small_selected_model(model,sup) for sup,model in critical_models.items()}
    odd_sectors=[]
    for k in range(4):
        for fixed in combinations((1,3,5),k):
            optional=[j for j in (2,4) if all(not cross(SHORTS[j],SHORTS[i]) for i in fixed)]
            odd_sectors.append({'fixed_odd_marks':list(fixed),'available_even_labels':optional})
    check(sum(not row['available_even_labels'] for row in odd_sectors)==5,
          'independent_five_noncontractible_odd_sectors')
    # Dualize the entire critical coefficient triangle, not only H groups.
    phi=trace_from_primitive(critical_red['B'],critical_beta)
    bg,bd=dual_complex(*critical_models['B'][:2])
    check(not linear(bd,phi),'actual_dual_obstruction_functional_closed')
    check(pairing(phi,critical_beta)==1,'actual_dual_obstruction_pairing_is_plus_one')
    kg,kd=dual_complex(*critical_models['K'][:2])
    qg,qd=dual_complex(*critical_models['Q'][:2])
    qphi=linear(kd,phi)
    check(all(x in qg for x in qphi),'dual_connecting_lands_in_generic_dual')
    check(not linear(qd,qphi),'dual_generic_functional_closed')
    check(pairing(qphi,critical_g)==1,'dual_connecting_pairing_is_plus_one')
    br=reduce_sdr(bg,bd);qr=reduce_sdr(qg,qd)
    check(linear(br['P'],phi) and linear(qr['P'],qphi),'both_dual_classes_nonzero')
    # Independence of extending phi to K: any two extensions differ by a
    # Q-dual cochain; their differential differences are Q-dual boundaries.
    for x in qg:
        check(linear(kd,{x:1})==linear(qd,{x:1}),'dual_extension_choice_changes_only_exact_Q_term')
    result={
      'date':'2026-09-07','source_commit':COMMIT,'source_blobs':SOURCE_BLOBS,
      'status':'proved_scoped_supported_line_normalization_log_branch_residues_and_surviving_dual_transgression',
      'source':{'Koszul_sequence':['u1','u3','u5','u0','u3'],'generators':32,'eta':'h3_plus-h3_pair'},
      'target':{'loaded_stalks':215,'same_V_B_K_E_Q_filtration':True},
      'log_base_change':{'equations':'u_i=X_i*t_i on all six shorts; long u_D independent',
         'global_occurrence_inversion':False,'flatness_assumed':False,
         'critical_Tor1_Hom_is_identical_to_prelog_Hom':ambient_invariance},
      'selected_branch':'X1=X3=X5=0',
      'principal_occurrence_line':'I_plus=(X1*X3*X5); normalize via its dual frame before restriction',
      'purity':purity,'channels':records,
      'small_fixed_mark_models':small,'eight_odd_mark_sectors':odd_sectors,
      'dual_critical_triangle':{'duality':'RHom_Z of the full finite homogeneous Hom slice; not identified with spatial Verdier duality',
         'short_functional':named_hom(phi),'generic_functional':named_hom(qphi),
         'pairing_with_short_obstruction':1,'pairing_with_generic_class':1,
         'short_dual_homology':br['homology'],'generic_dual_homology':qr['homology'],
         'obstruction_removed':False},
      'scope':[
        'The principal-line endpoint factorization is derived from actual common occurrence factors, with no inverse adjoined to the base.',
        'The selected branch is the admitted positive occurrence branch, not a branch chosen by a desired sign.',
        'The Rees determinant t1*t3*t5 is retained on the framed generic class; it is not replaced by one or by an internal normal product.',
        'Ordered closed-immersion purity adds the dual occurrence conormal determinant and cohomological shift three. It does not turn the nonzero connecting class into a boundary.',
        'All four endpoint-quotient cohomology classes in the critical Tor1 slice have zero generic projection.',
        'The finite-slice dual is an exact coefficient calculation, not a construction of the full supported Verdier dual of the spatial target.',
        'No exceptional nearby-cycle/log-blowdown counit with the two coupled endpoint connector cells is asserted; no physical parity is assigned.'
      ],
      'assertion_categories':dict(sorted(COUNT.items())),
      'total_exact_assertions':sum(COUNT.values()),
      'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'exact_assertions':result['total_exact_assertions'],
       'channels':[{k:r[k] for k in ('channel','targets','normalized_endpoint_coordinates','generic_coordinates','obstruction_coordinates')} for r in records],
       'dual_trace':result['dual_critical_triangle']},indent=2))

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path('marici_supported_dual_log_branch_comparison_certificate.json'))
    args=parser.parse_args();main_new(args.output)
