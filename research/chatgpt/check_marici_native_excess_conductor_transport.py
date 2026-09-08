#!/usr/bin/env python3
"""Exact native-normalization pullback of the selected branch/pair excess.

Python 3.10+, standard library only. Coefficients are integer polynomials.
The all-degree result is proved in the accompanying note; the finite census
exhausts the monomial-domain breakpoints, not a numerical approximation.
This constructs a derived source diagram and its cap base change. It does
not identify the resulting source packets with physical collar 2-cells.
"""
from __future__ import annotations
import argparse, hashlib, json, time
from collections import Counter
from itertools import combinations, product
from pathlib import Path

COMMIT='d1947b67a60d3e88ba77f4ca60ea02c2a306ee61'
SOURCE_BLOBS={
 'src/ledger/20260814-93 Alternating Fusion Normalization-Conductor Square.md':'840258522d45e450e4f1e8bb927d9aae58c75566',
 'src/ledger/20260814-100 Support-Directed Can-Var Packet and Three Local Cousin Traces.md':'d5ed0c89e804284a4bf45bfa1e0c0bc2eab6eb12',
 'research/voevodsky/check_global_k6_koszul_cech_promotion.rs':'e972b69d0e2b1b0a0aee5e0a027c8216bcace3e8'}
# X0,...,X5, XD03,XD14,XD25, t0,...,t5,uD03,uD14,uD25.
NV=18; ZERO=(0,)*NV; COUNT=Counter()
EV=(0,2,4);OD=(1,3,5);ORDER=EV+OD

def check(ok,tag):
    if not ok:raise AssertionError(tag)
    COUNT[tag]+=1

def pm(n):return -1 if n%2 else 1

def subsets(s):return [v for k in range(len(s)+1) for v in combinations(s,k)]

def ex(es):return tuple(es.get(i,0) for i in range(NV))

def ea(a,b):return tuple(x+y for x,y in zip(a,b))

def es(a,b):return tuple(x-y for x,y in zip(a,b))

def add(*vs):
    out={}
    for v in vs:
        for k,c in v.items():
            out[k]=out.get(k,0)+c
            if not out[k]:del out[k]
    return out

def scale(v,c):return {k:c*a for k,a in v.items() if c*a}

def mul(v,e,c=1):return {(b,ea(m,e)):c*a for (b,m),a in v.items() if c*a}

def apply(d,v):
    out={}
    for (b,e),c in v.items():out=add(out,mul(d.get(b,{}),e,c))
    return out

def lin(d,v):
    out={}
    for b,c in v.items():out=add(out,scale(d.get(b,{}),c))
    return out

def one(b):return {(b,ZERO):1}

def wedge(a,b):
    if set(a)&set(b):return None,0
    return tuple(sorted(a+b)),pm(sum(i>j for i in a for j in b))

def exterior_map(columns):
    out={}
    for s in subsets(tuple(range(5))):
        v=one(())
        for i in s:
            nxt={}
            for (a,e),c in v.items():
                for (bb,ee),cc in columns[i].items():
                    z,sg=wedge(a,bb)
                    if sg:nxt=add(nxt,{(z,ea(e,ee)):c*cc*sg})
            v=nxt
        out[s]=v
    return out

def koszul(equations,weights=None):
    if weights is None:weights=equations
    g={};d={};wt={}
    for s in subsets(tuple(range(len(equations)))):
        g[s]=len(s);w=ZERO
        for i in s:w=ea(w,weights[i])
        wt[s]=w
        d[s]={(s[:j]+s[j+1:],equations[i]):pm(j)
              for j,i in enumerate(s) if equations[i] is not None}
    return g,d,wt

def source_models(branch=OD,partner=0,shared=3):
    # Both originals use the ordered three branch factors, then the pair.
    br=tuple(sorted(branch));r=br.index(shared)
    selected=[ex({i:1}) for i in br]+[ex({partner:1,9+partner:1}),ex({shared:1,9+shared:1})]
    raw=[ex({i:1,9+i:1}) for i in br]+selected[3:]
    dx=koszul(selected);du=koszul(raw)
    ww=selected[:4]+[selected[4]]
    splitx=koszul(selected[:4]+[None],ww)
    splitu=koszul(raw[:4]+[None],raw[:4]+[raw[4]])
    # eta_x=t_shared h_shared^branch-h_shared^pair; eta_u=h_branch-h_pair.
    cx=[one((i,)) for i in range(4)]+[add(mul(one((r,)),ex({9+shared:1})),scale(one((4,)),-1))]
    cu=[one((i,)) for i in range(4)]+[add(one((r,)),scale(one((4,)),-1))]
    bx=exterior_map(cx);bu=exterior_map(cu)
    # In each case the change is an involution with determinant -1.
    selection=exterior_map([mul(one((i,)),ex({9+j:1})) for i,j in enumerate(br)]+[one((3,)),one((4,))])
    selections=exterior_map([mul(one((i,)),ex({9+j:1})) for i,j in enumerate(br)]+[one((3,)),one((4,))])
    for s in dx[0]:
        check(not apply(dx[1],dx[1][s]),'selected_d_squared')
        check(not apply(du[1],du[1][s]),'raw_d_squared')
        check(apply(dx[1],bx[s])==apply(bx,splitx[1][s]),'selected_basis_chain')
        check(apply(bx,bx[s])==one(s),'selected_basis_integral_inverse')
        check(apply(du[1],bu[s])==apply(bu,splitu[1][s]),'raw_basis_chain')
        check(apply(bu,bu[s])==one(s),'raw_basis_integral_inverse')
        check(apply(dx[1],selection[s])==apply(selection,du[1][s]),'raw_selected_chain')
        check(apply(selection,bu[s])==apply(bx,selections[s]),'selection_in_excess_basis')
    return {'raw':du,'selected':dx,'split_raw':splitu,'split_selected':splitx,
            'basis_raw':bu,'basis_selected':bx,'selection':selection,'split_selection':selections,
            'branch':br,'partner':partner,'shared':shared}

def legal_ring(e,ring,branch=OD):
    if min(e)<0:return False
    odd=set(branch);even=set(range(6))-odd
    a=any(e[i]>0 for i in odd);b=any(e[i]>0 for i in even)
    if ring=='B':return not(a and b)
    if ring=='+':return not b
    if ring=='-':return not a
    if ring=='C':return not a and not b
    if ring=='A':return True
    raise ValueError(ring)

def restrict(v,ring,branch=OD):return {(b,e):c for (b,e),c in v.items() if legal_ring(e,ring,branch)}

def rd(model,v,ring,branch=OD):return restrict(apply(model[1],v),ring,branch)

def base_change(model,ring,branch=OD):return {b:restrict(v,ring,branch) for b,v in model[1].items()}

def central(v,labels):return {(b,e):c for (b,e),c in v.items() if all(e[9+i]==0 for i in labels)}

def hom_block(model,alpha,ring,branch=OD):
    weights=model[2]
    g={s:n for s,n in model[0].items() if legal_ring(es(alpha,weights[s]),ring,branch)}
    d={s:{} for s in g}
    for s in g:
        coeff=es(alpha,weights[s])
        for (ss,e),c in model[1][s].items():
            ee=ea(coeff,e)
            if legal_ring(ee,ring,branch):
                check(ss in g and ee==es(alpha,weights[ss]),'homogeneous_domain')
                d[s][ss]=c
    return g,d

def reduce_units(g,original,projection=False):
    d={s:dict(v) for s,v in original.items()};P={s:{s:1} for s in d} if projection else None
    count=0
    while True:
        hit=next(((b,a,c) for b,v in d.items() for a,c in v.items() if abs(c)==1),None)
        if hit is None:break
        b,a,c=hit;others=[s for s in d if s not in (a,b)];count+=1
        tail={y:-c*z for y,z in d[b].items() if y!=a}
        if projection:
            for s,v in P.items():
                va=v.get(a,0)
                v={y:z for y,z in v.items() if y not in (a,b)}
                if va:v=add(v,scale(tail,va))
                P[s]=v
        nxt={}
        for s in others:
            v=d[s];ca=v.get(a,0)
            v={y:z for y,z in v.items() if y not in (a,b)}
            if ca:v=add(v,scale(tail,ca))
            nxt[s]=v
        d=nxt
    check(not any(d.values()),'all_integral_Smith_factors_unit')
    return dict(sorted(Counter(g[s] for s in d).items())),P,count

def M0_has(e,branch=OD,partner=0):
    return legal_ring(e,'-',branch) and not(e[partner]>=1 and e[9+partner]>=1)

def J_has(e,branch=OD,partner=0):
    if not legal_ring(e,'-',branch):return False
    even=set(range(6))-set(branch)
    if sum(e[i] for i in even)==0:return False
    if e[partner]>=1 and e[9+partner]>=1:
        rem=list(e);rem[partner]-=1
        if any(rem[i]>0 for i in even):return False
    return True

def predicted(model,alpha,ring,branch=OD,partner=0):
    ans=Counter();w=model[2]
    if ring=='C':
        allowed=subsets(tuple(range(5)));fun=lambda e:legal_ring(e,'C',branch)
    elif ring=='+':
        allowed=subsets((3,4));fun=lambda e:legal_ring(e,'C',branch)
    elif ring=='-':
        allowed=subsets((0,1,2,4));fun=lambda e:M0_has(e,branch,partner)
    elif ring=='B':
        for eta in ((),(4,)):
            e=es(alpha,w[eta])
            if M0_has(e,branch,partner):ans[len(eta)]+=1
            for j in subsets((0,1,2))[1:]:
                s=j+eta
                if J_has(es(alpha,w[s]),branch,partner):ans[len(s)]+=1
        return dict(sorted(ans.items()))
    else:raise ValueError(ring)
    for s in allowed:
        if fun(es(alpha,w[s])):ans[len(s)]+=1
    return dict(sorted(ans.items()))

def census(model):
    # All breakpoints of the selected/source wedge weights and quotient ideals.
    dims=[(0,1,2)]*6;dims[3]=(0,1,2,3)
    records=Counter();blocks=0;pivots=0;matrices=0
    for xx in product(*dims):
        for t0,t3 in product(range(3),repeat=2):
            alpha=ex({**{i:a for i,a in enumerate(xx)},9:t0,12:t3})
            for ring in ('B','+','-','C'):
                g,d=hom_block(model,alpha,ring)
                # Check every boundary square; each is an exact integer equality.
                for s in g:check(not lin(d,d[s]),'homogeneous_d_squared')
                actual,_,p=reduce_units(g,d)
                check(actual==predicted(model,alpha,ring),'module_formula_matches_full_homology')
                matrices+=1;pivots+=p;records[(ring,tuple(actual.items()))]+=1
            blocks+=1
    return {'degree_patterns':blocks,'complexes':matrices,'unit_cancellations':pivots,
            'profile_count':len(records)}

def conductor_connectors(models):
    D=models['split_selected'];U=models['split_raw'];br=models['branch'];p=models['partner'];v=ex({p:1,9+p:1})
    records=[]
    for j in subsets((0,1,2))[1:]:
        for eps in (0,1):
            ss=j+(3,)+((4,) if eps else ())
            tt=j+((4,) if eps else ())
            # Difference map is plus minus minus. Lift on the minus sheet.
            c=pm(len(j)+1)
            lift=scale(one(ss),-c)
            image={(tt,v):1}
            for S in (D,U):
                bound=rd(S,lift,'-',br)
                check(bound==image,'connector_actual_minus_lift_boundary')
                check(not rd(S,image,'B',br),'connector_native_cycle')
                check(not restrict(image,'+',br),'connector_plus_image_zero')
            alpha=ea(D[2][tt],v)
            g,d=hom_block(D,alpha,'B',br);hs,pr,_=reduce_units(g,d,True)
            val=lin(pr,{tt:1})
            check(bool(val) and any(abs(z)==1 for z in val.values()),'connector_integrally_primitive_nonboundary')
            # Every short variable annihilates this class. All annihilations
            # are witnessed in the original polynomial node complex.
            for a in range(6):
                multiple=mul(image,ex({a:1}))
                if a in br:
                    check(not restrict(multiple,'B',br),'odd_annihilator_is_node_relation')
                else:
                    witness=mul(one(ss),ex({a:1}),pm(len(j)))
                    check(rd(D,witness,'B',br)==multiple,'even_annihilator_has_existing_Koszul_witness')
            factor=ZERO
            for i in j:factor=ea(factor,ex({9+br[i]:1}))
            check(apply(models['split_selection'],image)==mul(image,factor),'connecting_selection_exact_factor')
            selected_lift=apply(models['split_selection'],lift)
            check(rd(D,selected_lift,'-',br)==mul(image,factor),'selection_commutes_with_connecting_lift')
            for central_set in subsets(tuple(range(6))):
                survives=not(({p}|set(br[i] for i in j))&set(central_set))
                check(bool(central(mul(image,factor),central_set))==survives,'all_Rees_faces_connector_selection')
                check(central(one((4,)),central_set)==one((4,)),'split_eta_survives_all_Rees_faces')
            records.append({'odd_subset':[br[i] for i in j],'eta':eps,'homological_degree':len(tt),
                            'sign_of_conductor_input':c,'Rees_order':len(j),
                            'source_wedge':list(ss),'target_cycle_wedge':list(tt),
                            'target_coefficient':f't{p}*X{p}',
                            'selection_multiplier':[f't{br[i]}' for i in j]})
    return records


def central_block(model,alpha,ring,central_labels,branch=OD):
    ok=lambda e:legal_ring(e,ring,branch) and all(e[9+i]==0 for i in central_labels)
    g={s:n for s,n in model[0].items() if ok(es(alpha,model[2][s]))}
    d={s:{} for s in g}
    for s in g:
        coeff=es(alpha,model[2][s])
        for (ss,e),c in model[1][s].items():
            ee=ea(coeff,e)
            if ok(ee):
                check(ss in g and ee==es(alpha,model[2][ss]),'central_block_domain')
                d[s][ss]=c
    return g,d

def central_selection_matrix(raw,selected,table,alpha,ring,center,branch=OD):
    sg,sd=central_block(raw,alpha,ring,center,branch)
    tg,td=central_block(selected,alpha,ring,center,branch)
    mat={s:{} for s in sg}
    for s in sg:
        coeff=es(alpha,raw[2][s])
        for (t,e),c in table[s].items():
            ee=ea(coeff,e)
            if legal_ring(ee,ring,branch) and all(ee[9+i]==0 for i in center):
                check(t in tg and ee==es(alpha,selected[2][t]),'central_selection_domain')
                mat[s][t]=c
    for s in sg:check(lin(td,mat[s])==lin(mat,sd[s]),'central_complete_selection_chain')
    cg={('t',t):n for t,n in tg.items()};cg.update({('s',s):n+1 for s,n in sg.items()})
    cd={('t',t):{('t',tt):c for tt,c in v.items()} for t,v in td.items()}
    for s in sg:cd['s',s]=add({('t',t):c for t,c in mat[s].items()},{('s',ss):-c for ss,c in sd[s].items()})
    hs,_,_=reduce_units(sg,sd);ht,_,_=reduce_units(tg,td);hc,_,_=reduce_units(cg,cd)
    ranks={};prev=0
    for n in range(8):
        im=ht.get(n,0)+hs.get(n-1,0)-hc.get(n,0)-prev
        check(0<=im<=min(hs.get(n,0),ht.get(n,0)),'central_image_long_exact_sequence')
        ranks[n]=im;prev=im
    return hs,ht,hc,ranks

def first_jet_and_central_image(models):
    D=models['split_selected'];U=models['split_raw'];br=models['branch'];p=models['partner']
    v=ex({p:1,9+p:1});center=br;records=[]
    for j in subsets((0,1,2))[1:]:
        for eps in (0,1):
            tt=j+((4,) if eps else ());alpha=ea(D[2][tt],v);k=len(tt)
            hs,ht,hc,ranks=central_selection_matrix(U,D,models['split_selection'],alpha,'B',center,br)
            check(ht.get(k)==1,'central_prescribed_attachment_target_rank_one')
            want=int(len(j)==1)
            check(ranks[k]==want,'central_conductor_attachment_exact_image')
            # The raw connecting representative becomes a boundary at this
            # center. It is distinct from the alternative first-jet lift.
            ss=j+(3,)+((4,) if eps else ());im={(tt,v):1}
            rawd={s:central(z,center) for s,z in U[1].items()}
            witness=scale(one(ss),pm(len(j)))
            check(restrict(apply(rawd,witness),'B',br)==im,'raw_attachment_is_boundary_at_branch_center')
            if len(j)==1:
                i=j[0];s0=(3,)+((4,) if eps else ())
                jet=mul(one(s0),ex({br[i]:1}))
                check(not rd(U,jet,'B',br),'native_first_jet_is_actual_raw_cycle')
                check(apply(models['split_selection'],jet)==jet,'selection_preserves_first_jet_lift')
                check(rd(D,one(ss),'B',br)==add(jet,scale(im,-1)),'first_jet_to_conductor_explicit_homotopy')
            records.append({'branch_subset':[br[i] for i in j],'eta':eps,'degree':k,
                            'source_H':hs,'target_H':ht,'cone_H':hc,'image_rank':ranks[k]})
    # The first-jet formula is tested on every polynomial monomial domain
    # through degree five, and A-linearity on every ambient variable. The
    # all-polynomial proof uses I/I^2 and appears in the derivation.
    def jet_coeff(e):
        if not legal_ring(e,'+',br):return {}
        if sum(e[i] for i in br)!=1:return {}
        i=next(i for i in br if e[i]);r=list(e);r[i]-=1
        return {i:tuple(r)}
    for powers in product(range(6),repeat=3):
        if not any(powers):continue
        e=ex({i:a for i,a in zip(br,powers)});j=jet_coeff(e)
        check(bool(j)==(sum(powers)==1),'first_jet_kernel_exact_degree_test')
        for a in range(6):
            after=jet_coeff(ea(e,ex({a:1})))
            check(not after,'first_jet_A_linearity_in_conductor_target')
        for i in range(6):
            after=jet_coeff(ea(e,ex({9+i:1})))
            check(after=={a:ea(ee,ex({9+i:1})) for a,ee in j.items()},'first_jet_Rees_linearity')
    return {'rank_one_lifts':sum(r['image_rank'] for r in records),
            'missing_rank_one_targets':sum(1-r['image_rank'] for r in records),
            'records':records,
            'first_jet_map':'I_branch*h_partner -> C*v*span(h_branch); Xi*h_partner maps to v*hi',
            'kernel':'I_branch^2*h_partner',
            'meaning':'The prescribed source selection reaches all six first-conormal/eta attachment channels, but none of the eight higher-wedge channels, at the branch Rees center.'}


def higher_image_ideals(models):
    def no_eta(S):return ({s:n for s,n in S[0].items() if 4 not in s},
                         {s:v for s,v in S[1].items() if 4 not in s},
                         {s:w for s,w in S[2].items() if 4 not in s})
    D=no_eta(models['split_selected']);U=no_eta(models['split_raw'])
    F={s:v for s,v in models['split_selection'].items() if 4 not in s}
    br=models['branch'];p=models['partner'];v=ex({p:1,9+p:1});tested=0
    for j in subsets((0,1,2))[1:]:
        for powers in product(range(3),repeat=3):
            e=ex({9+br[i]:powers[i] for i in range(3)})
            alpha=ea(ea(D[2][j],v),e)
            hs,ht,hc,rank=central_selection_matrix(U,D,F,alpha,'B',(),br)
            check(ht.get(len(j))==1,'full_Rees_conductor_line_rank_one')
            want=int(len(j)==1 or all(powers[i]>=1 for i in j))
            check(rank[len(j)]==want,'full_Rees_exact_image_ideal')
            tested+=1
    return {'complete_homology_map_frames':tested,
            'size_one':'C; primitive lift Xi*h0, including its eta-labelled counterpart',
            'size_two':'(ti*tj)*C',
            'size_three':'(t1*t3*t5)*C',
            'argument':'For k>=2, the raw native homology is J tensor exterior^k(raw branch normals), so selection multiplies each labelled wedge by its exact t-product. Extra H1 cycles Xi*h0 supply the primitive first-jet lift.'}

def permutation_exponent(e,per):
    out=list(e)
    for i in range(6):out[per(i)]=e[i];out[9+per(i)]=e[9+i]
    return tuple(out)

def transport_source(v,source_branch,target_branch,per):
    position={a:i for i,a in enumerate(target_branch)}
    pmap={i:position[per(a)] for i,a in enumerate(source_branch)};pmap.update({3:3,4:4})
    out={}
    for (s,e),c in v.items():
        images=tuple(pmap[i] for i in s)
        sg=pm(sum(images[i]>images[j] for i in range(len(images)) for j in range(i+1,len(images))))
        out=add(out,{(tuple(sorted(images)),permutation_exponent(e,per)):sg*c})
    return out

def source_transport_audit(base,other,per):
    br=base['branch'];tar=other['branch']
    for typ in ('raw','selected','split_raw','split_selected'):
        S=base[typ];T=other[typ]
        for s in S[0]:
            tr=transport_source(one(s),br,tar,per)
            check(apply(T[1],tr)==transport_source(S[1][s],br,tar,per),'six_source_transports_chain_equation')
    for s in base['raw'][0]:
        left=transport_source(base['selection'][s],br,tar,per)
        right=apply(other['selection'],transport_source(one(s),br,tar,per))
        check(left==right,'six_source_selection_naturality')
    for support in subsets(tuple(range(6))):
        e=ex({i:1 for i in support});v=one(())
        v=mul(v,e)
        for ring in ('B','+','-','C'):
            check(transport_source(restrict(v,ring,br),br,tar,per)==restrict(transport_source(v,br,tar,per),ring,tar),'six_normalization_transports_keep_quotient_maps')

# Original native free resolution, cap, and target are reconstructed below.
def node():
    bot=('P',(),());g={bot:0};d={bot:{}};w={bot:ZERO}
    for u in subsets(EV)[1:]:
        for v in subsets(OD)[1:]:
            b=('P',u,v);g[b]=len(u)+len(v)-1;w[b]=ex({i:1 for i in u+v});z={}
            if len(u)==len(v)==1:z[bot,ex({u[0]:1,v[0]:1})]=1
            else:
                if len(u)>1:
                    for j,i in enumerate(u):z[('P',u[:j]+u[j+1:],v),ex({i:1})]=pm(j)
                if len(v)>1:
                    for j,i in enumerate(v):z[('P',u,v[:j]+v[j+1:]),ex({i:1})]=pm(len(u)-1+j)
            d[b]=z
    return g,d,w

def diag(i,j):return tuple(sorted((i%6,j%6)))

def cross(a,b):
    x,y=a;u,v=b
    return x<u<y<v or u<x<v<y
DS=tuple((i,j) for i in range(6) for j in range(i+1,6) if j-i not in (1,5))
SHORT=tuple(diag(i,i+2) for i in range(6));LONG=tuple(diag(i,i+3) for i in range(3))
IX={a:i for i,a in enumerate(SHORT+LONG)}
FACES=tuple(f for k in range(4) for f in combinations(DS,k) if all(not cross(a,b) for a,b in combinations(f,2)))
CELLS=tuple((f,h) for f in FACES for h in subsets(f))
VP=tuple(sorted(SHORT[i] for i in OD));VM=tuple(sorted(SHORT[i] for i in EV))
GAMMA=ex({15:1,16:1,17:1})

def cell_degree(c):return 3-len(c[0])+len(c[1])

def omega(t):
    f=tuple(sorted(SHORT[i] for i in t))
    if f not in FACES:return {}
    e=ea(GAMMA,ex({9+i:-1 for i in t}));z={((f,()),e):1}
    for l in LONG:
        if all(not cross(l,b) for b in f):
            c=(tuple(sorted(f+(l,))),(l,));m=ea(e,ex({IX[l]:1,9+IX[l]:-1}))
            z[c,m]=-pm(sum(b>l for b in f))
    return z

def cap_sign(i):
    t=tuple(a for a in ORDER if a not in i)
    inv=sum(SHORT[t[a]]>SHORT[t[b]] for a in range(len(t)) for b in range(a+1,len(t)))
    return pm(len(t)+sum(ORDER.index(a) for a in t)+inv)

def graph_exp(e):
    out=list(e)
    for i in range(6):out[i]+=out[9+i]
    return tuple(out)

def graph(v):return {(c,graph_exp(e)):a for (c,e),a in v.items()}

def target_boundary(c):
    f,h=c;out={}
    for a in DS:
        if a not in f and all(not cross(a,b) for b in f):
            t=(tuple(sorted(f+(a,))),h)
            out[t,graph_exp(ex({IX[a]:1,9+IX[a]:-1}))]=pm(sum(b<a for b in f))
    for j,a in enumerate(h):out[(f,tuple(b for b in h if b!=a)),ZERO]=pm(3-len(f)+j)
    return out

BD={c:target_boundary(c) for c in CELLS}

def target_legal(c,e):
    local={IX[a] for a in c[0] if a not in c[1]}
    return all(e[i]>=0 or i in local for i in range(6)) and all(e[i]>=0 for i in range(6,9)) and all(e[9+i]>=0 or i in local for i in range(9))

def cap_data():
    P=node();cap={i:scale(omega(tuple(j for j in ORDER if j not in i)),cap_sign(i)) for i in subsets(ORDER)}
    F={b:({} if not b[1] else graph(scale(cap[b[1]+b[2]],-pm(len(b[1]))))) for b in P[0]}
    aa={b:add(apply(BD,F[b]),scale(apply(F,P[1][b]),-1)) for b in P[0]}
    for b in P[0]:
        check(all(c[0] in (VP,VM) for c,e in aa[b]),'native_cap_defect_is_both_endpoints')
        check(all(target_legal(c,e) for c,e in F[b]),'native_cap_original_stalk_domains')
        check(add(apply(BD,aa[b]),apply(aa,P[1][b]))=={},'native_endpoint_cochain_closed')
    check(sum(map(len,F.values()))==43,'native_cap_43_terms')
    check(sum(map(len,aa.values()))==6,'native_endpoint_6_terms')
    return P,F,aa

def tensor_d(left_g,left_d,right):
    g={};d={}
    for a,n in left_g.items():
        for s,k in right[0].items():
            b=(a,s);g[b]=n+k
            z={((aa,s),e):c for (aa,e),c in left_d[a].items()}
            z=add(z,{((a,ss),e):pm(n)*c for (ss,e),c in right[1][s].items()})
            d[b]=z
    return g,d

def tensor_map(table,S):return {(p,s):{((c,s),e):a for (c,e),a in v.items()} for p,v in table.items() for s in S[0]}

def cap_tensor_audit(models):
    P,F,a=cap_data();D=models['selected'];U=models['raw']
    sg,sd=tensor_d(P[0],P[1],D)
    tg,td=tensor_d({c:cell_degree(c) for c in CELLS},BD,D)
    ff=tensor_map(F,D);aa=tensor_map(a,D)
    for b in sg:
        check(not apply(sd,sd[b]),'native_excess_1600_source_d_squared')
        check(add(apply(td,ff[b]),scale(apply(ff,sd[b]),-1))==aa[b],'complete_cap_excess_tensor_equation')
        check(not add(apply(td,aa[b]),apply(aa,sd[b])),'complete_endpoint_excess_tensor_closed')
    # Strict commuting squares for the actual selection, on both cap parts.
    for p in P[0]:
        for s in U[0]:
            for table in (F,a):
                first={}
                for (c,e),v in table[p].items():
                    for (ss,m),w in models['selection'][s].items():first=add(first,{((c,ss),ea(e,m)):v*w})
                second={}
                for (ss,m),w in models['selection'][s].items():
                    for (c,e),v in table[p].items():second=add(second,{((c,ss),ea(e,m)):w*v})
                check(first==second,'whole_cap_selection_square')
    return {'source_generators':len(sg),'target_generators':len(tg),
            'cap_terms':sum(map(len,ff.values())),'endpoint_terms':sum(map(len,aa.values()))}

def homogeneous_hom(S,T,lam):
    g={};coef={};d={}
    for a,da in S[0].items():
        for b,db in T[0].items():
            e=es(ea(S[2][a],lam),T[2][b])
            if min(e)>=0:g[a,b]=db-da;coef[a,b]=e
    inc={a:[] for a in S[0]}
    for a,v in S[1].items():
        for (aa,e),z in v.items():inc[aa].append((a,e,z))
    for (a,b),n in g.items():
        v={}
        for (bb,e),z in T[1][b].items():
            y=a,bb;check(y in g and ea(coef[a,b],e)==coef[y],'source_comparison_target_degree')
            v=add(v,{y:z})
        for aa,e,z in inc[a]:
            y=aa,b;check(y in g and ea(coef[a,b],e)==coef[y],'source_comparison_source_degree')
            v=add(v,{y:-pm(n)*z})
        d[a,b]=v
    return g,d,coef

def primitive_replacement_gate(P,models):
    # A possible identification of the native conductor dual with the dual
    # selected excess must at least have a unit coefficient on this top pair.
    pt=('P',EV,OD);dt=tuple(range(5));D=models['selected']
    lam=es(D[2][dt],P[2][pt]);g,d,coef=homogeneous_hom(P,D,lam)
    for b in g:check(not lin(d,d[b]),'replacement_Hom_d_squared')
    hh,_,p=reduce_units(g,d)
    check(not hh,'primitive_top_frame_entire_Hom_acyclic')
    check(max(g.values())==0,'primitive_top_frame_no_positive_homological_degree')
    # Thus even the cycles of map degree zero vanish, not just their classes.
    check((pt,dt) in g and coef[pt,dt]==ZERO,'primitive_top_coordinate_included')
    return {'columns':len(g),'unit_pivots':p,'homology':hh,'top_degree':0,'internal_degree':lam,
            'conclusion':'No ordinary degree-zero homogeneous chain map has a unit native-top to selected-excess-top coefficient.'}

def main(output,quick=False):
    started=time.time();m=source_models();D=m['split_selected']
    for S in (m['selected'],m['raw'],D,m['split_raw']):
        for ring in ('B','+','-','C'):
            dd=base_change(S,ring)
            for s in S[0]:check(not apply(dd,dd[s]),'actual_normalization_stalk_d_squared')
    census_result=census(D) if not quick else {'skipped':True}
    connectors=conductor_connectors(m)
    central_images=first_jet_and_central_image(m)
    image_ideals=higher_image_ideals(m)
    # Full source matrix checks on every conjugate selected branch/pair.
    orbit=[]
    for reflected in (False,True):
        for rot in range(3):
            per=lambda i:(2*rot+(1-i if reflected else i))%6
            branch=tuple(sorted(per(i) for i in OD));partner=per(0);shared=per(3)
            mm=source_models(branch,partner,shared)
            rr=conductor_connectors(mm)
            source_transport_audit(m,mm,per)
            check(len(rr)==14,'six_labelled_charts_keep_all_connectors')
            orbit.append({'branch':branch,'partner':partner,'shared':shared,'connectors':14})
    tensor=cap_tensor_audit(m)
    gate=primitive_replacement_gate(node(),m)
    result={
      'status':'proved_native_normalization_pullback_and_conductor_transport_for_the_declared_selected_Rees_source',
      'commit':COMMIT,'source_blobs':SOURCE_BLOBS,
      'selected_source_equations':['X1','X3','X5','t0*X0','t3*X3'],
      'independent_excess':'eta=t3*h3_branch-h3_pair; integral basis change determinant -1',
      'normalization_branch_profiles':{
          'plus':{'coefficient':'C=R','exterior_generators':['h0','eta'],'ranks':[1,2,1]},
          'minus':{'coefficient':'M=R[X0,X2,X4]/(t0*X0)','exterior_generators':['h1','h3','h5','eta'],'ranks':[1,4,6,4,1]},
          'conductor':{'coefficient':'C=R','exterior_generators':['h1','h3','h5','h0','eta'],'ranks':[1,5,10,10,5,1]}},
      'native_homology_modules':{'0':'M','1':'J^3 + M*eta','2':'J^3 + J^3*eta','3':'J + J^3*eta','4':'J*eta','other':'0'},
      'J':'(X0,X2,X4)/(t0*X0*(X0,X2,X4)) over R[X0,X2,X4]',
      'exterior_determinants':'All h-subset and eta internal degrees retained; unshifted multiplicities above are not identifications of frames.',
      'exact_conductor_module_sequence':'0 -> C<v> -> J -> M -> C -> 0, v=t0*X0; C<v> maps 1 to [v]',
      'native_conductor_connectors':connectors,
      'connector_counts_by_homology_degree':dict(sorted(Counter(r['homological_degree'] for r in connectors).items())),
      'connector_counts_by_Rees_order':dict(sorted(Counter(r['Rees_order'] for r in connectors).items())),
      'all_connector_annihilators':'(X0,X1,X2,X3,X4,X5); no integer or Rees parameter annihilates the primitive generator',
      'central_connecting_representatives':'The 14 raw connecting representatives become boundaries after t1=t3=t5=0, and their selected images vanish. They must not be confused with all possible source classes.',
      'full_central_selection_image':central_images,
      'full_Rees_image_ideals':image_ideals,
      'normalization_degree_census':census_result,'six_orbit_charts':orbit,
      'whole_native_cap_base_change':tensor,'primitive_source_identification_gate':gate,
      'scope':[
          'Source diagram is the actual derived pullback of the normalization sequence by the selected Koszul source, not an asserted map to physical collars.',
          'The native homology formula is a formula for graded homology modules, not a formality or splitting theorem for the coupled dg object.',
          'Exterior multiplicities occur over distinct coefficient modules on the two branches.',
          'The full central map reaches six first-jet attachment channels and misses eight higher-wedge channels. Vanishing of the original connecting representatives alone would incorrectly predict that all fourteen are missed.',
          'The cap tensor equation lands in the derived-base-changed target; no unproved counit from that target to the original physical target is used.',
          'The top-frame gate is for an ordinary A-linear, degree-zero source comparison, with the full necessary internal degree adjustment allowed.',
          'Both physical collar identifications and reflection parity remain unassigned.',
          'This is exact executable algebra with an accompanying all-degree proof, not proof-assistant certification.'
      ],
      'assertions':dict(sorted(COUNT.items())),'total_exact_assertions':sum(COUNT.values()),
    }
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ('status','normalization_degree_census','connector_counts_by_homology_degree','connector_counts_by_Rees_order','whole_native_cap_base_change','primitive_source_identification_gate','total_exact_assertions')},indent=2))
    print('elapsed_seconds',round(time.time()-started,2))

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output',type=Path,default=Path('marici_native_excess_conductor_transport_certificate.json'))
    p.add_argument('--quick',action='store_true',help='Skip the exhaustive coefficient-domain census; for development only.')
    args=p.parse_args();main(args.output,args.quick)
