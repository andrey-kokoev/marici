#!/usr/bin/env python3
"""Exact five-row extraction for R_{03,13}.

No physical connector coefficients are supplied or invented.  The default run
reconstructs the target, its five-row quotient, and the grading-forced zero on
the independently documented D03 three-face sector. Standard library only.
"""
from __future__ import annotations
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path
import hashlib
import json

DIAGS = tuple((i,j) for i in range(6) for j in range(i+1,6)
              if j-i != 1 and (i,j) != (0,5))
SLOT = {d:i for i,d in enumerate(DIAGS)}
A, B, C, D = (0,3), (1,3), (0,4), (3,5)
ZERO = (0,)*18
CHECKS: Counter[str] = Counter()

def require(test: bool, label: str) -> None:
    CHECKS[label] += 1
    if not test:
        raise AssertionError(label)

def crossing(a, b):
    if set(a) & set(b):
        return False
    return (a[0] < b[0] < a[1]) != (a[0] < b[1] < a[1])

def subsets(f):
    return [frozenset(z) for n in range(len(f)+1)
            for z in combinations(sorted(f),n)]

FACES = [frozenset(f) for n in range(4) for f in combinations(DIAGS,n)
         if not any(crossing(a,b) for a,b in combinations(f,2))]
CELLS = [(f,h) for f in FACES for h in subsets(f)]
INDEX = {c:i for i,c in enumerate(CELLS)}
VP = frozenset(((1,3),(1,5),(3,5)))
VM = frozenset(((0,2),(0,4),(2,4)))
ENDPOINTS = {i for i,(f,h) in enumerate(CELLS) if f in (VP,VM)}
Q = {i for i,(f,h) in enumerate(CELLS)
     if not f or len(f)==1 and next(iter(f))[1]-next(iter(f))[0]==3}
E = set(range(len(CELLS))) - ENDPOINTS

def mono(x=None, u=None):
    p = [0]*18
    for a,v in (x or {}).items(): p[SLOT[a]] += v
    for a,v in (u or {}).items(): p[9+SLOT[a]] += v
    return tuple(p)

def madd(p,q): return tuple(a+b for a,b in zip(p,q))

def plus(*vectors):
    out = defaultdict(int)
    for v in vectors:
        for k,c in v.items(): out[k] += c
    return {k:c for k,c in out.items() if c}

def scale(v, p=ZERO, s=1):
    return {(j,madd(q,p)):c*s for (j,q),c in v.items() if c*s}

def vector(i,p=ZERO,s=1): return {(i,p):s} if s else {}

def apply(op,v):
    return plus(*(scale(op(i),p,c) for (i,p),c in v.items()))

def deg(i):
    f,h = CELLS[i]
    return 3-len(f)+len(h)

def diff(i, relative=False):
    f,h = CELLS[i]
    out = {}
    for a in DIAGS:
        if a in f or len(f)==3 or any(crossing(a,b) for b in f): continue
        j = INDEX[(f|{a},h)]
        if not relative or j not in ENDPOINTS:
            out[j,mono({a:1},{a:-1})] = (-1)**sum(b<a for b in f)
    for pos,a in enumerate(sorted(h)):
        j = INDEX[(f,h-{a})]
        if not relative or j not in ENDPOINTS:
            out[j,ZERO] = (-1)**(3-len(f)+pos)
    return out

def de(i): return diff(i,True)

def cap(i,a):
    f,h = CELLS[i]
    return (vector(INDEX[(f,h-{a})],s=(-1)**sum(b<a for b in h))
            if a in h else {})

def T(i):
    return scale(apply(lambda j:cap(j,B),cap(i,A)),mono(u={A:-1,B:-1}))

def H(i):
    f,h = CELLS[i]
    if A not in f-h or B not in h: return {}
    return scale(cap(i,B),mono(u={A:-1,B:-1}),(-1)**(3-len(f)))

def radial(i):
    # Definition through the checked commutator, not the five desired outputs.
    return plus(apply(de,H(i)),apply(H,de(i)),scale(T(i),s=-1))

def legal(p,i):
    f,h = CELLS[i]
    return all(v>=0 for v in p[:9]) and all(
        p[9+SLOT[a]]>=0 or a in f-h for a in DIAGS)

def rho(v):
    q = {k:c for k,c in v.items() if k[0] in Q}
    e = plus(*(scale({k:c for k,c in diff(i).items() if k[0] in ENDPOINTS},p,b)
               for (i,p),b in v.items()))
    return q,e

def name(a): return ''.join(map(str,a))

def cell_record(i):
    f,h=CELLS[i]
    return {'index':i, 'face':[name(a) for a in sorted(f)],
            'marks':[name(a) for a in sorted(h)], 'homological_degree':deg(i)}

def mono_record(p):
    return {('X_' if i<9 else 'u_')+name(DIAGS[i%9]):n
            for i,n in enumerate(p) if n}

INPUT_SPEC = [((B,),(B,)), ((C,B),(B,)), ((C,B),(C,B)),
              ((B,D),(B,)), ((B,D),(B,D))]
INPUT = [INDEX[(frozenset(f),frozenset(h))] for f,h in INPUT_SPEC]

def projection(i): return vector(i) if i in INPUT else {}

def dsmall(i): return {k:c for k,c in de(i).items() if k[0] in INPUT}

def degree_obstruction(i, sigma):
    f,h = CELLS[i]
    # A degree-zero homogeneous image has coefficient degree sigma - deg(e_F).
    needed = tuple(sigma[j]+int(a in f) for j,a in enumerate(DIAGS))
    return needed, any(v<0 for v in needed)


def main():
    require(len(CELLS)==215,'census')
    require(len(ENDPOINTS)==16 and len(Q)==7,'census')
    require(sum(len(diff(i)) for i in range(215))==522,'census')
    allrad={i:radial(i) for i in E if radial(i)}
    require(set(allrad)==set(INPUT),'five_rows')
    common=mono({A:1},{A:-2,B:-1})
    signs=[-1,1,-1,1,1]
    OUTPUT=[]
    for i,sign in zip(INPUT,signs):
        f,h=CELLS[i]
        j=INDEX[(f|{A},h-{B})]
        OUTPUT.append(j)
        require(allrad[i]==vector(j,common,sign),'five_rows')
        require(deg(i)-deg(j)==2,'five_rows')
    # Full differential tests and localization legality.
    for i in E:
        require(apply(de,de(i))=={},'d_squared')
        require(apply(de,T(i))==apply(T,de(i)),'T_chain_map')
        require(apply(de,radial(i))==apply(radial,de(i)),'R_chain_map')
        require(apply(dsmall,projection(i))==apply(projection,de(i)),
                'five_row_quotient_chain_map')
        for op in (H,T,radial):
            q,e=rho(op(i))
            require(not q and not e,'complete_boundary_zero')
            for (j,p),coef in op(i).items():
                require(legal(p,j),'localization_legal')
                fi,hi=CELLS[i]; fj,hj=CELLS[j]
                require(fi-hi<=fj-hj,'source_localization_retained')
    # The two-term row differential in the order (1,3,5) -> (2,4).
    yC=mono({C:1},{C:-1}); yD=mono({D:1},{D:-1})
    expected={INPUT[0]:plus(vector(INPUT[1],yC),vector(INPUT[3],yD,-1)),
              INPUT[2]:vector(INPUT[1],s=-1),
              INPUT[4]:vector(INPUT[3]), INPUT[1]:{},INPUT[3]:{}}
    for i in INPUT: require(dsmall(i)==expected[i],'small_matrix')
    require(all(j in OUTPUT for i in OUTPUT for j,p in de(i)),
            'output_subcomplex')
    # In every coefficient module multiplication by the common monomial is
    # injective: its occurrence variable is a nonzero divisor in the polynomial
    # ring, all permitted normal localizations remain domains.  Hence all five
    # rows, rather than only a scalar sum, decide strict vanishing.
    require(len(set(OUTPUT))==5,'distinct_outputs')

    sigma=[0]*9; sigma[SLOT[D]]=1; sigma[SLOT[A]]=-1
    needed_rows=[]
    for i in INPUT:
        needed,blocked=degree_obstruction(i,sigma)
        require(blocked and needed[SLOT[A]]==-1,'normalization_sector_zero')
        needed_rows.append({name(a):v for a,v in zip(DIAGS,needed) if v})
    # No coface without D03 admits any homogeneous coefficient in this degree.
    for i in E:
        needed,blocked=degree_obstruction(i,sigma)
        if A not in CELLS[i][0]:
            require(blocked,'all_absent_D03_forbidden')
    # Negative control: the same condition must NOT discard actual PC source
    # generators of occurrence degree -sum(F).  Each identity row is legal.
    for i in INPUT:
        sigma_i=tuple(-int(a in CELLS[i][0]) for a in DIAGS)
        needed,blocked=degree_obstruction(i,sigma_i)
        require(needed==(0,)*9 and not blocked,'negative_control_nonzero_rows_allowed')

    # Explicit source degree-zero boundary variation (ungraded coefficient
    # category): it changes rows while preserving Q and endpoint restrictions.
    # Source disk in degrees 3->2 with boundary one. Its homotopy sends the
    # degree-two generator to input 3. It is not asserted to be physical.
    j=INPUT[2]
    variation={3:vector(j),2:de(j)}
    require(apply(de,variation[3])==variation[2],'row_variation_control')
    require(apply(de,variation[2])=={},'row_variation_control')
    for v in variation.values():
        require(rho(v)==({},{}),'row_variation_boundary_zero')
    rv={n:apply(radial,v) for n,v in variation.items()}
    require(rv[3]==vector(OUTPUT[2],common,-1),'row_variation_control')
    require(rv[2]==vector(OUTPUT[1],common,-1),'row_variation_control')
    require(apply(de,radial(j))==rv[2],'row_variation_nullhomotopy')

    cert={
      'schema':'marici.branchA.five-row-connector-extraction.v1',
      'scope':'target extraction plus source-grading-forced evaluation, not a full physical connector matrix',
      'reference_commit':'d1947b67a60d3e88ba77f4ca60ea02c2a306ee61',
      'target_basis':'endpoint-relative PC/Cech; original 215-cell indices retained',
      'checks':dict(CHECKS),'check_count':sum(CHECKS.values()),
      'common_factor':mono_record(common),
      'five_rows':[{'input':cell_record(i),'output':cell_record(j),'sign':s,
                    'source_coefficient_needed_at_sigma':nr,
                    'value_on_fixed_normalization_sector':0,
                    'full_physical_connector_row':None}
                   for i,j,s,nr in zip(INPUT,OUTPUT,signs,needed_rows)],
      'row_quotient':{'degree_3_inputs':[1,3,5],'degree_2_inputs':[2,4],
                      'differential':[['X_04/u_04',-1,0],['-X_35/u_35',0,1]]},
      'fixed_source_sector':{'occurrence_degree':{name(a):v for a,v in zip(DIAGS,sigma) if v},
                            'source_terms':['H_Morse p','q_J p','d(xi_tilde) h_3'],
                            'R_kappa':0,
                            'assumptions':['degree-zero occurrence-homogeneous comparison',
                                           'independent normals have occurrence degree zero',
                                           'no occurrence variable inverted']},
      'full_physical_composite':{'status':'not_determined','value':None,
          'reason':'No generator-level normalization-to-PC map on the complete source is supplied by the inspected integration and signature checkers.'},
      'strict_zero_criterion':'K_1=K_2=K_3=K_4=K_5=0',
      'no_integer_torsion_or_homotopy_conclusion_from_unknown_rows':True,
      'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    }
    dst=Path(__file__).with_name('five_row_connector_extraction_certificate.json')
    dst.write_text(json.dumps(cert,indent=2)+'\n')
    print(json.dumps({'checks':sum(CHECKS.values()),'five_rows':5,
          'normalization_sector_composite':0,
          'full_physical_composite':'NOT_DETERMINED',
          'certificate':str(dst)},indent=2))

if __name__=='__main__': main()
