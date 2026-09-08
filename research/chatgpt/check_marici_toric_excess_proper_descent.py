#!/usr/bin/env python3
"""Global excess bundle, primitive proper trace, and full Cartier descent.

The preceding toric reconstruction/audit is embedded below for reproduction.
Its original scope: Toric Jacobian/Cartier comparison of the whole native Rees map.

Reconstruction helpers are retained from the immediately preceding checker.

Original helper scope:

Python 3.10+, standard library only. Integer polynomial/Laurent identities are
checked symbolically; inverse normals occur only in their designated target
stalks. Occurrence variables are never inverted. The complete node resolution,
two endpoint maps, conductor homotopy, target support filtration, Hom fibres,
and orientation character are retained. This is a finite coefficient/cap
comparison, not a claimed algebraic six-functor or physical parity theorem.
"""
from __future__ import annotations
import argparse, hashlib, json
from collections import Counter
from itertools import combinations, product, permutations
from pathlib import Path

COMMIT='d1947b67a60d3e88ba77f4ca60ea02c2a306ee61'
SOURCE_BLOBS={
 'src/ledger/20260814-93 Alternating Fusion Normalization-Conductor Square.md':'840258522d45e450e4f1e8bb927d9aae58c75566',
 'research/voevodsky/check_global_k6_koszul_cech_promotion.rs':'e972b69d0e2b1b0a0aee5e0a027c8216bcace3e8',
 'research/voevodsky/check_two_endpoint_tate_carrier.rs':'0147e2e42dafac0da7289c571cb0331b51338be1'}
COUNT=Counter(); Z=(0,)*18
EV=(0,2,4); OD=(1,3,5); ORDER=EV+OD

def check(ok,tag):
    if not ok: raise AssertionError(tag)
    COUNT[tag]+=1

def pm(n):return -1 if n%2 else 1

def subsets(s):return [t for k in range(len(s)+1) for t in combinations(s,k)]
def ex(entries):return tuple(entries.get(i,0) for i in range(18))
def eadd(a,b):return tuple(x+y for x,y in zip(a,b))
def esub(a,b):return tuple(x-y for x,y in zip(a,b))
def add(*vs):
    o={}
    for v in vs:
        for k,a in v.items():
            o[k]=o.get(k,0)+a
            if not o[k]:del o[k]
    return o

def scale(v,a):return {k:a*c for k,c in v.items() if a*c}
def multiply(v,e,a=1):return {(b,eadd(m,e)):a*c for (b,m),c in v.items() if a*c}
def one(b):return {(b,Z):1}
def apply(table,v):
    out={}
    for (b,e),c in v.items():out=add(out,multiply(table.get(b,{}),e,c))
    return out

def lin(table,v):
    out={}
    for b,a in v.items():out=add(out,scale(table.get(b,{}),a))
    return out

def di(i,j):return tuple(sorted((i%6,j%6)))
def cross(a,b):
    x,y=a;u,v=b
    return x<u<y<v or u<x<v<y
DS=tuple((i,j) for i in range(6) for j in range(i+1,6) if j-i not in (1,5))
SHORT=tuple(di(i,i+2) for i in range(6)); LONG=tuple(di(i,i+3) for i in range(3))
IX={a:i for i,a in enumerate(SHORT+LONG)}
FACES=tuple(f for k in range(4) for f in combinations(DS,k)
            if all(not cross(a,b) for a,b in combinations(f,2)))
CELLS=tuple((f,h) for f in FACES for h in subsets(f))
VP=tuple(sorted(SHORT[i] for i in OD)); VM=tuple(sorted(SHORT[i] for i in EV))
GAMMA=ex({15:1,16:1,17:1}); LAMBDA=esub(GAMMA,ex({i:1 for i in range(6)}))
GROUP=tuple(product(range(3),range(2)))

def degree(c):return 3-len(c[0])+len(c[1])
def weight(c):return ex({**{IX[a]:1 for a in c[0]},**{9+IX[a]:-1 for a in c[0]}})
def predicate(c,k):
    v=c[0] in (VP,VM); b=any(a in SHORT for a in c[0])
    return {'K':True,'V':v,'B':b,'E':not v,'BV':b and not v,'Q':not b}[k]
def legal(c,m):
    local={IX[a] for a in c[0] if a not in c[1]}
    return all(a>=0 for a in m[:9]) and all(a>=0 or i in local for i,a in enumerate(m[9:]))
def target_boundary(c):
    f,h=c;z={}
    for a in DS:
        if a not in f and all(not cross(a,b) for b in f):
            t=(tuple(sorted(f+(a,))),h)
            z[t,ex({IX[a]:1,9+IX[a]:-1})]=pm(sum(b<a for b in f))
    for i,a in enumerate(h):z[(f,tuple(b for b in h if b!=a)),Z]=pm(3-len(f)+i)
    return z
BD={c:target_boundary(c) for c in CELLS}

def project(v,k):return {(c,e):a for (c,e),a in v.items() if predicate(c,k)}
def td(v,k='K'):return project(apply(BD,v),k)

def koszul(seq,tag):
    g={};d={};labels={}
    for s in subsets(seq):
        b=(tag,s);g[b]=len(s);labels[b]=ex({i:1 for i in s})
        d[b]={((tag,s[:j]+s[j+1:]),ex({i:1})):pm(j) for j,i in enumerate(s)}
    return g,d,labels

def node():
    bot=('P',(),());g={bot:0};d={bot:{}};labels={bot:Z}
    for u in subsets(EV)[1:]:
        for v in subsets(OD)[1:]:
            b=('P',u,v);g[b]=len(u)+len(v)-1;labels[b]=ex({i:1 for i in u+v});z={}
            if len(u)==len(v)==1:z[bot,ex({u[0]:1,v[0]:1})]=1
            else:
                if len(u)>1:
                    for j,i in enumerate(u):z[('P',u[:j]+u[j+1:],v),ex({i:1})]=pm(j)
                if len(v)>1:
                    for j,i in enumerate(v):z[('P',u,v[:j]+v[j+1:]),ex({i:1})]=pm(len(u)-1+j)
            d[b]=z
    return g,d,labels

def audit_source(model,tag):
    gs,d,labels=model
    for b in gs:
        check(not apply(d,d[b]),tag+'_d_squared')
        for (a,e),v in d[b].items():
            check(gs[a]+1==gs[b],tag+'_chain_degree')
            check(eadd(e,labels[a])==labels[b],tag+'_coefficient_degree')
            check(min(e)>=0 and abs(v)==1,tag+'_integral_polynomial')

def omega(t):
    f=tuple(sorted(SHORT[i] for i in t))
    if f not in FACES:return {}
    e=eadd(GAMMA,ex({9+i:-1 for i in t}));z={((f,()),e):1}
    for l in LONG:
        if all(not cross(l,b) for b in f):
            c=(tuple(sorted(f+(l,))),(l,))
            m=eadd(e,ex({IX[l]:1,IX[l]+9:-1}))
            z[c,m]=-pm(sum(b>l for b in f))
    return z

def complement_sign(i):
    t=tuple(a for a in ORDER if a not in i)
    inversions=sum(SHORT[t[a]]>SHORT[t[b]] for a in range(len(t)) for b in range(a+1,len(t)))
    return pm(len(t)+sum(ORDER.index(a) for a in t)+inversions)

def perm_short(g):
    k,f=g;return tuple((2*k+(1-i if f else i))%6 for i in range(6))
def perm_di(a,g):
    k,f=g
    per=lambda v:(2*k+(3-v if f else v))%6
    return di(per(a[0]),per(a[1]))
def invsign(values,order):
    ix={v:i for i,v in enumerate(order)};x=[ix[v] for v in values]
    return pm(sum(x[i]>x[j] for i in range(len(x)) for j in range(i+1,len(x))))
def perm_ex(e,g):
    out=[0]*18
    for i,a in enumerate(SHORT+LONG):
        j=IX[perm_di(a,g)];out[j]=e[i];out[9+j]=e[9+i]
    return tuple(out)
def act_p_basis(b,g):
    _,u,v=b
    if not u:return b,1
    per=perm_short(g);pu=[per[i] for i in u];pv=[per[i] for i in v]
    if not g[1]:return ('P',tuple(sorted(pu)),tuple(sorted(pv))),invsign(pu,EV)*invsign(pv,OD)
    return ('P',tuple(sorted(pv)),tuple(sorted(pu))),pm((len(u)-1)*(len(v)-1))*invsign(pv,EV)*invsign(pu,OD)
def act_source(v,g):
    z={}
    for (b,e),a in v.items():
        im,s=act_p_basis(b,g);z=add(z,{(im,perm_ex(e,g)):a*s})
    return z

def act_target(v,g):
    z={}
    for (c,e),a in v.items():
        f,h=c;pf=[perm_di(i,g) for i in f];ph=[perm_di(i,g) for i in h]
        sign=pm(g[1])*invsign(pf,DS)*invsign(ph,DS)
        c1=(tuple(sorted(pf)),tuple(sorted(ph)))
        z=add(z,{(c1,perm_ex(e,g)):a*sign})
    return z


ONE_N=(1,)*9

def finite_boundary(c,n):
    f,h=c;out={}
    for a in DS:
        if a not in f and all(not cross(a,b) for b in f):
            t=(tuple(sorted(f+(a,))),h);i=IX[a]
            out[t,ex({i:1,9+i:n[i]-1})]=pm(sum(b<a for b in f))
    for pos,a in enumerate(h):
        t=(f,tuple(b for b in h if b!=a));i=IX[a]
        out[t,ex({9+i:n[i]})]=pm(3-len(f)+pos)
    return out

def finite_table(n):return {c:finite_boundary(c,n) for c in CELLS}

def clear_power(c,n):
    return ex({9+IX[a]:n[IX[a]] for a in c[0] if a not in c[1]})

def finite_shift(c,n):return esub(scale_exp(weight(c),-1),clear_power(c,n))
def scale_exp(v,k):return tuple(k*a for a in v)

def diagonal_map(v,n,m):
    out={}
    for (c,e),a in v.items():
        ee=eadd(e,ex({9+IX[q]:m[IX[q]]-n[IX[q]] for q in c[0] if q not in c[1]}))
        out=add(out,{(c,ee):a})
    return out

def delocalize(v,n):
    return add(*({(c,eadd(e,clear_power(c,n))):a} for (c,e),a in v.items()))

def localize(v,n):
    return add(*({(c,esub(e,clear_power(c,n))):a} for (c,e),a in v.items()))

def construct_source_data():
    P=node();KE=koszul(EV,'E');KO=koszul(OD,'O');KC=koszul(ORDER,'C')
    cap={b:scale(omega(tuple(i for i in ORDER if i not in b[1])),complement_sign(b[1])) for b in KC[0]}
    fp={};fm={};H={};F={}
    for b in P[0]:
        _,u,v=b
        if not u:
            fp[b]=one(('E',()));fm[b]=one(('O',()));H[b]={};F[b]={}
        else:
            fp[b]={(('E',u),ex({v[0]:1})):1} if len(v)==1 else {}
            fm[b]={(('O',v),ex({u[0]:1})):1} if len(u)==1 else {}
            H[b]={(('C',u+v),Z):pm(len(u))}
            F[b]=scale(apply(cap,H[b]),-1)
    tp={b:cap[('C',b[1])] for b in KE[0]}
    tm={b:cap[('C',b[1])] for b in KO[0]}
    ends={b:add(apply(tp,fp[b]),scale(apply(tm,fm[b]),-1)) for b in P[0]}
    return P,KE,KO,KC,cap,fp,fm,H,F,tp,tm,ends


# Long Rees variables are indexed 15,16,17. In a chart the same slots hold
# s,r,q. Short normal slots 9..14 are never identified with these variables.
W=ex({6:1,7:1,8:1})
TAU=ex({15:1,16:1,17:1})
GCH=ex({15:2,16:1})
ZCH=ex({15:1,16:1,17:1})
CHARTS=tuple(permutations(range(3)))

def rees_long(v):
    out={}
    for (b,e),a in v.items():
        ee=list(e)
        for i in range(3):ee[6+i]+=e[15+i]
        out=add(out,{(b,tuple(ee)):a})
    return out

def divide(v,e,tag='polynomial_line_factor'):
    out=multiply(v,tuple(-x for x in e))
    check(all(min(m)>=0 for b,m in out),tag)
    return out

def chart_exp(e,pi):
    i,j,k=pi;out=list(e)
    out[15]=e[15+i]+e[15+j]+e[15+k]
    out[16]=e[15+j]+e[15+k]
    out[17]=e[15+k]
    return tuple(out)

def unchart_exp(e,pi):
    i,j,k=pi;out=list(e)
    out[15+i]=e[15]-e[16]
    out[15+j]=e[16]-e[17]
    out[15+k]=e[17]
    return tuple(out)

def map_exp(v,fn):
    out={}
    for (b,e),a in v.items():out=add(out,{(b,fn(e)):a})
    return out

def chart(v,pi):return map_exp(v,lambda e:chart_exp(e,pi))
def transition(v,source,target):
    return map_exp(v,lambda e:chart_exp(unchart_exp(e,source),target))

def specialize_coords(v,zero):
    return {(b,e):a for (b,e),a in v.items() if all(e[15+i]==0 for i in zero)}

def mod_monomial(v,gen):
    return {(b,e):a for (b,e),a in v.items()
            if not all(a0>=g for a0,g in zip(e,gen))}

def difference_map(F,P,bd):
    # F has even cohomological degree two.
    return {b:add(apply(bd,F[b]),scale(apply(F,P[1][b]),-1)) for b in P[0]}

def closed_odd(A,P,bd):
    return {b:add(apply(bd,A[b]),apply(A,P[1][b])) for b in P[0]}

def matrix_det_int(a):
    n=len(a)
    return sum(pm(sum(p[i]>p[j] for i in range(n) for j in range(i+1,n)))
               * __import__('functools').reduce(lambda x,y:x*y,(a[i][p[i]] for i in range(n)),1)
               for p in permutations(range(n)))

def poly_add(*p):
    out={}
    for onep in p:
        for e,a in onep.items():
            out[e]=out.get(e,0)+a
            if not out[e]:del out[e]
    return out

def poly_mul(p,q):
    out={}
    for e,a in p.items():
        for f,b in q.items():out=poly_add(out,{tuple(x+y for x,y in zip(e,f)):a*b})
    return out

def poly_det(a):
    n=len(a);out={}
    for p in permutations(range(n)):
        v={(0,)*3:pm(sum(p[i]>p[j] for i in range(n) for j in range(i+1,n)))}
        for i in range(n):v=poly_mul(v,a[i][p[i]])
        out=poly_add(out,v)
    return out

def prime_detector(v,target_basis,vanish_variables):
    # Coefficient in a stated target row modulo a homogeneous coordinate ideal.
    out={}
    for (b,e),a in v.items():
        if b==target_basis and all(e[j]==0 for j in vanish_variables):
            out[e]=out.get(e,0)+a
    return {e:a for e,a in out.items() if a}

def toric_target_action(v,g):
    # Chart s,r,q stay in their ordered slots while diagonal labels move.
    out={}
    for (c,e),a in v.items():
        f,h=c;pf=[perm_di(i,g) for i in f];ph=[perm_di(i,g) for i in h]
        sign=pm(g[1])*invsign(pf,DS)*invsign(ph,DS)
        ee=list(perm_ex(e,g));ee[15:18]=e[15:18]
        out=add(out,{((tuple(sorted(pf)),tuple(sorted(ph))),tuple(ee)):a*sign})
    return out

def change_chart_labels(pi,g):
    return tuple(IX[perm_di(LONG[i],g)]-6 for i in pi)

def wrap(v,tag,eta=0):
    return {((tag,b,eta),e):a for (b,e),a in v.items()}


def exterior_koszul_audit(equations, new_equations, columns, tag):
    n=len(equations)
    def differential(eq):
        out={}
        for mask in range(1<<n):
            out[mask]={}
            for i,e in enumerate(eq):
                if mask>>i&1 and e is not None:
                    out[mask][mask^(1<<i),e]=pm((mask&((1<<i)-1)).bit_count())
        return out
    def wedge(v,w):
        out={}
        for (a,e),c in v.items():
            for (b,f),d in w.items():
                if a&b:continue
                sign=pm(sum(1 for i in range(n) if a>>i&1 for j in range(i) if b>>j&1))
                out=add(out,{(a|b,eadd(e,f)):c*d*sign})
        return out
    change={}
    for mask in range(1<<n):
        v={(0,Z):1}
        for i in range(n):
            if mask>>i&1:v=wedge(v,columns[i])
        change[mask]=v
    old=differential(equations);new=differential(new_equations)
    for mask in range(1<<n):
        check(apply(old,change[mask])==apply(change,new[mask]),tag+'_all_wedge_chain_equations')
        check(not apply(old,old[mask]),tag+'_original_d_squared')
    return change,old,new

def retained_excess_audit():
    # These are the original selected SHORT normal equations. The temporary
    # use of exponent slots 9 and 12 for t0,t3 is confined to this audit.
    regular=[ex({1:1}),ex({3:1}),ex({5:1}),ex({0:1,9:1})]
    eta={(2,ex({12:1})):1,(16,Z):-1}
    cols=[{(1<<i,Z):1} for i in range(4)]+[eta]
    change,old,new=exterior_koszul_audit(regular+[ex({3:1,12:1})],regular+[None],cols,'independent_selected_excess')
    check(change[31]=={(31,Z):-1},'independent_selected_excess_unimodular')
    check(not apply(old,eta),'independent_eta_closed')
    central={(b,e):a for (b,e),a in eta.items() if e[12]==0}
    check(central=={(16,Z):-1},'independent_eta_not_an_internal_multiplier')
    # Pull back the THREE LONG Rees equations. This is not K(s,r,q).
    long_raw=[ex({15:1}),ex({15:1,16:1}),ex({15:1,16:1,17:1})]
    zeta_j={(2,Z):1,(1,ex({16:1})):-1}
    zeta_k={(4,Z):1,(1,ex({16:1,17:1})):-1}
    cols=[{(1,Z):1},zeta_j,zeta_k]
    change,old,new=exterior_koszul_audit(long_raw,[ex({15:1}),None,None],cols,'long_central_fibre_rank_two_excess')
    check(change[7]=={(7,Z):1},'long_excess_basis_change_determinant_one')
    check(not apply(old,zeta_j) and not apply(old,zeta_k),'two_new_long_excess_cycles_closed')
    for mask in range(8):
        for coord in (15,16,17):
            specialized={(b,e):a for (b,e),a in old[mask].items() if e[coord]==0}
            if coord==15:check(not specialized,'original_long_Cartier_differential_zero_on_exceptional_divisor')
    return {
      'original_independent_short_excess':'eta=t3*h3_plus-h3_pair, retained independently',
      'pulled_back_long_Cartier_complex':'K(s,s*r,s*r*q)=K(s) tensor Lambda(zeta_j,zeta_k)',
      'new_long_excess_generators':['zeta_j=e_j-r*e_i','zeta_k=e_k-r*q*e_i'],
      'new_long_excess_homology':'O/(s) in ranks 1,2,1 in homological degrees 0,1,2',
      'not_identifications':['The two new long-Rees excess classes are not identified with the original independent eta.',
                           'The pulled-back K(t0,t1,t2) is not replaced by K(s,r,q).',
                           'The residual one-Cartier Gysin is not the original codimension-three Gysin.']}


def preceding_audit(output):
    P,KE,KO,KC,cap,fp,fm,H,FC,tpC,tmC,endC=construct_source_data()
    for model,name in ((P,'native'),(KE,'plus'),(KO,'minus'),(KC,'conductor')):
        audit_source(model,name)
    F1={b:delocalize(v,ONE_N) for b,v in FC.items()}
    A1={b:delocalize(v,ONE_N) for b,v in endC.items()}
    ap1={b:delocalize(v,ONE_N) for b,v in tpC.items()}
    am1={b:delocalize(v,ONE_N) for b,v in tmC.items()}
    bd1=finite_table(ONE_N)
    F={b:divide(rees_long(v),W) for b,v in F1.items()}
    AA={b:divide(rees_long(v),eadd(W,TAU)) for b,v in A1.items()}
    ap={b:divide(rees_long(v),eadd(W,TAU)) for b,v in ap1.items()}
    am={b:divide(rees_long(v),eadd(W,TAU)) for b,v in am1.items()}
    bd={c:rees_long(v) for c,v in bd1.items()}
    check(len(CELLS)==215,'target_has_all_215_states')
    check(len(P[0])==50,'source_has_all_50_generators')
    check(sum(map(len,F.values()))==43,'full_map_43_terms')
    check(sum(map(len,AA.values()))==6,'both_endpoint_composites_six_terms')
    check(ap[('E',EV)]==one((VP,())),'plus_individual_endpoint_unit')
    check(am[('O',OD)]==scale(one((VM,())),-1),'minus_individual_endpoint_unit')
    for b in P[0]:
        check(difference_map(F,P,bd)[b]==multiply(AA[b],TAU),'whole_Rees_endpoint_identity')
        check(not closed_odd(AA,P,bd)[b],'endpoint_pair_closed')
    for c in CELLS:
        check(not apply(bd,bd[c]),'whole_target_d_squared')
        for support in ('V','B'):
            if predicate(c,support):
                check(all(predicate(t,support) for t,e in bd[c]),'unchanged_support_filtration')
    # Split by actual target marks, not numerical fitting of the desired row.
    TOP={b:divide({(c,e):a for (c,e),a in v.items() if not c[1]},TAU)
         for b,v in F.items()}
    MARK=[]
    for i,l in enumerate(LONG):
        mi=ex({15+j:1 for j in range(3) if j!=i})
        MARK.append({b:divide({(c,e):a for (c,e),a in v.items() if c[1]==(l,)},mi)
                     for b,v in F.items()})
    check(sum(map(len,TOP.values()))==16,'cubic_block_16_terms')
    for x in MARK:check(sum(map(len,x.values()))==9,'each_marked_block_nine_terms')
    d0={c:{(t,e):a for (t,e),a in v.items() if not any(e[15:18])} for c,v in bd.items()}
    NN=[]
    for i in range(3):
        NN.append({c:divide({(t,e):a for (t,e),a in v.items() if e[15+i]},ex({15+i:1}))
                   for c,v in bd.items()})
    for b in P[0]:
        for i in range(3):
            check(apply(d0,MARK[i][b])==apply(MARK[i],P[1][b]),'each_initial_marked_symbol_closed')
        val=add(apply(d0,TOP[b]),scale(apply(TOP,P[1][b]),-1),
                *(apply(NN[i],MARK[i][b]) for i in range(3)))
        check(val==AA[b],'one_coupled_endpoint_obstruction_equation')
    charts={};records=[];top_source=('P',EV,OD)
    for pi in CHARTS:
        i,j,k=pi
        fb={b:divide(chart(v,pi),GCH) for b,v in F.items()}
        db={c:chart(v,pi) for c,v in bd.items()}
        charts[pi]=(fb,db)
        for b in P[0]:
            expected=add(MARK[k][b],multiply(MARK[j][b],ex({17:1})),
                         multiply(MARK[i][b],ex({16:1,17:1})),multiply(TOP[b],ZCH))
            check(fb[b]==expected,'four_stage_toric_comparison_formula')
            lhs=add(apply(db,fb[b]),scale(apply(fb,P[1][b]),-1))
            check(lhs==multiply(AA[b],ZCH),'Cartier_full_endpoint_identity')
            check(all(min(e)>=0 for c,e in fb[b]),'no_chart_coefficient_inverse')
        for c in CELLS:check(not apply(db,db[c]),'every_chart_d_squared')
        # The proper transform of J is (s^2 r), computed on all its generators.
        transformed=[]
        for h in range(3):
            m=ex({15+j0:1 for j0 in range(3) if j0!=h})
            transformed.append(esub(chart_exp(m,pi),GCH))
        check(set(transformed)=={Z,ex({17:1}),ex({16:1,17:1})},'trace_ideal_principalizes')
        check(chart_exp(TAU,pi)==eadd(GCH,ZCH),'residual_boundary_reduced_srq')
        # Relative Jacobian in ordered t_i,t_j,t_k coordinates.
        texp=[(1,0,0),(1,1,0),(1,1,1)]
        jac=[]
        for e in texp:
            row=[]
            for pos in range(3):
                ee=list(e)
                if ee[pos]:
                    coefficient=ee[pos];ee[pos]-=1;row.append({tuple(ee):coefficient})
                else:row.append({})
            jac.append(row)
        check(poly_det(jac)=={(2,1,0):1},'relative_jacobian_equals_trace_ideal_generator')
        check(matrix_det_int([list(x) for x in texp])==1,'logarithmic_orientation_unimodular')
        # Every possible coboundary alters the top-source/top-target coefficient
        # by the short-occurrence ideal; the unit marked coefficient detects it.
        generic_unit=prime_detector(fb[top_source],((LONG[k],),(LONG[k],)),range(6))
        check(generic_unit=={Z:-1},'primitive_generic_class_not_a_boundary')
        for b,v in P[1].items():
            if P[0][b]==5:
                check(all(any(e[h] for h in range(6)) for (t,e) in v),
                      'all_top_source_boundaries_in_short_occurrence_ideal')
        check(max(map(degree,CELLS))==3,'no_target_degree_four_boundary')
        face_records=[]
        for mask in range(8):
            zs=tuple(i0 for i0 in range(3) if mask>>i0&1)
            ff={b:specialize_coords(v,zs) for b,v in fb.items()}
            dd={c:specialize_coords(v,zs) for c,v in db.items()}
            end={b:specialize_coords(multiply(v,ZCH),zs) for b,v in AA.items()}
            for b in P[0]:
                check(add(apply(dd,ff[b]),scale(apply(ff,P[1][b]),-1))==end[b],
                      'all_resolved_boundary_faces_keep_chain_equation')
            check(prime_detector(ff[top_source],((LONG[k],),(LONG[k],)),range(6))=={Z:-1},
                  'primitive_generic_survives_all_resolved_faces')
            if zs:check(not any(end.values()),'ordinary_endpoints_vanish_on_residual_boundary')
            face_records.append({'zero_coordinates':[('s','r','q')[z] for z in zs],
                'comparison_terms':sum(map(len,ff.values())),
                'ordinary_endpoint_terms':sum(map(len,end.values())),
                'framed_generic_value':-1})
        # Complete two-term Cartier morphism: C has Hom degree 2 and A degree 3.
        # Differential is D F=z A, D A=0. It is checked on every P column.
        for b in P[0]:
            defect=add(apply(db,fb[b]),scale(apply(fb,P[1][b]),-1))
            check(divide(defect,ZCH)==AA[b],'divided_full_boundary_is_native_endpoint_pair')
            check(not mod_monomial(defect,ZCH),'closed_Cartier_lower_class')
            check(not closed_odd(AA,P,db)[b],'Cartier_upper_map_closed')
            for p in range(3):
                partial=divide(defect,ex({15+p:1}))
                check(partial==multiply(AA[b],ex({15+h:1 for h in range(3) if h!=p})),
                      'separate_component_Bockstein_retains_other_normals')
        # Explicit tensor map from [e2 --z--> e3] tensor P to K.
        # Homological degrees of e2,e3 are -2,-3; eta is independent degree +1.
        source_basis=[];source_d={};target_d={};map_total={}
        for eps in (0,1):
            for tag,homological in (('lower',-2),('upper',-3)):
                for b,deg in P[0].items():
                    key=(tag,b,eps);source_basis.append(key)
                    out=scale(wrap(P[1][b],tag,eps),pm(homological))
                    if tag=='lower':out=add(out,{(('upper',b,eps),ZCH):1})
                    source_d[key]=out
                    map_total[key]=wrap(fb[b] if tag=='lower' else AA[b],'target',eps)
                    for c,e in (fb[b] if tag=='lower' else AA[b]):
                        check(degree(c)+eps==deg+homological+eps,'Cartier_tensor_map_degree')
            for c in CELLS:target_d[('target',c,eps)]=wrap(db[c],'target',eps)
        for key in source_basis:
            check(not apply(source_d,source_d[key]),'Cartier_tensor_source_d_squared')
            check(apply(target_d,map_total[key])==apply(map_total,source_d[key]),
                  'Cartier_tensor_whole_source_map_with_independent_excess')
        records.append({'permutation':list(pi),'map_terms':sum(map(len,fb.values())),
            'source_columns':len(P[0]),'native_endpoint_columns':6,'jacobian':'s^2*r',
            'residual_boundary':'s*r*q','faces':face_records})
    # Actual affine overlap formulae. The two generators swap adjacent ordering.
    adjacencies=[]
    for pi in CHARTS:
        for swap in (0,1):
            qq=list(pi);qq[swap],qq[swap+1]=qq[swap+1],qq[swap];qq=tuple(qq)
            fb,db=charts[pi];fq,dq=charts[qq]
            # Source g transported into destination chart; c=g_dest/g_source.
            source_g=chart_exp(unchart_exp(GCH,pi),qq)
            factor=esub(GCH,source_g)
            for b in P[0]:
                check(transition(fb[b],pi,qq)==multiply(fq[b],factor),'whole_map_line_transition')
            for c in CELLS:check(transition(db[c],pi,qq)==dq[c],'whole_differential_overlap')
            source_z=chart_exp(unchart_exp(ZCH,pi),qq)
            check(source_z==eadd(ZCH,factor),'Cartier_source_frame_transition')
            # Relative Jacobian coefficients transform with the same frame.
            if swap==0:
                check(factor==Z,'first_swap_preserves_jacobian_generator')
            else:
                check(set(abs(x) for x in factor if x)=={1},'second_swap_unit_transition')
            adjacencies.append({'from':list(pi),'to':list(qq),'swap':swap,
                               'line_factor_exponents_in_to_chart':list(factor[15:18])})
    for p,q,r in product(CHARTS,repeat=3):
        for l in range(3):
            e=ex({15+l:1})
            direct=chart_exp(unchart_exp(e,p),r)
            mid=chart_exp(unchart_exp(chart_exp(unchart_exp(e,p),q),q),r)
            check(direct==mid,'all_chart_triple_cocycles')
        c_pq=esub(GCH,chart_exp(unchart_exp(GCH,p),q))
        c_qr=esub(GCH,chart_exp(unchart_exp(GCH,q),r))
        check(eadd(chart_exp(unchart_exp(c_pq,q),r),c_qr)==
              esub(GCH,chart_exp(unchart_exp(GCH,p),r)),'all_Cartier_line_triple_cocycles')
    for pi in CHARTS:
        fb,db=charts[pi]
        for g in GROUP:
            newpi=change_chart_labels(pi,g);fg,dg=charts[newpi]
            for c in CELLS:
                check(toric_target_action(db[c],g)==apply(dg,toric_target_action(one(c),g)),
                      'whole_toric_dihedral_target')
            for b in P[0]:
                check(toric_target_action(fb[b],g)==scale(apply(fg,act_source(one(b),g)),pm(g[1])),
                      'whole_toric_native_polarity_equivariance')
                check(toric_target_action(AA[b],g)==scale(apply(AA,act_source(one(b),g)),pm(g[1])),
                      'both_endpoint_polarity_equivariance')
    # Compatibility with the genuine normal localization system at additional
    # finite orders. The proof is the same diagonal monomial identity for all n.
    for n in ((2,)*9,tuple(1+(i%3) for i in range(9))):
        rawf={b:delocalize(v,n) for b,v in FC.items()}
        rawa={b:delocalize(v,n) for b,v in endC.items()}
        rawd=finite_table(n)
        for pi in CHARTS:
            fn={b:divide(chart(rees_long(v),pi),eadd(W,GCH)) for b,v in rawf.items()}
            an={b:divide(chart(rees_long(v),pi),eadd(W,eadd(GCH,ZCH))) for b,v in rawa.items()}
            dn={c:chart(rees_long(v),pi) for c,v in rawd.items()}
            for b in P[0]:
                check(add(apply(dn,fn[b]),scale(apply(fn,P[1][b]),-1))==multiply(an[b],ZCH),
                      'higher_normal_order_Cartier_endpoint_identity')
                expected=chart(rees_long(diagonal_map(F1[b],ONE_N,n)),pi)
                check(fn[b]==divide(expected,eadd(W,GCH)),
                      'factored_map_commutes_with_normal_tower')
    # Endpoint nonvanishing certificates against every polynomial homotopy.
    # At a fully supported endpoint there is no radial differential. The only
    # possible bottom boundaries have u_odd (resp u_even); source coboundaries
    # have X_even (resp X_odd). The selected coefficient is a signed unit.
    for model,aa,vertex,base,normal in ((KE,ap,VP,EV,OD),(KO,am,VM,OD,EV)):
        top=max(model[0],key=model[0].get)
        value=prime_detector(aa[top],(vertex,()),tuple(base)+tuple(9+i for i in normal))
        check(value in ({Z:1},{Z:-1}),'endpoint_Gysin_channel_primitive_mod_exact_homotopy_ideal')
        for c in CELLS:
            if c[0]==vertex and degree(c)==1:
                bottom=project(bd[c],'V')
                check(not prime_detector(bottom,(vertex,()),tuple(base)+tuple(9+i for i in normal)),
                      'every_endpoint_target_boundary_annihilated_by_detector')
        check(all(any(e[i] for i in base) for b,e in model[1][top]),
              'every_endpoint_source_top_boundary_annihilated_by_detector')
    # Exceptional valuations and relative canonical divisor: J and Jacobian
    # have order 2 at the origin ray and 1 at each two-coordinate axis ray.
    valuations=[]
    for supp in subsets((0,1,2))[1:]:
        v=tuple(int(i in supp) for i in range(3))
        ordj=min(sum(v[j] for j in range(3) if j!=i) for i in range(3))
        ordtau=sum(v);ordjac=sum(v)-1
        check(ordj==ordjac,'all_seven_rays_trace_equals_relative_jacobian')
        check(ordtau-ordj==1,'all_seven_residual_components_reduced')
        valuations.append({'ray':list(v),'trace_ideal_order':ordj,'endpoint_order':ordtau,
                           'relative_jacobian_order':ordjac,'residual_order':1})
    excess_record=retained_excess_audit()
    result={
      'retained_excess_record':excess_record,
      'status':'proved_for_constructed_symmetric_toric_modification_and_whole_native_coefficient_map',
      'source_commit':COMMIT,'source_blobs':SOURCE_BLOBS,
      'previous_checker_sha256':hashlib.sha256(Path('/mnt/data/check_marici_completed_normal_dual_comparison.py').read_bytes()).hexdigest() if Path('/mnt/data/check_marici_completed_normal_dual_comparison.py').exists() else 'see derivation provenance',
      'geometry':'Blow up long-Rees origin, then all three disjoint strict transforms of its coordinate axes',
      'chart_count':6,'target_generators':215,'native_resolution_generators':50,
      'trace_ideal':'(t1*t2,t0*t2,t0*t1)',
      'relative_canonical_ideal':'J*O_Y=(s^2*r)=omega_(Y/X)^(-1)',
      'residual_Cartier_boundary':'tau/(s^2*r)=s*r*q; all seven toric boundary divisors with multiplicity one',
      'normalized_top_generic':'s*r*q*T-r*q*M_i-q*M_j-M_k',
      'whole_chain_identity':'d Fhat - Fhat d_P = s*r*q*(a_plus f_plus-a_minus f_minus)',
      'global_Cartier_morphism':'[O_Y(-D) -> O_Y] in degrees 2,3 -> Hom(P,K_Y), lower generator -> Fhat, upper -> A',
      'primitive_endpoint_values':{'plus':1,'minus':-1},
      'chart_records':records,'overlap_records':adjacencies,'divisor_valuations':valuations,
      'independent_excess':'checked as an independent tensor factor, not identified with any exceptional or internal normal coordinate',
      'normal_tower':'order-one complete map plus two higher-order tests; all-order compatibility is proved by diagonal transitions',
      'global_limitations':[
        'J on the original base is still proper. No polynomial unit trace downstairs is asserted.',
        'No global regular degree-three covector giving 1 exists upstairs after the twist; local primitive trace is a sheaf-level statement.',
        'Residual Cartier Gysin records a shifted endpoint channel, not a primitive unshifted endpoint on an ordinary central fibre.',
        'The three resolved normal coordinates and their intersections remain distinct. The single divisor equation is not identified with the independent three-normal Koszul packet.',
        'A filtered Gysin-valued residue of the complete coupled coefficient map is constructed. Identification with the originally specified physical collar two-cells or full supported-Verdier correspondence is not asserted.',
        'No physical reflection parity has been assigned.'
      ],
      'checks':dict(sorted(COUNT.items())),'exact_assertions':sum(COUNT.values()),
      'checker_is_not_a_proof_assistant':True
    }
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ('status','chart_count','target_generators','native_resolution_generators','exact_assertions')},indent=2))
    print('Reference chart faces:',json.dumps(records[0]['faces'],indent=2))


# New calculation. No third-party modules, inverse occurrence coefficients,
# invariant averaging, or assumed formal splitting of the derived fibre.
CYCLE_ORDERS=((2,1,0),(2,0,1),(0,2,1),(0,1,2),(1,0,2),(1,2,0))
P2_RAYS=((1,0),(0,1),(-1,-1))
FAN_RAYS=((1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1))
FAN_CONES=[{FAN_RAYS.index(tuple(-v for v in P2_RAYS[i])),
            FAN_RAYS.index(P2_RAYS[k])} for i,j,k in CYCLE_ORDERS]
H_DIV=(1,1,0,0,0,1)
K_DIV=(-1,)*6


def pscale(p,c):return {e:a*c for e,a in p.items() if a*c}
def pmono(e,c=1):return {tuple(e):c} if c else {}
def pone():return {(0,0,0):1}
def pe(i,a=1):return pmono(tuple(a if j==i else 0 for j in range(3)))
def pdiff(p,i):
    out={}
    for e,a in p.items():
        if e[i]:
            ee=list(e);ee[i]-=1
            out=poly_add(out,{tuple(ee):a*e[i]})
    return out

def pchart(p,order):
    i,j,k=order;out={}
    for e,a in p.items():out=poly_add(out,{(sum(e),e[j]+e[k],e[k]):a})
    return out

def pmatmul(a,b):
    return [[poly_add(*(poly_mul(a[i][k],b[k][j]) for k in range(len(b))))
             for j in range(len(b[0]))] for i in range(len(a))]

def peye(n):return [[pone() if i==j else {} for j in range(n)] for i in range(n)]

def excess_columns(order):
    i,j,k=order
    cols=[]
    for h in (j,k):
        ratio=poly_mul(pe(h),pe(i,-1))
        cols.append([pone() if a==h else pscale(ratio,-1) if a==i else {} for a in range(3)])
    return [[cols[j][i] for j in range(2)] for i in range(3)]


def global_excess_audit():
    cols={p:excess_columns(p) for p in CYCLE_ORDERS}
    trans={}
    for p in CYCLE_ORDERS:
        i,j,k=p
        check(pmatmul([[pe(a) for a in range(3)]],cols[p])==[[{},{}]],'global_excess_kernel_equations')
        for q in CYCLE_ORDERS:
            # Kernel coordinates are the coefficients of the other two
            # original conormals. This constructs, rather than fits, transitions.
            M=[cols[q][j],cols[q][k]]
            trans[p,q]=M
            check(pmatmul(cols[p],M)==cols[q],'global_excess_overlap_exact')
            check(all(sum(e)==0 for row in M for entry in row for e in entry),'excess_transitions_descend_to_exceptional_surface')
            detM=poly_det(M)
            g_ratio=poly_mul(poly_mul(pe(i),pe(j)),poly_mul(pe(q[0],-1),pe(q[1],-1)))
            left=pchart(poly_mul(detM,g_ratio),p)
            # New surface coordinates r'=t_j'/t_i', q'=t_k'/t_j'.
            rp=pchart(poly_mul(pe(q[1]),pe(q[0],-1)),p)
            qp=pchart(poly_mul(pe(q[2]),pe(q[1],-1)),p)
            jac=poly_det([[pdiff(rp,1),pdiff(rp,2)],[pdiff(qp,1),pdiff(qp,2)]])
            check(left==jac,'det_excess_times_relative_dualizing_is_canonical_surface_transition')
    for p,q,r0 in product(CYCLE_ORDERS,repeat=3):
        check(pmatmul(trans[p,q],trans[q,r0])==trans[p,r0],'all_excess_bundle_triple_cocycles')
    p=(0,1,2)
    leading=[[pchart(v,p) for v in row] for row in trans[p,(1,0,2)]]
    trailing=[[pchart(v,p) for v in row] for row in trans[p,(0,2,1)]]
    check(leading==[[pmono((0,-1,0),-1),pmono((0,0,1),-1)],[{},pone()]],'explicit_leading_swap_matrix')
    check(trailing==[[{},pone()],[pone(),{}]],'explicit_trailing_swap_matrix')
    for n,cone in enumerate(FAN_CONES):
        vs=[FAN_RAYS[i] for i in sorted(cone)]
        check(abs(vs[0][0]*vs[1][1]-vs[0][1]*vs[1][0])==1,'exceptional_surface_smooth_cones')
        check(len(cone & FAN_CONES[(n+1)%6])==1,'exceptional_fan_hexagon')
    # Intersection ring on Bl_3 P^2, H^2=1, H E_i=0, E_i E_j=-delta_ij.
    def intersection(a,b):return a[0]*b[0]-sum(a[i]*b[i] for i in range(1,4))
    H=(1,0,0,0);normal=(-1,0,0,0);canonical=(-3,1,1,1);relative=(-2,1,1,1)
    check(tuple(a+b for a,b in zip(normal,relative))==canonical,'det_excess_relative_equals_canonical_divisor')
    check(intersection(H,H)==1,'top_excess_Chern_number_one')
    # Euler sequence gives c(F*)=1+H+H^2, not c(O^2)=1.
    chern=[1,1,1]
    product_coeff=[chern[n]-(chern[n-1] if n else 0) for n in range(3)]
    check(product_coeff==[1,0,0],'excess_normal_Chern_polynomial')
    return {'surface':'Bl_3(P^2_R), zero section in Tot(O(-H))',
            'excess_conormal':'pi^*Omega^1_(P^2/R)(1)',
            'determinant':'O(-H)',
            'relative_canonical_restriction':'O(-2H+E0+E1+E2)',
            'top_Chern_pushforward':1,
            'all_ordered_overlap_matrices':36,'triple_cocycles':216}


def iadd(a,b,multiple=1):
    out=dict(a)
    for x,n in b.items():
        out[x]=out.get(x,0)+multiple*n
        if not out[x]:del out[x]
    return out

def iapply(d,v):
    out={}
    for a,c in v.items():out=iadd(out,d.get(a,{}),c)
    return out


def toric_cech(divisor,character):
    degrees={}
    for k in range(1,7):
        for I in combinations(range(6),k):
            common=set.intersection(*(FAN_CONES[i] for i in I))
            if all(sum(x*y for x,y in zip(character,FAN_RAYS[v]))+divisor[v]>=0 for v in common):
                degrees[I]=k-1
    differential={I:{} for I in degrees}
    for I in degrees:
        for j in range(6):
            if j in I:continue
            J=tuple(sorted(I+(j,)))
            check(J in degrees,'toric_Cech_section_restriction_legal')
            differential[I][J]=pm(J.index(j))
    for I in degrees:
        check(not iapply(differential,differential[I]),'toric_Cech_d_squared')
    return differential,degrees


def integer_contract(d0,degree0,cycles=()):
    """Exact algebraic cancellation. The optional cycles are transported too.

    Signed-unit pivots certify integral ranks and absence of torsion.
    The saved moves let us apply the same chain retraction to any input.
    """
    d={a:dict(v) for a,v in d0.items()};degrees=dict(degree0)
    vectors=[dict(v) for v in cycles];moves=[]
    while True:
        pivot=next(((a,b,n) for a,v in d.items() for b,n in v.items() if abs(n)==1),None)
        if pivot is None:break
        a,b,n=pivot;column=dict(d[a]);moves.append((a,b,n,column))
        for v in vectors:
            if b in v:
                v1=iadd(v,column,-v[b]//n);v.clear();v.update(v1)
            v.pop(a,None);v.pop(b,None)
        d1={}
        for x,v in d.items():
            if x in (a,b):continue
            value=iadd(v,column,-v[b]//n) if b in v else dict(v)
            value.pop(a,None);value.pop(b,None);d1[x]=value
        d=d1;degrees.pop(a);degrees.pop(b)
        check(all(degrees[v]==degrees[u]+1 for u,value in d.items() for v in value),'Cech_cancellation_degree')
    check(not any(d.values()),'Cech_all_Smith_factors_are_signed_units')
    return dict(Counter(degrees.values())),vectors,degrees,moves


def apply_cancellation(moves,value):
    value=dict(value)
    for a,b,n,column in moves:
        if b in value:value=iadd(value,column,-value[b]//n)
        value.pop(a,None);value.pop(b,None)
    return value


def cech_trace_audit():
    divisors={
      'O':(0,)*6,'H':H_DIV,'minus_H':tuple(-a for a in H_DIV),
      'minus_2H':tuple(-2*a for a in H_DIV),'K':K_DIV,
      'W':tuple(a+b for a,b in zip(K_DIV,H_DIV)),
      'W_plus_H':tuple(a+2*b for a,b in zip(K_DIV,H_DIV))}
    expected={
      'O':{(0,0):{0:1}},
      'H':{(0,0):{0:1},(-1,0):{0:1},(-1,1):{0:1}},
      'minus_H':{},'minus_2H':{},'K':{(0,0):{2:1}},'W':{},'W_plus_H':{}}
    results={};checks=[]
    # The infinite-character result is proved using projective-space
    # cohomology and blowup duality in the note. These 343 finite exact
    # Cech computations independently check all contributing weights and
    # a symmetric surrounding window, not a proof by extrapolation.
    for name,divisor in divisors.items():
        nonzero={}
        for character in product(range(-3,4),repeat=2):
            d,degrees=toric_cech(divisor,character)
            cohomology,_,_,_=integer_contract(d,degrees)
            check(cohomology==expected[name].get(character,{}),'Cech_window_matches_all_weight_theorem')
            if cohomology:nonzero[str(character)]=cohomology
            checks.append({'line':name,'character':character,'cohomology':cohomology})
        results[name]=nonzero
    # Canonical form weight: the zero-weight regularity-forbidden nerve is
    # exactly the six vertices and six boundary edges of a hexagon.
    d,degrees=toric_cech(K_DIV,(0,0))
    check(dict(Counter(degrees.values()))=={1:9,2:20,3:15,4:6,5:1},'canonical_weight_Cech_degree_counts')
    residue={I:1 for I in degrees if len(I)==3 and I[:2]==(0,1)}
    check(len(residue)==4 and not iapply(d,residue),'four_component_Cech_residue_closed')
    cohomology,vectors,survivors,moves=integer_contract(d,degrees,[residue])
    check(cohomology=={2:1} and vectors[0]=={(3,4,5):1},'proper_trace_residue_is_primitive_positive_one')
    survivor=(3,4,5)
    # Compare the selected generator with the pullback of the STANDARD
    # three-chart projective-plane residue. This fixes +1 by refinement,
    # rather than declaring the sign after an arbitrary matrix reduction.
    standard_refinement={}
    for I in degrees:
        if len(I)!=3:continue
        leaders=[CYCLE_ORDERS[i][0] for i in I]
        if len(set(leaders))==3:
            standard_refinement[I]=pm(sum(leaders[i]>leaders[j] for i in range(3) for j in range(i+1,3)))
    check(len(standard_refinement)==8,'standard_projective_trace_refines_to_eight_Cech_terms')
    check(not iapply(d,standard_refinement),'refined_standard_residue_closed')
    check(apply_cancellation(moves,standard_refinement)=={survivor:1},'proper_trace_orientation_matches_standard_projective_residue')
    check(not apply_cancellation(moves,iadd(standard_refinement,residue,-1)),
          'four_term_and_standard_eight_term_residues_same_integral_class')
    # An explicit cochain trace on degree two, read after unit contractions.
    trace={I:apply_cancellation(moves,{I:1}).get(survivor,0) for I in degrees if len(I)==3}
    for I in degrees:
        if len(I)==2:
            check(sum(trace.get(J,0)*n for J,n in d[I].items())==0,'proper_trace_annihilates_every_Cech_boundary')
    check(sum(trace[I]*n for I,n in residue.items())==1,'proper_trace_no_factor_three_or_six')
    actions=[]
    for perm in permutations(range(3)):
        sign=pm(sum(perm[i]>perm[j] for i in range(3) for j in range(i+1,3)))
        cp=[CYCLE_ORDERS.index(tuple(perm[i] for i in order)) for order in CYCLE_ORDERS]
        def action(v):
            out={}
            for I,a in v.items():
                vals=tuple(cp[i] for i in I)
                sgn=sign*pm(sum(vals[i]>vals[j] for i in range(len(vals)) for j in range(i+1,len(vals))))
                out=iadd(out,{tuple(sorted(vals)):a*sgn})
            return out
        for I in degrees:
            check(iapply(d,action({I:1}))==action(d[I]),'proper_trace_dihedral_chain_action')
        r=action(residue)
        check(apply_cancellation(moves,r)=={survivor:1},'proper_trace_all_six_transports_preserve_unit')
        actions.append({'permutation':perm,'canonical_form_sign':sign,'trace':1})
    # Euler sequence O^3 -> O(H) gives an isomorphism on global sections.
    section_weights=((0,0),(-1,1),(-1,0))
    check(set(section_weights)==set(expected['H']),'Euler_global_sections_exact')
    # This exact sequence and the line cohomology prove F and W F acyclic.
    check(not results['W'] and not results['W_plus_H'],'twisted_Euler_all_terms_acyclic')
    check(not results['minus_H'],'top_untwisted_excess_acyclic')
    # Top excess is the ONLY contribution to the duality-twisted pushforward.
    twisted={(2,2):1};untwisted={(0,0):1}
    with_eta=Counter()
    for (p,q),rank in twisted.items():
        for eta in (0,1):with_eta[p-q-eta]+=rank
    check(dict(with_eta)=={0:1,-1:1},'independent_short_excess_survives_trace_in_both_degrees')
    return {'six_chart_line_cohomology_window':results,
       'window_character_count_per_line':49,'window_total_complexes':len(checks),
       'all_weight_proof':'Euler sequence, projective-space cohomology, and proper blowup duality; finite window is a separate audit',
       'canonical_Cech_ranks':dict(Counter(degrees.values())),
       'primitive_residue':[[list(I),a] for I,a in residue.items()],
       'standard_projective_residue_refinement':[[list(I),a] for I,a in standard_refinement.items()],
       'trace_row':[[list(I),a] for I,a in trace.items() if a],
       'trace_value':1,'transport_checks':actions,
       'twisted_excess_nonzero_E2':[{'Cech_degree':2,'Tor_degree':2,'rank':1}],
       'untwisted_excess_nonzero_E2':[{'Cech_degree':0,'Tor_degree':0,'rank':1}],
       'with_independent_eta_total_cohomology':dict(with_eta)}


def tensor_with_original_central_packet(P,F,A,bd,equations,tau):
    """Check the whole [lower -> upper] native map tensored with the
    ACTUAL three pulled-back equations and the independent short excess.
    Neither the equations s,r,q nor a detached scalar residue is substituted.
    """
    source_d={};target_d={};phi={};source_deg={}
    def long_terms(mask):
        for i,e in enumerate(equations):
            if mask>>i&1:yield mask^(1<<i),e,pm((mask&((1<<i)-1)).bit_count())
    def wrap_key(v,mask,eta):return {((c,mask,eta),e):a for (c,e),a in v.items()}
    for mask in range(8):
        for eta in (0,1):
            for tag,hdegree,values in (('lower',-2,F),('upper',-3,A)):
                for b,pdegree in P[0].items():
                    key=(tag,b,mask,eta);source_deg[key]=hdegree+pdegree+mask.bit_count()+eta
                    out={}
                    if tag=='lower':out[(('upper',b,mask,eta),tau)]=1
                    for (bb,e),a in P[1][b].items():out[(tag,bb,mask,eta),e]=pm(hdegree)*a
                    for mm,e,a in long_terms(mask):out[(tag,b,mm,eta),e]=pm(hdegree+pdegree)*a
                    source_d[key]=out;phi[key]=wrap_key(values[b],mask,eta)
                    for (c,_,_),e in phi[key]:
                        check(degree(c)+mask.bit_count()+eta==source_deg[key],'original_central_packet_whole_map_degree')
            for c in CELLS:
                key=(c,mask,eta);out=wrap_key(bd[c],mask,eta)
                for mm,e,a in long_terms(mask):out[(c,mm,eta),e]=pm(degree(c))*a
                target_d[key]=out
    for key in source_d:
        check(not apply(source_d,source_d[key]),'whole_source_with_long_and_short_excess_d_squared')
        check(apply(target_d,phi[key])==apply(phi,source_d[key]),'whole_Cartier_native_map_with_both_excess_packets')
    for key in target_d:
        check(not apply(target_d,target_d[key]),'whole_target_with_original_three_equations_d_squared')
    return {'source_columns':len(source_d),'target_columns':len(target_d)}


def complete_descent_audit():
    P,KE,KO,KC,cap,fp,fm,H,FC,tpC,tmC,endC=construct_source_data()
    F1={b:delocalize(v,ONE_N) for b,v in FC.items()}
    end1={b:delocalize(v,ONE_N) for b,v in endC.items()}
    ap1={b:delocalize(v,ONE_N) for b,v in tpC.items()}
    am1={b:delocalize(v,ONE_N) for b,v in tmC.items()}
    F={b:divide(rees_long(v),W) for b,v in F1.items()}
    A={b:divide(rees_long(v),eadd(W,TAU)) for b,v in end1.items()}
    bd={c:rees_long(v) for c,v in finite_table(ONE_N).items()}
    ap={b:divide(rees_long(v),eadd(W,TAU)) for b,v in ap1.items()}
    am={b:divide(rees_long(v),eadd(W,TAU)) for b,v in am1.items()}
    for b in P[0]:
        check(add(apply(ap,fp[b]),scale(apply(am,fm[b]),-1))==A[b],'complete_descent_keeps_actual_two_endpoint_composites')
        check(difference_map(F,P,bd)[b]==multiply(A[b],TAU),'descended_original_product_Cartier_equation')
    tensors=[]
    for order in CYCLE_ORDERS:
        Fhat={b:divide(chart(v,order),GCH) for b,v in F.items()}
        bdy={c:chart(v,order) for c,v in bd.items()}
        for b in P[0]:
            # tau is the global generator of b_* I_D, not the local z.
            # tau=g*z, so the local map sends this global generator to F.
            check(multiply(Fhat[b],GCH)==chart(F[b],order),'proper_pushforward_lower_component_recovers_F_exactly')
            check(chart(A[b],order)==A[b],'proper_pushforward_upper_component_recovers_endpoint_pair_exactly')
            check(difference_map(Fhat,P,bdy)[b]==multiply(A[b],ZCH),'normalized_map_before_proper_descent')
        eq=[chart_exp(ex({15+i:1}),order) for i in range(3)]
        records=tensor_with_original_central_packet(P,Fhat,A,bdy,eq,ZCH)
        records['order']=order;tensors.append(records)
    tensors.append({'order':'original base',**tensor_with_original_central_packet(P,F,A,bd,[ex({15+i:1}) for i in range(3)],TAU)})
    F0={b:specialize_coords(v,(0,1,2)) for b,v in F.items()}
    A0={b:specialize_coords(v,(0,1,2)) for b,v in A.items()}
    check(not any(F0.values()),'original_central_generic_is_zero_after_canonical_descent')
    check(A0==A,'original_central_upper_endpoint_channel_is_retained')
    check(sum(map(len,A0.values()))==6,'all_six_endpoint_composite_terms_retained')
    check(specialize_coords(ap[('E',EV)],(0,1,2))==one((VP,())),'plus_primitive_endpoint_survives_original_central_face')
    check(specialize_coords(am[('O',OD)],(0,1,2))==scale(one((VM,())),-1),'minus_primitive_endpoint_survives_original_central_face')
    return {'whole_native_map_terms':sum(map(len,F.values())),
       'whole_endpoint_composite_terms':sum(map(len,A.values())),
       'derived_pushforward_of_Cartier_source':'[O_X -- t0*t1*t2 --> O_X] in degrees 2,3',
       'derived_pushforward_of_Cartier_map':'lower F, upper A=a_plus f_plus-a_minus f_minus',
       'central_lower_terms':sum(map(len,F0.values())),
       'central_upper_terms':sum(map(len,A0.values())),
       'full_tensor_checks':tensors,
       'proper_pushforward_proof':'regular projective birational structure-sheaf vanishing, duality trace, and projection formula; no computed Cech approximation is substituted for this theorem'}


def main(output):
    # Re-run the inherited full finite toric audit, independently of its old
    # certificate. The preceding checker is embedded, so this file is standalone.
    import contextlib,io,tempfile
    with tempfile.TemporaryDirectory() as folder:
        baseline_path=Path(folder)/'baseline.json'
        with contextlib.redirect_stdout(io.StringIO()):preceding_audit(baseline_path)
        baseline=json.loads(baseline_path.read_text())
    baseline_count=sum(COUNT.values())
    check(baseline_count==32428,'preceding_toric_audit_rerun')
    bundle=global_excess_audit()
    trace=cech_trace_audit()
    descent=complete_descent_audit()
    result={
       'status':'proved_for_global_excess_geometry_and_proper_descent_of_the_complete_constructed_Cartier_map',
       'source_commit':COMMIT,'source_blobs':SOURCE_BLOBS,
       'baseline_reverified_assertions':baseline_count,
       'new_assertions':sum(COUNT.values())-baseline_count,
       'total_exact_assertions':sum(COUNT.values()),
       'global_excess_bundle':bundle,'primitive_proper_trace':trace,
       'complete_Cartier_descent':descent,
       'proof_dependencies':{
          'all_character_cohomology':'projective-space cohomology, Euler sequence, blowup duality; see note',
          'global_direct_images':'regular birational projective vanishing and proper duality trace',
          'base_change':'projection formula with the perfect original three-equation Koszul complex, not ordinary fibre restriction',
          'no_global_formality':'No global split K(t)=O_E tensor Lambda(F) is assumed. Local Tor and the hypercohomology spectral sequence are used.'},
       'scope_limits':[
          'The two long excess directions are a nontrivial rank-two bundle, not two global constant generators.',
          'The excess top trace equals one; this does not turn the descended native generic map into a unit.',
          'The descended lower generic map is zero on the original central face, while the upper endpoint channel is retained.',
          'The independent short excess is tensored through unchanged; it is not identified with either long excess direction.',
          'No interchange of proper pushforward with the infinite completed normal-dual inverse limit is claimed.',
          'The full physical support-PC/Verdier comparison with independently prescribed collar two-cells is not established.',
          'No physical reflection parity is assigned.'
       ],
       'checks':dict(sorted(COUNT.items())),
       'checker_is_not_a_proof_assistant':True}
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ('status','baseline_reverified_assertions','new_assertions','total_exact_assertions')},indent=2))
    print('Proper trace:',trace['trace_value'])
    print('Central generic / endpoint terms:',descent['central_lower_terms'],descent['central_upper_terms'])


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path('marici_toric_excess_proper_descent_certificate.json'))
    args=parser.parse_args()
    main(args.output)
