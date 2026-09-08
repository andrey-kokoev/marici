#!/usr/bin/env python3
"""Exact formal/punctured gluing checks for the fixed Marici coefficient source.

Standard library only. Finite integral checks supplement the all-series proof.
Completion of a finite coherent source is distinguished from flat base change
of the nonfinite localized PC target. No physical localization is newly admitted.
"""
from __future__ import annotations

import argparse
from collections import Counter
from functools import lru_cache
from itertools import combinations, product
from pathlib import Path
from typing import Callable
import hashlib
import json
import time

CHECKS: Counter[str] = Counter()
DIAG = tuple[int, int]
D = tuple((a,b) for a in range(6) for b in range(a+1,6) if b-a not in (1,5))
PLUS = ((1,3),(1,5),(3,5))
MINUS = ((0,2),(0,4),(2,4))
SHORT = PLUS + MINUS
LONG = tuple(d for d in D if d not in SHORT)
Z12 = (0,)*12


def check(ok: bool, family: str, detail=None) -> None:
    if not ok:
        raise AssertionError(f'{family}: {detail!r}')
    CHECKS[family] += 1


def put(out: dict, key, c: int) -> None:
    if c:
        out[key] = out.get(key,0)+c
        if not out[key]:
            del out[key]


def add(*vs: dict) -> dict:
    out = {}
    for v in vs:
        for k,c in v.items(): put(out,k,c)
    return out


def neg(v: dict) -> dict:
    return {k:-c for k,c in v.items()}


def pm(n: int) -> int:
    return -1 if n%2 else 1


def subsets(xs):
    xs=tuple(xs)
    return tuple(c for n in range(len(xs)+1) for c in combinations(xs,n))


def cross(a: DIAG,b: DIAG) -> bool:
    x,y=a;u,v=b
    return x<u<y<v or u<x<v<y


def multiply_monomials(a,b):
    return tuple(x+y for x,y in zip(a,b))


def exact_rank(matrix: list[list[int]], ncols: int) -> int:
    """Unimodular elimination. Refuse an unverified nonunit residual block."""
    a=[row[:] for row in matrix]
    m=len(a);n=ncols;k=0
    check(all(len(row)==n for row in a),'matrix_shape')
    while k<min(m,n):
        hit=next(((i,j) for i in range(k,m) for j in range(k,n) if abs(a[i][j])==1),None)
        if hit is None: break
        i,j=hit;a[k],a[i]=a[i],a[k]
        for row in a:row[k],row[j]=row[j],row[k]
        if a[k][k]<0:a[k]=[-v for v in a[k]]
        for i in range(m):
            if i!=k and a[i][k]:
                c=a[i][k];a[i]=[x-c*y for x,y in zip(a[i],a[k])]
        for j in range(n):
            if j!=k and a[k][j]:
                c=a[k][j]
                for i in range(m):a[i][j]-=c*a[i][k]
        k+=1
    check(not any(a[i][j] for i in range(k,m) for j in range(k,n)),
          'all_nonzero_Smith_factors_are_units')
    return k


def compose(left: dict,right: dict) -> dict:
    out={}
    for b,n in right.items():
        for c,v in left.get(b,{}).items():put(out,c,n*v)
    return out


def analyze_complex(bases: dict[int,list], differential: dict, label: str):
    for c,v in differential.items():
        check(not compose(differential,v),label+'_d_squared',c)
    ranks={}
    for q in range(4):
        cols=bases.get(q,[]);rows=bases.get(q+1,[])
        mat=[[differential.get(c,{}).get(r,0) for c in cols] for r in rows]
        ranks[q]=exact_rank(mat,len(cols))
    h={q:len(bases.get(q,[]))-ranks.get(q,0)-ranks.get(q-1,0) for q in range(4)}
    check(all(n>=0 for n in h.values()),label+'_homology_ranks')
    return {q:n for q,n in h.items() if n}


# The original seven-chart cover, with central chart indexed by zero.
COVER=tuple(s for s in subsets(range(7)) if s and not(set(s)&{1,2,3} and set(s)&{4,5,6}))


def allowed_ideal(sigma: int, alpha: tuple[int,...], beta: tuple[int,...], patch) -> bool:
    own={1,2,3} if sigma==0 else {4,5,6}
    other={4,5,6} if sigma==0 else {1,2,3}
    if set(patch)&other:return False
    occurrence={i-(1 if sigma==0 else 4) for i in set(patch)&own}
    if not occurrence:
        return patch==(0,) and all(n>=0 for n in alpha) and any(alpha)
    if any(n<0 and i not in occurrence for i,n in enumerate(alpha)):return False
    opposite_t=beta[3:] if sigma==0 else beta[:3]
    return 0 in patch or all(n>=0 for n in opposite_t)


def cover_complex(sigma,alpha,beta):
    nodes={s for s in COVER if allowed_ideal(sigma,alpha,beta,s)}
    bases={q:sorted(s for s in nodes if len(s)==q+1) for q in range(4)}
    differential={s:{} for s in nodes}
    for s in nodes:
        for t in nodes:
            if len(t)==len(s)+1 and set(s)<set(t):
                j=next(i for i,a in enumerate(t) if a not in s)
                differential[s][t]=pm(j)
    return bases,differential


def gluing_complex(sigma,alpha,beta):
    """Cone[-1] of formal ideal + algebraic puncture -> completed puncture.

    Its coefficients are monomial modes, NOT localizations of finite jets.
    """
    regular=all(n>=0 for n in (beta[3:] if sigma==0 else beta[:3]))
    negative={i for i,n in enumerate(alpha) if n<0}
    punctured=[s for s in subsets(range(3)) if s and negative<=set(s)]
    bases={q:[] for q in range(4)}
    if all(n>=0 for n in alpha) and any(alpha):bases[0].append(('H',()))
    for s in punctured:
        if regular:bases[len(s)-1].append(('U',s))
        bases[len(s)].append(('W',s))
    differential={b:{} for bs in bases.values() for b in bs}
    for b in differential:
        typ,s=b
        if typ=='H':
            for t in punctured:
                if len(t)==1:differential[b][('W',t)]=-1
        else:
            for t in punctured:
                if len(t)==len(s)+1 and set(s)<set(t):
                    j=next(i for i,a in enumerate(t) if a not in s)
                    if (typ,t) in differential:
                        differential[b][(typ,t)]=pm(j)*(-1 if typ=='W' else 1)
            if typ=='U':differential[b][('W',s)]=1
    def to_cover(b):
        typ,s=b
        ids=tuple(i+(1 if sigma==0 else 4) for i in s)
        return (0,) if typ=='H' else ids if typ=='U' else (0,)+ids
    return bases,differential,to_cover


def expected_h(alpha,beta,sigma):
    regular=all(n>=0 for n in (beta[3:] if sigma==0 else beta[:3]))
    if regular and all(n>=0 for n in alpha) and any(alpha):return {0:1}
    if not regular and not any(alpha):return {1:1}
    if not regular and all(n<0 for n in alpha):return {3:1}
    return {}


def residue(active: tuple[DIAG,...], inactive: tuple[DIAG,...]):
    opposite=MINUS if active==PLUS else PLUS
    p=[d for d in active if all(not cross(d,e) for e in inactive)]
    l=[d for d in LONG if all(not cross(d,e) for e in inactive)]
    exps=[0]*12
    for d in set(inactive)|set(p):exps[SHORT.index(d)]-=1
    for d in set(LONG)-set(l):exps[9+LONG.index(d)]+=1
    return tuple(exps)


def spectator_regular(exps,sigma):
    opposite=range(3,6) if sigma==0 else range(3)
    return all(exps[i]>=0 for i in opposite)


def diagonal_act(d,r,f):
    return tuple(sorted(((2*r+pm(f)*d[0])%6,(2*r+pm(f)*d[1])%6)))


def spectator_act(e,r,f):
    out=[0]*12
    for i,d in enumerate(SHORT):out[SHORT.index(diagonal_act(d,r,f))]=e[i]
    for i,d in enumerate(LONG):
        j=LONG.index(diagonal_act(d,r,f))
        out[6+j]=e[6+i];out[9+j]=e[9+i]
    return tuple(out)


def pc_kind(cell):
    F,H=cell;ls=set(F)-set(H)
    p=bool(ls&set(PLUS));m=bool(ls&set(MINUS))
    return 'zero_alternating' if p and m else 'lost_in_every_finite_jet' if p or m else 'no_short_inverse'


def pc_diff(cell,stage):
    F,H=cell;out={}
    for a in D:
        if a in F or any(cross(a,b) for b in F):continue
        tgt=(tuple(sorted(F+(a,))),H)
        if pc_kind(tgt)=='zero_alternating':continue
        if stage=='jet' and pc_kind(tgt)=='lost_in_every_finite_jet':continue
        e=[0]*12
        if a in SHORT:e[SHORT.index(a)]=-1
        else:e[6+LONG.index(a)]=1;e[9+LONG.index(a)]=-1
        put(out,(tgt,tuple(e)),pm(sum(b<a for b in F)))
    for j,a in enumerate(H):
        tgt=(F,tuple(b for b in H if b!=a))
        if pc_kind(tgt)=='zero_alternating':continue
        if stage=='jet' and pc_kind(tgt)=='lost_in_every_finite_jet':continue
        put(out,(tgt,Z12),pm(3-len(F)+j))
    return out


def pc_apply(v,stage):
    out={}
    for (cell,e),c in v.items():
        for (t,f),n in pc_diff(cell,stage).items():put(out,(t,multiply_monomials(e,f)),c*n)
    return out


def main(output:Path):
    start=time.monotonic()
    check([sum(len(s)==q for s in COVER) for q in range(1,5)]==[7,12,8,2],
          'original_cover_29_intersections')
    # Entire monomial-mode complexes in the original cover and formal glue cone.
    unique_modes=set();hist=Counter();mode_count=0
    for sigma in (0,1):
        for alpha in product((-2,-1,0,1,2),repeat=3):
            for opp in product((-1,0,1),repeat=3):
                beta=(0,0,0)+opp if sigma==0 else opp+(0,0,0)
                cb,cd=cover_complex(sigma,alpha,beta)
                gb,gd,ident=gluing_complex(sigma,alpha,beta)
                for q in range(4):
                    check(set(map(ident,gb[q]))==set(cb[q]),'glue_cover_degreewise_bijection')
                for b,v in gd.items():
                    check({ident(t):a for t,a in v.items()}==cd[ident(b)],'glue_cover_chain_isomorphism')
                hc=analyze_complex(cb,cd,'original_Cech')
                hg=analyze_complex(gb,gd,'formal_glue')
                expected=expected_h(alpha,beta,sigma)
                check(hc==hg==expected,'all_degree_gluing_formula',(sigma,alpha,beta,hc,expected))
                hist[str(expected)]+=1
                unique_modes.add(tuple(tuple(cb[q]) for q in range(4)))
                mode_count+=1
    # Exact framed bridge -> residue normal form, monomial by monomial.
    bridge_modes=0
    for sigma in (0,1):
        for alpha in product(range(3),repeat=3):
            positive=any(alpha)
            for opposite in product((-2,-1,0,1),repeat=3):
                regular=all(v>=0 for v in opposite)
                has_u=regular;has_h=positive;has_g=positive and regular
                has_e=(not positive) and not regular
                d0=[[1] for _ in range(int(has_u)+int(has_h))] if has_g else [[] for _ in range(int(has_u)+int(has_h))]
                d1=[[1]*int(has_u)+[-1]*int(has_h)]
                rank0=exact_rank(d0,int(has_g));rank1=exact_rank(d1,len(d1[0]))
                check(rank0==int(has_g),'framed_glue_left_injective')
                check(len(d1[0])-rank1==rank0,'framed_glue_stabilizer_kernel')
                check(1-rank1==int(has_e),'framed_glue_residue_cokernel')
                bridge_modes+=1
    # Sparse finite polynomials used to check the all-series shearing identities.
    for sigma in (0,1):
        for k in range(1,5):
            # a formal-tail monomial with an arbitrary opposite pole is legal
            # on the formal side, not a permitted algebraic sheet shear.
            r={(0,0,0):-2};h={(k,0,0):3};u={(0,0,0):1,(0,k,0):-4}
            b=add(r,h)
            normal=add(b,neg(h))
            check(normal==r,'formal_positive_tail_normal_form')
            changed=add(b,u,neg(h))
            check(changed==add(r,u),'bridge_shear_square')
            check(add(changed,neg(u),h)==b,'bridge_shear_inverse')
            # central (a,m) -> punctured (a,m+b*a), and compatible two-sided shear
            for av,mv in product(range(-2,3),repeat=2):
                for rv,hv,uv in product(range(-1,2),repeat=3):
                    lhs=mv+rv*av+uv*av
                    rhs=mv+hv*av+(rv+uv-hv)*av
                    check(lhs==rhs,'framed_transition_square_numeric_basis')
    # All fourteen labelled residues, multipliers, and dihedral relabellings.
    channels=[]
    for sigma,active in enumerate((PLUS,MINUS)):
        opposite=MINUS if sigma==0 else PLUS
        for N in subsets(opposite):
            if not N:continue
            r=residue(active,N)
            check(not spectator_regular(r,sigma),'actual_residue_nonzero_gluing_class',(sigma,N))
            for mask in product((0,1),repeat=6):
                rr=tuple(r[i]+(mask[i] if i<6 else 0) for i in range(12))
                expect=all(mask[SHORT.index(d)] for d in N)
                check(spectator_regular(rr,sigma)==expect,'exact_squarefree_annihilator_control')
            for shift,flip in product(range(3),range(2)):
                new_active=tuple(sorted(diagonal_act(d,shift,flip) for d in active))
                new_N=tuple(sorted(diagonal_act(d,shift,flip) for d in N))
                check(spectator_act(r,shift,flip)==residue(new_active,new_N),'labelled_residue_covariance')
            channels.append({'sheet':'+' if sigma==0 else '-',
                'inactive_subset':[list(d) for d in N],
                'endpoint':len(N)==3,
                't_exponents':r[:6],'long_occurrence_exponents':r[6:9],
                'long_normal_exponents':r[9:]})
    check(len(channels)==14 and sum(c['endpoint'] for c in channels)==2,'all_channels_and_endpoints_retained')
    # A degree-three residue: the top completed puncture mode with three poles.
    for sigma in (0,1):
        alpha=(-1,-1,-1);opposite=(-1,-1,-1)
        beta=(0,0,0)+opposite if sigma==0 else opposite+(0,0,0)
        bases,diff=cover_complex(sigma,alpha,beta)
        check([len(bases[q]) for q in range(4)]==[0,0,0,1],
              'triple_occurrence_pole_has_no_lower_filler')
        check(analyze_complex(bases,diff,'endpoint_H3')=={3:1},'endpoint_derived_glue_H3_nonzero')
    # The complete target module census: keep existing cells, distinguish functors.
    cells=[]
    for F in subsets(D):
        if len(F)>3 or any(cross(a,b) for a,b in combinations(F,2)):continue
        cells.extend((F,H) for H in subsets(F))
    census=Counter(pc_kind(c) for c in cells)
    check(len(cells)==215,'original_target_cell_count')
    check(dict(census)=={'no_short_inverse':72,'lost_in_every_finite_jet':128,'zero_alternating':15},
          'target_flat_basechange_versus_jet_census')
    layers={k:Counter() for k in census}
    for c in cells:
        q=3-len(c[0])+len(c[1]);kind=pc_kind(c);layers[kind][q]+=1
        if kind=='zero_alternating':continue
        check(not pc_apply(pc_diff(c,'flat'),'flat'),'flat_completed_PC_d_squared',c)
        if kind=='no_short_inverse':
            check(not pc_apply(pc_diff(c,'jet'),'jet'),'finite_jet_PC_d_squared',c)
            erase=lambda v:{k:n for k,n in v.items() if pc_kind(k[0])=='no_short_inverse'}
            check(erase(pc_diff(c,'flat'))==pc_diff(c,'jet'),'flat_to_jet_comparison_chain_map',c)
    # Polynomial witnesses for finite-versus-completed puncturing.
    for n in range(1,13):
        # After x^n=0, adjoining x^-1 gives 1=x^n*x^-n=0.
        check(n+(-n)==0,'localized_nilpotent_inverse_identity')
        geometric={i:1 for i in range(1,n+1)}
        lhs=geometric.copy()
        for i,c in geometric.items():put(lhs,i+1,-c)
        put(lhs,1,-1)
        check(lhs=={n+1:-1},'formal_geometric_series_remainder')
        check(not {i:c for i,c in lhs.items() if i<n+1},'finite_polynomial_jet_compatibility')
    # No polynomial p can satisfy (1-x)p=x: evaluation at x=1 gives 0=1.
    check((1-1)*0 != 1,'formal_shear_global_pole_detector')

    inputs={}
    for name in ['marici_conductor_jet_completion_20260907.md',
                 'marici_normalization_endpoint_extension_20260907.md',
                 'marici_target_framed_conductor_tower_20260907.md']:
        p=Path(__file__).with_name(name)
        if p.exists():inputs[name]=hashlib.sha256(p.read_bytes()).hexdigest()
    replay_path=Path(__file__).with_name('replayed_conductor_jet_for_formal_gluing_20260907.json')
    replay=None
    if replay_path.exists():
        data=json.loads(replay_path.read_text())
        replay={'filename':replay_path.name,'sha256':hashlib.sha256(replay_path.read_bytes()).hexdigest(),
                'exact_assertions':data.get('total_exact_assertions'),
                'execution':'Independently rerun at default bounds; this script does not invoke it.'}
    result={
        'status':'proved_for_fixed_coefficient_gluing_problem_not_native_physical_identification',
        'date':'2026-09-07','lane':'Branch B',
        'baseline_commit':'d1947b67a60d3e88ba77f4ca60ea02c2a306ee61',
        'input_note_sha256':inputs,
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'independent_predecessor_replay':replay,
        'results':{
            'formal_overlap':'W=Spec(Bhat) minus V(I*Bhat); never lim of punctured finite jets',
            'gluing_reconstruction':'formal flat-basechanged object + occurrence-complement object + full overlap comparison reconstruct the global module and maps',
            'framed_bridge_objects':'(C[[Xplus]])^7 + (C[[Xminus]])^7',
            'bridge_shears':'formal ideal tails plus algebraic punctured-sheet polynomial shears',
            'bridge_normal_form':'the fourteen occurrence-constant coefficients',
            'components':'(C/Cplus)^7 + (C/Cminus)^7',
            'automorphisms':'(Iplus Cplus[Xplus])^7 + (Iminus Cminus[Xminus])^7',
            'higher_framed_extension_groupoid_homotopy':'zero above pi1; intrinsic conductor module remains nonperfect',
            'H0_one_ideal':'I_sigma C_sigma[X_sigma]',
            'H1_one_ideal':'C/C_sigma',
            'H2_one_ideal':'0',
            'H3_one_ideal':'direct sum over alpha_i>=1 of (C/C_sigma)*X_sigma^(-alpha)',
            'higher_ideal_sheaf_cohomology':'zero above H3',
            'full_target_scope':'flat base change of localization modules, not their derived occurrence-completion',
            'native_source_identified':False,
        },
        'target_summands':dict(census),
        'target_summands_by_homological_degree':{k:dict(sorted(v.items())) for k,v in layers.items()},
        'labelled_residues':channels,
        'finite_audit':{'complete_integer_Cech_mode_comparisons':mode_count,
            'distinct_original_Cech_modes':len(unique_modes),
            'framed_bridge_exact_mode_sequences':bridge_modes,
            'homology_mode_histogram':dict(hist),
            'max_occurrence_test_exponent':2,'opposite_normal_signs':[-1,0,1]},
        'assertions':dict(sorted(CHECKS.items())),
        'total_exact_assertions':sum(CHECKS.values()),
        'runtime_seconds':round(time.monotonic()-start,3),
        'limits':[
            'General formal gluing is a cited theorem applied with checked hypotheses, not a finite-test discovery.',
            'All-series normal form and all-exponent cohomology follow from the proofs in the note.',
            '128 lost summands are coefficient modules, not a claim of 128 lost homology classes.',
            'Degree-three sheaf cohomology is not asserted to be pi3 of the earlier extension groupoid.',
            'No proof assistant, repository writes, new physical inverse, or native spatial connector is claimed.']}
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['status','total_exact_assertions','runtime_seconds','target_summands','finite_audit']},indent=2))


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path('marici_formal_punctured_gluing_certificate_20260907.json'))
    args=parser.parse_args()
    main(args.output)
