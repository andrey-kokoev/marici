#!/usr/bin/env python3
"""Exact insertion/deletion transport and S6 decomposition of prime-packet kernels.

uv run --with python-flint python research/voevodsky/checkers/check_prime_packet_coherent_growth.py
"""
import itertools
import json
import math
import sys
from collections import defaultdict
from functools import lru_cache
from pathlib import Path
from flint import fmpz_mat

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT/'research/voevodsky'))
from prime_packet_signature_transport import insertion_pullback, deletion_pullback


def permutations(n):
    return list(itertools.permutations(range(n)))


def edge_word(w):
    mask = 0
    out = []
    for j in w:
        out.append((mask, j))
        mask |= 1 << j
    return out


def feature_supports(words, order):
    rows = defaultdict(list)
    for i, w in enumerate(words):
        edges = edge_word(w)
        for k in range(1, order+1):
            for slots in itertools.combinations(range(len(w)), k):
                rows[tuple(edges[j] for j in slots)].append(i)
    rows[()] = list(range(len(words)))
    return dict(rows)


def gram(words, order):
    rows = feature_supports(words, order)
    rows.pop(())  # mass is already in the span of first-order observations
    n = len(words)
    entries = [[0]*n for _ in range(n)]
    for support in rows.values():
        for i in support:
            for j in support:
                entries[i][j] += 1
    return fmpz_mat(entries)


def primitive_nullspace(G):
    X, nullity = G.nullspace()
    cols = []
    for j in range(nullity):
        col = [int(X[i, j]) for i in range(G.nrows())]
        divisor = math.gcd(*col)
        cols.append([x//divisor for x in col])
    return fmpz_mat(G.nrows(), nullity, [cols[j][i] for i in range(G.nrows()) for j in range(nullity)])


def insert(w, label, slot):
    return w[:slot]+(label,)+w[slot:]


def paired_kernel(words):
    n = len(words[0])
    blocks = sorted({tuple(tuple(sorted(w[j:j+2])) for j in range(0, n, 2)) for w in words})
    lookup = {b: j for j, b in enumerate(blocks)}
    matrix = [[0]*len(blocks) for _ in words]
    for i, w in enumerate(words):
        b = tuple(tuple(sorted(w[j:j+2])) for j in range(0, n, 2))
        sign = (-1)**sum(w[j] > w[j+1] for j in range(0, n, 2))
        matrix[i][lookup[b]] = sign
    return fmpz_mat(matrix), blocks


def zero(A):
    return all(A[i,j] == 0 for i in range(A.nrows()) for j in range(A.ncols()))


words = {d: permutations(d) for d in (4,5,6)}
indices = {d: {w: i for i,w in enumerate(ww)} for d,ww in words.items()}
G = {(4,1): gram(words[4],1), (5,1): gram(words[5],1),
     (5,2): gram(words[5],2), (6,1): gram(words[6],1), (6,2): gram(words[6],2)}
K4, _ = paired_kernel(words[4])
K5 = primitive_nullspace(G[5,1])
K6, blocks6 = paired_kernel(words[6])
kernels = {(4,1): K4, (5,1): K5, (5,2): fmpz_mat(120,0), (6,2): K6}
ranks = {key: int(A.rank()) for key,A in G.items()}
transport_rows = []
for d,k in ((4,1),(5,1),(5,2)):
    K = kernels[d,k]
    slot_checks = []
    for slot in range(d+1):
        image = [indices[d+1][insert(w,d,slot)] for w in words[d]]
        pulled_gram = fmpz_mat([[G[d+1,k][image[i],image[j]] for j in range(len(image))]
                              for i in range(len(image))])
        slot_checks.append({
            'slot': slot,
            'kernel_preserved': zero(pulled_gram*K),
            'observable_rank_preserved_exactly': pulled_gram.rank() == ranks[d,k],
            'deletion_is_left_inverse': all(tuple(x for x in insert(w,d,slot) if x != d) == w
                                            for w in words[d]),
        })
    old_null = math.factorial(d)-ranks[d,k]
    new_null = math.factorial(d+1)-ranks[d+1,k]
    transport_rows.append({'from': d, 'to': d+1, 'order': k,
        'old_kernel_dimension': old_null, 'new_kernel_dimension': new_null,
        'inherited_kernel_dimension_all_slots': (d+1)*old_null,
        'new_cross_slot_kernel_dimension': new_null-(d+1)*old_null,
        'old_observable_dimension': ranks[d,k], 'new_observable_dimension': ranks[d+1,k],
        'slots': slot_checks})

# Certify every compiled coordinate update on the complete five-to-six source.
old_features = feature_supports(words[5],2)
new_features = feature_supports(words[6],2)

def combine_rows(coefficients, features):
    out = defaultdict(int)
    for feature, coefficient in coefficients.items():
        for j in features.get(feature, []):
            out[j] += coefficient
    return {j:c for j,c in out.items() if c}

compiled_insertions = True
compiled_order = True
for slot in range(6):
    reverse = {indices[6][insert(w,5,slot)]:i for i,w in enumerate(words[5])}
    for feature,support in new_features.items():
        pull = insertion_pullback(feature,5,slot)
        actual = combine_rows(pull,old_features)
        expected = {reverse[j]:1 for j in support if j in reverse}
        compiled_insertions &= actual == expected
        compiled_order &= all(len(f)<=len(feature) for f in pull)
compiled_deletions = True
for feature,support in old_features.items():
    pull = deletion_pullback(feature,5)
    actual = combine_rows(pull,new_features)
    expected = {indices[6][insert(words[5][j],5,slot)]:1 for j in support for slot in range(6)}
    compiled_deletions &= actual == expected
    compiled_order &= all(len(f)<=len(feature) for f in pull)

# Label deletion annihilates every six-prime second-order kernel vector.
deletions = []
for label in range(6):
    keep = [j for j in range(6) if j != label]
    relabel = {j:i for i,j in enumerate(keep)}
    target_index = indices[5]
    D = fmpz_mat(120,720)
    for i,w in enumerate(words[6]):
        reduced = tuple(relabel[x] for x in w if x != label)
        D[target_index[reduced],i] = 1
    deletions.append(zero(D*K6))

# Two successive insertions commute after adjusting slots.
coherence = True
coherence_count = 0
for w in words[4]:
    for s in range(5):
        for t in range(6):
            left = insert(insert(w,4,s),5,t)
            if t <= s:
                right = insert(insert(w,5,t),4,s+1)
            else:
                right = insert(insert(w,5,t-1),4,s)
            coherence &= left == right
            coherence_count += 1


@lru_cache(None)
def partitions(n, cap=None):
    if n == 0:
        return ((),)
    if cap is None:
        cap=n
    return tuple((a,)+tail for a in range(min(cap,n),0,-1) for tail in partitions(n-a,a))


@lru_cache(None)
def character(lam, cycle_type):
    if not cycle_type:
        return int(not lam)
    length = cycle_type[0]
    answer = 0
    cells = {(i,j) for i,row in enumerate(lam) for j in range(row)}
    for mu in partitions(sum(lam)-length):
        if len(mu)>len(lam) or any(mu[i]>lam[i] for i in range(len(mu))):
            continue
        remaining = {(i,j) for i,row in enumerate(mu) for j in range(row)}
        skew = cells-remaining
        if len(skew) != length:
            continue
        seen = {next(iter(skew))}
        frontier = list(seen)
        while frontier:
            i,j = frontier.pop()
            for p in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
                if p in skew and p not in seen:
                    seen.add(p)
                    frontier.append(p)
        if seen != skew:
            continue
        if any({(i,j),(i+1,j),(i,j+1),(i+1,j+1)} <= skew for i,j in skew):
            continue
        height = len({i for i,j in skew})-1
        answer += (-1)**height*character(mu,cycle_type[1:])
    return answer


def class_size(cycle_type):
    counts = defaultdict(int)
    for a in cycle_type:
        counts[a]+=1
    divisor = math.prod(a**m*math.factorial(m) for a,m in counts.items())
    return math.factorial(sum(cycle_type))//divisor


def representative(cycle_type):
    g = list(range(sum(cycle_type)))
    start = 0
    for length in cycle_type:
        for i in range(length):
            g[start+i]=start+(i+1)%length
        start += length
    return tuple(g)


def kernel_character(K, ww, g):
    index = {w:i for i,w in enumerate(ww)}
    PK = fmpz_mat(K.nrows(), K.ncols())
    for i,w in enumerate(ww):
        j = index[tuple(g[x] for x in w)]
        for k in range(K.ncols()):
            PK[j,k]=K[i,k]
    coords = (K.transpose()*K).solve(K.transpose()*PK)
    # Check that label permutation genuinely preserves the kernel realization.
    assert K*coords == PK
    value = sum(coords[i,i] for i in range(coords.nrows()))
    assert value.denominator == 1
    return int(value)


def decompose(n, values):
    out=[]
    for lam in partitions(n):
        numerator=sum(class_size(c)*values[c]*character(lam,c) for c in partitions(n))
        assert numerator % math.factorial(n) == 0
        mult=numerator//math.factorial(n)
        assert mult>=0
        if mult:
            out.append({'partition':list(lam),'multiplicity':mult,
                        'irreducible_dimension':character(lam,(1,)*n)})
    return out


classes6=partitions(6)
chars6={c:kernel_character(K6,words[6],representative(c)) for c in classes6}
chars5old={c:kernel_character(K5,words[5],representative(c)) for c in partitions(5)}
restricted={c:chars6[tuple(sorted(c+(1,),reverse=True))] for c in partitions(5)}
decomp6=decompose(6,chars6)
decomp5=decompose(5,restricted)
old5=decompose(5,chars5old)

# Independent induced-character formula for ordered pair blocks.
def induced_pair_character(cycle_type):
    if any(a>2 for a in cycle_type):
        return 0
    t=cycle_type.count(2)
    m=3
    return (-1)**t*math.factorial(m)//math.factorial(m-t)*math.factorial(2*m-2*t)//2**(m-t)

orthogonality=all(sum(class_size(c)*character(lam,c)*character(mu,c) for c in classes6)
                  == (math.factorial(6) if lam==mu else 0)
                  for lam in partitions(6) for mu in partitions(6))
branch_counts=defaultdict(int)
for row in decomp6:
    lam=tuple(row['partition'])
    for j in range(len(lam)):
        if j+1<len(lam) and lam[j]==lam[j+1]:
            continue
        mu=list(lam)
        mu[j]-=1
        mu=tuple(x for x in mu if x)
        branch_counts[mu]+=row['multiplicity']
branching_ok=branch_counts=={tuple(r['partition']):r['multiplicity'] for r in decomp5}

# Construct the seven central isotypic projectors in the orthogonal parity basis.
def cycle_type_of(g):
    seen=set()
    lengths=[]
    for i in range(len(g)):
        if i in seen:
            continue
        length=0
        j=i
        while j not in seen:
            seen.add(j)
            length+=1
            j=g[j]
        lengths.append(length)
    return tuple(sorted(lengths,reverse=True))

block_index={b:i for i,b in enumerate(blocks6)}
projector_numerators={tuple(r['partition']):fmpz_mat(90,90) for r in decomp6}
for g in words[6]:
    c=cycle_type_of(g)
    action=[]
    for b in blocks6:
        oriented=[(g[a],g[z]) for a,z in b]
        sign=(-1)**sum(a>z for a,z in oriented)
        target=tuple(tuple(sorted(pair)) for pair in oriented)
        action.append((block_index[target],sign))
    for r in decomp6:
        lam=tuple(r['partition'])
        coefficient=r['irreducible_dimension']*character(lam,c)
        if not coefficient:
            continue
        P=projector_numerators[lam]
        for j,(i,sign) in enumerate(action):
            P[i,j]+=coefficient*sign
identity90=fmpz_mat([[int(i==j) for j in range(90)] for i in range(90)])
projector_checks={
    'all_projectors_idempotent':all(P*P==720*P for P in projector_numerators.values()),
    'all_projectors_self_adjoint':all(P.transpose()==P for P in projector_numerators.values()),
    'projectors_pairwise_orthogonal':all(zero(P*Q) for (lam,P),(mu,Q) in itertools.combinations(projector_numerators.items(),2)),
    'projectors_sum_to_identity':sum(projector_numerators.values(),fmpz_mat(90,90))==720*identity90,
    'projector_ranks_match_multiplicities':all(projector_numerators[tuple(r['partition'])].rank()
        ==r['multiplicity']*r['irreducible_dimension'] for r in decomp6),
}

# Independent first-order character formula from edge/vertex incidence.
def first_order_observable_character(c):
    return c.count(1)*2**(len(c)-1)-2**len(c)+2

def first_order_kernel_character(c):
    return (math.factorial(sum(c)) if all(x==1 for x in c) else 0)-first_order_observable_character(c)

birth_irreducibles=[]
for d in (4,5):
    values={c:(d+1)*first_order_observable_character(c)
              -first_order_observable_character(tuple(sorted(c+(1,),reverse=True)))
            for c in partitions(d)}
    birth_irreducibles.append({'from':d,'to':d+1,'order':1,
                              'dimension':values[(1,)*d],'irreducibles_under_old_label_group':decompose(d,values)})

checks={
    'compiled_insertion_pullbacks_all_coordinates': compiled_insertions,
    'compiled_deletion_pullbacks_all_coordinates': compiled_deletions,
    'compiled_updates_never_increase_signature_order': compiled_order,
    'first_order_character_formula_matches_explicit_kernel': all(chars5old[c] == first_order_kernel_character(c) for c in partitions(5)),
    'all_slot_insertions_preserve_and_reflect_invisibility': all(all(r['kernel_preserved'] and
        r['observable_rank_preserved_exactly'] and r['deletion_is_left_inverse'] for r in t['slots'])
        for t in transport_rows),
    'six_prime_kernel_dimension_90': K6.ncols()==90 and zero(G[6,2]*K6),
    'every_label_deletion_annihilates_six_prime_hidden_modes': all(deletions),
    'all_720_double_insertion_comparisons': coherence and coherence_count==720,
    'S6_character_table_orthogonality': orthogonality,
    'kernel_character_matches_induced_pair_sign': all(chars6[c]==induced_pair_character(c) for c in classes6),
    'S6_decomposition_dimension_90': sum(r['multiplicity']*r['irreducible_dimension'] for r in decomp6)==90,
    'S5_restriction_dimension_90': sum(r['multiplicity']*r['irreducible_dimension'] for r in decomp5)==90,
    'restriction_matches_young_branching': branching_ok,
    'all_seven_isotypic_projectors_certified':all(projector_checks.values()),
}
out={
    'schema':'marici.voevodsky.prime-packet-coherent-growth.v1',
    'arithmetic':'exact FLINT integer/rational matrices; Murnaghan-Nakayama character recurrence',
    'transport':transport_rows,
    'compiled_coordinate_transport': {'old_feature_count_including_mass':len(old_features),
                                     'new_feature_count_including_mass':len(new_features),
                                     'insertion_slots':6,'all_old_routes':120,'all_new_routes':720},
    'new_first_order_kernel_irreducibles':birth_irreducibles,
    'kernel_S6_character':[{'cycle_type':list(c),'class_size':class_size(c),'character':chars6[c]} for c in classes6],
    'kernel_S6_irreducibles':decomp6,
    'isotypic_projector_checks':projector_checks,
    'kernel_S5_restriction':decomp5,
    'five_prime_first_order_kernel_irreducibles':old5,
    'checks':{k:bool(v) for k,v in checks.items()},'passed':all(checks.values()),
    'scope':'Fixed-position insertion, label deletion, and label-permutation actions on full-route coefficient spaces. Restricting symmetry to S5 retains six-step routes; deleting a label maps to five-step routes.',
}
p=ROOT/'research/voevodsky/results/prime-packet-coherent-growth.json'
p.parent.mkdir(parents=True,exist_ok=True)
p.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
raise SystemExit(0 if out['passed'] else 1)
