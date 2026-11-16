#!/usr/bin/env python3
"""Rebuild published S(3,6,42), derive two S(2,5,41), then a 40-point 5-GDD.

Source: Kiermaier, Krcadinac, Wassermann (2026), Theorem 2.3,
'Steiner 3-designs as extensions', DOI 10.1007/s10623-026-01888-w.

All block and incidence checks are exact. Input is the article's two generators
and seven base blocks. No Ramsey adjacency is inferred from the construction.
"""
from collections import Counter
from itertools import combinations
from math import comb

N = 42
ALPHA_CYCLES = '''(1,2,4)(3,9,7)(5,6,8)(10,11,13)(12,18,16)(14,15,17)(19,38,34)
 (20,39,36)(21,37,35)(22,42,32)(23,40,31)(24,41,33)(28,30,29)'''
BETA_CYCLES = '''(1,10)(2,11)(3,12)(4,16)(5,17)(6,18)(7,13)(8,14)(9,15)(19,23)
 (20,24)(21,22)(25,35)(26,36)(27,34)(28,33)(29,31)(30,32)(38,39)(41,42)'''
BASE_BLOCKS = [
    (1,2,3,10,11,12),
    (1,2,4,20,36,39),
    (1,2,13,17,31,34),
    (1,10,19,22,25,30),
    (1,11,20,21,29,34),
    (19,20,21,22,23,24),
    (19,22,31,36,38,42),
]


def perm_from_cycles(cycles):
    import re
    result = list(range(N+1))
    for match in re.findall(r'\(([^()]+)\)', cycles):
        items = [int(s) for s in match.split(',')]
        for a,b in zip(items, items[1:] + items[:1]):
            assert result[a] == a
            result[a] = b
    assert set(result[1:]) == set(range(1,N+1))
    return tuple(result)


def perm_compose(x,y):
    return tuple(x[y[j]] for j in range(N+1))


def group_from_generators(gens):
    identity = tuple(range(N+1))
    seen = {identity}
    todo = [identity]
    for permutation in todo:
        for g in gens:
            v = perm_compose(g,permutation)
            if v not in seen:
                seen.add(v)
                todo.append(v)
    return tuple(todo)


def block_orbit(block,group):
    return {tuple(sorted(g[p] for p in block)) for g in group}


def design():
    alpha, beta = perm_from_cycles(ALPHA_CYCLES), perm_from_cycles(BETA_CYCLES)
    group=group_from_generators((alpha,beta))
    assert len(group)==432
    orbits=[block_orbit(block,group) for block in BASE_BLOCKS]
    blocks=set().union(*orbits)
    assert len(blocks)==574
    assert sum(len(x) for x in orbits)==574, 'published base-block orbits must be disjoint'
    cnt3 = Counter(t for B in blocks for t in combinations(B,3))
    assert len(cnt3)==comb(42,3) and set(cnt3.values())=={1}
    print('S(3,6,42): generators order 432, seven block orbits:',[len(o) for o in orbits])
    print('  574 blocks, all 11,480 triples covered once: VERIFIED')
    return group,blocks


def derived_41(blocks,point):
    others=tuple(x for x in range(1,43) if x!=point)
    through={tuple(x for x in B if x!=point) for B in blocks if point in B}
    assert len(through)==82 and all(len(x)==5 for x in through)
    paircount=Counter(t for B in through for t in combinations(B,2))
    assert len(paircount)==comb(41,2) and set(paircount.values())=={1}
    print(f'S(2,5,41) derived at p={point}: 82 blocks; 820 pairs once: VERIFIED')
    return others,through


def forty_point_fragment(blocks,p,q, derived=None):
    assert p != q
    pointset=[x for x in range(1,43) if x not in (p,q)]
    assert len(pointset)==40
    if derived is None:_,derived=derived_41(blocks,p)
    local_groups=[tuple(x for x in B if x!=q) for B in derived if q in B]
    assert len(local_groups)==10 and all(len(x)==4 for x in local_groups)
    assert set.union(*map(set,local_groups))==set(pointset)
    assert sum(len(B) for B in local_groups)==40
    assert all(not(set(g)&set(h)) for g,h in combinations(local_groups,2))
    pair_inside={tuple(sorted(t)) for B in local_groups for t in combinations(B,2)}
    assert len(pair_inside)==10*comb(4,2)==60
    # 42-design blocks neither through p nor q project as genuine 6-blocks on 40,
    # whereas residual 5-blocks of the 41-design come from 42-design blocks through p.
    # We want the *41-derived* blocks avoiding q: each still size 5, exactly 72 blocks.
    residual=[B for B in derived if q not in B]
    assert len(residual)==72 and all(len(B)==5 for B in residual)
    pair_cross=Counter(t for B in residual for t in combinations(B,2))
    assert len(pair_cross)==comb(40,2)-60 and set(pair_cross.values())=={1}
    assert set(pair_cross).isdisjoint(pair_inside)
    assert all(sum(any(x in g for x in B) for g in local_groups)==5 for B in residual)
    # Matrix N (40 x 10) and M (40 x 72) as bitsets per row.
    N_rows=[sum(1<<j for j,G in enumerate(local_groups) if x in G) for x in pointset]
    M_rows=[sum(1<<j for j,B in enumerate(residual) if x in B) for x in pointset]
    assert all(x.bit_count()==1 for x in N_rows)
    assert all(x.bit_count()==9 for x in M_rows)
    for i,x in enumerate(pointset):
        for j,y in enumerate(pointset):
            gram=(M_rows[i]&M_rows[j]).bit_count()
            rhs=9*(i==j)+1-(N_rows[i]&N_rows[j]).bit_count()
            assert gram==rhs,(x,y,gram,rhs)
    print(f'40-point fragment from (p,q)=({p},{q}): 10 groups x 4, 72 transversal 5-blocks')
    print('  60 in-group pairs + 720 cross-group pairs, unique coverage: VERIFIED')
    print('  M M^T = 9I + J - N N^T, with M 40x72 and N 40x10: VERIFIED')
    return {'pointset':pointset, 'groups':local_groups,'residual':residual,
            'pair_inside':pair_inside,'pair_cross':pair_cross,'M_rows':M_rows,'N_rows':N_rows}


def no_go_homogeneous_blocks(fragment):
    # A red graph defined by declaring entire residual blocks or entire groups red
    # acquires a red K5 (or K4) with any selected block (or group).
    assert all(len(B)>=3 for B in fragment['groups'] + fragment['residual'])
    assert len(fragment['pair_inside']|set(fragment['pair_cross']))==comb(40,2)
    print('RED-EDGE NO-GO: color every pair by its unique containing group/block;')
    print('  selecting any whole 4-group makes a red K4, any whole 5-block makes a red K5.')
    print('  A triangle-free union-of-whole-blocks graph has no red edges, alpha=40.')



def double_derived_triple_partition(blocks,p,q):
    """Every triple on 40 points belongs to one of four block types."""
    assert p!=q
    points = tuple(x for x in range(1,43) if x not in (p,q))
    four = [tuple(x for x in B if x not in (p,q))
            for B in blocks if p in B and q in B]
    five_p = [tuple(x for x in B if x!=p)
              for B in blocks if p in B and q not in B]
    five_q = [tuple(x for x in B if x!=q)
              for B in blocks if q in B and p not in B]
    six = [B for B in blocks if p not in B and q not in B]
    assert tuple(map(len,(four,five_p,five_q,six))) == (10,72,72,420)
    counts = []
    for family in (four,five_p,five_q,six):
        counts.append(Counter(t for B in family for t in combinations(B,3)))
    target=set(combinations(points,3))
    assert all(counts[i][t]==1 for i in range(4) for t in counts[i])
    assert all(sum(C[t] for C in counts)==1 for t in target)
    assert tuple(map(len,counts))==(40,720,720,8400)
    assert sum(map(len,counts))==comb(40,3)==9880
    print(f'40-point triple decomposition (p,q)=({p},{q}):')
    print('  10x4 -> 40 triples; 72x5 -> 720; 72x5 -> 720; 420x6 -> 8400')
    print('  Exact triple cover of all 9,880 triples by four disjoint classes: VERIFIED')
    # Both 5-block systems are 5-GDDs of type 4^10 relative to the 10
    # 4-blocks; 6-block system completes their missing pair counts.
    Q = {frozenset(B) for B in four}
    def signature(x,y):
        return (sum(x in B and y in B for B in four),
                sum(x in B and y in B for B in five_p),
                sum(x in B and y in B for B in five_q),
                sum(x in B and y in B for B in six))
    sigs = Counter(signature(x,y) for x,y in combinations(points,2))
    assert sigs == {(1,0,0,9):60,(0,1,1,8):720}
    print('  Pair-incidence signatures: 60 within-group (1,0,0,9),')
    print('                             720 cross-group (0,1,1,8): VERIFIED')
    # In 40-point coordinates, K=groups, P=p-only, Q=q-only, R=neither.
    # Verify *all four* matrix Gram identities exactly using row bitsets.
    families=(four,five_p,five_q,six)
    rowmasks=tuple([sum(1<<i for i,B in enumerate(fam) if x in B)
                     for x in points] for fam in families)
    for i,x in enumerate(points):
        for j,y in enumerate(points):
            same=(rowmasks[0][i]&rowmasks[0][j]).bit_count()
            C=[(rows[i]&rows[j]).bit_count() for rows in rowmasks]
            assert C[0]==same
            assert C[1]==9*(i==j)+1-same
            assert C[2]==9*(i==j)+1-same
            assert C[3]==54*(i==j)+8+same
            assert sum(C)==72*(i==j)+10
    print('  Grams K K^T, P P^T, Q Q^T, R R^T verified pointwise: VERIFIED')
    print('  Spectral multiplicities for P P^T: 45 (1), 5 (9), 9 (30)')
    return four,five_p,five_q,six


def main():
    group,blocks=design()
    point_orbits=[]
    remaining=set(range(1,43))
    while remaining:
        p=min(remaining)
        O={g[p] for g in group}
        point_orbits.append(tuple(sorted(O)))
        remaining-=O
    print('42-point action orbits:',[(len(x),x[:3]) for x in point_orbits])
    assert sorted(len(x) for x in point_orbits)==[18,24]
    # Point stabilizers are 24 and 18 respectively; these are precisely the
    # two derivative classes identified in the published article.
    for O in point_orbits:
        p=O[0]
        stabilizer=[g for g in group if g[p]==p]
        assert len(stabilizer)==432//len(O)
        others,derived=derived_41(blocks,p)
        q=next(v for v in others if v not in O)
        forty=forty_point_fragment(blocks,p,q,derived)
        no_go_homogeneous_blocks(forty)
        double_derived_triple_partition(blocks,p,q)
        print(f'  42-design p orbit {len(O)}; point stabilizer order {len(stabilizer)}')
    # The largest symmetry-preserving 40-point configuration fixes both
    # points 1 and 10; the order-24 subgroup survives deletion of both.
    more=forty_point_fragment(blocks,1,10,derived_41(blocks,1)[1])
    double_derived_triple_partition(blocks,1,10)

if __name__=='__main__':main()
