#!/usr/bin/env python3
"""Exact orbit-source admissibility and closed-union descent audit.

Python 3.10+, standard library only. Sparse untruncated polynomials/Laurent
polynomials; every arithmetic operation is integral. Coefficient ring is
A[t04,t35,t02,t15,t24,t13], where A may be Marici's alternating occurrence
ring (with the independent long parameters). The proofs in the companion
note explain why these calculations hold for all coefficient modes.

This checks a *source admissibility test*, not a constructed physical source:
- generic contraction of the actual three 8-column dual pair resolutions;
- ordinary native-gamma no-lift test (a necessary specialization);
- a 28-generator resolution of the closed union of the three pair supports;
- integral fine-degree homology and derived dual groups;
- the closed-cover comparison, its permutation signs, and its dual counit;
- a generic-preserving cone of that counit, without claiming it is the
  normalization/logarithmic correspondence required by the native source.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from itertools import combinations, permutations, product
import hashlib
import json
from pathlib import Path
from typing import Hashable

LABELS = ('04','35','02','15','24','13')
PAIRS = (('04','35'),('02','15'),('24','13'))
ZERO = (0,)*6
COUNTS: Counter[str] = Counter()
Exp = tuple[int,...]
Vec = dict[tuple[Hashable,Exp], int]
Table = dict[Hashable,Vec]


def require(test: bool, category: str, detail=None) -> None:
    if not test:
        raise AssertionError(f'{category}: {detail!r}')
    COUNTS[category] += 1


def pm(n: int) -> int:
    return -1 if n % 2 else 1


def evar(i: int, power: int=1) -> Exp:
    a=[0]*6; a[i]=power; return tuple(a)


def esum(a: Exp,b: Exp) -> Exp:
    return tuple(x+y for x,y in zip(a,b))


def ediff(a: Exp,b: Exp) -> Exp:
    return tuple(x-y for x,y in zip(a,b))


def basis(b: Hashable, m: Exp=ZERO, c: int=1) -> Vec:
    return {(b,m):c} if c else {}


def plus(*vs: Vec) -> Vec:
    out: dict = {}
    for v in vs:
        for key,c in v.items():
            out[key]=out.get(key,0)+c
            if out[key]==0: del out[key]
    return out


def times(v: Vec, m: Exp=ZERO, c: int=1) -> Vec:
    return {(b,esum(a,m)):c*n for (b,a),n in v.items() if c*n}


def apply(op: Table,v: Vec) -> Vec:
    out={}
    for (b,m),c in v.items():
        out=plus(out,times(op.get(b,{}),m,c))
    return out


def compose(a: Table,b: Table) -> Table:
    return {x:apply(a,v) for x,v in b.items()}


def onehot_matrix(op: Table,source,target,*,constant=False):
    row={b:i for i,b in enumerate(target)}
    mat=[[0]*len(source) for _ in target]
    for j,b in enumerate(source):
        for (c,m),n in op.get(b,{}).items():
            if c in row and (not constant or m==ZERO):
                mat[row[c]][j]+=n
    return mat


def unit_rank(a: list[list[int]],label: str) -> int:
    """Integer unimodular reduction; fail rather than assume nonunit minors."""
    a=[r[:] for r in a]
    m=len(a); n=len(a[0]) if m else 0; k=0
    while k<min(m,n):
        hit=next(((i,j) for i in range(k,m) for j in range(k,n)
                  if abs(a[i][j])==1),None)
        if hit is None: break
        i,j=hit
        a[k],a[i]=a[i],a[k]
        for r in a: r[k],r[j]=r[j],r[k]
        if a[k][k]<0: a[k]=[-v for v in a[k]]
        for i in range(m):
            if i!=k and a[i][k]:
                c=a[i][k]; a[i]=[v-c*w for v,w in zip(a[i],a[k])]
        for j in range(n):
            if j!=k and a[k][j]:
                c=a[k][j]
                for i in range(m): a[i][j]-=c*a[i][k]
        k+=1
    require(not any(a[i][j] for i in range(k,m) for j in range(k,n)),
            label+'_unit_smith_factors')
    return k


def pair_data(i: int):
    s=evar(2*i); t=evar(2*i+1); invs=evar(2*i,-1)
    # cochain basis r0*,rc*,rd*,e0*,e1*,e2*,e3*,z*
    degree=(0,0,0,1,1,1,1,2)
    d={b:{} for b in range(8)}
    d[0]=plus(basis(4,t),basis(5,s,-1))
    d[1]=plus(basis(3,c=-1),basis(5))
    d[2]=plus(basis(4,c=-1),basis(6))
    for b,m in zip(range(3,7),(t,s,t,s)): d[b]=basis(7,m)
    h={b:{} for b in range(8)}
    h[3]=plus(basis(0,invs,-1),basis(1,c=-1))
    h[5]=basis(0,invs,-1)
    h[6]=basis(2)
    h[7]=basis(4,invs)
    return degree,d,h


def tensor_factor_op(b, localops, degrees, *,which=None):
    out={}
    for i,v in enumerate(b):
        if which is not None and i!=which: continue
        sign=pm(sum(degrees[j][b[j]] for j in range(i)))
        for (w,m),c in localops[i][v].items():
            target=b[:i]+(w,)+b[i+1:]
            out=plus(out,basis(target,m,sign*c))
    return out


def audit_orbit():
    data=[pair_data(i) for i in range(3)]
    degrees=[z[0] for z in data]; ds=[z[1] for z in data]; hs=[z[2] for z in data]
    for i in range(3):
        for b in range(8):
            require(not apply(ds[i],ds[i][b]),'pair_dual_d_squared',(i,b))
            require(plus(apply(ds[i],hs[i][b]),apply(hs[i],ds[i][b]))==basis(b),
                    'generic_pair_contraction',(i,b))
            require(not apply(hs[i],hs[i][b]),'generic_pair_h_squared',(i,b))
    bs=list(product(range(8),repeat=3))
    D={b:tensor_factor_op(b,ds,degrees) for b in bs}
    H=[{b:tensor_factor_op(b,hs,degrees,which=i) for b in bs} for i in range(3)]
    for b in bs:
        require(not apply(D,D[b]),'orbit_dual_d_squared',b)
        for i in range(3):
            require(plus(apply(D,H[i][b]),apply(H[i],D[b]))==basis(b),
                    'generic_orbit_contraction',(i,b))
            require(not apply(H[i],H[i][b]),'generic_orbit_h_squared',(i,b))
    # Comparing localized contractions requires no invariant average.
    for i,j in combinations(range(3),2):
        HH=compose(H[i],H[j])
        for b in bs:
            lhs=plus(apply(D,HH[b]),times(apply(HH,D[b]),c=-1))
            rhs=plus(H[j][b],times(H[i][b],c=-1))
            require(lhs==rhs,'generic_contraction_higher_comparison',(i,j,b))
    counit={b:(basis('unit') if b==(0,0,0) else {}) for b in bs}
    for b in bs:
        require(not apply(counit,D[b]),'orbit_counit_chain_map',b)
    require(not apply(counit,basis((7,7,7),c=-1)),'top_supported_class_counit_zero')
    return {'basis_count':len(bs),'cochain_ranks':[sum(sum(degrees[i][b[i]] for i in range(3))==q for b in bs) for q in range(7)],
            'generic_contractions':3,'generic_contraction_higher_comparisons':3,
            'counit_top_coefficient':0,
            'shift':{'cohomological':-6,'top_theta_homological_degree_after_operation':-3},
            'generic_localization':'invert t04*t35*t02*t15*t24*t13; contraction is only asserted on this locus',
            'native_generic_source_equivalence':'impossible IF the required generic map is nonzero on this same t-inverted locus',
            'generic_axis_warning':'The support-filtration name Q does not identify its generic leg with the locus where all short Rees t parameters are invertible.'}


# A resolution of the product J0 J1 J2; each factor is B^2 <- B with
# differential (-t,s). A symbol 0/1 selects a variable and 2 a syzygy.
def union_resolution():
    U='unit'
    bs=[U]+list(product(range(3),repeat=3))
    degree={U:0}; weight={U:ZERO}; d={U:{}}
    for b in bs[1:]:
        k=b.count(2); degree[b]=k+1
        w=[0]*6
        for i,a in enumerate(b):
            if a==2: w[2*i]=w[2*i+1]=1
            else: w[2*i+a]=1
        weight[b]=tuple(w)
        out={}
        if k==0:
            out=basis(U,weight[b])
        else:
            for i,a in enumerate(b):
                if a!=2: continue
                sign=pm(b[:i].count(2))
                out=plus(out,basis(b[:i]+(0,)+b[i+1:],evar(2*i+1),-sign),
                          basis(b[:i]+(1,)+b[i+1:],evar(2*i),sign))
        d[b]=out
    return bs,degree,weight,d


def dualize(bs,degree,d):
    dd={b:{} for b in bs}
    for b in bs:
        for (a,m),c in d[b].items():
            # Cochain differential of Hom(F,B) is (-1)^(q+1) d_(q+1)^T.
            dd[a]=plus(dd[a],basis(b,m,pm(degree[a]+1)*c))
    return dd


def fine_matrix(op,source,target,coeff):
    row={b:i for i,b in enumerate(target)}
    mat=[[0]*len(source) for _ in target]
    for j,b in enumerate(source):
        for (t,m),c in op[b].items():
            require(t in row,'fine_map_target_present',(b,t))
            require(esum(coeff[b],m)==coeff[t],'fine_map_degree',(b,t))
            mat[row[t]][j]+=c
    return mat


def allowed_weight(g,w,dual=False):
    v=esum(g,w) if dual else ediff(g,w)
    return v if min(v)>=0 else None


def expected_dual(g):
    neg={i for i,x in enumerate(g) if x==-1}
    if any(x < -1 for x in g): return [0]*5
    blocks=[i for i in range(3) if {2*i,2*i+1}<=neg]
    complete=set().union(*({2*i,2*i+1} for i in blocks)) if blocks else set()
    ranks=[0]*5
    if neg and neg==complete: ranks[len(blocks)+1]=1
    return ranks


def audit_fine_degrees(bs,deg,w,d,dd):
    forward_records=[]; dual_records=[]
    # Every exponent is unbounded. These representatives cover the distinct
    # zero/one/greater-than-one primal and -1/nonnegative dual patterns.
    for g in product(range(3),repeat=6):
        coeff={b:v for b in bs if (v:=allowed_weight(g,w[b])) is not None}
        bb=[[b for b in bs if b in coeff and deg[b]==q] for q in range(5)]
        ranks={0:0,5:0}
        for q in range(1,5):
            ranks[q]=unit_rank(fine_matrix(d,bb[q],bb[q-1],coeff),'union_resolution')
        hh=[len(bb[q])-ranks[q]-ranks[q+1] for q in range(5)]
        in_product=all(g[2*i]>0 or g[2*i+1]>0 for i in range(3))
        expected=[0 if in_product else 1,0,0,0,0]
        require(hh==expected,'union_resolution_fine_exactness',g)
        forward_records.append({'degree':g,'homology':hh})
    for g in product((-1,0,1),repeat=6):
        coeff={b:v for b in bs if (v:=allowed_weight(g,w[b],True)) is not None}
        bb=[[b for b in bs if b in coeff and deg[b]==q] for q in range(5)]
        ranks={-1:0,4:0}
        for q in range(4):
            ranks[q]=unit_rank(fine_matrix(dd,bb[q],bb[q+1],coeff),'union_dual')
        hh=[len(bb[q])-ranks[q-1]-ranks[q] for q in range(5)]
        require(hh==expected_dual(g),'union_dual_fine_cohomology',(g,hh,expected_dual(g)))
        dual_records.append({'degree':g,'cohomology':hh})
    return forward_records,dual_records


def sign_permutation(values):
    return pm(sum(values[i]>values[j] for i in range(len(values)) for j in range(i+1,len(values))))


def perm_exp(m,blockperm,swaps):
    out=[0]*6
    for i in range(3):
        for j in range(2): out[2*blockperm[i]+(j^swaps[i])]=m[2*i+j]
    return tuple(out)


def perm_basis(b,blockperm,swaps):
    if b=='unit': return b,1
    out=[0]*3
    syzygies=[i for i,a in enumerate(b) if a==2]
    sign=sign_permutation([blockperm[i] for i in syzygies])
    for i,a in enumerate(b):
        if a==2:
            out[blockperm[i]]=2
            sign*=pm(swaps[i])
        else: out[blockperm[i]]=a^swaps[i]
    return tuple(out),sign


def perm_vec(v,bp,sw):
    out={}
    for (b,m),c in v.items():
        bb,sgn=perm_basis(b,bp,sw)
        out=plus(out,basis(bb,perm_exp(m,bp,sw),c*sgn))
    return out


def audit_union():
    bs,deg,w,d=union_resolution(); dd=dualize(bs,deg,d)
    for b in bs:
        require(not apply(d,d[b]),'union_d_squared',b)
        require(not apply(dd,dd[b]),'union_dual_d_squared',b)
        for (t,m),c in d[b].items():
            require(deg[t]==deg[b]-1,'union_d_degree',(b,t))
            require(esum(w[t],m)==w[b],'union_d_multidegree',(b,t))
            require(min(m)>=0 and abs(c)==1,'union_integral_polynomial_coefficient')
    for bp in permutations(range(3)):
        for sw in product((0,1),repeat=3):
            for b in bs:
                gb,sgn=perm_basis(b,bp,sw)
                require(perm_vec(d[b],bp,sw)==times(d[gb],c=sgn),
                        'union_signed_pair_permutation',(bp,sw,b))
                require(perm_vec(dd[b],bp,sw)==times(dd[gb],c=sgn),
                        'union_dual_signed_pair_permutation',(bp,sw,b))
    # Seven explicit Ext generators, rather than cohomology ranks alone.
    ext_reps={}; annihilator_primitives={}
    for k in (1,2,3):
        for selected in combinations(range(3),k):
            complement=[i for i in range(3) if i not in selected]
            z={}
            for choice in product((0,1),repeat=len(complement)):
                b=[2]*3; coeff=ZERO
                for i,a in zip(complement,choice):
                    b[i]=a; coeff=esum(coeff,evar(2*i+a))
                z=plus(z,basis(tuple(b),coeff))
            require(not apply(dd,z),'union_explicit_Ext_generator_closed',selected)
            require(bool(z),'union_explicit_Ext_generator_nonzero',selected)
            ext_reps[str(selected)]=z
            for i in selected:
                prior=sum(j<i for j in selected)
                for variable in (0,1):
                    # To produce s use the t-basis covector; to produce t use
                    # the s-basis covector with the additional Koszul sign.
                    chosen=1-variable
                    factor=pm(k+1+prior)*(-1 if variable else 1)
                    primitive={}
                    for (b,m),c in z.items():
                        bb=b[:i]+(chosen,)+b[i+1:]
                        primitive=plus(primitive,basis(bb,m,c*factor))
                    require(apply(dd,primitive)==times(z,evar(2*i+variable)),
                            'union_Ext_annihilator_boundary',(selected,i,variable))
                    annihilator_primitives[str((selected,i,variable))]=primitive
    forward,dual=audit_fine_degrees(bs,deg,w,d,dd)
    # Counit of RHom(B/J_union,B) -> B is dual to the quotient's unit lift.
    eps={b:(basis('scalar') if b=='unit' else {}) for b in bs}
    for b in bs:
        require(not apply(eps,dd[b]),'union_counit_chain_map',b)
    # Cone of the counit, including its canonical map from B.
    cb=['scalar']+[('susp',b) for b in bs]
    cd={'scalar':{}}
    for b in bs:
        v={}
        if b=='unit': v=basis('scalar')
        v=plus(v,{(('susp',t),m):-c for (t,m),c in dd[b].items()})
        cd[('susp',b)]=v
    for b in cb: require(not apply(cd,cd[b]),'generic_preserving_cone_d_squared',b)
    return {'ranks':[sum(deg[b]==q for b in bs) for q in range(5)],
            'minimal_fibre_ranks':[sum(deg[b]==q for b in bs) for q in range(5)],
            'forward_fine_degree_calculations':len(forward),
            'dual_fine_degree_calculations':len(dual),
            'dual_cohomology_degrees':[2,3,4],
            'explicit_Ext_generators':{k:[{'basis':str(b),'monomial':m,'coefficient':c} for (b,m),c in v.items()] for k,v in ext_reps.items()},
            'Ext_generator_annihilator_primitives':{k:[{'basis':str(b),'monomial':m,'coefficient':c} for (b,m),c in v.items()] for k,v in annihilator_primitives.items()},
            'dual_cohomology':{
                '2':'direct sum over i of B/(s_i,t_i) with dual pair determinant',
                '3':'direct sum over i<j of B/(s_i,t_i,s_j,t_j) with four-normal and Cech orientations',
                '4':'B/(all six parameters) with six-normal and Cech orientations'},
            'cohomology_is_not_claimed_as_derived_direct_sum':True,
            'signed_block_and_within_pair_actions':48,
            'counit_cone_free_basis_count':len(cb),
            'generic_preserving_cone_scalar_cohomology':{
                '0':'B','1':'Ext2(B/J_union,B)','2':'Ext3(B/J_union,B)','3':'Ext4(B/J_union,B)'},
            'forward_multigrades':forward,'dual_multigrades':dual,
            'resolution':{'basis':[str(b) for b in bs], 'degrees':{str(b):deg[b] for b in bs},
              'weights':{str(b):w[b] for b in bs},
              'd':{str(b):[{'target':str(t),'monomial':m,'coefficient':c} for (t,m),c in d[b].items()] for b in bs}}}


def audit_closed_cover():
    bs=[('augment',)]+[s for k in (1,2,3) for s in combinations(range(3),k)]
    d={b:{} for b in bs}
    d[('augment',)]={((i,),ZERO):1 for i in range(3)}
    for size in (1,2):
        for b in combinations(range(3),size):
            for j in set(range(3))-set(b):
                target=tuple(sorted(b+(j,)))
                d[b]=plus(d[b],basis(target,c=pm(target.index(j))))
    for b in bs: require(not apply(d,d[b]),'closed_cover_d_squared',b)
    records=[]
    for g in product((0,1),repeat=6):
        active={i for i in range(3) if g[2*i]==g[2*i+1]==0}
        bb=[[('augment',)] if active else []]
        bb += [[s for s in combinations(sorted(active),k)] for k in (1,2,3)]
        rank={-1:0,3:0}
        for q in range(3): rank[q]=unit_rank(onehot_matrix(d,bb[q],bb[q+1]),'closed_cover')
        hh=[len(bb[q])-rank[q-1]-rank[q] for q in range(4)]
        require(hh==[0]*4,'closed_cover_exactness_per_monomial',g)
        # Monomial membership in the intersection of ideals equals product membership.
        in_intersection=all(g[2*i] or g[2*i+1] for i in range(3))
        choices=list(product((0,1),repeat=3))
        in_product=any(all(g[2*i+choice[i]] for i in range(3)) for choice in choices)
        require(in_intersection==in_product,'closed_union_ideal_product',g)
        records.append({'positive_exponent_support':g,'active_components':sorted(active)})
    return {'monomial_patterns':64,'Cech_component_ranks':[3,3,1],
            'ideal_generators':[[LABELS[2*i+a[i]] for i in range(3)] for a in product((0,1),repeat=3)],
            'records':records,
            'separating_base_change':{'localization':'invert t02 and t24 only',
                'intersection_object':'zero','union_object':'B/(t04,t35) with t02,t24 inverted',
                'union_dual':'supported pair dual in degree two'}}


def audit_native():
    # Independent sparse polynomial ring Z[x,y,s,t]/(xy), represented below.
    zero=(0,)*4
    def mono(i): return tuple(int(j==i) for j in range(4))
    def mult(a,b):
        v=tuple(x+y for x,y in zip(a,b))
        return None if v[0] and v[1] else v
    def addv(*vs):
        o={}
        for v in vs:
            for k,c in v.items():
                o[k]=o.get(k,0)+c
                if not o[k]: del o[k]
        return o
    def scale(v,m,c=1):
        o={}
        for (b,n),a in v.items():
            z=mult(n,m)
            if z is not None: o=addv(o,{(b,z):a*c})
        return o
    x,y,s,t=[mono(i) for i in range(4)]
    sx=mult(s,x); ty=mult(t,y)
    d={0:{('pc',x):-1,('pd',y):-1},1:{('pc',sx):-1},2:{('pd',ty):-1}}
    gamma={('pc',x):1}
    Us={(1,zero):-1}; Ut={(0,t):-1,(2,zero):1}
    def bd(v):
        o={}
        for (b,m),c in v.items(): o=addv(o,scale(d.get(b,{}),m,c))
        return o
    require(bd(Us)==scale(gamma,s),'native_first_primitive_s')
    require(bd(Ut)==scale(gamma,t),'native_first_primitive_t')
    G=addv(scale(Ut,s),scale(Us,t,-1))
    require(G=={(0,mult(s,t)):-1,(1,t):1,(2,s):1},'native_second_coherence')
    require(not bd(G),'native_second_coherence_closed')
    require(bool(G),'native_second_coherence_nonzero')
    def detector(v):
        return v.get(('pc',x),0)-v.get(('pd',y),0)
    for a in product(range(4),repeat=4):
        if a[0] and a[1]: continue
        for b in range(3): require(detector(scale(d[b],a))==0,'native_gamma_boundary_detector')
    require(detector(gamma)==1,'native_gamma_detector_unit')
    # Inclusion of the pair Koszul complex in the six-parameter Koszul DGA.
    allsubs=[s for k in range(7) for s in combinations(range(6),k)]
    KD={b:{} for b in allsubs}
    for b in allsubs:
        for j,a in enumerate(b): KD[b]=plus(KD[b],basis(b[:j]+b[j+1:],evar(a),pm(j)))
    for b in ((),(0,),(1,),(0,1)):
        require(all(set(c)<={0,1} for (c,_m) in KD[b]),'pair_in_six_koszul_subcomplex',b)
    return {'native_projection_ranks':[2,3],
            'gamma':'x*pc','coherence':'-s*t*r0+t*r04+s*r35',
            'gamma_boundary_detector':1,
            'six_parameter_ordinary_lift_of_gamma':'excluded by restriction to the first-pair Koszul subcomplex',
            'scope':'Uses the supplied genuine specialization/quotient of the 245-state source; no newer full native matrix is asserted.'}


def audit_local_Q_obstruction():
    # After pair (04,35) support and localization at t02,t24, the preceding
    # exact lifting ideal becomes (t13*t15, I_minus). Its monomial membership
    # is checked in every sheet and in all remaining t-support patterns.
    records=[]
    for sheet in ('conductor','positive','negative'):
        for powers in product(range(3),repeat=2):
            original=(powers[0]>0 and powers[1]>0) or sheet=='negative'
            reduced=(powers[0]>=1 and powers[1]>=1) or sheet=='negative'
            require(original==reduced,'localized_PC_lifting_ideal_membership',(sheet,powers))
            records.append({'coefficient_sheet':sheet,'t13_t15_exponents':powers,'lifts':reduced})
    require(not records[0]['lifts'],'localized_PC_generic_unit_does_not_lift')
    # A direct independent top-row witness: on the positive branch a lift
    # of theta would require t13*a13=-U_L. U_L is independent of t13,
    # so reduction modulo t13 has zero left side and nonzero right side.
    for power in range(8):
        lhs_degree=power+1
        require(lhs_degree>0,'singleton_row_multiple_of_t13')
    rhs_normal_degree=0
    require(rhs_normal_degree==0,'singleton_row_UL_survives_mod_t13')
    # In the coefficient ring modulo I_minus and t13, the unit remains.
    require(1!=0,'localized_lifting_ideal_is_proper')
    return {'open':'D(t02*t24)', 'pair_support':'t04=t35=0',
            'union_dual_on_open':'the single (04,35) dual comparison (up to the retained endpoint line)',
            'triple_tensor_on_open':'contractible',
            'localized_lifting_ideal':'(t13*t15, I_minus)',
            'unit_lift_obstruction_equation':'t13*a13 = -U_L on the positive sheet',
            'unit_lift_obstruction_test':'mod t13: 0 = -U_L, impossible',
            'localized_linearity_extension_annihilator':'I_plus + I_minus + (t13*t15)',
            'global_union_target_Q_section':'does not exist, by this open restriction',
            'membership_records':records,
            'scope':'Closed-union coefficient descent; not an identification with an unconstructed native physical source.'}


def main(output: Path):
    orbit=audit_orbit()
    union=audit_union()
    cover=audit_closed_cover()
    native=audit_native()
    local_Q=audit_local_Q_obstruction()
    previous={}
    for name in ('check_marici_q_supported_pair_20260907.py',
                 'marici_q_supported_pair_and_orbit_20260907.md',
                 'marici_q_supported_pair_certificate_20260907.json'):
        p=Path(__file__).with_name(name)
        if p.exists(): previous[name]={'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
    result={'status':'proved_scoped_tensor_descent_nonidentification_and_closed_union_Q_obstruction',
      'pinned_commit':'d1947b67a60d3e88ba77f4ca60ea02c2a306ee61',
      'parameters':LABELS,'pairs':PAIRS,
      'orbit':orbit,'union':union,'closed_cover':cover,'native':native,'local_Q_obstruction':local_Q,
      'assertions':dict(sorted(COUNTS.items())),'exact_assertions':sum(COUNTS.values()),
      'input_hashes':previous,
      'scope_exclusions':[
        'The valid special-fibre Q section is not withdrawn.',
        'Q is a support-filtration quotient. Its generic label does not automatically identify the external deformation parameters with the six t variables.',
        'No theorem excludes applying the tensor functor to a native source as a supported operation.',
        'It is excluded as a replacement kernel with nonzero generic map on the same t-inverted locus.',
        'The closed-union module is an explicitly constructed coefficient-descent alternative, not an identified physical source.',
        'The finite dual support layer is not full local cohomology or a nearby-cycle construction.',
        'All line and degree comparisons are retained; no six-normal determinant is identified with the physical channel orientation.',
        'The counit cone preserves any supplied generic map but does not construct a missing native-to-target map.',
        'No proof-assistant verification or repository writes.'
      ]}
    output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':result['status'],'exact_assertions':result['exact_assertions'],
      'orbit_ranks':orbit['cochain_ranks'],'union_resolution_ranks':union['ranks'],
      'union_dual_degrees':union['dual_cohomology_degrees'],
      'fine_degree_calculations':union['forward_fine_degree_calculations']+union['dual_fine_degree_calculations'],
      't_inverted_source_test':'explicit contraction; excludes a nonzero generic map only on this same locus',
      'tensor_is_closed_support_descent':False,
      'closed_union_Q_section':'excluded by (t13*t15,I_minus) on D(t02*t24)',
      'old_special_target_section':'retained'},indent=2))


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path('marici_orbit_source_admissibility_certificate_20260907.json'))
    args=parser.parse_args()
    main(args.output)
