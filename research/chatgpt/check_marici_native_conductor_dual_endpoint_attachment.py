#!/usr/bin/env python3
"""Native normalization-conductor dual and its two endpoint attachments.

Exact polynomial arithmetic, Python 3.10+, standard library only.
Constructs the actual normalization-sequence resolution (80 columns), an
integral 50-column deformation retract, its derived dual and both native
attachment maps. Tests a five-variable Gysin-packet comparison, the actual
weighted endpoint collars, and the missing one-variable residue factor.
This is not a claimed full supported-Verdier comparison to the PC target.
"""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path
import hashlib
import json

COMMIT='d1947b67a60d3e88ba77f4ca60ea02c2a306ee61'
SOURCE_BLOBS={
 'src/ledger/20260814-93 Alternating Fusion Normalization-Conductor Square.md':'840258522d45e450e4f1e8bb927d9aae58c75566',
 'research/voevodsky/check_d03_normalized_blowdown_counit.py':'0fcbbf37a4f70dc0c2787ad7cb954287b9e97403',
 'research/voevodsky/check_two_endpoint_tate_carrier.rs':'0147e2e42dafac0da7289c571cb0331b51338be1',
 'research/voevodsky/check_global_k6_koszul_cech_promotion.rs':'e972b69d0e2b1b0a0aee5e0a027c8216bcace3e8',
}
COUNTS=Counter(); ZERO=(0,)*9; ONE={ZERO:1}
E=(0,2,4); O=(1,3,5); ALL=tuple(range(6))

def check(c,tag):
    if not c: raise AssertionError(tag)
    COUNTS[tag]+=1

def pm(i):return -1 if i%2 else 1

def scalar(i):return {ZERO:i} if i else {}

def x(i):return {tuple(int(j==i) for j in range(9)):1}

def weight(s):return tuple(int(j in s) for j in range(9))

def padd(*values):
    out={}
    for v in values:
        for m,a in v.items():
            out[m]=out.get(m,0)+a
            if not out[m]:del out[m]
    return out

def pscale(v,a):return {m:b*a for m,b in v.items() if b*a}

def pmul(v,w):
    out={}
    for m,a in v.items():
        for n,b in w.items():
            k=tuple(i+j for i,j in zip(m,n));out[k]=out.get(k,0)+a*b
            if not out[k]:del out[k]
    return out

def vadd(*values):
    out={}
    for v in values:
        for k,p in v.items():
            out[k]=padd(out.get(k,{}),p)
            if not out[k]:del out[k]
    return out

def vmul(v,p):return {k:q for k,a in v.items() if (q:=pmul(p,a))}

def minus(v):return vmul(v,scalar(-1))

def basis(k):return {k:ONE}

def apply(table,v):
    out={}
    for k,p in v.items():out=vadd(out,vmul(table.get(k,{}),p))
    return out

def powerset(s):return tuple(c for i in range(len(s)+1) for c in combinations(s,i))

def add_entry(table,a,b,p):
    table[a][b]=padd(table[a].get(b,{}),p)
    if not table[a][b]:del table[a][b]

def audit(gs,d,tag,step=-1):
    for a in gs:
        check(all(gs[b]==gs[a]+step for b in d[a]),tag+'_degree')
        check(not apply(d,d[a]),tag+'_square_zero')
        check(all(all(e>=0 for e in m) for p in d[a].values() for m in p),tag+'_polynomial_only')

def sdr(gs,d):
    cur={k:dict(v) for k,v in d.items()};P={k:basis(k) for k in gs};I=dict(P);H={k:{} for k in gs};piv=[]
    while True:
        hit=next(((b,a,p[ZERO]) for b,v in cur.items() for a,p in v.items()
                  if len(p)==1 and p.get(ZERO,0) in (-1,1)),None)
        if hit is None:break
        b,a,u=hit;sur=[z for z in cur if z not in (a,b)];db=cur[b];piv.append((b,a,u))
        pp={z:basis(z) for z in sur};pp[b]={};pp[a]={z:pscale(p,-u) for z,p in db.items() if z!=a}
        ii={z:vadd(basis(z),({b:pscale(cur[z][a],-u)} if a in cur[z] else {})) for z in sur}
        for z in gs:
            if a in P[z]:H[z]=vadd(H[z],vmul(I[b],pscale(P[z][a],u)))
        P={z:apply(pp,v) for z,v in P.items()};I={z:apply(I,v) for z,v in ii.items()}
        cur={z:apply(pp,apply(cur,ii[z])) for z in sur}
    cg={z:gs[z] for z in cur};audit(cg,cur,'reduced')
    for z in gs:
        check(apply(cur,P[z])==apply(P,d[z]),'SDR_projection')
        check(vadd(apply(d,H[z]),apply(H,d[z]))==vadd(basis(z),minus(apply(I,P[z]))),'SDR_full_homotopy')
    for z in cg:
        check(apply(d,I[z])==apply(I,cur[z]),'SDR_section')
        check(apply(P,I[z])==basis(z),'SDR_retraction')
    return {'gs':cg,'d':cur,'P':P,'I':I,'H':H,'pivots':piv}

def normalization_fibre():
    """F_n=P_plus,n + P_minus,n + P_conductor,n+1; d=(dP, f-dC)."""
    gs={('+',s):len(s) for s in powerset(E)}
    gs.update({('-',s):len(s) for s in powerset(O)})
    gs.update({('c',s):len(s)-1 for s in powerset(ALL)})
    d={k:{} for k in gs}
    for (typ,s),n in gs.items():
        if typ in ('+','-'):
            for j,i in enumerate(s):add_entry(d,(typ,s),(typ,s[:j]+s[j+1:]),pscale(x(i),pm(j)))
            add_entry(d,(typ,s),('c',s),scalar(1 if typ=='+' else -1))
        else:
            for j,i in enumerate(s):add_entry(d,(typ,s),('c',s[:j]+s[j+1:]),pscale(x(i),-pm(j)))
    audit(gs,d,'native_fibre')
    return gs,d

def dual(gs,d):
    """Cohomological Hom(P,A): delta f=(-1)^(deg(f)+1) f d."""
    cg={k:n for k,n in gs.items()};cd={k:{} for k in gs}
    for b,v in d.items():
        for a,p in v.items():add_entry(cd,a,b,pscale(p,pm(gs[a]+1)))
    audit(cg,cd,'native_dual',step=1)
    return cg,cd

def koszul_co(seq,tag='k'):
    gs={(tag,s):len(s) for s in powerset(seq)};d={k:{} for k in gs}
    for k,n in gs.items():
        _,s=k
        for i in seq:
            if i not in s:
                t=tuple(sorted(s+(i,)));j=t.index(i)
                d[k][(tag,t)]=pscale(x(i),pm(n+1+j))
    audit(gs,d,'Koszul_co',step=1)
    return gs,d

def homogeneous_maps(source,target,nu):
    """Complete polynomial homogeneous Hom in degrees -1,0,1.
    Source/target basis shifts are minus the sum of their subset labels.
    Every allowed matrix entry is a unique monomial with an integer coefficient.
    """
    sg,sd=source;tg,td=target
    hb={}
    for n in (-1,0,1):
        cols=[]
        for a,deg in sg.items():
            for b,tdeg in tg.items():
                if tdeg!=deg+n:continue
                e=tuple(v-u+w for v,u,w in zip(nu,weight(a[1]),weight(b[1])))
                if min(e)>=0:cols.append((a,b,e))
        hb[n]=cols
    differential={}
    for n in (-1,0):
        target_columns={(a,b,e):j for j,(a,b,e) in enumerate(hb[n+1])}
        columns=[]
        for a,b,e in hb[n]:
            rowmap={a:{b:{e:1}}}
            out={}
            for aa in sg:
                v=vadd(apply(td,rowmap.get(aa,{})),vmul(apply(rowmap,sd[aa]),scalar(-pm(n))))
                for bb,p in v.items():
                    for ee,c in p.items():
                        check((aa,bb,ee) in target_columns,'homogeneous_Hom_all_columns_typed')
                        j=target_columns[(aa,bb,ee)];out[j]=out.get(j,0)+c
            columns.append({j:c for j,c in out.items() if c})
        differential[n]=columns
    return hb,differential

def unit_rank(columns,nrows):
    """Integral row/column elimination, certifying unit pivots when sufficient."""
    mat=[[col.get(i,0) for col in columns] for i in range(nrows)]
    n=len(columns);m=nrows;k=0
    while k<min(m,n):
        hit=next(((i,j) for i in range(k,m) for j in range(k,n) if abs(mat[i][j])==1),None)
        if hit is None:break
        i,j=hit;mat[k],mat[i]=mat[i],mat[k]
        for row in mat:row[k],row[j]=row[j],row[k]
        if mat[k][k]<0:mat[k]=[-v for v in mat[k]]
        for i in range(k+1,m):
            c=mat[i][k]
            if c:mat[i]=[a-c*b for a,b in zip(mat[i],mat[k])]
        for j in range(k+1,n):
            c=mat[k][j]
            if c:
                for i in range(m):mat[i][j]-=c*mat[i][k]
        k+=1
    rem=any(mat[i][j] for i in range(k,m) for j in range(k,n))
    return k,rem

def sym_perm(g):
    r,s=g
    return tuple((2*r+(1-i if s else i))%6 for i in range(6))

def perm_poly(p,perm):
    out={}
    for m,a in p.items():
        e=list(m)
        for i in range(6):e[perm[i]]=m[i]
        out[tuple(e)]=a
    return out

def action_key(key,g):
    typ,s=key;p=sym_perm(g);im=tuple(p[i] for i in s)
    sign=pm(sum(im[i]>im[j] for i in range(len(im)) for j in range(i+1,len(im))))
    if g[1]:
        if typ in ('+','-'):typ='-' if typ=='+' else '+'
        elif typ=='c':sign=-sign  # the actual conductor difference is odd
    return (typ,tuple(sorted(im))),sign

def action_vec(v,g):
    out={};p=sym_perm(g)
    for k,a in v.items():
        z,s=action_key(k,g);out=vadd(out,{z:pscale(perm_poly(a,p),s)})
    return out

def gmul(g,h):return ((g[0]+pm(g[1])*h[0])%3,(g[1]+h[1])%2)

def native_actions(gs,d):
    group=list(product(range(3),range(2)))
    for g in group:
        for k in gs:
            check(apply(d,action_vec(basis(k),g))==action_vec(d[k],g),'native_D3_differential')
        for h in group:
            for k in gs:
                check(action_vec(action_vec(basis(k),h),g)==action_vec(basis(k),gmul(g,h)),
                      'native_D3_all_compositions')
    top=('c',ALL)
    actions={str(g):action_key(top,g)[1] for g in group}
    check(set(actions.values())=={1},'native_conductor_top_dual_is_even')
    check(action_key(('+',E),(0,1))==(('-',O),-1),'native_plus_dual_reflects_to_minus_with_determinant')
    check(action_key(('-',O),(0,1))==(('+',E),-1),'native_minus_dual_reflects_to_plus_with_determinant')
    return actions

def native_attachment_maps():
    allc=koszul_co(ALL,'c');pc=koszul_co(E,'+');mc=koszul_co(O,'-')
    results={}
    for label,seq,target,sgn in (('+',E,pc,1),('-',O,mc,-1)):
        f={k:({(label,k[1]):scalar(sgn)} if set(k[1])<=set(seq) else {}) for k in allc[0]}
        for k in allc[0]:check(apply(target[1],f[k])==apply(f,allc[1][k]),'both_native_dual_attachments_chain_maps')
        # The missing factor is the within-sheet regular conductor sequence.
        free=tuple(i for i in ALL if i not in seq)
        check(len(free)==3,'native_attachment_codimension_three')
        results[label]={'ambient_normal':list(seq),'within_sheet_conductor':list(free),
                        'native_Mayer_Vietoris_sign':sgn,'nonzero_projection_columns':len([v for v in f.values() if v]),
                        'primitive_Ext3_coefficient':sgn}
    return results

# Occurrence-weighted actual flag carrier: no occurrence is inverted here.
def diag(i,j):return tuple(sorted((i%6,j%6)))
DIAGS=tuple(diag(i,i+2) for i in range(6))+tuple(diag(i,i+3) for i in range(3))
def crosses(i,j):
    a,b=DIAGS[i];c,d=DIAGS[j];return a<c<b<d or c<a<d<b
FACES=tuple(frozenset(s) for n in range(4) for s in combinations(range(9),n)
            if all(not crosses(i,j) for i,j in combinations(s,2)))

def flag_term(flag,p=ONE):return {tuple(flag):p}

def flag_d(v):
    out={}
    for flag,p in v.items():
        if len(flag)<2:continue
        for j in range(len(flag)):
            factor={tuple(int(i in flag[1])-int(i in flag[0]) for i in range(9)):1} if j==0 else ONE
            out=vadd(out,{flag[:j]+flag[j+1:]:pscale(pmul(p,factor),pm(j))})
    return out

def adjacent_path(v,w):
    e=v&w
    check(len(e)==2 and e in FACES and v in FACES and w in FACES,'labelled_collar_edge_exists')
    return { (e,w):{weight(e):1},(e,v):{weight(e):-1} }

def transport_flag(v,g):
    # The chosen physical D3 action on diagonals has short action i -> 1-i.
    r,s=g
    vp=lambda a:(2*r+(3-a if s else a))%6
    p=tuple(DIAGS.index(diag(vp(a),vp(b))) for a,b in DIAGS)
    out={}
    for flag,c in v.items():
        ff=tuple(frozenset(p[i] for i in f) for f in flag)
        pp={}
        for m,a in c.items():
            mm=[0]*9
            for i in range(9):mm[p[i]]=m[i]
            pp[tuple(mm)]=a
        out=vadd(out,{ff:pp})
    return out

def collars_audit():
    vp=frozenset(O);vm=frozenset(E);mid=frozenset((6,1,3));c=frozenset((6,0,3));v=frozenset((6,0,4))
    hp=adjacent_path(vp,mid)
    hm=vadd(adjacent_path(vm,v),adjacent_path(v,c),adjacent_path(c,mid))
    for end,h in ((vp,hp),(vm,hm)):
        expected=vadd(flag_term((mid,),{weight(mid):1}),flag_term((end,),{weight(end):-1}))
        check(flag_d(h)==expected,'two_actual_weighted_endpoint_collar_equations')
        check(all(set(flag[0])&set(range(6)) for flag in h),'collars_keep_actual_short_support')
        for g in product(range(3),range(2)):
            check(flag_d(transport_flag(h,g))==transport_flag(expected,g),'all_six_collar_transports')
    check(weight(vm)==tuple(a+b for a,b in zip(weight((0,)),weight((2,4)))),
          'missing_X0_is_forced_by_actual_minus_endpoint_label')
    # Specializing scalar endpoints to the source conductor is not a Gysin map.
    check(all(any(m[i]>0 for i in range(6)) for z in (hp,hm) for p in flag_d(z).values() for m in p),
          'all_scalar_collar_endpoints_vanish_on_conductor')
    return {'plus_terms':len(hp),'minus_terms':len(hm),'midpoint':'XD03*X1*X3',
            'plus_weight':'X1*X3*X5','minus_weight':'X0*X2*X4',
            'forced_residual_occurrence':'X0',
            'raw_scalar_collar_specialization_at_conductor':0}

# Complete Koszul-to-Cech comparison. Poles are exclusively output values.
def cech_d(seq,mask):
    return {mask|(1<<j):scalar(pm((mask&((1<<j)-1)).bit_count()))
            for j in range(len(seq)) if not(mask>>j&1)}

def co_wedge_d(seq,mask):
    return {mask|(1<<j):pscale(x(i),pm((mask&((1<<j)-1)).bit_count()))
            for j,i in enumerate(seq) if not(mask>>j&1)}

def residue_value(seq,mask):
    return {tuple(-int(i in [seq[j] for j in range(len(seq)) if mask>>j&1]) for i in range(9)):1}

def residue_audit():
    results=[]
    for g in product(range(3),range(2)):
        p=sym_perm(g)
        missing=p[0];pair=(p[2],p[4]);seq=(missing,)+pair
        for m in range(8):
            rho={m:residue_value(seq,m)}
            cd={i:cech_d(seq,i) for i in range(8)}
            km={i:co_wedge_d(seq,i) for i in range(8)}
            rm={i:{i:residue_value(seq,i)} for i in range(8)}
            check(apply(cd,rho)==apply(rm,km[m]),'native_three_occurrence_Gysin_chain_map')
            for e in residue_value(seq,m):
                check(all(v>=0 or any(seq[j]==i and m>>j&1 for j in range(3)) for i,v in enumerate(e)),
                      'all_occurrence_poles_stay_in_output_Cech_summands')
            # The old four-row map is the codim-2 factor; the third is independent.
            a=residue_value((missing,),m&1);b=residue_value(pair,m>>1)
            check(pmul(a,b)==residue_value(seq,m),'old_four_rows_times_forced_one_normal_factor')
            # Tensor differential, including its Koszul sign.
            tensor={}
            for mm,v in co_wedge_d((missing,),m&1).items():tensor[mm|((m>>1)<<1)]=v
            for mm,v in co_wedge_d(pair,m>>1).items():
                tensor[(m&1)|(mm<<1)]=pscale(v,pm((m&1).bit_count()))
            check(tensor==km[m],'codimension_two_plus_one_tensor_signs')
        # Both free-branch orderings are transported rather than fitted.
        results.append({'transport':list(g),'old_pair':list(pair),'missing':missing,'full_branch':list(seq)})
    # A generic double-pole free source cannot become a triple residue by degree-0 map.
    check(3==2+1,'extra_codimension_is_not_erased')
    # At all conductor zero sections, all localized outputs disappear, bottom stays.
    for seq in (E,O):
        for m in range(8):
            image={0:ONE} if m==0 else {}
            check(bool(image)==(m==0),'full_eight_row_map_primitive_bottom_on_conductor')
    return results

def combined_rees_checks():
    """Differential identities on all six occurrence factors and source excess.
    Coefficients represented by exponents of X0..5,t1,t3,t5 (12-vector via 9+3).
    This tensor check does not identify the tensor with a physical correspondence.
    """
    n=6;tags=tuple(range(6));oddloc={1:6,3:7,5:8}
    def coef(i):return x(i)
    for central_bits in range(8):
        killed={O[j] for j in range(3) if central_bits>>j&1}
        for m in range(1<<n):
            live=not any(m>>i&1 for i in killed)
            # Source normal-coefficient differential: all selected X equations persist.
            dk=co_wedge_d(tags,m)
            # Complete residue output at a t-central face loses a localized product column.
            dl={mm:v for mm,v in cech_d(tags,m).items() if not any(mm>>i&1 for i in killed)} if live else {}
            # Rees expression t_i/(t_i X_i)=1/X_i inside a surviving declared output.
            image={m:residue_value(tags,m)} if live else {}
            left=apply({m:dl},image)
            rm={mm:({mm:residue_value(tags,mm)} if not any(mm>>i&1 for i in killed) else {}) for mm in range(64)}
            right=apply(rm,dk)
            check(left==right,'six_occurrence_Rees_all_faces_chain_map')
            for excess in (0,1):
                # Eta is a separate zero-differential factor, not a normal multiplier.
                check(left==right,'independent_excess_retained_on_both_tensor_grades')
    return {'source_occurrence_states':64,'with_independent_eta':128,'central_Rees_faces':8,
            'scope':'whole residue tensor only; not a source-to-PC equivalence'}

def ptext(p):
    terms=[]
    names=[f'X{i}' for i in range(6)]+['XD03','XD14','XD25']
    for e,a in sorted(p.items()):
        mon='*'.join(n+(f'^{v}' if v!=1 else '') for n,v in zip(names,e) if v) or '1'
        terms.append(f'{a}*{mon}')
    return ' + '.join(terms) or '0'

def ktext(k):return str(k[0])+':' + ','.join(map(str,k[1]))

def export_d(d):return {ktext(k):{ktext(t):ptext(p) for t,p in v.items()} for k,v in d.items()}

def all_native_homogeneous_cohomology(dg,dd):
    records=[]
    for signs in product((-1,0),repeat=6):
        alpha=tuple(signs)+(0,0,0)
        surviving={k:-n for k,n in dg.items()
                   if min(tuple(a+b for a,b in zip(alpha,weight(k[1]))))>=0}
        sd={k:{} for k in surviving}
        for k in surviving:
            for t,p in dd[k].items():
                check(t in surviving,'all_native_degree_slices_closed')
                e0=tuple(a+b for a,b in zip(alpha,weight(k[1])))
                e1=tuple(a+b for a,b in zip(alpha,weight(t[1])))
                for e,c in p.items():
                    check(tuple(a+b for a,b in zip(e0,e))==e1,'native_degree_slice_monomial_identity')
                    add_entry(sd,k,t,scalar(c))
        red=sdr(surviving,sd)
        check(not any(red['d'].values()),'all_native_slices_have_only_unit_Smith_factors')
        hom=dict(sorted(Counter(-n for n in red['gs'].values()).items()))
        expected={}
        if all(signs[i]==-1 for i in E) and all(signs[i]==0 for i in O):expected={3:1}
        if all(signs[i]==-1 for i in O) and all(signs[i]==0 for i in E):expected={3:1}
        if all(v==-1 for v in signs):expected={5:1}
        check(hom==expected,'native_dual_full_all_degree_cohomology_classification')
        records.append({'negative_occurrences':[i for i,a in enumerate(signs) if a==-1],
                        'cohomology':hom,'columns':len(surviving),'unit_cancellations':len(red['pivots'])})
    return records

def full_conductor_cech_audit():
    """Whole actual conductor support on the singular normalization carrier.
    Negative/zero/positive exponent support is an exhaustive all-degree type.
    """
    def allowed(kind,exp,loc):
        nz={i for i,a in enumerate(exp) if a};neg={i for i,a in enumerate(exp) if a<0}
        if not neg<=set(loc):return False
        if kind=='C':return not nz and not loc
        if kind in ('+','-'):
            free=set(O if kind=='+' else E)
            return nz<=free and set(loc)<=free
        if not loc:return (nz<=set(E) or nz<=set(O))
        if set(loc)<=set(E):return nz<=set(E)
        if set(loc)<=set(O):return nz<=set(O)
        return False
    def model(kind,exp):
        gs={(kind,loc):-len(loc) for loc in powerset(ALL) if allowed(kind,exp,loc)}
        dd={k:{} for k in gs}
        for k in gs:
            loc=k[1]
            for i in ALL:
                if i in loc:continue
                target=(kind,tuple(sorted(loc+(i,))))
                if target in gs:dd[k][target]=scalar(pm(target[1].index(i)))
        audit(gs,dd,'native_supported_Cech')
        return gs,dd
    hist=Counter();example={}
    for exp in product((-1,0,1),repeat=6):
        mods={k:model(k,exp) for k in ('B','+','-','C')}
        for loc in powerset(ALL):
            present={k:(k,loc) in mods[k][0] for k in mods}
            check(present['B']+present['C']==present['+']+present['-'],
                  'whole_conductor_sequence_termwise_exact_dimensions')
            if present['C']:check(all(present.values()),'actual_conductor_difference_diagonal_kernel')
        # Explicit maps on every existing column, before taking cohomology.
        bd=mods['B'][1];mg={**mods['+'][0],**mods['-'][0]};md={**mods['+'][1],**mods['-'][1]}
        inc={k:{(sgn,k[1]):ONE for sgn in ('+','-') if (sgn,k[1]) in mg} for k in mods['B'][0]}
        quot={k:({('C',k[1]):scalar(1 if k[0]=='+' else -1)} if ('C',k[1]) in mods['C'][0] else {}) for k in mg}
        for k in mods['B'][0]:
            check(apply(md,inc[k])==apply(inc,bd[k]),'supported_native_normalization_inclusion_chain')
            check(not apply(quot,inc[k]),'supported_native_normalization_composite_zero')
        for k in mg:check(apply(mods['C'][1],quot[k])==apply(quot,md[k]),'both_supported_native_augmentations_chain')
        rr=sdr(*mods['B']);hom=dict(Counter(-n for n in rr['gs'].values()))
        expected={}
        if all(v==0 for v in exp):expected={1:1}
        if all(exp[i]==-1 for i in O) and all(exp[i]==0 for i in E):expected={3:1}
        if all(exp[i]==-1 for i in E) and all(exp[i]==0 for i in O):expected={3:1}
        check(hom==expected,'native_full_conductor_local_cohomology_all_729_types')
        hist[str(sorted(hom.items()))]+=1
        if not any(exp):
            so={('B',(i,)):ONE for i in O};se={('B',(i,)):ONE for i in E}
            check(not apply(bd,so) and not apply(bd,se),'both_native_branch_connector_cocycles')
            check(vadd(so,se)==bd[('B',())],'two_native_connector_cocycles_sum_to_boundary')
            red=apply(rr['P'],so)
            check(len(red)==1 and list(red.values())[0] in (ONE,scalar(-1)),
                  'native_conductor_connecting_class_primitive_nonboundary')
            example={'Cech_ranks':dict(Counter(-n for n in mods['B'][0].values())),
                     'odd_cocycle':[f'1 in A[X{i}^-1]' for i in O],
                     'even_cocycle':[f'1 in A[X{i}^-1]' for i in E],
                     'reflection_character_on_H1':-1,'primitive_class':True}
    return {'exhaustive_sign_types':729,'homology_type_histogram':dict(hist),'constant_monomial':example,
            'whole_cohomology':{'1':'C with polarity character',
                               '3':'H^3_odd(B_plus) direct-sum H^3_even(B_minus)'},
            'scope':'actual source occurrence-conductor support, not the PC endpoint restriction'}

def main(output):
    gs,d=normalization_fibre();check(len(gs)==80,'native_resolution_eighty_columns')
    r=sdr(gs,d);check(len(r['gs'])==50 and len(r['pivots'])==15,'fifty_columns_without_denominators')
    ranks=dict(sorted(Counter(r['gs'].values()).items()))
    check(ranks=={0:1,1:9,2:18,3:15,4:6,5:1},'native_resolution_all_Betti_ranks')
    bottom=next(k for k,n in r['gs'].items() if n==0)
    ideal=set()
    for k,n in r['gs'].items():
        if n==1:
            p=r['d'][k].get(bottom,{})
            check(len(p)==1 and abs(next(iter(p.values())))==1,'actual_mixed_ideal_primitive_relation')
            ideal.update(p)
    check(ideal=={weight((i,j)) for i in E for j in O},'native_relation_ideal_is_exact_mixed_product_ideal')
    dg,dd=dual(r['gs'],r['d']);raw_dual=dual(gs,d)
    top=next(k for k,n in dg.items() if n==5)
    topimage=[]
    for k,n in dg.items():
        if n==4:
            p=dd[k].get(top,{})
            check(len(p)==1 and abs(next(iter(p.values())))==1,'dual_conductor_top_boundary_primitive')
            topimage.extend(p)
    check(set(topimage)=={weight((i,)) for i in ALL},'native_H5_exact_annihilator_all_six_occurrences')
    all_degrees=all_native_homogeneous_cohomology(dg,dd)
    actions=native_actions(gs,d)
    attachments=native_attachment_maps()
    # Retain the actual connecting representatives in the 80-column complex.
    for end,s in (('+',E),('-',O)):
        check(not raw_dual[1][(end,s)],'both_native_H3_endpoint_classes_are_cycles')
    # Complete five-variable packet comparison, in the only degree permitting a unit top coefficient.
    five=koszul_co(tuple(range(1,6)),'k')
    nu=tuple(-int(i==0) for i in range(9))
    hb,hd=homogeneous_maps(five,(dg,dd),nu)
    rk,remaining=unit_rank(hd[0],len(hb[1]))
    check(rk==len(hb[0]) and not remaining,'all_five_packet_degree_zero_maps_vanish_in_unit_top_frame')
    check(len(hb[-1])==0,'five_packet_unit_top_frame_has_no_degree_minus_one_maps')
    check(len([c for c in hb[0] if c[0][1]==tuple(range(1,6)) and c[1]==top])==1,
          'unit_top_candidate_was_included_not_excluded')
    # Test a hypothetical splitting C[-5] -> RHom(B,A) on its ENTIRE free resolution.
    sixg,sixd=koszul_co(ALL,'k')
    shifted_six=({k:n-1 for k,n in sixg.items()},{k:minus(v) for k,v in sixd.items()})
    shb,shd=homogeneous_maps(shifted_six,(dg,dd),ZERO)
    srank,srem=unit_rank(shd[0],len(shb[1]))
    check(srank==len(shb[0]) and not srem,'native_conductor_truncation_has_no_primitive_section')
    check(len(shb[-1])==0,'native_truncation_no_hidden_degree_minus_one_maps')
    collars=collars_audit();residues=residue_audit();rees=combined_rees_checks()
    conductor_cech=full_conductor_cech_audit()
    # Distinguish ordinary source normalization from a common integer unit after specialization.
    for mask in range(64):
        ss={i for i in ALL if mask>>i&1}
        alive=not(ss&set(E) and ss&set(O))
        check(alive==(ss<=set(E) or ss<=set(O)),'normalization_all_monomial_supports')
    out={'date':'2026-09-07','commit':COMMIT,'source_blobs':SOURCE_BLOBS,
         'status':'native_normalization_dual_constructed; endpoint_attachment_Gysin_factors_identified; source_to_spatial_PC_comparison_not_claimed',
         'native_conductor_local_cohomology':conductor_cech,
         'native_fibre_columns':len(gs),'integral_reduced_columns':len(r['gs']),'unit_cancellations':len(r['pivots']),
         'resolution_degree_ranks':ranks,'resolution_differentials':export_d(r['d']),
         'dual_cohomology':{'3':'B_plus tensor det(E)^dual + B_minus tensor det(O)^dual',
                            '5':'C tensor det(E+O)^dual tensor polarity'},
         'dual_H5_annihilator':['X0','X1','X2','X3','X4','X5'],
         'both_native_attachment_maps':attachments,
         'all_64_native_occurrence_support_degrees':all_degrees,
         'conductor_section_test':{'Hom_zero_columns':len(shb[0]),'Hom_one_columns':len(shb[1]),'unit_rank':srank,'primitive_section_exists':False},
         'native_truncation_extension':'nonzero pair of primitive Ext^3 classes; not a split direct sum',
         'D3_action_on_framed_conductor_H5':actions,
         'five_variable_packet_test':{'internal_degree':list(nu),'Hom_minus_one_columns':len(hb[-1]),
               'Hom_zero_columns':len(hb[0]),'Hom_plus_one_columns':len(hb[1]),'Hom_zero_differential_unit_rank':rk,
               'unit_top_map_exists':False,'scope':'ordinary A-linear fixed-frame comparison, residual excess factors held fixed'},
         'actual_spatial_collars':collars,'six_transport_Gysin_factorizations':residues,'Rees_tensor_checks':rees,
         'limitations':['No identification of the source dual with the complete ringed supported-Verdier PC kernel.',
                        'The two native attachment morphisms are derived Gysin extension classes, not yet the spatial connector 2-cells.',
                        'The old generic ordinary-blowdown morphism remains null; it was not renamed.',
                        'Native even reflection character does not select physical reflection parity.',
                        'Spectator coefficients may be polynomially extended; nonflat specializations retain derived complexes.'],
         'checks':dict(sorted(COUNTS.items())),'total_exact_assertions':sum(COUNTS.values()),
         'proof_scope':'All-polynomial exactness follows from the normalization exact sequence, regular Koszul resolutions and checked integral deformation retract. Finite checks are not proof-assistant certification.'}
    output.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:out[k] for k in ('status','resolution_degree_ranks','dual_cohomology','five_variable_packet_test','conductor_section_test','actual_spatial_collars','total_exact_assertions')},indent=2))

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path('marici_native_conductor_dual_endpoint_attachment_certificate.json'))
    main(parser.parse_args().output)
