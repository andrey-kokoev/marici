#!/usr/bin/env python3
"""Native mixed-edge attachment triangle into the actual K6 generic target.

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


def main(output):
    P,F,a=build_cap();T=taylor();L=bridges()
    for S,tag in [(P,'native_node'),(T,'short_Taylor'),(L,'three_bridge_Koszuls')]:audit_source(S,tag)
    for cell in CELLS:
        check(not td(BD[cell]),'actual_target_d_squared')
        for sup in ('V','B'):
            if predicate(cell,sup):check(all(predicate(c,sup) for c,e in BD[cell]),'actual_target_support_filtration')
    mu=construct_mu(L,T)
    phi=lift_chain(T,P,{('T',()):one(('P',(),()))},'P')
    h=nullhomotopy(L,P,{b:apply(phi,mu[b]) for b in L[0]},'P')
    C=cone(mu,L,T)
    psi={('t',b):phi[b] for b in T[0]};psi.update({('l',b):h[b] for b in L[0]})
    for b in C[0]:check(apply(P[1],psi[b])==apply(psi,C[1][b]),'whole_attachment_cone_to_native_chain_map')
    inverse=lift_chain(P,C,{('P',(),()):one(('t',('T',())))},'C')
    inverse_h=nullhomotopy(P,P,{b:add(apply(psi,inverse[b]),scale(one(b),-1)) for b in P[0]},'P')
    cone_psi=cone(psi,C,P)
    equivalence=poly_sdr(cone_psi)
    check(not equivalence[0][0] and equivalence[-1]==81,'source_cone_equivalence_81_unit_pairs')
    source_frames=[]
    for bits in product((0,1),repeat=6):
        alpha=tuple(bits)+(0,)*12;r=frame_reduction(cone_psi,alpha,'cone_psi')
        check(not r['homology'],'source_equivalence_every_squarefree_occurrence_frame')
        source_frames.append({'positive_short_support':[i for i,b in enumerate(bits) if b],'unit_pairs':r['pivots']})
    tm=poly_sdr(T)
    check(Counter(tm[0][0].values())==Counter({0:1,1:6,2:9,3:6,4:2}),'short_minimal_resolution_ranks')
    Araw={b:apply(F,phi[b]) for b in T[0]}
    # The generic nullhomotopy is computed, not assumed. In this deterministic
    # native quotient lift it is identically zero: the generic composite is
    # already zero termwise on the full Taylor resolution.
    N=projmap({b:apply(Araw,tm[3][b]) for b in T[0]},'Q')
    A={b:add(Araw[b],scale(add(td(N[b]),apply(N,T[1][b])),-1)) for b in T[0]}
    G={b:add(apply(F,h[b]),scale(apply(N,mu[b]),-1)) for b in L[0]}
    aT={b:apply(a,phi[b]) for b in T[0]}
    for b in T[0]:
        check(not project(A[b],'Q'),'native_short_extension_has_zero_generic_composite')
        check(add(td(A[b]),scale(apply(A,T[1][b]),-1))==aT[b],'both_endpoint_defects_after_short_extension')
    for b in L[0]:
        check(add(td(G[b]),apply(G,L[1][b]))==add(apply(A,mu[b]),apply(a,h[b])),'entire_bridge_target_equation_with_endpoints')
    FC={b:apply(F,psi[b]) for b in C[0]};aC={b:apply(a,psi[b]) for b in C[0]}
    for b in C[0]:check(add(td(FC[b]),scale(apply(FC,C[1][b]),-1))==aC[b],'full_112_column_cone_cap_endpoint_equation')
    for table,src,n,tag in [(F,P,-2,'native_cap'),(A,T,-2,'short_composite'),(G,L,-1,'bridge_comparison'),(FC,C,-2,'cone_cap')]:
        audit_homogeneous_table(table,src,n,tag)
        for b in src[0]:
            for j in range(18):
                e=ex({j:1})
                check(td(multiply(table[b],e))==multiply(td(table[b]),e),tag+'_base_multiplication_naturality')
                check(all(legal(c,m) for c,m in multiply(table[b],e)),tag+'_multiplication_legal_domains')

    models={name:{sup:model_reduction(S,sup) for sup in ('V','BV','E','Q')}
            for name,S in [('native',P),('short',T),('bridges',L)]}
    expected={
      'native':{'V':{-3:2},'BV':{},'E':{-2:1},'Q':{-2:1}},
      'short':{'V':{-3:2},'BV':{-2:3},'E':{-2:1},'Q':{-1:2}},
      'bridges':{'V':{},'BV':{-2:3},'E':{},'Q':{-1:3}}}
    for name in models:
        for sup,(m,r) in models[name].items():check(r['homology']==expected[name][sup],'all_replacement_Hom_'+name+'_'+sup)
    PM,PR=models['native']['Q'];LQ,LQR=models['bridges']['Q'];TQ,TQR=models['short']['Q']
    LBV,LBVR=models['bridges']['BV'];TBV,TBVR=models['short']['BV'];TE,TER=models['short']['E'];TV,TVR=models['short']['V']
    fp=lin(PR['P'],as_cochain(projmap(F,'Q'),PM))
    check(len(fp)==1 and abs(next(iter(fp.values())))==1,'native_generic_primitive_frame')
    theta=[];betas=[];native_comparison_homotopies=[]
    for pair in BRIDGES:
        top=('L',pair,tuple(j for j in range(6) if j not in pair))
        # Ordered even-to-odd bridge incidence and the numeric complement
        # wedge determine this sign before the connecting map is evaluated.
        sg=-1 if pair[0]<pair[1] else 1
        tt={b:(scale(omega(()),sg) if b==top else {}) for b in L[0]}
        theta.append(tt)
        check(all(not v for v in hom_differential(projmap(tt,'Q'),L,-1,'Q').values()),'each_complete_bridge_Gysin_generic_cocycle')
        bv=hom_differential(tt,L,-1,'BV');betas.append(bv)
        check(len(bv[top])==18,'bridge_transgression_has_all_eighteen_short_terms')
        check(all(not v for v in hom_differential(bv,L,-2,'BV').values()),'bridge_transgression_closed')
        induced={b:{} for b in P[0]}
        for b,v in inverse.items():
            for ((kind,src),e),coef in v.items():
                if kind=='l':induced[b]=add(induced[b],multiply(tt[src],e,coef))
        v=as_cochain(projmap(induced,'Q'),PM)
        check(lin(PR['P'],v)==fp,'source_connecting_row_has_positive_unit_each_bridge')
        diff=add(v,scale(as_cochain(projmap(F,'Q'),PM),-1));hh=lin(PR['H'],diff)
        check(lin(PM[1],hh)==diff,'connecting_class_matches_native_generic_by_actual_homotopy')
        native_comparison_homotopies.append(cochain_table(hh,PM,P))
    Lkeys=list(LQR['g']);LBkeys=list(LBVR['g'])
    coords=lambda v,keys:[v.get(k,0) for k in keys]
    theta_cols=[coords(lin(LQR['P'],as_cochain(projmap(tt,'Q'),LQ)),Lkeys) for tt in theta]
    beta_cols=[coords(lin(LBVR['P'],as_cochain(bb,LBV)),LBkeys) for bb in betas]
    check(all(abs(x)==1 for col in theta_cols for x in col if x),'bridge_basis_integral_primitive')
    beta_restriction_columns=[];q_restriction_columns=[]
    for z in TQR['g']:
        tt=homogeneous_pullback(mu,TQR['I'][z],L,TQ)
        v=as_cochain(tt,LQ)
        q_restriction_columns.append(inverse_coordinates(theta_cols,coords(lin(LQR['P'],v),Lkeys)))
    for z in TBVR['g']:
        tt=homogeneous_pullback(mu,TBVR['I'][z],L,TBV)
        v=as_cochain(tt,LBV)
        beta_restriction_columns.append(inverse_coordinates(beta_cols,coords(lin(LBVR['P'],v),LBkeys)))
    check(len(q_restriction_columns)==2 and all(sum(v)==0 for v in q_restriction_columns),'generic_short_variations_are_augmentation_kernel')
    # Solve for both primitive differences, proving saturation rather than
    # only equality of rational ranks.
    for v in ([1,-1,0],[0,1,-1]):inverse_coordinates(q_restriction_columns,v)
    check(len(beta_restriction_columns)==3,'three_short_supported_classes')
    for j in range(3):inverse_coordinates(beta_restriction_columns,[int(j==i) for i in range(3)])

    # Pull the three literal bridge transgressions back to the short-face
    # source and compare them to the endpoint-coupled native cap.
    short_classes=[];short_comparisons=[];endpoint_two_cells=[];mu_comparison_homotopies=[]
    A_E=projmap(A,'E');A_E_v=as_cochain(A_E,TE);aEcoord=lin(TER['P'],A_E_v)
    check(len(aEcoord)==1 and abs(next(iter(aEcoord.values())))==1,'native_unit_survives_in_short_source_endpoint_target')
    aTvec=as_cochain(aT,TV)
    endpoint_coordinates={}
    for label,face in [('plus',VP),('minus',VM)]:
        vv={x:k for x,k in aTvec.items() if x[1][0]==face};cv=lin(TVR['P'],vv)
        check(len(cv)==1 and abs(next(iter(cv.values())))==1,'native_'+label+'_endpoint_class_primitive')
        endpoint_coordinates[label]={repr(k):v for k,v in cv.items()}
    for j in range(3):
        coeff=inverse_coordinates(beta_restriction_columns,[int(j==i) for i in range(3)])
        vv={}
        for z,v in zip(TBVR['g'],coeff):vv=add(vv,scale(TBVR['I'][z],v))
        uu=cochain_table(vv,TBV,T);short_classes.append(uu)
        im=as_cochain(uu,TE)
        check(lin(TER['P'],im)==aEcoord,'three_bridge_presentations_give_same_joint_endpoint_unit')
        diff=add(im,scale(A_E_v,-1));hv=lin(TER['H'],diff)
        check(lin(TE[1],hv)==diff,'bridge_presentation_to_native_E_homotopy')
        H=cochain_table(hv,TE,T);short_comparisons.append(H)
        ec=projmap(hom_differential(H,T,-1),'V');endpoint_two_cells.append(ec)
        check(not any(ec.values()),'constructed_E_comparison_has_zero_endpoint_component')
        alpha=hom_differential(uu,T,-2)
        for b in T[0]:
            check(all(predicate(cell,'V') for cell,e in alpha[b]),'new_presentation_has_only_endpoint_defect')
            check(alpha[b]==aT[b],'both_endpoint_maps_agree_exactly_in_three_presentations')
            check(add(alpha[b],scale(aT[b],-1))==scale(hom_differential(ec,T,-2,'V')[b],-1),'both_actual_endpoint_comparison_two_cell_equations')
        # Keep the inverse to mu^* as a cochain comparison, not a mere
        # correspondence between three cohomology dimensions.
        pull=homogeneous_pullback(mu,vv,L,TBV);pv=as_cochain(pull,LBV);bv=as_cochain(betas[j],LBV)
        dd=add(pv,scale(bv,-1));uv=lin(LBVR['H'],dd)
        check(lin(LBV[1],uv)==dd,'short_to_bridge_transgression_comparison_homotopy')
        mu_comparison_homotopies.append(cochain_table(uv,LBV,L))

    # The two generic variation classes are labelled by actual long-facet
    # disks. Their source precomposition is checked on every cochain, with
    # a displayed comparison for any exact residual.
    geometry=geometry_attachment();long_variations=[];long_variation_homotopies=[];long_support_homotopies=[]
    for col in geometry['matrix_columns']:
        coeff=inverse_coordinates(q_restriction_columns,col);v={}
        for z,a0 in zip(TQR['g'],coeff):v=add(v,scale(TQR['I'][z],a0))
        tt=cochain_table(v,TQ,T);long_variations.append(tt)
        expectedtheta={b:{} for b in L[0]}
        for coef,t in zip(col,theta):
            for b in L[0]:expectedtheta[b]=add(expectedtheta[b],scale(t[b],coef))
        got=homogeneous_pullback(mu,v,L,TQ);diff=add(as_cochain(got,LQ),scale(as_cochain(expectedtheta,LQ),-1));uv=lin(LQR['H'],diff)
        check(lin(LQ[1],uv)==diff,'literal_long_disk_difference_in_actual_generic_Hom')
        long_variation_homotopies.append(cochain_table(uv,LQ,L))
        bt=hom_differential(tt,T,-1,'BV')
        want={b:{} for b in T[0]}
        for coefficient,us in zip(col,short_classes):
            for b in T[0]:want[b]=add(want[b],scale(us[b],coefficient))
        sdifference=add(as_cochain(bt,TBV),scale(as_cochain(want,TBV),-1))
        sh=lin(TBVR['H'],sdifference)
        check(lin(TBV[1],sh)==sdifference,'source_target_connecting_square_full_cochain_homotopy')
        long_support_homotopies.append(cochain_table(sh,TBV,T))
    for b in T[0]:check(not add(*(v[b] for v in long_variations)),'three_long_generic_comparisons_have_exact_norm_relation')

    # Six labelled symmetries on complete source complexes and their maps.
    equivariance_homotopies={}
    for g in GROUP:
        for source in (P,T,L,C):
            for b in source[0]:check(apply(source[1],act_vector(one(b),g))==act_vector(source[1][b],g),'actual_source_D3_differential')
        for b in L[0]:check(act_vector(mu[b],g)==apply(mu,act_vector(one(b),g)),'canonical_bridge_inclusion_strict_D3')
        for pair,tt in zip(BRIDGES,theta):
            p=tuple(perm_short(g)[i] for i in pair);gp=p if p[0]%2==0 else p[::-1];other=theta[BRIDGES.index(gp)]
            for b in L[0]:check(act_target(tt[b],g)==scale(apply(other,act_vector(one(b),g)),pm(g[1])),'bridge_generic_classes_actual_polarity_covariance')
        diff={b:add(act_vector(phi[b],g),scale(apply(phi,act_vector(one(b),g)),-1)) for b in T[0]}
        hg=nullhomotopy(twisted_source(T,g),P,diff,'P')
        equivariance_homotopies[repr(g)]=serialize_map(hg)

    # Recheck the source cone->native comparison on all full target supports.
    # A polynomial contraction of Cone(psi) already proves this for arbitrary
    # coefficients; the homogeneous Hom computations above are independent.
    summaries={name:{sup:{'generators':len(m[0]),'Ext':{str(-n):k for n,k in r['homology'].items()},'unit_pairs':r['pivots']}
                     for sup,(m,r) in mm.items()} for name,mm in models.items()}
    total=sum(COUNT.values())
    cert={
      'status':'proved_native_mixed_short_edge_generic_attachment_triangle_in_fixed_normal_frame',
      'date':'2026-09-07','pinned_commit':COMMIT,'source_blobs':SOURCE_BLOBS,
      'frame':{'coefficient_order':['X0','X1','X2','X3','X4','X5','XD03','XD14','XD25','u0','u1','u2','u3','u4','u5','uD03','uD14','uD25'],
               'map_fine_degree':list(LAMBDA),'normal_frame':list(GAMMA)},
      'source_resolutions':{'native_node':[1,9,18,15,6,1],'short_Taylor':[1,6,15,20,15,6,1],
        'short_minimal':[1,6,9,6,2],'three_bridge_Koszuls':[3,12,18,12,3],
        'attachment_cone_ranks':[sum(n==i for n in C[0].values()) for i in range(7)],
        'cone_to_native_equivalence':{'total_generators':len(cone_psi[0]),'signed_unit_pairs':81,'remainder':0}},
      'source_equivalence_64_frames':source_frames,'complete_Hom_computations':summaries,
      'source_connecting_row_in_oriented_bridge_basis':[1,1,1],
      'generic_variations_columns':q_restriction_columns,
      'short_transgression_precomposition_columns':beta_restriction_columns,
      'endpoint_class_coordinates':endpoint_coordinates,'actual_long_disk_geometry':geometry,
      'maps':{
        'canonical_bridge_inclusion_into_Taylor':serialize_map(mu),
        'short_quotient_to_native_resolution':serialize_map(phi),
        'joint_inclusion_nullhomotopy':serialize_map(h),
        'attachment_cone_to_native':serialize_map(psi),'native_to_attachment_cone':serialize_map(inverse),
        'native_inverse_comparison_homotopy':serialize_map(inverse_h),
        'native_cap':serialize_map(F),'native_endpoint_defect':serialize_map(a),
        'short_supported_native_composite':serialize_map(A),'short_composite_endpoint_defect':serialize_map(aT),
        'bridge_K_comparison_with_coupled_defect':serialize_map(G),
        'generic_nullhomotopy_of_short_composite':serialize_map(N),
        'three_oriented_generic_bridge_cocycles':[serialize_map(v) for v in theta],
        'three_eighteen_term_bridge_transgressions':[serialize_map(v) for v in betas],
        'native_generic_comparison_homotopies':[serialize_map(v) for v in native_comparison_homotopies],
        'three_short_supported_presentations':[serialize_map(v) for v in short_classes],
        'presentation_to_native_E_homotopies':[serialize_map(v) for v in short_comparisons],
        'both_endpoint_two_cells_for_each_presentation':[serialize_map(v) for v in endpoint_two_cells],
        'short_bridge_transgression_homotopies':[serialize_map(v) for v in mu_comparison_homotopies],
        'three_labelled_long_generic_variations':[serialize_map(v) for v in long_variations],
        'long_to_bridge_generic_comparison_homotopies':[serialize_map(v) for v in long_variation_homotopies],
        'long_generic_to_short_attachment_homotopies':[serialize_map(v) for v in long_support_homotopies],
        'quotient_map_six_equivariance_homotopies':equivariance_homotopies},
      'scope':[
        'Full native node, actual mixed-edge occurrence ideals, full Taylor triangle, and original 215-state target differential.',
        'All polynomial maps and source-cone homotopies are verified symbolically over eighteen independent coefficients, with no occurrence inversion.',
        'All Hom cohomology and uniqueness/obstruction assertions are in the declared six-occurrence determinant and three-long-normal frame.',
        'Individual bridge-to-Q Gysin classes have a primitive obstruction to an independent E lift; this is not an obstruction to the coupled native cap.',
        'The three coordinate-edge modules are not renamed as the three long-facet states; they map through the actual connecting triangle.',
        'The long disks give the literal labelled difference relations; the supported polynomial modules are retained in the derived computation.',
        'Two endpoint comparison homotopies are retained for every presentation. Their equality with the independently specified physical collar operators is not asserted.',
        'No independent branch-pair excess/Rees-channel identification, full ringed six-functor equivalence, or physical reflection parity is claimed.',
        'Signed-unit SDRs and all-degree proofs are executable algebraic certificates, not proof-assistant verification.'
      ],
      'total_exact_assertions':total,'assertion_categories':dict(sorted(COUNT.items()))}
    cert['checker_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(json.dumps(cert,indent=2)+'\n')
    print(json.dumps({'status':cert['status'],'total_exact_assertions':total,'Hom':summaries,
          'source_connecting_row':[1,1,1],'source_cone_equivalence':cert['source_resolutions']['cone_to_native_equivalence'],
          'three_short_presentation_terms':[sum(map(len,v.values())) for v in short_classes],
          'three_endpoint_two_cell_terms':[sum(map(len,v.values())) for v in endpoint_two_cells],
          'physical_parity_assigned':False},indent=2))

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path('marici_mixed_short_edge_generic_attachment_triangle_certificate.json'))
    args=parser.parse_args();main(args.output)
