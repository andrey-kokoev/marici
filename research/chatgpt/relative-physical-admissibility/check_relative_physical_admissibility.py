#!/usr/bin/env python3
"""Relative coherence detector and labelled generic-Q support tests.

Standard library only. Reuses the explicitly retrieved polynomial endpoint
model (pinned Marici commit recorded below), then independently constructs
all coherent lifts, the strict obstruction lattice, and negative controls.
No averaging, denominator inversion, new homotopy generators, or repository
writes are used. Arbitrary-degree claims are proved in the accompanying note.
"""
from __future__ import annotations
import argparse
from collections import Counter
from pathlib import Path
import json
from typing import TypeAlias

Key: TypeAlias = tuple[str, str, int]
Vector: TypeAlias = dict[Key, int]
COUNTS: Counter[str] = Counter()
COMMIT = 'd1947b67a60d3e88ba77f4ca60ea02c2a306ee61'
SOURCES = {
    'research/voevodsky/check_normalization_conductor_bimodule_kernel.py': '2982163ca939dd1e09bb0b66b4229e31430e3c30',
    'research/voevodsky/check_conductor_road_endpoint_pullback.rs': 'cfe13e928e911f8914de6670f34cc4c8859b3402',
    'research/voevodsky/check_physical_derived_pullback_after_transform.py': '7993b2b1bbdba03d05c3f443a45717d7b8efeec5',
    'research/voevodsky/check_multirees_conductor_stalk_kernel.py': '1237d71e8c9fd56e064226825049d84dd03f42e2',
    'research/voevodsky/check_global_mixed_variance_transform.py': '3b23d8a71a374435e8f54d4fe9451a08cb8ab98e',
}

def check(value: bool, label: str) -> None:
    if not value:
        raise AssertionError(label)
    COUNTS[label] += 1


def add(*terms: Vector) -> Vector:
    out: Vector = {}
    for term in terms:
        for k, c in term.items():
            out[k] = out.get(k, 0) + c
            if not out[k]:
                del out[k]
    return out


def scale(v: Vector, c: int) -> Vector:
    return {k: c*a for k, a in v.items() if c*a}


def lift(fn, v: Vector) -> Vector:
    out: Vector = {}
    for k, a in v.items():
        out = add(out, scale(fn(k), a))
    return out


def one(k: Key) -> Vector:
    return {k: 1}


def degree(k: Key) -> int:
    return {'o': 0, 's': 1, 'q': 1, 'a': 2, 't': 2, 'z': 3}[k[0]]


def basis(n: int) -> list[Key]:
    return ([('o','',0), ('z','',0), ('a','c',0)]
            + [('s',b,j) for b in ('x','y') for j in range(n+1)]
            + [('a',b,j) for b in ('x','y') for j in range(1,n+1)]
            + [(b,'',j) for b in ('q','t') for j in range(3)])


def differential(k: Key) -> Vector:
    typ, branch, n = k
    if typ == 'z':
        return {('t','',j): 1 for j in range(3)}
    if typ == 'a':
        if branch == 'c':
            return {('s','x',0):1, ('s','y',0):1}
        return {('s',branch,n):1}
    if typ == 't':
        return {('q','',n):1, ('q','',(n+1)%3):-1}
    if typ == 's':
        return {('o','',0): 1 if branch == 'x' else -1} if n == 0 else {}
    if typ == 'q':
        return {('o','',0):-1}
    return {}


def projection(k: Key) -> Vector:
    typ, branch, n = k
    return {} if typ in ('a','s') and n > 0 else one(k)


def homotopy(k: Key) -> Vector:
    typ, branch, n = k
    return {('a',branch,n):1} if typ == 's' and n > 0 else {}


def rotation(k: Key) -> Vector:
    typ, b, n = k
    return {(typ,b,(n+1)%3):1} if typ in ('q','t') else one(k)


def reflection(k: Key) -> Vector:
    typ, b, n = k
    if typ in ('s','a') and b in ('x','y'):
        return {(typ, 'y' if b == 'x' else 'x', n):1}
    if typ == 'q':
        return {(typ,b,(-n)%3):-1}
    if typ == 't':
        return {(typ,b,(-n-1)%3):1}
    if typ == 'o':
        return {k:-1}
    return one(k)


def branch_multiply(k: Key, b: str) -> Vector:
    """Action of x or y as an A-module; conductor/road modules have x=y=0."""
    typ, branch, n = k
    if typ == 'a' and branch == 'c':
        return {('a',b,1):1}
    if typ in ('a','s') and branch == b:
        return {(typ,b,n+1):1}
    return {}


def readout(v: Vector) -> int:
    return sum(a for (typ,_,_),a in v.items() if typ == 'q')


def node(c: int, x: dict[int,int], y: dict[int,int]) -> Vector:
    out = {('a','c',0):c} if c else {}
    for b,terms in [('x',x),('y',y)]:
        for n,a in terms.items():
            if n < 1:
                raise ValueError('A positive branch term must have degree at least one')
            if a:
                out[('a',b,n)] = a
    return out


def cycle_from_data(k: int, common: int, q1: int, q2: int,
                    x: dict[int,int], y: dict[int,int]) -> tuple[Vector,Vector]:
    """Return a cycle and a witness for reduction to k times the primitive."""
    q0=k-q1-q2
    sheet = {('s','x',0):common+k, ('s','y',0):common}
    sheet = {a:b for a,b in sheet.items() if b}
    for branch,terms in [('x',x),('y',y)]:
        for n,c in terms.items():
            if c:
                sheet[('s',branch,n)]=c
    roads={('q','',j):q for j,q in enumerate((q0,q1,q2)) if q}
    tags={('t','',1):q1, ('t','',2):q1+q2}
    tags={a:b for a,b in tags.items() if b}
    witness=add(node(common,x,y),tags)
    return add(sheet,roads),witness


from fractions import Fraction
from itertools import product, combinations
from math import gcd
from functools import reduce
import hashlib

Group = tuple[int, int]
GROUP: tuple[Group, ...] = tuple(product(range(3), range(2)))
IDENTITY: Group = (0, 0)
ROT: Group = (1, 0)
REFL: Group = (0, 1)
DIAG: Key = ('a','c',0)
TOP: Key = ('z','',0)
Z: Vector = {('s','x',0):1, ('q','',0):1}


def mul(g: Group, h: Group) -> Group:
    return ((g[0] + (-1)**g[1]*h[0]) % 3, (g[1]+h[1]) % 2)


def chi(g: Group) -> int:
    return (-1)**g[1]


def star(g: Group, v: Vector) -> Vector:
    """Source action tensored with its once-relative orientation character."""
    if g[1]:
        v = scale(lift(reflection, v), -1)
    for _ in range(g[0]):
        v = lift(rotation, v)
    return v


def d(v: Vector) -> Vector:
    return lift(differential, v)


def edge_h(g: Group) -> Vector:
    i,e = g
    return add({DIAG:-e} if e else {}, {('t','',j):-1 for j in range(i)})


def carry(g: Group, h: Group) -> int:
    return -((g[0]+chi(g)*h[0]) // 3)


def face_k(g: Group, h: Group) -> Vector:
    n = carry(g,h)
    return {TOP:n} if n else {}


def defect(g: Group) -> Vector:
    return add(star(g,Z), scale(Z,-1))


def contract_cycle(v: Vector) -> Vector:
    """On cycles: d H0(v)=v-readout(v) Z. No division is needed."""
    if d(v):
        raise ValueError('contract_cycle requires an endpoint cycle')
    ans: Vector = {}
    c = v.get(('s','y',0),0)
    if c: ans[DIAG]=c
    for (kind,b,n),a in v.items():
        if kind=='s' and n>0: ans[('a',b,n)]=a
    q1=v.get(('q','',1),0)
    q2=v.get(('q','',2),0)
    if q1: ans[('t','',1)]=q1
    if q1+q2: ans[('t','',2)]=q1+q2
    return ans


def contract_relations(v: Vector) -> Vector:
    """On P2: H1(v)=t0 times the existing norm generator."""
    if any(degree(x)!=2 for x in v):
        raise ValueError('contract_relations requires degree-two input')
    t0 = v.get(('t','',0),0)
    return {TOP:t0} if t0 else {}


def determinant(a: list[list[int]]) -> int:
    if not a: return 1
    if len(a)==1: return a[0][0]
    return sum((-1)**j*a[0][j]*determinant([r[:j]+r[j+1:] for r in a[1:]]) for j in range(len(a)))


def invariant_factors(a: list[list[int]]) -> list[int]:
    """Small integer matrix Smith factors from determinantal divisors."""
    rows,cols=len(a),len(a[0])
    previous=1; out=[]
    for k in range(1,min(rows,cols)+1):
        minors=(abs(determinant([[a[i][j] for j in jj] for i in ii]))
                for ii in combinations(range(rows),k) for jj in combinations(range(cols),k))
        value=reduce(gcd,minors,0)
        if not value: break
        if value % previous: raise ArithmeticError('Invalid determinantal divisor')
        out.append(value//previous); previous=value
    return out


def encode(v: Vector) -> list[dict]:
    return [{'basis':list(k),'coefficient':a} for k,a in sorted(v.items())]



# D has the sign module in marking-chain degrees 1 and 2 and zero differential.
def detector(v: Vector) -> tuple[int,int]:
    return (v.get(DIAG,0),v.get(TOP,0))


def alpha(g: Group) -> int:
    return -g[1]


def db0(c: int, g: Group) -> int:
    return (chi(g)-1)*c


def db1(f, g: Group, h: Group) -> int:
    return chi(g)*f(h)-f(mul(g,h))+f(g)


def db2(f, g: Group, h: Group, k: Group) -> int:
    return chi(g)*f(h,k)-f(mul(g,h),k)+f(g,mul(h,k))-f(g,h)


# Sparse Laurent polynomials in nine X variables, nine normals, and an independent x3.
# No normal inverses are allowed in a coefficient unless its stalk permits them.
Exp=tuple[int,...]
Poly=dict[Exp,int]
ZERO_EXP=(0,)*19

def pol(c=1, exp=ZERO_EXP):
    return {exp:c} if c else {}

def padd(*ps):
    out={}
    for p in ps:
        for e,c in p.items():
            out[e]=out.get(e,0)+c
            if out[e]==0: del out[e]
    return out

def pscale(p,n): return {e:n*c for e,c in p.items() if n*c}

def pmul(a,b):
    out={}
    for e,c in a.items():
        for f,k in b.items():
            g=tuple(x+y for x,y in zip(e,f))
            out[g]=out.get(g,0)+c*k
            if not out[g]: del out[g]
    return out

def mono(changes):
    e=[0]*19
    for i,n in changes.items(): e[i]=n
    return pol(1,tuple(e))

def poly_in_stalk(p, allowed):
    return all(all(n>=0 for n in e[:9]) and
               all(n>=0 or i in allowed for i,n in enumerate(e[9:18])) and e[18]>=0 for e in p)

def cvadd(*vs):
    out={}
    for v in vs:
        for k,p in v.items():
            out[k]=padd(out.get(k,{}),p)
            if not out[k]: del out[k]
    return out

def cvscale(v,p): return {k:pmul(a,p) for k,a in v.items() if pmul(a,p)}

def cvapply(d,v):
    ans={}
    for k,p in v.items(): ans=cvadd(ans,cvscale(d[k],p))
    return ans

def normalize_diag(i,j): return tuple(sorted((i%6,j%6)))

def crosses(a,b):
    x,y=a;u,v=b
    return x<u<y<v or u<x<v<y

def k6_source():
    diagonals=tuple((i,j) for i in range(6) for j in range(i+1,6) if j-i not in (1,5))
    shorts=tuple(normalize_diag(i,i+2) for i in range(6))
    longs=tuple(normalize_diag(i,i+3) for i in range(3))
    ix={d:i for i,d in enumerate(shorts+longs)}
    faces=tuple(f for k in range(4) for f in combinations(diagonals,k)
                if all(not crosses(a,b) for a,b in combinations(f,2)))
    cells=tuple((f,m) for f in faces for k in range(len(f)+1) for m in combinations(f,k))
    vp=set(shorts[i] for i in (1,3,5));vm=set(shorts[i] for i in (0,2,4))
    V={c for c in cells if set(c[0]) in (vp,vm)}
    B={c for c in cells if any(d in shorts for d in c[0])}
    absd={};cechd={}
    for cell in cells:
        f,m=cell;a={};c={}
        for d in diagonals:
            if d not in f and all(not crosses(d,e) for e in f):
                target=(tuple(sorted(f+(d,))),m)
                sign=(-1)**sum(e<d for e in f);j=ix[d]
                a[target]=pscale(mono({j:1}),sign)
                c[target]=pscale(mono({j:1,j+9:-1}),sign)
        for pos,d in enumerate(m):
            target=(f,tuple(x for x in m if x!=d));sign=(-1)**(3-len(f)+pos);j=ix[d]
            a[target]=pscale(mono({j+9:1}),sign)
            c[target]=pol(sign)
        absd[cell]=a;cechd[cell]=c
    def lam(cell):
        f,m=cell
        return mono({ix[d]+9:-1 for d in f if d not in m})
    for cell in cells:
        check(not cvapply(absd,absd[cell]),'all_215_absolute_d_squared')
        check(not cvapply(cechd,cechd[cell]),'all_215_cech_d_squared')
        left=cvscale(cechd[cell],lam(cell))
        right={t:pmul(p,lam(t)) for t,p in absd[cell].items()}
        check(left==right,'all_215_kappa_chain_comparison')
        for t,p in cechd[cell].items():
            allowed={ix[d] for d in t[0] if d not in t[1]}
            check(poly_in_stalk(p,allowed),'target_stalk_denominator_admissibility')
        for support,name in [(V,'endpoints'),(B,'short_boundary')]:
            if cell in support:
                check(set(cechd[cell])<=support,'strict_support_'+name)
    qcells=set(cells)-B
    qd={cell:{t:p for t,p in cechd[cell].items() if t in qcells} for cell in qcells}
    check((len(cells),len(V),len(B),len(qcells))==(215,16,208,7),'source_support_counts')
    q3=[c for c in qcells if 3-len(c[0])+len(c[1])==3]
    q2=[c for c in qcells if 3-len(c[0])+len(c[1])==2]
    check((len(q3),len(q2))==(4,3),'seven_generator_Q_degrees')
    top=((),());normals=[((d,),(d,)) for d in longs];facets=[((d,),()) for d in longs]
    for i in range(3):
        check(qd[normals[i]]=={facets[i]:pol()},'Q_normal_is_localization_inclusion')
        check(qd[top][facets[i]]==mono({ix[longs[i]]:1,ix[longs[i]]+9:-1}),
              'Q_top_prescribed_X_over_u')
    return dict(ix=ix,longs=longs,top=top,normals=normals,facets=facets,qd=qd,
                cells=cells,cechd=cechd)


def main(output: Path, max_degree: int) -> None:
    COUNTS.clear()
    # Check the old full lift before imposing new relative data.
    for v in (one(x) for x in basis(max_degree)):
        check(not d(d(v)),'endpoint_d_squared')
        check(detector(d(v))==(0,0),'detector_is_chain_map')
        for g in GROUP:
            check(detector(star(g,v))==tuple(chi(g)*a for a in detector(v)),
                  'detector_compensated_equivariance')
    for g in GROUP:
        check(d(edge_h(g))==defect(g),'old_lift_edge')
        check(detector(edge_h(g))==(alpha(g),0),'node_coherent_profile')
        check(db0(1,g)==2*alpha(g),'twice_node_profile_is_boundary')
        for h in GROUP:
            check(d(face_k(g,h))==add(star(g,edge_h(h)),scale(edge_h(mul(g,h)),-1),edge_h(g)),
                  'old_lift_pair')
            check(detector(face_k(g,h))==(0,carry(g,h)),'norm_coherent_profile')
            check(db1(alpha,g,h)==0,'alpha_1_cocycle')
            check(db1(lambda x:-x[0],g,h)==3*carry(g,h),'triple_norm_profile_is_boundary')
            for k in GROUP:
                check(db2(carry,g,h,k)==0,'norm_2_cocycle_all_216')
                check(not add(star(g,face_k(h,k)),scale(face_k(mul(g,h),k),-1),
                              face_k(g,mul(h,k)),scale(face_k(g,h),-1)), 'old_lift_triple')
    check(alpha(REFL)%2==1,'node_profile_nonzero_mod2')
    cyclic_sum=sum(carry((i,0),ROT) for i in range(3))
    check(cyclic_sum==-1,'norm_profile_nonzero_C3')
    # Any normalized 1-cochain b has sum_i delta(b)(r^i,r)=3*b(r).
    for vals in product(range(-2,3),repeat=2):
        b=lambda g: 0 if g[0]==0 else vals[g[0]-1]
        check(sum(db1(b,(i,0),ROT) for i in range(3))==3*vals[0],
              'norm_test_for_all_cyclic_coboundaries_formula')
    # The two relative components differ by a loop represented by alpha
    # in the sign module at detector degree 2, not by a different state z.
    for n in range(-6,7):
        for g,h in product(GROUP,repeat=2):
            check(db1(lambda x:n*alpha(x),g,h)==0,'relative_connector_loop_is_cocycle')
        check((n*alpha(REFL))%2==n%2,'relative_connector_loop_parity')
    # Positive polynomial branch pairs are contractible through the node,
    # and their contractions have zero conductor detector value.
    for k in range(1,max_degree+1):
        for branch in ('x','y'):
            v=one(('s',branch,k));h=one(('a',branch,k))
            check(d(h)==v,'polynomial_relation_kept')
            check(detector(h)==(0,0),'polynomial_contraction_preserves_detector')
    data=k6_source();ix=data['ix'];ls=data['longs'];T=data['top'];Ns=data['normals'];fs=data['facets'];qd=data['qd']
    U=mono({ix[d]+9:1 for d in ls})
    omega={T:U}
    for i,D in enumerate(ls):
        omega[Ns[i]]=pscale(mono({ix[D]:1,**{ix[E]+9:1 for E in ls if E!=D}}),-1)
    check(not cvapply(qd,omega),'Q_full_polynomial_syzygy')
    # Every filler of -dT equals -T+b*omega. This all-b proof is in the note.
    sample_vars=(6,7,8,15,16,17)
    samples=[ZERO_EXP]
    for degree_n in (1,2,3):
        for comb in combinations(range(len(sample_vars)+degree_n-1),degree_n):
            # Stars-and-bars weakly increasing variable indices.
            idx=[a-i for i,a in enumerate(comb)]
            e=[0]*19
            for j in idx:e[sample_vars[j]]+=1
            samples.append(tuple(e))
    for exp in samples:
        for scalar in (-1,1):
            b=pol(scalar,exp)
            filler=cvadd({T:pol(-1)},cvscale(omega,b))
            check(cvapply(qd,filler)==cvscale(qd[T],pol(-1)),'all_filler_formula_test')
            check(all(poly_in_stalk(p,set()) for p in filler.values()),'all_filler_coefficients_unlocalized')
    # The forbidden alternative has top coefficient zero, but illegal normal
    # coefficients -X_i/u_i. It works only after enlarging those stalks.
    illegal={Ns[i]:pscale(qd[T][fs[i]],-1) for i in range(3)}
    check(cvapply(qd,illegal)==cvscale(qd[T],pol(-1)),'globally_localized_false_positive')
    check(all(not poly_in_stalk(p,set()) for p in illegal.values()),'forbidden_normal_inverses_detected')
    # Multiplying the connecting class by U gives a legal relative boundary.
    principal_parts=[qd[T][f] for f in fs]
    check(all(not poly_in_stalk(p,set()) for p in principal_parts),'top_connecting_class_nonzero')
    check(all(poly_in_stalk(pmul(U,p),set()) for p in principal_parts),'U_annihilates_top_connecting_class')
    for i,D in enumerate(ls):
        partial=mono({ix[E]+9:1 for E in ls if E!=D})
        check(not poly_in_stalk(pmul(partial,principal_parts[i]),set()),'each_normal_factor_necessary')
    for n in (2,3,6):
        check(all(not poly_in_stalk(pscale(p,n),set()) for p in principal_parts),
              'no_integer_prime_cancellation_of_principal_parts')
    # x3 is an independent first-Rees spectator; it is not any X_D or u_D.
    x3=mono({18:1});y=principal_parts[0]
    check(not padd(pmul(x3,pscale(y,-1)),pmul(y,x3)),'one_road_BC_coefficient_equation')
    check(poly_in_stalk(y,{6}),'one_road_target_only_normal_inverse')
    check(x3!=pol() and bool(x3),'first_Rees_is_nonzero_not_constant_unit')
    check(next(iter(x3))[18]==1,'first_Rees_conormal_order_one')
    check(all(not poly_in_stalk(pmul(x3,p),set()) for p in principal_parts),
          'first_Rees_coefficient_does_not_kill_Q_top_obstruction')
    for exp in samples:
        b=pol(1,exp)
        v=cvadd({T:pscale(x3,-1)},cvscale(omega,b))
        check(cvapply(qd,v)==cvscale(qd[T],pscale(x3,-1)),
              'all_first_Rees_top_fillers_formula')
    # More generally (a,k)=(-y*b,x3*b) is the full syzygy when x3,y are
    # independent up to the target-legal normal denominator.
    for exp in samples:
        b=pol(1,exp)
        a=pscale(pmul(y,b),-1);k=pmul(x3,b)
        check(not padd(pmul(x3,a),pmul(y,k)),'one_road_all_syzygy_formula')
    result={
      'status':'relative_detector_classified_and_actual_target_support_gate_computed',
      'source_commit':COMMIT,
      'source_model':'supplied integral conductor-road endpoint complex with its full D3 orientation-compensated action',
      'source_target_file':'research/voevodsky/check_global_k6_koszul_cech_promotion.rs',
      'source_target_blob':'e972b69d0e2b1b0a0aee5e0a027c8216bcace3e8',
      'old_lift_rechecked':True,
      'detector':{'D1':'Z_sign','D2':'Z_sign','differential':0,
                  'p1':'node constant','p2':'top norm coefficient','p0':0,
                  'physical_endpoint_Q_restriction_identified':False},
      'coherent_boundary_profile':{
          'node_H1_D3_Zsign':'Z/2','node_class':'nonzero',
          'norm_H2_D3_Zsign':'Z/3','norm_class':'nonzero',
          'alpha':'alpha(r^i s^e)=-e',
          'beta':'beta(r^i s^e,r^j s^f)=-floor((i+(-1)^e*j)/3)',
          'joint_order':6},
      'relative_lift_space':{
          'unmatched_profile':'empty',
          'zero_profile':'empty',
          'matched_fully_based_profile':'two contractible components',
          'components':'torsor for Z/2, no preferred component without comparison path',
          'higher_homotopy_groups':'zero'},
      'actual_loaded_target':{
          'full_generators':215,'endpoint_subcomplex':16,'short_boundary_subcomplex':208,
          'Q3_rank':4,'Q2_rank':3,
          'dT':'sum_i (X_i/u_i)*F_i','dN_i':'F_i',
          'normal_generator_coefficient_ring':'unlocalized R',
          'unmarked_facet_coefficient_ring':'R[u_i^-1]',
          'Q_cycle_generator':'omega=(prod_i u_i)*T-sum_i X_i*(prod_{j!=i}u_j)*N_i',
          'all_fillers_of_minus_dT':'-T+b*omega, b in R',
          'top_zero_filler':'none over independent polynomial target ring',
          'relative_top_connecting_class':'[(X_i/u_i)_i] in direct_sum R[u_i^-1]/R',
          'annihilator':'(prod_i u_i)',
          'additive_order':'infinite',
          'integer_prime_torsion':'none'},
      'actual_one_road_coefficient_test':{
          'generic_coefficient':'x3','lower_coefficient':'-X_D/u_D',
          'incidence':'x3*a+(X_D/u_D)*k=0',
          'coefficient_Beck_Chevalley_obstruction':0,
          'conormal_leading_coefficient':1,
          'support_attachment_or_endpoint_connector_inferred':False},
      'uncomputed_physical_data':[
          'support-typed normalization-sheet map into the fixed supported dual target',
          'both endpoint connector cells and their induced coherent restriction',
          'comparison from actual generic Q framing to the node/norm detector',
          'physical reflection parity; not selected by the two-point calculation'],
      'proof_scope':'Finite group equations and full 215-generator target identities are exact; all-polynomial syzygies and full homotopy groups use the accompanying proofs. No proof assistant, no source repository writes.',
      'checks':dict(sorted(COUNTS.items())), 'total_exact_assertions':sum(COUNTS.values())}
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ('status','relative_lift_space','actual_loaded_target','total_exact_assertions')},indent=2))

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path('relative_physical_admissibility_certificate.json'))
    parser.add_argument('--max-degree',type=int,default=12)
    args=parser.parse_args()
    if args.max_degree<1: parser.error('--max-degree must be positive')
    main(args.output,args.max_degree)
