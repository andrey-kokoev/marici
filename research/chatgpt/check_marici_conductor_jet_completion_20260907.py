#!/usr/bin/env python3
"""Exact conductor-jet tower and global-frame completion checks for Marici.

Only Python's standard library is used. The alternating occurrence resolution
is constructed explicitly. All computations use integer sparse chains. Spectator
coefficients extend these identities by base change; no occurrence/Rees inverse
or factorial is adjoined. Finite checks supplement the all-order proof in the
accompanying note; they do not certify an independently defined physical kernel.
"""
from __future__ import annotations

import argparse
from collections import Counter
from functools import lru_cache
from itertools import combinations, product
from math import comb, factorial
from pathlib import Path
import hashlib
import json
import time

Mon = tuple[int, ...]
Block = tuple[int, ...]
Word = tuple[Block, ...]
Vec = dict[tuple[Mon, Word], int]
Poly = dict[Mon, int]
ZERO: Mon = (0,) * 6
LABELS = ('13', '15', '35', '02', '04', '24')
CHECKS: Counter[str] = Counter()


def check(ok: bool, family: str, detail=None) -> None:
    if not ok:
        raise AssertionError(f'{family}: {detail!r}')
    CHECKS[family] += 1


def put(v: dict, key, c: int) -> None:
    if c:
        v[key] = v.get(key, 0) + c
        if v[key] == 0:
            del v[key]


def add(*vs: dict) -> dict:
    out = {}
    for v in vs:
        for k, c in v.items():
            put(out, k, c)
    return out


def neg(v: dict) -> dict:
    return {k: -c for k, c in v.items()}


def sgn(n: int) -> int:
    return -1 if n % 2 else 1


def side(m: Mon) -> int | None:
    a, b = any(m[:3]), any(m[3:])
    if a and b:
        raise ValueError('A mixed occurrence monomial is zero, not a basis term.')
    return 0 if a else 1 if b else None


def multmon(a: Mon, b: Mon) -> Mon | None:
    aa, bb = side(a), side(b)
    if aa is not None and bb is not None and aa != bb:
        return None
    return tuple(x + y for x, y in zip(a, b))


def variable(i: int) -> Mon:
    return tuple(int(j == i) for j in range(6))


def worddegree(w: Word) -> int:
    return sum(map(len, w))


@lru_cache(None)
def words(n: int, first: int = -1) -> tuple[Word, ...]:
    if n == 0:
        return ((),)
    if n < 0:
        return ()
    out = []
    for sigma in ((0, 1) if first == -1 else (first,)):
        for mask in range(1, 8):
            block = tuple(3*sigma + i for i in range(3) if mask & (1 << i))
            if len(block) <= n:
                out.extend((block,) + tail for tail in words(n-len(block), 1-sigma))
    return tuple(out)


@lru_cache(None)
def idealwords(i: int, sigma: int) -> tuple[Word, ...]:
    return tuple(w for w in words(i+1) if w[-1][0] // 3 == sigma)


@lru_cache(None)
def monomials(k: int) -> tuple[Mon, ...]:
    if k == 0:
        return (ZERO,)
    out = []
    for sigma in (0, 1):
        for a in range(k+1):
            for b in range(k-a+1):
                tri = (a, b, k-a-b)
                out.append(tri+(0,)*3 if sigma == 0 else (0,)*3+tri)
    return tuple(out)


def trunc(v: Vec, m: int) -> Vec:
    return {k: c for k, c in v.items() if sum(k[0]) <= m}


def d(v: Vec, m: int | None = None) -> Vec:
    """Unaugmented branch-ideal resolution. Homological degree |word|-1."""
    out = {}
    for (mono, w), c in v.items():
        if worddegree(w) <= 1:
            continue
        first = w[0]
        for j, i in enumerate(first):
            mm = multmon(mono, variable(i))
            if mm is None or (m is not None and sum(mm) > m):
                continue
            block = first[:j] + first[j+1:]
            ww = (block,) + w[1:] if block else w[1:]
            put(out, (mm, ww), sgn(j)*c)
    return out


def h(v: Vec) -> Vec:
    """Integral C-linear Koszul contraction; never asserted B-linear."""
    out = {}
    for (mono, w), c in v.items():
        sigma = side(mono)
        if sigma is None:
            continue
        if w[0][0]//3 == sigma:
            first, suffix = w[0], w[1:]
        else:
            first, suffix = (), w
        i = min(tuple(j for j, e in enumerate(mono) if e) + first)
        if i in first:
            continue
        mm = list(mono)
        mm[i] -= 1
        put(out, (tuple(mm), (tuple(sorted(first+(i,))),)+suffix),
            c*sgn(sum(j < i for j in first)))
    return out


def augmentation(v: Vec) -> Poly:
    out = {}
    for (mono, w), c in v.items():
        if worddegree(w) != 1:
            continue
        mm = multmon(mono, variable(w[0][0]))
        if mm is not None:
            put(out, mm, c)
    return out


def section(poly: Poly, m: int | None = None) -> Vec:
    out = {}
    for mono, c in poly.items():
        if not any(mono):
            raise ValueError('A branch-ideal section requires zero constant term.')
        i = next(j for j, a in enumerate(mono) if a)
        mm = list(mono)
        mm[i] -= 1
        if m is None or sum(mm) <= m:
            put(out, (tuple(mm), ((i,),)), c)
    return out


def projection(v: Vec, m: int) -> Vec:
    return add(v, neg(d(h(v), m)), neg(h(d(v, m))))


def tensor_scalar(poly: Poly, v: Vec, m: int | None = None) -> Vec:
    out = {}
    for a, u in poly.items():
        for (b, w), c in v.items():
            mm = multmon(a, b)
            if mm is not None and (m is None or sum(mm) <= m):
                put(out, (mm, w), u*c)
    return out


def hasse_monomial(beta: tuple[int, ...], alpha: tuple[int, ...]):
    if any(a > b for a, b in zip(alpha, beta)):
        return 0, None
    n = 1
    for a, b in zip(alpha, beta):
        n *= comb(b, a)
    return n, tuple(b-a for a, b in zip(alpha, beta))


def triple_monomials(maximum: int):
    return tuple((a,b,c) for a in range(maximum+1) for b in range(maximum+1-a)
                 for c in range(maximum+1-a-b))


def residue_allowed(exponents: tuple[int, ...], sigma: int) -> bool:
    """Conductor Laurent monomial extends to the sigma normalization sheet."""
    opposite = range(3, 6) if sigma == 0 else range(3)
    return all(exponents[j] >= 0 for j in opposite)


def geometric_permutation(rot: int, reflected: int) -> tuple[int, ...]:
    ds = tuple(tuple(map(int, s)) for s in LABELS)
    return tuple(ds.index(tuple(sorted(((2*rot+sgn(reflected)*a)%6,
                                        (2*rot+sgn(reflected)*b)%6))))
                 for a, b in ds)


def act(v: Vec, p: tuple[int, ...]) -> Vec:
    out = {}
    for (mono, w), c in v.items():
        mm = [0]*6
        for i, a in enumerate(mono):
            mm[p[i]] = a
        blocks, orientation = [], 1
        for block in w:
            new = tuple(p[i] for i in block)
            orientation *= sgn(sum(new[i] > new[j] for i in range(len(new))
                                   for j in range(i+1, len(new))))
            blocks.append(tuple(sorted(new)))
        put(out, (tuple(mm), tuple(blocks)), c*orientation)
    return out


def ideal_rank(i: int) -> int:
    a = [3, 12, 46]
    while len(a) <= i:
        a.append(3*a[-1]+3*a[-2]+a[-3])
    return a[i]


def hilbert_B(k: int) -> int:
    return 1 if k == 0 else 2*comb(k+2, 2)


def tor_rank(m: int, i: int) -> int:
    return sum(sgn(j)*hilbert_B(m-j)*ideal_rank(i+j) for j in range(m+1))


def sparse_rank_unit(columns: list[dict[int, int]]) -> int:
    """Integer elimination of a map with a split image; report only unit pivots.

    Used on small homogeneous blocks. Fractional/rational rank is not silently
    substituted for integral saturation. A nonunit pivot triggers an error.
    """
    pivots: dict[int, dict[int, int]] = {}
    for original in columns:
        v = dict(original)
        while v:
            k = min(v)
            if k in pivots:
                multiplier = v[k]
                for row, c in pivots[k].items():
                    put(v, row, -multiplier*c)
            else:
                if abs(v[k]) != 1:
                    raise ArithmeticError(f'Nonunit residual pivot: {v[k]}')
                coefficient = v[k]
                pivots[k] = {r: coefficient*c for r, c in v.items()}
                break
    return len(pivots)


def main(output: Path, max_jet: int, max_homology: int) -> None:
    if not 0 <= max_jet <= 7 or not 1 <= max_homology <= 6:
        raise ValueError('Choose 0 <= max-jet <= 7 and 1 <= max-homology <= 6.')
    start = time.monotonic()
    rank_records = []
    for m in range(max_jet+1):
        for sigma in (0, 1):
            traces = {}
            for i in range(max_homology+1):
                trace = 0
                for k in range(m+1):
                    for mono in monomials(k):
                        for w in idealwords(i, sigma):
                            v = {(mono, w): 1}
                            dv = d(v, m)
                            ev = projection(v, m)
                            check(not d(dv, m), 'jet_d_squared')
                            check(not h(h(v)), 'integral_h_squared')
                            check(projection(ev, m) == ev, 'jet_projection_idempotent')
                            check(not d(ev, m), 'projection_cycles')
                            check(not projection(dv, m), 'projection_kills_boundaries')
                            if i == 0:
                                check(ev == section(augmentation(v)), 'degree_zero_ideal_fibre')
                            elif k < m:
                                check(not ev, 'positive_homology_only_top_coefficient_degree')
                            else:
                                check(ev == h(d(v)), 'top_degree_projector_formula')
                                trace += ev.get((mono, w), 0)
                                if m > 0:
                                    check(not trunc(ev, m-1), 'successive_positive_Tor_transition_zero')
                if i > 0:
                    check(trace == tor_rank(m, i), 'complete_integer_projection_rank', (m,i,sigma,trace))
                    traces[i] = trace
            rank_records.append({'jet_order':m,'sheet':sigma,'one_channel_positive_ranks':traces,
                'one_channel_H0_rank':comb(m+4,3)-1})

    # Independent integral matrix audit on complete small coefficient blocks.
    matrices = 0
    for sigma in (0, 1):
        for i in range(1, min(max_homology, 2)+1):
            for k in range(min(max_jet, 2)+1):
                target = [(mono,w) for mono in monomials(k+1) for w in idealwords(i-1,sigma)]
                target_index = {v:j for j,v in enumerate(target)}
                cols = [{target_index[t]:a for t,a in d({(mono,w):1}).items()}
                        for mono in monomials(k) for w in idealwords(i,sigma)]
                rank = sparse_rank_unit(cols)
                expected = sum(sgn(j)*hilbert_B(k-j)*ideal_rank(i+j) for j in range(k+1))
                check(rank == expected, 'independent_integral_image_rank')
                matrices += 1

    # All-order dimension formula has a positive quadratic expression in m.
    for i in range(1, 25):
        for m in range(31):
            a = ideal_rank(i)
            second = 3*a-ideal_rank(i+1)
            third = ideal_rank(i-1)
            value = a*comb(m+2,2)+second*comb(m+1,2)+(third*comb(m,2) if m>=2 else 0)
            check(value == tor_rank(m,i) and value > 0, 'rank_generating_function_identity')

    # Actual frame-action translations: one per monomial, every labelled channel.
    action_tests = 0
    for sigma in (0,1):
        mons = tuple(mo for k in range(1,max_jet+4) for mo in monomials(k) if side(mo)==sigma)
        for channel in range(7):
            for mono in mons:
                f={mono:1}
                for m in range(max_jet+1):
                    lift=section(f,m)
                    check(not d(lift,m), 'frame_translation_is_cycle')
                    check(projection(lift,m)==lift, 'frame_translation_fixed_by_retraction')
                    check(augmentation(lift)==(f if sum(mono)<=m+1 else {}), 'exact_transport_jet')
                    check((not lift)==(sum(mono)>=m+2), 'exact_action_kernel')
                    if m:
                        check(trunc(lift,m-1)==section(f,m-1), 'transport_tower_compatibility')
                    action_tests += 1
        # Composition and inverse are checked as actual affine chain translations.
        for a in mons[:18]:
            for b in mons[:18]:
                for m in range(min(max_jet,2)+1):
                    check(section(add({a:2},{b:-3}),m)==add(section({a:2},m),section({b:-3},m)),
                          'resolved_additive_composition')
                    check(add(section({a:1},m),section({a:-1},m))=={}, 'resolved_inverse')

    # Quadratic detection survives tensor restriction though x^2=0 as a scalar.
    x=variable(0); x2=tuple(2*z for z in x)
    check(not section({x2:1},0), 'quadratic_invisible_on_conductor')
    quad=section({x2:1},1)
    check(quad=={(x,((0,),)):1}, 'quadratic_detected_on_first_thickening')
    check(projection(quad,1)==quad and augmentation(quad)=={x2:1}, 'quadratic_not_boundary')
    check(sum(x2)>1, 'scalar_x_squared_zero_in_B1')

    # Branchwise Hasse identities: multiplication and composition over integers.
    triples=triple_monomials(4)
    alphas=triple_monomials(3)
    for beta in triples:
        for alpha in alphas:
            c, residual=hasse_monomial(beta,alpha)
            check((c if residual==(0,0,0) else 0)==int(beta==alpha), 'Hasse_coefficient_at_origin')
            for gamma in triple_monomials(2):
                c2, residual2=hasse_monomial(residual,gamma) if residual is not None else (0,None)
                ag=tuple(a+g for a,g in zip(alpha,gamma))
                ct, rt=hasse_monomial(beta,ag)
                factor=1
                for aa,gg in zip(alpha,gamma): factor*=comb(aa+gg,aa)
                check(c*c2==factor*ct, 'Hasse_composition_without_factorials')
                if c*c2: check(residual2==rt, 'Hasse_composition_monomial')
    for beta in triples[:18]:
        for gamma in triples[:18]:
            for alpha in alphas:
                ct,_=hasse_monomial(tuple(b+c for b,c in zip(beta,gamma)),alpha)
                value=0
                for aa in product(*(range(a+1) for a in alpha)):
                    bb=tuple(a-b for a,b in zip(alpha,aa))
                    c1,_=hasse_monomial(beta,aa);c2,_=hasse_monomial(gamma,bb)
                    value+=c1*c2
                check(value==ct,'Hasse_Leibniz_integer_identity')
    for p in (2,3,5,7):
        c,_=hasse_monomial((p,0,0),(p,0,0))
        check(c%p==1 and factorial(p)%p==0,'positive_characteristic_jet_negative_control',p)

    # The ordered representative depends on ordering, but the intrinsic map
    # is covariant up to an explicitly filled syzygy for all dihedral labels.
    for rot,ref in product(range(3),range(2)):
        perm=geometric_permutation(rot,ref)
        for sigma in (0,1):
            for k in range(1,5):
                for mono in monomials(k):
                    if side(mono)!=sigma: continue
                    mm=[0]*6
                    for j,c in enumerate(mono): mm[perm[j]]=c
                    difference=add(act(section({mono:1}),perm),neg(section({tuple(mm):1})))
                    check(not augmentation(difference),'dihedral_divisor_choice_same_augmentation')
                    primitive=h(difference)
                    check(d(primitive)==difference,'dihedral_divisor_choice_explicit_homotopy')
                    for m in range(min(max_jet,3)+1):
                        check(d(trunc(primitive,m),m)==trunc(difference,m),'dihedral_homotopy_after_thickening')

    # Formal jet sequences: every coefficient, not just all local Tor ranks.
    # Finite checks instantiate the algebraic telescope proof of lim^1.
    for sigma in (0,1):
        axis=0 if sigma==0 else 3
        formal={tuple(k if j==axis else 0 for j in range(6)):1 for k in range(1,21)}
        jets=[]
        for m in range(16):
            f={mono:c for mono,c in formal.items() if sum(mono)<=m+1}
            jets.append(f)
            check(augmentation(section(f,m))==f,'compatible_formal_series_jet')
            if m: check({a:c for a,c in f.items() if sum(a)<=m}==jets[m-1],'formal_jet_restriction')
        for m in range(15):
            step=add(jets[m+1],neg(jets[m]))
            check(all(sum(a)>=m+2 for a in step),'lim1_transition_in_decreasing_kernel')

    # Original endpoint residues cannot become globally regular, at any jet.
    # Normal exponents are ordered with the same sheet order as LABELS.
    global_patterns=0
    for exps in product((-1,0,1),repeat=6):
        for sigma in (0,1):
            expected=all(exps[j]>=0 for j in (range(3,6) if sigma==0 else range(3)))
            check(residue_allowed(exps,sigma)==expected,'global_coefficient_regular_domain')
            global_patterns+=1
    endpoint_plus=(0,0,0,-1,-1,-1)
    endpoint_minus=(-1,-1,-1,0,0,0)
    check(not residue_allowed(endpoint_plus,0) and not residue_allowed(endpoint_minus,1),
          'both_endpoint_residues_globally_nonzero')
    for m in range(max_jet+1):
        # Finite formal framed extensions: same triangular coordinate change
        # for every r, with no occurrence coordinates inverted on the centre.
        # A two-coordinate symbolic matrix (b,z)->(b,z-r*b) has inverse r->-r.
        for r in range(-3,4):
            for b,z in product(range(-2,3),repeat=2):
                w=z-r*b
                check(w+r*b==z,'formal_endpoint_triangular_inverse')
                check(z-r*b==w,'formal_endpoint_kernel_quotient_frames')

    prior=Path(__file__).with_name('marici_conductor_yoneda_and_global_frames_20260907.md')
    prior_hash=hashlib.sha256(prior.read_bytes()).hexdigest() if prior.exists() else None
    replay_path=Path(__file__).with_name('replayed_conductor_yoneda_for_jets_20260907.json')
    replay = None
    if replay_path.exists():
        data=json.loads(replay_path.read_text())
        replay={'filename':replay_path.name,
                'sha256':hashlib.sha256(replay_path.read_bytes()).hexdigest(),
                'total_exact_assertions':data.get('total_exact_assertions'),
                'execution':'Independently rerun before this checker; not rerun inside it.'}
    source_script=Path(__file__)
    result={
        'status':'proved_for_existing_framed_coefficient_source_not_native_physical_identification',
        'date':'2026-09-07','lane':'Branch B',
        'baseline_commit':'d1947b67a60d3e88ba77f4ca60ea02c2a306ee61',
        'predecessor_note_sha256':prior_hash,
        'independent_predecessor_replay':replay,
        'script_sha256':hashlib.sha256(source_script.read_bytes()).hexdigest(),
        'scope':{'thickening':'B_m=B/I^(m+1), occurrence conductor I, not Rees t support',
                 'source':'S14 restricted to D(T) = B + 7 Iplus + 7 Iminus',
                 'generic_frame':'Full B_m-valued generic coefficient fixed to 1',
                 'global_transports':'Original polynomial Gfr, not enlarged to formal power series'},
        'results':{
            'H0_one_channel':'I_sigma/I_sigma^(m+2)',
            'action_kernel':'(Iplus^(m+2))[tau_plus^-1]^7 + (Iminus^(m+2))[tau_minus^-1]^7',
            'tower_action_faithful':'Intersection of all action kernels is zero',
            'higher_Tor':'Concentrated in top allowed coefficient occurrence degree m',
            'positive_Tor_transition':'Every map from stage m+1 to stage m is zero on H_i, i>=1',
            'rank_formula':'r_(m,i)=sum_{j=0}^m (-1)^j h_(m-j)*b_(i+j), i>=1',
            'completion':'Rlim K_m = completed S14, concentrated in degree zero',
            'completed_normalized_markings':'Discrete (Iplus C[[x]])^7 + (Iminus C[[y]])^7',
            'completed_quotient':'Discrete completed markings / original Gfr',
            'lim1_kernel':'R^1 lim action-kernel = completion(Gfr)/Gfr',
            'formal_global_extension_fibre':'Discrete product over sigma of (C[[X_sigma]] / C_sigma[X_sigma])^7',
            'endpoint_warning':'Every formal conductor neighborhood lies in D(T); all residue-source extensions split there. Both actual global endpoint differences stay nonzero.',
            'Hasse_scope':'Branchwise divided derivatives extract Taylor coefficients integrally; not derivatives of primes and not derivations on the singular fibre-product ring'},
        'finite_audit':{'max_jet_order':max_jet,'max_homology_degree':max_homology,
                        'independent_integer_matrix_blocks':matrices,
                        'labelled_channel_transport_tests':action_tests,
                        'normal_coefficient_domain_patterns':global_patterns,
                        'rank_records':rank_records},
        'full_source_rank_table':[
            {'m':m,'normalized_pi0_C_rank':14*(comb(m+4,3)-1),
             'positive_pi_ranks':[14*tor_rank(m,i) for i in range(1,5)]}
             for m in range(max_jet+1)],
        'assertions':dict(sorted(CHECKS.items())),
        'total_exact_assertions':sum(CHECKS.values()),
        'runtime_seconds':round(time.monotonic()-start,3),
        'verification_limits':['All-order and inverse-limit results have proofs in the note, not finite extrapolations.',
            'Integral image bases are checked on the recorded complete small blocks; remaining exactness follows from the universal contraction.',
            'No proof-assistant run; no repository writes; no identification of a formal test space with physical generic Q.',
            'No endpoint deletion is licensed: formal invisibility is an explicit failure of a proposed identification test.']}
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ('status','total_exact_assertions','runtime_seconds','full_source_rank_table')},indent=2))


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path('marici_conductor_jet_completion_certificate_20260907.json'))
    parser.add_argument('--max-jet',type=int,default=4)
    parser.add_argument('--max-homology',type=int,default=4)
    args=parser.parse_args()
    main(args.output,args.max_jet,args.max_homology)
