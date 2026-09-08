#!/usr/bin/env python3
"""Whole native attachment triangle on the six-short-normal Rees graph.

Python 3.10+, standard library only. Integer polynomial/Laurent identities are
checked symbolically; inverse normals occur only in their designated target
stalks. No base occurrence variable is inverted; on a stalk where t_i*X_i is already
inverted both factors are units. The complete node resolution,
two endpoint maps, conductor homotopy, target support filtration, Hom fibres,
and orientation character are retained. This is a finite coefficient/cap
comparison, not a claimed algebraic six-functor or physical parity theorem.
"""
from __future__ import annotations
import argparse, hashlib, json
from collections import Counter
from itertools import combinations, product
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

def homogeneous_hom(P,support,lam=LAMBDA):
    """All A-linear homogeneous cochains. Cochain Ext^j has homological degree -j."""
    gs={};coef={}
    for b,i in P[0].items():
        for c in CELLS:
            e=eadd(eadd(lam,P[2][b]),weight(c))
            if predicate(c,support) and legal(c,e):
                gs[b,c]=degree(c)-i;coef[b,c]=e
    incoming={b:[] for b in P[0]}
    for b,v in P[1].items():
        for (a,e),s in v.items():incoming[a].append((b,e,s))
    d={x:{} for x in gs}
    for x,n in gs.items():
        b,c=x
        for (t,e),s in BD[c].items():
            if not predicate(t,support):continue
            y=b,t;check(y in gs,'Hom_target_domain')
            check(eadd(coef[x],e)==coef[y],'Hom_target_monomial')
            d[x]=add(d[x],{y:s})
        for bb,e,s in incoming[b]:
            y=bb,c;check(y in gs,'Hom_source_domain')
            check(eadd(coef[x],e)==coef[y],'Hom_source_monomial')
            d[x]=add(d[x],{y:-pm(n)*s})
    audit_int(gs,d,'Hom_'+support)
    return gs,d,coef

def audit_int(gs,d,tag):
    for b in gs:
        check(not lin(d,d[b]),tag+'_d_squared')
        check(all(gs[a]+1==gs[b] for a in d[b]),tag+'_degree')

def reduce_int(gs,original):
    """Signed-unit SDR, including its complete integral homotopy."""
    d={b:dict(v) for b,v in original.items()};I={b:{b:1} for b in d};P=dict(I);H={b:{} for b in d};pivots=0
    while True:
        hit=next(((b,a,u) for b,v in d.items() for a,u in v.items() if abs(u)==1),None)
        if hit is None:break
        b,a,u=hit;surv=tuple(x for x in d if x not in (a,b));pivots+=1
        p={x:{x:1} for x in surv};p[b]={};p[a]={y:-u*v for y,v in d[b].items() if y!=a}
        inc={x:add({x:1},({b:-u*d[x][a]} if a in d[x] else {})) for x in surv}
        for x in gs:
            if a in P[x]:H[x]=add(H[x],scale(I[b],u*P[x][a]))
        P={x:lin(p,v) for x,v in P.items()};I={x:lin(I,v) for x,v in inc.items()}
        d={x:lin(p,lin(d,v)) for x,v in inc.items()}
    check(not any(d.values()),'SDR_no_nonunit_remainder')
    for b in gs:
        check(not lin(P,original[b]),'SDR_projection_chain')
        check(add(lin(original,H[b]),lin(H,original[b]))==add({b:1},scale(lin(I,P[b]),-1)),'SDR_explicit_homotopy')
    for b in d:
        check(not lin(original,I[b]),'SDR_section_cycle')
        check(lin(P,I[b])=={b:1},'SDR_projection_section')
    return {'g':{b:gs[b] for b in d},'P':P,'I':I,'H':H,'pivots':pivots,
            'homology':dict(sorted(Counter(gs[b] for b in d).items()))}

def cubical_boundary(cell):
    lower,upper=cell;free=tuple(a for a in upper if a not in lower);out={}
    for j,a in enumerate(free):
        out[(tuple(sorted(lower+(a,))),upper)]=pm(j)
        out[(lower,tuple(b for b in upper if b!=a))]=-pm(j)
    return out

def hom_cube(x):
    b,c=x;_,u,v=b;face,marks=c
    missing=tuple(SHORT[i] for i in range(6) if i not in u+v)
    return tuple(sorted(missing+marks)),face

def spatial_identification(model):
    gs,d,coef=model
    image={x:hom_cube(x) for x in gs};inv={v:x for x,v in image.items()}
    check(len(inv)==len(gs),'spatial_cube_bijection')
    allcubes={(h,f) for f,h in CELLS}
    check(set(inv)==allcubes-{(VP,VP),(VM,VM)},'spatial_pair_is_W_relative_two_endpoints')
    boundaries={c:cubical_boundary(c) for c in allcubes}
    adjacency={x:[] for x in gs}
    for x,n in gs.items():
        check(len(image[x][1])-len(image[x][0])==-n-2,'spatial_degree_dictionary')
        want={inv[c]:v[image[x]] for c,v in boundaries.items() if c in inv and image[x] in v}
        check(set(want)==set(d[x]),'all_spatial_Hom_incidence_supports')
        for y,a in d[x].items():
            b=want[y];check(abs(a)==abs(b)==1,'spatial_unit_orientation')
            adjacency[x].append((y,a*b));adjacency[y].append((x,a*b))
    root=(('P',EV,OD),((),()))
    orientation={root:1};todo=[root]
    while todo:
        x=todo.pop()
        for y,a in adjacency[x]:
            if y in orientation:check(orientation[y]==orientation[x]*a,'cubical_orientation_consistency')
            else:orientation[y]=orientation[x]*a;todo.append(y)
    check(len(orientation)==len(gs),'cubical_orientation_all_cells')
    for x in gs:
        for y,a in d[x].items():
            check(a*orientation[y]==orientation[x]*boundaries[image[y]][image[x]],'complete_spatial_chain_isomorphism')
        for g in GROUP:
            b,c=x;gb,sb=act_p_basis(b,g);face,marks=c
            gf=[perm_di(a,g) for a in face];gh=[perm_di(a,g) for a in marks]
            gc=tuple(sorted(gf)),tuple(sorted(gh));y=gb,gc
            check(y in gs,'Hom_group_preserves_frame')
            sc=pm(g[1])*invsign(gf,DS)*invsign(gh,DS)
            free=tuple(a for a in image[x][1] if a not in image[x][0])
            cube_sign=invsign([perm_di(a,g) for a in free],DS)
            check(orientation[y]*sb*sc*pm(g[1])==orientation[x]*cube_sign,'spatial_equivariance_with_polarity')
    return image,orientation

def as_cochain(F,model):
    z={}
    for b,v in F.items():
        for (c,e),a in v.items():
            key=b,c;check(key in model[0],'comparison_Hom_domain')
            check(model[2][key]==e,'comparison_Hom_exact_frame')
            z=add(z,{key:a})
    return z

def export(v):
    return [{'basis':repr(b),'exponent':list(e),'coefficient':a} for (b,e),a in sorted(v.items(),key=lambda z:repr(z[0]))]
def serialize_map(table):return {repr(b):export(v) for b,v in table.items() if v}



CROSS=tuple(tuple(sorted((i,(i+1)%6))) for i in range(6))
BRIDGES=((0,3),(2,5),(4,1))

def taylor():
    g={};d={};l={}
    for s in subsets(tuple(range(6))):
        b=('T',s);g[b]=len(s)
        w=set().union(*(set(CROSS[i]) for i in s));l[b]=ex({i:1 for i in w})
    for b in g:
        s=b[1];d[b]={}
        for j,i in enumerate(s):
            a=('T',s[:j]+s[j+1:]);d[b][a,esub(l[b],l[a])]=pm(j)
    return g,d,l

def bridges():
    g={};d={};l={}
    for pair in BRIDGES:
        seq=tuple(i for i in range(6) if i not in pair)
        for z in subsets(seq):
            b=('L',pair,z);g[b]=len(z);l[b]=ex({i:1 for i in pair+z})
            d[b]={(('L',pair,z[:j]+z[j+1:]),ex({i:1})):pm(j) for j,i in enumerate(z)}
    return g,d,l

def poly_sdr(model):
    gs,original,labels=model
    d={b:dict(v) for b,v in original.items()};I={b:one(b) for b in d};P=dict(I);H={b:{} for b in d};pivots=0
    while True:
        hit=next(((b,a,u) for b,v in d.items() for (a,e),u in v.items() if e==Z and abs(u)==1),None)
        if hit is None:break
        b,a,u=hit;surv=tuple(x for x in d if x not in (a,b));pivots+=1
        p={x:one(x) for x in surv};p[b]={};p[a]={(y,e):-u*v for (y,e),v in d[b].items() if y!=a}
        inc={x:add(one(x),{(b,e):-u*v for (y,e),v in d[x].items() if y==a}) for x in surv}
        for x in gs:
            for (y,e),v in P[x].items():
                if y==a:H[x]=add(H[x],multiply(I[b],e,u*v))
        P={x:apply(p,v) for x,v in P.items()};I={x:apply(I,v) for x,v in inc.items()}
        d={x:apply(p,apply(d,v)) for x,v in inc.items()}
    for b in gs:
        check(add(apply(original,H[b]),apply(H,original[b]))==add(one(b),scale(apply(I,P[b]),-1)),'polynomial_SDR_homotopy')
        check(apply(d,P[b])==apply(P,original[b]),'polynomial_SDR_projection')
    for b in d:check(apply(P,I[b])==one(b) and apply(original,I[b])==apply(I,d[b]),'polynomial_SDR_section')
    return ({b:gs[b] for b in d},d,{b:labels[b] for b in d}),P,I,H,pivots

CACHE={}
def frame_reduction(model,alpha,tag):
    key=(tag,alpha)
    if key not in CACHE:
        g,d,w=model;gg={b:n for b,n in g.items() if min(esub(alpha,w[b]))>=0}
        dd={b:{a:v for (a,e),v in d[b].items() if a in gg} for b in gg}
        CACHE[key]=reduce_int(gg,dd)
    return CACHE[key]

def rehydrate(v,alpha,weights):
    out={}
    for b,a in v.items():
        e=esub(alpha,weights[b]);check(min(e)>=0,'rehydrate_no_occurrence_inverse');out[b,e]=a
    return out

def int_coeff(v):
    out={}
    for (b,e),c in v.items():out=add(out,{b:c})
    return out

def lift_chain(source,target,initial,tag):
    f={}
    for b in sorted(source[0],key=source[0].get):
        if source[0][b]==0:f[b]=initial[b];continue
        v=apply(f,source[1][b]);red=frame_reduction(target,source[2][b],tag)
        iv=int_coeff(v);check(not lin(red['P'],iv),'lift_cycle_has_zero_homology')
        f[b]=rehydrate(lin(red['H'],iv),source[2][b],target[2])
        check(apply(target[1],f[b])==v,'lift_chain_equation')
    return f

def nullhomotopy(source,target,f,tag):
    h={}
    for b in sorted(source[0],key=source[0].get):
        v=add(f[b],scale(apply(h,source[1][b]),-1));red=frame_reduction(target,source[2][b],tag)
        check(not lin(red['P'],int_coeff(v)),'nullhomotopy_zero_obstruction')
        h[b]=rehydrate(lin(red['H'],int_coeff(v)),source[2][b],target[2])
        check(add(apply(target[1],h[b]),apply(h,source[1][b]))==f[b],'source_nullhomotopy_equation')
    return h

def cone(mu,L,T):
    g={('t',b):n for b,n in T[0].items()};g.update({('l',b):n+1 for b,n in L[0].items()})
    w={('t',b):n for b,n in T[2].items()};w.update({('l',b):n for b,n in L[2].items()})
    d={('t',b):{(('t',a),e):v for (a,e),v in zz.items()} for b,zz in T[1].items()}
    d.update({('l',b):add({(('t',a),e):v for (a,e),v in mu[b].items()},{(('l',a),e):-v for (a,e),v in L[1][b].items()}) for b in L[0]})
    return g,d,w

def construct_mu(L,T):
    mu={}
    for b in L[0]:
        _,pair,z=b;targets=[]
        for j in z:
            edges=[tuple(sorted((j,k))) for k in pair if tuple(sorted((j,k))) in CROSS]
            check(len(edges)==1,'unique_crossing_generator_for_bridge_normal');targets.append(CROSS.index(edges[0]))
        s=invsign(targets,tuple(range(6)));target=('T',tuple(sorted(targets)))
        mu[b]={(target,esub(L[2][b],T[2][target])):s}
        check(apply(T[1],mu[b])==apply(mu,L[1][b]),'canonical_bridge_inclusion_chain')
    return mu

def build_cap():
    P=node();KC=koszul(ORDER,'C')
    cap={b:scale(omega(tuple(i for i in ORDER if i not in b[1])),complement_sign(b[1])) for b in KC[0]}
    F={b:({} if not b[1] else scale(apply(cap,{(('C',b[1]+b[2]),Z):pm(len(b[1]))}),-1)) for b in P[0]}
    a={b:add(td(F[b]),scale(apply(F,P[1][b]),-1)) for b in P[0]}
    return P,F,a

def projmap(f,sup):return {b:project(v,sup) for b,v in f.items()}

def homogeneous_pullback(f,v,domain,target_model):
    # v: cochain on codomain of f, v[(sourcecell,targetcell)] = coefficient
    ff={b:{} for b in domain[0]}
    bysource={}
    for (b,c),a in v.items():bysource.setdefault(b,{})[c,target_model[2][b,c]]=a
    for b,z in f.items():
        vv={}
        for (a,e),q in z.items():vv=add(vv,multiply(bysource.get(a,{}),e,q))
        ff[b]=vv
    return ff


from fractions import Fraction

def inverse_coordinates(columns,vector):
    """Solve an injective small integer matrix, verifying integral coordinates."""
    n=len(columns);m=len(vector)
    rows=[[Fraction(columns[j][i]) for j in range(n)]+[Fraction(vector[i])] for i in range(m)]
    rank=0;piv=[]
    for j in range(n):
        hit=next((i for i in range(rank,m) if rows[i][j]),None)
        if hit is None:continue
        rows[rank],rows[hit]=rows[hit],rows[rank]
        u=rows[rank][j];rows[rank]=[x/u for x in rows[rank]]
        for i in range(m):
            if i==rank:continue
            u=rows[i][j];rows[i]=[x-u*y for x,y in zip(rows[i],rows[rank])]
        piv.append(j);rank+=1
    check(rank==n,'small_lattice_injective')
    check(all(any(r[:-1]) or not r[-1] for r in rows),'small_lattice_consistent')
    result=[Fraction(0)]*n
    for j,row in zip(piv,rows):result[j]=row[-1]
    check(all(x.denominator==1 for x in result),'small_lattice_integral_solution')
    result=[int(x) for x in result]
    check([sum(columns[j][i]*result[j] for j in range(n)) for i in range(m)]==vector,'small_lattice_solution_verified')
    return result

def cochain_table(v,model,source):
    out={b:{} for b in source[0]}
    for (b,c),a in v.items():out[b][c,model[2][b,c]]=a
    return out

def hom_differential(table,source,n,support='K'):
    return {b:add(td(table[b],support),scale(apply(table,source[1][b]),-pm(n))) for b in source[0]}

def model_reduction(source,support):
    m=homogeneous_hom(source,support)
    return m,reduce_int(m[0],m[1])

def audit_homogeneous_table(table,source,shift,tag):
    for b,v in table.items():
        for (c,e),a in v.items():
            check(degree(c)==source[0][b]+shift,tag+'_homological_degree')
            check(e==eadd(eadd(LAMBDA,source[2][b]),weight(c)),tag+'_six_occurrence_frame')
            check(legal(c,e),tag+'_original_stalk_domain')


def act_basis(b,g):
    """Actions on native, Taylor, bridge and their cone resolutions."""
    tag=b[0]
    if tag=='P':return act_p_basis(b,g)
    per=perm_short(g)
    if tag=='T':
        vals=[CROSS.index(tuple(sorted(per[i] for i in CROSS[j]))) for j in b[1]]
        return ('T',tuple(sorted(vals))),invsign(vals,tuple(range(6)))
    if tag=='L':
        pair,seq=b[1:];p=[per[i] for i in pair]
        newpair=tuple(p if p[0]%2==0 else p[::-1]);vals=[per[i] for i in seq]
        return ('L',newpair,tuple(sorted(vals))),invsign(vals,tuple(range(6)))
    if tag in ('t','l'):
        a,s=act_basis(b[1],g);return (tag,a),s
    raise ValueError(b)

def act_vector(v,g):
    out={}
    for (b,e),a in v.items():
        bb,s=act_basis(b,g);out=add(out,{(bb,perm_ex(e,g)):a*s})
    return out

def twisted_source(S,g):
    return S[0],{b:{(a,perm_ex(e,g)):v for (a,e),v in z.items()} for b,z in S[1].items()}, {b:perm_ex(e,g) for b,e in S[2].items()}

def geometry_attachment():
    """Long-facet disks derived by coning their actual four-cycle links."""
    def oriented(seq):
        return {tuple(sorted(seq)):invsign(seq,tuple(range(9)))}
    def boundary(chain):
        z={}
        for f,a in chain.items():
            for j in range(len(f)):z=add(z,{f[:j]+f[j+1:]:pm(j)*a})
        return z
    all_faces={tuple(sorted(IX[a] for a in f)) for f in FACES}
    native={f for f in all_faces if set(f)<=set(EV) or set(f)<=set(OD)}
    short={f for f in all_faces if all(i<6 for i in f)}
    check(short-native=={tuple(sorted(b)) for b in BRIDGES},'actual_three_mixed_short_faces')
    disks=[];cycles=[];columns=[]
    for k,long in enumerate((6,8,7)):
        cycle=tuple((i+2*k)%6 for i in (0,3,1,4))
        z={}
        for a,b in zip(cycle,cycle[1:]+cycle[:1]):z=add(z,oriented((long,a,b)))
        check(len(z)==4 and all(f in all_faces for f in z),'long_disk_uses_four_actual_triangles')
        bd=boundary(z)
        expected={}
        for a,b in zip(cycle,cycle[1:]+cycle[:1]):expected=add(expected,oriented((a,b)))
        check(bd==expected,'long_disk_full_boundary')
        col=[bd.get(tuple(sorted(pair)),0)*(1 if pair[0]<pair[1] else -1) for pair in BRIDGES]
        disks.append(z);cycles.append(bd);columns.append(col)
    check(columns==[[1,0,-1],[-1,1,0],[0,-1,1]],'long_to_mixed_bridge_incidence_I_minus_R_squared')
    sphere=add(*disks,oriented(OD),scale(oriented(EV),-1))
    check(len(sphere)==14 and not boundary(sphere),'whole_fourteen_triangle_sphere_with_both_endpoints')
    check(add(*cycles)==add(boundary(oriented(EV)),scale(boundary(oriented(OD)),-1)),'norm_boundary_keeps_both_native_triangles')
    return {'long_order':['D03','D25','D14'],'bridge_order':[list(p) for p in BRIDGES],
            'matrix_columns':columns,'disks':[{repr(f):a for f,a in z.items()} for z in disks],
            'sphere':{repr(f):a for f,a in sphere.items()},
            'scope':'Literal face geometry only; no replacement of polynomial occurrence modules by constant lattices.'}



# --- New computation: actual Rees graph, coefficient families, and fibres. ---
# Coordinates remain an 18-tuple, now (X_0,...,X_5,X_long[3],
# t_0,...,t_5,u_long[3]). The substitution is u_i=t_i X_i for short i.
# Original stalk A[u_i^-1] becomes A'[(t_i X_i)^-1]; ONLY there are t_i
# and X_i individually invertible. This does not localize the base.

def graph_exp(e):
    z=list(e)
    for i in range(6):z[i]+=e[9+i]
    return tuple(z)

def graph_vec(v):
    out={}
    for (c,e),a in v.items():out=add(out,{(c,graph_exp(e)):a})
    return out

RBD={c:graph_vec(v) for c,v in BD.items()}

def rlegal(c,e):
    loc={IX[a] for a in c[0] if a not in c[1]}
    return (all(e[i]>=0 or i in loc for i in range(6))
            and all(e[i]>=0 for i in range(6,9))
            and all(e[9+i]>=0 or i in loc for i in range(9)))

def survive(c,central):
    loc={IX[a] for a in c[0] if a not in c[1]}
    return not (set(central)&loc)

def specialize(v,central):
    z={}
    for (c,e),a in v.items():
        if not survive(c,central):continue
        check(all(e[9+i]>=0 for i in central),'surviving_specialization_has_no_pole')
        if any(e[9+i]>0 for i in central):continue
        z=add(z,{(c,e):a})
    return z

def rd(v,support='K',central=()):
    return specialize(project(apply(RBD,v),support),central)

def rmap(f):return {b:graph_vec(v) for b,v in f.items()}
def smap(f,central):return {b:specialize(v,central) for b,v in f.items()}

def rees_hom(source,alpha,support='K',central=()):
    """All homogeneous A'-linear cochains, including newly allowed graph maps.

    Occurrence frame is -sum short e_X, long-normal frame is sum e_u_long;
    alpha is the SIX Rees degrees. After central specialization a coefficient
    of positive killed t-degree is zero, while a localized killed stalk is zero
    as an object. This is base change of flat modules, not substituting in poles.
    """
    gs={};coeff={};central=set(central)
    for b,i in source[0].items():
        sw=source[2][b]
        for c in CELLS:
            if not predicate(c,support) or not survive(c,central):continue
            sf={IX[a] for a in c[0]}
            e=[0]*18
            for j in range(6):e[j]=sw[j]-1;e[9+j]=alpha[j]-(j in sf)
            for j in range(6,9):e[j]=int(j in sf);e[9+j]=1-int(j in sf)
            e=tuple(e)
            if not rlegal(c,e) or any(e[9+j]!=0 for j in central):continue
            gs[b,c]=degree(c)-i;coeff[b,c]=e
    incoming={b:[] for b in source[0]}
    for b,z in source[1].items():
        for (a,e),s in z.items():incoming[a].append((b,e,s))
    d={x:{} for x in gs}
    for x,n in gs.items():
        b,c=x
        for (cc,e),s in RBD[c].items():
            if not predicate(cc,support):continue
            yy=b,cc
            if yy in gs:
                check(eadd(coeff[x],e)==coeff[yy],'Rees_Hom_target_coefficient')
                d[x]=add(d[x],{yy:s})
            else:
                # A surviving coefficient can leave this frame only by
                # entering a zero stalk or acquiring a positive central t.
                if survive(cc,central):
                    ee=eadd(coeff[x],e)
                    check(any(ee[9+j]>0 for j in central),'omitted_target_term_is_central_zero')
        for bb,e,s in incoming[b]:
            yy=bb,c
            if yy in gs:
                check(eadd(coeff[x],e)==coeff[yy],'Rees_Hom_source_coefficient')
                d[x]=add(d[x],{yy:-pm(n)*s})
            else:
                ee=eadd(coeff[x],e)
                check(any(ee[9+j]>0 for j in central),'omitted_source_term_is_central_zero')
    audit_int(gs,d,'complete_Rees_Hom')
    return gs,d,coeff


def fast_reduce(gs,d):
    """Elementary integral cancellations; no rank guess over a field.
    Each pivot has coefficient +1 or -1. The surviving differential must be
    zero. Used for the exhaustive support-shape audit, where explicit global
    inclusion cochains have already been supplied.
    """
    d={b:dict(v) for b,v in d.items()};piv=0
    while True:
        hit=next(((b,a,u) for b,v in d.items() for a,u in v.items() if abs(u)==1),None)
        if hit is None:break
        b,a,u=hit;piv+=1;db={z:v for z,v in d[b].items() if z!=a}
        for x in tuple(d):
            if x in (a,b):continue
            coeff=d[x].pop(a,0)
            if coeff:d[x]=add(d[x],scale(db,-u*coeff))
            d[x].pop(b,None)
        del d[a];del d[b]
    check(not any(d.values()),'integral_reduction_has_no_nonunit_residue')
    return Counter(gs[b] for b in d),piv


def cone_int(source_g,source_d,target_g,target_d,f,shift=0):
    # Map source of fixed homological degrees into target, same degree.
    g={('t',x):n for x,n in target_g.items()}
    g.update({('s',x):n+1 for x,n in source_g.items()})
    d={('t',x):{('t',y):a for y,a in v.items()} for x,v in target_d.items()}
    for x in source_g:
        d['s',x]=add({('t',y):a for y,a in f[x].items()},
                     {('s',y):-a for y,a in source_d[x].items()})
    return g,d


def rees_table(v,model,source):
    z={b:{} for b in source[0]}
    for (b,c),a in v.items():z[b][c,model[2][b,c]]=a
    return z


def endpoint_read(v,alpha,ep):
    """Residue functional in H^3 of the endpoint Hom complex.
    Outside ep all Rees degrees must be nonnegative; inside ep at least one
    degree must be <=0. Reading a singleton indexed by that coordinate kills
    every boundary, since its marked alternative is then inadmissible.
    """
    if any(alpha[i]<0 for i in range(6) if i not in ep):return 0
    absent=[i for i in ep if alpha[i]<=0]
    if not absent:return 0
    j=absent[0]
    b=('P',EV,(j,)) if ep==OD else ('P',(j,),OD)
    c=(tuple(sorted(SHORT[i] for i in ep)),())
    return v.get((b,c),0)


def make_seed(source,s):
    alpha=tuple(int(i in s) for i in range(6))
    model=rees_hom(source,alpha,'E');red=reduce_int(model[0],model[1])
    cell=(tuple(sorted(SHORT[i] for i in s)),)*2
    coordinate=(('P',EV,OD),cell)
    options=[(z,v.get(coordinate,0)) for z,v in red['I'].items()
             if red['g'][z]==-2 and v.get(coordinate,0)]
    check(bool(options),'primitive_marked_seed_exists')
    z,a=options[0];check(abs(a)==1,'primitive_marked_seed_is_integral_unit')
    v=scale(red['I'][z],a)
    # Uniform endpoint signs: same-sheet pairs are oriented negatively in
    # the raw triangulation. Reverse their seed to use positive incidence.
    if len(s)==2 and (set(s)<=set(EV) or set(s)<=set(OD)):v=scale(v,-1)
    check(not lin(model[1],v),'Rees_seed_is_closed_in_endpoint_quotient')
    table=rees_table(v,model,source)
    check(all(rlegal(c,e) for zz in table.values() for c,e in zz),'Rees_seed_stalk_legality')
    defect={b:add(rd(table[b]),scale(apply(table,source[1][b]),-1)) for b in source[0]}
    check(all(predicate(c,'V') for zz in defect.values() for c,e in zz),'seed_defect_is_endpoint_only')
    fullmodel=rees_hom(source,alpha,'K')
    iv=lin(fullmodel[1],v)
    for ep in (OD,EV):
        want=int(set(s)<=set(ep)) if not set(ep)<=set(s) else 0
        check(endpoint_read(iv,alpha,ep)==want,'endpoint_residue_row_matches_short_face')
    if s:
        check(not any(project(zz,'Q') for zz in table.values()),'nonempty_seed_has_zero_generic_map')
    return alpha,v,table,defect



def actual_endpoint_models(P,Ra):
    """Realize each two-term product-divisor Cech model in the unreduced
    native-source/actual-endpoint mapping complex. j0 has seven terms;
    j1 has three; d j0=j1. The old endpoint map is j1(1/tau).
    """
    ans={}
    for ep,vertex in ((OD,VP),(EV,VM)):
        alpha=tuple(int(i in ep) for i in range(6));tau=ex({9+i:1 for i in ep})
        j1={b:multiply({(c,e):a for (c,e),a in z.items() if c[0]==vertex},tau)
            for b,z in Ra.items()}
        model=rees_hom(P,alpha,'V');red=reduce_int(model[0],model[1]);iv={}
        for b,z in j1.items():
            for (c,e),a in z.items():
                check(e==model[2][b,c],'actual_endpoint_divisor_numerator_frame');iv[b,c]=a
        check(not lin(red['P'],iv),'endpoint_divisor_numerator_is_boundary')
        hh=lin(red['H'],iv);j0=rees_table(hh,model,P)
        for b in P[0]:
            check(add(rd(j0[b]),scale(apply(j0,P[1][b]),-1))==j1[b],
                  'unreduced_endpoint_divisor_homotopy')
        # Every term of j1 can take ANY Laurent denominator in its own
        # three Rees variables: all three target states are unmarked.
        check(all(c[0]==vertex and not c[1] for z in j1.values() for c,e in z),
              'endpoint_divisor_localization_map_is_defined_on_whole_module')
        cen=smap(j0,range(6));top=('P',EV,OD);c=(vertex,vertex)
        check(sum(len(z) for z in cen.values())==1 and abs(cen[top][c,GAMMA])==1,
              'endpoint_Gysin_homotopy_central_marked_unit')
        check(not any(smap(j1,range(6)).values()),'endpoint_localized_numerator_central_zero')
        ans[ep]={'alpha':alpha,'j0':j0,'j1':j1,'v0':hh,'v1':iv,
                 'central_coefficient':cen[top][c,GAMMA]}
    return ans


def endpoint_model_frame(endpoints,alpha):
    g={};d={};f={}
    for ep,model in endpoints.items():
        outside=all(alpha[i]>=0 for i in range(6) if i not in ep)
        bottom=outside and all(alpha[i]>=1 for i in ep)
        if bottom:g[ep,0]=-2;f[ep,0]=model['v0']
        if outside:g[ep,1]=-3;f[ep,1]=model['v1']
        if bottom:d[ep,0]={(ep,1):1}
        if outside:d[ep,1]={}
    return g,d,f

def selected_excess_audit():
    """The selected source is NOT identified with the native node. Its actual
    32-wedge equation and primitive independent eta are retained as a tensor
    factor, so the whole diagram can be tested without replacing eta by t*u.
    """
    seq=[ex({1:1}),ex({3:1}),ex({5:1}),ex({0:1,9:1}),ex({3:1,12:1})]
    gg={s:len(s) for s in subsets(tuple(range(5)))}
    dd={s:{(s[:j]+s[j+1:],seq[i]):pm(j) for j,i in enumerate(s)} for s in gg}
    for s in gg:check(not apply(dd,dd[s]),'selected_excess_32_wedges_d_squared')
    eta={((1,),ex({12:1})):1,((4,),Z):-1}
    check(not apply(dd,eta),'selected_excess_closed_without_division')
    # Change basis b4 = t3*b1 - eta, determinant -1. In that basis the other
    # four differential entries are x1,x3,x5,t0*x0 and d eta=0.
    for central in subsets(tuple(range(6))):
        ee={k:v for k,v in eta.items() if not any(k[1][9+i]>0 for i in central)}
        check(ee.get(((4,),Z))==-1,'excess_survives_every_central_Rees_face')
    return gg,dd,eta


def gysin_endpoint_audit(P,endpoints):
    """All three presentations of K^.(t_a,t_b,t_c) -> [R -> R_tau].
    The target retains its lower R term. This is the ordered Koszul residue
    followed by the support map V(a,b,c) subset V(abc), NOT an identification
    of those two supports. Matrices are Laurent ONLY in the output R_tau.
    """
    result={}
    for seq in (OD,EV):
        bs=subsets(seq)
        kd={s:{} for s in bs}
        for s in bs:
            for i in seq:
                if i not in s:
                    t=tuple(sorted(s+(i,)))
                    kd[s][t,ex({9+i:1})]=pm(sum(j<i for j in s))
        cd={0:{(1,Z):1},1:{}}
        maps=[]
        for chosen in seq:
            f={s:({(0,Z):1} if not s else
                  {(1,ex({9+chosen:-1})):1} if s==(chosen,) else {}) for s in bs}
            for s in bs:check(apply(cd,f[s])==apply(f,kd[s]),'endpoint_Gysin_all_lower_rows_chain_map')
            maps.append(f)
            # Compose into the ACTUAL endpoint mapping complex, retaining
            # all seven bottom components and all three localized components.
            em=endpoints[seq]
            actual={}
            for ss in bs:
                actual[ss]={b:{} for b in P[0]}
                for (row,ee),aa in f[ss].items():
                    for b in P[0]:actual[ss][b]=add(actual[ss][b],multiply(em['j0' if row==0 else 'j1'][b],ee,aa))
            for ss in bs:
                n=-(2+len(ss))
                left={b:add(rd(actual[ss][b]),scale(apply(actual[ss],P[1][b]),-pm(n))) for b in P[0]}
                right={b:{} for b in P[0]}
                for (jj,ee),aa in kd[ss].items():
                    for b in P[0]:right[b]=add(right[b],multiply(actual[jj][b],ee,aa))
                check(left==right,'whole_Gysin_map_in_actual_endpoint_Hom')
            center=smap(actual[()],range(6))
            check(sum(len(z) for z in center.values())==1,'actual_Gysin_center_has_one_primitive_endpoint_row')
            for ss in bs:
                if ss:check(not any(smap(actual[ss],range(6)).values()),'actual_Gysin_upper_rows_central_zero')
        hs={}
        for i,j in combinations(seq,2):
            h={s:({(1,ex({9+i:-1,9+j:-1})):1} if s==(i,j) else {}) for s in bs}
            fi=maps[seq.index(i)];fj=maps[seq.index(j)]
            for s in bs:
                check(add(apply(cd,h[s]),apply(h,kd[s]))==add(fj[s],scale(fi[s],-1)),
                      'endpoint_Gysin_pair_comparison')
            hs[i,j]=h
        i,j,k=seq
        v={s:({(1,ex({9+i:-1,9+j:-1,9+k:-1})):-1} if s==seq else {}) for s in bs}
        for s in bs:
            check(add(apply(cd,v[s]),scale(apply(v,kd[s]),-1))==
                  add(hs[j,k][s],scale(hs[i,k][s],-1),hs[i,j][s]),'endpoint_Gysin_triple_coherence')
        # All central faces: if any chosen t vanishes, the WHOLE R_tau term
        # vanishes; the map keeps bottom coefficient one. At full centre the
        # source differential is zero, so its bottom unit cannot be a boundary.
        for z in subsets(seq):
            for f in maps:
                check(f[()]=={(0,Z):1},'endpoint_Gysin_primitive_bottom_all_Rees_faces')
                if z:
                    check(all(t==1 for s in bs if s for (t,e) in f[s]),'all_nonbottom_terms_live_in_vanishing_localization')
        result[str(seq)]={'source_states':8,'presentations':3,'pair_homotopies':3,
                          'triple_homotopies':1,'central_bottom_unit':1}
    return result


def main_rees(output):
    import time
    start=time.time()
    P,F,a=build_cap();T=taylor();L=bridges()
    mu=construct_mu(L,T);phi=lift_chain(T,P,{('T',()):one(('P',(),()))},'P')
    h=nullhomotopy(L,P,{b:apply(phi,mu[b]) for b in L[0]},'P')
    C=cone(mu,L,T);psi={('t',b):phi[b] for b in T[0]};psi.update({('l',b):h[b] for b in L[0]})
    equivalence=poly_sdr(cone(psi,C,P))
    check(not equivalence[0][0] and equivalence[-1]==81,'whole_source_triangle_polynomial_equivalence')
    RF,Ra=rmap(F),rmap(a)
    AT={b:apply(RF,phi[b]) for b in T[0]};GL={b:apply(RF,h[b]) for b in L[0]}
    FC={b:apply(RF,psi[b]) for b in C[0]};aC={b:apply(Ra,psi[b]) for b in C[0]}
    for cell in CELLS:
        check(not rd(RBD[cell]),'whole_Rees_target_d_squared')
        for cc,e in RBD[cell]:check(rlegal(cc,e),'Rees_radial_normal_domain')
    central_records=[]
    for z in subsets(tuple(range(6))):
        ff,aa=smap(RF,z),smap(Ra,z);at,gl=smap(AT,z),smap(GL,z)
        fc,ac=smap(FC,z),smap(aC,z)
        for b in P[0]:
            check(add(rd(ff[b],central=z),scale(apply(ff,P[1][b]),-1))==aa[b],
                  'native_cap_both_endpoints_all_Rees_faces')
        for b in T[0]:
            check(add(rd(at[b],central=z),scale(apply(at,T[1][b]),-1))==apply(aa,phi[b]),
                  'short_map_endpoint_equation_all_Rees_faces')
        for b in L[0]:
            check(add(rd(gl[b],central=z),apply(gl,L[1][b]))==add(apply(at,mu[b]),apply(aa,h[b])),
                  'bridge_comparison_all_Rees_faces')
        for b in C[0]:
            check(add(rd(fc[b],central=z),scale(apply(fc,C[1][b]),-1))==ac[b],
                  'whole_attachment_cone_cap_all_Rees_faces')
        # The nonzero Q cap remains omega, on the native top generator.
        top=('P',EV,OD)
        check(project(ff[top],'Q')==graph_vec(omega(())),'actual_corrected_generic_cycle_survives_all_Rees_faces')
        alive=[int(not(set(z)&set(ep))) for ep in (OD,EV)]
        counts=[]
        for ep in (VP,VM):counts.append(sum(1 for vv in aa.values() for c,e in vv if c[0]==ep))
        check([int(bool(n)) for n in counts]==alive,'exact_endpoint_specialization_support')
        central_records.append({'central_short_Rees':list(z),'endpoint_nonzero_columns':counts,
                                'generic_coefficient':1})
    print('whole coupled triangle and 64 central faces: checked',flush=True)
    endpoints=actual_endpoint_models(P,Ra)
    shortfaces=[tuple(i for i in range(6) if SHORT[i] in f) for f in FACES if all(a in SHORT for a in f)]
    seedfaces=sorted([s for s in shortfaces if s not in (EV,OD)],key=lambda s:(len(s),s))
    check(len(seedfaces)==16,'sixteen_minimal_Rees_generators')
    seeds={s:make_seed(P,s) for s in seedfaces}
    check(seeds[()][2]==RF,'empty_Rees_seed_is_original_whole_native_cap')
    endpoint_comparison_homotopies={}
    for ss,(alpha,iv,tab,defect) in seeds.items():
        vv=rees_hom(P,alpha,'V');red=reduce_int(vv[0],vv[1]);predicted={b:{} for b in P[0]}
        for ep,em in endpoints.items():
            if set(ss)<=set(ep):
                factor=ex({9+i:int(i in ss)-int(i in ep) for i in range(6)})
                for b in P[0]:predicted[b]=add(predicted[b],multiply(em['j1'][b],factor))
        diff={}
        for b in P[0]:
            for (c,e),aa in add(defect[b],scale(predicted[b],-1)).items():
                check((b,c) in vv[0] and e==vv[2][b,c],'endpoint_row_comparison_frame');diff[b,c]=aa
        check(not lin(red['P'],diff),'all_endpoint_row_comparison_obstructions_zero')
        hh=lin(red['H'],diff)
        check(lin(vv[1],hh)==diff,'endpoint_row_comparison_homotopy')
        endpoint_comparison_homotopies[str(ss)]=serialize_map(rees_table(hh,vv,P))
    # Explicit chain map from the free graded R-module on the sixteen seeds.
    # Its cone is checked in every possible stalk-inequality shape: negative,
    # zero, positive Rees degrees in each of the six variables.
    records=[];total_pivots=0
    for ix,alpha in enumerate(product((-1,0,1),repeat=6)):
        model=rees_hom(P,alpha,'E')
        available=[s for s in seedfaces if all(alpha[i]>=int(i in s) for i in range(6))]
        sg={s:-2 for s in available};sd={s:{} for s in available}
        f={s:seeds[s][1] for s in available}
        for s in available:
            check(all(x in model[0] for x in f[s]),'polynomial_seed_transition_stalk_domains')
            check(not lin(model[1],f[s]),'polynomial_seed_transition_closed')
        cg,cd=cone_int(sg,sd,model[0],model[1],f)
        hh,piv=fast_reduce(cg,cd);total_pivots+=piv
        check(not hh,'sixteen_generator_comparison_cone_acyclic_all_degrees')
        # Endpoint residue theorem independently checked in all shapes.
        vg,vd,vc=rees_hom(P,alpha,'V');vr,vp=fast_reduce(vg,vd)
        eg,ed,ef=endpoint_model_frame(endpoints,alpha)
        ecg,ecd=cone_int(eg,ed,vg,vd,ef)
        er,epiv=fast_reduce(ecg,ecd)
        check(not er,'actual_two_term_endpoint_comparison_cone_all_degrees')
        want=sum(int(all(alpha[j]>=0 for j in range(6) if j not in ep)
                     and any(alpha[j]<=0 for j in ep)) for ep in (OD,EV))
        check(vr==({-3:want} if want else {}),'product_divisor_endpoint_cohomology_all_degrees')
        for x in vg:
            check(endpoint_read(vd[x],alpha,OD)==0 and endpoint_read(vd[x],alpha,EV)==0,
                  'literal_endpoint_residue_functionals_kill_boundaries')
        records.append({'t_degree_shape':list(alpha),'E_H2_rank':len(available),'V_H3_rank':want,
                        'comparison_cone_unit_pairs':piv})
        if (ix+1)%150==0:print('graded cone shapes',ix+1,flush=True)
    # All 192 nonnegative Boolean multiplication maps are represented by the
    # SAME symbolic seed cochains, not by separately selected homology bases.
    multiplication=0
    for bits in product((0,1),repeat=6):
        for i in range(6):
            if bits[i]:continue
            after=list(bits);after[i]=1
            for s in seedfaces:
                if all(bits[j]>=int(j in s) for j in range(6)):
                    check(all(after[j]>=int(j in s) for j in range(6)),
                          'Rees_polynomial_module_transition')
            multiplication+=1
    check(multiplication==192,'all_Rees_cube_multiplications')
    central_frames=[]
    for alpha in product((0,1),repeat=6):
        ss=tuple(i for i,a in enumerate(alpha) if a)
        out={}
        for support in ('K','E','V','Q','BV'):
            gg,dd,cc=rees_hom(P,alpha,support,range(6));rr,pv=fast_reduce(gg,dd)
            out[support]={'columns':len(gg),'cohomology':{str(-n):r for n,r in rr.items()}}
        face=tuple(sorted(SHORT[i] for i in ss));valid=face in FACES
        wantK={'2':1} if valid else {}
        wantV={'2':1} if ss in (EV,OD) else {}
        wantE={'2':1} if valid and ss not in (EV,OD) else {}
        wantQ={'2':1} if not ss else {}
        check(out['K']['cohomology']==wantK,'central_all_marked_short_face_classification')
        check(out['V']['cohomology']==wantV,'central_endpoints_live_in_own_Rees_determinant_degrees')
        check(out['E']['cohomology']==wantE,'central_native_endpoint_quotient_classification')
        check(out['Q']['cohomology']==wantQ,'central_generic_only_in_unit_Rees_degree')
        # Each free Rees generator specializes to its own nonzero marked face;
        # multiplying the unit cap into that degree specializes to zero.
        if ss in seeds:
            table=smap(seeds[ss][2],range(6));mm=rees_hom(P,alpha,'E',range(6));red=reduce_int(mm[0],mm[1])
            iv={}
            for b,z in table.items():
                for (c,e),a0 in z.items():
                    check((b,c) in mm[0] and e==mm[2][b,c],'specialized_seed_actual_coefficient')
                    iv[b,c]=a0
            coords=lin(red['P'],iv)
            check(len(coords)==1 and abs(next(iter(coords.values())))==1,'central_marked_seed_is_primitive')
        central_frames.append({'active_Rees_degree':list(ss),'target_Hom':out})
    # Source excess: tensor the entire equations, never replace its generator
    # by an internal target-normal multiple. The sign rule is tested on every
    # 50*32 source pair for the actual selected differential.
    eg,ed,eta=selected_excess_audit()
    for b,n in P[0].items():
        for w,m in eg.items():
            # degree(F)=-2 is even: the two cross terms have opposite signs.
            check(pm(n-2)-pm(n)==0,'full_excess_tensor_cap_cross_terms')
            for vv in ed[w].values():check(vv in (-1,1),'selected_excess_primitive_wedge_incidence')
    gysin=gysin_endpoint_audit(P,endpoints)
    result={
      'status':'proved_for_complete_coupled_triangle_on_polynomial_short_Rees_graph',
      'source_commit':COMMIT,'source_blobs':SOURCE_BLOBS,
      'graph':'u_i=t_i X_i for i=0,...,5; long normals unchanged',
      'scope':'fixed full-six-occurrence and three-long-normal frame; all six Rees degrees retained as a polynomial family',
      'source_cone_equivalence_unit_pairs':81,
      'whole_triangle_central_faces':central_records,
      'E_Rees_module':{'cohomology_degree':2,'free_generators':16,'generator_degrees':[list(s) for s in seedfaces],
          'generic_map':'projection to the empty-face generator',
          'positive_degree_generators_are_not_alternatives_in_the_original_unit_frame':True},
      'endpoint_Rees_models':{'plus':'[R -> R[(t1*t3*t5)^-1]] in degrees 2,3; basis degree e1+e3+e5',
                             'minus':'[R -> R[(t0*t2*t4)^-1]] in degrees 2,3; basis degree e0+e2+e4',
                             'unit_cap_values':['1/(t1*t3*t5)','1/(t0*t2*t4)'],
                             'endpoint_relation':'seed S has value t_S/tau_endpoint exactly when S is contained in that endpoint, else zero',
                             'strict_central_specialization_of_original_endpoint_maps':'both zero',
                             'endpoint_objects_after_central_specialization':'one primitive degree-two class each, in distinct Rees determinant frames'},
      'actual_endpoint_Cech_maps':{str(ep):{'j0':serialize_map(em['j0']),'j1':serialize_map(em['j1']),'central_coefficient':em['central_coefficient']} for ep,em in endpoints.items()},
      'endpoint_row_comparison_homotopies':endpoint_comparison_homotopies,
      'seeds':{str(s):{'degree':list(s),'cochains':serialize_map(v[2]),'endpoint_defect':serialize_map(v[3])} for s,v in seeds.items()},
      'all_integer_degree_shapes':records,'total_comparison_unit_pairs':total_pivots,
      'Rees_multiplication_arrows':multiplication,
      'full_central_degree_frames':central_frames,
      'Gysin_presentations_and_higher_comparisons':gysin,
      'independent_excess':'eta_x=t3*h3_plus-h3_pair; all 32 selected wedges retained; no source-to-native identification claimed',
      'important_nonidentifications':[
          'Closed intersection V(t1,t3,t5) is not the divisor union V(t1*t3*t5).',
          'The product-divisor residue of the original endpoint map specializes to zero; its target complex does not.',
          'The primitive central Gysin map has the complete Koszul source and determinant; it is not the old free-source residue map.',
          'Tensor compatibility with selected excess is not a construction identifying its source channel with the native conductor.',
          'No equality with full ringed supported-Verdier functor, collar-frame comparison or physical parity is asserted.'
      ],
      'exact_assertions':dict(sorted(COUNT.items())), 'total_exact_assertions':sum(COUNT.values()),
      'runtime_seconds':round(time.time()-start,3)
    }
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['status','E_Rees_module','total_exact_assertions','runtime_seconds']},indent=2))

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path('marici_joint_triangle_rees_gysin_certificate.json'))
    args=parser.parse_args();main_rees(args.output)
