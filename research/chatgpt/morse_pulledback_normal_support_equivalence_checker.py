#!/usr/bin/env python3
"""Full pulled-back-normal Morse/support comparison for the D03 blowdown.

Standard library only; no network, external artifact, or placeholder checks.
Reconstructs the 1169-state barycentric coefficient source and its separate
occurrence factor, the 255-state pulled-back-normal cellular subdivision,
and the 215-state original PC target.  All identities are over the independent
polynomial occurrence/normal ring; the graph-normalization base change is
checked separately.  Only +/-1 pivots are inverted.

Writes morse_pulledback_normal_support_equivalence_certificate.json.
Usage: python morse_pulledback_normal_support_equivalence_checker.py --output DIR
"""
from __future__ import annotations
import argparse
from collections import Counter, defaultdict
from hashlib import sha256
from itertools import combinations
import json
from pathlib import Path

N = 6
DIAGONALS = tuple((a, b) for a in range(N) for b in range(a + 1, N)
                  if b-a != 1 and (a,b) != (0,5))
DI = {d:i for i,d in enumerate(DIAGONALS)}
SHORT = tuple(i for i,d in enumerate(DIAGONALS) if (d[1]-d[0])%3 != 0)
LONG = tuple(i for i in range(9) if i not in SHORT)
PLUS = frozenset(DI[d] for d in ((1,3),(1,5),(3,5)))
MINUS = frozenset(DI[d] for d in ((0,2),(0,4),(2,4)))
AD = DI[(0,3)]; X1 = DI[(1,3)]; X3 = DI[(3,5)]; X5 = DI[(1,5)]; X0 = DI[(0,2)]
EXCEPTIONAL = 9
VARIABLES = (tuple('X%02d' % (10*a+b) for a,b in DIAGONALS)
             + tuple('u%02d' % (10*a+b) for a,b in DIAGONALS))
NV = len(VARIABLES)
ZERO_EXP = (0,)*NV
Poly = dict[tuple[int,...],int]
Vector = dict[int,Poly]
ONE: Poly = {ZERO_EXP:1}
TESTS = Counter()

def check(condition: bool, label: str) -> None:
    TESTS[label] += 1
    if not condition:
        raise AssertionError(label)

def p_add(p:Poly,q:Poly,sign:int=1)->Poly:
    ans=dict(p)
    for mon,c in q.items():
        ans[mon]=ans.get(mon,0)+sign*c
        if not ans[mon]: del ans[mon]
    return ans

def p_scale(p:Poly,c:int)->Poly:
    return {m:c*v for m,v in p.items() if c*v}

def p_mul(p:Poly,q:Poly,quotient:bool=True)->Poly:
    ans={}
    for m,c in p.items():
        for n,e in q.items():
            v=tuple(a+b for a,b in zip(m,n))
            if quotient and any(v[i] for i in PLUS) and any(v[i] for i in MINUS):
                continue
            ans[v]=ans.get(v,0)+c*e
            if not ans[v]:del ans[v]
    return ans

def p_reduce(p:Poly)->Poly:
    return {m:c for m,c in p.items()
            if not (any(m[i] for i in PLUS) and any(m[i] for i in MINUS))}

def p_eps(p:Poly)->Poly:
    return {m:c for m,c in p.items() if all(m[i]==0 for i in SHORT)}

def p_var(index:int)->Poly:
    exp=list(ZERO_EXP);exp[index]=1
    return {tuple(exp):1}

def occurrence(indices)->Poly:
    exp=list(ZERO_EXP)
    for i in indices:exp[i]+=1
    return {tuple(exp):1}

def normal(i:int)->Poly:
    return p_var(9+i)

def v_add(v:Vector,w:Vector,sign:int=1)->Vector:
    ans={i:dict(p) for i,p in v.items()}
    for i,p in w.items():
        ans[i]=p_add(ans.get(i,{}),p,sign)
        if not ans[i]:del ans[i]
    return ans

def v_scale(v:Vector,p:Poly,quotient:bool=True)->Vector:
    return {i:a for i,c in v.items() if (a:=p_mul(c,p,quotient))}

def apply(columns:list[Vector],v:Vector,quotient:bool=True)->Vector:
    ans={}
    for i,p in v.items():
        ans=v_add(ans,v_scale(columns[i],p,quotient))
    return ans

def crosses(d,e)->bool:
    if set(d)&set(e):return False
    def inside(v,a,b): return 0<(v-a)%N<(b-a)%N
    return (inside(e[0],*d)!=inside(e[1],*d)
            and inside(d[0],*e)!=inside(d[1],*e))

def old(face:frozenset[int])->frozenset[int]:
    return frozenset((face-{EXCEPTIONAL})|{AD,X1}) if EXCEPTIONAL in face else face

def reconstruct():
    faces=set()
    for k in range(4):
        for c in combinations(range(9),k):
            if all(not crosses(DIAGONALS[a],DIAGONALS[b]) for a,b in combinations(c,2)):
                faces.add(frozenset(c))
    expanded=set()
    for face in faces:
        if {AD,X1}<=face:
            for retained in (set(),{AD},{X1}):
                expanded.add(frozenset((face-{AD,X1})|{EXCEPTIONAL}|retained))
        else: expanded.add(face)
    expanded=tuple(sorted(expanded,key=lambda f:(len(f),tuple(sorted(f)))))
    flags=[]
    def extend(flag):
        flags.append(flag)
        for larger in expanded:
            if flag[-1]<larger:extend(flag+(larger,))
    for f in expanded:extend((f,))
    bare=[]
    for flag in flags:
        for k in range(len(old(flag[0]))+1):
            for H in combinations(sorted(old(flag[0])),k):bare.append((flag,H))
    states=[(flag,H,k) for flag,H in bare for k in (0,1)]
    def degree(state):return len(state[0])-1+len(state[1])+state[2]
    states.sort(key=lambda st:(degree(st),tuple(tuple(sorted(f)) for f in st[0]),st[1],st[2]))
    positions={st:i for i,st in enumerate(states)}
    ds=[]
    for flag,H,occ in states:
        col={}; base=len(flag)-1
        if len(flag)>=2:
            for j in range(len(flag)):
                ff=flag[:j]+flag[j+1:]
                poly=occurrence(old(flag[1])-old(flag[0])) if j==0 else ONE
                target=positions[(ff,H,occ)]
                col=v_add(col,{target:p_scale(poly,(-1)**j)})
        for j,h in enumerate(H):
            target=positions[(flag,H[:j]+H[j+1:],occ)]
            col=v_add(col,{target:p_scale(normal(h),(-1)**(base+j))})
        if occ:
            target=positions[(flag,H,0)]
            col=v_add(col,{target:p_scale(p_var(X3),(-1)**(base+len(H)))})
        ds.append(col)
    return expanded,flags,bare,states,positions,ds,degree


def add(v:Vector,w:Vector,sign:int=1)->Vector:
    return v_add(v,w,sign)

def scale(v:Vector,p:Poly)->Vector:
    return v_scale(v,p,quotient=False)

def act(columns,v:Vector)->Vector:
    ans={}
    for i,p in v.items():ans=add(ans,scale(columns[i],p))
    return ans

def unit_reduce(differential:dict[int,Vector],allowed):
    """Exact algebraic chain contraction by elementary +/-1 cancellations.

    Returns reduced d, inclusion i, projection p, degree +1 homotopy h,
    and the replayable list (target,source,unit) of cancelled pairs.
    Convention: d h + h d = id - i p.
    """
    original=sorted(differential)
    D={i:dict(col) for i,col in differential.items()}
    I={i:{i:ONE} for i in original}
    P={i:{i:ONE} for i in original}
    H={i:{} for i in original}
    active=set(original);pivots=[]
    while True:
        pivot=None
        for b in sorted(active,reverse=True):
            for a,p in sorted(D[b].items()):
                if allowed(a,b) and p in (ONE,p_scale(ONE,-1)):
                    pivot=(a,b,p[ZERO_EXP]);break
            if pivot:break
        if pivot is None:break
        a,b,u=pivot;pivots.append(pivot)
        v={j:p for j,p in D[b].items() if j!=a}
        affected={j:D[j][a] for j in active-{b} if a in D[j]}
        for k in original:
            if a in P[k]:H[k]=add(H[k],scale(I[b],p_scale(P[k][a],u)))
        for j,c in affected.items():
            if j!=a:I[j]=add(I[j],scale(I[b],p_scale(c,u)),-1)
        for k in original:
            ca=P[k].get(a,{})
            P[k]={j:p for j,p in P[k].items() if j not in(a,b)}
            if ca:P[k]=add(P[k],scale(v,p_scale(ca,-u)))
        for j in active-{a,b}:
            col={k:p for k,p in D[j].items() if k not in(a,b)}
            if j in affected:col=add(col,scale(v,p_scale(affected[j],u)),-1)
            D[j]=col
        del D[a],D[b],I[a],I[b]
        active-={a,b}
    return D,I,P,H,pivots

def verify_retract(Dbig,Dsmall,I,P,H,label):
    for j in Dsmall:
        check(act(Dbig,I[j])==act(I,Dsmall[j]),label+'_inclusion_chain')
        check(act(P,I[j])=={j:ONE},label+'_projection_inclusion')
    for j in Dbig:
        check(act(Dsmall,P[j])==act(P,Dbig[j]),label+'_projection_chain')
        check(add(act(Dbig,H[j]),act(H,Dbig[j]))==
              add({j:ONE},act(I,P[j]),-1),label+'_homotopy')

def face_name(f):
    return ['E' if i==EXCEPTIONAL else '%d%d'%DIAGONALS[i] for i in sorted(f)]

def state_name(st):
    flag,H,k=st
    return {'flag':[face_name(f) for f in flag],
            'normal_circles':face_name(H),
            'occurrence_factor':'h_occ35' if k else 'p_occ35'}

def cell_name(cell,occ=None):
    F,H=cell
    ans={'face':face_name(F),'normal_circles':face_name(H)}
    if occ is not None:ans['occurrence_factor']='h_occ35' if occ else 'p_occ35'
    return ans

def poly_json(p):
    return [{'coefficient':c,'powers':{VARIABLES[i]:e for i,e in enumerate(m) if e}}
            for m,c in sorted(p.items())]

def vector_json(v):
    return [{'target':i,'coefficient':poly_json(p)} for i,p in sorted(v.items())]

def columns_json(cols):
    return [{'source':j,'entries':vector_json(v)} for j,v in sorted(cols.items()) if v]

def chain_ranks(indices,degrees):
    count=Counter(degrees[i] for i in indices)
    return [count[i] for i in range(max(count,default=-1)+1)]

def graph_normalize(p:Poly)->Poly:
    """u_short -> t_short X_short, then kill all mixed-sheet products.

    The exponent slot u_i becomes the named t_i slot for a short i.
    No monodromy or occurrence coordinate is inverted.
    """
    ans={}
    for mon,c in p.items():
        new=list(mon)
        for i in SHORT:new[i]+=mon[9+i]
        if any(new[i] for i in PLUS) and any(new[i] for i in MINUS):continue
        key=tuple(new);ans[key]=ans.get(key,0)+c
        if not ans[key]:del ans[key]
    return ans

def specialize_vector(v):return {i:q for i,p in v.items() if (q:=graph_normalize(p))}

def specialize_columns(cols):return {i:specialize_vector(v)for i,v in cols.items()}

def normalized_act(cols,v):
    # In this ring p_mul's existing mixed-sheet reduction is exactly the relation.
    ans={}
    for i,p in v.items():ans=add(ans,v_scale(cols[i],p,quotient=True))
    return ans

def main(output:Path):
    TESTS.clear()
    expanded,flags,bare,S,pos,ds,degree=reconstruct()
    DS={i:col for i,col in enumerate(ds)}
    degS={i:degree(st)for i,st in enumerate(S)}
    bare_ids=[i for i,st in enumerate(S)if st[2]==0]
    DB={i:DS[i]for i in bare_ids}
    check(len(S)==2338 and len(bare_ids)==1169,'source_counts')
    for j,col in DS.items():
        check(not act(DS,col),'source_universal_square_zero')
        check(all(degS[i]==degS[j]-1 for i in col),'source_differential_degree')
    initial_group=lambda i:(S[i][0][0],S[i][1])
    Dred,Ired,Pred,Hred,pivots=unit_reduce(DB,
        lambda a,b:initial_group(a)==initial_group(b))
    check(len(pivots)==457 and len(Dred)==255,'cellular_reduction_counts')
    verify_retract(DB,Dred,Ired,Pred,Hred,'bar_to_cell')

    # Match the reduced cellular orientations to the prescribed ray-incidence
    # convention; the top, unmarked orientation is fixed to +1.
    cells={i:(S[i][0][0],S[i][1])for i in Dred}
    cp={cell:i for i,cell in cells.items()}
    check(len(cp)==len(cells),'one_cell_per_initial_face_normal_subset')
    DP={}
    for i,(F,HH)in cells.items():
        col={}
        for G in expanded:
            if F<G and len(G)==len(F)+1:
                a=next(iter(G-F));sgn=(-1)**sum(h<a for h in F)
                col=add(col,{cp[(G,HH)]:p_scale(occurrence(old(G)-old(F)),sgn)})
        for k,a in enumerate(HH):
            col=add(col,{cp[(F,HH[:k]+HH[k+1:])]:
                         p_scale(normal(a),(-1)**(3-len(F)+k))})
        DP[i]=col
        check(set(col)==set(Dred[i]),'cellular_differential_support')
        check(degS[i]==3-len(F)+len(HH),'cellular_degree')
    adj=defaultdict(list)
    for i in DP:
        for j,p in Dred[i].items():
            ratio=1 if p==DP[i][j] else -1
            check(p==p_scale(DP[i][j],ratio),'cellular_orientation_ratio')
            adj[i].append((j,ratio));adj[j].append((i,ratio))
    signs={};components=0
    for seed in sorted(DP,key=lambda i:(len(cells[i][0]),cells[i][1],i)):
        if seed in signs:continue
        components+=1;signs[seed]=1;stack=[seed]
        while stack:
            i=stack.pop()
            for j,r in adj[i]:
                val=signs[i]*r
                if j in signs:check(signs[j]==val,'orientation_cycle_consistency')
                else:signs[j]=val;stack.append(j)
    check(components==1,'cellular_orientation_connected')
    P={j:{i:p_scale(p,signs[i]) for i,p in col.items()}for j,col in Pred.items()}
    I={j:scale(Ired[j],p_scale(ONE,signs[j]))for j in DP}
    verify_retract(DB,DP,I,P,Hred,'oriented_bar_to_cell')

    # Native normals would be subsets of F.  This source instead retains
    # subsets of old(F), as specified by the actual pulled-back Morse model.
    oldfaces=sorted({old(F)for F in expanded},key=lambda F:(len(F),tuple(sorted(F))))
    oldcells=[]
    for F in oldfaces:
        for k in range(len(F)+1):
            oldcells.extend((F,hh)for hh in combinations(sorted(F),k))
    op={cell:j for j,cell in enumerate(oldcells)}
    DC={}
    for j,(F,HH)in enumerate(oldcells):
        col={}
        for G in oldfaces:
            if F<G and len(G)==len(F)+1:
                a=next(iter(G-F));sgn=(-1)**sum(h<a for h in F)
                col=add(col,{op[(G,HH)]:p_scale(p_var(a),sgn)})
        for k,a in enumerate(HH):
            col=add(col,{op[(F,HH[:k]+HH[k+1:])]:
                         p_scale(normal(a),(-1)**(3-len(F)+k))})
        DC[j]=col
    K={}
    for i,(F,HH)in cells.items():
        G=old(F)
        if len(G)!=len(F):K[i]={};continue
        seq=sorted(F)
        if EXCEPTIONAL in F:
            missing=next(iter({AD,X1}-F))
            seq=[missing if a==EXCEPTIONAL else a for a in seq]
        sgn=(-1)**sum(seq[a]>seq[b]for a in range(len(seq))for b in range(a+1,len(seq)))
        K[i]={op[(G,HH)]:p_scale(ONE,sgn)}
    for i in DP:
        check(act(DC,K[i])==act(K,DP[i]),'pulledback_blowdown_chain')
    check(len(DC)==215,'old_cell_count')

    # A degreewise split kernel of the pulled-back blowdown, retaining all 40
    # generators.  Its contractibility is computed, not inferred from a rank.
    preimages=defaultdict(list)
    for i,col in K.items():
        for j,p in col.items():preimages[j].append((i,p[ZERO_EXP]))
    check(len(preimages)==215,'blowdown_surjective_all_rows')
    chosen={j:sorted(preimages[j])[0]for j in DC}
    chosen_ids={i for i,s in chosen.values()}
    kernel_ids=sorted(set(DP)-chosen_ids)
    section={j:{i:p_scale(ONE,s)}for j,(i,s)in chosen.items()}
    inc={i:add({i:ONE},act(section,K[i]),-1)for i in kernel_ids}
    proj={i:({i:ONE}if i in kernel_ids else {})for i in DP}
    DN={i:act(proj,act(DP,inc[i]))for i in kernel_ids}
    attachment={j:act(proj,act(DP,section[j]))for j in DC}
    empty,_,_,hn,kernel_pivots=unit_reduce(DN,lambda a,b:True)
    check(not empty and len(kernel_pivots)==20,'blowdown_kernel_contractible')
    for i in DN:
        check(add(act(DN,hn[i]),act(hn,DN[i]))=={i:ONE},'kernel_contraction')
    jK={j:add(section[j],act(inc,act(hn,attachment[j])),-1)for j in DC}
    hK={i:act(inc,act(hn,proj[i]))for i in DP}
    verify_retract(DP,DC,jK,K,hK,'cellular_blowdown')
    R={i:act(K,P[i])for i in bare_ids}
    U={j:act(I,jK[j])for j in DC}
    G={i:add(Hred[i],act(I,act(hK,P[i])))for i in bare_ids}
    verify_retract(DB,DC,U,R,G,'complete_bare_equivalence')

    # Tensor the *entire* comparison and both homotopies with K_occ(X35).
    TC=[(j,k)for j in DC for k in (0,1)]
    tp={p:i for i,p in enumerate(TC)}
    degT={tp[(j,k)]:3-len(oldcells[j][0])+len(oldcells[j][1])+k for j,k in TC}
    DT={}
    for j,k in TC:
        col={tp[(i,k)]:p for i,p in DC[j].items()}
        if k:
            col=add(col,{tp[(j,0)]:p_scale(p_var(X3),
                (-1)**(3-len(oldcells[j][0])+len(oldcells[j][1])))})
        DT[tp[(j,k)]]=col
    Rt={};Ut={};Gt={}
    for i,st in enumerate(S):
        ib=pos[(st[0],st[1],0)];k=st[2]
        Rt[i]={tp[(j,k)]:p for j,p in R[ib].items()}
        Gt[i]={pos[(S[j][0],S[j][1],k)]:p for j,p in G[ib].items()}
    for j,k in TC:
        Ut[tp[(j,k)]]={pos[(S[i][0],S[i][1],k)]:p for i,p in U[j].items()}
    verify_retract(DS,DT,Ut,Rt,Gt,'complete_corrected_equivalence')
    for i,col in DT.items():check(not act(DT,col),'target_square_zero')

    # Keep both endpoint packets, the entire short-boundary packet, and the
    # complementary relative quotient.  A flag's initial face determines its
    # coefficient support; classifying by its terminal vertex is not a quotient.
    short=set(SHORT)
    Vsrc={i for i,st in enumerate(S)if old(st[0][0])in(PLUS,MINUS)}
    Bsrc={i for i,st in enumerate(S)if old(st[0][0])&short}
    Qsrc=set(DS)-Bsrc
    Vt={i for i,(j,k)in enumerate(TC)if oldcells[j][0]in(PLUS,MINUS)}
    Bt={i for i,(j,k)in enumerate(TC)if oldcells[j][0]&short}
    Qt=set(DT)-Bt
    for A,label in [(Vsrc,'source_endpoint'),(Bsrc,'source_short')]:
        for j in A:check(set(DS[j])<=A,label+'_subcomplex')
    for A,label in [(Vt,'target_endpoint'),(Bt,'target_short')]:
        for j in A:check(set(DT[j])<=A,label+'_subcomplex')
    for A,B,label in [(Vsrc,Vt,'endpoint'),(Bsrc,Bt,'short')]:
        for j in A:
            check(set(Rt[j])<=B,'projection_'+label+'_support')
            check(set(Gt[j])<=A,'homotopy_'+label+'_support')
        for j in B:check(set(Ut[j])<=A,'inclusion_'+label+'_support')
    for j in Vsrc:
        check(not Gt[j],'endpoint_homotopy_zero')
        flag,hh,k=S[j];F=old(flag[0]);sgn=1 if F==PLUS else -1
        check(Rt[j]=={tp[(op[(F,hh)],k)]:p_scale(ONE,sgn)},
              'endpoint_orientation_frame_all_normals')
    # Every comparison and homotopy is homogeneous in the independent
    # occurrence/normal grading; graph substitution gives the retained Rees
    # grading deg(t_i)=deg(u_i)-deg(X_i).
    def source_weight(st):
        flag,hh,k=st;w=[0]*18
        for a in old(flag[0]):w[a]-=1
        for a in hh:w[9+a]+=1
        w[X3]+=k
        return tuple(w)
    def target_weight(j):
        cell_id,k=TC[j];F,hh=oldcells[cell_id];w=[0]*18
        for a in F:w[a]-=1
        for a in hh:w[9+a]+=1
        w[X3]+=k
        return tuple(w)
    sw={j:source_weight(st)for j,st in enumerate(S)}
    tw={j:target_weight(j)for j in DT}
    for cols,fromw,tow,label in [(DS,sw,sw,'source'),(DT,tw,tw,'target'),
                                (Rt,sw,tw,'comparison'),(Ut,tw,sw,'inverse'),
                                (Gt,sw,sw,'homotopy')]:
        for j,col in cols.items():
            for i,poly in col.items():
                for mon in poly:
                    check(tuple(a+b for a,b in zip(mon,tow[i]))==fromw[j],
                          label+'_internal_grading')
    check((len(Vsrc),len(Bsrc),len(Qsrc))==(32,1552,786),'source_support_counts')
    check((len(Vt),len(Bt),len(Qt))==(32,416,14),'target_support_counts')
    QD={j:{i:p for i,p in DS[j].items()if i in Qsrc}for j in Qsrc}
    qD={j:{i:p for i,p in DT[j].items()if i in Qt}for j in Qt}
    qR={j:{i:p for i,p in Rt[j].items()if i in Qt}for j in Qsrc}
    qU={j:{i:p for i,p in Ut[j].items()if i in Qsrc}for j in Qt}
    qG={j:{i:p for i,p in Gt[j].items()if i in Qsrc}for j in Qsrc}
    verify_retract(QD,qD,qU,qR,qG,'full_support_quotient')
    check(chain_ranks(Qt,degT)==[0,0,3,7,4],'corrected_Q_degrees')

    # Thin generic subposet is a subcomplex, but projection onto it is not a
    # chain map: mixed flags have generic terms in their boundaries.
    thin={i for i,st in enumerate(S)if not(old(st[0][-1])&short)}
    defects={j:{i:p for i,p in DS[j].items()if i in thin}
             for j in set(DS)-thin}
    defects={j:c for j,c in defects.items()if c}
    check(len(thin)==20,'thin_generic_counts')
    top=frozenset();D03=frozenset({AD});corner=frozenset({AD,X0,X3})
    tri=pos[((top,D03,corner),(),0)]
    edge=pos[((top,D03),(),0)]
    check(defects[tri]=={edge:ONE},'omitted_mixed_triangle_unit_defect')
    check(bool(DS[edge]),'generic_edge_not_a_cycle')

    # Named Morse chains are independently assembled from the supplied flags.
    ec=frozenset({X1,X3});er=frozenset({AD,X3})
    b1=frozenset({EXCEPTIONAL,X1,X3});he=frozenset({EXCEPTIONAL,X3})
    bd=frozenset({EXCEPTIONAL,AD,X3})
    def single(flag,coef=ONE,sgn=1,k=0):
        return {pos[(tuple(flag),(),k)]:p_scale(coef,sgn)}
    hm={}
    for apex,ed,left,right,coef in [(top,ec,PLUS,b1,ONE),(top,he,b1,bd,ONE),
                                  (D03,er,bd,corner,p_var(AD))]:
        hm=add(hm,single((apex,ed,right),coef,-1))
        hm=add(hm,single((apex,ed,left),coef))
    hm=add(hm,single((top,D03,bd)))
    xi={}
    for ed,left,right,coef in [(ec,PLUS,b1,p_var(X1)),
                              (he,b1,bd,occurrence((AD,X1))),
                              (er,bd,corner,p_var(AD))]:
        xi=add(xi,single((ed,right),coef));xi=add(xi,single((ed,left),coef,-1))
    qj=add(add(single((top,PLUS),ONE,-1),single((top,D03))),
           single((D03,corner),p_var(AD)))
    check(act(DS,hm)==add(qj,scale(xi,p_var(X3)),-1),'morse_identity')
    def occ_lift(v):return {pos[(S[i][0],S[i][1],1)]:p for i,p in v.items()}
    dxi=act(DS,xi)
    hhat=add(hm,occ_lift(xi),-1);qhat=add(qj,occ_lift(dxi),-1)
    check(act(DS,hhat)==qhat,'corrected_morse_identity')
    check(not act(DS,qhat),'corrected_roof_closed')
    Gamma={tp[(op[(frozenset({AD,X3}),())],0)]:p_var(AD),
           tp[(op[(frozenset({X1,X3}),())],0)]:p_var(X1)}
    check(not act(Rt,hm),'cellular_morse_thimble_image_zero')
    check(act(Rt,xi)==Gamma,'cellular_gallery_image')
    check(act(Rt,qj)==scale(Gamma,p_var(X3)),'cellular_raw_roof_image')
    for v,label in [(hm,'thimble'),(xi,'gallery'),(qj,'roof'),(hhat,'corrected_thimble'),(qhat,'corrected_roof')]:
        check(not {i:p for i,p in act(Rt,v).items()if i in Qt},'Q_image_'+label+'_zero')
    check(not Rt[edge],'pure_generic_edge_image_zero')
    # A second Q-nullhomotopy comes from the explicit deformation retract.
    pq=lambda v:{i:p for i,p in v.items()if i in Qsrc}
    Hq=act(qG,pq(qj));higher=act(qG,pq(hm))
    check(act(QD,Hq)==pq(qj),'retraction_Q_filler')
    check(add(pq(hm),Hq,-1)==act(QD,higher),'Morse_vs_retraction_higher_comparison')

    # The genuine finite Q complex and its universal closed top generator.
    longlist=list(LONG);qtop=tp[(op[(top,())],0)]
    ps=[tp[(op[(frozenset({l}),())],0)]for l in longlist]
    hs=[tp[(op[(frozenset({l}),(l,))],0)]for l in longlist]
    theta={qtop:ONE}
    prod=ONE
    for l in longlist:prod=p_mul(prod,normal(l),quotient=False)
    theta={qtop:prod}
    for l,h0 in zip(longlist,hs):
        coef=p_scale(p_var(l),-1)
        for other in longlist:
            if other!=l:coef=p_mul(coef,normal(other),quotient=False)
        theta=add(theta,{h0:coef})
    check(not act(qD,theta),'true_Q_top_cycle')
    check(act(qR,act(qU,theta))==theta,'true_Q_top_cycle_preserved')
    qfacet_representatives={face_name({l})[0]:qU[p]for l,p in zip(longlist,ps)}
    for l,p in zip(longlist,ps):
        check(not act(QD,qU[p]),'true_Q_facet_relative_cycle')
        check(len(qU[p])==8,'true_Q_facet_eight_triangles')
    # Nonvanishing control on the actual quotient: set every occurrence and
    # normal variable to zero.  All monodromy units 1+u_i remain equal to one.
    # The coordinate p03 cannot occur in any specialized boundary.
    def q_test(p):
        total=0
        for mon,c0 in p.items():
            if any(mon):continue
            total+=c0
        return total
    p03=ps[longlist.index(AD)]
    for j in qD:check(q_test(qD[j].get(p03,{}))==0,'Q_facet_nonboundary_detector')
    check(q_test(ONE)==1,'Q_facet_detector_unit')

    # Recheck full comparison after the graph and alternating-sheet pullback.
    GS=specialize_columns(DS);GT=specialize_columns(DT)
    GR=specialize_columns(Rt);GU=specialize_columns(Ut);GG=specialize_columns(Gt)
    for j in GS:
        check(normalized_act(GT,GR[j])==normalized_act(GR,GS[j]),'normalization_graph_chain')
        check(add(normalized_act(GS,GG[j]),normalized_act(GG,GS[j]))==
              add({j:ONE},normalized_act(GU,GR[j]),-1),'normalization_graph_homotopy')
    for j in GT:
        check(normalized_act(GR,GU[j])=={j:ONE},'normalization_graph_inverse')

    # Store enough information to inspect every row and replay every identity.
    source_basis=[state_name(st)for st in S]
    target_basis=[cell_name(oldcells[j],k)for j,k in TC]
    payload={'source_basis':source_basis,'target_basis':target_basis,
             'source_differential':columns_json(DS),'target_differential':columns_json(DT),
             'comparison_R':columns_json(Rt),'inverse_U':columns_json(Ut),
             'source_homotopy_G':columns_json(Gt),
             'Q_source_indices':sorted(Qsrc),'Q_target_indices':sorted(Qt),
             'source_short_indices':sorted(Bsrc),'target_short_indices':sorted(Bt),
             'source_endpoint_indices':sorted(Vsrc),'target_endpoint_indices':sorted(Vt),
             'cellular_reduction_pivots':pivots,'kernel_reduction_pivots':kernel_pivots,
             'pulledback_cellular_basis':{str(i):cell_name(c)for i,c in sorted(cells.items())},
             'pulledback_cellular_differential':columns_json(DP),
             'pulledback_blowdown':columns_json(K),
             'pulledback_kernel_differential':columns_json(DN),
             'pulledback_kernel_homotopy':columns_json(hn),
             'true_Q_facet_representatives':{name:vector_json(v)for name,v in qfacet_representatives.items()},
             'true_Q_top_cycle':vector_json(theta),
             'morse_thimble':vector_json(hm),'morse_roof':vector_json(qj),
             'morse_gallery':vector_json(xi),'corrected_morse_thimble':vector_json(hhat),
             'corrected_morse_roof':vector_json(qhat),
             'cellular_gallery_image':vector_json(Gamma),
             'Q_retraction_filler':vector_json(Hq),'Q_filler_comparison_primitive':vector_json(higher)}
    digest=sha256(json.dumps(payload,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    result={
        'schema':'marici.morse_pulledback_normal_support_equivalence.v1',
        'source_commit':'d1947b67a60d3e88ba77f4ca60ea02c2a306ee61',
        'source_paths':['research/voevodsky/check_d03_pabs_morse_pullback.rs',
                        'research/voevodsky/check_d03_normalized_blowdown_counit.py',
                        'research/voevodsky/check_global_k6_koszul_cech_promotion.rs',
                        'src/ledger/20260817-397 The Descended qJ Roof Is the Canonical D03 Yoneda Generator.md'],
        'coefficient_ring':{'universal_variables':VARIABLES,'source_localizations':[],
                            'graph_pullback':'u_short -> t_short X_short; long normals remain independent',
                            'normalization_relations':'all mixed positive/negative short occurrence products vanish',
                            'nonflat_base_change':'chain-homotopy identities remain valid after tensoring'},
        'counts':{'expanded_faces':len(expanded),'strict_flags':len(flags),
                  'bare_source':len(bare_ids),'corrected_source':len(S),
                  'pulledback_normal_cellular':len(DP),'native_normal_cellular_distinct_model':245,
                  'finite_target':len(DC),'corrected_target':len(DT),
                  'bar_unit_cancellations':len(pivots),'blowdown_kernel_states':len(DN),
                  'blowdown_kernel_unit_cancellations':len(kernel_pivots),
                  'source_ranks':chain_ranks(DS,degS),'target_ranks':chain_ranks(DT,degT),
                  'source_support_ranks':{'endpoints':chain_ranks(Vsrc,degS),'short_boundary':chain_ranks(Bsrc,degS),'Q':chain_ranks(Qsrc,degS)},
                  'target_support_ranks':{'endpoints':chain_ranks(Vt,degT),'short_boundary':chain_ranks(Bt,degT),'Q':chain_ranks(Qt,degT)},
                  'comparison_nonzero_columns':sum(bool(v)for v in Rt.values()),
                  'comparison_nonzero_entries':sum(len(v)for v in Rt.values()),
                  'inverse_nonzero_entries':sum(len(v)for v in Ut.values()),
                  'homotopy_nonzero_entries':sum(len(v)for v in Gt.values()),
                  'thin_projection_nonzero_defect_columns':len(defects),
                  'thin_projection_nonzero_defect_entries':sum(len(v)for v in defects.values())},
        'comparison_identities':['d R = R d','d U = U d','R U = id','d G + G d = id - U R'],
        'support':{'endpoints_and_short_boundary_preserved':True,'homotopy_on_endpoints':0,
                   'Q_subquotient_chain_homotopy_equivalence':True,
                   'endpoint_orientation_signs':{'positive':1,'negative':-1},
                   'physical_ray_to_sheet_swap_identified':False},
        'Q':{'bare_minimal_degrees':{'2':3,'3':4},'corrected_minimal_degrees':{'2':3,'3':7,'4':4},
             'bare_differential':'[X03 X14 X25 | diag(u03,u14,u25)]',
             'corrected_d3':'[M | X35 I3]', 'corrected_d4':'[-X35 I4; M]',
             'H1':0,'isolated_top_D03_flag_is_cycle':False,
             'thin_generic_projection_is_chain_map':False,
             'corrected_Morse_Q_image':0,
             'nonzero_facet_class_retained':True},
        'scope':{'ordinary_pulledback_normal_comparison_constructed':True,
                 'native_245_state_exceptional_kernel_killed_by_this_theorem':False,
                 'physical_extraordinary_conductor_comparison_constructed':False,
                 'physical_Delta_J_determined':False,
                 'all_claimed_homotopies_physical_frame_admissible':False,
                 'change_of_coefficient_frame_inferred_from_unit_signatures':False},
        'checks':dict(TESTS),'total_checks':sum(TESTS.values()),
        'matrix_sha256':digest,'matrices':payload}
    output.mkdir(parents=True,exist_ok=True)
    path=output/'morse_pulledback_normal_support_equivalence_certificate.json'
    path.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:result[k]for k in('counts','matrix_sha256','total_checks','scope')},indent=2))
    print('certificate:',path)

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path(__file__).resolve().parent)
    args=parser.parse_args()
    main(args.output)
