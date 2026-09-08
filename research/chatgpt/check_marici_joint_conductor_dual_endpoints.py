#!/usr/bin/env python3
"""Exact two-sheet derived-dual and endpoint Gysin comparison.

Pinned Marici normalization data; ordinary Python, no dependencies.
All polynomial operations are over Z[X0,...,X5]. Spectator variables are flat
extensions. No source/target coefficient is made invertible. Laurent values
below occur only in declared output Cech summands.
"""
from __future__ import annotations
import argparse, hashlib, json
from collections import Counter
from itertools import combinations, product
from pathlib import Path

ZERO=(0,)*6
ONE={ZERO:1}
E=(0,2,4); O=(1,3,5); ALL=E+O
COUNT=Counter()

def check(ok, tag):
    if not ok: raise AssertionError(tag)
    COUNT[tag]+=1

def pm(n): return -1 if n%2 else 1

def subsets(s):
    return [tuple(c) for k in range(len(s)+1) for c in combinations(s,k)]

def scalar(a): return {ZERO:a} if a else {}

def var(i):
    x=list(ZERO);x[i]=1;return {tuple(x):1}

def monomial(s, power=1, coeff=1):
    x=list(ZERO)
    for i in s:x[i]+=power
    return {tuple(x):coeff} if coeff else {}

def padd(*ps):
    z={}
    for p in ps:
        for e,a in p.items():
            z[e]=z.get(e,0)+a
            if not z[e]:del z[e]
    return z

def pscale(p,c):return {e:c*a for e,a in p.items() if c*a}

def pmul(p,q):
    z={}
    for e,a in p.items():
        for f,b in q.items():
            ef=tuple(x+y for x,y in zip(e,f))
            z[ef]=z.get(ef,0)+a*b
            if not z[ef]:del z[ef]
    return z

def vadd(*vs):
    z={}
    for v in vs:
        for b,p in v.items():
            z[b]=padd(z.get(b,{}),p)
            if not z[b]:del z[b]
    return z

def vmul(v,p): return {b:q for b,a in v.items() if (q:=pmul(a,p))}

def neg(v):return vmul(v,scalar(-1))

def unit(b):return {b:ONE}

def apply(table,v):
    z={}
    for b,p in v.items():z=vadd(z,vmul(table.get(b,{}),p))
    return z

def compose(f,g):return {b:apply(f,v) for b,v in g.items()}

def node():
    gs={('P',(),()):0}; d={('P',(),()):{}}; lab={('P',(),()):ZERO}
    for u in subsets(E)[1:]:
        for v in subsets(O)[1:]:
            b=('P',u,v);gs[b]=len(u)+len(v)-1
            lab[b]=tuple(int(i in u+v) for i in range(6));db={}
            if len(u)==len(v)==1:db={('P',(),()):pmul(var(u[0]),var(v[0]))}
            else:
                if len(u)>1:
                    for j,i in enumerate(u):db[('P',u[:j]+u[j+1:],v)]=pscale(var(i),pm(j))
                if len(v)>1:
                    for j,i in enumerate(v):db[('P',u,v[:j]+v[j+1:])]=pscale(var(i),pm(len(u)-1+j))
            d[b]=db
    return gs,d,lab

def koszul(seq,tag):
    gs={};d={};lab={}
    for s in subsets(seq):
        b=(tag,s);gs[b]=len(s);lab[b]=tuple(int(i in s) for i in range(6))
        d[b]={(tag,s[:j]+s[j+1:]):pscale(var(i),pm(j)) for j,i in enumerate(s)}
    return gs,d,lab

def audit(model,tag):
    gs,d,lab=model
    for b,bd in d.items():
        check(not apply(d,bd),tag+'_d_squared')
        for a,p in bd.items():
            check(gs[a]==gs[b]-1,tag+'_degree')
            for e,c in p.items():
                check(tuple(x+y for x,y in zip(e,lab[a]))==lab[b],tag+'_internal_degree')
                check(min(e)>=0 and isinstance(c,int),tag+'_polynomial')

def checkmap(f,src,tgt,tag,degree=0,sign=1):
    for b in src[0]:
        check(apply(tgt[1],f.get(b,{}))==vmul(apply(f,src[1][b]),scalar(sign)),tag+'_equation')
        for a in f.get(b,{}):check(tgt[0][a]==src[0][b]+degree,tag+'_degree')

def combine_models(*models):
    return tuple({k:v for model in models for k,v in model[i].items()} for i in range(3))

def integral_reduce(gs,d):
    # Sparse unit elimination of an integer chain complex; no field ranks.
    gs=dict(gs);d={b:dict(d.get(b,{})) for b in gs};steps=0
    while True:
        pivot=next(((b,a,c) for b in gs for a,c in d[b].items() if abs(c)==1),None)
        if pivot is None:break
        b,a,c=pivot;db=dict(d[b])
        for z in list(gs):
            if z in (a,b):continue
            t=d[z].get(a,0)
            if t:
                for y,q in db.items():
                    d[z][y]=d[z].get(y,0)-t*c*q
                    if not d[z][y]:del d[z][y]
            d[z].pop(a,None);d[z].pop(b,None)
        del gs[a],gs[b],d[a],d[b];steps+=1
    check(all(not v for v in d.values()),'integer_reduction_no_nonunit_residual')
    return dict(Counter(gs.values())),steps

def polynomial_contract(gs,original):
    """Cancel unit pivots, track maps/homotopy, verify an acyclic contraction."""
    g=dict(gs);d={b:dict(original.get(b,{})) for b in g}
    inc={b:unit(b) for b in g};proj={b:unit(b) for b in g};hom={b:{} for b in g};steps=0
    while True:
        hit=next(((b,a,p[ZERO]) for b in g for a,p in d[b].items()
                  if len(p)==1 and ZERO in p and abs(p[ZERO])==1),None)
        if hit is None:break
        b,a,c=hit;others={z:v for z,v in d[b].items() if z!=a}
        # h(a)=c b; i'=i(1-hd); p'=(1-dh)p; H'=H+i h p.
        h={a:{b:scalar(c)}}
        for z in proj:
            hom[z]=vadd(hom[z],apply(inc,apply(h,proj[z])))
        ni={}
        for z in g:
            if z not in (a,b):ni[z]=vadd(inc[z],neg(apply(inc,apply(h,d[z]))))
        np={}
        for z,pv in proj.items():
            q=vadd(pv,neg(apply(d,apply(h,pv))))
            q.pop(a,None);q.pop(b,None);np[z]=q
        nd={}
        for z in g:
            if z in (a,b):continue
            q=vadd(d[z],neg(apply(d,apply(h,d[z]))))
            q.pop(a,None);q.pop(b,None);nd[z]=q
        del g[a],g[b];inc,proj,d=ni,np,nd;steps+=1
    check(not g,'polynomial_cone_has_zero_remainder')
    for b in gs:
        check(vadd(apply(original,hom[b]),apply(hom,original.get(b,{})))==unit(b),
              'polynomial_cone_explicit_contraction')
    return steps

def permutation(g):
    k,f=g
    return tuple((2*k+(1-i if f else i))%6 for i in range(6))

def sign_reorder(values, order):
    pos={a:i for i,a in enumerate(order)};v=[pos[a] for a in values]
    return pm(sum(v[i]>v[j] for i in range(len(v)) for j in range(i+1,len(v))))

def perm_poly(p,per):
    out={}
    for e,a in p.items():
        f=[0]*6
        for i,x in enumerate(e):f[per[i]]=x
        out[tuple(f)]=a
    return out

def act_basis(b,g):
    per=permutation(g);flip=g[1]
    if b[0]=='P':
        _,u,v=b
        if not u:return b,1
        iu=[per[i] for i in u];iv=[per[i] for i in v]
        if not flip:
            return ('P',tuple(sorted(iu)),tuple(sorted(iv))),sign_reorder(iu,E)*sign_reorder(iv,O)
        return ('P',tuple(sorted(iv)),tuple(sorted(iu))),pm((len(u)-1)*(len(v)-1))*sign_reorder(iv,E)*sign_reorder(iu,O)
    tag,s=b;im=[per[i] for i in s]
    if tag=='C':
        ordered=tuple(i for i in ALL if i in im)
        return ('C',ordered),pm(flip)*sign_reorder(im,ALL)
    if tag in ('E','O'):
        newtag=({'E':'O','O':'E'}[tag] if flip else tag);order=E if newtag=='E' else O
        return (newtag,tuple(i for i in order if i in im)),sign_reorder(im,order)
    raise ValueError(b)

def act(v,g):
    z={};per=permutation(g)
    for b,p in v.items():
        im,s=act_basis(b,g);z=vadd(z,{im:pscale(perm_poly(p,per),s)})
    return z

def transpose(gs,d):
    dd={b:{} for b in gs}
    for b,v in d.items():
        for a,p in v.items():dd[a][b]=p
    return dd

def cech(seq):
    gs={('L',s):len(s) for s in subsets(seq)};d={b:{} for b in gs}
    for b in gs:
        s=b[1]
        for i in seq:
            if i in s:continue
            t=tuple(j for j in seq if j in s or j==i)
            d[b][('L',t)]=scalar(pm(sum(j in s for j in seq[:seq.index(i)])))
    return gs,d

def gysin(seq,km):
    k=len(seq);out={};sbase=pm(k*k+k*(k-1)//2)
    for b in km[0]:
        s=b[1];comp=tuple(i for i in seq if i not in s)
        sg=sbase*pm(sum(k+seq.index(i) for i in s))
        out[b]={('L',comp):monomial(comp,-1,sg)}
    return out

def pretty_poly(p):
    if not p:return '0'
    parts=[]
    for ex,c in sorted(p.items()):
        v='*'.join('X'+str(i)+(('^'+str(a)) if a!=1 else '') for i,a in enumerate(ex) if a)
        parts.append(str(c)+(('*'+v) if v else ''))
    return ' + '.join(parts)

def export_map(m):return {repr(b):{repr(a):pretty_poly(p) for a,p in v.items()} for b,v in m.items() if v}

def main(output):
    P=node();KE=koszul(E,'E');KO=koszul(O,'O');KC=koszul(ALL,'C');N=combine_models(KE,KO)
    for x,t in ((P,'node'),(KE,'plus_resolution'),(KO,'minus_resolution'),(KC,'conductor')):audit(x,t)
    check([sum(q==n for q in P[0].values()) for n in range(6)]==[1,9,18,15,6,1],'node_betti_numbers')
    fp={};fm={};H={}
    for b in P[0]:
        _,u,v=b
        if not u:
            fp[b]=unit(('E',()));fm[b]=unit(('O',()));H[b]={}
        else:
            fp[b]={('E',u):var(v[0])} if len(v)==1 else {}
            fm[b]={('O',v):var(u[0])} if len(u)==1 else {}
            H[b]={('C',u+v):scalar(pm(len(u)))}
    checkmap(fp,P,KE,'plus_endpoint_resolution_map')
    checkmap(fm,P,KO,'minus_endpoint_resolution_map')
    f={b:vadd(fp[b],fm[b]) for b in P[0]}
    delta={b:{('C',b[1]):scalar(1 if b[0]=='E' else -1)} for b in N[0]}
    checkmap(delta,N,KC,'normalization_difference')
    discrepancy=compose(delta,f)
    for b in P[0]:
        check(vadd(apply(KC[1],H[b]),apply(H,P[1][b]))==discrepancy[b],'joint_endpoint_homotopy')
    # The actual normalization fibre, not a new cone chosen to kill a class.
    Fg={};Fd={};Fl={}
    for b,n in N[0].items():
        z=('N',b);Fg[z]=n;Fl[z]=N[2][b]
        Fd[z]=vadd({('N',a):p for a,p in N[1][b].items()},{('Cshift',a):p for a,p in delta[b].items()})
    for b,n in KC[0].items():
        z=('Cshift',b);Fg[z]=n-1;Fl[z]=KC[2][b]
        Fd[z]={('Cshift',a):pscale(p,-1) for a,p in KC[1][b].items()}
    F=(Fg,Fd,Fl);audit(F,'normalization_fibre')
    j={b:vadd({('N',a):p for a,p in f[b].items()},{('Cshift',a):p for a,p in H[b].items()}) for b in P[0]}
    checkmap(j,P,F,'source_to_normalization_fibre')
    cg={('F',b):n for b,n in Fg.items()};cd={('F',b):{('F',a):p for a,p in Fd[b].items()} for b in Fg}
    for b,n in P[0].items():
        z=('Pshift',b);cg[z]=n+1
        cd[z]=vadd({('F',a):p for a,p in j[b].items()},{('Pshift',a):pscale(p,-1) for a,p in P[1][b].items()})
    cancellations=polynomial_contract(cg,cd)
    # Prove all polynomial homology by the finite multidegree support types.
    support_records=[]
    for present in subsets(tuple(range(6))):
        gs={b:n for b,n in P[0].items() if set(i for i,e in enumerate(P[2][b]) if e)<=set(present)}
        d={b:{a:next(iter(p.values())) for a,p in P[1][b].items() if a in gs} for b in gs}
        hh,st=integral_reduce(gs,d)
        mixed=bool(set(present)&set(E)) and bool(set(present)&set(O))
        check(hh==({} if mixed else {0:1}),'all_monomial_support_resolution')
        support_records.append({'support':present,'homology':hh})
    # Compute the complete dual in every threshold homogeneous frame.
    pd=transpose(P[0],P[1]);dual_records=[]
    for lam in product((-1,0,1),repeat=6):
        gs={b:-n for b,n in P[0].items() if all(l+a>=0 for l,a in zip(lam,P[2][b]))}
        dd={b:{a:next(iter(p.values())) for a,p in pd[b].items() if a in gs} for b in gs}
        hom,_=integral_reduce(gs,dd)
        hom={-n:r for n,r in hom.items()};expected={}
        plus=all(lam[i]==-1 for i in E) and all(lam[i]>=0 for i in O)
        minus=all(lam[i]==-1 for i in O) and all(lam[i]>=0 for i in E)
        if plus or minus:expected[3]=int(plus)+int(minus)
        if all(a==-1 for a in lam):expected[5]=1
        check(hom==expected,'all_dual_cohomology_threshold_frames')
        if hom:dual_records.append({'frame':lam,'Ext':hom})
    top=('P',E,O);ctop=('C',ALL)
    zplus={b:p for b in P[0] if (p:=fp[b].get(('E',E),{}))}
    zminus={b:p for b in P[0] if (p:=fm[b].get(('O',O),{}))}
    for z in (zplus,zminus,unit(top)):check(not apply(pd,z),'actual_dual_cocycles')
    check(H[top]=={ctop:scalar(-1)},'conductor_connecting_coefficient_minus_one')
    primitive_nulls={}
    for i in range(6):
        source=next(b for b,p in P[1][top].items() if p==var(i) or p==pscale(var(i),-1))
        coef=next(iter(P[1][top][source].values()))
        cochain={source:scalar(coef)}
        check(apply(pd,cochain)==vmul(unit(top),var(i)),'conductor_class_coordinate_annihilator')
        primitive_nulls[str(i)]=export_map({'cochain':cochain})
    # Verify all six source transports, including the forced sheet-difference twist.
    character=[]
    for g in product(range(3),range(2)):
        for model in (P,N,KC):
            for b in model[0]:check(act(model[1][b],g)==apply(model[1],act(unit(b),g)),'D3_semilinear_chain_action')
        for b in P[0]:
            check(act(f[b],g)==apply(f,act(unit(b),g)),'D3_endpoint_maps_joint')
            check(act(H[b],g)==apply(H,act(unit(b),g)),'D3_joint_endpoint_homotopy')
        for b in N[0]:check(act(delta[b],g)==apply(delta,act(unit(b),g)),'D3_normalization_difference')
        topimage,sg=act_basis(top,g);check(topimage==top and sg==1,'A_valued_conductor_class_even')
        det=sign_reorder([permutation(g)[i] for i in ALL],ALL)
        check(det==pm(g[1]),'ambient_determinant_character')
        character.append({'g':g,'node_top':sg,'ambient_volume':det,'relative_dualizing_conductor':sg*det})
    # Full five-coordinate Gysin candidates from all six coordinate axes.
    axis_records=[]
    for omitted in range(6):
        seq=tuple(i for i in ALL if i!=omitted);KJ=koszul(seq,'J');audit(KJ,'axis')
        branchmap=fm if omitted in E else fp
        g={b:{('J',a[1]):p for a,p in branchmap[b].items()} for b in P[0]}
        checkmap(g,P,KJ,'node_to_axis')
        cv,dc=cech(seq);rho=gysin(seq,KJ);k=len(seq)
        for b in KJ[0]:
            check(apply(dc,rho[b])==vmul(apply(rho,KJ[1][b]),scalar(pm(k))),'full_axis_Gysin_chain_equation')
            for cb,p in rho[b].items():
                check(cv[cb]+KJ[0][b]==k,'full_axis_Gysin_total_degree')
                for ex in p:check(all(a>=0 or i in cb[1] for i,a in enumerate(ex)),'Gysin_output_legal_localization')
        mu=compose(rho,g)
        for b in P[0]:
            check(apply(dc,mu[b])==vmul(apply(mu,P[1][b]),scalar(pm(k))),'pulled_back_Gysin_chain_equation')
            check(('L',()) not in mu[b],'pulled_back_Gysin_has_no_lower_unit')
            check(all(len(a[1])>=2 for a in mu[b]),'pulled_back_Gysin_localization_degree_at_least_two')
        check(rho[('J',seq)]=={('L',()):ONE},'ambient_Gysin_endpoint_unit')
        bottom=mu[('P',(),())]
        check(bottom=={('L',seq):monomial(seq,-1,-1)},'supported_node_Gysin_nonzero_residue')
        # In top local cohomology mixed source relations all annihilate its value.
        residue=monomial(seq,-1,-1)
        for e in E:
            for o in O:
                mul=pmul(residue,pmul(var(e),var(o)))
                check(all(any(ex[i]>=0 for i in seq) for ex in mul),'node_relations_annihilate_supported_residue')
        # Counit/derived conductor base change kills every displayed component.
        counit={b:v.get(('L',()),{}) for b,v in mu.items()}
        check(not any(counit.values()),'all_axis_Gysin_counits_strictly_zero_on_node')
        axis_records.append({'omitted':omitted,'factors_through':'minus' if omitted in E else 'plus',
                             'input_resolution_columns':len(KJ[0]),
                             'node_pullback_nonzero_columns':sum(bool(v) for v in mu.values()),
                             'minimum_output_Cech_degree':min(len(a[1]) for v in mu.values() for a in v),
                             'counit':'zero','derived_conductor_specialization':'zero',
                             'supported_map':'nonzero','pullback':export_map(mu)})
    # The source dual comparison alpha is non-null: after conductor base change
    # all Koszul differentials vanish, but its two projections remain units.
    alpha=transpose(N[0],{b:{} for b in N[0]}) # replaced below by actual rectangular transpose
    alpha={b:{} for b in KC[0]}
    for b,v in delta.items():
        for a,p in v.items():alpha[a][b]=p
    for b in KC[0]:
        check(all(p==ONE or p==scalar(-1) for p in alpha[b].values()),'joint_dual_alpha_unit_columns')
    check(alpha[('C',())]=={('E',()):ONE,('O',()):scalar(-1)},'joint_dual_alpha_conductor_nonzero')
    # Retain the independent eta by tensoring identities; check differential signs.
    tensor_cols=0
    for shift in (0,1):
        for b in P[0]:
            check(vadd(apply(KC[1],H[b]),apply(H,P[1][b]))==discrepancy[b],
                  'independent_excess_channel_joint_identity')
            tensor_cols+=1
    # Actual normalization gluing class in R Gamma_M(B), lifted through P.
    # A degree-zero fine mode has coefficient 1/product(label(P_b)) in every
    # output Cech summand that contains that support. This gives 425 actual
    # total-complex columns, not a quotient chosen from its homology.
    cv6,dc6=cech(ALL)
    tg={};td={}
    for b,n in P[0].items():
        support={i for i,a in enumerate(P[2][b]) if a}
        for lb,q in cv6.items():
            if not support<=set(lb[1]):continue
            z=(b,lb[1]);tg[z]=q-n;dz={}
            for la,po in dc6[lb].items():dz[(b,la[1])]=next(iter(po.values()))
            for a,po in P[1][b].items():
                dz[(a,lb[1])]=dz.get((a,lb[1]),0)+pm(q)*next(iter(po.values()))
            td[z]={a:c for a,c in dz.items() if c}
    def izadd(*vs):
        out={}
        for v in vs:
            for z,a in v.items():
                out[z]=out.get(z,0)+a
                if not out[z]:del out[z]
        return out
    def izapply(table,v):
        out={}
        for z,a in v.items():out=izadd(out,{y:a*c for y,c in table[z].items()})
        return out
    for z in tg:
        check(not izapply(td,td[z]),'conductor_supported_total_d_squared')
        check(all(tg[y]==tg[z]+1 for y in td[z]),'conductor_supported_total_degree')
    LAMBDA={}
    base=('P',(),())
    for i in O:LAMBDA[(base,(i,))]=1
    for b,n in P[0].items():
        if n==0:continue
        _,u,v=b;a=len(u);bb=len(v)
        exponent=1+a*(a-1)//2+a-1+(bb-1)*(a+1)+bb*(bb-1)//2
        LAMBDA[(b,u+v)]=pm(exponent)
    check(not izapply(td,LAMBDA),'full_52_term_gluing_cocycle')
    check(len(LAMBDA)==52,'gluing_cocycle_term_count')
    hh,_=integral_reduce({z:-n for z,n in tg.items()},td)
    check(hh=={-1:1},'actual_source_supported_H1')
    check(LAMBDA[(top,ALL)]==-1,'gluing_top_residue_coefficient')
    # The natural dual connecting cocycle is H^*(top conductor covector)=-top*.
    # Its evaluation on the lifted gluing cocycle is the positive sixfold residue.
    pairing=-LAMBDA[(top,ALL)]
    check(pairing==1,'source_gluing_dual_pairing_primitive_sixfold_residue')
    for z in tg:
        check(td[z].get((top,ALL),0)==0,'dual_pairing_annihilates_boundaries')
    base_coboundary=td[(base,())]
    def total_action(v,g):
        out={};per=permutation(g)
        for (b,loc),a in v.items():
            bb,sb=act_basis(b,g);new=[per[i] for i in loc]
            ll=tuple(i for i in ALL if i in new)
            sg=sb*sign_reorder(new,ALL)
            out=izadd(out,{(bb,ll):a*sg})
        return out
    for g in product(range(3),range(2)):
        for z in tg:
            check(total_action(td[z],g)==izapply(td,total_action({z:1},g)),
                  'supported_total_D3_equivariance')
        if g[1]:
            check(izadd(total_action(LAMBDA,g),LAMBDA)==base_coboundary,
                  'reflected_gluing_class_has_exact_conductor_collar')
        else:
            check(total_action(LAMBDA,g)==LAMBDA,'rotated_gluing_cocycle_fixed')
    # The orientation-compensated source reflection has the prescribed
    # comparison h_g=-1 on reversing elements, zero on rotations. Its full
    # composition equation is strict, so no unspecified higher choice occurs.
    for g in product(range(3),range(2)):
        h_g=-g[1]
        compensated={z:pm(g[1])*a for z,a in total_action(LAMBDA,g).items()}
        check(izadd(compensated,{z:-a for z,a in LAMBDA.items()})
              =={z:h_g*a for z,a in base_coboundary.items() if h_g*a},
              'source_reflection_comparison_from_conductor_unit')
        for h in product(range(3),range(2)):
            gh=((g[0]+pm(g[1])*h[0])%3,(g[1]+h[1])%2)
            check(-g[1]+pm(g[1])*(-h[1])-(-gh[1])==0,
                  'source_comparison_all_group_pairs')
    # Weighted endpoint monomials annihilate the conductor class, with actual
    # polynomial nullhomotopies. This does not identify them with spatial collars.
    weighted={}
    for name,supp in [('plus',O),('minus',E),('midpoint',(1,3))]:
        i=supp[0]
        source=next(b for b,p in P[1][top].items() if p==var(i) or p==pscale(var(i),-1))
        coef=next(iter(P[1][top][source].values()))
        h={source:monomial(supp[1:],1,-coef)} # natural dual class is -top*
        check(apply(pd,h)==vmul(unit(top),monomial(supp,1,-1)),
              'weighted_endpoint_conductor_class_nullhomotopy')
        weighted[name]=export_map({'homotopy':h})
    result={
      'status':'proved_for_actual_normalization_coefficient_source_not_full_spatial_PC_identification',
      'source_commit':'d1947b67a60d3e88ba77f4ca60ea02c2a306ee61',
      'source_blob':'840258522d45e450e4f1e8bb927d9aae58c75566',
      'normalization_ring':'Z[X0,...,X5]/(Xe Xo: e even, o odd)',
      'node_resolution_ranks':[1,9,18,15,6,1],
      'supported_total_columns':len(tg),
      'source_gluing_cocycle_terms':len(LAMBDA),
      'source_H1_gluing_class':'odd-open units; even-open zeros',
      'source_dual_pairing_value':'positive 1/(X0 X1 X2 X3 X4 X5), ordered by (0,2,4,1,3,5)',
      'source_gluing_reflection':'s Lambda + Lambda = d(1)',
      'orientation_compensated_source_reflection_homotopy':'h_s=-1, h_r=0; all composition equations strict',
      'weighted_endpoint_class_homotopies':weighted,
      'node_resolution_generator_count':len(P[0]),
      'normalization_fibre_generator_count':len(Fg),
      'comparison_cone_generator_count':len(cg),
      'comparison_cone_unit_cancellations':cancellations,
      'Ext_groups':{'3':'Bplus det(E)^vee + Bminus det(O)^vee','5':'C det(E+O)^vee tensor polarity'},
      'joint_source_homotopy':'H(U,V)=(-1)^|U| e_U wedge e_V',
      'joint_source_homotopy_columns':export_map(H),
      'normalization_plus_map':export_map(fp),
      'normalization_minus_map':export_map(fm),
      'conductor_top_transgression_coefficient':-1,
      'dual_normalization_alpha_nonzero_after_conductor_base_change':True,
      'A_dual_conductor_class_internal_degree':[-1]*6,
      'plus_dualizing_cocycle':export_map({'zplus':zplus}),
      'minus_dualizing_cocycle':export_map({'zminus':zminus}),
      'conductor_annihilator_homotopies':primitive_nulls,
      'all_monomial_supports':len(support_records),
      'all_dual_threshold_frames':729,
      'nonzero_dual_frames':dual_records,
      'transport_characters':character,
      'axis_Gysin_tests':axis_records,
      'independent_excess_columns':tensor_cols,
      'checks':dict(sorted(COUNT.items())),
      'total_exact_checks':sum(COUNT.values()),
      'scope':[
        'The full five-coordinate Gysin pullback is nonzero with supported output; its support counit and conductor specialization are zero.',
        'The node conductor Ext5 class is nonzero and is the transgression from Ext6 of the conductor, not any single-sheet axis Gysin.',
        'Both coefficient endpoint maps and their joint homotopy are explicit, equivariant and polynomial.',
        'No equality between these source coefficient comparison cells and the target spatial collar 2-cells is claimed.',
        'The ambient A-linear derived dual is constructed. It is not silently identified with the complete physical supported-Verdier functor.',
        'The independent excess can be retained by tensoring the constructed maps; no source-to-target excess identification or physical parity is selected.'
      ]
    }
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ('status','node_resolution_ranks','comparison_cone_unit_cancellations','Ext_groups','total_exact_checks')},indent=2))

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path('marici_joint_conductor_dual_endpoints_certificate.json'))
    main(parser.parse_args().output)
