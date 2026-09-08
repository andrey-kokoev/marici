#!/usr/bin/env python3
"""Exact conductor Yoneda operators and globally framed extension classification.

Standard library only. No repository writes or external access. The six operators
are explicit maps on the all-degree alternating resolution. Bounded tests audit
formulas; the accompanying proof establishes arbitrary degree and polynomial
exponents. Global gluing is over the already specified seven-chart test open,
not an identification with the native physical source.
"""
from __future__ import annotations
import argparse
from collections import Counter
from functools import lru_cache
from itertools import combinations, product
from pathlib import Path
import hashlib
import json

Block = tuple[int, ...]
Word = tuple[Block, ...]
Mon = tuple[int, ...]
Vec = dict[tuple[Mon, Word], int]
ZERO: Mon = (0,) * 6
COUNTS: Counter[str] = Counter()
LABELS = ('13', '15', '35', '02', '04', '24')
LONGS = ('03', '14', '25')
COMMIT = 'd1947b67a60d3e88ba77f4ca60ea02c2a306ee61'


def check(condition: bool, family: str, detail=None) -> None:
    if not condition:
        raise AssertionError(f'{family}: {detail!r}')
    COUNTS[family] += 1


def sign(n: int) -> int:
    return -1 if n % 2 else 1


def put(out: dict, key, value: int) -> None:
    if value:
        out[key] = out.get(key, 0) + value
        if not out[key]:
            del out[key]


def add(*vs: dict) -> dict:
    out = {}
    for v in vs:
        for k, a in v.items():
            put(out, k, a)
    return out


def scale(v: dict, n: int) -> dict:
    return {k: a*n for k, a in v.items() if a*n}


def degree(w: Word) -> int:
    return sum(map(len, w))


@lru_cache(None)
def words(n: int, first: int = -1) -> tuple[Word, ...]:
    if n < 0:
        return ()
    if n == 0:
        return ((),)
    out = []
    for side in ((0, 1) if first == -1 else (first,)):
        for mask in range(1, 8):
            a = tuple(3*side+i for i in range(3) if mask >> i & 1)
            if len(a) <= n:
                out.extend((a,)+v for v in words(n-len(a), 1-side))
    return tuple(out)


def side_of_monomial(m: Mon) -> int | None:
    if any(m[:3]) and any(m[3:]):
        raise ValueError('Mixed occurrence monomials are zero, not basis elements.')
    return 0 if any(m[:3]) else 1 if any(m[3:]) else None


def times_variable(m: Mon, i: int) -> Mon | None:
    side = side_of_monomial(m)
    if side is not None and side != i//3:
        return None
    a = list(m)
    a[i] += 1
    return tuple(a)


def d(v: Vec) -> Vec:
    out = {}
    for (m, w), c in v.items():
        if not w:
            continue
        a = w[0]
        for j, i in enumerate(a):
            mm = times_variable(m, i)
            if mm is None:
                continue
            aa = a[:j]+a[j+1:]
            ww = (aa,)+w[1:] if aa else w[1:]
            put(out, (mm, ww), c*sign(j))
    return out


def aug_h(v: Vec) -> Vec:
    """Integral C-linear contraction; not a B-linear contraction."""
    out = {}
    for (m, w), c in v.items():
        side = side_of_monomial(m)
        if side is None:
            continue
        a, suffix = (w[0], w[1:]) if w and w[0][0]//3 == side else ((), w)
        i = min(tuple(k for k, e in enumerate(m) if e) + a)
        if i in a:
            continue
        mm = list(m)
        mm[i] -= 1
        aa = tuple(sorted(a+(i,)))
        put(out, (tuple(mm), (aa,)+suffix), c*sign(sum(j<i for j in a)))
    return out


def op(i: int, v: Vec) -> Vec:
    """Degree-one End(P) cocycle: signed contraction of the LAST block."""
    out = {}
    for (m, w), c in v.items():
        if not w or i not in w[-1]:
            continue
        a = w[-1]
        j = a.index(i)
        aa = a[:j]+a[j+1:]
        ww = w[:-1]+((aa,) if aa else ())
        put(out, (m, ww), c*sign(degree(w)-len(a)+j))
    return out


def operator(w: Word, v: Vec) -> Vec:
    """Products are composition: rightmost generator acts first."""
    for i in reversed(tuple(i for a in w for i in a)):
        v = op(i, v)
        if not v:
            break
    return v


def mul(u: Word, v: Word) -> tuple[int, Word]:
    """Normal product in exterior(+) free-product exterior(-)."""
    if not u:
        return 1, v
    if not v:
        return 1, u
    if u[-1][0]//3 != v[0][0]//3:
        return 1, u+v
    a, b = u[-1], v[0]
    if set(a) & set(b):
        return 0, ()
    sg = sign(sum(i>j for i in a for j in b))
    return sg, u[:-1]+(tuple(sorted(a+b)),)+v[1:]


def mul_vec(u: dict[Word, int], v: dict[Word, int]) -> dict[Word, int]:
    out = {}
    for a, n in u.items():
        for b, m in v.items():
            sg, w = mul(a, b)
            put(out, w, n*m*sg)
    return out


def epsilon(v: Vec) -> int:
    return v.get((ZERO, ()), 0)


def wedge_sign(a: Block, b: Block) -> int:
    return sign(sum(i>j for i in a for j in b))


@lru_cache(None)
def coproduct(w: Word) -> dict[tuple[Word, Word], int]:
    """Degreewise dual of Yoneda multiplication in the normalized dual basis."""
    out = {}
    for k in range(len(w)+1):
        put(out, (w[:k], w[k:]), 1)
    for k, block in enumerate(w):
        for n in range(1, len(block)):
            for a in combinations(block, n):
                b = tuple(i for i in block if i not in a)
                put(out, (w[:k]+(a,), (b,)+w[k+1:]), wedge_sign(a,b))
    return out


def coaction(w: Word) -> dict[tuple[Word, Word], int]:
    """Tor(I_sigma) comodule; omit the empty ideal suffix."""
    if not w:
        raise ValueError('An ideal word must be nonempty.')
    return {(a,b):v for (a,b),v in coproduct(w).items() if b}


def iter_coprod(w: Word, left: bool) -> dict:
    out = {}
    for (a,b), v in coproduct(w).items():
        if left:
            for (c,e), k in coproduct(a).items():
                put(out, (c,e,b), v*k)
        else:
            for (c,e), k in coproduct(b).items():
                put(out, (a,c,e), v*k)
    return out


def iter_coaction(w: Word, left: bool) -> dict:
    out = {}
    for (a,b), v in coaction(w).items():
        if left:
            for (c,e), k in coproduct(a).items():
                put(out, (c,e,b), v*k)
        else:
            for (c,e), k in coaction(b).items():
                put(out, (a,c,e), v*k)
    return out


def perm_sign(seq) -> int:
    return sign(sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq))))


def geometric_permutation(rot: int, ref: int) -> tuple[int, ...]:
    diags = tuple(tuple(map(int, a)) for a in LABELS)
    images = []
    for a,b in diags:
        z = tuple(sorted(((2*rot+sign(ref)*a)%6, (2*rot+sign(ref)*b)%6)))
        images.append(diags.index(z))
    return tuple(images)


def act_word(w: Word, p: tuple[int, ...]) -> tuple[int, Word]:
    sg, out = 1, []
    for a in w:
        aa = tuple(p[i] for i in a)
        sg *= perm_sign(aa)
        out.append(tuple(sorted(aa)))
    return sg, tuple(out)


def act_vec(v: Vec, p: tuple[int, ...]) -> Vec:
    out = {}
    for (m,w), c in v.items():
        mm = [0]*6
        for i,e in enumerate(m):
            mm[p[i]] = e
        sg, ww = act_word(w,p)
        put(out, (tuple(mm),ww), sg*c)
    return out


def cross(a: str, b: str) -> bool:
    i,j = map(int,a)
    k,l = map(int,b)
    return i<k<j<l or k<i<l<j


def channel_data() -> list[dict]:
    out = []
    for side in (0,1):
        active = tuple(range(3*side,3*side+3))
        inactive = tuple(range(3*(1-side),3*(1-side)+3))
        for n in range(1,4):
            for ns in combinations(inactive,n):
                ps = tuple(p for p in active if all(not cross(LABELS[p],LABELS[q]) for q in ns))
                ls = tuple(l for l in LONGS if all(not cross(l,LABELS[q]) for q in ns))
                num = tuple(l for l in LONGS if l not in ls)
                beta = tuple(-int(i in ns or i in ps) for i in range(6))
                out.append({'side':side,'inactive':ns,'active_poles':ps,
                            'normal_exponents':beta,'long_numerator':num,
                            'endpoint':n==3})
    return out


def cover() -> tuple[tuple[int,...], ...]:
    out = []
    for n in range(1,8):
        for u in combinations(range(7),n):
            plus = any(1<=i<=3 for i in u)
            minus = any(4<=i<=6 for i in u)
            if not (plus and minus):
                out.append(u)
    return tuple(out)


COVER = cover()


def allowed(alpha: tuple[int,int,int], beta: Mon, u: tuple[int,...], side: int) -> bool:
    """Monomial coefficient of I_side on the exact named intersection."""
    ids = tuple(i-1 for i in u if i)
    live = None if not ids else ids[0]//3
    if live is not None and live != side:
        return False
    if live is None:
        return all(e>=0 for e in alpha) and any(alpha)
    inverted_x = {i%3 for i in ids}
    if any(e<0 and j not in inverted_x for j,e in enumerate(alpha)):
        return False
    if 0 not in u and any(e<0 and i//3 != side for i,e in enumerate(beta)):
        return False
    return True


def unit_rank(matrix: list[list[int]], columns: int) -> int:
    """Integral elimination, requiring all nonzero Smith factors to be units."""
    a = [row[:] for row in matrix]
    rows = len(a)
    k = 0
    while k < min(rows,columns):
        pos = next(((i,j) for i in range(k,rows) for j in range(k,columns) if abs(a[i][j])==1),None)
        if pos is None:
            break
        i,j = pos
        a[k],a[i] = a[i],a[k]
        for row in a:
            row[k],row[j] = row[j],row[k]
        if a[k][k] < 0:
            a[k] = [-v for v in a[k]]
        for i in range(rows):
            if i != k and a[i][k]:
                c = a[i][k]
                a[i] = [x-c*y for x,y in zip(a[i],a[k])]
        for j in range(columns):
            if j != k and a[k][j]:
                c = a[k][j]
                for i in range(rows):
                    a[i][j] -= c*a[i][k]
        k += 1
    check(not any(a[i][j] for i in range(k,rows) for j in range(k,columns)),
          'cech_nonzero_smith_factors_are_units')
    return k


def cech_monomial(alpha, beta, side) -> dict:
    bases = [tuple(u for u in COVER if len(u)==q+1 and allowed(alpha,beta,u,side)) for q in range(4)]
    mats = []
    ranks = []
    for q in range(3):
        source = {u:i for i,u in enumerate(bases[q])}
        a = [[0]*len(source) for _ in bases[q+1]]
        for i,u in enumerate(bases[q+1]):
            for k in range(len(u)):
                v = u[:k]+u[k+1:]
                if v in source:
                    a[i][source[v]] += sign(k)
        mats.append(a)
        ranks.append(unit_rank(a,len(source)))
    for q in range(2):
        a,b = mats[q+1],mats[q]
        check(all(sum(a[i][k]*b[k][j] for k in range(len(b)))==0
                  for i in range(len(a)) for j in range(len(bases[q]))), 'cech_d_squared')
    hs = [len(bases[q])-(ranks[q-1] if q else 0)-(ranks[q] if q<3 else 0) for q in range(4)]
    return {'bases':bases,'differentials':mats,'ranks':ranks,'cohomology':hs}


def actual_cocycle(c: dict) -> dict[tuple[int,int],int]:
    return {(0,i+1):1 for i in range(3*c['side'],3*c['side']+3)}


def serialize_word(w):
    return [[LABELS[i] for i in a] for a in w]


def main(output: Path, max_degree: int=6) -> None:
    if not 3<=max_degree<=8:
        raise ValueError('--max-degree must be from 3 through 8; degree 6 is the default.')
    generated = {n:words(n) for n in range(max_degree+1)}
    mons = [ZERO]+[tuple(int(i==j) for i in range(6)) for j in range(6)]
    pairs = tuple((i,j) for side in (0,1) for i,j in combinations(range(3*side,3*side+3),2))
    # Check the all-degree primal formulas at bounded words; every operator
    # is B-linear, so monomial coefficients need not be sampled for its identities.
    for n,ws in generated.items():
        for w in ws:
            v = {(ZERO,w):1}
            check(not d(d(v)), 'resolution_d_squared',w)
            check(add(d(aug_h(v)),aug_h(d(v))) == (v if w else {}), 'resolution_unit_word_contraction',w)
            for i in range(6):
                check(not add(d(op(i,v)),op(i,d(v))), 'yoneda_generator_is_end_cocycle',(w,i))
                check(not op(i,op(i,v)), 'yoneda_square_zero',(w,i))
            for i,j in pairs:
                check(not add(op(i,op(j,v)),op(j,op(i,v))), 'same_sheet_anticommutator_zero',(w,i,j))
            check(epsilon(operator(w,v))==sign(n*(n-1)//2), 'normal_word_unit_diagonal_pairing',w)
            check(iter_coprod(w,True)==iter_coprod(w,False),'coalgebra_coassociativity',w)
            check({b:k for (a,b),k in coproduct(w).items() if not a}=={w:1},'coalgebra_left_counit',w)
            check({a:k for (a,b),k in coproduct(w).items() if not b}=={w:1},'coalgebra_right_counit',w)
            if w:
                check(iter_coaction(w,True)==iter_coaction(w,False),'ideal_comodule_coassociativity',w)
                check(all(b and b[-1][0]//3==w[-1][0]//3 for a,b in coaction(w)), 'ideal_channel_polarity_preserved',w)
    # Independently test all dual-basis entries through degree 4, not just diagonals.
    for n in range(min(max_degree,4)+1):
        for w in generated[n]:
            for v in generated[n]:
                got = epsilon(operator(w,{(ZERO,v):1}))
                check(got==(sign(n*(n-1)//2) if w==v else 0),'full_yoneda_pairing_matrix',(w,v))
    for n in range(min(max_degree,4)+1):
        for w in generated[n]:
            for m in mons:
                v={(m,w):1}
                expected={} if not w and m==ZERO else v
                check(add(d(aug_h(v)),aug_h(d(v)))==expected,'monomial_resolution_contraction',(m,w))
    # Associativity is audited exhaustively by total degree, including zeros.
    for n in range(max_degree+1):
        for i in range(n+1):
            for j in range(n-i+1):
                k=n-i-j
                for u in generated[i]:
                    for v in generated[j]:
                        for w in generated[k]:
                            a,x=mul(u,v);b,y=mul(x,w) if a else (0,())
                            c,z=mul(v,w);e,t=mul(u,z) if c else (0,())
                            left={} if not a*b else {y:a*b}
                            right={} if not c*e else {t:c*e}
                            check(left==right,'yoneda_all_associativity',(u,v,w))
    # The coproduct is checked against every product of complementary degree.
    for n in range(max_degree+1):
        for i in range(n+1):
            for u in generated[i]:
                for v in generated[n-i]:
                    sg,w=mul(u,v)
                    if sg:
                        check(coproduct(w).get((u,v),0)==sg,'coproduct_dual_to_yoneda_product',(u,v))
                    elif n<=3:
                        check(all((u,v) not in coproduct(w) for w in generated[n]),
                              'zero_wedge_has_no_coproduct_entry',(u,v))
    # Check product/operator equality on higher inputs, not just on P_{i+j}.
    small=tuple(w for n in range(3) for w in generated[n])
    for u in small:
        for v in small:
            sg,w=mul(u,v)
            for n in range(degree(u)+degree(v),min(max_degree,5)+1):
                for z in generated[n]:
                    inp={(ZERO,z):1}
                    lhs=operator(u,operator(v,inp))
                    rhs=scale(operator(w,inp),sg) if sg else {}
                    check(lhs==rhs,'multiplication_is_actual_operator_composition',(u,v,z))
    # Labelled dihedral covariance of actual chain maps and coalgebra signs.
    for rot,ref in product(range(3),range(2)):
        p=geometric_permutation(rot,ref)
        for n in range(min(max_degree,4)+1):
            for w in generated[n]:
                v={(ZERO,w):1}
                check(act_vec(d(v),p)==d(act_vec(v,p)), 'resolution_dihedral_chain_action',(rot,ref,w))
                for i in range(6):
                    check(act_vec(op(i,v),p)==op(p[i],act_vec(v,p)), 'yoneda_dihedral_covariance',(rot,ref,w,i))
                sg,ww=act_word(w,p)
                left=scale(coproduct(ww),sg);right={}
                for (a,b),c in coproduct(w).items():
                    sa,aa=act_word(a,p);sb,bb=act_word(b,p)
                    put(right,(aa,bb),c*sa*sb)
                check(left==right,'coproduct_dihedral_covariance',(rot,ref,w))
    # E-module of each conductor-vanishing channel: left ideal of words ending there,
    # with degree reduced by one. All six first module relations are checked.
    for side in (0,1):
        labels=range(3*side,3*side+3)
        for i in labels:
            sg,_=mul(((i,),),((i,),))
            check(sg==0,'channel_generator_square_relation',(side,i))
        for i,j in combinations(labels,2):
            check(not add(mul_vec({((i,),):1},{((j,),):1}),mul_vec({((j,),):1},{((i,),):1})),
                  'channel_generator_exterior_relation',(side,i,j))
        for n in range(1,max_degree+1):
            for w in generated[n]:
                if w[-1][0]//3 != side:
                    continue
                i=w[-1][-1]
                a=w[-1][:-1]
                u=w[:-1]+((a,) if a else ())
                sg,ww=mul(u,((i,),))
                check((sg,ww)==(1,w),'all_channel_classes_generated_in_degree_zero',w)
    channels=channel_data()
    end=[j for j,c in enumerate(channels) if c['endpoint']]
    check(len(channels)==14 and len(end)==2,'fourteen_channels_and_both_endpoints')
    retained=[j for j in range(14) if j not in end]
    renumber={j:k for k,j in enumerate(retained)}
    def full_module_action(a, vector):
        out={}
        for (j,w),v in vector.items():
            sg,ww=mul(a,w)
            if sg:
                if ww[-1][0]//3 != channels[j]['side']:
                    raise AssertionError('Wrong full module sheet')
                put(out,(j,ww),v*sg)
        return out
    def forget(vector):
        return {(renumber[j],w):v for (j,w),v in vector.items() if j in renumber}
    def reduced_module_action(a, vector):
        out={}
        for (j,w),v in vector.items():
            sg,ww=mul(a,w)
            if sg:
                if ww[-1][0]//3 != channels[retained[j]]['side']:
                    raise AssertionError('Wrong reduced module sheet')
                put(out,(j,ww),v*sg)
        return out
    for n in range(max_degree):
        qplus=[w for w in generated[n+1] if w[-1][0]//3==0]
        qminus=[w for w in generated[n+1] if w[-1][0]//3==1]
        check(len(qplus)==len(qminus),'two_sheet_channel_ranks',n)
        for j,c in enumerate(channels):
            ws=qplus if c['side']==0 else qminus
            for w in ws:
                for a in range(6):
                    sg,v=mul(((a,),),w)
                    check(not sg or v[-1][0]//3==c['side'],'all_channel_actions_preserve_endpoint_label',(j,a,w))
                    # Projection forgetting endpoints acts on channel labels, not words.
                    source={(j,w):1}
                    lhs=forget(full_module_action(((a,),),source))
                    rhs=reduced_module_action(((a,),),forget(source))
                    check(lhs==rhs,'endpoint_forgetting_intertwines_yoneda',(j,a,w))
    # Negative control: a multigraded Tor equivalence need not respect its coaction.
    xy=((0,),(3,));yx=((3,),(0,))
    delta_xy={k:v for k,v in coproduct(xy).items() if k[0] and k[1]}
    delta_yx={k:v for k,v in coproduct(yx).items() if k[0] and k[1]}
    check(delta_xy!=delta_yx,'rank_preserving_cross_word_swap_not_coalgebra_map')
    wa=((0,),(3,),(1,));wb=((1,),(3,),(0,));lower=((3,),(1,));a=((0,),)
    sg,w=mul(a,lower)
    check(sg==1 and w==wa and wa!=wb,'same_channel_tor_swap_fails_operation_naturality')
    check(sorted(i for b in wa for i in b)==sorted(i for b in wb for i in b),
          'nonadmissible_swap_preserves_full_occurrence_multigrade')

    # Global framed moduli: all finite sign patterns determining H^0 and H^1.
    hist=Counter();patterns=0
    for side in (0,1):
        for alpha in product((-1,0,1),repeat=3):
            for beta in product((-1,0),repeat=6):
                c=cech_monomial(alpha,beta,side);hs=c['cohomology'];patterns+=1
                global_section=int(all(a>=0 for a in alpha) and any(alpha)
                                   and all(e>=0 or i//3==side for i,e in enumerate(beta)))
                obstruction=int(not any(alpha) and any(e<0 and i//3!=side for i,e in enumerate(beta)))
                check(hs[0]==global_section,'global_framed_automorphism_monomials',(side,alpha,beta))
                check(hs[1]==obstruction,'global_framed_extension_monomials',(side,alpha,beta))
                hist[tuple(hs)]+=1
    # Every actual residue, including both endpoint residues, is checked in the Cech
    # matrix that contains it. Its own opposite pole subset is its exact C-annihilator.
    residue_records=[]
    for j,f in enumerate(channels):
        c=cech_monomial((0,0,0),f['normal_exponents'],f['side'])
        coc=actual_cocycle(f)
        v=[coc.get(u,0) for u in c['bases'][1]]
        check(not c['bases'][0], 'actual_residue_has_no_zero_cochain_filler',j)
        check(c['cohomology'][1]==1 and any(v),'actual_residue_nonzero_class',j)
        check(all(sum(x*y for x,y in zip(row,v))==0 for row in c['differentials'][1]),
              'actual_residue_triple_overlap_cocycle',j)
        for bits in product((0,1),repeat=6):
            beta=tuple(x+y for x,y in zip(f['normal_exponents'],bits))
            cc=cech_monomial((0,0,0),beta,f['side'])
            expected=int(all(bits[i] for i in f['inactive']))
            check((cc['cohomology'][1]==0)==bool(expected),'channel_exact_normal_annihilator',(j,bits))
        residue_records.append({'index':j,'sheet':'+' if f['side']==0 else '-',
            'inactive':[LABELS[i] for i in f['inactive']], 'endpoint':f['endpoint'],
            'residue_t_exponents':dict(zip(LABELS,f['normal_exponents'])),
            'residue_u_numerator':list(f['long_numerator']),
            'scalar_multiplier_annihilator':'*'.join('t'+LABELS[i] for i in f['inactive']),
            'cech_basis_dimensions':[len(v) for v in c['bases']],
            'cech_differential_ranks':c['ranks'], 'cocycle':[[list(u),v] for u,v in coc.items()]})
    for bits in product((0,1),repeat=6):
        killed_all=all(all(bits[i] for i in f['inactive']) for f in channels)
        killed_end=all(all(bits[i] for i in channels[j]['inactive']) for j in end)
        check(killed_all==all(bits)==killed_end,'endpoint_pair_detects_full_cyclic_class',bits)
    # Genuine extension automorphisms are unipotent shears. The matrix identities
    # are audited coordinatewise without dividing any coefficient or parameter.
    def matrix_product(a,b):
        out={}
        for (i,k),x in a.items():
            for (l,j),y in b.items():
                if k==l:
                    put(out,(i,j),x*y)
        return out
    identity={(j,j):1 for j in range(15)}
    for j in range(14):
        for k in range(14):
            nj={(j+1,0):1};nk={(k+1,0):1}
            check(not matrix_product(nj,nk),'framed_shear_cross_products_zero',(j,k))
            tj=add(identity,nj);tk=add(identity,nk)
            check(matrix_product(tj,tk)==add(identity,nj,nk),'framed_automorphism_addition_law',(j,k))
            check(matrix_product(tj,add(identity,scale(nj,-1)))==identity,'framed_automorphism_inverse',j)
    check([sum(len(u)==n for u in COVER) for n in range(1,5)]==[7,12,8,2],'whole_named_cover_retained')


    # Actual frame automorphisms on the central source resolution. A loop is a
    # GLOBAL ideal section f. Resolve its shear by lifting every monomial into
    # one degree-zero ideal generator; only its linear monomials survive C tensor.
    # Model vector keys: (occurrence monomial, channel, word), channel=-1 generic.
    def bmul(m,n):
        sm=side_of_monomial(m);sn=side_of_monomial(n)
        if sm is not None and sn is not None and sm!=sn:
            return None
        return tuple(x+y for x,y in zip(m,n))
    def rd(vector):
        out={}
        for (m,j,w),v in vector.items():
            if j==-1 or degree(w)==1:
                continue
            for (mm,ww),c in d({(m,w):v}).items():
                put(out,(mm,j,ww),c)
        return out
    def lift_loop(loop):
        out={}
        for (j,m),v in loop.items():
            if not any(m) or side_of_monomial(m)!=channels[j]['side']:
                raise ValueError('A framed loop must lie in its channel ideal.')
            i=min(i for i,e in enumerate(m) if e)
            mm=list(m);mm[i]-=1
            put(out,(tuple(mm),j,((i,),)),v)
        return out
    def shear(loop,vector):
        out=dict(vector);tail=lift_loop(loop)
        for (m,j,w),v in vector.items():
            if j!=-1:
                continue
            for (mm,k,ww),c in tail.items():
                prod=bmul(m,mm)
                if prod is not None:
                    put(out,(prod,k,ww),v*c)
        return out
    def conductor_reduce(vector):
        return {(j,w):v for (m,j,w),v in vector.items() if m==ZERO}
    def first_jet(loop):
        out={}
        for (j,m),v in loop.items():
            if sum(m)==1:
                i=m.index(1)
                put(out,(j,((i,),)),v)
        return out
    def expected_conductor_action(loop,vector):
        reduced=conductor_reduce(vector);out=dict(reduced)
        scalar=reduced.get((-1,()),0)
        for k,c in first_jet(loop).items():
            put(out,k,scalar*c)
        return out
    loops=[]
    for j,c in enumerate(channels):
        for exponents in product(range(4),repeat=3):
            if not 1<=sum(exponents)<=3:
                continue
            m=tuple(exponents)+(0,0,0) if c['side']==0 else (0,0,0)+tuple(exponents)
            loop={(j,m):1};loops.append(loop)
            ll=lift_loop(loop)
            check(not rd(ll),'framed_loop_resolves_to_closed_ideal_column',(j,m))
            check(conductor_reduce(ll)==first_jet(loop),'derived_framed_transport_is_first_conductor_derivative',(j,m))
            check(bool(conductor_reduce(ll))==(sum(m)==1),'framed_transport_exact_quadratic_kernel',(j,m))
            for coeff in mons:
                inp={(coeff,-1,()):1}
                actual=shear(loop,inp)
                check(rd(actual)==shear(loop,rd(inp)),'source_framed_shear_chain_map_generic',(j,m,coeff))
                check(conductor_reduce(actual)==expected_conductor_action(loop,inp),
                      'full_derived_transport_first_jet_formula',(j,m,coeff))
                check(shear(scale(loop,-1),actual)==inp,'resolved_framed_transport_inverse',(j,m,coeff))
    unit={(ZERO,-1,()):1}
    for f in loops:
        for g in loops:
            check(shear(f,shear(g,unit))==shear(add(f,g),unit),'resolved_additive_group_action',None)
    # Check all source ideal differential columns through cohomological degree 3.
    # The lift changes the generic source column only, and all higher source
    # columns are ideal columns; use actual differentials to verify this fact.
    sample_loops=(loops[0],loops[-1],add(loops[0],loops[-1]))
    for j,c in enumerate(channels):
        for n in range(1,min(max_degree,4)+1):
            for w in generated[n]:
                if w[-1][0]//3!=c['side']:
                    continue
                inp={(ZERO,j,w):1}
                for f in sample_loops:
                    check(rd(shear(f,inp))==shear(f,rd(inp)), 'source_framed_shear_all_ideal_chain_columns',(j,w))
                    check(conductor_reduce(shear(f,inp))==conductor_reduce(inp),
                          'source_framed_shear_fixes_all_positive_Tor_channels',(j,w))
    # Pure-branch frame sections are global iff their negative spectator powers
    # occur on their own normal triple. Its linear coefficient image is C_sigma^21.
    for j,c in enumerate(channels):
        for i in range(3):
            alpha=tuple(int(k==i) for k in range(3))
            for beta in product((-1,0),repeat=6):
                cc=cech_monomial(alpha,beta,c['side'])
                check(cc['cohomology'][0]==int(all(e>=0 or k//3==c['side'] for k,e in enumerate(beta))),
                      'global_first_jet_image_exact_spectator_lattice',(j,i,beta))

    prior=Path(__file__).with_name('replayed_intrinsic_conductor_for_yoneda_20260907.json')
    replay=None
    if prior.exists():
        p=json.loads(prior.read_text())
        replay={'filename':prior.name,'sha256':hashlib.sha256(prior.read_bytes()).hexdigest(),
                'assertions':p.get('total_exact_assertions')}
    result={
      'status':'explicit_all_degree_Yoneda_dga_and_global_framed_extension_groupoid',
      'date':'2026-09-07','lane':'Branch B','baseline_commit':COMMIT,
      'new_all_degree_results':{
        'Ext_algebra':'Lambda_C(xi13,xi15,xi35) *_C Lambda_C(eta02,eta04,eta24)',
        'generator_degrees':1,'square_relations':6,'same_sheet_anticommutator_relations':6,
        'mixed_relations':'none',
        'dga_model':'As C-dg algebras, the zero-differential algebra embeds by six last-block contractions into End_B(P) and is a multiplicative quasi-isomorphism. This is not a strict B-dg-algebra map.',
        'operator':'T_i(w)=(-1)^(degree(prefix)+position(i,last))*(word with i deleted from last block), or 0.',
        'full_word_pairing':'epsilon T_w(v)=(-1)^(n*(n-1)/2) delta(w,v) for words of degree n.',
        'channel_module':'Ext^n_B(I_sigma,C)=(E E_sigma^{>0})^{n+1}; action by left Yoneda multiplication.',
        'whole_source_module':'Ext_B^*(S14,C)=C_triv + 7 shifted positive left ideals + 7 shifted negative left ideals, on D(T) only.',
        'global_warning':'Local multiplicative formality is not global splitting. It does not remove endpoint transitions.'},
      'bounded_verification':{
        'operator_max_input_degree':max_degree,
        'all_pairing_entries_max_degree':min(max_degree,4),
        'all_associativity_max_total_degree':max_degree,
        'all_coproduct_max_degree':max_degree,
        'actual_operator_composition_max_input_degree':min(max_degree,5),
        'same_degree_monomials_for_contraction':len(mons),
        'global_complete_sign_patterns':patterns,
        'cech_pattern_histogram':[{'cohomology_ranks':list(k),'patterns':v} for k,v in sorted(hist.items())]},
      'graded_ranks':{'conductor':[len(generated[n]) for n in range(max_degree+1)],
        'one_channel':[sum(w[-1][0]//3==0 for w in generated[n+1]) for n in range(max_degree)],
        'S14':[int(n==0)+7*len(generated[n+1]) for n in range(max_degree)]},
      'negative_controls':{
        'coalgebra_swap_words':[serialize_word(xy),serialize_word(yx)],
        'coalgebra_swap_reduced_coproducts':[
            [[serialize_word(a),serialize_word(b),v] for (a,b),v in x.items()] for x in (delta_xy,delta_yx)],
        'one_channel_multigraded_swap':[serialize_word(wa),serialize_word(wb)],
        'coaction_naturality_failure':'Fixes degree-zero and degree-one channel data, changes xi13*(eta02*xi15). It cannot be E-linear.',
        'endpoint_deletion':'Remains equivalent on the entire derived conductor fibre, including coaction, because the local triangular change is B-linear. Not a counterexample to local functoriality.'},
      'global_framed_extension_moduli':{
        'object':'Map_D(O_V)(O_V,M14[1]), M14=7 Iplus + 7 Iminus with channel grading lines',
        'pi0':'(C_T/C_plus)^7 + (C_T/C_minus)^7',
        'pi1':'Iplus[tplus^-1]^7 + Iminus[tminus^-1]^7',
        'pi_n_n_ge_2':'0',
        'frame':'Identity on generic quotient and all fourteen labelled kernel channels. No native physical identification.',
        'endpoint_multiplier_classes':'C/(tau_minus) + C/(tau_plus)',
        'endpoint_preserving_equivalence':'Changing two endpoint multipliers gives equivalent framed extensions iff their differences lie in (tau_minus) and (tau_plus), respectively.',
        'all_degrees_no_repair':'Any derived frame-preserving equivalence of resolutions induces an equivalence of short exact sequences on H^0; therefore a nonzero residue-difference class cannot be removed by higher homotopies.',
        'separate_obstruction':'This compares generic-extension objects with all kernel labels fixed. It is not the endpoint-forgetting Ext^1(S12,Nend) problem, whose annihilator is different.'},
      'global_frame_action_on_intrinsic_markings':{
        'acting_group':'A=Gamma(V,M14)=Iplus[tau_plus^-1]^7 + Iminus[tau_minus^-1]^7',
        'resolved_action':'id + lift(f)*generic_projection; lifts add and their cross products vanish',
        'derived_action':'On generic coefficient 1, translate the 42 degree-zero channel coordinates by df|D. All positive-degree Tor coordinates are unchanged.',
        'action_kernel':'K2=(Iplus^2)[tau_plus^-1]^7 + (Iminus^2)[tau_minus^-1]^7',
        'first_jet_image':'C_plus^21 + C_minus^21 inside C_T^42',
        'homotopy_quotient':'Y_r = X14 // A, for a fixed globally framed source S14(r)',
        'pi0':'(C_T/C_plus)^21 + (C_T/C_minus)^21',
        'pi1_at_chosen_component':'C_T^168 direct-sum K2',
        'pi_n_n_ge_2':'C_T^(14*b_n), with b(z)=(3+3z+z^2)/(1-3z-3z^2-z^3)',
        'scope':'Explicit labelled central-frame model. These are automorphisms of the whole fixed coefficient source, not paths allowed to change its nonzero extension class.',
        'first_derivative_not_prime_derivative':True,
        'homotopy_group_category':'Additive groups/modules over the unlocalized spectator ring. C_T/C_sigma is not a quotient ring and not generally a C_T-module.',
        'loop_monomial_test_count':len(loops)},
      'channel_residues':residue_records,
      'replayed_predecessor':replay,
      'assertions':dict(sorted(COUNTS.items())),
      'total_exact_assertions':sum(COUNTS.values()),
      'limitations':['No physical native-source equivalence.',
        'No identification of the test open with a physical generic deformation.',
        'No claim of integer-prime torsion or nontrivial Whitehead products in the additive Dold-Kan fibre.',
        'Local Yoneda formality does not imply formality of the global residue diagram.',
        'Arbitrary degree and coefficient exponents follow from the proofs; the certificate tests finite instances.',
        'No proof-assistant verification and no repository writes.']}
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'total_exact_assertions':result['total_exact_assertions'],
                      'ranks':result['graded_ranks'],'sign_patterns':patterns,
                      'replayed_predecessor':replay},indent=2))


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path('marici_conductor_yoneda_and_global_frames_certificate_20260907.json'))
    parser.add_argument('--max-degree',type=int,default=6)
    args=parser.parse_args()
    main(args.output,args.max_degree)
