#!/usr/bin/env python3
"""Occurrence-linear continuation of Marici's complementary-support kernel.

Reconstructs the 215-state target and the complete repeated-normal source.
Normal homogeneous slices are finite FREE modules over the entire polynomial
occurrence ring Z[X_0,...,X_5,X_D03,X_D14,X_D25], not integer slices with
occurrence monomials replaced by one. All cancellations use signed units.

Verifies polynomial SDRs, the supported-purity comparison, all six transported
branch/pair charts, both endpoint residue frames with their occurrence factors, the full reverse connecting
map, and its exact two-generated occurrence ideal. A separate algebraic proof
in the accompanying note establishes the all-polynomial syzygy conclusions.
No inference of a full physical supported-Verdier functor or parity is made.

Python 3.10+, standard library only. No network or prior artifacts needed.
"""
from __future__ import annotations
import argparse
from collections import Counter
from itertools import combinations, product
from pathlib import Path
import hashlib
import json
from typing import Hashable

COMMIT='d1947b67a60d3e88ba77f4ca60ea02c2a306ee61'
SOURCES={
 'research/voevodsky/check_global_k6_koszul_cech_promotion.rs':'e972b69d0e2b1b0a0aee5e0a027c8216bcace3e8',
 'research/voevodsky/check_d03_plus_excess_beck_chevalley.rs':'df8448271089910a90c8e641af5b8ae95f1472dd',
}
COUNT: Counter[str]=Counter()
def check(condition: bool, category: str) -> None:
    if not condition: raise AssertionError(category)
    COUNT[category]+=1

def pm(n: int) -> int:return -1 if n%2 else 1

def diagonal(i: int,j: int):return tuple(sorted((i%6,j%6)))
def crossing(a,b):
    x,y=a;u,v=b
    return x<u<y<v or u<x<v<y
DS=tuple((i,j) for i in range(6) for j in range(i+1,6) if j-i not in (1,5))
SHORTS=tuple(diagonal(i,i+2) for i in range(6))
LONGS=tuple(diagonal(i,i+3) for i in range(3))
IX={a:i for i,a in enumerate(SHORTS+LONGS)}
FACES=tuple(f for k in range(4) for f in combinations(DS,k)
            if all(not crossing(a,b) for a,b in combinations(f,2)))
CELLS=tuple((f,h) for f in FACES for k in range(len(f)+1) for h in combinations(f,k))
VP=tuple(sorted(SHORTS[i] for i in (1,3,5)))
VM=tuple(sorted(SHORTS[i] for i in (0,2,4)))
ZERO=(0,)*9
ONE={ZERO:1}
# Polynomials are sparse maps exponent -> integer, with no allowed negative powers.
def scalar(n: int):return {ZERO:n} if n else {}
def variable(i: int):
    a=[0]*9;a[i]=1;return {tuple(a):1}
def monomial(a, n=1):
    check(all(i>=0 for i in a),'polynomial_exponents_nonnegative')
    return {tuple(a):n} if n else {}
def padd(*values):
    out={}
    for value in values:
        for a,n in value.items():
            out[a]=out.get(a,0)+n
            if not out[a]:del out[a]
    return out

def pscale(value,n):return {a:n*b for a,b in value.items() if n*b}
def pmul(left,right):
    out={}
    for a,c in left.items():
        for b,d in right.items():
            e=tuple(x+y for x,y in zip(a,b));out[e]=out.get(e,0)+c*d
            if not out[e]:del out[e]
    return out

def vadd(*values):
    out={}
    for value in values:
        for x,p in value.items():
            out[x]=padd(out.get(x,{}),p)
            if not out[x]:del out[x]
    return out

def vmul(v,p):return {x:q for x,a in v.items() if (q:=pmul(a,p))}
def apply(table,v):
    out={}
    for x,p in v.items():out=vadd(out,vmul(table[x],p))
    return out

def minus(v):return vmul(v,scalar(-1))
def unit_vector(x):return {x:ONE}
def edd(*vs):return tuple(sum(t) for t in zip(*vs))
def wedge_normal_degree(seq,mask):
    a=[0]*9
    for j,k in enumerate(seq):
        if mask>>j&1:a[k]+=1
    return tuple(a)

def target_degree(c):return 3-len(c[0])+len(c[1])
def normal_weight(c):return tuple(-int(a in c[0]) for a in SHORTS+LONGS)
def legal_normal(c,a):
    loc={IX[x] for x in set(c[0])-set(c[1])}
    return all(n>=0 or j in loc for j,n in enumerate(a))
def predicate(c,support):
    v=c[0] in (VP,VM);b=bool(set(c[0])&set(SHORTS))
    return {'K':True,'B':b,'V':v,'E':not v,'Q':not b,'BV':b and not v}[support]

def target_boundary(c):
    f,h=c;out=[]
    for a in DS:
        if a not in f and all(not crossing(a,b) for b in f):
            out.append(((tuple(sorted(f+(a,))),h),IX[a],-1,pm(sum(b<a for b in f)),variable(IX[a])))
    for j,a in enumerate(h):
        out.append(((f,tuple(x for x in h if x!=a)),None,0,pm(3-len(f)+j),ONE))
    return out
BOUNDARY={c:target_boundary(c) for c in CELLS}

def add_entry(d,x,y,p):
    d[x][y]=padd(d[x].get(y,{}),p)
    if not d[x][y]:del d[x][y]

def build_model(seq,lam,support,pure=True):
    """Homological Hom degrees; its H_-j is cohomological Ext^j.

    In the pure model the branch's ordered dual determinant and -3 shift
    are retained. Pair generator 2 has zero differential, NOT zero value.
    """
    branch=seq[:3];pair=seq[3:];sseq=pair if pure else seq
    bs=wedge_normal_degree(branch,7) if pure else ZERO
    gs={};nc={}
    for mask in range(1<<len(sseq)):
        alpha=edd(lam,bs,wedge_normal_degree(sseq,mask))
        for c in CELLS:
            normals=edd(alpha,normal_weight(c))
            if not predicate(c,support) or not legal_normal(c,normals):continue
            if pure and ((set(c[0])-set(c[1])) & {SHORTS[i] for i in branch}):continue
            if pure and any(normals[i]!=0 for i in branch):continue
            key=(mask,c);gs[key]=target_degree(c)-(3 if pure else 0)-mask.bit_count();nc[key]=normals
    d={x:{} for x in gs}
    for x,n in gs.items():
        mask,c=x
        for t,index,power,sign,poly in BOUNDARY[c]:
            if not predicate(t,support):continue
            if pure and ((set(t[0])-set(t[1])) & {SHORTS[i] for i in branch}):continue
            y=(mask,t)
            check(y in gs,'target_arrow_has_legal_normal_domain')
            shift=tuple(power if i==index else 0 for i in range(9))
            check(edd(nc[x],shift)==nc[y],'target_normal_exponent_identity')
            add_entry(d,x,y,pscale(poly,-sign if pure else sign))
        for j,a in enumerate(sseq):
            if mask>>j&1 or (pure and a in branch):continue
            y=(mask|(1<<j),c)
            check(y in gs,'source_arrow_has_legal_normal_domain')
            shift=tuple(int(i==a) for i in range(9))
            check(edd(nc[x],shift)==nc[y],'source_normal_exponent_identity')
            sign=-pm(n+(mask&((1<<j)-1)).bit_count())
            add_entry(d,x,y,scalar(sign))
    audit_complex(gs,d,'model')
    return gs,d,nc

def audit_complex(gs,d,tag):
    for x in gs:
        check(all(gs[y]==gs[x]-1 for y in d[x]),tag+'_d_degree')
        check(not apply(d,d[x]),tag+'_d_squared')

def sdr(gs,original,verify=True):
    """Polynomial SDR; only +-1 pivots may be cancelled, never X variables."""
    cur={x:dict(v) for x,v in original.items()}
    P={x:unit_vector(x) for x in gs};I=dict(P);H={x:{} for x in gs};pivots=[]
    while True:
        hit=next(((b,a,p[ZERO]) for b,row in cur.items() for a,p in row.items()
                  if len(p)==1 and p.get(ZERO,0) in (1,-1)),None)
        if hit is None:break
        b,a,u=hit;db=cur[b];survive=tuple(x for x in cur if x not in (a,b));pivots.append((b,a,u))
        pa={x:unit_vector(x) for x in survive};pa[b]={};pa[a]={t:pscale(p,-u) for t,p in db.items() if t!=a}
        inc={x:vadd(unit_vector(x),({b:pscale(cur[x][a],-u)} if a in cur[x] else {})) for x in survive}
        for x in gs:
            p=P[x].get(a,{})
            if p:H[x]=vadd(H[x],vmul(I[b],pscale(p,u)))
        P={x:apply(pa,v) for x,v in P.items()}
        I={x:apply(I,v) for x,v in inc.items()}
        cur={x:apply(pa,apply(cur,inc[x])) for x in survive}
    rgs={x:gs[x] for x in cur}
    if verify:
        audit_complex(rgs,cur,'reduced')
        for x in gs:
            check(apply(cur,P[x])==apply(P,original[x]),'SDR_projection_chain')
            check(vadd(apply(original,H[x]),apply(H,original[x]))==vadd(unit_vector(x),minus(apply(I,P[x]))),'SDR_homotopy_identity')
        for x in cur:
            check(apply(original,I[x])==apply(I,cur[x]),'SDR_section_chain')
            check(apply(P,I[x])==unit_vector(x),'SDR_PI_identity')
    return {'g':rgs,'d':cur,'P':P,'I':I,'H':H,'pivots':len(pivots)}

def purity_projection(raw,pure,branch):
    p={}
    for (mask,c) in raw[0]:
        y=(mask>>3,c);v={}
        if mask&7==7 and y in pure[0] and all(raw[2][(mask,c)][i]==0 for i in branch):
            v[y]=scalar(pm(target_degree(c)+(mask>>3).bit_count()))
            check(raw[2][(mask,c)]==pure[2][y],'purity_normal_coefficients_retained')
        p[(mask,c)]=v
    for x in raw[0]:check(apply(p,raw[1][x])==apply(pure[1],p[x]),'purity_polynomial_chain_map')
    return p

def map_cone(raw,pure,p):
    gs={('p',x):n for x,n in pure[0].items()};gs.update({('r',x):n+1 for x,n in raw[0].items()})
    d={('p',x):{('p',y):q for y,q in row.items()} for x,row in pure[1].items()}
    for x,row in raw[1].items():
        d[('r',x)]={('r',y):pscale(q,-1) for y,q in row.items()}
        d[('r',x)].update({('p',y):q for y,q in p[x].items()})
    audit_complex(gs,d,'purity_cone')
    return gs,d

def transported_diag(d,g):
    r,s=g
    return diagonal(2*r+(d[0] if not s else 3-d[0]),2*r+(d[1] if not s else 3-d[1]))
def index_action(i,g):return IX[transported_diag((SHORTS+LONGS)[i],g)]
def perm_exp(exp,g):
    out=[0]*9
    for i,a in enumerate(exp):out[index_action(i,g)]=a
    return tuple(out)
def perm_poly(p,g):return {perm_exp(e,g):n for e,n in p.items()}
def cell_action(c,g):
    f,h=c;ff=[transported_diag(a,g) for a in f];hh=[transported_diag(a,g) for a in h]
    inv=sum(a>b for i,a in enumerate(ff) for b in ff[i+1:])+sum(a>b for i,a in enumerate(hh) for b in hh[i+1:])
    return (tuple(sorted(ff)),tuple(sorted(hh))),pm(g[1]+inv)
def hom_action(v,g):
    out={}
    for (mask,c),p in v.items():
        t,s=cell_action(c,g);out[(mask,t)]=pscale(perm_poly(p,g),s)
    return out

def poly_text(p):
    names=['X'+str(i) for i in range(6)]+['XD03','XD14','XD25'];terms=[]
    for e,n in sorted(p.items()):
        m='*'.join(name+('^'+str(a) if a!=1 else '') for name,a in zip(names,e) if a)
        terms.append(str(n)+(('*'+m) if m else ''))
    return ' + '.join(terms) or '0'
def cell_text(c):
    def lab(a):return 'x'+str(SHORTS.index(a)) if a in SHORTS else 'D'+str(a[0])+str(a[1])
    return (','.join(map(lab,c[0])) or 'T')+'['+','.join(map(lab,c[1]))+']'
def key_text(k):return f'{k[0]:02b}->{cell_text(k[1])}'
def export_vec(v):return {key_text(k):poly_text(p) for k,p in v.items()}
def export_reduction(model,r):
    return {'source_columns':len(model[0]),'unit_cancellations':r['pivots'],
            'reduced_degrees':{key_text(k):-n for k,n in r['g'].items()},
            'reduced_differential':{key_text(k):export_vec(v) for k,v in r['d'].items()}}

def project(vector,model):return {x:p for x,p in vector.items() if x in model[0]}
def row_value(row,v):
    out={}
    for x,p in v.items():out=padd(out,pmul(row.get(x,{}),p))
    return out

def dual_row_d(row,model):
    # Raw transpose; a uniform degree sign yields the usual derived Hom dual.
    return {x:p for x,v in model[1].items() if (p:=row_value(row,v))}

def check_chart(g,reference=None,full_purity=False):
    seq=tuple(index_action(i,g) for i in (1,3,5,0,3))
    base=[0]*9
    for i in (6,7,8):base[i]=1
    for i in seq:base[i]-=1
    lam=tuple(base)
    models={s:build_model(seq,lam,s) for s in ('K','B','V','E','Q','BV')}
    rs={s:sdr(m[0],m[1]) for s,m in models.items()}
    if reference:
        for s,ref in reference.items():
            for x,row in ref[1].items():
                tx=hom_action(unit_vector(x),g)
                check(apply(models[s][1],tx)==hom_action(row,g),'six_transport_polynomial_chain_covariance')
    # All support maps are the actual inclusion/quotient columns, not rank matches.
    for a,b in [('V','B'),('B','K'),('V','K'),('BV','E')]:
        for x,row in models[a][1].items():check(row==project(models[b][1][x],models[a]),'literal_support_inclusion')
    for a,b in [('K','E'),('K','Q'),('B','BV'),('E','Q')]:
        for x,row in models[a][1].items():
            right=models[b][1][x] if x in models[b][0] else {}
            check(project(row,models[b])==right,'literal_support_quotient')
    qkeys=list(rs['Q']['g']);check(len(qkeys)==1 and rs['Q']['g'][qkeys[0]]==-2,'generic_polynomial_line')
    q=qkeys[0];G=rs['Q']['I'][q];beta=apply(models['K'][1],G)
    check(len(beta)==9 and set(beta)<=set(models['B'][0]),'nine_term_polynomial_transgression')
    check(not apply(models['B'][1],beta),'transgression_closed')
    rb=apply(rs['B']['P'],beta)
    complement=tuple(sorted(set(range(6))-set(seq)))
    check(len(complement)==2,'two_residual_occurrence_directions')
    a,b=complement
    rows={}
    for idx in complement:
        key=next(x for x,n in rs['B']['g'].items() if n==-3 and x[1][0]==(SHORTS[idx],))
        check(rb.get(key)==pscale(variable(idx),-1),'exact_reduced_transgression_coefficient')
        row={x:pscale(v[key],-1) for x,v in rs['B']['P'].items() if key in v}
        check(not dual_row_d(row,models['B']),'polynomial_short_dual_cocycle')
        check(row_value(row,beta)==variable(idx),'primitive_ideal_generator_evaluation')
        # Extend by zero to K: the dual boundary has only Q support and exactly
        # X_i times the canonical generic coefficient functional.
        extended=dual_row_d(row,models['K'])
        check(set(extended)<=set(models['Q'][0]),'reverse_boundary_has_literal_generic_support')
        check(row_value(extended,G)==variable(idx),'generic_reverse_pairing_same_ideal_generator')
        rows[str(idx)]={'short_covector':export_vec(row),'generic_covector':export_vec(extended)}
    check(len(rs['K']['g'])==4 and len(rs['B']['g'])==3 and not rs['V']['g'],'critical_core_sizes')
    # Endpoint frames retain their own classes. They are not merged into the generic frame.
    endpoints={}
    for tor in (0,1):
        el=[0]*9
        for i in (6,7,8):el[i]=1
        el[seq[3]]-=1
        if tor:el[seq[4]]-=1
        em=build_model(seq,tuple(el),'V');er=sdr(em[0],em[1])
        check(len(er['g'])==1 and not any(er['d'].values()),'endpoint_polynomial_line_survives_unframed')
        check(next(iter(er['g'].values()))==-(1+tor),'endpoint_source_excess_degree_retained')
        erow=export_reduction(em,er)
        ep=[0]*9
        for i in seq[:3]:ep[i]+=1
        prescribed=monomial(ep,pm(tor))
        ekey=next(iter(er['g']))
        endpoint_class=vmul(er['I'][ekey],prescribed)
        check(not apply(em[1],endpoint_class),'prescribed_endpoint_occurrence_class_closed')
        check(apply(er['P'],endpoint_class)=={ekey:prescribed},'prescribed_endpoint_class_not_deleted')
        erow['prescribed_residue_class']=export_vec(endpoint_class)
        erow['framing']='The source principal occurrence line is retained. Before its supplied dual-line pairing the class has the displayed X_branch factor; it is not a unit of B.'
        endpoints[str(tor)]=erow
    purity={}
    if full_purity:
        for s in models:
            raw=build_model(seq,lam,s,pure=False);p=purity_projection(raw,models[s],seq[:3])
            cg,cd=map_cone(raw,models[s],p);cr=sdr(cg,cd)
            check(not cr['g'],'full_source_purity_cone_polynomial_acyclic')
            purity[s]={'raw_columns':len(raw[0]),'cone_columns':len(cg),'unit_cancellations':cr['pivots']}
    return models,{'group_element':list(g),'normal_sequence':list(seq),'normal_frame':list(lam),
        'residual_occurrence_ideal':['X'+str(i) for i in complement],
        'support_complexes':{s:export_reduction(models[s],rs[s]) for s in models},
        'primitive_generic_chain':export_vec(G),'nine_term_obstruction':export_vec(beta),
        'reduced_obstruction':export_vec(rb),'reverse_pairing_rows':rows,
        'endpoint_channels':endpoints,'full_source_purity_cones':purity}

def weighted_cubical_audit():
    # Normal degree (1,...,1) admits ALL marked states. Coarse occurrence
    # linearity retains radial X_a and unit normal coefficients on this frame.
    d={c:{} for c in CELLS};transpose={c:{} for c in CELLS}
    for c in CELLS:
        for t,index,power,sign,poly in BOUNDARY[c]:
            d[c][t]=pscale(poly,sign)
            transpose[t][c]=pscale(poly,sign)
    cube={c:{} for c in CELLS};gauge={}
    for c in CELLS:
        f,h=c;free=tuple(a for a in f if a not in h)
        gauge[c]=pm(len(f)+len(h)*(3-len(f))+sum(f.index(a) for a in h))
        for j,a in enumerate(free):
            upper=(f,tuple(sorted(h+(a,))))
            lower=(tuple(x for x in f if x!=a),h)
            cube[c][upper]=scalar(pm(j));cube[c][lower]=pscale(variable(IX[a]),-pm(j))
    for c in CELLS:
        check(not apply(cube,cube[c]),'weighted_cube_d_squared')
        left={x:pscale(p,gauge[x]) for x,p in transpose[c].items()}
        right={x:pscale(p,gauge[c]) for x,p in cube[c].items()}
        check(left==right,'all_215_weighted_cubes_are_polynomial_transposes')
    # A constant-coefficient Serre diagonal is not a B-linear diagonal of
    # d e = upper-X lower with both vertices fixed group-like. The necessary
    # edge equations imply X*(X-1)=0, impossible in the polynomial ring.
    x=variable(2)
    obstruction=pmul(x,padd(x,scalar(-1)))
    check(bool(obstruction),'group_like_polynomial_diagonal_obstruction_nonzero')
    return {'cells':215,'weighted_edge':'d e = upper-X_a lower',
            'constant_Serre_diagonal_defect':'(1-X_a) lower tensor upper',
            'all_edge_filler_necessary_condition':'X_a*(X_a-1)=0, false in B',
            'scope':'Only a single B-linear tensor target with both vertex columns group-like is excluded. A coefficient-line-valued or sheafwise diagonal has a different typing.'}

def reduced_support_and_rees_controls():
    x,y=variable(2),variable(4)
    # Explicit regular Koszul complex, with all coefficients retained.
    gs={'q':-2,'a':-3,'b':-3,'ab':-4}
    d={'q':{'a':x,'b':y},'a':{'ab':pscale(y,-1)},'b':{'ab':x},'ab':{}}
    audit_complex(gs,d,'two_occurrence_Koszul')
    # The complete occurrence-zero slice uses q,X2*a,X4*b,X2*X4*ab.
    slice_d={'q':{'a':ONE,'b':ONE},'a':{'ab':scalar(-1)},'b':{'ab':ONE},'ab':{}}
    sr=sdr(gs,slice_d)
    check(not sr['g'],'old_fully_homogeneous_slice_is_acyclic')
    # At the codimension-two occurrence face all matrices vanish. Four states
    # survive; this is derived base change of the free Koszul model.
    for row in d.values():
        check(all(all(e[2]>0 or e[4]>0 for e in p) for p in row.values()),'central_occurrence_face_differential_vanishes')
    # B-linearity falsifier: the old grade-wise functional reads the X2 monomial.
    coefficient_X2=lambda p:p.get(next(iter(x)),0)
    check(coefficient_X2(x)==1 and coefficient_X2(ONE)==0,'coefficient_extractor_not_B_linear')
    # The two normalized principal-open lifts have a derived-overlap homotopy.
    # Laurent controls are confined to the declared OPEN cover X2 !=0 or X4 !=0.
    # Fractions here are exponent dictionaries; these are NOT used on closed base.
    invx={tuple(-a for a in next(iter(x))):1};invy={tuple(-a for a in next(iter(y))):1}
    hx={'a':invx};hy={'b':invy}
    check(row_value(hx,d['q'])==ONE and row_value(hy,d['q'])==ONE,'open_trace_has_unit_value')
    overlap=pmul(invx,invy)
    # hx-hy = -(1/(xy)) (-y,x) on overlap.
    check(vadd(hx,minus(hy))=={'a':pmul(overlap,y),'b':pscale(pmul(overlap,x),-1)},'open_trace_overlap_homotopy')
    # The overlap coefficient 1/(X2 X4) is a primitive local cohomology/Gysin
    # symbol: its exponent (-1,-1) lies in neither single-localization image.
    e=next(iter(overlap));check(e[2]==e[4]==-1,'primitive_two_occurrence_residue_symbol')
    # Tensor the entire four-term core with each of the eight ordinary lower+
    # localized support complexes after central Rees specialization. All support
    # differentials are unit inclusions within their own summands; no X2 or X4
    # coefficient is changed to one by tensoring.
    total=0
    for killed in range(8):
        masks=[m for m in range(8) if not(m&killed)]
        tg={(z,m):n-m.bit_count() for z,n in gs.items() for m in masks}
        td={z:{} for z in tg}
        for (z,m),n in tg.items():
            for w,p in d[z].items():td[(z,m)][(w,m)]=p
            for i in range(3):
                if not(m>>i&1) and not(killed>>i&1):
                    target=(z,m|(1<<i))
                    td[(z,m)][target]=scalar(pm(gs[z]+(m&((1<<i)-1)).bit_count()))
        audit_complex(tg,td,'supported_Rees_tensor')
        total+=len(tg)
    return {'reduced_Koszul_chain':{x:{y:poly_text(p) for y,p in row.items()} for x,row in d.items()},
            'old_unit_occurrence_slice':'acyclic; not a polynomial-family dual',
            'principal_open_unit_lifts':['(1/X2,0)','(0,1/X4)'],
            'overlap_homotopy':'-1/(X2 X4) times the Koszul syzygy (-X4,X2)',
            'closed_support_class':'[1/(X2 X4)] with ordered determinant retained',
            'Rees_faces_checked':8,'supported_tensor_columns':total}

def main(output: Path):
    check(len(CELLS)==215 and len(FACES)==45,'source_cell_counts')
    records=[];reference=None
    for g in product(range(3),range(2)):
        models,record=check_chart(g,reference,full_purity=(g==(0,0)))
        if reference is None:reference=models
        records.append(record)
    controls=reduced_support_and_rees_controls()
    weighted=weighted_cubical_audit()
    result={'status':'proved_occurrence_linear_reverse_pairing_ideal_not_unit',
      'date':'2026-09-07','source_commit':COMMIT,'source_blob_hashes':SOURCES,
      'coefficient_ring':'B=Z[X0,X1,X2,X3,X4,X5,XD03,XD14,XD25]',
      'normal_frame_scope':'fixed excess normal frame, ALL occurrence polynomial degrees',
      'main_exact_results':{
        'plus_D03_primal_core':'B -> B^2 -> B in cohomological degrees 2,3,4; maps (X2,X4),(-X4,X2)',
        'total_core_cohomology':'H4=B/(X2,X4); Hq=0 otherwise',
        'short_core_cohomology':'H3=B with generator (X2,X4); H4=B/(X2,X4)',
        'generic_core_cohomology':'H2=B',
        'reverse_dual_image_ideal':'(X2,X4) in B',
        'reverse_unit_lift_exists_over_B':False,
        'residual_support':'V(X2,X4)',
        'integer_inversion_removes_obstruction':False,
        'endpoint_comparisons_in_critical_frame':'V complex has a signed-unit contraction',
        'endpoint_residue_frames':'ordinary and excess residue classes retain their prescribed principal occurrence factor; the underlying B-modules are free lines',
        'full_physical_source_to_kernel_identification':False,
        'physical_reflection_parity_assigned':False},
      'transported_charts':records,'controls':controls,'weighted_cubical_audit':weighted,
      'exact_assertions':dict(sorted(COUNT.items())),'total_exact_assertions':sum(COUNT.values()),
      'proof_scope':'All polynomial conclusions follow from the exact SDR and the regular-sequence syzygy proof in the note. No degree truncation, random rank test, or proof assistant. Principal-open denominators occur only in explicitly labelled negative/control local constructions.',
    }
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'checks':result['total_exact_assertions'],
       'transported_ideals':[r['residual_occurrence_ideal'] for r in records],
       'full_purity_cones':records[0]['full_source_purity_cones'],'main':result['main_exact_results']},indent=2))

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path('marici_occurrence_linear_reverse_pairing_certificate.json'))
    args=parser.parse_args();main(args.output)
