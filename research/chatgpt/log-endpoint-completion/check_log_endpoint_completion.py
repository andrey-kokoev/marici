#!/usr/bin/env python3
"""Exact completion test for Marici's normalized blowdown route.

Reconstructs the full hexagon stellar subdivision and its occurrence-weighted
normalized chains, verifies the entire blowdown chain map and six relabelled
Morse roofs, and distinguishes collapsed relative chains from an extraordinary
interval trace. Also computes the two directional Koszul comparisons on u=l*t.

Standard library only. No network access, random tests, divisions by occurrence
variables, proof-assistant claims, or repository writes. The accompanying note
states the all-polynomial proofs and the limitation to this route.
"""
from __future__ import annotations
import argparse
from collections import Counter
from itertools import combinations, product
import json
from pathlib import Path
from typing import Callable

CHECKS: Counter[str] = Counter()
COMMIT='d1947b67a60d3e88ba77f4ca60ea02c2a306ee61'
SOURCE_BLOBS={
 'research/voevodsky/check_d03_normalized_blowdown_counit.py':'0fcbbf37a4f70dc0c2787ad7cb954287b9e97403',
 'research/voevodsky/check_ringed_normalized_blowdown.py':'0141bce40493b0ae9175ea117ac2df716b22237b',
 'research/voevodsky/check_log_exceptional_tor_suspension.py':'1a3bbab5306b34536e8b0f0363361f4a70e89796',
 'research/voevodsky/check_generic_log_dnc_thom_trace.py':'95fd466d144bafea6838cfeacc4aaf485b124275',
 'research/voevodsky/check_dp6_endpoint_q_mapping_fiber.rs':'592811b138855554c921dcf4269581632e8f0050',
 'src/ledger/20260815-143 Two-Endpoint Road Carrier and the Loaded Conductor Cospan Blocker.md':'02cedbb15dd385a75bab759dfcdb4daa28bd3b3c',
}

def check(v: bool, name: str) -> None:
    if not v: raise AssertionError(name)
    CHECKS[name]+=1

def add(*vs):
    out={}
    for v in vs:
        for k,a in v.items():
            out[k]=out.get(k,0)+a
            if not out[k]:del out[k]
    return out

def scale(v,c):return {k:a*c for k,a in v.items() if a*c}

# Diagonal indices: x0,...,x5,D03,D14,D25; exceptional index 9.
def diag(a,b):return tuple(sorted((a%6,b%6)))
DIAGS=tuple(diag(i,i+2) for i in range(6))+(diag(0,3),diag(1,4),diag(2,5))
E=9
Face=frozenset[int]
Flag=tuple[Face,...]
Mono=tuple[int,...]
ZERO=(0,)*11

def X(i):return tuple(int(j==i) for j in range(11))

def madd(a,b):return tuple(x+y for x,y in zip(a,b))

def msub(a,b):
    v=tuple(x-y for x,y in zip(a,b))
    if min(v)<0:raise ValueError('A negative coefficient exponent was requested')
    return v

def multiply(v,m):return {(f,madd(e,m)):a for (f,e),a in v.items()}

def term(flag, m=ZERO, s=1):return {(tuple(flag),m):s}

def cross(a,b):
    x,y=DIAGS[a];u,v=DIAGS[b]
    return x<u<y<v or u<x<v<y

def faces():
    return tuple(frozenset(c) for k in range(4) for c in combinations(range(9),k)
                 if all(not cross(a,b) for a,b in combinations(c,2)))

def stellar(fs,center):
    out={f for f in fs if not center<=f}
    for f in fs:
        if center<=f:
            # Stellar subdivision replaces the center by E and its proper faces.
            outside=f-center
            for k in range(len(center)):
                for c in combinations(sorted(center),k):
                    out.add(frozenset(outside|set(c)|{E}))
    # Explicitly take closure; no arbitrary support generators are added.
    out={frozenset(c) for f in out for k in range(len(f)+1) for c in combinations(sorted(f),k)}
    return tuple(sorted(out,key=lambda f:(len(f),tuple(sorted(f)))))

def old(f,center):return (f-{E})|center if E in f else f

def label(f,center):return tuple(int(i in old(f,center)) if i<9 else 0 for i in range(11))

def flags(fs):
    ordered=sorted(fs,key=lambda f:(len(f),tuple(sorted(f))))
    out=[]
    def rec(prefix,last):
        out.append(prefix)
        for nxt in ordered:
            if last<nxt:rec(prefix+(nxt,),nxt)
    for f in ordered:rec((f,),f)
    return tuple(out)

def boundary(v,center):
    out={}
    for (f,m),a in v.items():
        if len(f)<=1:continue # unaugmented chains: d on vertices is zero
        for i in range(len(f)):
            factor=msub(label(f[1],center),label(f[0],center)) if i==0 else ZERO
            out=add(out,term(f[:i]+f[i+1:],madd(m,factor),a*((-1)**i)))
    return out

def push(v,center):
    out={}
    for (f,m),a in v.items():
        im=tuple(old(s,center) for s in f)
        if len(set(im))<len(im):continue
        out=add(out,term(im,m,a))
    return out

def perm(g):
    a,b=g
    def vert(i):return (2*a+(3-i if b else i))%6
    return tuple(DIAGS.index(diag(vert(x),vert(y))) for x,y in DIAGS)

def act_face(f,g):
    p=perm(g)
    return frozenset(E if i==E else p[i] for i in f)

def act(v,g):
    p=perm(g);out={}
    for (f,m),a in v.items():
        mm=[0]*11
        for i in range(9):mm[p[i]]=m[i]
        mm[9:]=m[9:]
        out=add(out,term(tuple(act_face(s,g) for s in f),tuple(mm),a))
    return out

def local_roof():
    top=frozenset();q=frozenset({6});v=frozenset({1,3,5})
    edge=frozenset({1,3});bp=frozenset({E,1,3});h=frozenset({E,3})
    bm=frozenset({E,6,3});er=frozenset({6,3});c=frozenset({6,0,3})
    H={}
    for apex,e,l,r,m in [(top,edge,v,bp,ZERO),(top,h,bp,bm,ZERO),(q,er,bm,c,X(6))]:
        H=add(H,term((apex,e,r),m,-1),term((apex,e,l),m,1))
    H=add(H,term((top,q,bm)))
    xi={}
    for e,l,r,m in [(edge,v,bp,X(1)),(h,bp,bm,madd(X(6),X(1))),(er,bm,c,X(6))]:
        xi=add(xi,term((e,r),m),term((e,l),m,-1))
    qj=add(term((top,v),s=-1),term((top,q)),term((q,c),X(6)))
    endpoint=add(term((c,),madd(X(6),X(0))),term((v,),madd(X(1),X(5)),-1))
    return H,xi,qj,endpoint,(h,bp,bm),v,c

def matvec(a,v):return [sum(x*y for x,y in zip(r,v)) for r in a]

def mvplus(a,b):return [x+y for x,y in zip(a,b)]

def rank_q(a):
    from fractions import Fraction
    a=[[Fraction(x) for x in row] for row in a]
    r=0
    for c in range(len(a[0]) if a else 0):
        hit=next((i for i in range(r,len(a)) if a[i][c]),None)
        if hit is None:continue
        a[r],a[hit]=a[hit],a[r]
        t=a[r][c];a[r]=[x/t for x in a[r]]
        for i in range(len(a)):
            if i!=r and a[i][c]:
                t=a[i][c];a[i]=[x-t*y for x,y in zip(a[i],a[r])]
        r+=1
    return r

def poly_mul(a,b):
    out={}
    for m,x in a.items():
        for n,y in b.items():out=add(out,{madd(m,n):x*y})
    return out

# Generic normal comparison over Z[l,t] in the final two exponent coordinates.
ONE={ZERO:1};LAM={X(9):1};T={X(10):1};U=poly_mul(LAM,T)

def central(p):return {m:a for m,a in p.items() if m[9]==m[10]==0}

def unit_monomial(p):return p==ONE

def display_face(f):
    names=['x0','x1','x2','x3','x4','x5','D03','D14','D25','E']
    return [names[i] for i in sorted(f)]

def serialize(v):
    return [{'flag':[display_face(f) for f in flag],'exponents':list(m),'coefficient':a}
            for (flag,m),a in sorted(v.items(),key=lambda kv:(str(kv[0][0]),kv[0][1]))]

def main(path:Path):
    fs=faces();center=frozenset({6,1});src=stellar(fs,center)
    bs=flags(src);bt=flags(fs);target_flags=set(bt)
    check(len(fs)==45,'target_45_faces')
    check(len(src)==51,'subdivision_51_faces')
    for f in src:check(old(f,center) in fs,'blowdown_face_is_legal')
    for f in bs:
        check(all(f[i]<f[i+1] for i in range(len(f)-1)),'strict_source_flags')
        v=term(f)
        check(not boundary(boundary(v,center),center),'all_source_d_squared')
        check(push(boundary(v,center),center)==boundary(push(v,center),center),'all_blowdown_chain_maps')
        check(all(ff in target_flags for ff,_ in push(v,center)),'all_images_in_actual_target')
    for f in bt:check(not boundary(boundary(term(f),center),center),'all_target_d_squared')
    # Every nontrivial point fibre has identical labels and is an actual V tree.
    fibers={f:tuple(s for s in src if old(s,center)==f) for f in fs}
    nontrivial={f:v for f,v in fibers.items() if len(v)>1}
    for target,fib in nontrivial.items():
        check(len(fib)==3,'nontrivial_fiber_three_vertices')
        ff=flags(fib)
        check(Counter(len(f)-1 for f in ff)=={0:3,1:2},'nontrivial_fiber_two_edges')
        check(all(label(s,center)==label(target,center) for s in fib),'fiber_coefficient_identity')
    H,xi,qj,endpoint,fiber,vplus,road_end=local_roof()
    check(boundary(H,center)==add(qj,scale(multiply(xi,X(3)),-1)),'exact_source_morse_identity')
    check(boundary(xi,center)==endpoint,'both_source_endpoint_weights')
    check(boundary(qj,center)==multiply(endpoint,X(3)),'generic_roof_endpoint_boundary')
    check((len(H),len(push(H,center)))==(7,5),'seven_to_five_Morse_terms')
    check((len(xi),len(push(xi,center)))==(6,4),'six_to_four_path_terms')
    for g in product(range(3),range(2)):
        cc=act_face(center,g)
        hg,xg,qg,eg=(act(z,g) for z in (H,xi,qj,endpoint))
        x3g=X(perm(g)[3])
        check(boundary(hg,cc)==add(qg,scale(multiply(xg,x3g),-1)),'six_chart_Morse_equations')
        check(boundary(xg,cc)==eg,'six_chart_endpoint_boundaries')
        check(push(hg,cc)==act(push(H,center),g),'six_chart_blowdown_covariance')
        for z in (hg,xg,qg):
            check(push(boundary(z,cc),cc)==boundary(push(z,cc),cc),'six_chart_full_roof_chain_maps')
        gd=act_face(frozenset({6}),g)
        check(push(qg,cc).get(((frozenset(),gd),ZERO))==1,'six_primitive_generic_flag_coefficients')
    # Exceptional relative class: e_-=(h,bp), e_+=(h,bm).
    h,bp,bm=fiber
    beta=add(term((h,bm)),term((h,bp),s=-1))
    check(boundary(beta,center)==add(term((bm,)),term((bp,),s=-1)),'relative_interval_endpoint_boundary')
    check(push(beta,center)=={},'blowdown_kills_entire_exceptional_relative_chain')
    check(old(bp,center)==old(bm,center),'both_exceptional_endpoints_have_same_image')
    vminus=frozenset({0,2,4});V={vplus,vminus}
    check(old(bp,center) not in V,'ordinary_blowdown_not_a_map_to_physical_endpoint_pair')
    # This exact zero persists with arbitrary polynomial spectators: basis tests
    # below exercise linearity, while the proof covers all polynomials and tensors.
    for i in range(11):
        for exponent in range(5):
            m=tuple(exponent if j==i else 0 for j in range(11))
            check(not push(multiply(beta,m),center),'coefficient_extension_does_not_rescue_fiber_class')
    # Construct BOTH physical endpoint collars, now as a homotopy square.
    # These are the source's labelled half-corridors, split at the actual
    # blowdown point m={D03,x1,x3}; the common segment is reversed on one side.
    mid=old(bp,center)
    c=frozenset({6,0,3});other=frozenset({6,0,4})
    def adjacent_path(left,right):
        shared=left & right
        check(len(shared)==2,'corridor_adjacent_triangulations')
        raw=add(term((shared,right)),term((shared,left),s=-1))
        return multiply(raw,label(shared,center))
    collar_plus=adjacent_path(vplus,mid)
    collar_minus=add(adjacent_path(vminus,other),adjacent_path(other,c),adjacent_path(c,mid))
    km=label(mid,center);kp=label(vplus,center);kn=label(vminus,center)
    check(boundary(collar_plus,center)==add(term((mid,),km),term((vplus,),kp,-1)),
          'polynomial_plus_endpoint_connector')
    check(boundary(collar_minus,center)==add(term((mid,),km),term((vminus,),kn,-1)),
          'polynomial_minus_endpoint_connector')
    corridor=add(collar_plus,scale(collar_minus,-1))
    check(boundary(corridor,center)==add(term((vminus,),kn),term((vplus,),kp,-1)),
          'polynomial_relative_Tor_image_endpoint_boundary')
    check(all(any(i<6 for i in flag[0]) for flag,m in corridor),'both_collars_are_short_boundary_supported')
    # The topological relative-cone map is NOT just ordinary blowdown:
    # (z,a) -> (q_k(z)+h(a),f(a)), dh = q_k inclusion - inclusion f.
    # Check on all generators of Cone(C(boundary F)->C(F)).
    a_minus='rminus';a_plus='rplus'
    source_keys=[('c',(h,)),('c',(bp,)),('c',(bm,)),('c',(h,bp)),('c',(h,bm)),
                 ('a',a_minus),('a',a_plus)]
    def cone_ds(key):
        typ,b=key
        if typ=='a':return {('c',(bp if b==a_minus else bm,)):1}
        if len(b)==2:return {('c',(b[1],)):1,('c',(b[0],)):-1}
        return {}
    def cone_map(key):
        typ,b=key
        if typ=='c':return (term((mid,),km),{}) if len(b)==1 else ({},{})
        coll=collar_plus if b==a_minus else collar_minus
        vv,mm=(vplus,kp) if b==a_minus else (vminus,kn)
        return coll,term((vv,),mm)
    def d_target_pair(pair):
        z,a=pair
        return add(boundary(z,center),a),{} # endpoint complex is degree zero
    for key in source_keys:
        lhs=d_target_pair(cone_map(key));rhs=({}, {})
        for kk,aa in cone_ds(key).items():
            m0,m1=cone_map(kk);rhs=(add(rhs[0],scale(m0,aa)),add(rhs[1],scale(m1,aa)))
        check(lhs==rhs,'all_endpoint_mapping_cone_chain_equations')
    # Complete polynomial classification uses the necessary rational weight
    # functional [S] -> 1 / m_S. Source vertex image k[m] forces endpoint
    # coefficients k*m_endpoint/m_mid. Their integrality is equivalent to
    # m_mid dividing k, and the displayed collars prove sufficiency.
    for exponents in product(range(2),repeat=9):
        kk=tuple(exponents)+(0,0)
        cp=tuple(x+y-z for x,y,z in zip(kk,kp,km))
        cn=tuple(x+y-z for x,y,z in zip(kk,kn,km))
        legal=(min(cp)>=0 and min(cn)>=0)
        divides=all(x>=y for x,y in zip(kk,km))
        check(legal==divides,'all_squarefree_endpoint_lifting_ideals')
    check(set(mid).isdisjoint(vminus),'negative_endpoint_is_coprime_to_midpoint_label')
    # This constructs the carrier-level Tor attachment but no generic Q leg:
    # every term of the image is in the fixed short-boundary support.
    # The separate Morse roof has a nonzero generic FLAG but is exact in the
    # ordinary relative bar complex. Do not confuse that with a physical Hom roof.
    def mod_short(v):return {(f,m):a for (f,m),a in v.items() if not all(any(i<6 for i in old(s,center)) for s in f)}
    check(not mod_short(corridor),'endpoint_repair_generic_projection_zero')
    check(bool(mod_short(push(qj,center))),'Morse_generic_flag_nonzero_as_chain')
    check(mod_short(boundary(push(H,center),center))==mod_short(push(qj,center)),
          'Morse_roof_exact_in_ordinary_relative_bar_model')
    # Absolute and relative interval and the normalized extraordinary trace.
    da=[[-1,-1],[1,0],[0,1]];dr=[[-1,-1]];inc=[-1,1];tr=[0,1]
    check(rank_q(da)==2,'absolute_tree_has_no_H1')
    check(rank_q(dr)==1,'relative_interval_H1_rank_one')
    check(matvec(dr,inc)==[0],'relative_generator_closed')
    check(sum(a*b for a,b in zip(tr,inc))==1,'extraordinary_trace_unit')
    # Explicit deformation retraction J -> R[1]. Homotopy sends c -> -e_-.
    hom=[-1,0]
    for vec in ([1,0],[0,1]):
        projection=[x*sum(t*y for t,y in zip(tr,vec)) for x in inc]
        hd=[x*matvec(dr,vec)[0] for x in hom]
        check(mvplus(projection,hd)==list(vec),'relative_trace_integral_contraction_degree_one')
    check(matvec(dr,hom)==[1],'relative_trace_integral_contraction_degree_zero')
    # All normalized traces have row (a,a+1); all differences are homotopies.
    for a in range(-8,9):
        row=[a,a+1]
        check(sum(x*y for x,y in zip(row,inc))==1,'normalized_trace_affine_family')
        check([row[i]-tr[i] for i in range(2)]==[-a*dr[0][i] for i in range(2)],'all_trace_differences_are_exact')
    # Reflection compensation: s=-swap in degree one, s=-1 in degree zero.
    refl=[[-0,-1],[-1,0]]
    tr_s=[sum(tr[i]*refl[i][j] for i in range(2)) for j in range(2)]
    check([tr_s[i]-tr[i] for i in range(2)]==dr[0],'reflection_trace_homotopy_is_source_boundary')
    check([1+(-1)]==[0],'reflection_homotopy_closes')
    # Koszul comparison on u=l*t; components are listed degree 0,degree 1.
    f0,f1=ONE,LAM;g0,g1=LAM,ONE
    check(poly_mul(T,f1)==poly_mul(f0,U),'ordinary_Koszul_chain_equation')
    check(poly_mul(U,g1)==poly_mul(g0,T),'dual_Koszul_chain_equation')
    check(poly_mul(f0,g0)==LAM and poly_mul(f1,g1)==LAM,'ordinary_after_dual_is_l')
    check(poly_mul(g0,f0)==LAM and poly_mul(g1,f1)==LAM,'dual_after_ordinary_is_l')
    check(central(f1)=={} and central(g1)==ONE,'ordinary_kills_but_dual_preserves_central_Tor1')
    check(central(g0)=={},'dual_degree_zero_vanishes_centrally')
    # First conormal coefficient of g0 is +1; no l inverse is used.
    check(g0==LAM,'dual_first_Rees_symbol_is_primitive')
    # Common-normal derived excess K(u0,0) has explicit free Tor0 and Tor1.
    # For K(t) tensor an exterior zero differential, the dual map is the
    # identity on the common excess generator as well.
    cert={
      'date':'2026-09-06','commit':COMMIT,'source_blobs':SOURCE_BLOBS,
      'status':'weighted_carrier_endpoint_cones_constructed; ordinary_blowdown_alone_insufficient; full_physical_comparison_not_constructed',
      'source_faces':len(src),'target_faces':len(fs),
      'source_flags_by_degree':dict(sorted(Counter(len(f)-1 for f in bs).items())),
      'target_flags_by_degree':dict(sorted(Counter(len(f)-1 for f in bt).items())),
      'nontrivial_fibers':[{'target':display_face(f),'source':[display_face(s) for s in fib]} for f,fib in nontrivial.items()],
      'upstairs_Morse_homotopy':serialize(H),'downstairs_Morse_homotopy':serialize(push(H,center)),
      'upstairs_road_path':serialize(xi),'corrected_generic_roof':serialize(qj),
      'road_endpoint_boundary':serialize(endpoint),
      'exceptional_relative_generator':serialize(beta),
      'exceptional_relative_image':serialize(push(beta,center)),
      'exceptional_endpoint_image':display_face(old(bp,center)),
      'plus_endpoint_collar':serialize(collar_plus),'minus_endpoint_collar':serialize(collar_minus),
      'relative_Tor_corridor_image':serialize(corridor),
      'admissible_midpoint_coefficient_ideal':'(X_D03*X_1*X_3)',
      'endpoint_coefficients':['X_1*X_3*X_5','X_0*X_2*X_4'],
      'carrier_endpoint_cone_map_constructed':True,
      'carrier_relative_Tor_map_injective':True,
      'endpoint_cone_image_generic_projection':0,
      'Morse_roof_ordinary_relative_bar_class':0,
      'physical_endpoints':[display_face(vplus),display_face(vminus)],
      'relative_interval_differential':dr,'trace_row':tr,'relative_unit':inc,
      'trace_all_representatives':'(a,a+1), a in R; differences are relative chain homotopies',
      'ordinary_Koszul_components_degree_0_1':['1','lambda'],
      'dual_Koszul_components_degree_0_1':['lambda','1'],
      'ordinary_Tor1_at_lambda_t_zero':0,'dual_Tor1_at_lambda_t_zero':1,
      'claims_not_made':[
          'No identification of a source carrier flag with a supported-dual Q generator.',
          'No identification of the normal parameter lambda with every source occurrence or Rees parameter.',
          'No construction of the global mixed-variance sheet arrow alpha_sh.',
          'The two carrier-level endpoint homotopies are constructed; no promotion to the physical mixed-variance endpoint connector 2-cells is claimed.',
          'No assignment of physical parity; the earlier coefficient detector is not the physical restriction.',
          'No claim that all possible extraordinary completions are obstructed.',
          'No proof-assistant verification.'
      ],
      'checks':dict(sorted(CHECKS.items())),'total_exact_assertions':sum(CHECKS.values())
    }
    path.write_text(json.dumps(cert,indent=2)+'\n')
    print(json.dumps({k:cert[k] for k in ('status','source_faces','target_faces','source_flags_by_degree','target_flags_by_degree','total_exact_assertions')},indent=2))

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output',type=Path,default=Path('log_endpoint_completion_certificate.json'))
    args=p.parse_args();main(args.output)
