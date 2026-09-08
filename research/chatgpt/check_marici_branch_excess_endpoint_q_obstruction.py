#!/usr/bin/env python3
"""Source-excess to actual endpoint/Q comparison, with integral obstructions.

Python 3.10+, standard library only. Uses the original 32-generator repeated-
normal Koszul source, not a formal replacement by a Tor label. Reconstructs
all 215 target stalks and their exact localization rules. Computes 24 complete
homogeneous derived-Hom slices. Critical reductions retain and verify full
integral projection, inclusion and contracting-homotopy matrices.

This checks the direct R-linear coefficient problem. It does not implement
an fs/Kato six-operation kernel or assign a physical reflection parity.
"""
from __future__ import annotations
import argparse
from collections import Counter
from itertools import combinations, product
from math import gcd
import hashlib
import json
from pathlib import Path

COMMIT='d1947b67a60d3e88ba77f4ca60ea02c2a306ee61'
SOURCE_BLOBS={
 'research/voevodsky/check_d03_plus_excess_beck_chevalley.rs':'df8448271089910a90c8e641af5b8ae95f1472dd',
 'research/voevodsky/check_global_k6_koszul_cech_promotion.rs':'e972b69d0e2b1b0a0aee5e0a027c8216bcace3e8',
 'research/voevodsky/check_two_endpoint_tate_carrier.rs':'0147e2e42dafac0da7289c571cb0331b51338be1',
}
COUNT=Counter()
def check(ok,category):
    if not ok:raise AssertionError(category)
    COUNT[category]+=1

def pm(n):return -1 if n%2 else 1

def add(*vs):
    out={}
    for v in vs:
        for k,a in v.items():
            out[k]=out.get(k,0)+a
            if not out[k]:del out[k]
    return out

def scale(v,a):return {k:a*b for k,b in v.items() if a*b}
def linear(table,v):
    out={}
    for k,a in v.items():out=add(out,scale(table[k],a))
    return out

def diag(i,j):return tuple(sorted((i%6,j%6)))
def cross(a,b):
    x,y=a;u,v=b
    return x<u<y<v or u<x<v<y

DS=tuple((i,j) for i in range(6) for j in range(i+1,6) if j-i not in (1,5))
SHORTS=tuple(diag(i,i+2) for i in range(6))
LONGS=tuple(diag(i,i+3) for i in range(3))
IX={d:i for i,d in enumerate(SHORTS+LONGS)}
FACES=tuple(f for k in range(4) for f in combinations(DS,k)
            if all(not cross(a,b) for a,b in combinations(f,2)))
CELLS=tuple((f,h) for f in FACES for k in range(len(f)+1) for h in combinations(f,k))
VP=tuple(sorted(SHORTS[i] for i in (1,3,5)))
VM=tuple(sorted(SHORTS[i] for i in (0,2,4)))
ZERO=(0,)*18
G=tuple(product(range(3),range(2)))
SEQ=(1,3,5,0,3)
BRANCH=(1,3,5)
ISET=frozenset((0,1,3,5))

def ex(data):return tuple(data.get(i,0) for i in range(18))
def eadd(a,b):return tuple(x+y for x,y in zip(a,b))
def esub(a,b):return tuple(x-y for x,y in zip(a,b))
GAMMA=ex({15:1,16:1,17:1})

def weight(f):return ex({**{IX[a]:1 for a in f},**{IX[a]+9:-1 for a in f}})
def degree(c):return 3-len(c[0])+len(c[1])
def legal(c,e):
    loc={IX[a] for a in c[0] if a not in c[1]}
    return all(a>=0 for a in e[:9]) and all(a>=0 or i in loc for i,a in enumerate(e[9:]))

def target_pred(c,support):
    v=c[0] in (VP,VM)
    b=any(a in SHORTS for a in c[0])
    return {'K':True,'B':b,'V':v,'E':not v,'Q':not b,'BV':b and not v}[support]

def boundary(c):
    f,h=c;out={}
    for a in DS:
        if a not in f and all(not cross(a,b) for b in f):
            t=(tuple(sorted(f+(a,))),h)
            out[(t,ex({IX[a]:1,IX[a]+9:-1}))]=pm(sum(b<a for b in f))
    for i,a in enumerate(h):
        t=(f,tuple(b for b in h if b!=a))
        out[(t,ZERO)]=pm(3-len(f)+i)
    return out
BD={c:boundary(c) for c in CELLS}

def mask_degree(seq,mask):
    out=[0]*18
    for i,a in enumerate(seq):
        if mask>>i&1:out[9+a]+=1
    return tuple(out)

def hom_complex(seq,lam,support,zero_last=False):
    """Hom_n consists of maps source_i -> target_(i+n). Ext^j=H_(-j)."""
    gens={};coeff={}
    for mask in range(1<<len(seq)):
        target_grade=eadd(lam,mask_degree(seq,mask))
        for c in CELLS:
            m=eadd(target_grade,weight(c[0]))
            if target_pred(c,support) and legal(c,m):
                key=(mask,c);gens[key]=degree(c)-mask.bit_count();coeff[key]=m
    d={x:{} for x in gens}
    for x,n in gens.items():
        mask,c=x
        for (t,m),s in BD[c].items():
            y=(mask,t)
            if not target_pred(t,support):continue
            check(y in gens,'Hom_target_differential_domain')
            check(eadd(coeff[x],m)==coeff[y],'Hom_target_exact_monomial')
            d[x][y]=s
        for i,a in enumerate(seq):
            if mask>>i&1 or (zero_last and i==len(seq)-1):continue
            y=(mask|(1<<i),c)
            check(y in gens,'Hom_source_differential_domain')
            check(eadd(coeff[x],ex({9+a:1}))==coeff[y],'Hom_source_exact_monomial')
            d[x][y]=-pm(n+(mask&((1<<i)-1)).bit_count())
    for x,n in gens.items():
        check(all(gens[y]==n-1 for y in d[x]),'Hom_homological_degree')
        check(not linear(d,d[x]),'Hom_d_squared')
    return gens,d,coeff

def reduce_fast(gens,original):
    """Exact algebraic cancellation. All pivots are signed units."""
    d={x:dict(v) for x,v in original.items()};incoming={x:set() for x in d};pivots=[]
    for x,v in d.items():
        for y in v:incoming[y].add(x)
    while True:
        hit=next(((b,a,u) for b,v in d.items() for a,u in v.items() if abs(u)==1),None)
        if hit is None:break
        b,a,u=hit;db=dict(d[b]);pivots.append((b,a,u))
        check(gens[b]==gens[a]+1 and u*u==1,'integral_unit_pivot')
        for z in list(incoming[a]-{b}):
            v=d[z][a]*u
            for t,c in db.items():
                n=d[z].get(t,0)-v*c
                if n:d[z][t]=n;incoming[t].add(z)
                else:d[z].pop(t,None);incoming[t].discard(z)
        for z in list(incoming[b]):d[z].pop(b,None)
        for t in db:incoming[t].discard(b)
        for t in d[a]:incoming[t].discard(a)
        del d[a];del d[b];del incoming[a];del incoming[b]
    check(not any(d.values()),'zero_residual_differential_integral_homology')
    return dict(sorted(Counter(gens[x] for x in d).items())),pivots

def reduce_sdr(gens,original):
    """Full I,P,H retained for independent chain identities on critical slices."""
    cells=tuple(gens);current={c:dict(v) for c,v in original.items()}
    P={c:{c:1} for c in cells};I=dict(P);H={c:{} for c in cells};np=0
    while True:
        hit=next(((b,a,u) for b in current for a,u in current[b].items() if abs(u)==1),None)
        if hit is None:break
        b,a,u=hit;db=current[b];survive=tuple(c for c in current if c not in (a,b));np+=1
        pa={c:{c:1} for c in survive};pa[b]={};pa[a]={t:-u*v for t,v in db.items() if t!=a}
        inc={c:add({c:1},({b:-u*current[c][a]} if a in current[c] else {})) for c in survive}
        for c in cells:
            acoef=P[c].get(a,0)
            if acoef:H[c]=add(H[c],scale(I[b],u*acoef))
        P={c:linear(pa,v) for c,v in P.items()}
        I={c:linear(I,v) for c,v in inc.items()}
        current={c:linear(pa,linear(current,inc[c])) for c in survive}
    check(not any(current.values()),'SDR_zero_residual')
    for c in cells:
        check(not linear(P,original[c]),'SDR_projection_chain_map')
        check(add(linear(original,H[c]),linear(H,original[c]))==add({c:1},scale(linear(I,P[c]),-1)),
              'SDR_dH_plus_Hd')
    for c,v in I.items():
        check(not linear(original,v),'SDR_section_closed')
        check(linear(P,v)=={c:1},'SDR_projection_section_identity')
    return {'homology':dict(sorted(Counter(gens[c] for c in current).items())),
            'P':P,'I':I,'H':H,'pivots':np}

def wedge(v,w):
    out={}
    for a,ca in v.items():
        for b,cb in w.items():
            if a&b:continue
            inv=sum((b&((1<<i)-1)).bit_count() for i in range(5) if a>>i&1)
            out=add(out,{a|b:ca*cb*pm(inv)})
    return out

def change_basis():
    # old h3(03) = new h3(+) - eta; the same substitution is its inverse.
    table={}
    for mask in range(32):
        v={0:1}
        for i in range(5):
            if mask>>i&1:v=wedge(v,{1<<i:1} if i<4 else {2:1,16:-1})
        table[mask]=v
    for mask,v in table.items():
        check(linear(table,v)=={mask:1},'excess_basis_change_is_integral_involution')
        check(all(mask_degree(SEQ,m)==mask_degree(SEQ,mask) for m in v),'excess_basis_change_preserves_normal_degree')
    return table
CHANGE=change_basis()

def source_d(mask,zero_last=False):
    out={}
    for i,a in enumerate(SEQ):
        if mask>>i&1 and not(zero_last and i==4):
            out[(mask^(1<<i),a)]=pm((mask&((1<<i)-1)).bit_count())
    return out

def check_source():
    for m in range(32):
        left={};right={}
        for n,c in CHANGE[m].items():
            for (t,a),s in source_d(n,True).items():left=add(left,{(t,a):c*s})
        for (n,a),c in source_d(m).items():
            for t,s in CHANGE[n].items():right=add(right,{(t,a):c*s})
        check(left==right,'excess_basis_change_commutes_with_source_d')
    # eta is degree one, differential zero, independent from the other four.
    check(CHANGE[16]=={2:1,16:-1},'eta_is_difference_of_shared_normals')

def precompose_old(v_split):
    grouped={}
    for (mask,c),a in v_split.items():grouped.setdefault(mask,{})[c]=a
    out={}
    for old,terms in CHANGE.items():
        for new,s in terms.items():
            for c,a in grouped.get(new,{}).items():out=add(out,{(old,c):s*a})
    return out

def named_cell(c):
    def dn(a):return 'x'+str(SHORTS.index(a)) if a in SHORTS else 'D'+str(a[0])+str(a[1])
    f,h=c
    return ('T' if not f else ','.join(dn(a) for a in f))+'['+','.join(dn(a) for a in h)+']'
def named_hom(v):return {f'{mask:05b} -> {named_cell(c)}':a for (mask,c),a in sorted(v.items())}
def ext_groups(homology):return {str(-n):r for n,r in sorted(homology.items(),reverse=True)}
def frame(*negative):
    result=list(GAMMA)
    for i in negative:result[9+i]-=1
    return tuple(result)

OMEGA={((),()):1}
for a in LONGS:OMEGA[((a,),(a,))]=-1

def generic_map(tor):
    return precompose_old({(31 if tor else 15,c):a for c,a in OMEGA.items()})

def endpoint_map(tor):
    out={}
    for sub in range(8):
        vals=[SHORTS[BRANCH[i]] for i in range(3) if sub>>i&1]
        orient=pm(sum(a>b for i,a in enumerate(vals) for b in vals[i+1:]))
        coeff=orient*(1 if tor else pm(len(vals)))
        out[(sub|8|(16 if tor else 0),(VP,tuple(sorted(vals))))]=coeff
    return precompose_old(out)

def reduced_regular(lam,support):
    vals={a:lam[9+a] for a in ISET}
    if any(x not in (0,-1) for x in vals.values()):return {}
    required={SHORTS[a] for a,x in vals.items() if x==0}
    forbidden={SHORTS[a] for a,x in vals.items() if x==-1}
    fs=[f for f in FACES if not any(a in LONGS for a in f) and required<=set(f) and not(set(f)&forbidden)
        and target_pred((f,()),support)]
    gs={f:3-len(f)-len(forbidden) for f in fs};d={f:{} for f in fs}
    for f in fs:
        for (t,_),s in BD[(f,())].items():
            if t[0] in gs:d[f][t[0]]=s
    return reduce_fast(gs,d)[0]

def reduced_excess(lam,support):
    h=Counter(reduced_regular(lam,support))
    up=eadd(lam,ex({12:1}))
    for n,r in reduced_regular(up,support).items():h[n-1]+=r
    return dict(sorted({n:r for n,r in h.items() if r}.items()))

def group_diag(d,g):
    r,s=g
    return diag(2*r+(d[0] if not s else 3-d[0]),2*r+(d[1] if not s else 3-d[1]))
def act_exp(v,g):
    out=[0]*18
    for a,i in IX.items():
        j=IX[group_diag(a,g)];out[j]=v[i];out[9+j]=v[9+i]
    return tuple(out)
def act_cell(c,g):
    f,h=c;vf=[group_diag(a,g) for a in f];vh=[group_diag(a,g) for a in h]
    inv=sum(a>b for i,a in enumerate(vf) for b in vf[i+1:])+sum(a>b for i,a in enumerate(vh) for b in vh[i+1:])
    return (tuple(sorted(vf)),tuple(sorted(vh))),pm(g[1]+inv)
def act_hom(v,g):
    out={}
    for (m,c),a in v.items():
        t,s=act_cell(c,g);out[(m,t)]=a*s
    return out


def main(path):
    check(len(CELLS)==215 and len(FACES)==45,'source_target_counts')
    check_source()
    for c in CELLS:
        square={}
        for (t,m),s in BD[c].items():
            check(legal(t,m),'native_target_denominator_rule')
            for (v,n),z in BD[t].items():square=add(square,{(v,eadd(m,n)):s*z})
        check(not square,'all_215_native_polynomial_target_d_squared')
    for m in range(32):
        square={}
        for (n,a),s in source_d(m).items():
            for (t,b),z in source_d(n).items():square=add(square,{(t,tuple(sorted((a,b)))):s*z})
        check(not square,'all_32_repeated_normal_source_d_squared')
    # Full 24-grade coefficient Hom classification, not merely maps on H_*.
    records=[]
    for ns in product((0,-1),repeat=3):
        for n3 in (0,-1,-2):
            lam=list(GAMMA)
            for a,n in zip((0,1,5),ns):lam[9+a]=n
            lam[12]=n3;lam=tuple(lam)
            rec={'normal_frame':{'u0':ns[0],'u1':ns[1],'u3':n3,'u5':ns[2]},'targets':{}}
            for support in ('V','E','Q','B','K'):
                gs,d,cs=hom_complex(SEQ,lam,support)
                h,piv=reduce_fast(gs,d)
                check(h==reduced_excess(lam,support),'full_Hom_agrees_with_independent_face_reduction')
                rec['targets'][support]={'generators':len(gs),'Ext':ext_groups(h),'unit_pivots':len(piv)}
            records.append(rec)
    critical=[];endpoint=[]
    for tor in (False,True):
        lam=frame(0,1,3,5,*((3,) if tor else ()))
        cocycle=generic_map(tor);models={};sdrs={}
        for support in ('V','E','Q','B','K'):
            models[support]=hom_complex(SEQ,lam,support)
            sdrs[support]=reduce_sdr(models[support][0],models[support][1])
        check(all(x in models['Q'][0] for x in cocycle),'generic_source_map_legal')
        check(not linear(models['Q'][1],cocycle),'generic_source_map_closed')
        cohomdegree=2 if tor else 1
        qcoords=linear(sdrs['Q']['P'],cocycle)
        check(len(qcoords)==1 and list(qcoords.values())[0] in (1,-1),'generic_source_map_primitive')
        check(sdrs['E']['homology'].get(-cohomdegree,0)==0,'no_generic_lift_even_in_derived_category')
        defect=linear(models['E'][1],cocycle)
        check(all(x in models['B'][0] for x in defect),'generic_lift_defect_is_actual_short_support')
        check(not linear(models['B'][1],defect),'generic_defect_is_closed')
        bcoords=linear(sdrs['B']['P'],defect)
        check(bcoords and gcd(*[abs(a) for a in bcoords.values()])==1,'generic_defect_primitive_in_free_integral_group')
        check(sdrs['V']['homology']=={},'critical_source_endpoint_complex_acyclic')
        if tor:
            check(sdrs['E']['homology']=={} and sdrs['K']['homology']=={},'Tor_channel_full_target_derived_Hom_acyclic')
            check(sdrs['B']['homology']=={-3:1},'Tor_channel_short_support_Ext3_line')
            check(len(defect)==18,'Tor_channel_eighteen_term_transgression')
        # Multiplying by a source normal changes the prescribed generic class
        # to zero. Its nullhomotopy is precomposition by the existing Koszul
        # wedge, not an inversion or newly adjoined relation.
        for a in sorted(ISET):
            i=SEQ.index(a)
            nextlam=eadd(lam,ex({9+a:1}))
            for sup,closed in (('Q',cocycle),('B',defect)):
                ng,nd,nc=hom_complex(SEQ,nextlam,sup)
                n=next(models[sup][0][key] for key in closed)
                hs={}
                for mask in range(32):
                    if mask>>i&1:continue
                    high=mask|(1<<i)
                    sign=pm(n+(mask&((1<<i)-1)).bit_count())
                    for (source,c),value in closed.items():
                        if source==high:hs=add(hs,{(mask,c):sign*value})
                check(all(key in ng for key in hs),'source_normal_nullhomotopy_is_stalk_legal')
                check(linear(nd,hs)==closed,'source_normal_multiplication_kills_prescribed_class_by_Koszul_homotopy')
        critical.append({'channel':'Tor1' if tor else 'Tor0','normal_frame':list(lam),
            'generic_Ext_degree':cohomdegree,'targets':{k:{'generators':len(models[k][0]),'Ext':ext_groups(sdrs[k]['homology'])} for k in models},
            'generic_cocycle_original_source_basis':named_hom(cocycle),
            'short_support_obstruction_original_source_basis':named_hom(defect),
            'generic_homology_coordinates':named_hom(qcoords),
            'obstruction_homology_coordinates':named_hom(bcoords),
            'obstruction_additive_order':'infinite; primitive free class'})
        # The primitive selected-endpoint residue in each source excess grade.
        le=frame(0,*((3,) if tor else ()))
        ge,de,ce=hom_complex(SEQ,le,'V')
        fe=endpoint_map(tor)
        check(all(x in ge for x in fe),'endpoint_excess_map_legal')
        check(not linear(de,fe),'endpoint_excess_map_closed')
        red=reduce_sdr(ge,de);fc=linear(red['P'],fe)
        check(len(fc)==1 and abs(next(iter(fc.values())))==1,'endpoint_excess_map_primitive')
        check(esub(lam,le)==ex({10:-1,12:-1,14:-1}),'generic_endpoint_weight_gap_is_dual_branch_determinant')
        endpoint.append({'channel':'Tor1' if tor else 'Tor0','normal_frame':list(le),
            'Ext':ext_groups(red['homology']),'cochain':named_hom(fe),
            'primitive_class_coordinates':named_hom(fc)})
        # Transport the entire source Hom complex, not just its class count.
        for g in G:
            seqg=tuple(IX[group_diag(SHORTS[a],g)] for a in SEQ)
            for lf,sup,v in ((lam,'Q',cocycle),(lam,'B',defect),(lam,'E',cocycle),(le,'V',fe)):
                orig=hom_complex(SEQ,lf,sup)
                new=hom_complex(seqg,act_exp(lf,g),sup)
                for x in orig[0]:
                    yvec=act_hom({x:1},g)
                    check(all(y in new[0] for y in yvec),'six_source_charts_transport_all_generators')
                    check(act_hom(orig[1][x],g)==linear(new[1],yvec),'six_source_charts_transport_full_Hom_differential')
                    y=next(iter(yvec))
                    check(act_exp(orig[2][x],g)==new[2][y],'six_source_charts_transport_coefficient_frames')
                check(all(y in new[0] for y in act_hom(v,g)),'transported_endpoint_or_generic_cochain_is_legal')
    # Endpoint normal Koszul -> Cech residue, including every marked state.
    kappa=[]
    for mask in range(8):
        vals=[SHORTS[BRANCH[i]] for i in range(3) if mask>>i&1]
        sg=pm(sum(a>b for i,a in enumerate(vals) for b in vals[i+1:]))
        c=(VP,tuple(sorted(vals)))
        m=eadd(eadd(GAMMA,ex({IX[a]+9:1 for a in vals})),weight(VP))
        check(legal(c,m),'endpoint_Koszul_Cech_denominators_are_target_local')
        left={}
        for (t,bm),a in BD[c].items():left=add(left,{(t,eadd(m,bm)):sg*a})
        right={}
        for i,a in enumerate(BRANCH):
            if not(mask>>i&1):continue
            mm=mask^(1<<i);vv=[SHORTS[BRANCH[j]] for j in range(3) if mm>>j&1]
            tt=(VP,tuple(sorted(vv)))
            orient=pm(sum(x>y for j,x in enumerate(vv) for y in vv[j+1:]))
            e=eadd(eadd(GAMMA,ex({IX[x]+9:1 for x in vv})),weight(VP))
            right=add(right,{(tt,eadd(e,ex({9+a:1}))):pm((mask&((1<<i)-1)).bit_count())*orient})
        check(left==right,'endpoint_Koszul_Cech_map_commutes_with_d')
        kappa.append({'source_mask':mask,'target':named_cell(c),'coefficient_exponents':list(m),'sign':sg})
    result={'date':'2026-09-07','source_commit':COMMIT,'source_blobs':SOURCE_BLOBS,
      'status':'proved_scoped_source_Koszul_endpoint_maps_and_derived_Q_obstruction',
      'source_normal_sequence':['u1','u3','u5','u0','u3'],
      'eta':'h3_plus-h3_pair; homological degree 1 and normal degree e_u3',
      'endpoint_Koszul_Cech_map':kappa,'endpoint_maps':endpoint,
      'critical_generic_lift_problems':critical,'all_24_normal_frames':records,
      'six_transported_branch_pair_charts':6,
      'scope':[
       'Original 32-generator source and all 215 target stalks are retained before taking homogeneous Hom slices.',
       'All polynomial coefficients in each named frame are covered exactly: each legal source/target basis pair has one coefficient monomial and arbitrary integer coefficient.',
       'The 24 frames exhaust possible nonzero Hom cohomology when occurrence map degree is zero, long-normal map degrees are one, and the two short normals outside the intersection have map degree zero.',
       'Negative map degrees are conormal-frame shifts, never permission to add a forbidden inverse to a marked target stalk.',
       'No nonzero integral multiple of the displayed generic class lifts in its specified degree; every replacement cochain and homotopy is included in that Hom complex.',
       'This excludes the direct R-linear map into the covariant BM target, not a mixed-variance or supported-dual logarithmic correspondence.',
       'No globally coupled endpoint connector, physical parity, RH statement or repository write is claimed.'
      ],'assertion_categories':dict(sorted(COUNT.items())),'total_exact_assertions':sum(COUNT.values()),
      'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'assertions':result['total_exact_assertions'],
      'critical':[{k:c[k] for k in ('channel','targets','obstruction_additive_order')} for c in critical],
      'endpoints':[{k:c[k] for k in ('channel','Ext')} for c in endpoint]},indent=2))

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path('marici_branch_excess_endpoint_q_obstruction_certificate.json'))
    args=parser.parse_args();main(args.output)
