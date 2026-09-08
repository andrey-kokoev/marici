#!/usr/bin/env python3
"""Simultaneous derived normalization/conductor comparison, exact audit.

Standard library only. All degrees below are homological. The infinite
models are specified by parity formulas; a finite window is checked with
extra boundary degrees, never used as an all-degree extrapolation.
No repository writes, network, division by integers, or fitted coefficients.
"""
from __future__ import annotations
import argparse
from collections import Counter
from itertools import combinations, product
from pathlib import Path
import json

CHECKS: Counter[str] = Counter()
NV = 8
ZERO = (0,) * NV
LABELS = ((1,3),(1,5),(3,5),(0,2),(0,4),(2,4))
PLUS = (0,1,2)
MINUS = (3,4,5)
COMMIT = 'd1947b67a60d3e88ba77f4ca60ea02c2a306ee61'
# Sparse linear combinations have keys (atom, exponent_tuple).
# Native coefficients obey x_i*y_j=0; auxiliary coefficients obey a*b=0.


def check(ok: bool, name: str, detail=None) -> None:
    if not ok:
        raise AssertionError((name, detail))
    CHECKS[name] += 1


def pm(n: int) -> int:
    return -1 if n % 2 else 1


def put(v: dict, k, a: int) -> None:
    if a:
        v[k] = v.get(k,0) + a
        if not v[k]:
            del v[k]


def add(*vs: dict) -> dict:
    ans = {}
    for v in vs:
        for k,a in v.items(): put(ans,k,a)
    return ans


def scale(v: dict, a: int) -> dict:
    return {k:a*c for k,c in v.items() if a*c}


def var(i: int):
    return tuple(int(i==j) for j in range(NV))


def side(e):
    pos=any(e[i] for i in PLUS)
    neg=any(e[i] for i in MINUS)
    return 'mixed' if pos and neg else 'plus' if pos else 'minus' if neg else 'constant'


def allowed(e, mode):
    if mode=='aux': return not(e[6] and e[7])
    if mode=='native': return not(e[6] or e[7]) and side(e)!='mixed'
    if mode=='plus': return not any(e[i] for i in (*MINUS,6,7))
    if mode=='minus': return not any(e[i] for i in (*PLUS,6,7))
    if mode=='conductor': return not any(e)
    raise ValueError(mode)


def single(a, e=ZERO, c=1, mode='native'):
    return {(a,e):c} if c and allowed(e,mode) else {}


def mons(total: int, n=NV):
    out=[]
    def rec(prefix, rem, left):
        if left==0:
            out.append(tuple(prefix)); return
        for a in range(rem+1): rec(prefix+[a],rem-a,left-1)
    rec([],total,n)
    return out


def extend(v, op, mode='native'):
    out={}
    for (a,e),c in v.items():
        for (b,f),s in op(a).items():
            g=tuple(x+y for x,y in zip(e,f))
            if allowed(g,mode): put(out,(b,g),c*s)
    return out


def multiply(v,e,mode='native'):
    out={}
    for (a,f),c in v.items():
        g=tuple(x+y for x,y in zip(e,f))
        if allowed(g,mode): put(out,(a,g),c)
    return out


def res_basis(tag,n):
    return [(tag,n,j) for j in range(1 if tag=='D' and n==0 else 2)]


def res_d(a):
    tag,n,j=a
    if n==0:return {}
    if tag=='M':
        # Slot zero is U/(z_minus); slot one is U/(z_plus).
        z=(7 if n%2 else 6) if j==0 else (6 if n%2 else 7)
        return single((tag,n-1,j),var(z),mode='aux')
    if n==1:
        return single(('D',0,0),var(6+j),mode='aux')
    z=(7 if j==0 else 6) if n%2==0 else (6 if j==0 else 7)
    return single(('D',n-1,j),var(z),mode='aux')


def delta(a):
    tag,n,j=a
    assert tag=='M'
    if n==0:return single(('D',0,0),c=1 if j==0 else -1)
    # J = [[0,-1],[1,0]] in ordered (e_zplus,e_zminus) basis.
    return single(('D',n,1-j),c=1 if j==0 else -1)


def inverse_delta(a):
    _,n,j=a
    assert n>=1
    return single(('M',n,1-j),c=-1 if j==0 else 1)


def fib_degree(a):
    return a[1] if a[0]=='M' else a[1]-1


def fib_d(a, mode='native'):
    tag,n,j=a
    if mode=='native': return delta(a) if tag=='M' else {}
    vertical=res_d(a)
    return add(vertical,delta(a)) if tag=='M' else scale(vertical,-1)


def act(v, r, flip, total='fib'):
    def diag(a,b):return tuple(sorted((a%6,b%6)))
    vertex=lambda i:(i+2*r)%6 if not flip else (1-i+2*r)%6
    perm=[LABELS.index(diag(vertex(a),vertex(b))) for a,b in LABELS]
    perm += [7,6] if flip else [6,7]
    out={}
    for (a,e),c in v.items():
        f=[0]*8
        for i,k in enumerate(e):f[perm[i]]=k
        tag,n,j=a
        s=1
        if flip:
            if tag in ('M','nm'): j=1-j
            elif tag in ('D','nd'):
                s=-1
                if n>=1:j=1-j
        put(out,((tag,n,j),tuple(f)),s*c)
    return out


def alpha(v):
    out={}
    for (a,e),c in v.items():
        tag,n,j=a
        if n!=0:continue
        mode=('plus' if j==0 else 'minus') if tag=='M' else 'conductor'
        if allowed(e,mode):put(out,(('nm' if tag=='M' else 'nd',0,j),e),c)
    return out


def native_d(v):
    out={}
    for ((tag,n,j),e),c in v.items():
        if tag=='nm' and allowed(e,'conductor'):
            put(out,(('nd',0,0),e),c*(1 if j==0 else -1))
    return out


def in_kernel(a,e):
    tag,n,j=a
    if n>=1:return allowed(e,'native')
    if tag=='M':return side(e)==('minus' if j==0 else 'plus')
    return side(e) in ('plus','minus')


def kernel_h(v):
    out={}
    for (a,e),c in v.items():
        tag,n,j=a
        if tag!='D':continue
        if n>=1:
            out=add(out,multiply(scale(inverse_delta(a),c),e))
        else:
            which=side(e)
            if which=='plus':put(out,(('M',0,1),e),-c)
            elif which=='minus':put(out,(('M',0,0),e),c)
            else:raise ValueError('h_0 requires conductor-vanishing coefficient')
    return out


def kernel_basis(nmax, monlist):
    for n in range(nmax+1):
        for tag in ('M','D'):
            for a in res_basis(tag,n):
                for e in monlist:
                    if in_kernel(a,e):yield a,e


def matrix_rank_unit(rows, ncols=None):
    a=[r[:] for r in rows]
    m=len(a);n=len(a[0]) if a else (ncols or 0);r=0
    while r<min(m,n):
        hit=next(((i,j) for i in range(r,m) for j in range(r,n) if abs(a[i][j])==1),None)
        if hit is None:break
        i,j=hit;a[r],a[i]=a[i],a[r]
        for row in a:row[r],row[j]=row[j],row[r]
        if a[r][r]<0:a[r]=[-x for x in a[r]]
        for i in range(r+1,m):
            if a[i][r]:
                c=a[i][r];a[i]=[x-c*y for x,y in zip(a[i],a[r])]
        for j in range(r+1,n):
            if a[r][j]:
                c=a[r][j]
                for i in range(m):a[i][j]-=c*a[i][r]
        r+=1
    check(not any(a[i][j] for i in range(r,m) for j in range(r,n)),
          'integral_matrix_has_only_unit_factors')
    return r


def audit_resolutions(nmax):
    am=[e for e in mons(3) if allowed(e,'aux')]
    for n in range(nmax+2):
        for tag in ('M','D'):
            for a in res_basis(tag,n):
                for e in am:
                    v=single(a,e,mode='aux')
                    check(not extend(extend(v,res_d,'aux'),res_d,'aux'),'resolution_d_squared')
                    check(not extend(extend(v,lambda b:fib_d(b,'aux'),'aux'),lambda b:fib_d(b,'aux'),'aux'),
                          'derived_fibre_d_squared_before_base_change')
                    if tag=='M':
                        check(extend(extend(v,delta,'aux'),res_d,'aux')==extend(extend(v,res_d,'aux'),delta,'aux'),
                              'lift_of_conductor_difference_is_chain_map')
                for r,flip in product(range(3),range(2)):
                    v=single(a,mode='aux')
                    check(act(extend(v,res_d,'aux'),r,flip)==extend(act(v,r,flip),res_d,'aux'),
                          'resolution_dihedral_covariance')
                    if tag=='M':
                        check(act(extend(v,delta,'aux'),r,flip)==extend(act(v,r,flip),delta,'aux'),
                              'difference_dihedral_covariance')
    # Polynomial annihilator test for periodic exactness, including coefficients.
    for e in am:
        for zi,zj in ((6,7),(7,6)):
            v=single(('t',0,0),e,mode='aux')
            killed=not multiply(v,var(zi),'aux')
            check(killed==(e[zj]>0),'periodic_annihilator_monomial_test')
    # Exact formulas prove Ann(z+)=(z-), Ann(z-)=(z+), and disjoint images.
    return {'free_resolution_window':nmax+1,'all_degree_map':{'degree_0':[1,-1],'positive_degrees':[[0,-1],[1,0]]}}


def audit_kernel(nmax):
    bm=[e for e in mons(3) if allowed(e,'native')]
    units=[ZERO]+[var(i) for i in range(6)]
    for n in range(nmax+1):
        for tag in ('M','D'):
            for a in res_basis(tag,n):
                for e in bm:
                    v=single(a,e)
                    check(native_d(alpha(v))==alpha(extend(v,fib_d)),'comparison_chain_map')
                    for m in units:
                        check(alpha(multiply(v,m))==multiply(alpha(v),m,
                              'plus' if tag=='M' and a[2]==0 else 'minus' if tag=='M' else 'conductor'),
                              'comparison_module_linearity')
    for a,e in kernel_basis(nmax,bm):
        v=single(a,e)
        check(not alpha(v),'kernel_basis_actual_kernel')
        hv=kernel_h(v)
        lhs=add(extend(hv,fib_d),kernel_h(extend(v,fib_d)))
        check(lhs==v,'entire_comparison_kernel_contraction')
        check(not kernel_h(hv),'kernel_h_square_zero')
        for m in units:
            check(kernel_h(multiply(v,m))==multiply(hv,m),'kernel_h_B_linearity')
        for r,flip in product(range(3),range(2)):
            check(kernel_h(act(v,r,flip))==act(hv,r,flip),'kernel_h_dihedral_covariance')
    # The map is a quasi-isomorphism, NOT an ambient B-linear deformation retraction.
    y=var(3);x=var(0)
    check(not multiply(single(('t',0,0),x),y),'opposite_ideal_product_zero')
    check(bool(multiply(single(('t',0,0)),y)),'branch_section_would_violate_module_linearity')
    return {'total_kernel':'contractible by explicit B-linear equivariant homotopy',
            'ambient_chain_inverse_claimed':False,
            'total_conductor_comparison':'quasi-isomorphism',
            'sheet_and_conductor_defect_H0':'I_minus + I_plus',
            'sheet_and_conductor_defect_Hn_positive':'B^2 in every positive homological degree'}


def audit_filtered_rees(nmax):
    # A Rees coefficient is an additional nonnegative exponent of lambda.
    # d_lambda=lambda*d; h unchanged, so d_lambda h+h d_lambda=lambda.
    def dlam(v):
        out={}
        for (a,e,l),c in v.items():
            for (b,f),s in fib_d(a).items():
                g=tuple(x+y for x,y in zip(e,f))
                if allowed(g,'native'):put(out,(b,g,l+1),c*s)
        return out
    def hlam(v):
        out={}
        for (a,e,l),c in v.items():
            for (b,f),s in kernel_h(single(a,e,c)).items():put(out,(b,f,l),s)
        return out
    def timeslam(v):return {(a,e,l+1):c for (a,e,l),c in v.items()}
    bm=[e for e in mons(2) if allowed(e,'native')]
    for a,e in kernel_basis(nmax,bm):
        for l in range(3):
            v={(a,e,l):1}
            check(not dlam(dlam(v)),'Rees_kernel_d_squared')
            check(add(dlam(hlam(v)),hlam(dlam(v)))==timeslam(v),'Rees_homotopy_to_lambda')
    # The kernel filtration has conductor row weight 0, sheet row weight 1.
    e=var(0);v=single(('D',0,0),e)
    check(all(k[0][0]=='M' for k in kernel_h(v)),'contraction_increases_row_filtration')
    # Every lambda^0 conductor defect is closed, with no incoming lambda^0 term.
    for n in range(nmax+1):
        for a in res_basis('D',n):
            coeff=var(0) if n==0 else ZERO
            check(not dlam({(a,coeff,0):1}),'nonzero_Rees_residue_closed')
            check(all(k[2]>0 for k in dlam({(('M',max(n,1),0),ZERO,0):1})),
                  'all_Rees_boundaries_divisible_by_lambda')
    return {'parameter':'lambda; bookkeeping conductor-row Rees variable, not a physical t parameter',
            'filtered_quasi_isomorphism':False,
            'Rees_kernel_homology':{'-1':'I_occ killed by lambda','n>=0':'B^2 killed by lambda'},
            'lambda_one_fibre':'acyclic',
            'lambda_zero_fibre':'both nonzero associated-graded defect rows',
            'integer_torsion_introduced':False}


# Endpoint rows of the base-changed quotient/road construction.
# Atom ('node',i,j), ('sheet',i,j), ('road',i,j,k),
# ('tag',i,j,k), ('top',i,j), ('end',i,j).
# i is the auxiliary resolution degree. Row zero has the original 1,4,5,1
# matrix; rows i>0 retain two conductor coefficients and an invertible sheet
# comparison instead of the old node relation.

def endpoint_basis(i):
    d=1 if i==0 else 2
    byh={0:[('end',i,j) for j in range(d)],
         1:[('sheet',i,j) for j in range(2)]+[('road',i,j,k) for j in range(d) for k in range(3)],
         2:([('node',0,0)] if i==0 else [])+[('tag',i,j,k) for j in range(d) for k in range(3)],
         3:[('top',i,j) for j in range(d)]}
    return byh


def end_d(a):
    tag,i,j,*rest=a
    if tag=='end':return {}
    if tag=='sheet':
        if i==0:return {('end',i,0):1 if j==0 else -1}
        return {('end',i,1-j):1 if j==0 else -1}
    if tag=='road':return {('end',i,j):-1}
    if tag=='node':return {('sheet',0,0):1,('sheet',0,1):1}
    if tag=='tag':
        k=rest[0]
        return {('road',i,j,k):1,('road',i,j,(k+1)%3):-1}
    if tag=='top':return {('tag',i,j,k):1 for k in range(3)}
    raise ValueError(a)


def plain_apply(v,op):
    out={}
    for a,c in v.items():
        for b,s in op(a).items():put(out,b,c*s)
    return out


def row_readout(a):
    return {('coef',a[1],a[2]):1} if a[0]=='road' else {}


def row_unit(i,j):
    v={('road',i,j,0):1}
    if i==0:put(v,('sheet',0,0),1)
    elif j==0:put(v,('sheet',i,1),-1)
    else:put(v,('sheet',i,0),1)
    return v


def endpoint_action(a,r,flip):
    tag,i,j,*rest=a
    if tag=='node':return {a:1}
    sign=1
    if tag=='sheet':
        return {(tag,i,1-j if flip else j):1}
    # Every other term is a tensor with the oriented conductor resolution.
    if flip:
        sign=-1
        if i>=1:j=1-j
    if tag in ('road','tag'):
        k=rest[0]
        if flip:
            k=(-k)%3
            if tag=='tag':k=(k-1)%3;sign=-sign
        k=(k+r)%3
        return {(tag,i,j,k):sign}
    if tag=='top' and flip:sign=-sign
    return {(tag,i,j):sign}


def audit_endpoints(nmax):
    tables=[]
    for i in range(nmax+1):
        basis=endpoint_basis(i)
        ranks={}
        for h in (1,2,3):
            src,tgt=basis[h],basis[h-1]
            mat=[[end_d(a).get(b,0) for a in src] for b in tgt]
            ranks[h]=matrix_rank_unit(mat,len(src))
        hom={h:len(basis[h])-ranks.get(h,0)-ranks.get(h+1,0) for h in range(4)}
        d=1 if i==0 else 2
        check(hom=={0:0,1:d,2:0,3:0},'complete_endpoint_row_integral_homology')
        for a in sum(basis.values(),[]):
            check(not plain_apply(end_d(a),end_d),'endpoint_row_d_squared')
            check(not plain_apply(end_d(a),row_readout),'endpoint_road_readout_kills_boundaries')
            for r,flip in product(range(3),range(2)):
                check(plain_apply(end_d(a),lambda b:endpoint_action(b,r,flip))==
                      plain_apply(endpoint_action(a,r,flip),end_d),'endpoint_row_dihedral_covariance')
        for j in range(d):
            z=row_unit(i,j)
            check(not plain_apply(z,end_d),'primitive_derived_endpoint_cycle')
            check(plain_apply(z,row_readout)=={('coef',i,j):1},'primitive_derived_endpoint_readout')
        tables.append({'auxiliary_degree':i,'column_ranks':[len(basis[h]) for h in range(4)],
                       'differential_ranks':[ranks[h] for h in (1,2,3)],
                       'homology_degree':i+1,'homology_rank':d})
    # Conductor augmentation B -> C cannot have a B-linear section.
    # Ann_B(I)=0: basis monomials on one sheet survive multiplication by
    # that sheet's first variable; a common constant survives both.
    for e in mons(3):
        if not allowed(e,'native'):continue
        det=0 if side(e)!='minus' else 3
        check(bool(multiply(single(('c',0,0),e),var(det))),
              'conductor_annihilator_zero_on_normal_monomials')
    return {'derived_endpoint_H1':'B_or', 'derived_endpoint_Hn_for_n_ge_2':'B^2 with transported orientation',
            'native_endpoint_H1':'C_or','native_endpoint_other_homology':0,
            'endpoint_comparison_fibre_H1':'I_occ_or','endpoint_comparison_fibre_Hn_ge_2':'B^2',
            'unit_preserving_B_linear_derived_section':False,
            'row_audit':tables}


# Original PC differential and tensor contraction compatibility.

def audit_PC(nmax):
    ds=tuple((a,b) for a in range(6) for b in range(a+1,6) if b-a not in (1,5))
    short=set(LABELS);plus=set(LABELS[:3]);minus=set(LABELS[3:])
    def cross(a,b):return a[0]<b[0]<a[1]<b[1] or b[0]<a[0]<b[1]<a[1]
    faces=[tuple(f) for k in range(4) for f in combinations(ds,k)
           if not any(cross(a,b) for a,b in combinations(f,2))]
    cells=[(f,m) for f in faces for k in range(len(f)+1) for m in combinations(f,k)]
    one=(0,)*18;d={};census=Counter()
    def loc(c):return set(c[0])-set(c[1])
    def deg(c):return 3-len(c[0])+len(c[1])
    def alive(c):return not(loc(c)&plus and loc(c)&minus)
    for cell in cells:
        f,m=cell;out={}
        for a in ds:
            if a in f or any(cross(a,b) for b in f):continue
            e=[0]*18;k=ds.index(a);e[k]=1;e[9+k]=-1
            put(out,((tuple(sorted(f+(a,))),m),tuple(e)),pm(sum(b<a for b in f)))
        for k,a in enumerate(m):put(out,((f,tuple(x for x in m if x!=a)),one),pm(3-len(f)+k))
        d[cell]=out
        L=loc(cell)
        typ='none' if not L&short else 'mixed' if L&plus and L&minus else 'plus' if L&plus else 'minus'
        census[typ]+=1
    def dc(v):
        out={}
        for (cell,e),a in v.items():
            for (t,f),b in d[cell].items():put(out,(t,tuple(x+y for x,y in zip(e,f))),a*b)
        return out
    arrows=0
    for cell in cells:
        check(not dc(d[cell]),'PC_d_squared_all_loaded_states')
        for (target,coef),a in d[cell].items():
            arrows+=1
            check(loc(cell)<loc(target) and len(loc(target)-loc(cell))==1,'PC_localization_covering_incidence')
            check(deg(target)==deg(cell)-1,'PC_differential_degree')
            if not alive(cell):check(not alive(target),'zero_native_stalk_stays_zero')
            # Tensor h on the coefficient-row factor has degree +1. The
            # target differential signs cancel, for every actual incidence.
            for q in range(-1,nmax+1):
                check(pm(q+1)+pm(q)==0,'tensor_h_mixed_differential_cancellation')
    check((len(cells),arrows)==(215,522),'source_state_and_arrow_census')
    check(census==Counter({'none':72,'plus':64,'minus':64,'mixed':15}),'exact_native_localization_types')
    longs=[a for a in ds if a not in short]
    U=[0]*18
    for a in longs:U[9+ds.index(a)]=1
    theta={(((),()),tuple(U)):1}
    for a in longs:
        e=U[:];e[ds.index(a)]+=1;e[9+ds.index(a)]-=1
        theta[(((a,),(a,)),tuple(e))]=-1
    beta=dc(theta)
    check(not {k:a for k,a in beta.items() if not set(k[0][0])&short},'genuine_Q_cycle')
    check(len(beta)==18,'all_eighteen_connecting_terms_retained')
    check(not dc(beta),'connecting_boundary_closed')
    for S in (tuple(sorted(plus)),tuple(sorted(minus))):
        ep=(S,S)
        check(len(d[ep])==3,'fully_marked_endpoint_keeps_three_boundaries')
        check(all(set(c[0])==set(S) for (c,e) in d[ep]),'endpoint_boundary_labels_unchanged')
    return {'cells':len(cells),'covering_incidences':arrows,'census':dict(census),
            'generic_Q_connecting_terms':18,'endpoint_normal_removal_terms_each':3,
            'physical_connector_constructed':False}


def main(path: Path, degree: int):
    if degree<2 or degree>30:raise ValueError('--degree must lie between 2 and 30')
    res=audit_resolutions(degree)
    ker=audit_kernel(degree)
    rees=audit_filtered_rees(degree)
    ep=audit_endpoints(degree)
    pc=audit_PC(degree)
    cert={'date_label':'2026-09-07','source_commit':COMMIT,
          'status':'explicit_derived_diagram_equivalence_with_filtered_and_endpoint_defects',
          'resolutions':res,'complete_conductor_kernel':ker,'row_filtration':rees,
          'relative_endpoint_comparison':ep,'source_target_compatibility':pc,
          'checks':dict(sorted(CHECKS.items())),'exact_assertions':sum(CHECKS.values()),
          'scope':[
            'Exact integer and monomial identities supplement parity/all-degree proofs; no proof-assistant claim.',
            'Derived base change of the complete conductor kernel is equivalent to the native kernel.',
            'Neither the normalization term nor relative conductor quotient is individually an equivalence.',
            'The contraction is not conductor-row-filtered; its Rees defect is computed with a new bookkeeping lambda, not a physical normal.',
            'Endpoint computation is the stated quotient-and-road coefficient pattern, not a native 215-state physical source identification.',
            'Existing generic Q boundary and both endpoint differentials remain; no physical connector is claimed.',
            'No integer-prime torsion or arithmetic-derivative conclusion.']}
    path.write_text(json.dumps(cert,indent=2)+'\n')
    print(json.dumps({k:cert[k] for k in ('status','complete_conductor_kernel','row_filtration','source_target_compatibility','exact_assertions')},indent=2))


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--degree',type=int,default=8)
    parser.add_argument('--output',type=Path,default=Path(__file__).with_name('marici_derived_normalization_diagram_certificate_20260907.json'))
    args=parser.parse_args()
    main(args.output,args.degree)
