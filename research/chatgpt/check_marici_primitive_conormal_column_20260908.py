#!/usr/bin/env python3
"""Exact target-side primitive-column computation for the marked collar.

Standard library only.  This script does NOT import or reconstruct Branch C's
128/1024-state physical sources.  It constructs the specified two-layer
conormal module, its conductor-resolution Hom matrices, and tests the relative
operation orbit of the conormal inclusion.  The physical map a, the framed
endpoint covectors, and the resulting physical control cohomology remain unset.

The bounded computations verify the formulas in the accompanying proof; they
are not claimed to prove all-degree statements by extrapolation.
"""
from __future__ import annotations
import argparse
from collections import Counter, defaultdict
from functools import lru_cache
from itertools import combinations, product
from pathlib import Path
import hashlib
import json

Word = tuple[tuple[int, ...], ...]
Poly = dict[Word, int]
LABELS = ('13', '15', '35', '02', '04', '24')
PLUS = (0, 1, 2)
MINUS = (3, 4, 5)
CHECKS: Counter[str] = Counter()


def check(ok: bool, name: str, detail=None) -> None:
    if not ok:
        raise AssertionError(f'{name}: {detail!r}')
    CHECKS[name] += 1


def pm(n: int) -> int:
    return -1 if n % 2 else 1


def put(v: dict, key, c: int) -> None:
    if c:
        v[key] = v.get(key, 0) + c
        if not v[key]:
            del v[key]


def add(*terms: dict) -> dict:
    out = {}
    for v in terms:
        for k, c in v.items():
            put(out, k, c)
    return out


def scale(v: dict, c: int) -> dict:
    return {k: c*a for k, a in v.items() if c*a}


def subs(items):
    for n in range(len(items) + 1):
        yield from combinations(items, n)


def degree(w: Word) -> int:
    return sum(map(len, w))


def flatten(w: Word) -> tuple[int, ...]:
    return tuple(i for block in w for i in block)


def word_weight(w: Word) -> tuple[int, ...]:
    f = flatten(w)
    return tuple(f.count(i) for i in range(6))


def sign(seq) -> int:
    return pm(sum(seq[i] > seq[j] for i in range(len(seq)) for j in range(i+1,len(seq))))


@lru_cache(None)
def words(n: int, first: int = -1) -> tuple[Word, ...]:
    if n < 0:
        return ()
    if n == 0:
        return ((),)
    out = []
    for side in (0,1):
        if first >= 0 and side != first:
            continue
        for block in subs(PLUS if side == 0 else MINUS):
            if not block or len(block) > n:
                continue
            out.extend((block,) + rest for rest in words(n-len(block), 1-side))
    return tuple(out)


def normal_form(seq: tuple[int, ...]) -> Poly:
    out = []
    c = 1
    k = 0
    while k < len(seq):
        j = k+1
        while j < len(seq) and seq[j]//3 == seq[k]//3:
            j += 1
        block = seq[k:j]
        if len(block) != len(set(block)):
            return {}
        c *= sign(block)
        out.append(tuple(sorted(block)))
        k = j
    return {tuple(out):c}


def mul(a: Poly, b: Poly) -> Poly:
    out = {}
    for w, aw in a.items():
        for v, bv in b.items():
            for t, c in normal_form(flatten(w)+flatten(v)).items():
                put(out, t, aw*bv*c)
    return out


def bracket(a: Poly, b: Poly) -> Poly:
    if not a or not b:
        return {}
    return add(mul(a,b), scale(mul(b,a), -pm(degree(next(iter(a)))*degree(next(iter(b))))))


MIXED = tuple(J for J in subs(tuple(range(6))) if any(i<3 for i in J) and any(i>=3 for i in J))


@lru_cache(None)
def generator(J) -> Poly:
    root = min(i for i in J if i<3)
    value = normal_form((root,))
    for i in reversed(tuple(i for i in J if i != root)):
        value = bracket(normal_form((i,)), value)
    return value


@lru_cache(None)
def relative_words(n):
    if n == 0:
        return ((),)
    return tuple((J,)+v for J in MIXED if len(J)<=n for v in relative_words(n-len(J)))


@lru_cache(None)
def relative_image(w) -> Poly:
    if not w:
        return {():1}
    return mul(generator(w[0]), relative_image(w[1:]))


def independent_unit_columns(columns: list[Poly]) -> int:
    pivots = {}
    for column in columns:
        value = dict(column)
        while value:
            p = min(value)
            c = value[p]
            if p in pivots:
                value = add(value, scale(pivots[p], -c))
            else:
                check(abs(c)==1, 'relative_injectivity_unit_pivot')
                pivots[p] = scale(value,c)
                break
        check(bool(value), 'relative_columns_independent')
    return len(pivots)


# Differential on the genuine free B-resolution.  Coefficients are occurrence
# monomials; mixed-sheet coefficient products are zero in B.
def variable_times(m, i):
    if any(m[j] for j in range(6) if j//3 != i//3):
        return None
    a = list(m); a[i] += 1
    return tuple(a)


def d_source(chain):
    out = {}
    for (m,w),c in chain.items():
        if not w:
            continue
        first = w[0]
        for pos,i in enumerate(first):
            new_m = variable_times(m,i)
            if new_m is None:
                continue
            block = first[:pos]+first[pos+1:]
            new_w = (block,)+w[1:] if block else w[1:]
            put(out,(new_m,new_w),pm(pos)*c)
    return out


def dual_prefix_columns(n: int, k: int) -> dict[Word, Poly]:
    """Transpose the X_k coefficient of d:P_(n+1)->P_n, independently of mul."""
    out = {w:{} for w in words(n)}
    for target in words(n+1):
        block=target[0]
        if k not in block:
            continue
        pos=block.index(k)
        rem=block[:pos]+block[pos+1:]
        source=(rem,)+target[1:] if rem else target[1:]
        put(out[source],target,pm(pos))
    return out


def dihedral():
    ds=tuple(tuple(int(c) for c in name) for name in LABELS)
    perms=[]
    for r,reflect in product(range(3),(False,True)):
        p=[]
        for a,b in ds:
            image=tuple(sorted((((1-a if reflect else a)+2*r)%6,
                                ((1-b if reflect else b)+2*r)%6)))
            p.append(ds.index(image))
        perms.append(tuple(p))
    return tuple(perms)


def transport(v: Poly,p) -> Poly:
    out={}
    for w,c in v.items():
        out=add(out,scale(normal_form(tuple(p[i] for i in flatten(w))),c))
    return out


def record(v: Poly):
    return [{'word':[[LABELS[i] for i in b] for b in w], 'coefficient':c}
            for w,c in sorted(v.items())]


# Noncommutative block formulas with typed arrows.  Identity of d_Y^2 is
# reduced only by d^2=0 and the supplied chain-map identities for q and pi.
def reduce_arrow_word(w):
    if w in (('dZ','dZ'),('dE','dE'),('dL','dL')):
        return None
    if w==('q','dZ'):
        return ('dL','q')
    if w==('pi','dE'):
        return ('dL','pi')
    if w in (('pi','j'),('dE','j')):
        return None
    return w


def apoly_multiply(a,b):
    out={}
    for u,c in a.items():
        for v,d in b.items():
            w=reduce_arrow_word(u+v)
            if w is not None:
                put(out,w,c*d)
    return out


def block_multiply(A,B):
    return [[add(*(apoly_multiply(a,b) for a,b in zip(row,col)))
             for col in zip(*B)] for row in A]


def primitive_linear_system(D0, D35, nu0, nu35, beta, zero, one, multiply):
    """Compile the primitive E_beta,35 row equations over a commutative ring.

    D0,D35 are n-by-m incoming differential matrices after conductor constant
    and first-35 coefficient extraction. nu0,nu35 are length-n column data
    for the selected source marking. Columns of the returned system are
    (A_1,...,A_n,B_1,...,B_n), where f(e_j)=A_j*u+B_j*v.
    This compiles equations; it does not solve a general polynomial system.
    """
    n=len(D0)
    if not n or len(D35)!=n or len(nu0)!=n or len(nu35)!=n:
        raise ValueError('Incompatible source-column dimensions')
    m=len(D0[0])
    if any(len(r)!=m for r in D0+D35):
        raise ValueError('Ragged incoming source matrix')
    matrix=[]; rhs=[]
    for c in range(m):
        matrix.append([D0[j][c] for j in range(n)]+[zero]*n)
        rhs.append(zero)
    for c in range(m):
        matrix.append([multiply(beta,D35[j][c]) for j in range(n)]
                      +[D0[j][c] for j in range(n)])
        rhs.append(zero)
    matrix.append(list(nu0)+[zero]*n); rhs.append(zero)
    matrix.append([multiply(beta,x) for x in nu35]+list(nu0)); rhs.append(one)
    return matrix,rhs


def run(output: Path, max_degree: int):
    if not 2 <= max_degree <= 7:
        raise ValueError('--max-degree must be between 2 and 7')
    k=LABELS.index('35')
    atom=normal_form((k,))
    zero_m=(0,)*6

    # Strict B-module matrices X_k u=beta v, X_i v=0, X_i u=0 for i!=k.
    # Store polynomial entries as beta-power->integer.
    zero={}; one={0:1}; beta={1:1}
    N={i:[[{},{}], [beta if i==k else {},{}]] for i in range(6)}
    def pmul(a,b):
        out={}
        for e,c in a.items():
            for f,d in b.items(): put(out,e+f,c*d)
        return out
    def mm(A,B):
        return [[add(*(pmul(a,b) for a,b in zip(row,col))) for col in zip(*B)] for row in A]
    j=[[zero],[one]]; pi=[[one,zero]]
    for i in range(6):
        check(mm(N[i],j)==[[{}],[{}]],'conormal_inclusion_B_linear',i)
        check(mm(pi,N[i])==[[{},{}]],'conductor_projection_B_linear',i)
        for t in range(6):
            check(mm(N[i],N[t])==[[{},{}],[{},{}]],'occurrence_module_relations',(i,t))
    check(mm(pi,j)==[[{}]],'primitive_projection_zero')
    check(mm(N[k],[[one],[zero]])==[[{}],[beta]],'scalar_unit_first_equation_defect')
    check(beta!={},'scalar_unit_defect_nonzero_polynomial')

    # Compile the actual diagnostic primitive system directly from its six
    # incoming conductor-resolution coefficients, not from a declared rank.
    D0=[[zero for _ in range(6)]]
    D35=[[one if i==k else zero for i in range(6)]]
    mat,rhs=primitive_linear_system(D0,D35,[one],[zero],beta,zero,one,pmul)
    for row,target in zip(mat,rhs):
        check(add(pmul(row[0],zero),pmul(row[1],one))==target,
              'compiled_primitive_system_accepts_v')
    check(mat[6+k]==[beta,zero],'compiled_first_nonzero_relation_row')

    # Full native resolution, not the 64-state ambient Koszul complex.
    rows=[]
    ranks=[len(words(n)) for n in range(max_degree+2)]
    for n in range(max_degree+2):
        for w in words(n):
            d=d_source({(zero_m,w):1})
            check(not d_source(d),'native_resolution_d_squared',(n,w))
            check(all(sum(m)+degree(v)==n for m,v in d),'native_d_preserves_total_weight',(n,w))
            # A primitive map P_C -> E has only its degree-zero column.
            # Every incoming source coefficient is an occurrence and kills v.
            if n==1:
                i=w[0][0]
                check(mm(N[i],j)==[[{}],[{}]],'primitive_column_chain_equation',i)

    for n in range(max_degree+1):
        columns=dual_prefix_columns(n,k)
        images=[]
        for w,v in columns.items():
            check(v==mul(atom,{w:1}),'Hom_differential_equals_left_prefix',(n,w))
            check(not mul(atom,v),'Hom_differential_squared',(n,w))
            if v:
                check(len(v)==1 and abs(next(iter(v.values())))==1,'prefix_signed_unit_column',(n,w))
                images.append(next(iter(v)))
        check(len(images)==len(set(images)),'prefix_images_distinct',n)
        kernel_basis={w for w in words(n) if not columns[w]}
        previous_images=set()
        if n:
            for w in words(n-1): previous_images.update(mul(atom,{w:1}))
        check(kernel_basis==previous_images,'left_prefix_kernel_image_exact',n)
        # At degree n, im L_k from n-1 has rank a_n.
        a_n=len(previous_images)
        free=1 if n==0 else ranks[n]
        tors=0 if n==0 else a_n
        rows.append({'degree':n,'native_Ext_rank':ranks[n],
                     'rank_prefix_from_previous_degree':a_n,
                     'Ext_C_to_E_free_rank_over_C':free,
                     'Ext_C_to_E_C_mod_beta_summands':tors,
                     'beta_zero_Ext_rank':2*ranks[n],
                     'beta_invertible_Ext_rank':ranks[n]})
        # Standard Hom sign and the stated cochain rephasing.
        check(pm((n+1)*(n+2)//2)*pm(n+1)*pm(n*(n+1)//2)==1,
              'Hom_sign_rephasing',n)

    # All 49 relative generators and their product words up to the selected degree.
    generator_records=[]
    for J in MIXED:
        g=generator(J)
        check(bool(g),'relative_generator_nonzero',J)
        check(bool(mul(atom,g)),'relative_generator_not_in_prefix_ideal',J)
        generator_records.append({'labels':[LABELS[i] for i in J],
             'degree':len(J),'image_under_conormal_map':record(g),
             'meaning':'class of v times this right-precomposition operation; not a physical seed image'})
    for n in range(max_degree+1):
        grouped=defaultdict(list)
        for w in relative_words(n):
            v=mul(atom,relative_image(w))
            check(bool(v),'relative_word_orbit_detected',w)
            grouped[word_weight(next(iter(v)))].append(v)
        rank=sum(independent_unit_columns(cols) for cols in grouped.values())
        check(rank==len(relative_words(n)),'relative_prefix_injectivity_rank',n)

    # The actual decomposable reflection correction is not dropped.
    e=[normal_form((i,)) for i in range(6)]
    g=bracket(e[1],bracket(e[3],bracket(e[4],e[0])))
    r21=bracket(e[1],e[3]); r12=bracket(e[0],e[4])
    s=(4,3,5,1,0,2)
    correction=bracket(r21,r12)
    check(transport(g,s)==add(scale(g,-1),correction),'full_reflection_correction')
    check(bool(correction),'decomposable_reflection_nonzero')
    check(bool(mul(normal_form((s[k],)),correction)),
          'reflection_correction_survives_conormal_comparison')
    for p in dihedral():
        for J in MIXED:
            gJ=generator(J)
            check(transport(mul(atom,gJ),p)==mul(normal_form((p[k],)),transport(gJ,p)),
                  'labelled_conormal_operation_covariance',(p,J))
    check(s[k]!=k,'fixed_D35_not_reflection_stable')

    # Formal cone identities retaining the entire (unspecified here) dZ block.
    az=lambda name:{(name,):1}
    DY=[[az('dZ'),{},{}],[{},az('dE'),{}],[az('q'),scale(az('pi'),-1),scale(az('dL'),-1)]]
    check(block_multiply(DY,DY)==[[{}]*3 for _ in range(3)],'full_pullback_block_d_squared')
    JJ=[[{}],[az('j')],[{}]]
    check(block_multiply(DY,JJ)==[[{}],[{}],[{}]],'full_pullback_primitive_column_closed')

    # Primitive Hom rows displayed in coefficient matrices, independently built.
    primitive_rows=[]
    for i in range(6):
        primitive_rows.append({'source_relation':f'd e_{LABELS[i]}=X_{LABELS[i]} e_empty',
                              'row_on_(u,v)': ['beta' if i==k else '0','0']})
    # A covariance check concerns a FAMILY E_beta,k; it is not an invented
    # endomorphism of the fixed 35 target under branch exchange.
    cert={
      'status':'constructed_target_side_primitive_column_only',
      'physical_b_on_complete_framed_source_constructed':False,
      'physical_source_replaced_by_conductor_resolution':False,
      'physical_source_a':None,
      'physical_endpoint_covectors_kappa_plus_minus':None,
      'actual_physical_frame_identifications':None,
      'physical_control_cohomology':{'H1':None,'H0':None,'Hminus1':None},
      'target_projection_from_declared_pullback':'p: D35 -> omega[2], (z,e,h) -> z',
      'primitive_inclusion':'j35: C*v*Pi_dual[3] -> D35, v -> (0,v,0)',
      'module_X35_matrix':[['0','0'],['beta','0']],
      'module_other_X_matrices':[['0','0'],['0','0']],
      'module_projection_pi':['1','0'],
      'primitive_column':['0','1'],
      'primitive_relation_matrix':primitive_rows,
      'compiled_primitive_system':{'matrix':mat,'rhs':rhs,'unknowns':['A_u','B_v']},
      'general_source_first_jet_system':'A*D0=0; B*D0+beta*A*D35=0; A*nu0=0; B*nu0+beta*A*nu35=1',
      'boundary_a_equations':'A_X*a0=A_A; B_X*a0+beta*A_X*a35=B_A',
      'Hom_B_C_Ebeta35':'C*v when beta is a nonzerodivisor',
      'scalar_unit_lift':'obstructed by beta*eta35; not a statement about the different physical source',
      'right_precomposition_action_kernel':'beta*eta35*E_B',
      'relative_operation_orbit_of_v':'injective R -> Ext_B(C,Ebeta35); same-variance identification with endpoint M_sigma not supplied',
      'relative_generator_images':generator_records,
      'intrinsic_target_Ext_cohomology':rows,
      'cohomological_shift':'[3] places the coefficient module in degree -3',
      'formal_weight_relation':'wt(v)=wt(u)+wt(X35)-wt(beta); Pi_dual is retained',
      'lambda':'independent bookkeeping parameter, degree 0 for displayed maps',
      'scope':[
        'The complete non-split dualizing complex is retained symbolically as Z=omega[2]; no cohomology-only replacement is made.',
        'The given block formula determines p for the declared pullback; no numeric physical dualizing/source matrices are claimed.',
        'The native alternating conductor resolution is only a diagnostic domain for the primitive target column.',
        'The physical 128-state and 1024-state source files were not recovered; state counts are not used to infer maps or degrees.',
        'Precomposition on RHom_B(C,E) is not identified with postcomposition on K(X)=RHom_B(X,C).',
        'No geometric bivariant endpoint operation or physical homotopy-fixed collar is certified.'
      ],
      'verification_max_degree':max_degree,
      'checks':dict(sorted(CHECKS.items())),
      'exact_assertions':sum(CHECKS.values()),
    }
    output.write_text(json.dumps(cert,indent=2)+'\n')
    print(json.dumps({key:cert[key] for key in ('status','physical_b_on_complete_framed_source_constructed',
          'primitive_column','intrinsic_target_Ext_cohomology','exact_assertions')},indent=2))


if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output',type=Path,default=Path('marici_primitive_conormal_column_certificate_20260908.json'))
    ap.add_argument('--max-degree',type=int,default=6)
    args=ap.parse_args()
    run(args.output,args.max_degree)
