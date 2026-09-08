#!/usr/bin/env python3
"""Exact boundary-restriction calculation for the stated D03 coefficient candidate.

R=Z[x1,x5,X,U]; L=R[U^-1]. Only the target p term is localized.
This does not supply the missing spatial images of the physical connector cells.
Uses only Python's standard library. The proof in the companion note establishes
all-degree statements; the tests here check identities and constructive witnesses.
"""
from __future__ import annotations
import argparse
import json
from collections import Counter
from fractions import Fraction
from itertools import product
from pathlib import Path

# Exponents in x1,x5,X,U. Negative exponents are permitted only for U in L.
Exp = tuple[int, int, int, int]
Poly = dict[Exp, int]
Vec = tuple[Poly, ...]
CHECKS: Counter[str] = Counter()


def ck(condition: bool, name: str) -> None:
    if not condition:
        raise AssertionError(name)
    CHECKS[name] += 1


def mono(a: int=0, b: int=0, c: int=0, u: int=0, coef: int=1) -> Poly:
    if min(a,b,c) < 0:
        raise ValueError('Only U may have a negative exponent')
    return {(a,b,c,u):coef} if coef else {}


def add(*items: Poly) -> Poly:
    ans: Poly={}
    for p in items:
        for e,c in p.items():
            ans[e]=ans.get(e,0)+c
            if ans[e]==0: del ans[e]
    return ans


def neg(p: Poly) -> Poly:
    return {e:-c for e,c in p.items()}


def mul(p: Poly, q: Poly) -> Poly:
    ans: Poly={}
    for e,c in p.items():
        for f,d in q.items():
            g=tuple(a+b for a,b in zip(e,f))
            ans[g]=ans.get(g,0)+c*d
            if ans[g]==0: del ans[g]
    return ans


ONE=mono(); X1=mono(a=1); X5=mono(b=1); X=mono(c=1); U=mono(u=1); Y=mono(c=1,u=-1)


def zvec(n: int) -> Vec:
    return tuple({} for _ in range(n))


def vadd(a: Vec,b: Vec) -> Vec:
    if len(a)!=len(b): raise ValueError('Unequal vector lengths')
    return tuple(add(x,y) for x,y in zip(a,b))


def vneg(a: Vec) -> Vec:
    return tuple(neg(x) for x in a)


def iszero(v: Vec) -> bool:
    return not any(v)


# Slots labelled True take L coefficients; False take R coefficients.
MT={-3:(False,False), -2:(False,False,False,False,True),
    -1:(False,False,True,True), 0:(True,)}
NT={-3:(False,False), -2:(False,False,False,False,True), -1:(True,True)}


def validate(v: Vec, typ: tuple[bool,...]) -> None:
    if len(v)!=len(typ): raise ValueError('Wrong vector dimension')
    for p,localized in zip(v,typ):
        if any(min(e[:3])<0 or (e[3]<0 and not localized) for e in p):
            raise ValueError('Illegal coefficient localization')


def dm(n: int, v: Vec) -> Vec:
    validate(v,MT.get(n,()))
    if n==-3:
        a,b=v
        ans=(mul(X5,a),mul(X5,b),mul(X1,a),mul(X1,b),add(mul(Y,a),b))
    elif n==-2:
        a,b,c,d,z=v
        ans=(add(mul(X1,a),neg(mul(X5,c))),
             add(mul(X1,b),neg(mul(X5,d))),
             add(mul(Y,a),b,neg(mul(X5,z))),
             add(mul(Y,c),d,neg(mul(X1,z))))
    elif n==-1:
        a,b,c,d=v
        ans=(add(mul(Y,a),b,neg(mul(X1,c)),mul(X5,d)),)
    else:
        ans=()
    validate(ans,MT.get(n+1,()))
    return ans


def dn(n: int, v: Vec) -> Vec:
    validate(v,NT.get(n,()))
    if n==-3:
        a,b=v
        ans=(mul(X5,a),mul(X5,b),mul(X1,a),mul(X1,b),add(mul(Y,a),b))
    elif n==-2:
        a,b,c,d,z=v
        ans=(add(mul(Y,a),b,neg(mul(X5,z))),
             add(mul(Y,c),d,neg(mul(X1,z))))
    else:
        ans=()
    validate(ans,NT.get(n+1,()))
    return ans


def r(n: int, v: Vec) -> Vec:
    validate(v,MT.get(n,()))
    ans=v if n in (-3,-2) else (v[2:] if n==-1 else ())
    validate(ans,NT.get(n,()))
    return ans


def lift(n: int, v: Vec) -> Vec:
    """Graded splitting of r, NOT a chain map."""
    validate(v,NT.get(n,()))
    ans=v if n in (-3,-2) else (({}, {}, *v) if n==-1 else zvec(len(MT.get(n,()))))
    validate(ans,MT.get(n,()))
    return ans


def df(n: int, v: tuple[Vec,Vec]) -> tuple[Vec,Vec]:
    m,h=v
    return dm(n,m),vadd(r(n,m),vneg(dn(n-1,h)))


def split_w(p: Poly) -> tuple[Poly,Poly,Poly]:
    """p = w + Y*a + b; w is the canonical representative in W=L/(R+YR)."""
    w: Poly={}; a: Poly={}; b: Poly={}
    for e,c in p.items():
        if e[3]>=0:
            b[e]=c
        elif e[3]==-1 and e[2]>=1:
            a[(e[0],e[1],e[2]-1,0)]=c
        else:
            w[e]=c
    return w,a,b


def nw(p: Poly) -> Poly:
    return split_w(p)[0]


def invariant(f: Poly,h: Vec) -> Poly:
    if len(h)!=2: raise ValueError('Two endpoint connectors required')
    return nw(add(f,mul(X1,h[0]),neg(mul(X5,h[1]))))


def n_boundary_witness(h: Vec) -> Vec | None:
    """Return t in N^-2 with d_N t=h iff its class in H^-1(N) is zero.

    Constructive regular-pair syzygy calculation over the normal-form module W.
    """
    if invariant({},h): return None
    w0,a0,b0=split_w(h[0]); w2,a2,b2=split_w(h[1])
    if any(e[1]<1 for e in w0):
        raise AssertionError('Syzygy does not have the forced x5 divisor')
    z={(e[0],e[1]-1,e[2],e[3]):c for e,c in w0.items()}
    if nw(mul(X1,z))!=w2:
        raise AssertionError('Second syzygy component mismatch')
    # Multiplication by x1,x5 does not alter W-normality.
    witness=(a0,b0,a2,b2,neg(z))
    if dn(-2,witness)!=h:
        raise AssertionError('Incorrect N boundary witness')
    return witness


def fibre_boundary_witness(f: Poly,h: Vec) -> tuple[Vec,Vec] | None:
    """Return (s,t) in F^-1 with D(s,t)=(f,h), whenever the invariant is zero."""
    z=add(f,mul(X1,h[0]),neg(mul(X5,h[1])))
    w,a,b=split_w(z)
    if w: return None
    s=(a,b,h[0],h[1])
    t=zvec(5)
    if df(-1,(s,t))!=((f,),h):
        raise AssertionError('Incorrect framed nullhomotopy')
    return s,t


def test_monomials(localized: bool, bound: int):
    us=range(-bound,bound+1) if localized else range(bound+1)
    for a,b,c,u in product(range(3),range(3),range(2),us):
        yield mono(a,b,c,u)


def audit_mapping(bound: int) -> dict:
    # Basis checks are symbolic matrix identities; additional monomials test typed localization.
    for n,typ in MT.items():
        for slot,localized in enumerate(typ):
            for p in test_monomials(localized,bound):
                v=list(zvec(len(typ))); v[slot]=p; v=tuple(v)
                ck(iszero(dm(n+1,dm(n,v))), 'M_d_squared')
                ck(r(n+1,dm(n,v))==dn(n,r(n,v)), 'restriction_chain_map')
    for n,typ in NT.items():
        for slot,localized in enumerate(typ):
            for p in test_monomials(localized,bound):
                v=list(zvec(len(typ))); v[slot]=p; v=tuple(v)
                ck(iszero(dn(n+1,dn(n,v))), 'N_d_squared')
                ck(r(n,lift(n,v))==v, 'graded_restriction_surjectivity')
    # Verify fibre differential and normal-form invariance on all its degree -1 slots.
    for slot,localized in enumerate(MT[-1]):
        for p in test_monomials(localized,bound):
            s=list(zvec(4)); s[slot]=p; s=tuple(s)
            f,h=df(-1,(s,zvec(5)))
            ck(invariant(f[0],h)=={}, 'fibre_boundary_invariant_zero')
            d2=df(0,(f,h)); ck(iszero(d2[0]) and iszero(d2[1]), 'fibre_d_squared')
    for slot,localized in enumerate(NT[-2]):
        for p in test_monomials(localized,bound):
            t=list(zvec(5)); t[slot]=p; t=tuple(t)
            f,h=df(-1,(zvec(4),t))
            ck(invariant(f[0],h)=={}, 'higher_connector_boundary_invariant_zero')
    # The actual candidate f(e)=p and its endpoint-vanishing primitive.
    s=({},ONE,{}, {})
    ck(dm(-1,s)==(ONE,), 'unit_attachment_ambient_primitive')
    ck(r(-1,s)==({},{}), 'unit_attachment_primitive_endpoint_restriction')
    ck(invariant(ONE,({},{}))=={}, 'zero_connector_unit_attachment_is_framed_zero')
    # Nonuniqueness of that nullhomotopy: U k-X n is a genuine closed upper map.
    upper=(U,neg(X),{}, {})
    ck(iszero(dm(-1,upper)), 'upper_syzygy_closed')
    ck(r(-1,upper)==({},{}), 'upper_syzygy_boundary_zero')
    # Illegal inverse on an upper target term must be rejected.
    rejected=False
    try: validate((mono(u=-1),{}, {}, {}),MT[-1])
    except ValueError: rejected=True
    ck(rejected,'upper_target_inverse_rejected')
    return {
        'source_degrees':{'2':['e3'],'1':['q0','q2'],'0':['a']},
        'target_degrees':{'3':['R*k','R*n'],'2':['R[U^-1]*p']},
        'M_modules':{'-3':'R^2','-2':'R^4+L','-1':'R^2+L^2','0':'L'},
        'N_modules':{'-3':'R^2','-2':'R^4+L','-1':'L^2'},
        'r_minus3':'identity','r_minus2':'identity','r_minus1':'(A,B,c0,c2)->(c0,c2)','r_zero':'zero',
        'ambient_unit_primitive':'s(e3)=n; s(q0)=s(q2)=s(a)=0',
        'r_of_unit_primitive':[0,0],
        'framed_H0':'W=L/(R+(X/U)R)',
        'framed_Hminus1':'R*(U*k-X*n)',
        'framed_other_cohomology':'zero',
        'secondary_cokernel':'(x1,x5)*W',
        'secondary_coordinate_for_unit_attachment':'[x1*h0-x5*h2] in W',
    }


def audit_normal_forms(bound: int) -> dict:
    ps=list(test_monomials(True,bound))
    for p in ps:
        w,a,b=split_w(p)
        ck(p==add(w,mul(Y,a),b),'normal_form_decomposition')
        ck(nw(w)==w,'normal_form_idempotence')
        ck(nw(mul(Y,a))=={} and nw(b)=={},'denominator_submodule_annihilated')
    hs=[({},{}),(ONE,{}),({},ONE),(mono(u=-1),{}),({},mono(u=-1)),
        (mul(X5,mono(u=-1)),mul(X1,mono(u=-1))),
        (Y,{}),({},Y)]
    for z in ps:
        # Derived endpoint-augmentation relation, with regular and Y corrections.
        hs.append((add(mul(X5,z),ONE,Y),add(mul(X1,z),X5,Y)))
    for h in hs:
        residual=invariant({},h)
        witness=n_boundary_witness(h)
        ck((witness is not None)==(residual=={}),'N_boundary_witness_iff_zero')
        if witness is not None:
            ck(dn(-2,witness)==h,'N_boundary_witness_equation')
        for f in (ONE,{},Y,mono(u=-1)):
            fw=fibre_boundary_witness(f,h)
            ck((fw is not None)==(invariant(f,h)=={}),'framed_boundary_witness_iff_zero')
            if fw is not None:
                ck(df(-1,fw)==((f,),h),'framed_boundary_witness_equation')
    # Test any ambient degree -1 cocycle has trivial H^-1 restriction.
    for slot,localized in enumerate(MT[-2]):
        for p in test_monomials(localized,bound):
            v=list(zvec(5));v[slot]=p;v=tuple(v)
            cycle=dm(-2,v)
            ck(iszero(dm(-1,cycle)),'ambient_primitive_change_closed')
            boundary=n_boundary_witness(r(-1,cycle))
            ck(boundary is not None,'ambient_closed_change_boundary_exact')
    ck(invariant(ONE,(mono(u=-1),{}))==mono(a=1,u=-1),'nonzero_connector_example')
    ck(invariant(ONE,(mul(X5,mono(u=-1)),mul(X1,mono(u=-1))))=={},'augmentation_connector_cancellation')
    ck(nw(mul(U,mono(u=-1)))=={} and nw(mul(X,mono(u=-1)))=={},'first_principal_part_annihilators')
    ck(nw(mono(u=-2))!= {},'higher_principal_part_survival')
    return {
        'W_as_Zx1x5X_module':'(Z[x1,x5]*U^-1) + direct_sum_{n>=2} Z[x1,x5,X]*U^-n',
        'regular_connector_residual':'zero',
        'example_h_zero':{'h':[0,0],'residual':'0'},
        'example_h_principal_part':{'h':['U^-1','0'],'residual':'[x1/U] != 0'},
        'example_h_augmentation':{'h':['x5/U','x1/U'],'residual':'0, with explicit N^-2 witness'},
        'integer_torsion':'none, by coefficient normal form',
    }


def rank(matrix: list[list[int]]) -> int:
    if not matrix:return 0
    a=[[Fraction(x) for x in row] for row in matrix]
    r0=0
    for c in range(len(a[0])):
        piv=next((r for r in range(r0,len(a)) if a[r][c]),None)
        if piv is None:continue
        a[r0],a[piv]=a[piv],a[r0]
        s=a[r0][c]; a[r0]=[x/s for x in a[r0]]
        for r in range(len(a)):
            if r!=r0 and a[r][c]:
                s=a[r][c];a[r]=[x-s*y for x,y in zip(a[r],a[r0])]
        r0+=1
    return r0


def det(a: list[list[int]]) -> int:
    if not a:return 1
    if len(a)==1:return a[0][0]
    return sum((-1)**j*a[0][j]*det([row[:j]+row[j+1:] for row in a[1:]]) for j in range(len(a)))


def audit_source_connector_carrier() -> dict:
    rays=[(1,0),(0,1),(-1,-1)]
    fan=[]; cones=[]
    for i in range(3):
        fan.extend([rays[i],tuple(x+y for x,y in zip(rays[i],rays[(i+1)%3]))])
        cones.extend([(i,(i+1)%3,True),(i,(i+2)%3,False)])
    for i in range(6):
        a,b=fan[i],fan[(i+1)%6]
        ck(a[0]*b[1]-a[1]*b[0]==1,'source_dp6_smooth_fan')
    shared=[]
    for i in range(6):
        s=set(cones[i][:2])&set(cones[(i+1)%6][:2])
        ck(len(s)==1,'source_shared_ray_unique');shared.append(next(iter(s)))
    def image(c,ray):
        a,b,pos=c
        if ray not in (a,b): raise ValueError('Ray outside cone')
        return ('v+' if pos else 'v-') if ray==a else f'c{3-a-b}'
    vertices=['v+','v-','c0','c1','c2']
    def bd(a,b):
        v=[0]*5;v[vertices.index(a)]-=1;v[vertices.index(b)]+=1;return v
    edges=[]; columns=[];con_columns=[]
    for i in range(6):
        a=image(cones[i],shared[(i-1)%6]);b=image(cones[i],shared[i])
        c=image(cones[(i+1)%6],shared[i])
        edges.extend([{'name':f'ell{i}','from':a,'to':b}, {'name':f'kappa{i}','from':b,'to':c}])
        columns.extend([bd(a,b),bd(b,c)]);con_columns.append(bd(b,c))
    matrix=[list(row) for row in zip(*columns)]
    connectors=[list(row) for row in zip(*con_columns)]
    ck(all(sum(row)==0 for row in matrix),'source_connector_telescope')
    ck(rank(matrix)==4,'source_target_incidence_rank')
    ck(rank(connectors)==3,'source_connector_only_rank')
    for i in (0,2,4):
        ck(con_columns[i]==[-1,1,0,0,0],'source_endpoint_connector_column')
    ck(con_columns[1]==[0,0,1,-1,0],'source_center_connector_1')
    ck(con_columns[3]==[0,0,0,1,-1],'source_center_connector_3')
    ck(con_columns[5]==[0,0,-1,0,1],'source_center_connector_5')
    # Four tree edges: ell0(c2->+), kappa0(+->-), ell2(c0->+), ell4(c1->+).
    minor=[[matrix[r][c] for c in (0,1,4,8)] for r in (1,2,3,4)]
    ck(abs(det(minor))==1,'source_primitive_spanning_tree_minor')
    return {'source':'check_dp6_oriented_boundary_connector_realization.rs',
            'vertices':vertices,'edges':edges,'full_incidence_matrix':matrix,
            'connector_matrix':connectors,'rank_full':4,'rank_connectors':3,
            'scope':'These are source-defined constructible/KN cellular boundaries, NOT Hom-complex connector cochains h0,h2.',
            'physical_connector_images_in_local_Hom':'not supplied'}


def main() -> None:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output',type=Path,default=Path('endpoint_boundary_restriction_certificate.json'))
    p.add_argument('--laurent-test-bound',type=int,default=4)
    args=p.parse_args()
    if args.laurent_test_bound<1:raise ValueError('Positive test bound required')
    out={'schema':'marici.branch-a.endpoint-restriction.v1',
         'source_commit':'d1947b67a60d3e88ba77f4ca60ea02c2a306ee61',
         'mapping_restriction':audit_mapping(args.laurent_test_bound),
         'normal_forms':audit_normal_forms(args.laurent_test_bound),
         'actual_constructible_connector_boundaries':audit_source_connector_carrier(),
         'provenance':{
             'endpoint_hull_117':'af6874dc6928614a824a14105fa8e4ba37d96306',
             'local_collar_174':'ae5d4fc93fa135e7dc0ee6088928f9b8f8cad405',
             'constructible_connector_checker_249':'7b0bc2735e99d3075968e11da0ea6f9f0937ea38'},
         'limits':['Computes the fully specified endpoint-Koszul/local-collar coefficient candidate.',
                   'Does not identify Boolean q0/q2 endpoints with the physical v+/v- costalks.',
                   'Does not manufacture missing physical connector images, full source/target comparison, or Q framing.',
                   'No physical h-r(s) value, endpoint parity, or RH criterion is claimed.',
                   'Finite tests supplement all-degree algebraic proofs; no proof-assistant check is claimed.',
                   'No repository files were modified.']}
    out['checks']=dict(sorted(CHECKS.items()));out['total_checks']=sum(CHECKS.values())
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'checks':out['total_checks'],'certificate':str(args.output)},indent=2))


if __name__=='__main__':main()
