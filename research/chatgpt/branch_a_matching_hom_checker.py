#!/usr/bin/env python3
"""Matching-Hom coefficient audit; physical matching data remain uninstantiated.

Standalone; Python standard library only. Reconstructs the complete ten-state
post-reciprocal trace target, the two trace maps and normalization homotopies,
the conductor resolution through degree four, the first conormal extension,
and all degree-two/degree-three Yoneda products used by the proof.

The source resolution is the alternating exterior-block resolution over
R=A[X02,X04,X24,X13,X15,X35]/(I_minus I_plus), A=Z[beta,X03,X14,X25].
An explicit A-linear contraction is checked on monomials and proved for
arbitrary degrees in the accompanying proof. No polynomial sampling is used
as a replacement for that exactness proof.
"""
from __future__ import annotations
import argparse
from ast import literal_eval
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, product
import json
from pathlib import Path

SHORT=('02','04','24','13','15','35')
VARS=tuple('X'+s for s in SHORT)+('beta','X03','X14','X25')
MINUS=(0,1,2); PLUS=(3,4,5); Z=5; BETA=6; ZERO=(0,)*10
COUNTS=Counter()

def check(ok,label,detail=None):
    if not ok: raise AssertionError(f'{label}: {detail}')
    COUNTS[label]+=1

def put(out,key,value):
    if value:
        out[key]=out.get(key,0)+value
        if not out[key]: del out[key]

def add(v,w,c=1):
    out=dict(v)
    for key,a in w.items(): put(out,key,c*a)
    return out

def mon(*indices):
    p=[0]*10
    for i in indices: p[i]+=1
    return tuple(p)

def plus(p,q): return tuple(a+b for a,b in zip(p,q))
def survive(p): return not(any(p[i] for i in MINUS) and any(p[i] for i in PLUS))
def mul(v,p,c=1,mode='R'):
    out={}
    for (j,q),a in v.items():
        r=plus(p,q)
        if legal(r,mode): put(out,(j,r),a*c)
    return out

def legal(p,mode):
    if mode=='A': return not any(p[:6])
    if mode=='+': return not any(p[i] for i in MINUS)
    if mode=='-': return not any(p[i] for i in PLUS)
    return survive(p)

def specialize(v,mode): return {(j,p):a for (j,p),a in v.items() if legal(p,mode)}
def apply(F,v,mode='R'):
    out={}
    for (s,p),a in v.items(): out=add(out,mul(F.get(s,{}),p,a,mode))
    return out

def unit(s,c=1): return {(s,ZERO):c}

def degree(w): return sum(map(len,w))
def weight(w): return mon(*(i for block in w for i in block))

def words(n,first=None):
    if n==0: return [()]
    ans=[]
    for side in (0,1):
        if first is not None and side!=first: continue
        for k in range(1,min(3,n)+1):
            for block in combinations((MINUS,PLUS)[side],k):
                for tail in words(n-k,1-side): ans.append((block,)+tail)
    return ans

def resolution(nmax=4):
    levels=[words(n) for n in range(nmax+1)]
    st=[w for lev in levels for w in lev]
    d={w:{} for w in st}
    for w in st:
        if not w: continue
        block=w[0]
        for j,i in enumerate(block):
            rem=block[:j]+block[j+1:]
            target=((rem,)+w[1:]) if rem else w[1:]
            put(d[w],(target,mon(i)),(-1)**j)
    check([len(lev) for lev in levels]==[1,6,24,92,354],'conductor_resolution_ranks')
    for w in st:
        check(not apply(d,d[w]),'conductor_resolution_d_squared',w)
        for (v,p),a in d[w].items():
            check(degree(v)==degree(w)-1,'conductor_resolution_degree')
            check(plus(weight(v),p)==weight(w),'conductor_resolution_weight')
    return levels,st,d

def contract(v):
    """A-linear contracting homotopy of the augmented resolution."""
    out={}
    for (w,p),a in v.items():
        support=[i for i in range(6) if p[i]]
        if not support: continue
        side=0 if support[0] in MINUS else 1
        fside=None if not w else (0 if w[0][0] in MINUS else 1)
        if fside!=side:
            i=min(support); q=list(p); q[i]-=1
            put(out,(((i,),)+w,tuple(q)),a)
        else:
            i=min(support+list(w[0]))
            if i in w[0]: continue
            q=list(p);q[i]-=1
            sign=(-1)**sum(j<i for j in w[0])
            put(out,((tuple(sorted(w[0]+(i,))),)+w[1:],tuple(q)),sign*a)
    return out

def verify_contraction(levels,d):
    coeffs={ZERO}
    for n in (1,2):
        for side in (MINUS,PLUS):
            for inds in product(side,repeat=n): coeffs.add(mon(*inds))
    for i in range(6):
        for n in (3,5): coeffs.add(mon(*([i]*n)))
    for w in [w for lev in levels[:4] for w in lev]:
        for p in sorted(coeffs):
            v={(w,p):1}
            # The formula also has arbitrary A coefficients; these commute.
            ans=add(apply(d,contract(v)),contract(apply(d,v)))
            target={} if not w and not any(p[:6]) else v
            check(ans==target,'resolution_A_linear_contraction',(w,p))

def ten_state_target():
    st=('p03','p25','g','h03','h25','p03k','p25k','gk','h03k','h25k')
    deg={s:(2 if s in ('p03','p25') else 4 if s in ('gk','h03k','h25k') else 3) for s in st}
    d={s:{} for s in st}
    d['g']={('p03',mon(7)):1,('p25',mon(9)):1}
    d['h03']={('p03',mon(BETA,7)):1}
    d['h25']={('p25',mon(BETA,9)):1}
    d['p03k']={('p03',mon(Z)):1};d['p25k']={('p25',mon(Z)):1}
    for s in ('g','h03','h25'):
        d[s+'k']={(t+'k',p):a for (t,p),a in d[s].items()}
        put(d[s+'k'],(s,mon(Z)),-1)
    for s in st:
        check(not apply(d,d[s]),'full_trace_target_d_squared',s)
        check(all(deg[t]==deg[s]-1 for t,p in d[s]),'full_trace_target_degree',s)
    xi={('h03',ZERO):1,('h25',ZERO):1,('g',mon(BETA)):-1}
    xik={('h03k',ZERO):1,('h25k',ZERO):1,('gk',mon(BETA)):-1}
    check(not apply(d,xi),'complete_interval_cycle')
    check(apply(d,xik)==mul(xi,mon(Z),-1),'occurrence_interval_boundary')
    q={s:{} for s in st};q['g']=unit('e0');q['gk']=unit('e1')
    od={'e0':{},'e1':{('e0',mon(Z)):-1}}
    for s in st: check(apply(od,q[s])==apply(q,d[s]),'actual_relative_endpoint_quotient',s)
    endpoints=set(st)-{'g','gk'}
    kappa={s:{(t,p):a for (t,p),a in d[s].items() if t in endpoints} for s in ('g','gk')}
    return st,deg,d,xi,xik,q,od,endpoints,kappa

def delta(F,ds,dt,offset=0,mode='R'):
    return {s:add(apply(dt,F.get(s,{}),mode),apply(F,ds[s],mode),-((-1)**offset)) for s in ds}

def traces(st,ds,dt,xi,xik):
    E={s:{} for s in st};RR={s:{} for s in st}
    HE={s:{} for s in st};HR={s:{} for s in st}
    HE[()]=xi;HR[()]=xi;HR[((Z,),)]=xik
    for i in PLUS:
        E[((i,),)]=mul(xi,mon(i))
        if i!=Z: RR[((i,),)]=mul(xi,mon(i))
    for i in PLUS:
        if i!=Z: RR[((i,Z),)]=mul(xik,mon(i))
    for name,F in (('E',E),('R',RR)):
        DD=delta(F,ds,dt)
        for s in st: check(not DD[s],'complete_resolved_trace_equation',(name,s))
    for F,H,name in ((E,HE,'E'),(RR,HR,'R')):
        D=delta(H,ds,dt,1,'+')
        for s in st:
            check(D[s]==specialize(F[s],'+'),'normalization_positive_homotopy',(name,s))
            check(not specialize(F[s],'-'),'negative_sheet_trace_zero',(name,s))
    U={s:{} for s in st};U[((Z,),)]=mul(xik,ZERO,-1)
    diff={s:add(E[s],RR[s],-1) for s in st}
    dU=delta(U,ds,dt,1)
    rel={s:add(diff[s],dU[s],-1) for s in st}
    expected={s:{} for s in st}
    for i in MINUS: expected[((i,),(Z,))]=mul(xik,mon(i))
    check(rel==expected,'relation_only_difference_full_source_columns')
    for s,v in delta(rel,ds,dt).items():check(not v,'relation_only_cocycle',s)
    return E,RR,HE,HR,U,rel

def normalization_fibre(dt,deg):
    labels=('G','-','+')
    d={(tag,s):{} for tag in labels for s in dt}
    dg={(tag,s):deg[s]-int(tag!='G') for tag,s in d}
    for s in dt:
        for (t,p),a in dt[s].items():
            put(d['G',s],(('G',t),p),a)
            for tag in ('-','+'):
                if legal(p,tag):put(d[tag,s],((tag,t),p),-a)
        for tag in ('-','+'):put(d['G',s],((tag,s),ZERO),1)
    def napply(F,v):
        out={}
        for (s,p),a in v.items():
            for (t,q),b in F.get(s,{}).items():
                r=plus(p,q)
                mode=t[0] if t[0] in ('-','+') else 'R'
                if legal(r,mode): put(out,(t,r),a*b)
        return out
    for s in d:
        check(not napply(d,d[s]),'normalization_fibre_d_squared',s)
        check(all(dg[t]==dg[s]-1 for t,p in d[s]),'normalization_fibre_degree',s)
    return d,dg,napply

def normalized_readout(st,ds,dt,deg,q,E,RR,HE,HR,rel,xik):
    nd,ng,napply=normalization_fibre(dt,deg)
    rho={s:{} for s in nd}
    for tag,s in nd:
        if tag=='G':continue
        for (j,p),a in q[s].items():put(rho[tag,s],(j,p),a*(1 if tag=='+' else -1))
    # Target A e0[2] plus A L_z e1[3], with zero differential.
    for s in nd:
        check(not apply(rho,nd[s],'A'),'conductor_relative_projection_chain',s)
    lifts={};readouts={}
    for name,F,H in (('E',E,HE),('R',RR,HR)):
        L={s:{} for s in st}
        for s in st:
            for (j,p),a in F[s].items():put(L[s],(('G',j),p),a)
            for (j,p),a in H[s].items():
                if legal(p,'+'):put(L[s],(('+',j),p),a)
            check(napply(nd,L[s])==napply(L,ds[s]),'normalized_full_trace_chain',(name,s))
        lifts[name]=L
        out={s:apply(rho,L[s],'A') for s in st};readouts[name]=out
    expectedE={s:{} for s in st};expectedR={s:{} for s in st}
    expectedE[()]={('e0',mon(BETA)):-1}
    expectedR[()]={('e0',mon(BETA)):-1}
    expectedR[((Z,),)]={('e1',mon(BETA)):-1}
    check(readouts['E']==expectedE,'first_grade_trace_E_exact')
    check(readouts['R']==expectedR,'first_grade_trace_R_exact')
    difference={s:add(readouts['E'][s],readouts['R'][s],-1) for s in st}
    expected={s:{} for s in st};expected[((Z,),)]={('e1',mon(BETA)):1}
    check(difference==expected,'conormal_difference_beta_e35_dual')
    # Residual relation-only map has a negative-sheet homotopy e_z -> xi*k.
    HK={s:{} for s in st};HK[((Z,),)]=xik
    for s,v in delta(HK,ds,dt,1,'-').items():
        check(v==specialize(rel[s],'-'),'relation_only_negative_normalization_homotopy',s)
    LR={s:{} for s in st}
    for s in st:
        for (j,p),a in rel[s].items():put(LR[s],(('G',j),p),a)
        for (j,p),a in HK[s].items():
            if legal(p,'-'):put(LR[s],(('-',j),p),a)
    check({s:apply(rho,LR[s],'A') for s in st}==expected,
          'relation_only_and_trace_difference_same_conormal_class')
    return nd,rho,lifts,readouts,difference

def rank(rows):
    if not rows:return 0
    a=[[Fraction(x) for x in r] for r in rows]
    m=len(a);n=len(a[0]);r=0
    for c in range(n):
        p=next((j for j in range(r,m) if a[j][c]),None)
        if p is None:continue
        a[r],a[p]=a[p],a[r];v=a[r][c];a[r]=[x/v for x in a[r]]
        for j in range(r+1,m):
            if a[j][c]:
                v=a[j][c];a[j]=[x-v*y for x,y in zip(a[j],a[r])]
        r+=1
        if r==m:break
    return r

def solve_columns(cols,rhs):
    keys=sorted(set(rhs)|{key for c in cols for key in c},key=repr)
    if not cols:
        check(not rhs,'empty_chain_lift_solvable');return []
    mat=[[Fraction(c.get(key,0)) for c in cols]+[Fraction(rhs.get(key,0))] for key in keys]
    n=len(cols);piv=[];r=0
    for c in range(n):
        p=next((j for j in range(r,len(mat)) if mat[j][c]),None)
        if p is None:continue
        mat[r],mat[p]=mat[p],mat[r];v=mat[r][c];mat[r]=[a/v for a in mat[r]]
        for j in range(len(mat)):
            if j!=r and mat[j][c]:
                v=mat[j][c];mat[j]=[a-v*b for a,b in zip(mat[j],mat[r])]
        piv.append(c);r+=1
        if r==len(mat):break
    check(all(any(row[:n]) or not row[n] for row in mat),'Yoneda_chain_lift_consistent')
    ans=[Fraction(0)]*n
    for j,c in enumerate(piv):ans[c]=mat[j][-1]
    check(all(v.denominator==1 for v in ans),'Yoneda_chain_lift_integral')
    out={}
    for col,v in zip(cols,ans):out=add(out,col,int(v))
    check(out==rhs,'Yoneda_chain_lift_verified')
    return list(map(int,ans))

def yoneda_products(levels,ds):
    lifts=[]
    for i in range(6):
        phi={():{}}
        for n in (1,2,3):
            for w in levels[n]:
                if n==1:
                    phi[w]=unit(()) if w==((i,),) else {}
                else:
                    wt=list(weight(w));wt[i]-=1
                    allowed=[u for u in levels[n-1] if weight(u)==tuple(wt)] if min(wt)>=0 else []
                    rhs=apply(phi,ds[w]);rhs={k:-a for k,a in rhs.items()}
                    ans=solve_columns([ds[u] for u in allowed],rhs)
                    phi[w]={(u,ZERO):a for u,a in zip(allowed,ans) if a}
                check(not add(apply(ds,phi[w]),apply(phi,ds[w])),
                      'Yoneda_degree_minus_one_chain_lift',(i,w))
        lifts.append(phi)
    pairs={}
    for a,b in product(range(6),repeat=2):
        f={}
        for w in levels[2]:
            v=lifts[b][w].get((((a,),),ZERO),0)
            if v:f[w]=v
        pairs[a,b]=f
    rows=[[pairs[a,b].get(w,0) for a,b in product(range(6),repeat=2)] for w in levels[2]]
    check(rank(rows)==24,'all_pair_products_rank_24')
    for i in range(6):check(not pairs[i,i],'conormal_square_zero',i)
    for side in (MINUS,PLUS):
        for i,j in combinations(side,2):
            check(add(pairs[i,j],pairs[j,i])=={},'same_sheet_anticommutator', (i,j))
            check(len(pairs[i,j])==1 and set(pairs[i,j].values())<={1,-1},
                  'same_sheet_distinct_product_primitive',(i,j))
    for a in MINUS:
        for b in PLUS:
            check(pairs[a,b]=={((a,),(b,)):-1},'ordered_mixed_product_minus_dual',(a,b))
            check(pairs[b,a]=={((b,),(a,)):-1},'reverse_mixed_product_independent',(a,b))
    chosen=[]
    for w in levels[2]:
        if len(w)==1:
            i,j=w[0];chosen.append((j,i))
        else:chosen.append((w[0][0],w[1][0]))
    minor=[[pairs[a,b].get(w,0) for a,b in chosen] for w in levels[2]]
    check(all(minor[i][j]==(minor[i][i] if i==j else 0) for i in range(24) for j in range(24)),
          'pair_product_unimodular_minor_diagonal')
    check(all(abs(minor[i][i])==1 for i in range(24)),'pair_product_unit_minor')
    # The twelve independent quadratic relations are complete by unit rank.
    relation_cols=[]
    pp=list(product(range(6),repeat=2))
    for i in range(6):relation_cols.append([int(p==(i,i)) for p in pp])
    for side in (MINUS,PLUS):
        for i,j in combinations(side,2):relation_cols.append([int(p in ((i,j),(j,i))) for p in pp])
    check(rank([list(r) for r in zip(*relation_cols)])==12,'quadratic_relation_kernel_rank_12')
    for c in relation_cols:check(all(sum(a*b for a,b in zip(row,c))==0 for row in rows),'all_quadratic_relations_in_kernel')
    fixed=[[pairs[a,Z].get(w,0) for a in range(6)] for w in levels[2]]
    check(rank(fixed)==5,'continuation_by_fixed_35_has_five_obstructions')
    check(all(row[Z]==0 for row in fixed),'same_35_continuation_kernel')
    # Degree-three checks verify that the computed quadratic table is coherent
    # on all 92 relations among relations.
    triples={}
    for a,b,c in product(range(6),repeat=3):
        f={}
        for w in levels[3]:
            vv=apply(lifts[b],lifts[c][w])
            val=vv.get((((a,),),ZERO),0)
            if val:f[w]=val
        triples[a,b,c]=f
    for i,a in product(range(6),repeat=2):
        check(not triples[i,i,a] and not triples[a,i,i],'squared_generator_relations_in_degree_three',(i,a))
    for side in (MINUS,PLUS):
        for i,j in combinations(side,2):
            for a in range(6):
                check(not add(triples[i,j,a],triples[j,i,a]),'left_quadratic_relation_degree_three',(i,j,a))
                check(not add(triples[a,i,j],triples[a,j,i]),'right_quadratic_relation_degree_three',(i,j,a))
    trows=[[triples[p].get(w,0) for p in product(range(6),repeat=3)] for w in levels[3]]
    check(rank(trows)==92,'degree_three_products_rank_92')
    return lifts,pairs,triples,rows,fixed

def small_linear_maps():
    # Matrices are column maps over A, with polynomial coefficients.
    def compose(A,B):return {j:apply(A,v) for j,v in B.items()}
    zero2={0:{},1:{}}
    zact={0:{(1,mon(BETA)):1},1:{}}
    actions={i:(zact if i==Z else zero2) for i in range(6)}
    for i,j in product(range(6),repeat=2):
        check(compose(actions[i],actions[j])==compose(actions[j],actions[i]),'rank_two_extension_commuting_actions',(i,j))
        if (i in MINUS)!=(j in MINUS):check(all(not v for v in compose(actions[i],actions[j]).values()),'rank_two_extension_mixed_products_zero',(i,j))
    check(all(not v for v in compose(zact,zact).values()),'rank_two_extension_z_squared_zero')
    # The unit lift u maps under e_z differential to beta*v, exactly the
    # connecting cocycle recovered from the normalization of the trace pair.
    cocycle={i:actions[i][0] for i in range(6)}
    check(cocycle[Z]=={(1,mon(BETA)):1} and all(not cocycle[i] for i in range(5)),
          'extension_connecting_cocycle_beta_e35_dual')
    # Arbitrary quotient lift u+c*v cannot change z(u+c*v)=beta*v.
    check(not zact[1],'splitting_change_cannot_change_conormal_coefficient')
    # Same-direction two-step continuation, with both raw coefficients beta.
    J={0:{(1,mon(BETA)):1},1:{(2,mon(BETA)):1},2:{}}
    JJ=compose(J,J);JJJ=compose(J,JJ)
    check(JJ[0]=={(2,mon(BETA,BETA)):1} and all(not v for v in JJJ.values()),
          'same_direction_length_three_module')
    # Opposite direction continuation. The mixed product acts by beta^2 on
    # the top-to-bottom entry, forbidden by R's actual relation X04*X35=0.
    Az={0:{(1,mon(BETA)):1},1:{},2:{}}
    Ay={0:{},1:{(2,mon(BETA)):1},2:{}}
    bad=compose(Ay,Az)
    check(bad[0]=={(2,mon(BETA,BETA)):1},'reflected_direction_quadratic_defect_beta_squared')
    check(compose(Az,Ay)!={j:bad[j] for j in bad},'mixed_direction_commutator_detected')
    # The first and second infinitesimal neighborhoods retain 1+6 and
    # 1+6+12 monomials; none of the nine mixed monomials is admitted.
    jets=[]
    for cap in (1,2,3):
        basis={ZERO}
        for n in range(1,cap+1):
            for side in (MINUS,PLUS):
                for inds in product(side,repeat=n):basis.add(mon(*inds))
        jets.append(sorted(basis))
    check([len(b) for b in jets]==[7,19,39],'conductor_infinitesimal_neighborhood_ranks')
    return {'rank_two_z_action':zact,'rank_three_same_z_action':J,
            'rank_three_mixed_z_action':Az,'rank_three_mixed_04_action':Ay,
            'mixed_product_defect':bad,'jet_basis_ranks':[7,19,39]}

def serialize_vec(v):return [[j,list(p),a] for (j,p),a in sorted(v.items(),key=lambda kv:repr(kv[0]))]
def serialize_map(F):return [[s,serialize_vec(v)] for s,v in F.items()]
def serialize_functional(F):return [[w,a] for w,a in F.items()]


# ---------------------------------------------------------------------------
# New calculations.  Exterior blocks are normal forms in the associative
# free product of the two exterior algebras.  This is an operation algebra,
# not a ring of occurrence coefficients.

def eword(seq):
    blocks=[]; sign=1
    for i in seq:
        side=0 if i in MINUS else 1
        if blocks and (0 if blocks[-1][0] in MINUS else 1)==side:
            block=blocks[-1]
            if i in block: return None,0
            sign*=(-1)**sum(j>i for j in block)
            blocks[-1]=tuple(sorted(block+(i,)))
        else: blocks.append((i,))
    return tuple(blocks),sign

def eletter(i): return {((i,),):1}

def emul(v,w):
    out={}
    for a,ca in v.items():
        for b,cb in w.items():
            seq=tuple(i for block in a+b for i in block)
            key,s=eword(seq)
            if s:put(out,key,ca*cb*s)
    return out

def escale(v,c): return {k:c*a for k,a in v.items() if c*a}

def edegree(v):
    ds={degree(w) for w in v}
    if len(ds)!=1: raise ValueError('Expected nonzero homogeneous operation')
    return next(iter(ds))

def bracket(v,w):
    if not v or not w:return {}
    return add(emul(v,w),emul(w,v),-(-1)**(edegree(v)*edegree(w)))

def eact(v,perm):
    out={}
    for w,c in v.items():
        key,s=eword(tuple(perm[i] for b in w for i in b))
        if s: put(out,key,c*s)
    return out

def coproduct(v):
    out={}
    for w,c in v.items():
        seq=tuple(i for b in w for i in b); n=len(seq)
        for mask in range(1<<n):
            left=tuple(seq[i] for i in range(n) if mask>>i&1)
            right=tuple(seq[i] for i in range(n) if not(mask>>i&1))
            l,sl=eword(left);r,sr=eword(right)
            inv=sum(not(mask>>i&1) and (mask>>j&1) for i in range(n) for j in range(i+1,n))
            if sl*sr:put(out,(l,r),c*sl*sr*(-1)**inv)
    return out

def exterior_image(v):
    out={}
    for w,c in v.items():
        seq=tuple(i for b in w for i in b)
        if len(set(seq))<len(seq):continue
        inv=sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))
        put(out,tuple(sorted(seq)),c*(-1)**inv)
    return out

def relative_generators():
    gs={}
    for p in range(1,4):
        for I in combinations(MINUS,p):
            for q in range(1,4):
                for J in combinations(PLUS,q):
                    val=bracket(eletter(I[0]),eletter(J[0]))
                    for i in I[1:]:val=bracket(eletter(i),val)
                    for j in J[1:]:val=bracket(eletter(j),val)
                    gs[(I,J)]=val
    counts=Counter(edegree(v) for v in gs.values())
    check(dict(sorted(counts.items()))=={2:9,3:18,4:15,5:6,6:1},'relative_primitive_counts')
    for k,v in gs.items():
        expected={}
        for w,c in v.items():put(expected,(w,()),c);put(expected,((),w),c)
        check(coproduct(v)==expected,'all_49_generators_primitive',k)
        check(not exterior_image(v),'all_49_generators_exterior_quotient_zero',k)
    return gs

def sparse_basis(columns):
    """Echelon reduction over Q, retaining coordinates in the input basis."""
    piv={}
    for idx,col in enumerate(columns):
        v={k:Fraction(a) for k,a in col.items()};coord={idx:Fraction(1)}
        while v:
            r=min(v)
            if r not in piv:
                c=v[r];check(abs(c)==1,'relative_word_basis_unit_pivot',idx)
                v={k:a/c for k,a in v.items()};coord={k:a/c for k,a in coord.items()}
                piv[r]=(v,coord);break
            row,coeff=piv[r];c=v[r]
            v=add(v,row,-c);coord=add(coord,coeff,-c)
        check(bool(v),'relative_word_basis_independent',idx)
    def read(col):
        v={k:Fraction(a) for k,a in col.items()};ans={}
        while v:
            r=min(v)
            check(r in piv,'relative_action_lies_in_generated_algebra',r)
            row,coord=piv[r];c=v[r];v=add(v,row,-c);ans=add(ans,coord,c)
        check(all(a.denominator==1 for a in ans.values()),'relative_action_integral')
        return {k:int(a) for k,a in ans.items()}
    return read

def operation_calculation():
    gs=relative_generators(); keys=list(gs); degs={k:edegree(v) for k,v in gs.items()}
    # Actual hexagon relabellings on the declared ordered short labels.
    labelpairs=[tuple(map(int,s)) for s in SHORT]
    def perm_vertices(fn):
        return {i:labelpairs.index(tuple(sorted((fn(p[0])%6,fn(p[1])%6)))) for i,p in enumerate(labelpairs)}
    rot=perm_vertices(lambda v:v+1);ref=perm_vertices(lambda v:3-v)
    check([SHORT[rot[i]] for i in range(6)]==['13','15','35','24','02','04'],'rotation_label_dictionary')
    check([SHORT[ref[i]] for i in range(6)]==['13','35','15','02','24','04'],'reflection_label_dictionary')
    actions={}
    # Relative-word bases are used only through operation degree six.  This
    # verifies all 49 generator transports, including decomposables.
    relwords={0:[()]}
    expansions={():{():1}}
    for n in range(1,7):
        relwords[n]=[]
        for k in keys:
            d=degs[k]
            if d>n:continue
            for tail in relwords[n-d]:
                w=(k,)+tail
                relwords[n].append(w)
                expansions[w]=emul(gs[k],expansions[tail])
    check([len(relwords[n]) for n in range(2,7)]==[9,18,96,330,1324],'relative_word_counts_through_six')
    for n in range(2,7):
        bw=relwords[n]; read=sparse_basis([expansions[w] for w in bw])
        for k in keys:
            if degs[k]!=n:continue
            for name,perm in [('rotation',rot),('reflection',ref)]:
                actual=eact(gs[k],perm); coeff=read(actual)
                recon={}
                for j,c in coeff.items():recon=add(recon,expansions[bw[j]],c)
                check(recon==actual,'full_decomposable_symmetry_reconstruction',(name,k))
                actions[(name,k)]=[(bw[j],c) for j,c in sorted(coeff.items())]
    for k,v in gs.items():
        a=v
        for _ in range(6):a=eact(a,rot)
        check(a==v,'relative_rotation_sixth_power',k)
        check(eact(eact(v,ref),ref)==v,'relative_reflection_square',k)
        lhs=eact(eact(eact(v,ref),rot),ref);rhs=v
        for _ in range(5):rhs=eact(rhs,rot)
        check(lhs==rhs,'relative_dihedral_relation',k)
    decomposable=[(name,k,v) for (name,k),v in actions.items() if any(len(w)>1 for w,c in v)]
    check(bool(decomposable),'decomposable_symmetry_terms_required')
    rgs={k:v for k,v in gs.items() if degs[k]==2}
    a35=eletter(Z)
    acted=[emul(v,a35) for v in rgs.values()]
    comm=[bracket(v,a35) for v in rgs.values()]
    def sparse_rank(cols):
        rows=sorted(set().union(*(set(c) for c in cols)))
        return rank([[c.get(r,0) for c in cols] for r in rows])
    check(sparse_rank(acted)==9,'all_nine_relative_quadratics_act_independently_on_e35')
    check(sparse_rank(comm)==6,'quadratic_centrality_defect_rank_six')
    for (I,J),v in rgs.items():
        a,b=I[0],J[0]
        check(emul(v,eletter(a))==emul(emul(eletter(a),eletter(b)),eletter(a)), 'negative_endpoint_action_identity',(a,b))
        check(emul(v,eletter(b))==emul(emul(eletter(b),eletter(a)),eletter(b)), 'positive_endpoint_action_identity',(a,b))
        check(bool(emul(v,eletter(a))) and bool(emul(v,eletter(b))),'both_endpoint_operation_actions_nonzero',(a,b))
    oa=emul(eletter(1),a35); ob=emul(a35,eletter(1));rr=add(oa,ob)
    check(bool(exterior_image(oa)),'ordered_mixed_obstruction_not_in_hopf_kernel')
    check(not exterior_image(rr),'symmetric_mixed_sum_in_relative_kernel')
    # Multiplication is associative on all letters and all displayed relative
    # generators; this also fixes the meaning of their transported products.
    for a,b,c in product(range(6),repeat=3):
        check(emul(emul(eletter(a),eletter(b)),eletter(c))==emul(eletter(a),emul(eletter(b),eletter(c))), 'operation_associativity_letters')
    higher={}
    for n in range(2,7):
        vals=[emul(v,a35) for k,v in gs.items() if degs[k]==n]
        higher[n]={'generator_count':len(vals),'right_action_rank':sparse_rank(vals)}
    return gs,actions,rot,ref,{'relative_counts':dict(sorted(Counter(degs.values()).items())),
      'relative_word_counts':[len(relwords[n]) for n in range(7)],
      'quadratic_action_rank':9,'centrality_defect_rank':6,
      'higher_actions':higher,'sample_decomposable':decomposable[0]}

# Ordinary graded module enlargements. Each action lowers the displayed
# filtration, but has cohomological degree zero. Normal-line and regulator
# shifts are checked separately, rather than turned into homological shifts.
def compose_maps(F,G):return {s:apply(F,v) for s,v in G.items()}

def module_checks():
    def zero(n):return {j:{} for j in range(n)}
    def actions(n,entries):
        out={i:zero(n) for i in range(6)}
        for i,src,tgt,c,p in entries:put(out[i][src],(tgt,p),c)
        return out
    def validate(M,n,name):
        for i,j in product(range(6),repeat=2):
            ij=compose_maps(M[i],M[j]);ji=compose_maps(M[j],M[i])
            check(ij==ji,name+'_commutative',(i,j))
            if (i in MINUS)!=(j in MINUS):check(not any(ij.values()),name+'_mixed_relations',(i,j))
    bp=mon(BETA)
    E=actions(2,[(Z,0,1,1,bp)]);validate(E,2,'rank_two_extension')
    # Pullback along scalar -beta. It has no rank-one source substitute.
    P=actions(2,[(Z,0,1,-1,mon(BETA,BETA))]);validate(P,2,'scalar_pullback_source')
    f={0:{(0,bp):-1},1:unit(1)}
    for i in range(6):check(compose_maps(E[i],f)==compose_maps(f,P[i]),'pullback_source_map_R_linearity',i)
    # One ordered mixed continuation: u -> v+c -> w, the two intermediate
    # states have the SAME 35 normal line. Neither mixed monomial is restored.
    O=actions(4,[(Z,0,1,1,bp),(Z,0,2,1,bp),(1,1,3,1,bp),(1,2,3,-1,bp)])
    validate(O,4,'ordered_compensated_module')
    check(compose_maps(O[1],O[Z])[0]=={},'ordered_two_path_cancellation')
    # Exact prescribed first extension is a quotient, not a subquotient
    # assertion based just on ranks.
    proj={0:unit(0),1:unit(1),2:{},3:{}}
    for i in range(6):check(compose_maps(E[i],proj)==compose_maps(proj,O[i]),'ordered_module_quotient_is_original_extension',i)
    # Reflection closed, with distinct 35 and 04 normal lines. Six A-basis
    # states: u,v35,c35,v04,c04,w. Four middle states, not a falsely merged
    # compensator of two different occurrence weights.
    S=actions(6,[(Z,0,1,1,bp),(Z,0,2,1,bp),(1,0,3,1,bp),(1,0,4,1,bp),
       (1,1,5,1,bp),(1,2,5,-1,bp),(Z,3,5,1,bp),(Z,4,5,-1,bp)])
    validate(S,6,'reflection_closed_compensated_module')
    perm={0:0,1:3,2:4,3:1,4:2,5:5};J={i:unit(perm[i]) for i in range(6)}
    check(compose_maps(J,J)=={i:unit(i) for i in range(6)},'compensated_reflection_square')
    for i,j in [(Z,1),(1,Z)]:check(compose_maps(J,S[i])==compose_maps(S[j],J),'compensated_reflection_intertwiner',(i,j))
    # Normal weight convention: variable Xi has occurrence +ei and beta
    # degree +1; a first-layer vector has (ei,-1).
    ow=[(ZERO[:6],0),(mon(Z)[:6],-1),(mon(Z)[:6],-1),
        (mon(1)[:6],-1),(mon(1)[:6],-1),(mon(1,Z)[:6],-2)]
    for i,F in S.items():
        for src,v in F.items():
            for (tgt,p),c in v.items():
                left=tuple(ow[src][0][j]+int(j==i) for j in range(6))
                right=tuple(ow[tgt][0][j]+p[j] for j in range(6))
                check(left==right and ow[src][1]==ow[tgt][1]+p[BETA],'all_compensated_module_occurrence_regulator_degrees',(i,src,tgt))
    # Ordinary normalization restrictions and their Tor connecting rows.
    check(E[Z][0]=={(1,bp):1},'minus_branch_Tor_connecting_e35_beta')
    check(all(not E[i][0] for i in MINUS),'plus_branch_Tor_connecting_zero')
    # Square-zero shear describes automorphisms fixing the two graded pieces.
    N={0:unit(1),1:{}}
    check(not any(compose_maps(N,N).values()),'extension_shear_nilpotent')
    for i in range(6):check(compose_maps(N,E[i])==compose_maps(E[i],N),'ungraded_extension_shears_commute',i)
    return {'E_beta35':serialize_map(E[Z]),'scalar_minus_beta_pullback':serialize_map(P[Z]),
      'ordered_compensation':[[SHORT[i],serialize_map(F)] for i,F in O.items()],
      'reflection_closed_compensation':[[SHORT[i],serialize_map(F)] for i,F in S.items()],
      'reflection_matrix':serialize_map(J),'basis_weights':ow,
      'normalization_restriction_H0_plus':'E_beta35',
      'normalization_restriction_H0_minus':'A*u direct_sum (A/beta)*v',
      'opposite_branch_Tor_boundary':['0','0','beta'],
      'minimal_ordered_middle_rank':2,'minimal_paired_middle_rank_under_labelled_conditions':4}

# A finite ambient resolution of the nonsplit relative dualizing object.
def ambient_duality_checks():
    levels=[[('unit',)]]
    for n in range(1,6):
        levels.append([(I,J) for p in range(1,4) for I in combinations(MINUS,p)
                       for q in range(1,4) for J in combinations(PLUS,q) if p+q==n+1])
    st=sum(levels,[]);d={s:{} for s in st}
    for n in range(1,6):
        for s in levels[n]:
            I,J=s
            if n==1:d[s]={(('unit',),mon(I[0],J[0])):1};continue
            if len(I)>1:
                for k,i in enumerate(I):put(d[s],((I[:k]+I[k+1:],J),mon(i)),(-1)**k)
            if len(J)>1:
                for k,j in enumerate(J):put(d[s],((I,J[:k]+J[k+1:]),mon(j)),(-1)**(len(I)-1+k))
    def ambient_mul(v,p,c=1):return {(j,plus(q,p)):c*a for (j,q),a in v.items() if c*a}
    def ambient_apply(F,v):
        out={}
        for (s,p),a in v.items():out=add(out,ambient_mul(F.get(s,{}),p,a))
        return out
    check([len(x) for x in levels]==[1,9,18,15,6,1],'ambient_resolution_fifty_states')
    for s in st:check(not ambient_apply(d,d[s]),'ambient_mixed_ideal_resolution_d_squared',s)
    dual={s:{} for s in st}
    deg={s:n for n,L in enumerate(levels) for s in L}
    for s,col in d.items():
        for (t,p),c in col.items():put(dual[t],(s,p),c*(-1)**(deg[t]+1))
    for s in st:check(not ambient_apply(dual,dual[s]),'complete_dualizing_differential_squared',s)
    # The two components of the primitive dualizing attachment on the
    # ambient conductor Koszul resolution.
    ko=[I for n in range(7) for I in combinations(range(6),n)]
    kd={I:{(I[:k]+I[k+1:],mon(i)):(-1)**k for k,i in enumerate(I)} for I in ko}
    gamma_minus={I:(unit('omega_minus',-1) if I==MINUS else {}) for I in ko}
    gamma_plus={I:(unit('omega_plus') if I==PLUS else {}) for I in ko}
    for I in ko:
        check(not apply(gamma_minus,kd[I],'-'),'negative_branch_dualizing_attachment_closed',I)
        check(not apply(gamma_plus,kd[I],'+'),'positive_branch_dualizing_attachment_closed',I)
    check(gamma_minus[MINUS]==unit('omega_minus',-1) and gamma_plus[PLUS]==unit('omega_plus'), 'dualizing_attaching_coefficients_minus_plus')
    # The finite Koszul-to-sheet Hom differential lies in the short ideal;
    # a unit top coordinate cannot be an exact cochain.
    check(all(any(p[:6]) for col in kd.values() for (_,p) in col),'dualizing_attachment_unit_nonboundary_ideal_test')
    return {'ambient_resolution_degrees':[len(L) for L in levels],
      'ambient_resolution':serialize_map(d),'relative_dualizing_differential':serialize_map(dual),
      'dualizing_homological_degrees':{repr(s):6-deg[s] for s in st},
      'primitive_attachment':{'minus':-1,'plus':1},
      'unchanged_dualizing_cohomology_degrees':[-3,-1]}

# A genuinely enlarged target in which a nonzero mixed product is
# nullhomotopic. This does NOT assert a nullhomotopy in the original target.
def universal_cone_check(levels,ds,pairs):
    a,b=1,Z
    cochain=pairs[a,b]
    st=sum(levels,[])
    # C_b = Cone(P_A -> A L04 L35[2]); source P_A has its whole resolution.
    # In homological convention: C_n=B_n + P_(n-1); d(b,p)=(db+f p,-dp).
    states=[('B',0)]+[('P',w) for w in st]
    cd={s:{} for s in states}
    f={w:({(('B',0),mon(BETA,BETA)):cochain[w]} if w in cochain else {}) for w in st}
    for w in st:
        col=dict(f[w])
        for (u,p),c in ds[w].items():put(col,(('P',u),p),-c)
        cd[('P',w)]=col
    # R acts on the B part by augmentation, while the P part is free.
    def cmul(v,p,c=1):
        out={}
        for (s,q),aa in v.items():
            r=plus(p,q)
            if s[0]=='B' and any(r[:6]):continue
            if survive(r):put(out,(s,r),c*aa)
        return out
    def capp(F,v):
        out={}
        for (s,p),c in v.items():out=add(out,cmul(F.get(s,{}),p,c))
        return out
    H={w:{(('P',w),ZERO):1} for w in st}
    for s in states:check(not capp(cd,cd[s]),'universal_obstruction_cofiber_d_squared',s)
    for w in st:
        check(add(capp(cd,H[w]),capp(H,ds[w]))==f[w], 'universal_cofiber_nullhomotopy_equation',w)
    # No such homotopy exists before this enlargement: Hom(P_A,A) has d=0.
    check(bool(cochain) and any(c in (-1,1) for c in cochain.values()), 'original_mixed_class_nonzero_before_cofiber')
    return {'attached_map':'beta^2 eta04 eta35: A -> A L04 L35[2]',
      'cone_differential':serialize_map(cd),'canonical_nullhomotopy':serialize_map(H),
      'source_resolution_truncation_checked':4,
      'scope':'All-degree cone formula; finite check through the displayed source resolution. Not a quasi-isomorphic replacement of the old target.'}

# Rees/occurrence line transport. The determinant is evaluated separately
# from products of Ext operations; this avoids a false reflection-square sign.
def symmetry_line_checks(rot,ref):
    def sgn(seq):return (-1)**sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))
    data={}
    for name,perm in [('rotation',rot),('reflection',ref)]:
        minus=tuple(perm[i] for i in MINUS);plus_=tuple(perm[i] for i in PLUS)
        data[name]={'normal_labels':[SHORT[perm[i]] for i in range(6)],
          'minus_determinant_sign':sgn(minus),'plus_determinant_sign':sgn(plus_),
          'ambient_determinant_sign':sgn(tuple(perm[i] for i in range(6))),
          'polarity_sign':-1 if perm[MINUS[0]] in PLUS else 1,
          'pair_02_35_sign':sgn((perm[0],perm[Z]))}
        check(data[name]['ambient_determinant_sign']==data[name]['minus_determinant_sign']*data[name]['plus_determinant_sign']*(-1 if perm[0] in PLUS else 1),'block_determinant_and_polarity_transport',name)
    check(data['reflection']['minus_determinant_sign']==-1 and data['reflection']['plus_determinant_sign']==-1,'physical_reflection_branch_determinants')
    check(data['rotation']['ambient_determinant_sign']==-1 and data['reflection']['ambient_determinant_sign']==-1,'six_normal_ambient_orientation_signs')
    return data

def new_run(out):
    levels,st,ds=resolution(4);verify_contraction(levels,ds)
    ts,tdg,dt,xi,xik,q,od,ep,kappa=ten_state_target()
    E,RR,HE,HR,U,rel=traces(st,ds,dt,xi,xik)
    nf,rho,nflifts,readouts,diff=normalized_readout(st,ds,dt,tdg,q,E,RR,HE,HR,rel,xik)
    lifts,pairs,triples,cup,fixed=yoneda_products(levels,ds)
    previous_small_controls=small_linear_maps()
    mods=module_checks();dual=ambient_duality_checks();cones=universal_cone_check(levels,ds,pairs)
    gs,actions,rot,ref,ops=operation_calculation();line=symmetry_line_checks(rot,ref)
    ranks=[len(words(n)) for n in range(8)]
    check(ranks[:5]==[1,6,24,92,354],'higher_obstruction_ranks_initial')
    for n in range(4,8):check(ranks[n]==3*ranks[n-1]+3*ranks[n-2]+ranks[n-3],'all_degree_hilbert_recurrence_checked',n)
    cert={'schema':'marici.branchA.physical_collar_conormal_leg.v1',
      'status':'coefficient_two_grade_target_quadratic_obstructions_and_labelled_enlargements_constructed; physical_endpoint_and_Q_assembly_not_certified',
      'scope':{'coefficient_ring':'A=Z[beta,X03,X14,X25]; R=A[X02,X04,X24,X13,X15,X35]/(Iminus Iplus)',
        'derived_source':'Normalized trace diagrams retain their specified branch homotopies; an independently framed physical collar is NOT identified with the ten-state target.',
        'input_Q':'Primitive bare-Q class accepted from task; product-Cartier chain map and determinant interface unavailable in the supplied material.',
        'no_physical_Delta_value':True},
      'normalization_trace_target':{'states':ts,'degrees':tdg,'d':serialize_map(dt)},
      'normalization_maps':{'E':serialize_map(E),'R':serialize_map(RR),'H_E':serialize_map(HE),'H_R':serialize_map(HR),'relation_correction':serialize_map(rel)},
      'normalization_readout':{name:serialize_map(v) for name,v in readouts.items()},
      'normalization_fibre_d':serialize_map(nf),
      'source_resolution':{'ranks':ranks[:5],'d':serialize_map(ds)},
      'quadratic':{'ordered_columns':[[list(k),serialize_functional(v)] for k,v in pairs.items()],
        'fixed_35_matrix':fixed,'unscaled_rank':5,'kernel':'A eta35',
        'image_polynomial_beta':'beta times a primitive free rank-five lattice; cokernel has (A/beta)^5',
        'two_normal_physical_coefficients':'beta^2 times ordered Yoneda product, with L_i tensor L35',
        'same_ring_derived_nullhomotopy':'does not exist for the nonzero mixed product'},
      'higher_ext_ranks':ranks,
      'relative_operation_checks':ops,
      'relative_generators':[[[list(k[0]),list(k[1])],serialize_functional(v)] for k,v in gs.items()],
      'full_relative_symmetry':[[name,[list(k[0]),list(k[1])],[[[[list(a),list(b)] for a,b in w],c] for w,c in val]] for (name,k),val in actions.items()],
      'module_enlargements':mods,'universal_cofiber_enlargement':cones,
      'same_direction_and_obstructed_rank_three_controls':{k:serialize_map(v) if isinstance(v,dict) else v for k,v in previous_small_controls.items()},
      'nonsplit_dualizing_model':dual,'normal_line_symmetry':line,
      'physical_obstructions_not_evaluated':[
        'Endpoint connector morphisms into the upper-shriek duality/conormal target are not provided.',
        'The exact product-Cartier source and bare-Q map are not provided; no auxiliary-factor replacement is made.',
        'No map from the independently framed physical collar into the normalized trace-diagram source is constructed.',
        'The coefficient pairing/duality morphism is not asserted to be the physical Pochhammer-Cousin or conductor-Morse morphism.'
      ],
      'counts':dict(sorted(COUNTS.items()))}
    payload=json.dumps(cert,sort_keys=True,separators=(',',':')).encode();cert['certificate_content_sha256']=sha256(payload).hexdigest()
    out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'status':cert['status'],'exact_checks':sum(COUNTS.values()),'higher_ext_ranks':ranks,
      'mixed_obstruction_rank':5,'relative_quadratic_action_rank':9,'centrality_defect_rank':6,
      'minimal_ordered_module_A_rank':4,'reflection_closed_labelled_module_A_rank':6,
      'certificate_content_sha256':cert['certificate_content_sha256']},sort_keys=True))


# ---------------------------------------------------------------------------
# Matching-Hom audit. The preceding implementation is vendored, not imported
# from an assumed companion file. Physical endpoint arrows are NOT fabricated.

MH_VARS=tuple('X'+s for s in SHORT)+('beta','X03','X14','X25','u03','u14','u25')+tuple('t'+str(i) for i in range(6))
MH_ZERO=(0,)*len(MH_VARS)
MH_SOURCE_ORDER=(0,3,2,5,1,4)  # X0,...,X5 = 02,13,24,35,04,15

def mh_mon(*inds):
    z=[0]*len(MH_VARS)
    for i in inds:z[i]+=1
    return tuple(z)

def mh_vec(s,c=1,p=None):return {(s,MH_ZERO if p is None else p):c} if c else {}

def mh_apply(F,v,mode='S'):
    out={}
    for (s,p),c in v.items():
        for (t,q),a in F.get(s,{}).items():
            z=tuple(x+y for x,y in zip(p,q))
            if mode=='R' and any(z[:3]) and any(z[3:6]):continue
            if mode=='A' and any(z[:6]):continue
            put(out,(t,z),c*a)
    return out

def mh_ser(F):
    return [[repr(s),[[repr(t),list(p),c] for (t,p),c in sorted(v.items(),key=lambda x:repr(x[0]))]] for s,v in F.items()]

def mh_sparse_rank(cols):
    if not cols:return 0
    piv={}
    for col in cols:
        v={r:Fraction(c) for r,c in col.items() if c}
        while v:
            r=min(v,key=repr)
            if r not in piv:
                z=v[r];v={k:c/z for k,c in v.items()};piv[r]=v;break
            v=add(v,piv[r],-v[r])
    return len(piv)

def mh_unit_pivot_rank(cols):
    piv={}
    for col in cols:
        v=dict(col)
        while v:
            r=min(v,key=repr)
            if r not in piv:
                check(abs(v[r])==1,'matching_primitive_image_unit_pivot',r)
                z=v[r];piv[r]={k:c*z for k,c in v.items()};break
            v=add(v,piv[r],-v[r])
    return len(piv)

def mh_q_and_duality():
    qst=('T','h03','h14','h25','p03','p14','p25')
    qdeg={s:3 if s in qst[:4] else 2 for s in qst}
    qd={s:{} for s in qst}
    for i in range(3):
        qd['T'].update(mh_vec(qst[4+i],p=mh_mon(7+i)))
        qd[qst[1+i]]=mh_vec(qst[4+i],p=mh_mon(10+i))
    theta=mh_vec('T',p=mh_mon(10,11,12))
    for i in range(3):theta=add(theta,mh_vec(qst[1+i],-1,mh_mon(7+i,*[10+j for j in range(3) if j!=i])))
    check(not mh_apply(qd,theta),'matching_full_Q_top_cycle')
    # Relative internal weights are fixed by d_Q.  The absolute top line is
    # retained as a formal q_T; it is NOT assigned a physical parity.
    qweights={'T':MH_ZERO}
    for i in range(3):
        a=[0]*len(MH_VARS);a[7+i]=-1;qweights[qst[4+i]]=tuple(a)
        a[10+i]=1;qweights[qst[1+i]]=tuple(a)
    for src,col in qd.items():
        for (dst,p),c in col.items():
            check(plus(qweights[dst],p)==qweights[src],
                  'matching_Q_relative_internal_grading',(src,dst))
    theta_weight=mh_mon(10,11,12)
    for (q,p),c in theta.items():
        check(plus(qweights[q],p)==theta_weight,'matching_Theta_relative_line_degree',q)
    # Four actual maps Q_R -> E_beta,35[3] lift the four conductor
    # truncation columns. Their degree-zero connecting cocycle is zero.
    qlifts=[]
    def e_apply(F,v):
        out={}
        for (src,p),c in v.items():
            for (dst,q),a in F.get(src,{}).items():
                z=list(plus(p,q));short=sum(z[:6])
                if short==0:put(out,(dst,tuple(z)),c*a)
                elif dst=='u' and short==1 and z[Z]==1:
                    z[Z]=0;z[BETA]+=1;put(out,('v',tuple(z)),c*a)
        return out
    for chosen in qst[:4]:
        f={q:(mh_vec('u') if q==chosen else {}) for q in qst}
        for q in qst:
            check(not e_apply(f,qd[q]),'matching_explicit_Q_to_E_chain_lift',(chosen,q))
        qlifts.append({'top_coordinate':chosen,'Q_to_E3':mh_ser(f),
                       'connecting_cocycle':[],'chosen_nullhomotopy':[]})
    # Native fifty-state ambient resolution. This is used over S, not as
    # a falsely strict R-free model of the dualizing complex.
    plevels=[[('unit',)]]
    for n in range(1,6):
        plevels.append([(I,J) for p in range(1,4) for I in combinations(MINUS,p)
                       for q in range(1,4) for J in combinations(PLUS,q) if p+q==n+1])
    pst=sum(plevels,[]);pd={s:{} for s in pst};pdeg={s:n for n,L in enumerate(plevels) for s in L}
    for n in range(1,6):
        for s in plevels[n]:
            I,J=s
            if n==1:pd[s]=mh_vec(('unit',),p=mh_mon(I[0],J[0]));continue
            if len(I)>1:
                for k,i in enumerate(I):put(pd[s],((I[:k]+I[k+1:],J),mh_mon(i)),(-1)**k)
            if len(J)>1:
                for k,j in enumerate(J):put(pd[s],((I,J[:k]+J[k+1:]),mh_mon(j)),(-1)**(len(I)-1+k))
    st=[(p,q) for p in pst for q in qst];d={s:{} for s in st};deg={s:pdeg[s[0]]+qdeg[s[1]] for s in st}
    for p,q in st:
        for (pp,m),c in pd[p].items():put(d[p,q],((pp,q),m),c)
        for (qq,m),c in qd[q].items():put(d[p,q],((p,qq),m),(-1)**pdeg[p]*c)
    for s in st:
        check(not mh_apply(d,d[s]),'matching_350_state_ambient_Q_resolution_d_squared',s)
        check(all(deg[t]==deg[s]-1 for t,m in d[s]),'matching_ambient_Q_total_degree',s)
    hd={s:{} for s in st}
    for s,col in d.items():
        for (t,m),c in col.items():put(hd[t],(s,m),(-1)**(deg[t]+1)*c)
    for s in st:check(not mh_apply(hd,hd[s]),'matching_350_state_duality_Hom_d_squared',s)
    ranks=[sum(deg[s]-8==n for s in st) for n in range(-6,1)]
    check(ranks==[3,31,90,117,78,27,4],'matching_aQ_Hom_ranks')
    top=plevels[5][0];h0=[(top,q) for q in qst[:4]];hminus1=[s for s in st if deg[s]==7]
    incoming={s:hd[s] for s in hminus1}
    # The 24 ambient columns generate each short variable times each row.
    shortcols=[s for s in hminus1 if pdeg[s[0]]==4]
    expected={(q,i) for q in qst[:4] for i in range(6)};actual=set()
    for s in shortcols:
        check(len(hd[s])==1,'matching_top_boundary_single_short_column',s)
        ((t,m),c),=hd[s].items()
        check(abs(c)==1 and sum(m)==1 and any(m[:6]),'matching_top_boundary_primitive_short',s)
        actual.add((t[1],m.index(1)))
    check(actual==expected,'matching_aQ_top_short_boundary_ideal')
    # The three remaining columns are -M_Q^t, with the ordered tensor sign.
    for i in range(3):
        ex=add(mh_vec((top,'T'),-1,mh_mon(7+i)),mh_vec((top,qst[1+i]),-1,mh_mon(10+i)))
        check(hd[top,qst[4+i]]==ex,'matching_aQ_top_three_long_relations',i)
    # Evaluation on theta annihilates the three displayed relations.
    ev={q:mh_vec('scalar',c,m) for (q,m),c in theta.items()}
    for i in range(3):
        v=add(mh_vec('T',p=mh_mon(7+i)),mh_vec(qst[1+i],p=mh_mon(10+i)))
        check(not mh_apply(ev,v),'matching_theta_evaluation_relation',i)
    check(all(sum(m[10:13])>=2 for col in ev.values() for t,m in col),'matching_theta_evaluation_proper_normal_ideal')
    return {'coefficient_variables':MH_VARS,'Q_degrees':qdeg,'Q_differential':mh_ser(qd),'theta':mh_ser({'top':theta}),
      'absolute_Q_top_line':'q_T retained formally; no physical parity assigned',
      'relative_Q_state_internal_weights':{k:list(v) for k,v in qweights.items()},
      'explicit_four_Q_to_E_lifts':qlifts,
      'coefficient_variance':'Hom_S(Q_S,i_*omega[2]) = Hom_R(R tensor_S^L Q_S,omega[2]); both inputs are represented by their complete derived base changes',
      'ambient_Hom_degrees':list(range(-6,1)),'ambient_Hom_ranks':ranks,
      'ambient_Q_resolution':mh_ser(d),'ambient_duality_Hom_differential':mh_ser(hd),
      'H0_boundary_matrix_columns':mh_ser(incoming),'H0_basis':[repr(s) for s in h0],
      'H0_presentation':'coker(M_Q^t:C^3 -> C^4) tensor Pi^vee',
      'H0_evaluation_isomorphism':'(u03*u14*u25, X03*u14*u25, X14*u03*u25, X25*u03*u14) tensor q_Theta^vee tensor Pi^vee',
      'all_aQ_conormal_obstructions_zero':True,
      'reason':'Q is R-perfect in homological degrees 2,3; Hom_R(Q,A L35 Pi^vee[4]) has no degree-zero chains.',
      'aQ_is_physically_selected':False},qd,theta

def mh_koszul_source(qd,theta):
    ks=[I for n in range(8) for I in combinations(range(7),n)]
    results=[]
    for k in (2,3):
      for T in combinations((1,3,5),k):
        eq=[mh_mon(i) for i in MH_SOURCE_ORDER]+[mh_mon(*[13+i for i in T])]
        d={I:{(I[:j]+I[j+1:],eq[i]):(-1)**j for j,i in enumerate(I)} for I in ks}
        for I in ks:
            check(not mh_apply(d,d[I]),'matching_full_seven_equation_Koszul_d_squared',(T,I))
            check(not mh_apply(d,d[I],'R'),'matching_derived_node_basechange_d_squared',(T,I))
        # This is a reconstructed bare-Q representative, NOT a claim to
        # have recovered C's final excess-frame identification.
        q={I:(theta if len(I)==7 else {}) for I in ks}
        for I in ks:check(mh_apply(qd,q[I],'R')==mh_apply(q,d[I],'R'),'matching_bare_Q_top_representative_full_chain_equation',(T,I))
        # Hom_R(K_R[-4],A L35 Pi^vee[3]): 64 exact Cartier pairs.
        hd={I:{} for I in ks}
        for J,col in d.items():
            for (I,m),c in col.items():
                if any(m[:6]):continue
                put(hd[I],(J,m),(-1)**len(I)*c)
        for I in ks:
            ex={} if 6 in I else mh_vec(I+(6,),p=eq[6])
            check(hd[I]==ex,'matching_conormal_Hom_exact_Cartier_column',(T,I))
            check(not mh_apply(hd,hd[I]),'matching_conormal_Hom_d_squared',(T,I))
        # The obstruction target [4] has max cochain degree -1.
        check(max(len(I)-8 for I in ks)==-1,'matching_Koszul_obstruction_has_no_degree_zero_chains',T)
        for eps in (0,1):
            results.append({'T':list(T),'epsilon':eps,'source_order':['X'+SHORT[i] for i in MH_SOURCE_ORDER]+['t_'+'_'.join(map(str,T))],
              'source_homological_shift':-4,'source_ranks':[len([I for I in ks if len(I)==n]) for n in range(8)],
              'Koszul_differential':mh_ser(d),'bare_Q_reconstructed_representative':mh_ser(q),
              'conormal_Hom_degrees':list(range(-7,1)),'conormal_Hom_ranks':[len([I for I in ks if len(I)==n]) for n in range(8)],
              'conormal_Hom_differential':mh_ser(hd),'conormal_Hom_cohomology_ranks_over_C_mod_tT':[1,6,15,20,15,6,1],
              'cohomology_degrees':list(range(-6,1)),
              'line':'F_(T,epsilon)^vee tensor Lambda^(n+6)(N_occ^vee) tensor L_tT^vee tensor L35 tensor Pi^vee',
              'external_excess_line_identification_imported':False,
              'framed_equality_to_C_final_qC_certified':False})
    check(len(results)==8,'matching_eight_supported_Cartier_frames')
    return {'frames':results,'scope':'All seven equations and all 128 columns retained. Final excess-line isomorphism and equality to Branch C final framed representative NOT supplied.'}

def mh_sheet_resolutions():
    out={};levels=[words(n) for n in range(5)]
    for sheet,last in [('+',MINUS),('-',PLUS)]:
        lev=[[()]]+[[w for w in levels[n] if w[-1][0] in last] for n in range(1,5)]
        st=sum(lev,[]);d={w:{} for w in st}
        for w in st:
            if not w:continue
            block=w[0]
            for j,i in enumerate(block):
                rem=block[:j]+block[j+1:];v=((rem,)+w[1:]) if rem else w[1:]
                put(d[w],(v,mon(i)),(-1)**j)
        for w in st:
            check(all(v in d for v,p in d[w]),'matching_sheet_resolution_closed',(sheet,w))
            check(not apply(d,d[w]),'matching_sheet_resolution_d_squared',(sheet,w))
        check([len(L) for L in lev]==[1,3,12,46,177],'matching_sheet_resolution_ranks',sheet)
        # Augmented exactness is proved by the same monomial contraction,
        # leaving a polynomial monomial precisely on the surviving sheet.
        coeffs={ZERO}
        for n in (1,2):
            for side in (MINUS,PLUS):
                for inds in product(side,repeat=n):coeffs.add(mon(*inds))
        for w in sum(lev[:4],[]):
            for p in sorted(coeffs):
                v={(w,p):1}
                def sheet_contract(terms):
                    terms={key:c for key,c in terms.items()
                           if key[0] or any(key[1][i] for i in last)}
                    return contract(terms)
                h=sheet_contract(v)
                check(all(t in d for t,q in h),'matching_sheet_contraction_stays_in_resolution',(sheet,w,p))
                got=add(apply(d,h),sheet_contract(apply(d,v)))
                target={} if not w and not any(p[i] for i in last) else v
                check(got==target,'matching_sheet_augmented_contraction',(sheet,w,p))
        out[sheet]={'degrees':list(range(5)),'ranks':[len(L) for L in lev],'resolution':serialize_map(d),
          'Ext_differential':'zero after Hom_R(-,A); no underived sheet restriction used',
          'upper_shriek_dualizing':'R_'+sheet+' Omega_'+sheet+'[5]',
          'upper_shriek_D':'R_'+sheet+' Omega_'+sheet+'[5] direct_sum RHom_R(R_'+sheet+',A) L35 Pi^vee[3]',
          'scope':'Derived coefficient target. This does NOT identify a physical endpoint source.'}
    return out

def mh_endpoint_operations():
    gs=relative_generators();rgs={k:v for k,v in gs.items() if edegree(v)==2}
    def proj(v,sheet):
        keep=MINUS if sheet=='+' else PLUS
        return {w:c for w,c in v.items() if not w or w[-1][0] in keep}
    data={}
    for sheet in ('+','-'):
        cols=[proj(v,sheet) for v in rgs.values()]
        check(mh_sparse_rank(cols)==9,'matching_nine_native_sheet_unit_actions',sheet)
        pp=[proj(emul(a,b),sheet) for a in rgs.values() for b in rgs.values()]
        check(mh_sparse_rank(pp)==81,'matching_81_quadratic_endpoint_products',sheet)
        deg4=[proj(v,sheet) for v in gs.values() if edegree(v)==4]+pp
        check(mh_sparse_rank(deg4)==96,'matching_degree_four_endpoint_relative_orbit_rank',sheet)
        ranks={}
        for n in range(2,7):
            cs=[proj(v,sheet) for v in gs.values() if edegree(v)==n]
            ranks[n]=mh_sparse_rank(cs)
            check(ranks[n]==len(cs),'matching_all_49_primitive_endpoint_unit_actions',(sheet,n))
        # Closure of the native left-module quotient under actual products.
        for a,b in product(range(6),repeat=2):
            for v in rgs.values():
                l=proj(emul(emul(eletter(a),eletter(b)),v),sheet)
                r=proj(emul(eletter(a),proj(emul(eletter(b),v),sheet)),sheet)
                check(l==r,'matching_native_endpoint_action_associativity',(sheet,a,b))
        powers=[];v={():1};r0=next(iter(rgs.values()))
        for n in range(1,9):
            v=emul(r0,v);pv=proj(v,sheet)
            check(bool(pv) and any(abs(c)==1 for c in pv.values()),'matching_unbounded_relative_orbit_primitive_power',(sheet,n))
            powers.append({'power':n,'terms':serialize_functional(pv)})
        eta_z_unit=proj(eletter(Z),sheet)
        ordered_unit=proj(emul(eletter(1),eletter(Z)),sheet)
        reverse_unit=proj(emul(eletter(Z),eletter(1)),sheet)
        orbit_z=[proj(emul(v,eletter(Z)),sheet) for v in rgs.values()]
        comm_z=[proj(bracket(v,eletter(Z)),sheet) for v in rgs.values()]
        check(bool(eta_z_unit)==(sheet=='-'),'matching_shriek_conormal_unit_direction',sheet)
        check(bool(ordered_unit)==(sheet=='-'),'matching_shriek_ordered_mixed_unit_direction',sheet)
        check(bool(reverse_unit)==(sheet=='+'),'matching_shriek_reverse_mixed_unit_direction',sheet)
        check(mh_sparse_rank(orbit_z)==(0 if sheet=='+' else 9),
              'matching_shriek_nine_actions_on_first_conormal',(sheet,))
        check(mh_sparse_rank(comm_z)==6,'matching_shriek_six_commutator_images',sheet)
        data[sheet]={'quadratic_keys':[repr(k) for k in rgs],
          'eta35_on_canonical_sheet_unit':serialize_functional(eta_z_unit),
          'eta04_eta35_on_canonical_sheet_unit':serialize_functional(ordered_unit),
          'eta35_eta04_on_canonical_sheet_unit':serialize_functional(reverse_unit),
          'nine_r_eta35_unit_columns':[serialize_functional(c) for c in orbit_z],
          'nine_commutator_unit_columns':[serialize_functional(c) for c in comm_z],
          'physical_endpoint_nu_identified_with_sheet_unit':False,
          'quadratic_unit_columns':[serialize_functional(c) for c in cols],
          'quadratic_product_columns':[serialize_functional(c) for c in pp],
          'primitive_action_ranks':ranks,'degree_four_relative_orbit_rank':96,'powers':powers}
    # Check transport on both endpoint quotients, including product columns.
    pairlabels=[tuple(map(int,s)) for s in SHORT]
    rot={i:pairlabels.index(tuple(sorted(((a+1)%6,(b+1)%6)))) for i,(a,b) in enumerate(pairlabels)}
    ref={i:pairlabels.index(tuple(sorted(((3-a)%6,(3-b)%6)))) for i,(a,b) in enumerate(pairlabels)}
    for name,perm in [('r',rot),('f',ref)]:
      for sheet in ('+','-'):
        other='-' if sheet=='+' else '+'
        for v in list(gs.values())+[emul(a,b) for a in rgs.values() for b in rgs.values()]:
            check(eact(proj(v,sheet),perm)==proj(eact(v,perm),other),'matching_endpoint_full_labelled_transport',(name,sheet))
    return {'native_sheet_modules':data,'scope':'Derived Ext_R(R_plus/minus,A) module actions, constructed by comparison with the conductor resolution; not an assumed ordinary-module action on P_phys.'}

def mh_six_state_tests():
    b=('u','v35','c35','v04','c04','w');idx={s:i for i,s in enumerate(b)}
    acts={i:{} for i in range(6)}
    acts[Z]={'u':{'v35':1,'c35':1},'v04':{'w':1},'c04':{'w':-1}}
    acts[1]={'u':{'v04':1,'c04':1},'v35':{'w':1},'c35':{'w':-1}}
    def act(i,v):
        out={}
        for s,c in v.items():
            for t,a in acts[i].get(s,{}).items():put(out,t,c*a)
        return out
    p35={'u':{'u':1},'v35':{'v':1}};p04={'u':{'u':1},'v04':{'v':1}}
    def project(P,v):
        out={}
        for s,c in v.items():
            for t,a in P.get(s,{}).items():put(out,t,c*a)
        return out
    for P,z in [(p35,Z),(p04,1)]:
        for s in b:
            for i in range(6):
                lhs=project(P,act(i,{s:1}));vv=project(P,{s:1});rhs={'v':vv.get('u',0)} if i==z and vv.get('u',0) else {}
                check(lhs==rhs,'matching_six_state_to_E_quotient',(z,s,i))
    a35={'v35':1,'c35':1};a04={'v04':1,'c04':1}
    for a in (a35,a04):
        for i in range(6):check(not act(i,a),'matching_six_state_corrected_middle_conductor_vector')
    check(project(p35,a35)=={'v':1},'matching_six_state_first_conormal_class_lift')
    # No section over the fixed quotient: X04 applied to any lift of u has
    # primitive coefficients +beta on both v04,c04, unaffected by kernel.
    check(act(1,{'u':1}).get('v04')==1,'matching_six_state_no_section_detector_u')
    for s in b[1:]:check(act(1,{s:1}).get('v04',0)==0,'matching_six_state_no_section_detector_kernel')
    # Kernel J6 and its actual conductor Hom matrices; beta is factored out.
    jb=b[1:];levels=[words(n) for n in range(4)]
    dres={}
    for n in range(1,4):
        for w in levels[n]:
            block=w[0];col=[]
            for k,i in enumerate(block):
                rem=block[:k]+block[k+1:];v=((rem,)+w[1:]) if rem else w[1:]
                col.append((v,i,(-1)**k))
            dres[w]=col
    ranks=[];mats=[]
    for n in range(3):
        cs=[(w,j) for w in levels[n] for j in jb];columns=[]
        for w,j in cs:
            col={}
            for v in levels[n+1]:
                for ww,i,sgn in dres[v]:
                    if ww!=w:continue
                    for jj,c in act(i,{j:1}).items():
                        if jj in jb:put(col,(v,jj),(-1)**(n+1)*sgn*c)
            columns.append(col)
        rr=mh_unit_pivot_rank(columns);ranks.append(rr)
        mats.append({'degree':n,'domain_basis':[repr(c) for c in cs],
                     'columns':[[[repr(k),v] for k,v in col.items()] for col in columns],
                     'scalar_factor':'beta','rank_after_factoring_beta':rr})
    check(ranks==[2,10,38],'matching_six_state_kernel_Hom_ranks')
    for n in range(2):
        cs1=[(w,j) for w in levels[n+1] for j in jb]
        nextcols={s:{literal_eval(k):v for k,v in col} for s,col in zip(cs1,mats[n+1]['columns'])}
        for col in mats[n]['columns']:
            out={}
            for k,c in col:
                for kk,v in nextcols[literal_eval(k)].items():put(out,kk,c*v)
            check(not out,'matching_six_state_kernel_Hom_d_squared',n)
    free=[5-ranks[0],30-ranks[1]-ranks[0],120-ranks[2]-ranks[1]]
    check(free==[3,18,72],'matching_six_state_kernel_Ext_free_ranks')
    return {'basis':b,'actions_with_beta_factored_out':acts,
      'projection_to_E35':[[int(s=='u') for s in b],[int(s=='v35') for s in b]],
      'projection_to_E04':[[int(s=='u') for s in b],[int(s=='v04') for s in b]],
      'R_linear_section_to_E35_exists':False,'no_section_detector':'v04 coefficient of X04 applied to a lift of u is beta',
      'corrected_first_middle_vectors':{'a35':a35,'a04':a04},'kernel_Hom_matrices':mats,
      'kernel_Ext_degrees':[0,1,2],'kernel_Ext_free_ranks':free,'kernel_Ext_A_mod_beta_multiplicities':[0,2,10],
      'mixed_class_lift_maps_to_original_nonzero_class':True}

def mh_cofiber_tests():
    ww=emul(eletter(1),eletter(Z));rev=emul(eletter(Z),eletter(1))
    check(mh_sparse_rank([ww,rev])==2,'matching_ordered_and_reflected_mixed_classes_independent')
    ranks=[];columns=[]
    for n in range(3):
        cols=[emul(ww,{w:1}) for w in words(n)]
        rr=mh_unit_pivot_rank(cols);ranks.append(rr)
        columns.append({'input_degree':n,'columns':[serialize_functional(c) for c in cols],
                        'coefficient':'beta^2','rank':rr})
    check(ranks==[1,5,19],'matching_mixed_cofiber_low_degree_composition_ranks')
    gs=relative_generators();quad=[v for v in gs.values() if edegree(v)==2]
    # Nine orbit classes remain independent even after adjoining the chosen
    # degree-two relation: test them over the beta-inverted field, the
    # strongest quotient for this independence test.
    orbit=[emul(v,eletter(Z)) for v in quad]
    boundaries=[emul(ww,eletter(i)) for i in range(6)]
    check(mh_sparse_rank(boundaries+orbit)-mh_sparse_rank(boundaries)==9,
          'matching_nine_conormal_orbits_survive_single_mixed_cofiber')
    return {'map':'A L04^vee Pi^vee[1] -> D35, induced by beta^2 eta04 eta35 and fibre inclusion',
      'projection_to_original_omega_retained':True,'retraction_to_D35_compatible_with_inclusion_exists':False,
      'original_class_nonzero':serialize_functional(ww),'reflected_ordered_class':serialize_functional(rev),
      'Hom_cone_composition_matrices':columns,'coefficient_probe':'RHom_R(A[2],target)',
      'coefficient_probe_cohomology':{'H^-1':'A L35 Pi^vee','H^0':'A scalar plus Ext^1_R(A,A L35 Pi^vee)',
        'H^1':'coker(beta^2 w:E^0 L04^vee Pi^vee -> E^2 L35 Pi^vee) plus ker(w:E^1 -> E^3), with displayed source lines',
        'ungraded_H1_free_rank':24,'ungraded_H1_A_mod_beta_squared_multiplicity':1},
      'nine_relative_orbits_rank_mod_attached_relation':9,
      'single_ordered_attachment_reflection_closed':False}

def mh_main(output):
    import tempfile
    from contextlib import redirect_stdout
    from io import StringIO
    with tempfile.TemporaryDirectory() as td:
        pp=Path(td)/'retained.json'
        with redirect_stdout(StringIO()):new_run(pp)
        retained=json.loads(pp.read_text())
    before=sum(COUNTS.values())
    aq,qd,theta=mh_q_and_duality()
    source=mh_koszul_source(qd,theta)
    sheets=mh_sheet_resolutions()
    native=mh_endpoint_operations()
    six=mh_six_state_tests()
    cofiber=mh_cofiber_tests()
    cert={'schema':'marici.branchA.matching_Hom_audit.v1',
      'status':'coefficient_duality_Hom_and_derived_endpoint_targets_calculated; physical_total_matching_NOT_instantiated',
      'retained_certificate_content_sha256':retained['certificate_content_sha256'],
      'source_retrieval_scope':'The final Branch C physical-endpoint and source-relative-excess proof files were not retrieved. An older complete K7 source and the actual bare Q differential were retrieved.',
      'source_repository_commit':'538594ab137c4459e11a5ee9d8e0bf6e1dfd1bf0',
      'source_files_read':['research/nima/rzk/40-reduced-seven-state-q-cell.rzk.md','research/chatgpt/marici_short_rees_supported_defect.md'],
      'retained_replay':retained,'Q_to_duality':aq,'seven_equation_source':source,
      'derived_sheet_targets':sheets,'native_sheet_operation_checks':native,'six_state_comparison':six,
      'mixed_cofiber_comparison':cofiber,
      'coefficient_probe_not_physical_F':{
        'probe':'T_Y=RHom_R(A[2],Y), ungraded over A',
        'D35':{'H^-1':'A','H^0':'A^7','H^1':'A^24'},
        'D6':{'H^-1':'A^3','H^0':'A^19 plus (A/beta)^2','H^1':'A^72 plus (A/beta)^10'},
        'D_b':{'H^-1':'A','H^0':'A^7','H^1':'A^24 plus A/(beta^2)'}},
      'physical_matching':{'aQ_physically_selected':False,'plus_endpoint_map':None,'minus_endpoint_map':None,
        'endpoint_pair_comparison_matrix':None,'U':None,'P':None,'Z':None,'u_star':None,'b_star':None,
        'H1_F':None,'obstruction_in_H1_F':None,'H0_F':None,'Hminus1_F':None,
        'first_missing_arrows':[
          'gamma_+: P_plus^phys -> RHom_R(R_plus,A) L35 Pi^vee[3], together with its branch-volume component and full frames',
          'gamma_-: P_minus^phys -> RHom_R(R_minus,A) L35 Pi^vee[3], together with its branch-volume component and full frames',
          'comparison b_* into Z with a relative kernel receiving each primitive endpoint R-orbit'],
        'missing_source_data':['final product-Cartier/excess frame isomorphism','both framed endpoint differentials','Cech and normal incidence maps','native operation chain actions on those physical sources'],
        'empty_or_inhabited':'undetermined, not an emptiness claim'},
      'verification':{'retained_assertions':before,'new_assertions':sum(COUNTS.values())-before,
         'total_assertions':sum(COUNTS.values()),'counts':dict(sorted(COUNTS.items())),
         'physical_endpoint_bar_or_Cech_d_squared_certified':False}}
    # Do not self-certify an absent physical computation.
    check(cert['physical_matching']['H1_F'] is None,'matching_missing_physical_H1_not_fabricated')
    check(cert['physical_matching']['endpoint_pair_comparison_matrix'] is None,'matching_endpoint_pair_not_relabelled_zero')
    cert['verification']['total_assertions']=sum(COUNTS.values())
    cert['verification']['new_assertions']=sum(COUNTS.values())-before
    cert['verification']['counts']=dict(sorted(COUNTS.items()))
    raw=json.dumps(cert,sort_keys=True,separators=(',',':')).encode()
    cert['certificate_content_sha256']=sha256(raw).hexdigest()
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(json.dumps(cert,sort_keys=True,indent=2)+'\n')
    print(json.dumps({'status':cert['status'],'assertions':cert['verification']['total_assertions'],
      'new_assertions':cert['verification']['new_assertions'],'certificate_content_sha256':cert['certificate_content_sha256']},sort_keys=True))

if __name__=='__main__':
    parser=argparse.ArgumentParser(description='Exact coefficient matching-Hom audit; explicitly reports uninstantiated physical arrows.')
    parser.add_argument('--output',type=Path,default=Path('branch_a_matching_hom_certificate.json'))
    mh_main(parser.parse_args().output)
