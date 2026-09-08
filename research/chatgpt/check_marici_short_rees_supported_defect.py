#!/usr/bin/env python3
"""Supported defect of native raw-to-selected excess transport.

Core polynomial routines are retained from the preceding checked model.
Original helper scope:

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


# New calculation. Localizations below are separate output terms, never a
# change to the original polynomial native source or target stalks.
def localized_ok(e, ring, branch, inverted, mode='loc'):
    invert={9+i for i in inverted}
    if any(x<0 and i not in invert for i,x in enumerate(e)):return False
    ep=list(e)
    for i in invert:ep[i]=max(ep[i],0)
    if not legal_ring(tuple(ep),ring,branch):return False
    if mode=='res':return any(e[i]<0 for i in invert)
    if mode=='top':return all(e[i]<0 for i in invert)
    return True


def out_reduce(v,ring,branch,inverted,mode='loc'):
    return {(b,e):c for (b,e),c in v.items() if localized_ok(e,ring,branch,inverted,mode)}


def mode_d(D,v,ring,branch,inverted,mode):
    return out_reduce(apply(D[1],v),ring,branch,inverted,mode)


def mode_block(D,alpha,ring,branch,inverted,mode):
    ok=lambda e:localized_ok(e,ring,branch,inverted,mode)
    g={s:n for s,n in D[0].items() if ok(es(alpha,D[2][s]))}
    d={s:{} for s in g}
    for s in g:
        coeff=es(alpha,D[2][s])
        for (a,m),c in D[1][s].items():
            total=ea(coeff,m)
            if ok(total):
                check(a in g and total==es(alpha,D[2][a]),'new_supported_homogeneous_domain')
                d[s][a]=c
    return g,d


def inverse_on_wedges(D,branch,labels=None):
    labels=set(branch if labels is None else labels)
    return {s:mul(one(s),ex({9+branch[i]:-1 for i in s if i<3 and branch[i] in labels})) for s in D[0]}


def cone_model(U,S,map_s):
    g={('x',a):n for a,n in S[0].items()}
    g.update({('u',a):n+1 for a,n in U[0].items()})
    w={('x',a):v for a,v in S[2].items()};w.update({('u',a):v for a,v in U[2].items()})
    d={('x',a):{(('x',b),m):c for (b,m),c in v.items()} for a,v in S[1].items()}
    for a in U[0]:
        d['u',a]=add({(('x',b),m):c for (b,m),c in map_s[a].items()},
                     {(('u',b),m):-c for (b,m),c in U[1][a].items()})
    return g,d,w


def localization_cone(U):
    # The 'x' arm is U_tau, not the selected complex.
    return cone_model(U,U,{a:one(a) for a in U[0]})


def raw_to_supported_cone(models):
    U=models['split_raw'];S=models['split_selected'];sigma=models['split_selection'];br=models['branch']
    alpha=inverse_on_wedges(S,br)
    C=cone_model(U,S,sigma);L=localization_cone(U)
    phi={('x',a):{(('x',b),m):c for (b,m),c in alpha[a].items()} for a in S[0]}
    phi.update({('u',a):one(('u',a)) for a in U[0]})
    beta={a:phi['x',a] for a in S[0]}
    for a in S[0]:
        check(apply(U[1],alpha[a])==apply(alpha,S[1][a]),'new_inverse_full_chain_map')
        check(apply(alpha,sigma[a])==one(a),'new_inverse_left_identity')
        check(apply(sigma,alpha[a])==one(a),'new_inverse_right_identity')
    for a in C[0]:
        check(not apply(C[1],C[1][a]),'new_selection_cone_d_squared')
        check(not apply(L[1],L[1][a]),'new_support_cone_d_squared')
        check(apply(L[1],phi[a])==apply(phi,C[1][a]),'new_whole_supported_triangle_chain')
    for a in S[0]:
        check(apply(L[1],beta[a])==apply(beta,S[1][a]),'new_selected_support_map_chain')
    for ring in ('B','+','-','C'):
        for a in C[0]:
            lhs=out_reduce(apply(L[1],phi[a]),ring,br,br)
            rhs=out_reduce(apply(phi,C[1][a]),ring,br,br)
            check(lhs==rhs,'new_all_normalization_cone_restrictions')
        for a in S[0]:
            val=out_reduce(alpha[a],ring,br,br,'res')
            check(mode_d(U,val,ring,br,br,'res')==out_reduce(apply(alpha,S[1][a]),ring,br,br,'res'),
                  'new_residue_quotient_chain_map')
    return C,L,phi,beta,alpha


def analyze_attachment_residues(models,alpha):
    U=models['split_raw'];S=models['split_selected'];br=models['branch'];p=models['partner'];v=ex({p:1,9+p:1})
    records=[]
    for J in subsets((0,1,2))[1:]:
        labels=tuple(br[i] for i in J);factor=ex({9+i:1 for i in labels});k=len(J)
        for eps in (0,1):
            w=J+((4,) if eps else ());top=J+(3,)+((4,) if eps else ())
            b=mul(one(w),v);res=out_reduce(apply(alpha,b),'B',br,br,'res')
            check(res==mul(one(w),es(v,factor)),'new_actual_residue_formula')
            check(not mode_d(U,res,'B',br,br,'res'),'new_residue_closed')
            degree=ea(S[2][w],v)
            g,d=mode_block(U,degree,'B',br,br,'res');h,pr,_=reduce_units(g,d,True)
            value=lin(pr,{w:1}) if res else {}
            nonzero=bool(value)
            check(nonzero==(k>=2),'new_six_zero_eight_nonzero_residues')
            if nonzero:check(any(abs(c)==1 for c in value.values()),'new_residue_primitive')
            # Exact product-support annihilator on all monomial divisibility types.
            tests=[]
            for powers in product(range(3),repeat=3):
                shift=ex({9+i:a for i,a in zip(br,powers)})
                rr=out_reduce(mul(res,shift),'B',br,br,'res')
                aa=ea(degree,shift);gg,dd=mode_block(U,aa,'B',br,br,'res')
                _,projection,_=reduce_units(gg,dd,True)
                cc={w:1} if rr else {}
                alive=bool(lin(projection,cc))
                wanted=(k>=2 and not all(powers[br.index(i)]>=1 for i in labels))
                check(alive==wanted,'new_all_residue_annihilator_types')
                tests.append(alive)
            # The source h0 boundary retains all partial-pole terms.
            W=mul(one(top),tuple(-a for a in factor))
            dw=mode_d(U,W,'B',br,br,'res')
            partial={}
            for pos,i in enumerate(J):
                rem=J[:pos]+J[pos+1:]+(3,)+((4,) if eps else ())
                exp=ea(ex({br[i]:1}),tuple(-a for a in factor));exp=ea(exp,ex({9+br[i]:1}))
                partial=add(partial,mul(one(rem),exp,pm(pos)))
            partial=out_reduce(partial,'B',br,br,'res')
            check(dw==add(partial,scale(res,pm(k))),'new_full_partial_pole_homotopy')
            if k==1:check(mode_d(U,scale(W,-1),'B',br,br,'res')==res,'new_first_jet_supported_nullhomotopy')
            # Project only to top local cohomology for the T-coordinate intersection.
            rtop=out_reduce(res,'B',br,labels,'top')
            wtop=out_reduce(scale(W,pm(k)),'B',br,labels,'top')
            check(mode_d(U,wtop,'B',br,labels,'top')==rtop,'new_top_intersection_residue_exact')
            # For |T|=2 the partial-pole terms are separate one-divisor cycles.
            if k==2:
                for (basis,mon),coeff in partial.items():
                    neg=tuple(i for i in br if mon[9+i]<0)
                    check(len(neg)==1,'new_pair_partial_pole_single_divisor')
                    term={(basis,mon):coeff}
                    check(not mode_d(U,term,'B',br,neg,'res'),'new_pair_partial_pole_cycle')
            # Native occurrence annihilators retain their existing polynomial witnesses.
            for i in range(6):
                rr=out_reduce(mul(res,ex({i:1})),'B',br,br,'res')
                if i in br:check(not rr,'new_residue_odd_annihilator')
                else:
                    wh=mul(W,ex({i:1}),pm(k))
                    check(mode_d(U,wh,'B',br,br,'res')==rr,'new_residue_even_annihilator_homotopy')
            records.append({'branch_subset':list(labels),'eta':eps,'homological_degree':len(w),
                'supported_class_nonzero':nonzero,'residue_reduced_H':h,
                'Rees_annihilator':list(labels) if nonzero else 'unit',
                'top_intersection_projection':'boundary',
                'partial_pole_terms':len(partial),
                'annihilator_divisibility_frames':len(tests)})
    return records


def parameter_cube(models):
    br=models['branch'];u=models['split_raw'];p=models['partner'];shared=models['shared']
    allsets=subsets(br);stages={}
    for P0 in allsets:
        eq=[ex({i:1}) if i in P0 else ex({i:1,9+i:1}) for i in br]
        eq += [ex({p:1,9+p:1}),None]
        weights=eq[:4]+[ex({shared:1,9+shared:1})]
        stages[P0]=koszul(eq,weights)
    maps={};inverses={}
    for P0 in allsets:
        for Q0 in allsets:
            if not set(P0)<=set(Q0):continue
            added=set(Q0)-set(P0)
            f={w:mul(one(w),ex({9+br[i]:1 for i in w if i<3 and br[i] in added})) for w in u[0]}
            inv=inverse_on_wedges(stages[Q0],br,added)
            maps[P0,Q0]=f;inverses[P0,Q0]=inv
            for w in u[0]:
                check(apply(stages[Q0][1],f[w])==apply(f,stages[P0][1][w]),'new_partial_selection_chain')
                check(apply(stages[P0][1],inv[w])==apply(inv,stages[Q0][1][w]),'new_partial_inverse_chain')
    triples=0
    for P0 in allsets:
        for Q0 in allsets:
            for R0 in allsets:
                if not set(P0)<=set(Q0)<=set(R0):continue
                triples+=1
                for w in u[0]:
                    check(apply(maps[Q0,R0],maps[P0,Q0][w])==maps[P0,R0][w],'new_partial_selection_composition')
                    check(apply(inverses[P0,Q0],inverses[Q0,R0][w])==inverses[P0,R0][w],'new_local_inverse_composition')
    return {'stages':len(stages),'comparable_pairs_including_identities':len(maps),'composable_triples_including_identities':triples}


def central_cone_checks(models,C,L,phi,beta):
    U=models['split_raw'];S=models['split_selected'];br=models['branch']
    def specialize_model(M,center,kill_local_arm=False):
        gg={b:n for b,n in M[0].items() if not(kill_local_arm and center and b[0]=='x')}
        dd={b:{(a,e):c for (a,e),c in central(M[1][b],center).items() if a in gg} for b in gg}
        ww={b:M[2][b] for b in gg}
        return gg,dd,ww
    records=[]
    for center in subsets(br):
        C0=specialize_model(C,center)
        L0=specialize_model(L,center,True)
        phi0={b:{(a,e):c for (a,e),c in phi[b].items() if a in L0[0] and (a[0]=='x' or all(e[9+i]==0 for i in center))} for b in C0[0]}
        # In a nonempty central face every localized target arm vanishes.
        if center:
            for b in C0[0]:
                check(phi0[b]==({} if b[0]=='x' else one(b)),'new_central_cone_is_raw_projection')
                check(apply(L0[1],phi0[b])==apply(phi0,C0[1][b]),'new_central_cone_map_chain')
            for b in S[0]:check(not phi0['x',b],'new_central_selected_residue_map_zero')
        records.append({'center':list(center),'remaining_support_cone_generators':len(L0[0]),
                        'selected_to_support_is_zero':bool(center)})
    # Check that the eight obstructed selected classes remain nonzero in the full central selection cone.
    p=models['partner'];v=ex({p:1,9+p:1})
    for J in subsets((0,1,2))[1:]:
        for eps in (0,1):
            w=J+((4,) if eps else ());alpha=ea(S[2][w],v)
            hs,ht,hc,ranks=central_selection_matrix(U,S,models['split_selection'],alpha,'B',br,br)
            check(ranks[len(w)]==int(len(J)==1),'new_central_no_supported_ordinary_repair')
    return records


def cap_on_whole_supported_triangle(C,L,phi):
    P,F,a=cap_data()
    sg,sd=tensor_d(P[0],P[1],C)
    kg={c:cell_degree(c) for c in CELLS}
    tg,td=tensor_d(kg,BD,L)
    def product_map(table):
        result={}
        for p in P[0]:
            for b in C[0]:
                value={}
                for (c,e),z in table[p].items():
                    for (bb,m),zz in phi[b].items():
                        value=add(value,{((c,bb),ea(e,m)):z*zz})
                result[p,b]=value
        return result
    FF=product_map(F);AA=product_map(a)
    for b in sg:
        check(not apply(sd,sd[b]),'new_whole_supported_source_d_squared')
        check(add(apply(td,FF[b]),scale(apply(FF,sd[b]),-1))==AA[b],'new_whole_cap_supported_triangle')
        check(not add(apply(td,AA[b]),apply(AA,sd[b])),'new_both_endpoints_supported_closed')
        for ((cell,arm),e),c in FF[b].items():
            ep=list(e)
            if arm[0]=='x':
                for i in OD:ep[9+i]=max(ep[9+i],0)
            check(target_legal(cell,tuple(ep)),'new_cap_poles_only_in_declared_output')
        for ((cell,arm),e),c in AA[b].items():
            check(cell[0] in (VP,VM),'new_actual_two_endpoints_retained')
    return {'source_generators':len(sg),'target_generators':len(tg),
            'cap_terms':sum(map(len,FF.values())),'endpoint_terms':sum(map(len,AA.values()))}


def source_to_cone_cartier_map(models,C,L,phi,branch_subset,eps):
    br=models['branch'];p=models['partner'];U=models['split_raw'];S=models['split_selected']
    J=tuple(br.index(i) for i in branch_subset);k=len(J);degree=k+eps
    w=J+((4,) if eps else ());top=J+(3,)+((4,) if eps else ())
    v=ex({p:1,9+p:1});factor=ex({9+i:1 for i in branch_subset})
    resolution=koszul([ex({i:1}) for i in range(6)]+[factor])
    table={a:{} for a in resolution[0]}
    table[()]={(('x',w),v):1}
    for i in set(range(6))-set(br):
        table[i,]={(('x',top),ex({i:1})):pm(k)}
    table[6,]={(('u',w),v):1}
    for i in set(range(6))-set(br):
        table[i,6]={(('u',top),ex({i:1})):pm(k+1)}
    # A degree-d homological map uses d f=(-1)^d f d.
    table={a:scale(val,pm(degree*len(a))) for a,val in table.items()}
    for a in resolution[0]:
        lhs=restrict(apply(C[1],table[a]),'B',br)
        rhs=restrict(scale(apply(table,resolution[1][a]),pm(degree)),'B',br)
        check(lhs==rhs,'new_complete_128_column_Cartier_to_defect_map')
    comp={a:apply(phi,z) for a,z in table.items()}
    for a in resolution[0]:
        check(out_reduce(apply(L[1],comp[a]),'B',br,br)==
              out_reduce(scale(apply(comp,resolution[1][a]),pm(degree)),'B',br,br),
              'new_complete_128_column_supported_Cartier_composition')
    return resolution,table,comp,degree,ea(S[2][w],v),w,top


def node_hom_frame(S,T,lam,branch,center):
    ok=lambda e:legal_ring(e,'B',branch) and all(e[9+i]==0 for i in center)
    g={};coef={};d={}
    for a,da in S[0].items():
        for b,db in T[0].items():
            e=es(ea(S[2][a],lam),T[2][b])
            if ok(e):g[a,b]=db-da;coef[a,b]=e
    inc={a:[] for a in S[0]}
    for a,z in S[1].items():
        for (aa,e),c in z.items():inc[aa].append((a,e,c))
    for (a,b),n in g.items():
        z={}
        for (bb,e),c in T[1][b].items():
            ee=ea(coef[a,b],e)
            if not ok(ee):continue
            y=(a,bb);check(y in g and coef[y]==ee,'new_full_native_Hom_target_domain')
            z=add(z,{y:c})
        for aa,e,c in inc[a]:
            ee=ea(coef[a,b],e)
            if not ok(ee):continue
            y=(aa,b);check(y in g and coef[y]==ee,'new_full_native_Hom_source_domain')
            z=add(z,{y:-pm(n)*c})
        d[a,b]=z
    for a in g:check(not lin(d,d[a]),'new_full_native_Hom_d_squared')
    return g,d,coef


def complete_central_Gysin_channels(models,C,L,phi):
    br=models['branch'];U=models['split_raw'];p=models['partner']
    L0g={('u',a):n+1 for a,n in U[0].items()}
    L0d={('u',a):{(('u',b),e):-c for (b,e),c in central(U[1][a],br).items()} for a in U[0]}
    L0w={('u',a):w for a,w in U[2].items()};L0=L0g,L0d,L0w
    records=[];maps=[]
    for labels in subsets(br):
        if len(labels)<2:continue
        for eps in (0,1):
            K,j,psi,m,lam,w,top=source_to_cone_cartier_map(models,C,L,phi,labels,eps)
            K0=(K[0],{a:central(z,br) for a,z in K[1].items()},K[2])
            psi0={a:{(b,e):c for (b,e),c in z.items() if b in L0g and all(e[9+i]==0 for i in br)} for a,z in psi.items()}
            # Remove the boundary-valued product-Cartier row, retaining all
            # rows generated by the normalization zero-section equations.
            H={a:{} for a in K0[0]};H[6,]={(('u',top),ZERO):pm(eps+1)}
            residual={};explicit={a:{} for a in K0[0]}
            for i in br:explicit[i,6]={(('u',top),ex({i:1})):pm(len(labels))}
            for a in K0[0]:
                dH=restrict(add(apply(L0d,H[a]),scale(apply(H,K0[1][a]),pm(m))),'B',br)
                residual[a]=restrict(add(psi0[a],scale(dH,-1)),'B',br)
                check(residual[a]==explicit[a],'new_central_Gysin_is_native_conductor_three_rows')
                check(restrict(apply(L0d,residual[a]),'B',br)==
                      restrict(scale(apply(residual,K0[1][a]),pm(m)),'B',br),
                      'new_central_Gysin_three_row_chain')
            gg,dd,cf=node_hom_frame(K0,L0,lam,br,br)
            hs,pr,piv=reduce_units(gg,dd,True)
            vec={}
            for a,z in residual.items():
                for (b,e),c in z.items():
                    check((a,b) in cf and cf[a,b]==e,'new_central_Gysin_in_full_Hom_frame')
                    vec[a,b]=c
            vv=lin(pr,vec)
            check(bool(vv) and any(abs(x)==1 for x in vv.values()),'new_central_complete_Gysin_primitive_nonzero')
            # The three-row cocycle is exactly the source's odd-sheet
            # normalization cocycle, with a retained product-Cartier generator.
            for i in range(6):
                multiplied={a:restrict(mul(z,ex({i:1})),'B',br) for a,z in residual.items()}
                if i not in br:
                    check(not any(multiplied.values()),'new_central_Gysin_even_occurrence_annihilator')
                else:
                    witness={a:{} for a in K0[0]}
                    witness[6,]={(('u',top),ex({i:1})):pm(eps)}
                    for a in K0[0]:
                        bd=restrict(add(apply(L0d,witness[a]),scale(apply(witness,K0[1][a]),pm(m))),'B',br)
                        check(bd==multiplied[a],'new_central_Gysin_odd_annihilator_homotopy')
            records.append({'branch_subset':list(labels),'eta':eps,'map_homological_degree':m,
                'complete_Cartier_source_generators':len(K[0]),'nonzero_original_source_columns':sum(bool(z) for z in j.values()),
                'central_supported_cochain_rows':sum(map(len,psi0.values())),
                'central_normalization_rows':sum(map(len,residual.values())),
                'complete_central_Hom_columns':len(gg),'Hom_homology':hs,'unit_cancellations':piv,
                'primitive_central_Gysin':True})
            maps.append((K,j,psi,m))
    return records,maps






def integral_block_homotopy(g,initial):
    """Explicit signed-unit SDR, including the original-basis homotopy."""
    d={a:dict(v) for a,v in initial.items()};I={a:{a:1} for a in g};P={a:{a:1} for a in g};H={a:{} for a in g}
    while True:
        hit=next(((b,a,c) for b,v in d.items() for a,c in v.items() if abs(c)==1),None)
        if hit is None:break
        b,a,c=hit
        for x in g:
            if P[x].get(a):H[x]=add(H[x],scale(I[b],c*P[x][a]))
        survivors=[x for x in d if x not in (a,b)]
        proj={x:{x:1} for x in survivors};proj[b]={}
        proj[a]={y:-c*z for y,z in d[b].items() if y!=a}
        inc={x:add({x:1},{b:-c*d[x].get(a,0)}) for x in survivors}
        I={x:lin(I,z) for x,z in inc.items()};P={x:lin(proj,z) for x,z in P.items()}
        d={x:lin(proj,lin(d,z)) for x,z in inc.items()}
    for x in g:
        lhs=add(lin(initial,H[x]),lin(H,initial[x]));rhs=add({x:1},scale(lin(I,P[x]),-1))
        check(lhs==rhs,'new_native_resolution_block_homotopy')
    return H,d


def native_free_lifts(models,C,L,phi,maps):
    P,F,a=cap_data();bottom=('P',(),())
    pg,pd,pw=P
    hg={};hd={}
    for supp in subsets(tuple(range(6))):
        alpha=ex({i:1 for i in supp});g,d=hom_block(P,alpha,'A')
        h,reduced=integral_block_homotopy(g,d)
        pure=not(set(supp)&set(EV) and set(supp)&set(OD))
        check(len(reduced)==int(pure),'new_native_resolution_all_64_support_blocks')
        hg[supp]=h
    eg,ed=tensor_d(pg,pd,C)
    kg={c:cell_degree(c) for c in CELLS};tg,td=tensor_d(kg,BD,L)
    def h_vertical(vec):
        z={}
        for ((p,c),e),a0 in vec.items():
            alpha=ea(e,pw[p]);supp=tuple(i for i in range(6) if alpha[i]>0)
            for pp,cc in hg[supp][p].items():
                coeff=es(alpha,pw[pp]);check(min(coeff)>=0,'new_resolution_lift_no_denominators')
                z=add(z,{((pp,c),coeff):a0*cc})
        return z
    def delta_right(vec):
        z={}
        for ((p,c),e),a0 in vec.items():
            for (cc,m),b in C[1][c].items():
                z=add(z,{((p,cc),ea(e,m)):a0*pm(pg[p])*b})
        return z
    def h_total(vec):
        term=h_vertical(vec);out={}
        for j in range(9):
            out=add(out,scale(term,pm(j)))
            term=h_vertical(delta_right(term))
            if not term:break
        check(not term,'new_resolution_perturbation_terminates')
        return out
    def projection(vec):
        z={}
        for ((p,c),e),a0 in vec.items():
            if p==bottom and legal_ring(e,'B'):z=add(z,{(c,e):a0})
        return z
    def compose(vec,table):
        z={}
        for ((p,c),e),a0 in vec.items():
            for (cell,m),cc in table[p].items():
                for (ccell,mm),ccc in phi[c].items():
                    z=add(z,{((cell,ccell),ea(e,ea(m,mm))):a0*cc*ccc})
        return z
    records=[]
    for source,j,psi,m in maps:
        lift={};cap={};ends={}
        for b in sorted(source[0],key=lambda x:(len(x),x)):
            naive={((bottom,c),e):cc for (c,e),cc in j[b].items()}
            target_rhs=scale(apply(lift,source[1][b]),pm(m))
            error=add(target_rhs,scale(apply(ed,naive),-1))
            check(not projection(error),'new_lift_error_native_augmentation_zero')
            check(not apply(ed,error),'new_lift_error_closed')
            correction=h_total(error)
            check(apply(ed,correction)==error,'new_lift_exact_correcting_homotopy')
            lift[b]=add(naive,correction)
            check(projection(lift[b])==j[b],'new_lift_recovers_supported_Cartier_map')
            check(apply(ed,lift[b])==target_rhs,'new_free_A_linear_complete_Gysin_lift')
            cap[b]=compose(lift[b],F);ends[b]=compose(lift[b],a)
        for b in source[0]:
            check(add(apply(td,cap[b]),scale(apply(cap,source[1][b]),-pm(m)))==ends[b],
                  'new_free_Gysin_actual_cap_endpoint_equation')
            check(not add(apply(td,ends[b]),scale(apply(ends,source[1][b]),pm(m))),
                  'new_free_Gysin_actual_endpoint_composite_closed')
            for ((cell,arm),e),cc in cap[b].items():
                ee=list(e)
                if arm[0]=='x':
                    for i in OD:ee[9+i]=max(ee[9+i],0)
                check(target_legal(cell,tuple(ee)),'new_free_lift_actual_target_stalk_domains')
        sides=Counter()
        for val in ends.values():
            for ((cell,arm),e),cc in val.items():
                check(cell[0] in (VP,VM),'new_free_lift_only_two_endpoint_supports')
                sides['plus' if cell[0]==VP else 'minus']+=1
        records.append({'map_degree':m,'free_source_columns':len(source[0]),
            'lift_terms':sum(map(len,lift.values())),
            'higher_resolution_correction_terms':sum(sum(p!=bottom for ((p,c),e) in val) for val in lift.values()),
            'actual_cap_terms':sum(map(len,cap.values())),
            'actual_endpoint_terms':dict(sides),
            'all_coefficients_polynomial_on_source':all(min(e)>=0 for val in lift.values() for (b,e) in val)})
    return records


def main(output):
    models=source_models();C,L,phi,beta,alpha=raw_to_supported_cone(models)
    records=analyze_attachment_residues(models,alpha)
    cube=parameter_cube(models)
    centers=central_cone_checks(models,C,L,phi,beta)
    cap=cap_on_whole_supported_triangle(C,L,phi)
    gysin,gysin_maps=complete_central_Gysin_channels(models,C,L,phi)
    free_lifts=native_free_lifts(models,C,L,phi,gysin_maps)
    for row,frame in zip(free_lifts,gysin):
        row['branch_subset']=frame['branch_subset'];row['eta']=frame['eta']
    transports=0
    # Six transports generated by rotation i->i+2 and reflection i->3-i.
    for refl in (0,1):
        for r in (0,2,4):
            per=tuple((r+(3-i if refl else i))%6 for i in range(6))
            br=tuple(sorted(per[i] for i in OD));p=per[0];shared=per[3]
            other=source_models(br,p,shared)
            C1,L1,ph1,be1,al1=raw_to_supported_cone(other)
            U=models['split_raw'];S=models['split_selected']
            for w in S[0]:
                transported=transport_source(alpha[w],OD,br,lambda i:per[i])
                rhs=apply(al1,transport_source(one(w),OD,br,lambda i:per[i]))
                check(transported==rhs,'new_six_source_inverse_transports')
            # Check the same exact supported-class classification, not just exterior dimensions.
            others=analyze_attachment_residues(other,al1)
            check(sum(z['supported_class_nonzero'] for z in others)==8,'new_six_transported_eight_residues')
            for labels in subsets(OD):
                if len(labels)<2:continue
                image_labels=tuple(sorted(per[i] for i in labels))
                mapped_labels=tuple(per[i] for i in labels)
                orient=pm(sum(mapped_labels[i]>mapped_labels[j] for i in range(len(labels)) for j in range(i+1,len(labels))))
                for eps in (0,1):
                    K0,j0,*_=source_to_cone_cartier_map(models,C,L,phi,labels,eps)
                    K1,j1,*_=source_to_cone_cartier_map(other,C1,L1,ph1,image_labels,eps)
                    for a,z in j0.items():
                        values=tuple(per[i] if i<6 else 6 for i in a)
                        sa=pm(sum(values[i]>values[j] for i in range(len(values)) for j in range(i+1,len(values))))
                        left={}
                        for ((arm,w),e),cc in z.items():
                            vv=transport_source({(w,e):cc},OD,br,lambda i:per[i])
                            left=add(left,{((arm,ww),ee):ccc for (ww,ee),ccc in vv.items()})
                        right=scale(j1[tuple(sorted(values))],orient*sa)
                        check(left==right,'new_all_eight_supported_maps_six_oriented_transports')
            transports+=1
    result={
      'status':'proved_supported_defect_and_central_native_extensions',
      'source_commit':COMMIT,'source_blobs':SOURCE_BLOBS,
      'formula':'beta = quotient composed with sigma_tau^{-1}; Phi:Cone(sigma)->Cone(U->U_tau)',
      'original_polynomial_source_unchanged':True,
      'independent_eta':'identity, with original labelled internal degree',
      'conductor_channels':records,'partial_selection_cube':cube,
      'complete_Gysin_channels':gysin,'free_A_linear_Gysin_lifts':free_lifts,
      'primitive_central_complete_supported_maps':8,
      'ordinary_primitive_raw_lifts_created':False,
      'central_faces':centers,'coupled_cap':cap,'transported_branch_pair_charts':transports,
      'nonzero_supported_higher_channels':sum(z['supported_class_nonzero'] for z in records),
      'primitive_first_conormal_channels_with_zero_supported_defect':sum(not z['supported_class_nonzero'] for z in records),
      'higher_annihilator':'(X0,...,X5, product(t_i for i in T))',
      'intersection_top_residue_control':'all fourteen channel images are boundaries; all eight nonzero union-support classes are lost',
      'specialization_control':'at a nonempty branch Rees face the selected-to-support map is zero; the full cone map retains shifted raw projection',
      'physical_collar_identification_constructed':False,'physical_reflection_parity_assigned':False,
      'checks':dict(sorted(COUNT.items())),'total_exact_assertions':sum(COUNT.values()),
      'verification_boundary':'Exact finite chain computations plus accompanying all-polynomial proofs; not proof-assistant verification.'}
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ('status','nonzero_supported_higher_channels','primitive_first_conormal_channels_with_zero_supported_defect','coupled_cap','free_A_linear_Gysin_lifts','partial_selection_cube','total_exact_assertions')},indent=2))

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path('marici_short_rees_supported_defect_certificate.json'))
    args=parser.parse_args();main(args.output)
