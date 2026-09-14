#!/usr/bin/env python3
"""Exact conormal trace extension and quadratic continuation audit.

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

def run(out):
    levels,st,ds=resolution(4);verify_contraction(levels,ds)
    ts,tdg,dt,xi,xik,q,od,endpoints,kappa=ten_state_target()
    E,RR,HE,HR,U,rel=traces(st,ds,dt,xi,xik)
    for F,name in ((E,'E'),(RR,'R')):
        relmap={s:apply(q,F[s]) for s in st}
        dV={s:{(t,p):a for (t,p),a in dt[s].items() if t in endpoints} for s in endpoints}
        fV={s:{(t,p):a for (t,p),a in F[s].items() if t in endpoints} for s in st}
        rawquot={s:{(t,p):a for (t,p),a in F[s].items() if t not in endpoints} for s in st}
        for s in st:
            lhs=add(apply(dV,fV[s]),apply(kappa,rawquot[s]))
            check(lhs==apply(fV,ds[s]),'both_edge_endpoint_connector_equations',(name,s))
    nd,rho,lifts,readouts,difference=normalized_readout(st,ds,dt,tdg,q,E,RR,HE,HR,rel,xik)
    phi,pairs,triples,cup,fixed=yoneda_products(levels,ds)
    modules=small_linear_maps()
    # Physical coefficient involution 3-v swaps (02,13), (04,35), (24,15).
    reflection={0:3,1:5,2:4,3:0,4:2,5:1}
    check(all(reflection[reflection[i]]==i for i in range(6)),'physical_label_involution_square')
    check(reflection[Z]==1,'physical_label_35_maps_to_04')
    check(pairs[1,Z]=={((1,),(Z,)):-1},'reflected_conormal_ordered_product_nonzero')
    cert={
      'schema':'marici.branchA.conormal_trace_extension_and_mixed_obstruction.v1',
      'status':'constructed_normalized_conormal_extension_and_complete_quadratic_continuation_test',
      'coefficient_ring':'R=A[X02,X04,X24,X13,X15,X35]/(I_minus I_plus), A=Z[beta,X03,X14,X25]',
      'variables':VARS,'ordered_short_labels':SHORT,
      'source_resolution':{'ranks':[len(lev) for lev in levels],'states':st,'differential':serialize_map(ds),
        'exactness':'All-degree alternating-block contraction is proved in the companion text; bounded controls verify its implementation.'},
      'trace_target':{'states':ts,'degrees':tdg,'differential':serialize_map(dt),'xi':serialize_vec(xi),'xi_k':serialize_vec(xik)},
      'trace_maps':{'E':serialize_map(E),'R':serialize_map(RR)},
      'normalization_homotopies':{'positive_E':serialize_map(HE),'positive_R':serialize_map(HR),'negative':'zero'},
      'normalization_fibre_differential':serialize_map(nd),
      'relative_normalization_projection':serialize_map(rho),
      'normalized_trace_lifts':{k:serialize_map(v) for k,v in lifts.items()},
      'two_grade_readouts':{k:serialize_map(v) for k,v in readouts.items()},
      'trace_difference_readout':serialize_map(difference),
      'two_grade_matrix':[['-beta','-beta'],['0','-beta']],
      'conormal_class':'beta*[X35]^vee tensor L35 in Ext^1_R(A,A tensor L35)',
      'extension_presentation':{'A_basis':['u','v'],'X35_u':'beta*v','X35_v':'0','other_short_actions':'0',
        'sequence':'0 -> A tensor L35 -> E_beta,35 -> A -> 0',
        'beta_unit_model':'R/(X_i for i !=35, X35^2)',
        'splitting_criterion':'The extension splits exactly when beta=0 after base change; over the displayed A it is nonsplit.',
        'annihilator_of_class_over_R':'I_minus+I_plus'},
      'small_module_matrices':{k:serialize_map(v) if isinstance(v,dict) else v for k,v in modules.items()},
      'degree_one_chain_lifts':[serialize_map(v) for v in phi],
      'cup_product_columns':[[[SHORT[a],SHORT[b]],serialize_functional(v)] for (a,b),v in pairs.items()],
      'cup_product_rank':24,'quadratic_relation_kernel_rank':12,
      'quadratic_relations':'eta_i^2=0; eta_i eta_j + eta_j eta_i=0 within one sheet; no mixed quadratic relation',
      'degree_three_products':[[[SHORT[a],SHORT[b],SHORT[c]],serialize_functional(v)] for (a,b,c),v in triples.items()],
      'degree_three_rank':92,
      'continuation_matrix_fixed_X35':fixed,
      'continuation_rank':5,'continuation_kernel':'A*eta35',
      'physical_label_reflected_product':'eta04 eta35 = -m_(04,35)^vee under the stated chain-lift convention',
      'relation_only_comparison':{'homotopy':serialize_map(U),'residual':serialize_map(rel)},
      'both_endpoint_connector':serialize_map(kappa),
      'limitations':[
        'The refined readout has the complete normalized trace maps and their branch homotopies as input; no unrestricted map T -> a scalar/conormal target is claimed.',
        'The rank-two extension is a module-valued representative of the resulting Ext^1 class, not a second scalar residue.',
        'The rank-three continuation problem fixes one-dimensional successive A-quotients. Its obstruction does not prohibit a larger or genuinely derived comparison.',
        'The product of reflected conormal classes is not the square of the physical reflection action.',
        'The physical H_cond, its comparison with the Morse trivialization, and Delta_J remain unassigned.'
      ],
      'provenance':{'repo':'andrey-kokoev/marici','commit':'d1947b67a60d3e88ba77f4ca60ea02c2a306ee61',
        'source':'Entry 93 normalization ring and polarity; existing ten-state trace and explicit source-relation formulas reconstructed here'},
      'counts':dict(sorted(COUNTS.items()))
    }
    payload=json.dumps(cert,sort_keys=True,separators=(',',':')).encode()
    cert['certificate_content_sha256']=sha256(payload).hexdigest()
    out.write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'status':cert['status'],'exact_checks':sum(COUNTS.values()),
       'conormal_difference':'beta*eta35','cup_ranks':[6,24,92],
       'next_direction_obstruction_rank':5,'next_direction_kernel':'A*eta35',
       'certificate_content_sha256':cert['certificate_content_sha256']},sort_keys=True))

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path('branch_a_conormal_trace_extension_and_mixed_obstruction_certificate.json'))
    run(parser.parse_args().output)
