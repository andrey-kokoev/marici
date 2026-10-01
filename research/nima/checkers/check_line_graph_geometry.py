"""Exact all-source hop distances and ball volumes for paw promotions0..7.

Each edge has unit length by assumption. No cosmological metric/time law is
inferred. Bitset breadth-first search visits every source, not a sample.
"""
from collections import Counter, defaultdict
from itertools import combinations
from fractions import Fraction
from pathlib import Path
import json


def metrics(n, edges):
    adjacency = [0]*n
    for a,b in edges:
        adjacency[a] |= 1 << b
        adjacency[b] |= 1 << a
    shells = Counter()
    eccentricities = []
    full = (1 << n)-1
    for source in range(n):
        seen = frontier = 1 << source
        distance = 0
        while seen != full:
            union = 0
            pending = frontier
            while pending:
                bit = pending & -pending
                union |= adjacency[bit.bit_length()-1]
                pending ^= bit
            frontier = union & ~seen
            assert frontier, 'disconnected graph'
            distance += 1
            shells[distance] += frontier.bit_count()
            seen |= frontier
        eccentricities.append(distance)
    assert sum(shells.values()) == n*(n-1)
    assert shells[1] == 2*len(edges)
    cumulative = n
    balls = {'0': '1'}
    for r in range(1,max(eccentricities)+1):
        cumulative += shells[r]
        balls[str(r)] = str(Fraction(cumulative,n))
    assert cumulative == n*n
    return {
        'vertices':n,'edges':len(edges),
        'mean_degree':str(Fraction(2*len(edges),n)),
        'edge_density':str(Fraction(2*len(edges),n*(n-1))),
        'diameter':max(eccentricities),'radius':min(eccentricities),
        'mean_distance':str(Fraction(sum(r*c for r,c in shells.items()),n*(n-1))),
        'mean_ball_volumes':balls,
        'ordered_distance_histogram':dict(sorted(shells.items())),
        'eccentricity_histogram':dict(sorted(Counter(eccentricities).items())),
    }


# Independent closed examples check BFS normalization and radii.
triangle = metrics(3,set(combinations(range(3),2)))
assert triangle['diameter']==1 and triangle['mean_distance']=='1'
path = metrics(4,{(0,1),(1,2),(2,3)})
assert path['diameter']==3 and path['radius']==2 and path['mean_distance']=='5/3'

edges = {(0,1),(0,2),(1,2),(0,3)}
supports = [1 << i for i in range(4)]
rows = []
for cycle in range(8):
    row = metrics(len(supports),edges)
    row['cycle'] = cycle
    row['ancestral_support_size_histogram'] = dict(sorted(Counter(s.bit_count() for s in supports).items()))
    row['fraction_covering_all_seed_records'] = str(Fraction(sum(s==15 for s in supports),len(supports)))
    rows.append(row)
    print(cycle,row['vertices'],row['edges'],row['diameter'],
          f"{float(Fraction(row['mean_distance'])):.6f}",
          row['mean_ball_volumes'].get('1'),row['mean_ball_volumes'].get('2'),flush=True)
    if cycle == 7: break
    incidence = defaultdict(list)
    next_supports = []
    for index,(a,b) in enumerate(sorted(edges)):
        incidence[a].append(index); incidence[b].append(index)
        next_supports.append(supports[a] | supports[b])
    edges = {tuple(sorted(pair)) for ids in incidence.values() for pair in combinations(ids,2)}
    supports = next_supports

result = {'status':'passed','metric':'unit edge length, undirected shortest-path distance',
          'method':'exact bitset BFS from every vertex at every reported cycle',
          'ball_convention':'closed balls include the centre; volumes averaged over all vertices',
          'cycles':rows,
          'scope':'graph geometry through7 promotions only; physical length, cosmological time, matter and causal dynamics unspecified.'}
out = Path(__file__).resolve().parents[1]/'results/line-graph-geometry.json'
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print('PASS: all-source distance counts and independent BFS controls.')
