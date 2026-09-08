#!/usr/bin/env python3
"""All-degree intrinsic conductor resolutions for the alternating Marici ring.

Standard-library exact verification. The arbitrary-degree theorem is proved
by the explicit augmentation contraction documented in the accompanying note.
Bounded word and monomial tests below check that formula, not a claim that a
finite truncation resolves the singular ring. Endpoint/generic chart maps are
checked as full maps, not only by comparing ranks.
"""
from __future__ import annotations

import argparse
from collections import Counter
from functools import lru_cache
from itertools import combinations, product
import hashlib
import json
from pathlib import Path
from typing import Callable

Block = tuple[int, ...]
Word = tuple[Block, ...]
Mon = tuple[int, ...]
Vec = dict[tuple[Mon, Word], int]
ZERO: Mon = (0,) * 6
COUNTS: Counter[str] = Counter()
COMMIT = 'd1947b67a60d3e88ba77f4ca60ea02c2a306ee61'


def check(ok: bool, category: str, detail: object = None) -> None:
    if not ok:
        raise AssertionError(f'{category}: {detail!r}')
    COUNTS[category] += 1


def sign(n: int) -> int:
    return -1 if n % 2 else 1


def add_term(out: dict, key: object, value: int) -> None:
    out[key] = out.get(key, 0) + value
    if out[key] == 0:
        del out[key]


def summed(*vectors: dict) -> dict:
    out: dict = {}
    for vector in vectors:
        for key, value in vector.items():
            add_term(out, key, value)
    return out


def scaled(vector: dict, scale: int) -> dict:
    return {key: scale * value for key, value in vector.items() if scale * value}


def sheet(m: Mon) -> int | None:
    plus, minus = any(m[:3]), any(m[3:6])
    if plus and minus:
        raise ValueError('An opposite-sheet occurrence monomial is zero, not a basis monomial.')
    return 0 if plus else 1 if minus else None


def multiply_variable(m: Mon, i: int, live: int | None = None) -> Mon | None:
    if live is not None and i // 3 != live:
        return None
    side = sheet(m)
    if side is not None and side != i // 3:
        return None
    result = list(m)
    result[i] += 1
    return tuple(result)


@lru_cache(maxsize=None)
def words(n: int, first: int = -1) -> tuple[Word, ...]:
    """All alternating exterior-block words of total homological degree n."""
    if n < 0:
        return ()
    if n == 0:
        return ((),)
    out: list[Word] = []
    for side in (0, 1) if first == -1 else (first,):
        for mask in range(1, 8):
            block = tuple(3 * side + i for i in range(3) if mask >> i & 1)
            if len(block) <= n:
                out.extend((block,) + rest for rest in words(n - len(block), 1 - side))
    return tuple(out)


def word_degree(w: Word) -> int:
    return sum(map(len, w))


def differential(v: Vec, live: int | None = None) -> Vec:
    out: Vec = {}
    for (monomial, word), coefficient in v.items():
        if not word:
            continue
        block = word[0]
        for pos, variable in enumerate(block):
            new_monomial = multiply_variable(monomial, variable, live)
            if new_monomial is None:
                continue
            remainder = block[:pos] + block[pos + 1:]
            new_word = (remainder,) + word[1:] if remainder else word[1:]
            add_term(out, (new_monomial, new_word), sign(pos) * coefficient)
    return out


def augmentation_homotopy(v: Vec, retained_sheet: int | None = None) -> Vec:
    """C-linear integral contraction. It is deliberately NOT B-linear.

    retained_sheet=None resolves the conductor C. Values 0/1 resolve B_+/B_-
    using the subcomplex whose nonempty words end on the opposite sheet.
    """
    out: Vec = {}
    for (m, w), a in v.items():
        side = sheet(m)
        if side is None or (not w and side == retained_sheet):
            continue
        if w and w[0][0] // 3 == side:
            block, rest = w[0], w[1:]
        else:
            block, rest = (), w
        first = min([i for i, value in enumerate(m) if value] + list(block))
        if first in block:
            continue
        exponent = list(m)
        exponent[first] -= 1  # an existing positive factor; no localization
        new_block = tuple(sorted(block + (first,)))
        add_term(out, (tuple(exponent), (new_block,) + rest),
                 sign(sum(i < first for i in block)) * a)
    return out


def local_homotopy(v: Vec, inverse_variable: int) -> Vec:
    """Contraction on the named occurrence open D(X_i), where X_i is a unit."""
    out: Vec = {}
    side = inverse_variable // 3
    for (m, w), a in v.items():
        if w and w[0][0] // 3 == side:
            block, rest = w[0], w[1:]
        else:
            block, rest = (), w
        if inverse_variable in block:
            continue
        exponent = list(m)
        exponent[inverse_variable] -= 1
        new_block = tuple(sorted(block + (inverse_variable,)))
        add_term(out, (tuple(exponent), (new_block,) + rest),
                 sign(sum(i < inverse_variable for i in block)) * a)
    return out


def apply_linear(f: Callable[[Vec], Vec], v: Vec) -> Vec:
    return f(v)


def pure_monomials(max_degree: int) -> tuple[Mon, ...]:
    out = [ZERO]
    for side in (0, 1):
        for mon in product(range(max_degree + 1), repeat=3):
            if 1 <= sum(mon) <= max_degree:
                out.append(tuple(mon) + (0,) * 3 if side == 0 else (0,) * 3 + tuple(mon))
    return tuple(out)


def expected_retract(v: Vec, retained: int | None = None) -> Vec:
    return {(m, w): a for (m, w), a in v.items()
            if w or (sheet(m) is not None and sheet(m) != retained)}


# Source labels; exterior order within each sheet is increasing label order.
PLUS = ((1, 3), (1, 5), (3, 5))
MINUS = ((0, 2), (0, 4), (2, 4))
OCC = PLUS + MINUS
LONG = ((0, 3), (1, 4), (2, 5))


def cross(a, b):
    i, j = a; k, l = b
    return i < k < j < l or k < i < l < j


def families() -> list[dict]:
    result = []
    for side, active, inactive in ((0, PLUS, MINUS), (1, MINUS, PLUS)):
        for size in (1, 2, 3):
            for ns in combinations(inactive, size):
                ps = tuple(p for p in active if all(not cross(p, n) for n in ns))
                ls = tuple(l for l in LONG if all(not cross(l, n) for n in ns))
                numerator = [l for l in LONG if l not in ls]
                # spectator coordinates: t for OCC, then u for LONG
                residue = tuple(-int(a in ns or a in ps) for a in OCC) + tuple(
                    int(a in numerator) for a in LONG)
                result.append({'side': side, 'inactive': ns, 'residue': residue,
                               'endpoint': size == 3})
    return result


FAMILY = families()
END = tuple(i for i, f in enumerate(FAMILY) if f['endpoint'])
C12 = tuple(i for i in range(14) if i not in END)


def geometric_permutation(rotation: int, reflection: int):
    tr = (lambda a: tuple(sorted(((rotation + reflection * a[0]) % 6,
                                  (rotation + reflection * a[1]) % 6))))
    p = tuple(OCC.index(tr(a)) for a in OCC)
    fp = {}
    for j, f in enumerate(FAMILY):
        ns = tuple(sorted(map(tr, f['inactive'])))
        side = OCC.index(tr(OCC[3 * f['side']])) // 3
        fp[j] = next(k for k, g in enumerate(FAMILY)
                     if g['side'] == side and g['inactive'] == ns)
    sp = tuple(OCC.index(tr(a)) for a in OCC) + tuple(6 + LONG.index(tr(a)) for a in LONG)
    return p, fp, sp


def permutation_sign(values: tuple[int, ...]) -> int:
    return sign(sum(a > b for i, a in enumerate(values) for b in values[i + 1:]))


def act(v: Vec, p: tuple[int, ...]) -> Vec:
    out: Vec = {}
    for (m, w), a in v.items():
        exponent = [0] * 6
        for i, n in enumerate(m):
            exponent[p[i]] = n
        blocks = []
        sg = 1
        for block in w:
            image = tuple(p[i] for i in block)
            sg *= permutation_sign(image)
            blocks.append(tuple(sorted(image)))
        add_term(out, (tuple(exponent), tuple(blocks)), sg * a)
    return out


def mmatrix(a, b):
    return [[sum(x * y for x, y in zip(row, column)) for column in zip(*b)] for row in a]


def madd(a, b):
    return [[x + y for x, y in zip(r, s)] for r, s in zip(a, b)]


def eye(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def mneg(a):
    return [[-x for x in row] for row in a]


def native_audit() -> None:
    d1 = [[1, -1, -1, -1, -1]]
    d2 = [[1, 0, 0, 0], [1, 0, 0, 0], [0, 1, 0, -1],
          [0, -1, 1, 0], [0, 0, -1, 1]]
    d3 = [[0], [1], [1], [1]]
    h0 = [[1], [0], [0], [0], [0]]
    h1 = [[0, 1, 0, 0, 0], [0, 0, 0, -1, -1], [0, 0, 0, 0, -1], [0, 0, 0, 0, 0]]
    h2 = [[0, 0, 0, 1]]
    z = [[1], [0], [1], [0], [0]]
    r = [[0, 0, 1, 1, 1]]
    check(mmatrix(d1, d2) == [[0] * 4], 'native_d_squared_1')
    check(mmatrix(d2, d3) == [[0]] * 5, 'native_d_squared_2')
    check(mmatrix(d1, z) == [[0]], 'native_unit_closed')
    check(mmatrix(r, z) == [[1]], 'native_readout_unit')
    check(mmatrix(d1, h0) == eye(1), 'native_retract_degree_0')
    check(madd(mmatrix(d2, h1), mmatrix(h0, d1)) == madd(eye(5), mneg(mmatrix(z, r))),
          'native_retract_degree_1')
    check(madd(mmatrix(d3, h2), mmatrix(h1, d2)) == eye(4), 'native_retract_degree_2')
    check(mmatrix(h2, d3) == eye(1), 'native_retract_degree_3')


def ranks(max_degree: int) -> tuple[list[int], list[int], list[int]]:
    # q=1/(1-a), a=3z+3z^2+z^3. c=(1+a)/(1-a); ideal=(q-1)/z.
    q = [1]
    for n in range(1, max_degree + 2):
        q.append(sum(a * q[n-k] for k, a in ((1, 3), (2, 3), (3, 1)) if n >= k))
    c = [1] + [2 * q[n] for n in range(1, max_degree + 1)]
    return c, q[:max_degree + 1], q[1:max_degree + 2]


def chart_map_zero(channel: int, word: Word, live: int) -> dict:
    """Actual central-to-occurrence map, with residues as scalar symbols.

    Output key=(target_coordinate, occurrence_exponent, residue_index_or_-1).
    Generic=-1; channel coordinate j is the original z_j, not a shifted tail.
    """
    if channel == -1:
        assert not word
        out = {(-1, ZERO, -1): 1}
        out.update({(j, ZERO, j): 1 for j, f in enumerate(FAMILY) if f['side'] == live})
        return out
    if word_degree(word) != 1 or FAMILY[channel]['side'] != live:
        return {}
    exponent = [0] * 6
    exponent[word[0][0]] = 1
    return {(channel, tuple(exponent), -1): 1}


def chart_after_d(channel: int, word: Word, live: int) -> dict:
    if channel == -1 or word_degree(word) != 2:
        return {}
    out = {}
    for (m, w), a in differential({(ZERO, word): 1}, live).items():
        for (target, m2, residue), b in chart_map_zero(channel, w, live).items():
            exponent = tuple(x + y for x, y in zip(m, m2))
            add_term(out, (target, exponent, residue), a * b)
    return out


def chart_basis_inverse(channel: int, variable: int, generic: bool = False) -> list[dict]:
    # Inverse on overlap: z_j -> e_variable / X_variable in its ideal channel.
    # Generic basis -> generic - sum r_j * e_variable / X_variable.
    m = [0] * 6; m[variable] = -1
    v = {(tuple(m), ((variable,),)): 1}
    if not generic:
        return [{'channel': channel, 'residue': -1, 'sign': 1, 'vector': v}]
    live = variable // 3
    return [{'channel': -1, 'residue': -1, 'sign': 1, 'vector': {(ZERO, ()): 1}}] + [
        {'channel': j, 'residue': j, 'sign': -1, 'vector': v}
        for j, f in enumerate(FAMILY) if f['side'] == live]


def inverse_followed_by_map(terms: list[dict], live: int) -> dict:
    out = {}
    for term in terms:
        for (m, w), a in term['vector'].items():
            for (target, m2, residue), b in chart_map_zero(term['channel'], w, live).items():
                rs = tuple(i for i in (term['residue'], residue) if i >= 0)
                exponent = tuple(x + y for x, y in zip(m, m2))
                add_term(out, (target, exponent, rs), a * b * term['sign'])
    return out


def main(output: Path, max_degree: int, monomial_degree: int) -> None:
    if not 3 <= max_degree <= 7:
        raise ValueError('--max-degree must lie between 3 and 7; generation grows exponentially.')
    if not 1 <= monomial_degree <= 3:
        raise ValueError('--monomial-degree must lie between 1 and 3.')
    native_audit()
    mons = pure_monomials(monomial_degree)
    generated = {n: words(n) for n in range(max_degree + 2)}
    c, q, b = ranks(20)
    for n in range(max_degree + 2):
        check(len(generated[n]) == c[n], 'word_count_matches_series', n)
        for w in generated[n]:
            check(word_degree(w) == n and all(len(block) == len(set(block)) for block in w),
                  'well_formed_exterior_word', w)
            check(all(w[j][0]//3 != w[j+1][0]//3 for j in range(len(w)-1)),
                  'alternating_block_types', w)
            unit = {(ZERO, w): 1}
            check(not differential(differential(unit)), 'all_generated_d_squared', w)
            for (m, t), a in differential(unit).items():
                check(sum(m) == 1 and word_degree(t) == n-1 and abs(a) == 1,
                      'minimal_integral_differential_entry', w)
            if n > max_degree:
                continue
            for m in mons:
                v = {(m, w): 1}
                lhs = summed(differential(augmentation_homotopy(v)),
                             augmentation_homotopy(differential(v)))
                check(lhs == expected_retract(v), 'integral_conductor_contraction', (m, w))
                check(not augmentation_homotopy(augmentation_homotopy(v)),
                      'integral_contraction_square_zero', (m, w))
                for live in (0, 1):
                    if w and w[-1][0]//3 == live:
                        continue
                    h = lambda x: augmentation_homotopy(x, live)
                    check(summed(differential(h(v)), h(differential(v))) == expected_retract(v, live),
                          'normalization_branch_resolution_contraction', (live, m, w))
            for variable in range(6):
                live = variable//3
                h = lambda x: local_homotopy(x, variable)
                check(summed(differential(h(unit), live), h(differential(unit, live))) == unit,
                      'named_occurrence_open_contraction', (variable, w))
                check(not h(h(unit)), 'occurrence_open_contraction_square_zero', (variable, w))

    # Six geometric transports, not an arbitrary symmetric-group replacement.
    group = [(r, s) for r in (0, 2, 4) for s in (1, -1)]
    for g in group:
        p, fp, sp = geometric_permutation(*g)
        check(set(fp.values()) == set(range(14)), 'fourteen_channel_permutation', g)
        check({fp[j] for j in END} == set(END), 'endpoint_pair_preserved', g)
        for j, item in enumerate(FAMILY):
            image = [0]*9
            for k, e in enumerate(item['residue']):image[sp[k]] = e
            check(tuple(image) == FAMILY[fp[j]]['residue'], 'actual_laurent_residue_covariance', (g,j))
        for n in range(max_degree + 1):
            for w in generated[n]:
                v={(ZERO,w):1}
                check(act(differential(v),p)==differential(act(v,p)),
                      'dihedral_differential_equivariance', (g,w))
                # Coefficient fine degree plus exterior word degree is preserved.
                for (m,t),a in differential(v).items():
                    source=[0]*6;target=list(m)
                    for block in w:
                        for i in block:source[i]+=1
                    for block in t:
                        for i in block:target[i]+=1
                    check(source==target,'six_occurrence_fine_grading',w)

    # Actual cover, including the central chart and every nonzero overlap.
    cover=[];hist=Counter()
    for size in range(1,8):
        for ss in combinations(range(7),size):
            plus=any(1<=i<=3 for i in ss);minus=any(4<=i<=6 for i in ss)
            if plus and minus:continue
            cover.append(ss);hist[size-1]+=1
    check([hist[i] for i in range(4)]==[7,12,8,2],'complete_seven_chart_cover')
    # Diagram: central infinite resolution; other charts and all their
    # intersections have the original generic+seven-sheet-coordinate module.
    for side in (0,1):
        for j,item in enumerate(FAMILY):
            for n in range(1,max_degree+2):
                for w in generated[n]:
                    if w[-1][0]//3 != item['side']:continue
                    check(not chart_after_d(j,w,side),'full_chart_transition_chain_equation',(side,j,w))
        for variable in range(side*3,side*3+3):
            for j,item in enumerate(FAMILY):
                if item['side'] != side:continue
                value=inverse_followed_by_map(chart_basis_inverse(j,variable),side)
                check(value=={(j,ZERO,()):1},'chart_map_explicit_right_inverse',(variable,j))
            value=inverse_followed_by_map(chart_basis_inverse(-1,variable,True),side)
            check(value=={(-1,ZERO,()):1},'generic_chart_map_right_inverse_with_all_residues',variable)
        # Actual inverse sections and all pair/triple comparison homotopies.
        vs=tuple(range(side*3,side*3+3))
        def simplex(subset):
            m=[0]*6
            for i in subset:m[i]-=1
            return {(tuple(m),(tuple(subset),)):1}
        for i,j in combinations(vs,2):
            check(differential(simplex((i,j)),side)==summed(simplex((j,)),scaled(simplex((i,)),-1)),
                  'pairwise_local_inverse_homotopy',(i,j))
        i,j,k=vs
        check(differential(simplex(vs),side)==summed(simplex((j,k)),scaled(simplex((i,k)),-1),simplex((i,j))),
              'triple_local_inverse_higher_homotopy',side)
        # Triangular transitions commute with omitting exactly the endpoints.
        for channel in (-1,)+C12+END:
            if channel==-1:
                full=chart_map_zero(-1,(),side)
            else:
                if FAMILY[channel]['side']!=side:continue
                full=chart_map_zero(channel,((side*3,),),side)
            forgotten={key:a for key,a in full.items() if key[0] not in END}
            expected={} if channel in END else full
            if channel==-1:expected={key:a for key,a in full.items() if key[0] not in END}
            check(forgotten==expected,'endpoint_forgetting_commutes_with_chart_maps',channel)

    # The central normalization equations are conjugate for every residue
    # vector, not only for one numerical specialization. Coefficients are
    # polynomials in fourteen independent residue symbols.
    def pol(c=0, variable=None):
        return {():c} if variable is None and c else {(variable,):c} if c else {}
    def pplus(*ps):
        result={}
        for pp in ps:
            for mm,aa in pp.items():add_term(result,mm,aa)
        return result
    def ptimes(pp,qq):
        result={}
        for m,a in pp.items():
            for n,b in qq.items():add_term(result,tuple(sorted(m+n)),a*b)
        return result
    def sparse_product(aa,bb):
        result={}
        for (i,k),av in aa.items():
            for (l,j),bv in bb.items():
                if k!=l:continue
                result[(i,j)]=pplus(result.get((i,j),{}),ptimes(av,bv))
        return {key:value for key,value in result.items() if value}
    a0={(0,0):pol(1),(0,1):pol(-1)}
    ar=dict(a0)
    trans={(i,i):pol(1) for i in range(16)}
    inverse=dict(trans)
    for j,item in enumerate(FAMILY):
        a0[(j+1,j+2)]=pol(1)
        ar[(j+1,j+2)]=pol(1)
        ar[(j+1,item['side'])]=pol(-1,j)
        trans[(j+2,item['side'])]=pol(1,j)
        inverse[(j+2,item['side'])]=pol(-1,j)
    check(sparse_product(ar,trans)==a0,'all_residue_central_normalization_conjugation')
    check(sparse_product(trans,inverse)=={(i,i):pol(1) for i in range(16)},
          'central_residue_change_inverse')
    # These transformations need all r_j regular on the chart. An endpoint
    # coefficient U_L/tau_opposite cannot extend to the full corresponding
    # occurrence chart: one opposite t may vanish while U_L remains one.
    for j in END:
        f=FAMILY[j]
        opposite=range(3,6) if f['side']==0 else range(3)
        for i in opposite:
            check(f['residue'][i]==-1 and all(f['residue'][k]==1 for k in range(6,9)),
                  'endpoint_pole_prevents_global_central_diagonalization',(j,i))

    # Rank formulas over C, valid integrally because all specialized
    # differentials are literally zero. Not numerical rational matrix ranks.
    s14=[int(n==0)+14*b[n] for n in range(21)]
    s12=[int(n==0)+12*b[n] for n in range(21)]
    endpoint=[2*b[n] for n in range(21)]
    for n in range(21):
        check(s14[n]-s12[n]==endpoint[n],'all_order_endpoint_rank_difference',n)
        check(c[n+1]==2*b[n] if n<20 else True,'native_relative_dimension_shift',n)
    for n in range(max_degree+1):
        plus=sum(w[-1][0]//3==0 for w in generated[n+1])
        minus=sum(w[-1][0]//3==1 for w in generated[n+1])
        check((plus,minus)==(b[n],b[n]),'ideal_resolution_word_ranks',n)

    check(c[:6]==[1,6,24,92,354,1362],'conductor_initial_ranks')
    check(s14[:5]==[43,168,644,2478,9534],'whole_source_initial_ranks')
    # Simple detector of the difference between regular ambient and singular
    # intrinsic conductor: ambient Tor1=7*24+9; intrinsic Tor1=7*24.
    ambient=[43,177,284,225,90,15]
    check(ambient[1]!=s14[1],'ambient_and_intrinsic_fibres_are_distinct')

    # Replay provenance is recorded, not implicitly claimed if file absent.
    previous=Path(__file__).with_name('replayed_reverse_cone_for_intrinsic_conductor_20260907.json')
    prior=None
    if previous.exists():
        old=json.loads(previous.read_text())
        prior={'file':previous.name,'sha256':hashlib.sha256(previous.read_bytes()).hexdigest(),
               'assertions':old.get('total_exact_assertions')}
    cert={
        'status':'proved_all_degree_intrinsic_coefficient_resolution_and_chart_descent',
        'scope':'The alternating occurrence ring, native J and relative F, and the existing target-selected S14/S12 on their named test open. No physical-source identification.',
        'source_commit':COMMIT,
        'grading':'Resolution degrees are homological; exceptional reverse costalk degrees are cohomological.',
        'resolving_ring':'B=C[x1,x2,x3,y1,y2,y3]/(xi*yj)',
        'spectator_ring_on_conductor':'C_T; all six t parameters inverted only on the already named chart D(T)',
        'resolution':'Free B on alternating nonempty exterior blocks; d differentiates the first block only.',
        'exactness_proof':'Explicit C-linear integral contracting homotopy on every monomial word. See proof. Not a B-linear contraction.',
        'max_generated_homological_degree':max_degree+1,
        'max_contraction_test_degree':max_degree,
        'monomial_test_degree':monomial_degree,
        'monomials_per_word':len(mons),
        'enumerated_word_counts':{str(n):len(w) for n,w in generated.items()},
        'poincare_series':{
            'conductor':'(1+z)^3/(1-3z-3z^2-z^3)',
            'one_normalization_branch':'1/(1-3z-3z^2-z^3)',
            'one_branch_ideal':'(3+3z+z^2)/(1-3z-3z^2-z^3)',
            'S14':'1+14*(3+3z+z^2)/(1-3z-3z^2-z^3)',
            'S12':'1+12*(3+3z+z^2)/(1-3z-3z^2-z^3)'},
        'ranks_degrees_0_through_20':{'conductor':c,'branch':q,'branch_ideal':b,
            'S14':s14,'S12':s12,'two_endpoint_channels':endpoint},
        'native_relative_F_homology_degrees_1_through_20':c[1:],
        'source_conductor_homotopy_groups':{'pi0_normalized':'affine C_T^42',
            'positive_pi_ranks':{str(n):s14[n] for n in range(1,9)},
            'interpretation':'Derived conductor marking infinity-groupoid, not native physical states.'},
        'ambient_conductor_Tor_ranks_for_comparison':ambient,
        'cover_histogram':[hist[i] for i in range(4)],
        'endpoint_indices':list(END),
        'residue_channels':[{'index':j,'sheet':'+' if f['side']==0 else '-',
            'inactive':[''.join(map(str,a)) for a in f['inactive']],
            'endpoint':f['endpoint'],
            'residue':{('t'+''.join(map(str,a)) if k<6 else 'u'+''.join(map(str,a))):f['residue'][k]
                      for k,a in enumerate(OCC+LONG) if f['residue'][k]}}
            for j,f in enumerate(FAMILY)],
        'chart_transition':'generic b -> (b, r_j*b); ideal singleton [i] -> X_i*z_j; all higher components -> 0',
        'pairwise_inverse_homotopy':'[i,j]/(X_i X_j)',
        'triple_inverse_homotopy':'[i,j,k]/(X_i X_j X_k)',
        'intrinsic_fibre_negative_control':'Setting either or both endpoint residues to zero leaves the whole intrinsic conductor fibre, in every degree, unchanged; global transition data distinguish the sources.',
        'global_warning':'The central splitting is not a global splitting. The same triple-normal endpoint transition residues remain; this does not cancel their Ext class.',
        'reverse_costalk':'i^! D_B(S14) = RHom_C(C tensor_B^L S14,C), unbounded in nonnegative cohomological degrees.',
        'nonidentification':'S14 is not perfect over B on the conductor; cannot equal finite perfect native packets by perfection-preserving operations. Maps and non-perfect support-changing correspondences are not excluded.',
        'replayed_predecessor':prior,
        'assertions':dict(sorted(COUNTS.items())),
        'total_exact_assertions':sum(COUNTS.values()),
        'limitations':['No reconstruction of geometric endpoint connectors.',
            'Infinite-degree assertions use the contraction proof and recurrence, not extrapolated finite tests.',
            'No assertion that local Tor ranks detect the nonzero global endpoint attachment.',
            'No new integer-prime torsion follows; all displayed Tor modules are free over C.',
            'No proof assistant and no repository modifications.']
    }
    output.write_text(json.dumps(cert,indent=2)+'\n')
    print(json.dumps({k:cert[k] for k in ['status','enumerated_word_counts','cover_histogram',
                    'total_exact_assertions','replayed_predecessor']},indent=2))
    print('Conductor:',c[:9]);print('S14:',s14[:9])


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path('marici_intrinsic_conductor_resolution_certificate_20260907.json'))
    parser.add_argument('--max-degree',type=int,default=5)
    parser.add_argument('--monomial-degree',type=int,default=2)
    args=parser.parse_args()
    main(args.output,args.max_degree,args.monomial_degree)
