#!/usr/bin/env python3
"""Exact audit of a separated-coefficient conductor-dilation test.

Standard library only.  Computes B[t] tensor_S^L R, where
R=S/(I_minus I_plus), S=A[x_1,...,x_6], and x_i maps to t*Y_i.
The target ring B inverts Y02 and Y35, not the source occurrences.
Retains the full occurrence complex, both edge endpoints, and two resolved
trace maps.  This is a derived-incidence test, NOT a physical Gysin theorem
or a claim that this nonflat incidence is the flat Rees deformation.
"""
from __future__ import annotations
import argparse
from collections import Counter
from hashlib import sha256
from itertools import combinations
import json
from pathlib import Path

NAMES=('Y02','Y04','Y24','Y13','Y15','Y35','t','beta','X03','X14','X25','t_plus')
NV=len(NAMES)
ZERO=(0,)*NV
TINDEX=6
NEG=(0,1,2)
POS=(3,4,5)
ZINDEX=5
COUNTS=Counter()
COMMIT='d1947b67a60d3e88ba77f4ca60ea02c2a306ee61'


def check(value, family, detail=''):
    if not value:
        raise AssertionError(f'{family}: {detail}')
    COUNTS[family]+=1


def put(v,key,c):
    if c:
        v[key]=v.get(key,0)+c
        if not v[key]:del v[key]


def add(v,w,sign=1):
    out=dict(v)
    for key,c in w.items():put(out,key,sign*c)
    return out


def mono(*names):
    q=[0]*NV
    for name in names:q[NAMES.index(name)]+=1
    return tuple(q)


def exponent(i,power=1):
    q=[0]*NV;q[i]=power
    return tuple(q)


def times(v,m,c=1):
    out={}
    for (i,p),a in v.items():put(out,(i,tuple(x+y for x,y in zip(p,m))),c*a)
    return out


def unit(i):return {(i,ZERO):1}


def apply(M,v):
    out={}
    for (j,m),c in v.items():
        for (i,p),a in M.get(j,{}).items():
            put(out,(i,tuple(x+y for x,y in zip(p,m))),a*c)
    return out


def compose(M,N):return {j:apply(M,v) for j,v in N.items()}


def ident(n):return {j:unit(j) for j in range(n)}


def equal(M,N):
    return all(M.get(j,{})==N.get(j,{}) for j in set(M)|set(N))


def term(row,m=ZERO,c=1):return {(row,m):c} if c else {}


def rowpoly(col,i):return {m:c for (r,m),c in col.items() if r==i}


def sublists(items,empty=False):
    return [x for n in range(0 if empty else 1,len(items)+1)
            for x in combinations(items,n)]


PSTATES=[((),())]+[(a,b) for a in sublists(NEG) for b in sublists(POS)]
PSTATES.sort(key=lambda v:(0 if v==((),()) else len(v[0])+len(v[1])-1,v))
PID={x:i for i,x in enumerate(PSTATES)}
PDEG=[0 if v==((),()) else len(v[0])+len(v[1])-1 for v in PSTATES]
QSTATES=sublists(tuple(range(6)),True)
QID={x:i for i,x in enumerate(QSTATES)}
QDEG=[len(x)+2 for x in QSTATES]
OSTATES=[(p,k) for p in range(50) for k in (0,1)]
OID={x:i for i,x in enumerate(OSTATES)}
ODEG=[PDEG[p]+k+3 for p,k in OSTATES]


def coefficient(i,dilated):
    p=list(exponent(i));p[TINDEX]+=int(dilated)
    return tuple(p)


def product(*mm):return tuple(sum(v) for v in zip(*mm))


def resolution(coeffs):
    """S-free resolution of S/(I_minus I_plus), augmented by S in degree 0."""
    d={j:{} for j in range(50)}
    for j,(a,b) in enumerate(PSTATES):
        if PDEG[j]==1:
            if coeffs[a[0]] is not None and coeffs[b[0]] is not None:
                put(d[j],(0,product(coeffs[a[0]],coeffs[b[0]])),1)
        elif PDEG[j]>1:
            if len(a)>1:
                for k,i in enumerate(a):
                    if coeffs[i] is not None:
                        put(d[j],(PID[a[:k]+a[k+1:],b],coeffs[i]),(-1)**k)
            if len(b)>1:
                for k,i in enumerate(b):
                    if coeffs[i] is not None:
                        put(d[j],(PID[a,b[:k]+b[k+1:]],coeffs[i]),(-1)**(len(a)-1+k))
    return d


def koszul_source(coeffs):
    d={j:{} for j in range(64)}
    for j,w in enumerate(QSTATES):
        for k,i in enumerate(w):
            if coeffs[i] is not None:
                put(d[j],(QID[w[:k]+w[k+1:]],coeffs[i]),(-1)**k)
    return d


def occurrence_target(dp,z):
    """P_R tensor K(z)[3]; its occurrence differential is -z."""
    d={j:{} for j in range(100)}
    for j,(p,k) in enumerate(OSTATES):
        for (pp,m),c in dp[p].items():put(d[j],(OID[pp,k],m),c)
        if k:put(d[j],(OID[p,0],z),(-1)**(PDEG[p]+1))
    return d


def trace_maps(coeffs):
    """S-projective lifts of the two already recorded R-linear trace maps.

    Source is K_S(six occurrences)[2].  Compose with augmentation P_R -> R
    to recover epsilon_E and epsilon_R on generator/second-relation columns.
    """
    E={j:{} for j in range(64)};R={j:{} for j in range(64)}
    for j,w in enumerate(QSTATES):
        a=tuple(i for i in w if i<3);b=tuple(i for i in w if i>=3)
        if len(w)==1 and b:
            put(E[j],(OID[0,0],coeffs[b[0]]),1)
            if b[0]!=ZINDEX:put(R[j],(OID[0,0],coeffs[b[0]]),1)
        if a and b:
            put(E[j],(OID[PID[a,b],0],ZERO),(-1)**(len(b)-1))
            if ZINDEX not in b:
                put(R[j],(OID[PID[a,b],0],ZERO),(-1)**(len(b)-1))
            elif len(b)>1:
                put(R[j],(OID[PID[a,b[:-1]],1],ZERO),(-1)**(len(b)-2))
        elif not a and len(b)==2 and b[-1]==ZINDEX:
            put(R[j],(OID[0,1],coeffs[b[0]]),1)
    return E,R


def audit_complex(d,degrees,name):
    for j,v in d.items():
        check(not apply(d,v),name+'_square_zero',j)
        check(all(degrees[i]==degrees[j]-1 for i,p in v),name+'_degree',j)


def audit_map(F,ds,dt,deg_s,deg_t,name):
    for j,v in F.items():
        check(apply(dt,v)==apply(F,ds[j]),name+'_chain',j)
        check(all(deg_t[i]==deg_s[j] for i,p in v),name+'_degree',j)


def exterior(B,basis):
    ind={w:j for j,w in enumerate(basis)}
    out={j:{} for j in range(len(basis))}
    for j,w in enumerate(basis):
        v={((),ZERO):1}
        for k in w:
            new={}
            for (old,m),c in v.items():
                for (i,p),a in B[k].items():
                    if i not in old:
                        sign=(-1)**sum(i0>i for i0 in old)
                        put(new,(tuple(sorted(old+(i,))),product(m,p)),c*a*sign)
            v=new
        for (key,m),c in v.items():put(out[j],(ind[key],m),c)
    return out


def bases():
    """Independent target-unit frames; only Y02 and Y35 are inverted."""
    B={j:{} for j in range(6)};BI={j:{} for j in range(6)}
    put(B[0],(0,exponent(0,-1)),1)
    for j in (1,2):
        put(B[j],(j,ZERO),1)
        put(B[j],(0,product(exponent(j),exponent(0,-1))),-1)
    put(B[3],(5,exponent(5,-1)),1)
    for j,i in ((4,3),(5,4)):
        put(B[j],(i,ZERO),1)
        put(B[j],(5,product(exponent(i),exponent(5,-1))),-1)
    for i in (0,1,2):put(BI[i],(0,exponent(i)),1)
    put(BI[1],(1,ZERO),1);put(BI[2],(2,ZERO),1)
    for i in (3,4,5):put(BI[i],(3,exponent(i)),1)
    put(BI[3],(4,ZERO),1);put(BI[4],(5,ZERO),1)
    check(equal(compose(B,BI),ident(6)),'native_basis_inverse')
    BQ=exterior(B,QSTATES);BIQ=exterior(BI,QSTATES)
    def makep(B):
        en=exterior(B,[()]+sublists(NEG));ep=exterior(B,[()]+sublists(POS))
        nl=[()]+sublists(NEG);pl=[()]+sublists(POS)
        ni={w:i for i,w in enumerate(nl)};pj={w:j for j,w in enumerate(pl)}
        out={j:{} for j in range(50)};out[0]=unit(0)
        for j,(a,b) in enumerate(PSTATES[1:],1):
            for (i,m),c in en[ni[a]].items():
                for (k,p),r in ep[pj[b]].items():
                    put(out[j],(PID[nl[i],pl[k]],product(m,p)),c*r)
        return out
    BP=makep(B);BIP=makep(BI)
    def makeo(BP,kpower):
        out={j:{} for j in range(100)}
        for j,(p,k) in enumerate(OSTATES):
            for (i,m),c in BP[p].items():
                put(out[j],(OID[i,k],product(m,exponent(5,kpower*k))),c)
        return out
    BO=makeo(BP,-1);BIO=makeo(BIP,1)
    for M,MI,n in ((BQ,BIQ,64),(BP,BIP,50),(BO,BIO,100)):
        check(equal(compose(M,MI),ident(n)),'exterior_basis_inverse',n)
        check(equal(compose(MI,M),ident(n)),'exterior_inverse_basis',n)
    return BP,BIP,BQ,BIQ,BO,BIO


def split(d0,degrees):
    """Unimodular block diagonalization. No t-power is made invertible.

    Monomial division occurs only where a displayed coefficient is exactly
    divisible by the pivot; all resulting basis operations are polynomial.
    Nonunit t and t^2 blocks are RETAINED, not contracted.
    """
    n=len(degrees);d={j:dict(d0[j]) for j in range(n)}
    B=ident(n);BI=ident(n);active=set(range(n));pairs=[];operations=[]
    def shear(src,dst,m,c):
        check(m[TINDEX]>=0 and all(v==0 for k,v in enumerate(m) if k!=TINDEX),
              'unimodular_polynomial_shear')
        d[dst]=add(d[dst],times(d[src],m,c))
        for col in range(n):
            rr=rowpoly(d[col],dst)
            for p,a in rr.items():put(d[col],(src,product(p,m)),-c*a)
        B[dst]=add(B[dst],times(B[src],m,c))
        for col in range(n):
            rr=rowpoly(BI[col],dst)
            for p,a in rr.items():put(BI[col],(src,product(p,m)),-c*a)
        operations.append(['shear',src,dst,list(m),c])
    while True:
        vals=[]
        for j in sorted(active):
            for (i,m),c in d[j].items():
                if i in active:
                    check(abs(c)==1 and all(v==0 for k,v in enumerate(m) if k!=TINDEX),
                          'normal_form_monomial_entry',(j,i,m,c))
                    vals.append((m[TINDEX],j,i,c))
        if not vals:break
        power,j,i,c=min(vals)
        if c<0:
            d[j]={key:-v for key,v in d[j].items()}
            for col in range(n):
                for m,a in list(rowpoly(d[col],j).items()):put(d[col],(j,m),-2*a)
            B[j]={key:-v for key,v in B[j].items()}
            for col in range(n):
                for m,a in list(rowpoly(BI[col],j).items()):put(BI[col],(j,m),-2*a)
            operations.append(['sign',j])
        pivot=exponent(TINDEX,power)
        for jj in sorted(active):
            if jj==j:continue
            rr=rowpoly(d[jj],i)
            if rr:
                check(len(rr)==1 and degrees[jj]==degrees[j],'isolating_column_shape')
                m,a=next(iter(rr.items()))
                ratio=tuple(x-y for x,y in zip(m,pivot))
                shear(j,jj,ratio,-a)
        for ii in sorted(active):
            if ii==i:continue
            rr=rowpoly(d[j],ii)
            if rr:
                check(len(rr)==1 and degrees[ii]==degrees[i],'isolating_row_shape')
                m,a=next(iter(rr.items()))
                ratio=tuple(x-y for x,y in zip(m,pivot))
                shear(ii,i,ratio,a)
        check(d[j]==term(i,pivot),'isolated_differential_column')
        check(all(not rowpoly(d[k],i) for k in range(n) if k!=j),'isolated_differential_row')
        check(not d[i] and all(not rowpoly(d[k],j) for k in range(n)),'isolated_adjacent_maps')
        pairs.append((i,j,power));active.remove(i);active.remove(j)
    check(equal(compose(BI,B),ident(n)),'normal_form_inverse',n)
    check(equal(compose(B,BI),ident(n)),'normal_form_inverse_reverse',n)
    check(equal(compose(d0,B),compose(B,d)),'normal_form_differential',n)
    check(not active,'normal_form_no_isolated_free_states',n)
    return d,B,BI,pairs,operations


def interval(dp,z):
    pe=('p03','p25','g','h03','h25');pg=(0,0,1,1,1)
    states=[(p,j,k) for p in range(50) for j in range(5) for k in (0,1)]
    ids={v:i for i,v in enumerate(states)}
    deg=[PDEG[p]+pg[j]+k+2 for p,j,k in states]
    end={i for i,(_,j,_) in enumerate(states) if j!=2}
    d={i:{} for i in range(500)}
    dx=mono('X03');dv=mono('X25');dbx=mono('beta','X03');dbv=mono('beta','X25')
    dpe={0:{},1:{},2:{(0,dx):1,(1,dv):1},3:{(0,dbx):1},4:{(1,dbv):1}}
    for col,(p,j,k) in enumerate(states):
        for (pp,m),c in dp[p].items():put(d[col],(ids[pp,j,k],m),c)
        for (jj,m),c in dpe[j].items():put(d[col],(ids[p,jj,k],m),c*(-1)**PDEG[p])
        if k:put(d[col],(ids[p,j,0],z),(-1)**(PDEG[p]+pg[j]))
    quotient={j:{} for j in range(500)};lift={j:{} for j in range(100)}
    for j,(p,k) in enumerate(OSTATES):
        g=ids[p,2,k];quotient[g]=unit(j);lift[j]=unit(g)
    de=occurrence_target(dp,z)
    defect={j:add(apply(d,lift[j]),apply(lift,de[j]),-1) for j in range(100)}
    audit_complex(d,deg,'full_two_endpoint_interval')
    audit_map(quotient,d,de,deg,ODEG,'two_endpoint_quotient')
    for j,(p,k) in enumerate(OSTATES):
        expected=add(term(ids[p,0,k],dx,(-1)**PDEG[p]),term(ids[p,1,k],dv,(-1)**PDEG[p]))
        check(defect[j]==expected,'both_endpoint_connectors',j)
        check(all(i in end for i,m in defect[j]),'connecting_support',j)
        check(not add(apply(d,defect[j]),apply(defect,de[j])), 'connecting_closed',j)
    return states,deg,d,quotient,lift,defect


def export_matrix(M):
    return [[j,i,list(p),c] for j in sorted(M) for (i,p),c in sorted(M[j].items())]


def coefficient_detector(F,negative,positive):
    source=QID[(negative,positive)]
    target=OID[PID[((negative,),(positive,))],0]
    return {p:c for (i,p),c in F[source].items() if i==target and p[TINDEX]==0}




def full_trace_lifts(source_d,occurrence_d,fe,fr,interval_data):
    states,degrees,d,quotient,lift,defect=interval_data
    ids={v:i for i,v in enumerate(states)}
    normal={j:{} for j in range(100)}
    for j,(p,k) in enumerate(OSTATES):
        normal[j]=add(unit(ids[p,3,k]),unit(ids[p,4,k]))
    output={}
    for name,F in (('E',fe),('R',fr)):
        tilde=compose(lift,F);B=compose(normal,F)
        nu={j:add(B[j],times(tilde[j],mono('beta')),-1) for j in range(64)}
        a={j:add(apply(d,tilde[j]),apply(tilde,source_d[j]),-1) for j in range(64)}
        audit_map(nu,source_d,d,QDEG,degrees,'full_dilated_trace_'+name)
        check(equal(compose(quotient,nu),{j:times(F[j],mono('beta'),-1) for j in range(64)}),
              'full_trace_relative_projection',name)
        for j in range(64):
            check(add(apply(d,B[j]),apply(B,source_d[j]),-1)==times(a[j],mono('beta')),
                  'full_endpoint_trace_homotopy',(name,j))
            check(all(states[i][1]!=2 for i,m in a[j]),'trace_defect_both_endpoints',(name,j))
            check(a[j]==apply(defect,F[j]),'trace_connecting_naturality',(name,j))
        output[name]={'full_trace':export_matrix(nu),'graded_relative_lift':export_matrix(tilde),
                      'endpoint_correction':export_matrix(B),'endpoint_defect':export_matrix(a)}
    return output

def two_parameter_coefficients():
    return [product(exponent(i),exponent(TINDEX if i in NEG else 11)) for i in range(6)]


def two_parameter_blocks(dp):
    """Direct block decomposition after normalizing one row on each sheet.

    Truncated K(t,0,0) = R + K(t)^2 + K(t)[1].  Tensor the two
    truncations, retain their product augmentation, and record all blocks.
    """
    def label(sub,offset):
        w=tuple(i-offset for i in sub)
        table={(0,):(0,0,0),(1,):(1,0,0),(0,1):(1,0,1),
               (2,):(2,0,0),(0,2):(2,0,1),
               (1,2):(3,1,0),(0,1,2):(3,1,1)}
        return table[w]
    groups={}
    for j,(a,b) in enumerate(PSTATES[1:],1):
        ln=label(a,0);lp=label(b,3)
        groups.setdefault((ln[0],lp[0]),[]).append((j,ln,lp))
    blocks=[]
    for key,entries in sorted(groups.items()):
        ids={j for j,_,_ in entries}
        if key==(0,0):
            ids.add(0);kind='product';bottom=0
            j=entries[0][0]
            check(dp[j]==term(0,product(exponent(TINDEX),exponent(11))), 'two_parameter_product_block')
        elif 0 in key:
            kind='minus' if key[1]==0 else 'plus'
            bottom=min(PDEG[j] for j,_,_ in entries)
            lo=next(j for j,_,_ in entries if PDEG[j]==bottom)
            hi=next(j for j,_,_ in entries if PDEG[j]==bottom+1)
            check(dp[hi]==term(lo,exponent(TINDEX if kind=='minus' else 11)),
                  'two_parameter_single_block',key)
        else:
            kind='pair';bn=entries[0][1][1];bp=entries[0][2][1];bottom=bn+bp+1
            ix={(ln[2],lp[2]):j for j,ln,lp in entries}
            sgn=(-1)**bn
            b=ix[0,0];m=ix[1,0];p=ix[0,1];top=ix[1,1]
            check(dp[m]==term(b,exponent(TINDEX)), 'two_parameter_pair_minus',key)
            check(dp[p]==term(b,exponent(11),sgn), 'two_parameter_pair_plus',key)
            check(dp[top]==add(term(p,exponent(TINDEX)),term(m,exponent(11),-sgn)),
                  'two_parameter_pair_top',key)
        for j in ids:
            check(all(i in ids for i,m in dp[j]),'two_parameter_direct_summand',key)
        blocks.append({'kind':kind,'bottom_degree':bottom,'indices':sorted(ids)})
    summary=Counter((b['kind'],b['bottom_degree']) for b in blocks)
    check(dict(summary)=={('product',0):1,('minus',1):2,('minus',2):1,
                          ('plus',1):2,('plus',2):1,('pair',1):4,('pair',2):4,('pair',3):1},
          'two_parameter_complete_block_profile')
    return blocks


def source_parameter_homotopy(pivot):
    """Exterior multiplication by e_pivot/Y_pivot on K(x_i)[2]."""
    H={j:{} for j in range(64)}
    for j,w in enumerate(QSTATES):
        if pivot not in w:
            out=tuple(sorted(w+(pivot,)))
            put(H[j],(QID[out],exponent(pivot,-1)),(-1)**sum(i<pivot for i in w))
    return H


def two_parameter_audit():
    coeffs=two_parameter_coefficients()
    dp=resolution(coeffs);dq=koszul_source(coeffs);do=occurrence_target(dp,coeffs[5])
    fe,fr=trace_maps(coeffs)
    for d,deg,name in ((dp,PDEG,'two_parameter_kernel'),(dq,QDEG,'two_parameter_source'),
                       (do,ODEG,'two_parameter_occurrence')):
        audit_complex(d,deg,name)
    for f,name in ((fe,'two_parameter_trace_E'),(fr,'two_parameter_trace_R')):
        audit_map(f,dq,do,QDEG,ODEG,name)
    BP,BIP,BQ,BIQ,BO,BIO=bases()
    nc=[exponent(TINDEX),None,None,exponent(11),None,None]
    normal=resolution(nc)
    check(equal(compose(dp,BP),compose(BP,normal)),'two_parameter_unit_frame')
    blocks=two_parameter_blocks(normal)
    # Each of the two independent scale coordinates annihilates both trace
    # classes. The homotopies come from the free SOURCE, not coefficient
    # cancellation in its homology.
    homotopies={}
    for pivot,var in ((0,TINDEX),(5,11)):
        H=source_parameter_homotopy(pivot)
        for j in range(64):
            check(add(apply(dq,H[j]),apply(H,dq[j]))==term(j,exponent(var)),
                  'source_scale_homotopy',(pivot,j))
        for f,label in ((fe,'E'),(fr,'R')):
            HF=compose(f,H)
            for j in range(64):
                check(add(apply(do,HF[j]),apply(HF,dq[j]))==times(f[j],exponent(var)),
                      'two_parameter_trace_annihilation',(pivot,label,j))
            homotopies[f'{label}_{NAMES[var]}']=HF
    def det(F,j):
        raw=coefficient_detector(F,0,j)
        return {m:c for m,c in raw.items() if m[11]==0}
    check([[det(f,j) for f in (fe,fr)] for j in (5,3)]==
          [[{ZERO:1},{}],[{ZERO:1},{ZERO:1}]],'two_parameter_trace_detector_matrix')
    for d in (dq,do):
        check(all(m[TINDEX]>0 or m[11]>0 for col in d.values() for i,m in col),
              'two_parameter_every_hom_boundary_in_scale_ideal')
    interval_data=interval(dp,coeffs[5])
    ts,td,dt,q,l,kappa=interval_data
    full_traces=full_trace_lifts(dq,do,fe,fr,interval_data)
    check(product(coeffs[0],coeffs[5],exponent(0,-1),exponent(5,-1))==
          product(exponent(TINDEX),exponent(11)),'independent_scale_product_relation')
    return {'block_decomposition':blocks,
            'full_trace_lifts':full_traces,
            'trace_submodule':'(B[t_minus,t_plus]/(t_minus,t_plus))^2',
            'trace_detector_matrix':[[1,0],[1,1]],
            'matrices':{'kernel_d':export_matrix(dp),'source_d':export_matrix(dq),
                        'occurrence_d':export_matrix(do),'trace_E':export_matrix(fe),'trace_R':export_matrix(fr),
                        'interval_d':export_matrix(dt),'endpoint_quotient':export_matrix(q),
                        'both_endpoint_connector':export_matrix(kappa),'unit_normalized_kernel_d':export_matrix(normal)},
            'trace_parameter_homotopies':{name:export_matrix(H) for name,H in homotopies.items()},
            't_minus_variable':'t','t_plus_variable':'t_plus'}

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,default=Path('branch_a_separated_coefficients_derived_dilation_certificate.json'))
    args=parser.parse_args()
    check(Counter(PDEG)=={0:1,1:9,2:18,3:15,4:6,5:1},'polynomial_resolution_ranks')
    xs=[coefficient(i,False) for i in range(6)]
    dp0=resolution(xs);dq0=koszul_source(xs);do0=occurrence_target(dp0,xs[5])
    audit_complex(dp0,PDEG,'universal_polynomial_resolution')
    audit_complex(dq0,QDEG,'universal_conductor_koszul')
    audit_complex(do0,ODEG,'universal_occurrence_resolution')
    fe0,fr0=trace_maps(xs)
    audit_map(fe0,dq0,do0,QDEG,ODEG,'universal_trace_E')
    audit_map(fr0,dq0,do0,QDEG,ODEG,'universal_trace_R')
    # Exact augmentation to the previously supplied R-linear maps.
    for j,w in enumerate(QSTATES):
        E={k:c for (i,m),c in fe0[j].items() if OSTATES[i][0]==0 for k in [(OSTATES[i][1],m)]}
        R={k:c for (i,m),c in fr0[j].items() if OSTATES[i][0]==0 for k in [(OSTATES[i][1],m)]}
        expectedE={};expectedR={}
        if len(w)==1 and w[0] in POS:
            expectedE={(0,xs[w[0]]):1}
            if w[0]!=5:expectedR=dict(expectedE)
        if len(w)==2 and all(i in POS for i in w) and w[-1]==5:
            expectedR={(1,xs[w[0]]):1}
        check(E==expectedE,'original_epsilon_E_augmentation',j)
        check(R==expectedR,'original_epsilon_R_augmentation',j)
    dil=[coefficient(i,True) for i in range(6)]
    dp=resolution(dil);dq=koszul_source(dil);do=occurrence_target(dp,dil[5])
    fe,fr=trace_maps(dil)
    for d,deg,name in ((dp,PDEG,'derived_dilation_kernel'),(dq,QDEG,'derived_conductor_source'),(do,ODEG,'derived_occurrence_target')):
        audit_complex(d,deg,name)
    audit_map(fe,dq,do,QDEG,ODEG,'dilated_trace_E')
    audit_map(fr,dq,do,QDEG,ODEG,'dilated_trace_R')
    BP,BIP,BQ,BIQ,BO,BIO=bases()
    nc=[exponent(TINDEX),None,None,exponent(TINDEX),None,None]
    dpn=resolution(nc);dqn=koszul_source(nc);don=occurrence_target(dpn,exponent(TINDEX))
    for old,B,new,n in ((dp,BP,dpn,50),(dq,BQ,dqn,64),(do,BO,don,100)):
        check(equal(compose(old,B),compose(B,new)),'unit_frame_chain_isomorphism',n)
    nfp,bp,ibp,pp,op=split(dpn,PDEG)
    nfq,bq,ibq,qp,oq=split(dqn,QDEG)
    nfo,bo,ibo,oo,oo_ops=split(don,ODEG)
    def profile(pairs,deg):return sorted([list(key)+[value] for key,value in Counter((deg[i],power) for i,j,power in pairs).items()])
    pprof=profile(pp,PDEG);qprof=profile(qp,QDEG);oprof=profile(oo,ODEG)
    check(pprof==[[0,2,1],[1,1,8],[2,1,10],[3,1,5],[4,1,1]],'kernel_exact_homology_profile')
    check(qprof==[[2,1,1],[3,1,5],[4,1,10],[5,1,10],[6,1,5],[7,1,1]],'conductor_exact_homology_profile')
    check(oprof==[[3,1,1],[4,1,9],[5,1,18],[6,1,15],[7,1,6],[8,1,1]],'occurrence_exact_homology_profile')
    # t is nullhomotopic on the full derived occurrence target.
    hblock={j:{} for j in range(100)}
    for i,j,power in oo:
        check(power==1,'occurrence_blocks_are_t')
        hblock[i]=unit(j)
    totalB=compose(BO,bo);totalBI=compose(ibo,BIO)
    h=compose(totalB,compose(hblock,totalBI))
    for j in range(100):
        lhs=add(apply(do,h[j]),apply(h,do[j]))
        check(lhs==term(j,exponent(TINDEX)),'occurrence_t_homotopy',j)
    homotopies=[]
    for label,F in (('E',fe),('R',fr)):
        HF=compose(h,F);homotopies.append(HF)
        for j in range(64):
            lhs=add(apply(do,HF[j]),apply(HF,dq[j]))
            check(lhs==times(F[j],exponent(TINDEX)),'trace_t_annihilation_'+label,j)
    # All differentials vanish modulo t, so each coefficient functional below
    # vanishes on EVERY Hom boundary, with no coefficient-degree cutoff.
    for d in (dq,do):
        check(all(m[TINDEX]>0 for col in d.values() for i,m in col),'all_hom_boundaries_zero_mod_t')
    detectors=[[coefficient_detector(F,0,j) for F in (fe,fr)] for j in (5,3)]
    check(detectors==[[{ZERO:1},{}],[{ZERO:1},{ZERO:1}]],'two_trace_unit_detector_matrix')
    # Verify the universal coefficient proof against every elementary Hom
    # homotopy basis. Any polynomial multiple then follows by linearity.
    for j,source_degree in enumerate(QDEG):
        for i,target_degree in enumerate(ODEG):
            if target_degree!=source_degree+1:continue
            H={jj:{} for jj in range(64)};H[j]=unit(i)
            boundary={jj:add(apply(do,H[jj]),apply(H,dq[jj])) for jj in range(64)}
            check(not coefficient_detector(boundary,0,5),'detector_E_all_homotopies',(j,i))
            check(not coefficient_detector(boundary,0,3),'detector_R_all_homotopies',(j,i))
    interval_data=interval(dp,dil[5])
    ts,td,dt,q,l,kappa=interval_data
    full_traces=full_trace_lifts(dq,do,fe,fr,interval_data)
    # Negative control: a literal coefficient substitution keeps only the
    # t^2=0 module and misses all four higher Tor degrees.
    check(sum(v for _,_,v in pprof[1:])==24,'higher_tor_not_discarded')
    # Exact saturation witness on the chosen independent-target open:
    # (t*Y02)(t*Y35)/(Y02*Y35) = t^2.
    check(product(dil[0],dil[5],exponent(0,-1),exponent(5,-1))==exponent(TINDEX,2),
          'saturation_witness_t_squared')
    # No inverse t, beta, long or source coefficient is used in any matrix.
    mats=[BP,BIP,BQ,BIQ,BO,BIO,bp,ibp,bq,ibq,bo,ibo,h,fe,fr,dt]
    for M in mats:
        for col in M.values():
            for i,m in col:
                check(all(a>=0 for k,a in enumerate(m) if k not in (0,5)),
                      'only_independent_target_units_inverted')
    two_parameter=two_parameter_audit()
    def diagonal_matrix(rows):
        M={}
        for j,i,mm,c in rows:
            m=list(mm);m[TINDEX]+=m[11];m[11]=0
            put(M.setdefault(j,{}),(i,tuple(m)),c)
        return M
    for name,M in (('kernel_d',dp),('source_d',dq),('occurrence_d',do),
                   ('trace_E',fe),('trace_R',fr),('interval_d',dt),
                   ('endpoint_quotient',q),('both_endpoint_connector',kappa)):
        check(equal(diagonal_matrix(two_parameter['matrices'][name]),M),
              'complete_diagonal_base_change',name)
    for name in ('E','R'):
        for part,rows in full_traces[name].items():
            base=diagonal_matrix(rows)
            diag=diagonal_matrix(two_parameter['full_trace_lifts'][name][part])
            check(equal(base,diag),'complete_trace_diagonal_base_change',(name,part))
    certificate={
      'schema':'marici.branch_a.separated_coefficients_derived_dilation.v2',
      'source_commit':COMMIT,
      'scope':{
        'constructed':'derived pullback along independent branch dilations, followed by their diagonal specialization',
        'not_claimed':['physical tangential trace','flat Rees model','nonzero generic coefficient correspondence','identification with Delta_J'],
        'base_ring':'A=Z[beta,X03,X14,X25]',
        'source_ambient':'S=A[x02,x04,x24,x13,x15,x35]',
        'source_normalization':'R=S/(Iminus Iplus)',
        'target_coefficients':'B=A[Y02,Y04,Y24,Y13,Y15,Y35,Y02^-1,Y35^-1]',
        'deformation_ring':'D=B[t]',
        'coefficient_map':'S -> D, x_i -> t Y_i',
        't_is_not_beta':True,
        'flat_strict_transform_on_chosen_open':'zero, because saturation of (t^2) by t is (1)',
        'generic_derived_incidence':'zero after inverting t'
      },
      'two_parameter':two_parameter,
      'full_trace_lifts':full_traces,
      'variable_order':NAMES,
      'matrix_encoding':'[source_column,target_row,exponent_vector,integer_coefficient]',
      'bases':{'normalization_resolution':PSTATES,'conductor_resolution':QSTATES,
               'occurrence_resolution':OSTATES,'two_endpoint_interval':ts},
      'degrees':{'kernel':PDEG,'source':QDEG,'occurrence':ODEG,'interval':td},
      'homology':{
        'block_encoding':'[homological_bottom_degree,t_exponent,multiplicity]',
        'kernel':pprof,'conductor_source':qprof,'occurrence_target':oprof,
        'trace_submodule':'(D/(t))^2, split by the two exported coefficient detectors',
        'trace_detector_matrix':[[1,0],[1,1]],
        'trace_detector_labels':[
          'coefficient of P_{02,35} p_occ in F(e02 wedge e35), modulo t',
          'coefficient of P_{02,13} p_occ in F(e02 wedge e13), modulo t'],
        'kernel_higher_tor_total_rank_over_B':24
      },
      'matrices':{
        'universal_resolution_d':export_matrix(dp0),
        'dilation_kernel_d':export_matrix(dp),
        'dilation_source_d':export_matrix(dq),
        'dilation_occurrence_d':export_matrix(do),
        'trace_E':export_matrix(fe),'trace_R':export_matrix(fr),
        'trace_E_t_nullhomotopy':export_matrix(homotopies[0]),
        'trace_R_t_nullhomotopy':export_matrix(homotopies[1]),
        'occurrence_t_homotopy':export_matrix(h),
        'interval_d':export_matrix(dt),'endpoint_quotient':export_matrix(q),
        'endpoint_graded_lift':export_matrix(l),'both_endpoint_connector':export_matrix(kappa),
        'kernel_unit_basis':export_matrix(BP),'kernel_unit_basis_inverse':export_matrix(BIP),
        'kernel_block_basis':export_matrix(bp),'kernel_block_basis_inverse':export_matrix(ibp),
        'kernel_block_d':export_matrix(nfp),
        'source_unit_basis':export_matrix(BQ),'source_unit_basis_inverse':export_matrix(BIQ),
        'source_block_basis':export_matrix(bq),'source_block_basis_inverse':export_matrix(ibq),
        'source_block_d':export_matrix(nfq),
        'occurrence_unit_basis':export_matrix(BO),'occurrence_unit_basis_inverse':export_matrix(BIO),
        'occurrence_block_basis':export_matrix(bo),'occurrence_block_basis_inverse':export_matrix(ibo),
        'occurrence_block_d':export_matrix(nfo)
      },
      'block_pairs':{'kernel':pp,'source':qp,'occurrence':oo},
      'basis_operations':{'kernel':op,'source':oq,'occurrence':oo_ops},
      'checks':dict(sorted(COUNTS.items())),
      'exact_check_count':sum(COUNTS.values())
    }
    canonical=json.dumps(certificate,sort_keys=True,separators=(',',':')).encode()
    certificate['semantic_sha256']=sha256(canonical).hexdigest()
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(certificate,sort_keys=True,indent=2)+'\n')
    print(json.dumps({'certificate':str(args.output),'checks':sum(COUNTS.values()),
                      'semantic_sha256':certificate['semantic_sha256'],
                      'resolution_ranks':[1,9,18,15,6,1],
                      'kernel_homology_blocks':pprof,
                      'retained_trace_classes':2,'generic_incidence_zero':True},indent=2))


if __name__=='__main__':main()
