#!/usr/bin/env python3
"""Full closed-union recollement and persistence of the Marici Q obstruction.

Python 3.10+, standard library only. All arithmetic is exact over Z.
Builds the 28-column duals for a cofinal family of support thickenings,
their transition maps, their stable localization complex, and the 27-column
open-complement complex. Verifies the six component decomposition and
saturation of the two previously computed obstruction annihilator ideals.
The all-exponent and derived-category claims require the companion proof;
finite tests are not presented as a proof of the physical source comparison.
"""
from __future__ import annotations
import argparse
from collections import Counter
from itertools import combinations, product
from pathlib import Path
import hashlib
import json

LABELS = ('04','35','02','15','24','13')
PAIRS = ((0,1),(2,3),(4,5))
PLUS = (1,3,5)
MINUS = (0,2,4)
UNIT = (-1,-1,-1)
BASIS = (UNIT,) + tuple(product(range(3), repeat=3))
ZERO = (0,)*6
COUNTS: Counter[str] = Counter()


def check(ok, what, detail=None):
    if not ok:
        raise AssertionError(f'{what}: {detail!r}')
    COUNTS[what] += 1


def sign(n):
    return -1 if n % 2 else 1


def degree(b):
    return 0 if b == UNIT else 1 + b.count(2)


def weight(b):
    w = [0]*6
    if b != UNIT:
        for i,k in enumerate(b):
            if k in (0,2): w[2*i] = 1
            if k in (1,2): w[2*i+1] = 1
    return tuple(w)


def esum(a,b):
    return tuple(x+y for x,y in zip(a,b))


def scale_exp(a,n):
    return tuple(n*x for x in a)


def plus(*vectors):
    out = {}
    for v in vectors:
        for key,c in v.items():
            out[key] = out.get(key,0)+c
            if not out[key]: del out[key]
    return out


def times(v, m=ZERO, c=1):
    return {(b,esum(e,m)):n*c for (b,e),n in v.items() if n*c}


def unit(b, m=ZERO, c=1):
    return {(b,m):c} if c else {}


def apply(op, v):
    out = {}
    for (b,m),c in v.items():
        out = plus(out,times(op.get(b,{}),m,c))
    return out


def free_d(n):
    """Free resolution of B/product_i(s_i^n,t_i^n), homological."""
    d = {b:{} for b in BASIS}
    for b in BASIS:
        if b == UNIT: continue
        if 2 not in b:
            d[b] = unit(UNIT,scale_exp(weight(b),n))
            continue
        for i,k in enumerate(b):
            if k != 2: continue
            before = sum(x == 2 for x in b[:i])
            for choice,var,sgn in ((0,2*i+1,-1),(1,2*i,1)):
                target = b[:i]+(choice,)+b[i+1:]
                m=[0]*6; m[var]=n
                d[b] = plus(d[b],unit(target,tuple(m),sign(before)*sgn))
    return d


def dual_d(n):
    fd=free_d(n); out={b:{} for b in BASIS}
    for c,v in fd.items():
        for (b,e),a in v.items():
            out[b] = plus(out[b],unit(c,e,sign(degree(b)+1)*a))
    return out


def stable_d():
    """Same incidence signs, but maps are inclusions of localizations."""
    d=dual_d(1)
    return {b:{(c,ZERO):a for (c,e),a in v.items()} for b,v in d.items()}


def transition():
    return {b:unit(b,weight(b)) for b in BASIS}


def fraction_map(n):
    return {b:unit(b,scale_exp(weight(b),-n)) for b in BASIS}


def residue_cycle(selected,n):
    out={}
    for choices in product((0,1),repeat=3-len(selected)):
        it=iter(choices); b=[]; m=[0]*6
        for i in range(3):
            if i in selected: b.append(2)
            else:
                c=next(it);b.append(c);m[2*i+c]=n
        out[tuple(b),tuple(m)]=1
    return out


def reduce_unit_matrix(matrix,ncols=None):
    """Unimodular row/column reduction; reject any nonunit residual."""
    a=[row[:] for row in matrix]
    m=len(a); n=len(a[0]) if m else (ncols or 0); k=0
    while k < min(m,n):
        hit=next(((i,j) for i in range(k,m) for j in range(k,n)
                  if abs(a[i][j]) == 1),None)
        if hit is None: break
        i,j=hit; a[k],a[i]=a[i],a[k]
        for row in a: row[k],row[j]=row[j],row[k]
        if a[k][k] == -1: a[k]=[-x for x in a[k]]
        for i in range(m):
            if i!=k and a[i][k]:
                c=a[i][k]; a[i]=[x-c*y for x,y in zip(a[i],a[k])]
        for j in range(n):
            if j!=k and a[k][j]:
                c=a[k][j]
                for i in range(m): a[i][j]-=c*a[i][k]
        k+=1
    check(not any(a[i][j] for i in range(k,m) for j in range(k,n)),
          'all_nonzero_Smith_factors_are_units')
    return k


def active(b,negative):
    return all(weight(b)[i] for i in negative)


def fine_complex(negative,open_part=False):
    d=stable_d()
    if open_part:
        bs=[b for b in BASIS if b!=UNIT and active(b,negative)]
        deg=lambda b: degree(b)-1
        tab={b:times({(c,e):a for (c,e),a in d[b].items()},c=-1) for b in bs}
        maxq=3
    else:
        bs=[b for b in BASIS if active(b,negative)]
        deg=degree; tab=d; maxq=4
    dims=[]; ranks=[]; matrices=[]
    for q in range(maxq+1):
        src=[b for b in bs if deg(b)==q]
        dst=[b for b in bs if deg(b)==q+1]
        dims.append(len(src))
        mat=[[tab[b].get((c,ZERO),0) for b in src] for c in dst]
        matrices.append((src,dst,mat))
        ranks.append(reduce_unit_matrix(mat,len(src)))
    hom={q:dim-(ranks[q-1] if q else 0)-ranks[q]
         for q,dim in enumerate(dims)}
    hom={q:r for q,r in hom.items() if r}
    return hom,dims,ranks,matrices


def is_nonboundary(v,negative):
    _,_,_,mats=fine_complex(negative)
    q=degree(next(iter(v))[0])
    exps={e for b,e in v};check(len(exps)==1,'residue_has_one_fine_degree')
    e=next(iter(exps))
    bs=[b for b in BASIS if degree(b)==q and active(b,negative)]
    incoming=mats[q-1][2] if q else [[] for _ in bs]
    vec=[v.get((b,e),0) for b in bs]
    nr=reduce_unit_matrix(incoming,len(mats[q-1][0]) if q else 0)
    augmented=[row+[a] for row,a in zip(incoming,vec)]
    return reduce_unit_matrix(augmented,(len(incoming[0])+1) if incoming else 1)==nr+1


def polynomial_specialize_d(n,values):
    d=dual_d(n); out={b:{} for b in BASIS}
    for b,v in d.items():
        for (c,e),a in v.items():
            z=a
            for k,p in enumerate(e): z*=values[k]**p
            if z: out[b][c]=out[b].get(c,0)+z
    return out


def constant_cohomology(bs,degrees,tab):
    lo=min(degrees.values());hi=max(degrees.values())
    ranks={};dims={}
    for q in range(lo,hi+1):
        src=[b for b in bs if degrees[b]==q]
        dst=[b for b in bs if degrees[b]==q+1]
        dims[q]=len(src)
        a=[[tab.get(b,{}).get(c,0) for b in src] for c in dst]
        ranks[q]=reduce_unit_matrix(a,len(src))
    return {q:d-ranks.get(q-1,0)-ranks[q] for q,d in dims.items()
            if d-ranks.get(q-1,0)-ranks[q]}


def cone_of_counit_constant(tab):
    b0=('target',); bs=[b0]+[('dual',b) for b in BASIS]
    deg={b0:0};deg.update({('dual',b):degree(b)-1 for b in BASIS})
    d={b:{} for b in bs}
    for b,v in tab.items():
        d[('dual',b)]={('dual',c):-a for c,a in v.items()}
    d[('dual',UNIT)][b0]=1
    return constant_cohomology(bs,deg,d)


# Monomial ideals in 12 variables: six t's followed by six X's in LABELS order.
def minimal(gens):
    ss=set(gens)
    return tuple(sorted(g for g in ss if not any(h!=g and h&g==h for h in ss)))


def intersect_ideals(a,b):
    return minimal(x|y for x in a for y in b)


def intersection(ideals):
    out=(0,)
    for i in ideals: out=intersect_ideals(out,i)
    return out


def contains(gens,m):
    return any(g&m==g for g in gens)


def principal_saturation(gens,m):
    return minimal(g&~m for g in gens)


def ideal_saturation(gens,j):
    return intersection(principal_saturation(gens,m) for m in j)


def enc_mask(m):
    names=tuple('t'+l for l in LABELS)+tuple('X'+l for l in LABELS)
    return [names[i] for i in range(12) if m>>i&1]


def main(output):
    sd=stable_d()
    check([sum(degree(b)==q for b in BASIS) for q in range(5)]==[1,8,12,6,1],
          'support_model_ranks')
    for b in BASIS:
        check(not apply(sd,sd[b]),'stable_d_squared',b)
        for (c,e),a in sd[b].items():
            check(degree(c)==degree(b)+1,'stable_degree',b)
            check(all(x<=y for x,y in zip(weight(b),weight(c))),
                  'localization_maps_only_enlarge_support',b)
    tr=transition()
    for n in range(1,5):
        d=dual_d(n); dn=dual_d(n+1); fd=free_d(n); frac=fraction_map(n)
        for b in BASIS:
            check(not apply(fd,fd[b]),'thickening_free_d_squared',(n,b))
            check(not apply(d,d[b]),'thickening_dual_d_squared',(n,b))
            check(apply(dn,tr[b])==apply(tr,d[b]),'thickening_transition_chain_map',(n,b))
            check(apply(sd,frac[b])==apply(frac,d[b]),'fraction_chain_map',(n,b))
            check(apply(fraction_map(n+1),tr[b])==frac[b],
                  'fractions_compatible_with_transition',(n,b))
        for r in range(1,4):
            for aa in combinations(range(3),r):
                z=residue_cycle(set(aa),n)
                check(not apply(d,z),'finite_residue_closed',(n,aa))
                zn=residue_cycle(set(aa),n+1)
                multiplier=tuple(1 if i//2 in aa else 0 for i in range(6))
                check(apply(tr,z)==times(zn,multiplier),
                      'residue_transition_multiplies_selected_determinants',(n,aa))
                vz=apply(frac,z)
                negative={2*i+k for i in aa for k in (0,1)}
                check(not apply(sd,vz),'stable_residue_closed',(n,aa))
                check(is_nonboundary(vz,negative),'residue_is_primitive_nonboundary',(n,aa))
        for a,b in product(range(2*n+1),repeat=2):
            check(a+b < 2*n-1 or max(a,b)>=n,'cofinal_powers_pigeonhole',(n,a,b))
    # Genuinely higher normal poles: the next s-pole is not killed by s.
    z2=apply(fraction_map(2),residue_cycle({0},2))
    t=[0]*6;t[1]=1
    high=times(z2,tuple(t))  # 1/(s1^2 t1)
    check(is_nonboundary(high,{0,1}),'higher_pole_survives')
    s=[0]*6;s[0]=1
    check(times(high,tuple(s))==apply(fraction_map(1),residue_cycle({0},1)),
          'higher_pole_maps_to_first_residue')

    fine=[]
    for mask in range(64):
        negative={i for i in range(6) if mask>>i&1}
        partial=any(len(negative&set(p))==1 for p in PAIRS)
        np=sum(set(p)<=negative for p in PAIRS)
        expected={} if partial or not np else {np+1:1}
        expected_open={} if partial else {np:1}
        hs,ds,rs,_=fine_complex(negative)
        ho,do,ro,_=fine_complex(negative,True)
        check(hs==expected,'all_support_negative_patterns',mask)
        check(ho==expected_open,'all_open_negative_patterns',mask)
        fine.append({'negative_coordinates':[LABELS[i] for i in sorted(negative)],
                     'support_ranks':ds,'support_differential_ranks':rs,
                     'support_cohomology':hs,'open_ranks':do,
                     'open_differential_ranks':ro,'open_cohomology':ho})
    # A monomial open chart makes at least one variable per pair a unit.
    # Pair-supported modules are killed by all 27 generic localization terms.
    for i,p in enumerate(PAIRS):
        for b in BASIS[1:]:
            check(any(weight(b)[k] for k in p),'closed_pair_kills_each_open_term',(i,b))
    # The finite counit cone, in contrast, has a nonzero derived closed fibre.
    finite=polynomial_specialize_d(1,(0,0,1,1,1,1))
    hu=constant_cohomology(BASIS,{b:degree(b) for b in BASIS},finite)
    hc=cone_of_counit_constant(finite)
    check(hu=={0:1,1:2,2:1},'finite_supported_derived_fibre')
    check(hc=={0:2,1:1},'finite_cone_not_open_localization')

    xplus=sum(1<<(6+i) for i in PLUS)
    xminus=sum(1<<(6+i) for i in MINUS)
    xp=tuple(1<<(6+i) for i in PLUS)
    xm=tuple(1<<(6+i) for i in MINUS)
    tp=sum(1<<i for i in PLUS);tm=sum(1<<i for i in MINUS);T=tp|tm
    cross=minimal(a|b for a in xp for b in xm)
    ann_beta=minimal(cross+(T,)+tuple(tp|a for a in xp)+tuple(tm|a for a in xm))
    ann_extension=minimal(tuple(1<<(6+i) for i in range(6))+(T,))
    primes_beta=[minimal(tuple(1<<(6+j) for j in MINUS)+(1<<i,)) for i in PLUS]
    primes_beta += [minimal(tuple(1<<(6+j) for j in PLUS)+(1<<i,)) for i in MINUS]
    primes_extension=[minimal(tuple(1<<(6+j) for j in range(6))+(1<<i,)) for i in range(6)]
    check(intersection(primes_beta)==ann_beta,'exact_primary_decomposition_beta')
    check(intersection(primes_extension)==ann_extension,'exact_primary_decomposition_extension')
    j=minimal(sum(1<<(2*i+c) for i,c in enumerate(cs)) for cs in product((0,1),repeat=3))
    check(len(j)==8,'eight_open_cover_monomials')
    check(contains(j,tp) and contains(j,tm),'sum_of_branch_products_in_support_ideal')
    check(ideal_saturation(ann_beta,j)==ann_beta,'exact_support_saturation_beta')
    check(ideal_saturation(ann_extension,j)==ann_extension,'exact_support_saturation_extension')
    for name,ps in (('beta',primes_beta),('extension',primes_extension)):
        for p in ps:
            # tau+ + tau- has one surviving monomial modulo every prime.
            check(contains(p,tp) != contains(p,tm),'regular_element_on_each_component',(name,p))
            check(not all(contains(p,m) for m in j),'no_obstruction_component_is_in_pair_union',(name,p))
    # Exhaustive support check covers every exponent because all ideals are squarefree.
    supports=0
    for m in range(1<<12):
        if contains(cross,m): continue
        supports+=1
        check(contains(ann_beta,m)==all(contains(p,m) for p in primes_beta),
              'beta_component_membership',m)
        check(contains(ann_extension,m)==all(contains(p,m) for p in primes_extension),
              'extension_component_membership',m)
    check(supports==960,'all_alternating_occurrence_and_normal_supports')

    # Each bad component has a literal point outside the three pair supports:
    # one branch occurrence and all other t's are 1, its selected t is 0.
    witnesses=[]
    for i in range(6):
        side=PLUS if i in PLUS else MINUS
        mon=sum(1<<j for j in range(6) if j!=i) | (1<<(6+i))
        check(contains(j,mon),'bad_point_is_in_open_complement',i)
        check(not contains(ann_beta,mon),'bad_point_has_nonzero_beta',i)
        for p in PAIRS:
            check(any(mon>>k&1 for k in p),'witness_avoids_every_pair_support',(i,p))
        # Actual singleton PC equation: X_i (U_L+t_i h_i)=0 cannot hold.
        # At this point X_i=U_L=1 and t_i=0, it reads 1=0.
        witnesses.append({'vanishing_normal':'t'+LABELS[i],
                          'nonzero_occurrence':'X'+LABELS[i],
                          'all_other_normals':1,'long_normal_product':1,
                          'singleton_equation_after_specialization':[0,-1]})

    out={
      'schema':'marici.union_recollement.target_persistence.v1',
      'date':'2026-09-07','lane':'Branch B',
      'coefficient_ring':'B=A[t04,t35,t02,t15,t24,t13], A alternating occurrence ring with independent long parameters',
      'support_pairs':[[LABELS[j] for j in p] for p in PAIRS],
      'finite_resolution_ranks':[1,8,12,6,1],
      'stable_support_localization_ranks':[1,8,12,6,1],
      'open_localization_ranks':[8,12,6,1],
      'thickening_ideals':'I_n=product_i(s_i^n,t_i^n); I^(2n-1) subset I_n subset I^n',
      'thickening_transition':'basis b dual maps to product of its selected normal variables times next dual basis',
      'stabilization_map':'b dual maps to b divided by weight(b)^n',
      'stable_support_cohomology':'H^(|S|+1)=direct sum_{nonempty S} top negative Laurent modules on exactly the complete normal pairs in S',
      'fine_degree_records':fine,
      'finite_cone_closed_fibre_cohomology':hc,
      'true_open_closed_fibre_cohomology':{},
      'ann_beta_generators_ambient':[enc_mask(g) for g in ann_beta],
      'ann_beta_minimal_primes':[[enc_mask(g) for g in p] for p in primes_beta],
      'ann_extension_generators':[enc_mask(g) for g in ann_extension],
      'ann_extension_minimal_primes':[[enc_mask(g) for g in p] for p in primes_extension],
      'open_cover_generators':[enc_mask(g) for g in j],
      'saturation_beta_unchanged':True,'saturation_extension_unchanged':True,
      'regular_support_element':'tau_plus+tau_minus',
      'top_homology_after_true_open_functor':'H3(E_open)=H3(E), H3(Q_open)=B theta; image stays a theta',
      'module_extension_restriction':'Ext^1_B(a,M) -> Ext^1_U(a_tilde,M_tilde) is injective by Hartogs for both ends and every extension',
      'generic_unit_closed_lift':'empty',
      'admissible_nonempty_lift_components':'same discrete M-torsors as before, M=I_plus^6 + I_minus^6',
      'six_independent_bad_open_witnesses':witnesses,
      'checks':dict(sorted(COUNTS.items())),
      'exact_assertions':sum(COUNTS.values()),
      'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      'proof_dependencies':[
        'Previous full-target top homology and annihilator theorems, independently replayed.',
        'Noetherian local cohomology equals colimit of derived duals over all thickenings.',
        'Explicit all-degree stable complex and monomial primary/saturation proofs.',
        'Hartogs statements and the extension-class restriction injection are proved in the note, not inferred from numeric tests.'
      ],
      'not_claimed':[
        'Identification of this coefficient-open complement with the physical generic deformation.',
        'New native-source spatial correspondence or missing endpoint connector cells.',
        'A no-go for changing variance, source boundary data, or independently justified support.',
        'Proof-assistant verification or repository modification.'
      ]
    }
    output.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:out[k] for k in ('schema','stable_support_localization_ranks',
       'open_localization_ranks','finite_cone_closed_fibre_cohomology',
       'saturation_beta_unchanged','saturation_extension_unchanged',
       'generic_unit_closed_lift','exact_assertions')},indent=2))


if __name__ == '__main__':
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output',type=Path,default=Path('marici_union_recollement_certificate_20260907.json'))
    args=ap.parse_args()
    main(args.output)
