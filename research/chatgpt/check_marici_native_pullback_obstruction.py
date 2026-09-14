#!/usr/bin/env python3
"""Native derived-pullback endpoint test. Standard library only.

New calculation: Y = B tensor_A^L RHom_A(G,V), not the previously falsified
coinduced/ambient Hom. In the fixed endpoint frame, Y is K_B(X_0,...,X_5)
times the retained primitive line. The complete B-action and all Koszul Tor
terms are kept. A B-linear primitive branch map already fails in resolution
degree two. No claim is made against all native coefficient targets.

No prior checker is imported or run. No new cone or physical cells are added.
"""
from __future__ import annotations
import argparse
from collections import Counter
from itertools import combinations, product
import json
from pathlib import Path

EV=(0,2,4)
OD=(1,3,5)
ZERO=(0,)*6
CHECKS=Counter()

def check(p, name):
    if not p:
        raise AssertionError(name)
    CHECKS[name]+=1

def sgn(n): return -1 if n%2 else 1

def subs(xs):
    xs=tuple(xs)
    return tuple(s for n in range(len(xs)+1) for s in combinations(xs,n))

SUBS=subs(range(6))

def unit(i):return tuple(int(j==i) for j in range(6))

def plus(a,b):return tuple(x+y for x,y in zip(a,b))

def minus(a,b):return tuple(x-y for x,y in zip(a,b))

def wt(I):return tuple(int(i in I) for i in range(6))

def native(a):
    return min(a)>=0 and not(any(a[i] for i in EV) and any(a[i] for i in OD))

def add(*vs):
    ans={}
    for v in vs:
        for k,a in v.items():
            ans[k]=ans.get(k,0)+a
            if not ans[k]:del ans[k]
    return ans

def scale(v,a):return {k:a*b for k,b in v.items() if a*b}

def apply(d,v):
    return add(*(scale(d.get(k,{}),a) for k,a in v.items()))

def homogeneous_koszul(alpha):
    g={I:len(I) for I in SUBS if native(minus(alpha,wt(I)))}
    d={I:{I[:j]+I[j+1:]:sgn(j) for j in range(len(I))
           if I[:j]+I[j+1:] in g} for I in g}
    for I in g:
        check(not apply(d,d[I]), 'new_native_Koszul_d_squared')
    return g,d

def integral_cancel(g, original):
    """Signed-unit elementary chain contractions; no rational rank inference."""
    d={x:dict(v) for x,v in original.items()}
    pivots=0
    while True:
        pivot=next(((s,t,a) for s,v in d.items() for t,a in v.items() if abs(a)==1),None)
        if pivot is None:break
        s,t,a=pivot
        check(g[s]==g[t]+1,'unit_cancellation_degree')
        tail={k:-a*b for k,b in d[s].items() if k!=t}
        kept=[x for x in d if x not in (s,t)]
        d={x:add({k:b for k,b in d[x].items() if k not in (s,t)},
                    scale(tail,d[x].get(t,0))) for x in kept}
        pivots+=1
    check(not any(d.values()),'all_remaining_differentials_zero_integrally')
    return dict(sorted(Counter(g[x] for x in d).items())),pivots

def repeat_contraction(alpha,g,d):
    j=next(i for i,a in enumerate(alpha) if a>=2)
    h={I:({tuple(sorted(I+(j,))):sgn(sum(i<j for i in I))}
             if j not in I else {}) for I in g}
    for I in g:
        check(all(J in g for J in h[I]), 'repeat_contraction_native_coefficient_domain')
        check(add(apply(d,h[I]),apply(h,d[I]))=={I:1},'repeat_exponent_integral_contraction')
        check(not apply(h,h[I]),'repeat_contraction_square_zero')

def koszul_audit():
    totals=Counter(); records=[]; columns=0; repeats=0
    for alpha in product(range(3),repeat=6):
        g,d=homogeneous_koszul(alpha);columns+=len(g)
        h,p=integral_cancel(g,d)
        is_squarefree=max(alpha)<=1
        even=sum(alpha[i] for i in EV);odd=sum(alpha[i] for i in OD)
        expected=({0:1} if not any(alpha) else
                  {sum(alpha)-1:1} if is_squarefree and even and odd else {})
        check(h==expected,'complete_native_Koszul_fine_weight_cohomology')
        if not is_squarefree:
            repeat_contraction(alpha,g,d);repeats+=1
        else:
            totals.update(h)
            records.append({'weight':alpha,'columns':len(g),'homological_ranks':h,'unit_pairs':p})
    check([totals[i] for i in range(6)]==[1,9,18,15,6,1],'native_Tor_rank_profile')
    return {'computed_weight_patterns':3**6,'columns':columns,'squarefree_records':records,
            'nonsquarefree_contractions':repeats,
            'homological_Tor_ranks':[totals[i] for i in range(6)],
            'all_exponent_proof':'Any repeated exponent has the explicit one-variable wedge contraction.'}

# Sparse polynomial vectors: (basis_label, monomial) -> integer coefficient.
def pmul(v,m):
    return {(k,plus(a,m)):c for (k,a),c in v.items() if native(plus(a,m))}

def papply(d,v):return add(*(scale(pmul(d.get(k,{}),m),c) for (k,m),c in v.items()))

def free_koszul():
    g={I:len(I) for I in SUBS}
    w={I:wt(I) for I in g}
    d={I:{(I[:j]+I[j+1:],unit(i)):sgn(j) for j,i in enumerate(I)} for I in g}
    return g,d,w

def branch_skeleton(killed):
    """Exact through degree one. All degree-two generators are actual syzygies."""
    surviving=tuple(i for i in range(6) if i not in killed)
    u=('unit',);g={u:0};w={u:ZERO};d={u:{}}
    for e in killed:
        a=('a',e);g[a]=1;w[a]=unit(e);d[a]={(u,unit(e)):1}
    for e,f in combinations(killed,2):
        a=('pure',e,f);g[a]=2;w[a]=plus(unit(e),unit(f))
        d[a]={(('a',f),unit(e)):1,(('a',e),unit(f)):-1}
    for e in killed:
        for o in surviving:
            a=('mixed',o,e);g[a]=2;w[a]=plus(unit(o),unit(e))
            d[a]={(('a',e),unit(o)):1}
    for a in g:
        check(not papply(d,d[a]),'native_branch_skeleton_d_squared')
        for (b,m),c in d[a].items():
            check(plus(w[b],m)==w[a] and g[b]+1==g[a], 'branch_skeleton_degree_and_weight')
    return g,d,w

def skeleton_homology_audit(killed):
    g,d,w=branch_skeleton(killed);columns=0
    for alpha in product(range(3),repeat=6):
        gg={a:n for a,n in g.items() if native(minus(alpha,w[a]))}
        dd={a:{} for a in gg}
        for a in gg:
            source_m=minus(alpha,w[a])
            for (b,m),c in d[a].items():
                if native(plus(source_m,m)):
                    check(b in gg,'branch_weight_domain')
                    dd[a][b]=dd[a].get(b,0)+c
        for a in gg:check(not apply(dd,dd[a]),'homogeneous_branch_d_squared')
        hh,_=integral_cancel(gg,dd);columns+=len(gg)
        check(hh.get(1,0)==0,'branch_skeleton_exact_in_degree_one')
        check(hh.get(0,0)==int(not any(alpha[i] for i in killed)), 'branch_quotient_degree_zero')
    return columns

def derived_branch_source_audit():
    """Retain, rather than silently discard, Tor in Lq*(B_sigma).
    The ordinary native branch and this derived source are different objects.
    """
    kg,kd,kw=free_koszul();records=[]
    for killed,side in ((EV,'plus'),(OD,'minus')):
        basis=subs(killed)
        source={I:{(I[:j]+I[j+1:],unit(i)):sgn(j) for j,i in enumerate(I)} for I in basis}
        inclusion={I:{(I,ZERO):1} for I in basis}
        for I in basis:
            check(papply(kd,inclusion[I])==papply(inclusion,source[I]),
                  'native_derived_branch_primitive_map_chain_equation')
        check(inclusion[()]=={((),ZERO):1},'derived_branch_source_primitive_coefficient')
        for e in killed:
            for o in range(6):
                if o in killed:continue
                cycle={((e,),unit(o)):1}
                check(not papply(source,cycle),'derived_branch_mixed_Tor_cycle_closed')
                check(papply(inclusion,cycle)==cycle,'derived_branch_Tor_not_discarded_by_map')
        records.append({'endpoint':side,'derived_source':'K_B(killed occurrence triple)',
                        'generators':len(basis),'primitive_map':'exterior inclusion into K_B(all six)',
                        'factorization_through_underived_B_sigma':'obstructed by the nine mapped Tor classes'})
    return records

def primitive_chain_equations(killed):
    S,ds,ws=branch_skeleton(killed);K,dk,wk=free_koszul()
    unknowns=[]; images=[]
    for s,n in S.items():
        for I,ni in K.items():
            a=minus(ws[s],wk[I])
            if ni==n and native(a):
                unknowns.append((s,I,a));images.append({s:{(I,a):1}})
    columns=[]; rowset=set()
    for table in images:
        residual={}
        for s in S:
            v=add(papply(dk,table.get(s,{})),scale(papply(table,ds[s]),-1))
            for (I,m),a in v.items():
                row=(s,I,m);residual[row]=a;rowset.add(row)
        columns.append(residual)
    rows=sorted(rowset,key=repr)
    M=[[col.get(r,0) for col in columns] for r in rows]
    primitive=unknowns.index((('unit',),(),ZERO))
    norm=[int(j==primitive) for j in range(len(unknowns))]
    equations=M+[norm];rhs=[0]*len(M)+[1]
    # Integral Gauss-Jordan with row provenance. A unit zero-row RHS is an exact detector.
    a=[r[:] for r in equations];b=rhs[:]
    provenance=[[int(i==j) for j in range(len(a))] for i in range(len(a))]
    row=0
    for col in range(len(unknowns)):
        hit=next((i for i in range(row,len(a)) if abs(a[i][col])==1),None)
        if hit is None:continue
        a[row],a[hit]=a[hit],a[row];b[row],b[hit]=b[hit],b[row]
        provenance[row],provenance[hit]=provenance[hit],provenance[row]
        if a[row][col]<0:
            a[row]=[-x for x in a[row]];b[row]=-b[row]
            provenance[row]=[-x for x in provenance[row]]
        for i in range(len(a)):
            if i!=row and a[i][col]:
                c=a[i][col]
                a[i]=[x-c*y for x,y in zip(a[i],a[row])];b[i]-=c*b[row]
                provenance[i]=[x-c*y for x,y in zip(provenance[i],provenance[row])]
        row+=1
    check(row==len(unknowns),'primitive_homogeneous_chain_matrix_injective')
    conflict=next((i for i in range(len(a)) if not any(a[i]) and abs(b[i])==1),None)
    check(conflict is not None,'primitive_affine_equations_inconsistent')
    detector=[b[conflict]*v for v in provenance[conflict]]
    check(all(sum(detector[i]*equations[i][j] for i in range(len(equations)))==0
              for j in range(len(unknowns))), 'affine_detector_annihilates_every_unknown')
    check(sum(x*y for x,y in zip(detector,rhs))==1,'affine_detector_reads_one')
    return {'unknowns':[repr(u) for u in unknowns],'rows':[repr(r) for r in rows]+['primitive=1'],
            'matrix':equations,'rhs':rhs,'inconsistency_detector':detector,
            'rank':row,'equations':len(equations),'new_candidate_not_ambient_forward':True}

def mixed_obstructions():
    records=[]
    for killed,side in ((EV,'plus'),(OD,'minus')):
        for e in killed:
            for o in range(6):
                if o in killed:continue
                alpha=plus(unit(e),unit(o));g,d=homogeneous_koszul(alpha)
                kappa={(e,):1};other={(o,):1}
                check(not apply(d,kappa),'mixed_Tor_class_closed')
                # Coefficients are respectively X_o k_e and X_e k_o.
                detector=lambda v:v.get((e,),0)+v.get((o,),0)
                check(all(detector(v)==0 for v in d.values()),'mixed_detector_annihilates_all_boundaries')
                check(detector(kappa)==1,'mixed_detector_primitive_value')
                sorted_I=tuple(sorted((o,e)));orientation=sgn(int(o>e))
                boundary=scale(d[sorted_I],orientation)
                check(boundary=={(e,):1,(o,):-1},'oriented_mixed_boundary_matrix')
                h,_=integral_cancel(g,d)
                check(h=={1:1},'mixed_Tor_class_integral_rank_one')
                records.append({'side':side,'killed':e,'surviving':o,'weight':alpha,
                                'basis':['X_surviving k_killed','X_killed k_surviving'],
                                'd2':[[1],[-1]],'required_rhs':[1,0],
                                'detector':[1,1],'detector_rhs':1})
    check(len(records)==18,'both_nine_mixed_obstruction_blocks')
    return records

def permute_monomial(m,p):
    out=[0]*6
    for i,a in enumerate(m):out[p[i]]=a
    return tuple(out)

def permutation_sign(xs):return sgn(sum(xs[i]>xs[j] for i in range(len(xs)) for j in range(i+1,len(xs))))

def transport_vec(v,p):
    return add(*({(tuple(sorted(p[i] for i in I)),permute_monomial(m,p)):
                     c*permutation_sign(tuple(p[i] for i in I))}
                  for (I,m),c in v.items()))

def symmetry_and_module_audit():
    K,d,w=free_koszul()
    rot=tuple((i+2)%6 for i in range(6));ref=tuple((1-i)%6 for i in range(6))
    comp=lambda a,b:tuple(a[b[i]] for i in range(6))
    ident=tuple(range(6));rr=comp(rot,rot)
    perms=(ident,rot,rr,ref,comp(rot,ref),comp(rr,ref))
    check(comp(rot,rr)==ident and comp(ref,ref)==ident and comp(ref,comp(rot,ref))==rr,
          'labelled_D3_relations')
    for p in perms:
        check(set(p)==set(range(6)),'transport_is_permutation')
        for I in K:
            lhs=transport_vec(d[I],p)
            rhs=papply(d,transport_vec({(I,ZERO):1},p))
            check(lhs==rhs,'native_target_transport_chain_equation')
        for a in perms:
            for b in perms:
                for I in SUBS:
                    v={(I,ZERO):1}
                    check(transport_vec(transport_vec(v,b),a)==transport_vec(v,comp(a,b)),
                          'exterior_transport_composition')
    for I in K:
        for j in range(6):
            v={(I,unit(j)):1}
            check(papply(d,v)==pmul(d[I],unit(j)),'full_native_B_action_differential')
    # Source relations and their primitive Tor defects transform covariantly.
    for p in perms:
        for e in EV:
            for o in OD:
                v={((e,),unit(o)):1}
                image=transport_vec(v,p)
                check(image=={((p[e],),unit(p[o])):1},'nine_relation_defects_transport')
    return {'permutations':perms,'short_diagonal_dictionary':{
        '0':'02','1':'13','2':'24','3':'35','4':'04','5':'15'},
        'reflection':'i -> 1-i mod 6; exchanges X04 and X35 and swaps endpoints',
        'physical_reflection_parity':'not assigned; external frames transported as lines'}

def endpoint_frame_audit():
    """Check the retained purity quotient, not a new purity theorem.
    This derives the sole legal endpoint row from the existing source weights.
    Every long-normal coefficient is still U_L; it is never inverted.
    """
    out=[]
    Ts=((1,3),(1,5),(3,5),(1,3,5))
    centers=subs(range(6))
    for T in Ts:
        for end,side in ((OD,'plus'),(EV,'minus')):
            for center in centers:
                legal=[]
                for z in (0,1):
                    for H in subs(end):
                        coefficient=tuple(-(1-z)*int(i in T)-int(i in H) for i in range(6))
                        allowed=min(coefficient)>=0 and all(coefficient[i]==0 for i in center)
                        if allowed:legal.append((z,H,coefficient))
                check(legal==[(1,(),ZERO)],'fixed_endpoint_frame_keeps_one_purity_row')
            out.append({'T':T,'endpoint':side,'conormal_order':end,
                        'remaining_source_row':'all six occurrence generators and z_T; empty dual-normal subset',
                        'target_row':'fully marked endpoint',
                        'coefficient':'u_D03 u_D14 u_D25',
                        'normalized_degree':0,'central_Rees_faces_checked':64})
    return out

def main(path):
    tor=koszul_audit()
    blocks=mixed_obstructions()
    source_columns={}
    systems={}
    for side,killed in (('plus',EV),('minus',OD)):
        source_columns[side]=skeleton_homology_audit(killed)
        systems[side]=primitive_chain_equations(killed)
    symmetry=symmetry_and_module_audit()
    frames=endpoint_frame_audit()
    derived_sources=derived_branch_source_audit()
    result={
        'status':'certified_obstruction_for_native_derived_pullback_target',
        'task_decision':3,
        'scope':'Canonical Y=B tensor_A^L RHom_A(G_sigma_T,V_sigma), equivalently RHom_B(Lq*G,Lq*V). No universal nonexistence claim for other native supported targets.',
        'new_vs_binding_result':'This is a native RHom_B problem with induced coefficients, not the already-falsified literal ambient/coinduced comparison.',
        'candidate':{'rings':{'A':'C[X0,...,X5]','B':'A/(X_even X_odd)','C':'spectator ring with all Rees, long occurrence and long normal parameters'},
                     'B_action':'left multiplication on B tensor K_A(X) tensor_C W, or multiplication on every base-changed endpoint stalk',
                     'cochain_model':'K_B(X0,...,X5) tensor_C W_sigma; W retains product-Cartier, normal-dual, determinant and excess labels',
                     'not_replaced_by_C':True,'not_coinduced':True,'Euler_evaluation':False,
                     'unit_normalization':'augmentation K_B -> C followed by the established primitive endpoint frame'},
        'Tor':tor,
        'derived_branch_source_control':derived_sources,
        'branch_resolution_through_degree_two':{'generator_ranks':[1,3,12],
              'computed_weight_patterns_per_endpoint':729,'homogeneous_columns':source_columns,
              'exactness_scope':'exact through degree one, suffices for necessary map equations; higher resolution cells cannot repair the displayed degree-two incompatibility'},
        'primitive_systems':systems,'first_nine_relation_blocks_per_endpoint':blocks,
        'symmetry':symmetry,'endpoint_frames':frames,
        'first_equation':{'matrix':[[1],[-1]],'rhs':[1,0],'detector':[1,1],
                          'value_on_boundaries':0,'value_on_required_primitive':1},
        'primitive_underlying_coefficient_class':'exists in Y and survives augmentation; fails to extend to a native branch-source morphism',
        'operation_intertwiners':'not reached: primitive native map fails in all nine mixed relation blocks',
        'outer_Q_symmetry':'not reached for this candidate; no physical vector fields inferred from associative operations',
        'three_layer_maps':'not constructed, conditional gates fail earlier',
        'alternative_targets':'not excluded, including D35 with a separately supplied native action and source mate',
        'new_assertions':dict(sorted(CHECKS.items())), 'total_new_assertions':sum(CHECKS.values()),
        'verification':'Independent standard-library finite chain calculation. All-exponent proof in companion note. No proof-assistant verification.'
    }
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'status':result['status'],'checks':result['total_new_assertions'],
                      'Tor':tor['homological_Tor_ranks'],
                      'primitive_systems':{s:{k:v[k] for k in ('rank','equations')} for s,v in systems.items()}},indent=2))

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path('marici_native_pullback_obstruction_certificate.json'))
    args=parser.parse_args();main(args.output)
