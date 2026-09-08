#!/usr/bin/env python3
"""Joint-normalization complementary-face comparison into the actual K6 target.

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


def main(output):
    P=node();KE=koszul(EV,'E');KO=koszul(OD,'O');KC=koszul(ORDER,'C')
    for m,name in ((P,'node'),(KE,'plus_sheet'),(KO,'minus_sheet'),(KC,'conductor')):audit_source(m,name)
    check([sum(n==i for n in P[0].values()) for i in range(6)]==[1,9,18,15,6,1],'node_ranks')
    check(len(CELLS)==215,'all_actual_target_states')
    for c in CELLS:
        check(not td(BD[c]),'target_d_squared')
        for (t,e),a in BD[c].items():
            check(legal(t,e),'target_arrow_stalk_domain')
            check(degree(t)+1==degree(c),'target_arrow_degree')
        for k in ('B','V'):
            if predicate(c,k):check(all(predicate(t,k) for t,e in BD[c]),'support_is_subcomplex')
    # Explicit short-incidence decorations in the original 215-state complex.
    shortfaces=tuple(t for t in subsets(tuple(range(6))) if tuple(sorted(SHORT[i] for i in t)) in FACES)
    for t in shortfaces:
        w=omega(t)
        for c,e in w:check(legal(c,e),'Omega_legal_coefficients')
        expected={};f=tuple(sorted(SHORT[i] for i in t))
        for a in range(6):
            if a not in t and all(not cross(SHORT[a],b) for b in f):
                expected=add(expected,multiply(omega(tuple(sorted(t+(a,)))),ex({a:1}),pm(sum(b<SHORT[a] for b in f))))
        check(td(w)==expected,'Omega_complete_radial_normal_identity')
    cap={b:scale(omega(tuple(i for i in ORDER if i not in b[1])),complement_sign(b[1])) for b in KC[0]}
    for b in KC[0]:check(td(cap[b])==scale(apply(cap,KC[1][b]),-1),'complementary_cap_antichain')
    fp={};fm={};H={};F={}
    for b in P[0]:
        _,u,v=b
        if not u:fp[b]=one(('E',()));fm[b]=one(('O',()));H[b]={};F[b]={}
        else:
            fp[b]={(('E',u),ex({v[0]:1})):1} if len(v)==1 else {}
            fm[b]={(('O',v),ex({u[0]:1})):1} if len(u)==1 else {}
            H[b]={ (('C',u+v),Z):pm(len(u)) }
            F[b]=scale(apply(cap,H[b]),-1)
    ie={b:one(('C',b[1])) for b in KE[0]};io={b:one(('C',b[1])) for b in KO[0]}
    tp={b:apply(cap,ie[b]) for b in KE[0]};tm={b:apply(cap,io[b]) for b in KO[0]}
    for b in P[0]:
        check(apply(KE[1],fp[b])==apply(fp,P[1][b]),'source_plus_chain_map')
        check(apply(KO[1],fm[b])==apply(fm,P[1][b]),'source_minus_chain_map')
        check(add(apply(KC[1],H[b]),apply(H,P[1][b]))==add(apply(ie,fp[b]),scale(apply(io,fm[b]),-1)),'source_joint_H')
    endpoint={b:add(apply(tp,fp[b]),scale(apply(tm,fm[b]),-1)) for b in P[0]}
    FE={b:project(v,'E') for b,v in F.items()};FQ={b:project(v,'Q') for b,v in F.items()}
    for b in P[0]:
        check(add(td(F[b]),scale(apply(F,P[1][b]),-1))==endpoint[b],'two_endpoint_comparison')
        check(all(predicate(c,'V') for c,e in endpoint[b]),'both_endpoint_supports_retained')
        check(td(FE[b],'E')==apply(FE,P[1][b]),'joint_source_to_E_chain_map')
        check(td(FQ[b],'Q')==apply(FQ,P[1][b]),'joint_source_to_Q_chain_map')
        for c,e in F[b]:
            check(legal(c,e),'source_to_target_legal_stalk')
            check(degree(c)==P[0][b]-2,'source_to_target_degree_minus_two')
            check(e==eadd(eadd(LAMBDA,P[2][b]),weight(c)),'six_occurrence_determinant_frame')
    top=('P',EV,OD)
    check(F[top]==omega(()),'generic_top_primitive_cycle')
    check(not td(FQ[top],'Q'),'generic_top_closed')
    check(cap[('C',EV)]==omega(OD),'plus_cap_orientation')
    check(cap[('C',OD)]==scale(omega(EV),-1),'minus_cap_orientation')
    check(sum(len(v) for v in F.values())==43,'complete_F_term_count')
    check(sum(len(v) for v in endpoint.values())==6,'endpoint_column_count')
    # Symbolic base-linearity and multiplication with every original variable.
    for b in P[0]:
        for j in range(18):
            e=ex({j:1})
            check(td(multiply(F[b],e))==multiply(td(F[b]),e),'polynomial_and_normal_linearity')
            for c,m in multiply(F[b],e):check(legal(c,m),'multiplication_stalk_domain')
    for g in GROUP:
        for c in CELLS:
            check(act_target(td(one(c)),g)==td(act_target(one(c),g)),'target_dihedral_chain_action')
        for b in P[0]:
            check(apply(P[1],act_source(one(b),g))==act_source(P[1][b],g),'source_dihedral_chain_action')
            check(act_target(F[b],g)==scale(apply(F,act_source(one(b),g)),pm(g[1])),'full_comparison_polarity_covariance')
            check(act_target(endpoint[b],g)==scale(apply(endpoint,act_source(one(b),g)),pm(g[1])),'endpoint_polarity_covariance')
    # Full homogeneous mapping complexes, not maps between homology readouts.
    models={k:homogeneous_hom(P,k) for k in ('K','V','B','BV','E','Q')}
    images,orientations=spatial_identification(models['K'])
    reductions={k:reduce_int(v[0],v[1]) for k,v in models.items()}
    expected={'K':{-3:1},'V':{-3:2},'B':{-3:2},'BV':{},'E':{-2:1},'Q':{-2:1}}
    for k in models:check(reductions[k]['homology']==expected[k],'critical_'+k+'_integral_cohomology')
    f=as_cochain(FE,models['E']);gq=as_cochain(FQ,models['Q']);a=as_cochain(endpoint,models['V'])
    spatial_f={images[x]:a*orientations[x] for x,a in f.items()}
    expected_spatial_f={images[x]:1 for x,n in models['E'][0].items() if n==-2}
    check(spatial_f==expected_spatial_f,'F_is_actual_constant_vertex_cochain_on_W_E')
    check(not lin(models['E'][1],f),'F_homogeneous_cocycle')
    check(not lin(models['Q'][1],gq),'generic_homogeneous_cocycle')
    check(not lin(models['V'][1],a),'endpoint_homogeneous_cocycle')
    check(sorted(abs(z) for z in lin(reductions['E']['P'],f).values())==[1],'primitive_E_class')
    check(sorted(abs(z) for z in lin(reductions['Q']['P'],gq).values())==[1],'primitive_Q_class')
    ap={b:project(v,'V') for b,v in endpoint.items()}
    ep={x:c for x,c in a.items() if x[1][0]==VP};em={x:c for x,c in a.items() if x[1][0]==VM}
    for v in (ep,em):
        check(not lin(models['V'][1],v),'separate_endpoint_cocycle')
        check(sorted(abs(c) for c in lin(reductions['V']['P'],v).values())==[1],'primitive_separate_endpoint')
    # Canonical full restriction C_E -> C_V[1] + C_Q. Off-diagonal maps are
    # the actual target support boundary, with no endpoint contraction first.
    vg,vd,_=models['V'];qg,qd,_=models['Q'];eg,ed,_=models['E']
    bg={('v',x):n+1 for x,n in vg.items()};bg.update({('q',x):n for x,n in qg.items()})
    bd={('v',x):{('v',y):-c for y,c in vd[x].items()} for x in vg}
    bd.update({('q',x):{('q',y):c for y,c in qd[x].items()} for x in qg})
    r={x:{} for x in eg}
    for x in eg:
        b,c=x
        for (t,e),s in BD[c].items():
            y=(b,t)
            if predicate(t,'V'):
                check(y in vg,'endpoint_restriction_Hom_domain');r[x]['v',y]=s
        if x in qg:r[x]['q',x]=1
    for x in eg:check(lin(bd,r[x])==lin(r,ed[x]),'full_endpoint_Q_restriction_chain')
    rg={('e',x):n for x,n in eg.items()};rg.update({('b',x):n-1 for x,n in bg.items()})
    rd={('e',x):add({('e',y):c for y,c in ed[x].items()},{('b',y):c for y,c in r[x].items()}) for x in eg}
    rd.update({('b',x):{('b',y):-c for y,c in bd[x].items()} for x in bg})
    audit_int(rg,rd,'complete_relative_fibre');rr=reduce_int(rg,rd)
    check(rr['homology']=={-3:2},'relative_fibre_has_only_degree_three')
    check(lin(r,f)==add({('v',x):c for x,c in a.items()},{('q',x):c for x,c in gq.items()}),'matching_data_1_1_1')
    # A/BV exactness is the all-replacement uniqueness proof for fixed generic
    # data. The SDR checks every cochain of the entire prescribed fine frame.
    # The adjoint covector on the framed generic T term is transported to
    # p_top^vee, which equals -kappa in the previous source convention.
    topcell=((),())
    transposed={b:a for b,v in FQ.items() for (c,e),a in v.items() if c==topcell}
    check(transposed=={top:1},'reverse_generic_covector_is_minus_source_kappa')
    # Independent excess factor: tensor a zero-differential exterior line;
    # both channels must satisfy the same complete endpoint equation.
    for eps in (0,1):
        for b in P[0]:
            lhs=add(td(F[b]),scale(apply(F,P[1][b]),-1))
            check({(eps,c,e):a for (c,e),a in lhs.items()}=={(eps,c,e):a for (c,e),a in endpoint[b].items()},'independent_excess_tensor_channel')
    certificate={
      'status':'constructed_joint_occurrence_cap_comparison_in_prescribed_normal_and_occurrence_frame',
      'date':'2026-09-07','commit':COMMIT,'source_blobs':SOURCE_BLOBS,
      'source_resolution_ranks':[1,9,18,15,6,1], 'actual_target_states':215,
      'spatial_identification':'Hom(P,K)_lambda = C^*(W,{v_plus,v_minus}) shifted by two; Hom(P,E)=C^*(W_E) shifted by two',
      'F_spatial_cochain':'constant +1 on all 43 vertices of W_E',
      'critical_map_terms':43,'critical_nonzero_source_columns':sum(bool(v) for v in F.values()),
      'endpoint_terms':6,'chain_degree_of_F':-2,'cohomological_Ext_degree':2,
      'map_fine_degree':list(LAMBDA),
      'Hom_complexes':{k:{'generators':len(m[0]),'chain_group_ranks':dict(sorted(Counter(m[0].values()).items())),
                          'cohomology':{-n:v for n,v in reductions[k]['homology'].items()},
                          'unit_cancellations':reductions[k]['pivots']} for k,m in models.items()},
      'restriction_on_critical_classes':{'E_to_Q':1,'E_to_endpoints':[1,1]},
      'relative_fibre':{'generators':len(rg),'cohomology':{3:2},'unit_cancellations':rr['pivots']},
      'fixed_generic_extension_space':'contractible in the full specified homogeneous mapping complex',
      'fixed_endpoint_and_Q_extension_space':'contractible when normalized data match (1,1,1); empty for other normalized endpoint values',
      'equivariance':'F(gp)=chi(g)*gF(p); twisting source by chi makes F strictly equivariant',
      'reverse_generic_value':'p_top^vee = -kappa in the previous conductor orientation convention',
      'F':serialize_map(F),'endpoint_defect':serialize_map(endpoint),'cap':serialize_map(cap),
      'primitive_E_reduced_coordinates':{repr(x):v for x,v in lin(reductions['E']['P'],f).items()},
      'primitive_Q_reduced_coordinates':{repr(x):v for x,v in lin(reductions['Q']['P'],gq).items()},
      'positive_endpoint_reduced_coordinates':{repr(x):v for x,v in lin(reductions['V']['P'],ep).items()},
      'negative_endpoint_reduced_coordinates':{repr(x):v for x,v in lin(reductions['V']['P'],em).items()},
      'scope':[
        'Full polynomial-linear map into original permitted target stalks; no occurrence inverses.',
        'Uniqueness is proved in the specified fine degree, not all possible degrees.',
        'Source is the joint node resolution, not the previously obstructed single-branch excess source.',
        'The two endpoint comparison maps are occurrence-resolution maps; equality to the original spatial collar operators with all normal/Rees frames is not asserted.',
        'An exterior excess factor is retained functorially; this does not identify it with the full physical excess correspondence.',
        'No equality with a ringed supported-Verdier or logarithmic six-functor is claimed.',
        'No physical reflection parity is assigned.'],
      'exact_assertions':sum(COUNT.values()),'assertion_categories':dict(sorted(COUNT.items()))}
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(json.dumps(certificate,indent=2)+'\n')
    print(json.dumps({k:certificate[k] for k in ('status','critical_map_terms','Hom_complexes','relative_fibre','exact_assertions')},indent=2))

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output',type=Path,default=Path('marici_joint_conductor_spatial_cap_comparison_certificate.json'))
    args=p.parse_args();main(args.output)
