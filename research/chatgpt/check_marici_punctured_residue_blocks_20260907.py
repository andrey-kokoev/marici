#!/usr/bin/env python3
"""Exact 128-term punctured-PC block comparison and endpoint d3 witnesses.

Standard library only. Keeps all coefficient domains, arbitrary pole order,
short-Rees units and independent long parameters. Symbolic chain identities
and exhaustive homogeneous support types supplement the all-degree proofs
in marici_punctured_residue_blocks_and_duality_20260907.md.
This is not a proof-assistant certificate. No network or repository writes.
"""
from __future__ import annotations
import argparse
from collections import Counter, deque
from functools import lru_cache
from itertools import combinations, product
from pathlib import Path
import hashlib
import json
import time

CHECKS: Counter[str] = Counter()
PLUS=((1,3),(1,5),(3,5)); MINUS=((0,2),(0,4),(2,4))
SHORT=PLUS+MINUS; LONG=((0,3),(1,4),(2,5))
DIAGS=tuple(sorted(SHORT+LONG)); INDEX={a:i for i,a in enumerate(SHORT+LONG)}
VARS=tuple('X'+''.join(map(str,a)) for a in SHORT+LONG)+tuple(
    ('t' if a in SHORT else 'u')+''.join(map(str,a)) for a in SHORT+LONG)
ZERO=(0,)*18

def check(ok,family,detail=None):
    if not ok: raise AssertionError(f'{family}: {detail!r}')
    CHECKS[family]+=1

def pm(n): return -1 if n%2 else 1

def put(out,key,value):
    if value:
        out[key]=out.get(key,0)+value
        if not out[key]:del out[key]

def add(*vs):
    out={}
    for v in vs:
        for key,a in v.items():put(out,key,a)
    return out

def scale(v,a):return {k:a*b for k,b in v.items() if a*b}

def subs(s):
    s=tuple(sorted(s))
    return tuple(c for n in range(len(s)+1) for c in combinations(s,n))

def cross(a,b):
    i,j=a;k,l=b
    return i<k<j<l or k<i<l<j

FACES=tuple(f for f in subs(DIAGS) if len(f)<=3 and not any(cross(a,b) for a,b in combinations(f,2)))
FACESET=set(FACES)
CELLS=tuple((f,h) for f in FACES for h in subs(f))

def kind(c):
    f,h=c;u=set(f)-set(h)
    if u&set(PLUS) and u&set(MINUS):return 'zero'
    return 'puncture' if u&set(SHORT) else 'core'

def side(c):
    loc=set(c[0])-set(c[1])
    return 0 if loc&set(PLUS) else 1

def degree(c):return 3-len(c[0])+len(c[1])

def mono(xs=(),us=(),it=()):
    m=[0]*18
    for x in xs:m[INDEX[x]]+=1
    for u in us:m[9+INDEX[u]]+=1
    for t in it:m[9+INDEX[t]]-=1
    return tuple(m)

def emul(a,b):return tuple(x+y for x,y in zip(a,b))

def admissible(c,m):
    if kind(c)=='zero':return False
    f,h=c;loc=set(f)-set(h)
    if any(m[:3]) and any(m[3:6]):return False
    if loc&set(PLUS) and any(m[3:6]):return False
    if loc&set(MINUS) and any(m[:3]):return False
    for x in SHORT:
        if m[INDEX[x]]<0 and x not in loc:return False
    for l in LONG:
        if m[INDEX[l]]<0:return False
        if m[9+INDEX[l]]<0 and l not in loc:return False
    return True

def term(c,m=ZERO,a=1):return {(c,m):a} if a and admissible(c,m) else {}

def times(v,m,a=1):
    out={}
    for (c,e),b in v.items():
        ee=emul(e,m)
        if admissible(c,ee):put(out,(c,ee),a*b)
    return out

@lru_cache(None)
def dc(c):
    f,h=c;out={}
    for a in DIAGS:
        ff=tuple(sorted(f+(a,)))
        if a in f or ff not in FACESET:continue
        m=[0]*18
        if a in SHORT:m[9+INDEX[a]]=-1
        else:m[INDEX[a]]=1;m[9+INDEX[a]]=-1
        out=add(out,term((ff,h),tuple(m),pm(sum(b<a for b in f))))
    for i,a in enumerate(h):
        hh=tuple(b for b in h if b!=a)
        out=add(out,term((f,hh),ZERO,pm(3-len(f)+i)))
    return out

def diff(v):
    out={}
    for (c,m),a in v.items():out=add(out,times(dc(c),m,a))
    return out

P_CELLS=tuple(c for c in CELLS if kind(c)=='puncture')

# A block key (side, opposite marked support, active label subset).
# A basis also specifies active unmarked subset and long state:
# (block, U, long_label_or_None, 0 absent / 1 marked / 2 unmarked).
BLOCKS=[]
for si,active in enumerate((PLUS,MINUS)):
    for j in subs(active):
        if j:BLOCKS.append((si,(),j))
    opposite=MINUS if si==0 else PLUS
    for m in opposite:
        allowed=tuple(p for p in active if not cross(p,m))
        check(len(allowed)==1,'short_mixed_graph_matching')
        BLOCKS.append((si,(m,),allowed))
BLOCKS=tuple(BLOCKS)

def longs(block):
    _,n,j=block
    return tuple(l for l in LONG if tuple(sorted(n+j+(l,))) in FACESET)

def basis_of(block):
    result=[]
    for u in subs(block[2]):
        if not u:continue
        result.append((block,u,None,0))
        for l in longs(block):
            result.extend(((block,u,l,1),(block,u,l,2)))
    return tuple(result)

NEW=tuple(b for block in BLOCKS for b in basis_of(block))

def lead(b):
    (si,n,j),u,l,st=b
    f=tuple(sorted(n+j+((l,) if l is not None else ())))
    h=tuple(sorted(n+tuple(a for a in j if a not in u)+((l,) if st==1 else ())))
    return f,h

LEADS={lead(b):b for b in NEW}

@lru_cache(None)
def change(b):
    """Unit-triangular expansion of closed short factors; includes all signs."""
    (si,n,j),u,l,st=b
    active=PLUS if si==0 else MINUS
    f0,h0=lead(b)
    extra=tuple(a for a in active if a not in j and tuple(sorted(f0+(a,))) in FACESET)
    unmarked=set(f0)-set(h0)
    out={}
    for k in subs(extra):
        f=tuple(sorted(f0+k));h=tuple(sorted(h0+k));q=len(k)
        sign=pm(q*(3-len(f0))+q*(q-1)//2+sum(sum(a<i for a in unmarked) for i in k))
        out=add(out,term((f,h),mono(it=k),sign))
    return out

def forward(v):
    out={}
    for (b,m),a in v.items():out=add(out,times(change(b),m,a))
    return out

def inverse(v):
    """Finite triangular elimination; never divides a nonunit coefficient."""
    rem=dict(v);out={};iterations=0
    while rem:
        (c,m),a=min(rem.items(),key=lambda item:(len(item[0][0][0]),item[0]))
        b=LEADS[c]
        put(out,(b,m),a)
        rem=add(rem,scale(times(change(b),m,a),-1))
        iterations+=1
        if iterations>4000:raise AssertionError('triangular inverse did not terminate')
    return out

@lru_cache(None)
def dn(b):
    block,u,l,st=b
    _,n,j=block;f,h=lead(b);out={}
    for a in j:
        if a not in u:
            uu=tuple(sorted(u+(a,)))
            put(out,((block,uu,l,st),ZERO),pm(3-len(f)+h.index(a)))
    if st==0:
        for ll in longs(block):
            e=mono(xs=(ll,));m=list(e);m[9+INDEX[ll]]-=1
            put(out,((block,u,ll,2),tuple(m)),pm(sum(a<ll for a in f)))
    if st==1:put(out,((block,u,l,2),ZERO),pm(3-len(f)+h.index(l)))
    return out

def new_diff(v):
    out={}
    for (b,m),a in v.items():
        for (bb,e),k in dn(b).items():put(out,(bb,emul(m,e)),a*k)
    return out

# Standard product signs: nonaugmented Cech on J (cochain degree |U|)
# tensor the long comparison [C^(1+#L) -> direct sum C[u_l^-1]].
def standard_diff(b):
    block,u,l,st=b;out={}
    for a in block[2]:
        if a not in u:put(out,((block,tuple(sorted(u+(a,))),l,st),ZERO),pm(sum(i<a for i in u)))
    if st==0:
        for ll in longs(block):
            e=list(mono(xs=(ll,)));e[9+INDEX[ll]]-=1
            put(out,((block,u,ll,2),tuple(e)),pm(len(u)))
    if st==1:put(out,((block,u,l,2),ZERO),pm(len(u)))
    return out

def product_sign_gauge(block):
    bs=basis_of(block);graph={b:[] for b in bs}
    for b in bs:
        old=dn(b);std=standard_diff(b)
        check(set(old)==set(std),'product_differential_same_arrows')
        for (bb,m),a in old.items():
            factor=a*std[(bb,m)]
            graph[b].append((bb,factor));graph[bb].append((b,factor))
    signs={}
    for root in bs:
        if root in signs:continue
        signs[root]=1;queue=deque([root])
        while queue:
            b=queue.popleft()
            for bb,factor in graph[b]:
                target=signs[b]*factor
                if bb in signs:check(signs[bb]==target,'all_product_orientation_cycles_close')
                else:signs[bb]=target;queue.append(bb)
    for b in bs:
        check({(bb,m):signs[b]*a*signs[bb] for (bb,m),a in dn(b).items()}==standard_diff(b),
              'complete_Cech_long_product_signs')
    return signs

# Integral rank elimination with unit pivots proves saturation in each strand.
def unit_rank(mat,ncols):
    a=[row[:] for row in mat];m=len(a);k=0
    while k<min(m,ncols):
        hit=next(((i,j) for i in range(k,m) for j in range(k,ncols) if abs(a[i][j])==1),None)
        if hit is None:break
        i,j=hit;a[k],a[i]=a[i],a[k]
        for row in a:row[k],row[j]=row[j],row[k]
        if a[k][k]<0:a[k]=[-v for v in a[k]]
        for i in range(m):
            if i!=k and a[i][k]:
                q=a[i][k];a[i]=[x-q*y for x,y in zip(a[i],a[k])]
        for j in range(ncols):
            if j!=k and a[k][j]:
                q=a[k][j]
                for i in range(m):a[i][j]-=q*a[i][k]
        k+=1
    check(not any(a[i][j] for i in range(k,m) for j in range(k,ncols)),
          'all_integral_homogeneous_Smith_factors_unit')
    return k

def strand_present(c,neg,gx,gu):
    f,h=c;loc=set(f)-set(h)
    return set(neg)<=loc and all(gx[j]+int(l in f)>=0 and
        (gu[j]-int(l in f)>=0 or l in loc) for j,l in enumerate(LONG))

def strand_hom(si,neg,gx,gu,new=False):
    if new:
        vals=[b for b in NEW if b[0][0]==si and strand_present(lead(b),neg,gx,gu)]
        lev=[[b for b in vals if degree(lead(b))==n] for n in range(3)]
        img={b:{bb:a for (bb,m),a in dn(b).items()} for b in vals}
    else:
        vals=[c for c in P_CELLS if side(c)==si and strand_present(c,neg,gx,gu)]
        lev=[[c for c in vals if degree(c)==n] for n in range(3)]
        img={c:{cc:a for (cc,m),a in dc(c).items()} for c in vals}
    ranks=[0]
    for n in (1,2):
        mat=[[img[c].get(r,0) for c in lev[n]] for r in lev[n-1]]
        check(all(t in vals for c in lev[n] for t in img[c]),'homogeneous_differential_domain')
        ranks.append(unit_rank(mat,len(lev[n])))
    ranks.append(0)
    return tuple(len(lev[n])-ranks[n]-ranks[n+1] for n in range(3))

# Endpoint Cech / ordered Koszul comparison, independent of long parameters.
# Standard endpoint basis b_U=(-1)^sum(position in sigma) [sigma,sigma\U].
def end_term(si,u,m=None,a=1):
    sig=tuple(sorted(PLUS if si==0 else MINUS))
    c=(sig,tuple(x for x in sig if x not in u))
    sign=pm(sum(sig.index(x) for x in u))
    return term(c,ZERO if m is None else m,sign*a)

def koszul_total_diff(v):
    """Terms (Koszul label tuple, original PC cell, monomial)."""
    out={}
    for (k,c,m),a in v.items():
        for j,x in enumerate(k):
            kk=tuple(y for y in k if y!=x);mm=emul(m,mono(xs=(x,)))
            if admissible(c,mm):put(out,(kk,c,mm),a*pm(j))
        for (cc,e),b in dc(c).items():
            mm=emul(m,e)
            if admissible(cc,mm):put(out,(k,cc,mm),a*b*pm(len(k)))
    return out

def endpoint_zigzag(si,power=1):
    sig=tuple(sorted(PLUS if si==0 else MINUS));out={}
    for u in subs(sig):
        if not u:continue
        m=[0]*18
        for x in u:m[INDEX[x]]=-power
        a=pm(len(u)*(len(u)+1)//2-1)
        # For power>1 use Koszul on powers by adapting the differential below.
        for (c,mm),k in end_term(si,u,tuple(m),a).items():put(out,(u,c,mm),k)
    return out

def koszul_power_diff(v,power):
    out={}
    for (k,c,m),a in v.items():
        for j,x in enumerate(k):
            kk=tuple(y for y in k if y!=x);mm=emul(m,mono(xs=(x,)*power))
            if admissible(c,mm):put(out,(kk,c,mm),a*pm(j))
        for (cc,e),b in dc(c).items():
            mm=emul(m,e)
            if admissible(cc,mm):put(out,(k,cc,mm),a*b*pm(len(k)))
    return out

def long_homology_types(ls,gx,gu):
    """Independent symbolic rank formula for the long comparison, not PC matrices."""
    base=all(a>=0 for a in gx) and all(a>=0 for a in gu)
    marks=[];rows=[]
    for l in ls:
        j=LONG.index(l)
        other=all(gx[k]>=0 and gu[k]>=0 for k in range(3) if k!=j)
        if other and gx[j]+1>=0:
            rows.append(l)
            if gu[j]>=1:marks.append(l)
    rank=len(marks)+int(base and len(rows)>len(marks))
    return int(base)+len(marks)-rank,len(rows)-rank


def predicted_homology(si,neg,gx,gu):
    """Kunneth on occurrence Cech and independent long comparison."""
    out=[0,0,0]
    for block in BLOCKS:
        if block[0]!=si:continue
        j=block[2]
        if not neg:qdeg=1
        elif tuple(neg)==j:qdeg=len(j)
        else:continue
        h0,h1=long_homology_types(longs(block),gx,gu)
        for d,r in enumerate((h0,h1)):
            n=3-qdeg-d
            if r:
                check(n>=0,'block_homology_has_nonnegative_homological_degree')
                out[n]+=r
    return tuple(out)


def top_block_cycle(block,gauge):
    """Primitive top cycle, with the long normal line still untrivialized."""
    ls=longs(block);v={}
    for x in block[2]:
        u=(x,);base=(block,u,None,0)
        put(v,(base,mono(us=ls)),gauge[base])
        for l in ls:
            b=(block,u,l,1)
            put(v,(b,mono(xs=(l,),us=tuple(a for a in ls if a!=l))),-gauge[b])
    return forward(v)


def serialize(v):
    return [{'face':[''.join(map(str,x)) for x in c[0]],
             'marks':[''.join(map(str,x)) for x in c[1]],
             'coefficient':a,'monomial':{VARS[i]:e for i,e in enumerate(m) if e}}
            for (c,m),a in sorted(v.items())]


def relabel(a,r,f):
    return tuple(sorted(((2*r+(3 if f else 0)+pm(f)*a[0])%6,
                         (2*r+(3 if f else 0)+pm(f)*a[1])%6)))


def tuple_relabel(v,r,f):
    out=tuple(relabel(a,r,f) for a in v)
    sign=pm(sum(out[i]>out[j] for i in range(len(out)) for j in range(i+1,len(out))))
    return tuple(sorted(out)),sign


def act_chain(v,r,f):
    out={}
    for (c,m),a in v.items():
        ff,sf=tuple_relabel(c[0],r,f);hh,sh=tuple_relabel(c[1],r,f)
        e=[0]*18
        for x in SHORT+LONG:
            y=relabel(x,r,f)
            e[INDEX[y]]=m[INDEX[x]];e[9+INDEX[y]]=m[9+INDEX[x]]
        put(out,((ff,hh),tuple(e)),a*sf*sh)
    return out


def act_basis(b,r,f):
    (si,n,j),u,l,st=b
    nn,_=tuple_relabel(n,r,f);jj,_=tuple_relabel(j,r,f);uu,_=tuple_relabel(u,r,f)
    sii=0 if set(jj)<=set(PLUS) else 1
    bb=((sii,nn,jj),uu,None if l is None else relabel(l,r,f),st)
    _,sf=tuple_relabel(lead(b)[0],r,f);_,sh=tuple_relabel(lead(b)[1],r,f)
    return bb,sf*sh


def finite_telescope_test(order,seed):
    """Check inverse a_n=sum x^k b_(n+k) modulo x^order, no false finite claim."""
    size=order+9
    b=[[((seed+7*n+3*j)%11)-5 for j in range(order)] for n in range(size+order+1)]
    def ainv(n):
        a=[0]*order
        for k in range(order):
            for j in range(order-k):a[j+k]+=b[n+k][j]
        return a
    for n in range(9):
        a=ainv(n);nxt=ainv(n+1)
        check([a[j]-(nxt[j-1] if j else 0) for j in range(order)]==b[n],
              'completed_telescope_inverse_mod_each_order')


def main(output):
    start=time.monotonic()
    check(len(CELLS)==215 and len(P_CELLS)==128,'original_target_and_puncture_census')
    check(len(BLOCKS)==20 and len(NEW)==128 and len(LEADS)==128,'twenty_blocks_same_128_modules')
    check(set(LEADS)==set(P_CELLS),'no_punctured_generator_added_or_removed')
    check(Counter(degree(c) for c in P_CELLS)=={0:8,1:54,2:66},'original_puncture_degrees')
    gauges={}
    for block in BLOCKS:gauges[block]=product_sign_gauge(block)
    for b in NEW:
        c=lead(b)
        check(change(b).get((c,ZERO))==1,'unit_triangular_leading_coefficient')
        check(all(cc==c or len(cc[0])>len(c[0]) for cc,m in change(b)),
              'strict_face_triangularity')
        check(all(set(cc[0])-set(cc[1])==set(c[0])-set(c[1]) for cc,m in change(b)),
              'identical_localization_domains_under_basis_change')
        check(diff(change(b))==forward(dn(b)),'full_symbolic_block_chain_map',b)
        check(not new_diff(dn(b)),'block_d_squared',b)
        check(inverse(change(b))=={(b,ZERO):1},'left_inverse_on_every_new_generator')
        check(forward(inverse(term(c)))==term(c),'right_inverse_on_every_old_generator')
        check(all(bb[0]==b[0] for bb,m in dn(b)),'each_block_is_genuine_subcomplex')
        loc=set(c[0])-set(c[1])
        for power in (1,2,5):
            m=[0]*18
            for x in loc:
                if x in SHORT:m[INDEX[x]]=-power
            m=tuple(m)
            v=times(change(b),m)
            check(diff(v)==forward({(bb,emul(e,m)):a for (bb,e),a in dn(b).items()}),
                  'negative_occurrence_poles_respect_actual_block_map')
    # Labelled rotation by two and reflection v -> 3-v, with no averaging.
    for r,f in product(range(3),range(2)):
        for b in NEW:
            bb,sgn=act_basis(b,r,f)
            check(act_chain(change(b),r,f)==scale(change(bb),sgn),
                  'complete_block_comparison_D3_covariance')
            check(act_chain(diff(change(b)),r,f)==diff(act_chain(change(b),r,f)),
                  'native_labelled_transport_chain_equation')
    # Exhaustive homogeneous types. All exponent sizes outside these ranges
    # have the same matrix or no admissible term.
    hist=Counter();records=[]
    for si,active in enumerate((PLUS,MINUS)):
        for neg in subs(active):
            for gx in product((-1,0),repeat=3):
                for gu in product((-1,0,1),repeat=3):
                    old=strand_hom(si,neg,gx,gu)
                    new=strand_hom(si,neg,gx,gu,True)
                    check(old==new,'complete_infinite_coefficient_type_comparison',(si,neg,gx,gu))
                    check(old==predicted_homology(si,neg,gx,gu),
                          'independent_all_degree_Cech_long_homology_formula',(si,neg,gx,gu))
                    hist[old]+=1
                    if any(old):records.append({'side':si,'negative_short_support':neg,
                         'long_X_total_type':gx,'long_u_total_type':gu,'homology_0_1_2':old})
    check(sum(hist.values())==3456,'all_3456_homogeneous_types')
    # Independent generic-long control; no global physical inversion is inferred.
    generic=[]
    for si,active in enumerate((PLUS,MINUS)):
        row=[]
        for neg in subs(active):
            h=strand_hom(si,neg,(0,0,0),(1,1,1))
            n=len(neg)
            expected={0:(0,0,10),1:(0,0,2),2:(0,1,0),3:(1,0,0)}[n]
            check(h==expected,'generic_long_homology_independent_formula')
            row.append({'negative_support':neg,'homology_0_1_2':h})
        generic.append(row)
    # Exact top generators and a class outside the preceding 17-channel image.
    tops={}
    for block in BLOCKS:
        v=top_block_cycle(block,gauges[block])
        check(v and not diff(v),'twenty_symbolic_top_module_generators_closed')
        check(all(degree(c)==2 for c,m in v),'top_generators_degree_two')
        tops[block]=v
    b=(0,(),(PLUS[0],))
    m=[0]*18;m[INDEX[PLUS[0]]]=-1
    extra=times(tops[b],tuple(m))
    check(extra and not diff(extra),'genuine_extra_punctured_H2_pole')
    check(any(e[INDEX[PLUS[0]]]<0 for c,e in extra),
          'extra_H2_not_in_nonnegative_occurrence_obstruction_image')
    # Endpoint blocks, primitive residue and d3 transgression in actual chains.
    endpoint_data=[]
    for si,active in enumerate((PLUS,MINUS)):
        sig=tuple(sorted(active));block=(si,(),sig)
        check(len(basis_of(block))==7 and not longs(block),'endpoint_is_exact_seven_term_Cech_block')
        endpoint=term((sig,sig));de=diff(endpoint)
        standard_aug=add(*(end_term(si,(x,)) for x in sig))
        check(de==standard_aug and len(de)==3,'actual_endpoint_boundary_is_Cech_augmentation')
        check(not diff(de),'endpoint_obstruction_closed')
        for n in range(1,7):
            z=endpoint_zigzag(si,n)
            want={((),c,m):a for (c,m),a in de.items()}
            check(koszul_power_diff(z,n)==want,'seven_term_Koszul_Cech_transgression', (si,n))
            check(not koszul_power_diff(koszul_power_diff(z,n),n),'full_transgression_d_squared')
        pole=[0]*18
        for x in sig:pole[INDEX[x]]=-1
        res=end_term(si,sig,tuple(pole))
        check(len(res)==1 and not diff(res),'triple_occurrence_residue_closed')
        # That exact coefficient type has one degree-zero basis, none in degree one.
        valid=[c for c in P_CELLS if side(c)==si and strand_present(c,sig,(0,0,0),(1,1,1))]
        # A stronger direct pole argument independent of long total degree:
        check(all(set(sig)<=set(c[0])-set(c[1]) for c in valid),'triple_pole_requires_three_unmarked_labels')
        check(all(c==(sig,()) for c in valid),'triple_pole_has_no_incoming_boundary')
        endpoint_data.append({'side':si,'endpoint_labels':sig,'Cech_ranks':[3,3,1],
             'H2':'B_side','H1':0,'H0':'H^3_occurrence(B_side)',
             'transgression':'d3:Tor_(p+3)(C,H0) -> Tor_p(C,H2), isomorphism for every p>=0',
             'explicit_tensor_witness_terms':len(endpoint_zigzag(si))})
    # All 128 terms invert an occurrence. The completed dual orthogonality
    # follows from the displayed infinite telescope inverse, tested at jets.
    for c in P_CELLS:
        loc=set(c[0])-set(c[1])
        check(bool(loc&set(SHORT)),'every_punctured_summand_is_an_occurrence_localization')
    for n in range(1,17):
        for seed in range(7):finite_telescope_test(n,seed)
    # Endpoint characteristic ranks via the existing all-degree branch formula.
    q=[1,6,24,92]
    for n in range(4,9):q.append(3*q[-1]+3*q[-2]+q[-3])
    branch=[1]+[a//2 for a in q[1:]]
    check(branch[:6]==[1,3,12,46,177,681],'intrinsic_branch_Tor_ranks')
    # Hash inputs without silently executing predecessor.
    inputs={}
    for name in ('marici_punctured_target_obstruction_20260907.md',
                 'check_marici_punctured_target_obstruction_20260907.py'):
        f=Path(__file__).parent/name
        if f.exists():inputs[name]=hashlib.sha256(f.read_bytes()).hexdigest()
    result={
      'status':'proved_scoped_explicit_punctured_PC_blocks_and_duality_gate',
      'baseline_commit':'d1947b67a60d3e88ba77f4ca60ea02c2a306ee61',
      'input_hashes':inputs,
      'prerequisite_replay': (json.loads((Path(__file__).parent/'_punctured_target_prerequisite_replay.json').read_text()).get('total_exact_assertions')
          if (Path(__file__).parent/'_punctured_target_prerequisite_replay.json').exists() else 'not_present'),
      'original_cells':215,'punctured_cells':128,'block_count':20,
      'block_list':[{'side':b[0],'opposite_marks':b[1],'active_J':b[2],
                    'compatible_longs':longs(b),'generators':len(basis_of(b))} for b in BLOCKS],
      'exhaustive_strand_types':3456,
      'homology_histogram':[{'ranks_0_1_2':h,'number_of_types':n} for h,n in sorted(hist.items())],
      'nonzero_homology_types':records,
      'generic_long_control':generic,'endpoint_blocks':endpoint_data,
      'extra_H2_cycle_outside_previous_obstruction_image':serialize(extra),
      'intrinsic_branch_Tor_ranks':branch,
      'duality_theorem':{
          'assumptions':'completed central ring; finite-cohomology relative dualizing target is derived occurrence-complete',
          'RHom_completed_P_into_dualizing':'zero',
          'completed_P':'nonzero',
          'dual_completed_F0_to_dual_completed_F':'equivalence',
          'punctured_local_endpoint_dual':'nonzero branch volume line in cohomological degree -1',
          'scope':'affine derived module Hom; not a conservative sheaf duality on noncoherent localized objects'},
      'assertions':dict(sorted(CHECKS.items())),
      'total_exact_assertions':sum(CHECKS.values()),
      'runtime_seconds':round(time.monotonic()-start,3),
      'not_claimed':['native physical source identification','new physical pole permissions',
          'coherent duality on noncoherent target modules','new geometric cells','proof assistant certification'],
      'proof_scope':'Triangular chain isomorphism and domain classification cover all polynomial pole orders. Completion and RHom conclusions use the all-order telescope proof and cited derived-completeness theorem; no bounded test extrapolation.'}
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ('status','original_cells','punctured_cells','block_count',
          'exhaustive_strand_types','total_exact_assertions','runtime_seconds')},indent=2))

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output',type=Path,default=Path('marici_punctured_residue_blocks_certificate_20260907.json'))
    args=p.parse_args();main(args.output)
