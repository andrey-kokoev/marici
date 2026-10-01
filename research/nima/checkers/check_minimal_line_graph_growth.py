"""Exhaust small simple undirected seeds for iterated line-graph growth.

Scope: unlabelled simple graphs (enumerated with labels), no loops/parallel edges.
Growth certificate: a connected component has minimum degree >=2 and some
vertex of degree >2. Then E>V, and iterated mean degree obeys d' >= 2d-2 > d,
guaranteeing unbounded growth. Leaves may be removed by promotion before this
certificate applies. Repetition/extinction is checked by exact isomorphism.
"""
from itertools import combinations, permutations
from fractions import Fraction
from pathlib import Path
from collections import Counter
import json


def normalize(edges):
    # Ignore isolated records for eventual-growth classification: they cannot
    # contribute an edge at any later step. The growing trace has no isolates.
    names = sorted({v for e in edges for v in e})
    ids = {v:i for i,v in enumerate(names)}
    return frozenset(tuple(sorted((ids[a],ids[b]))) for a,b in edges)


def line(edges):
    es = sorted(edges)
    return normalize({(i,j) for i,j in combinations(range(len(es)),2)
                      if set(es[i]) & set(es[j])})


def components(edges):
    remaining = {v for e in edges for v in e}
    while remaining:
        group = {min(remaining)}
        while True:
            larger = group | {v for e in edges if group & set(e) for v in e}
            if larger == group: break
            group = larger
        remaining -= group
        yield frozenset(e for e in edges if set(e) <= group)


def certificate(edges):
    for part in components(edges):
        deg = Counter(v for e in part for v in e)
        if min(deg.values()) >= 2 and max(deg.values()) > 2:
            mean = Fraction(2*len(part),len(deg))
            # d'(G) = sum d(v)(d(v)-1) / E >= 2(mean-1)
            next_mean = Fraction(sum(d*(d-1) for d in deg.values()),len(part))
            assert mean > 2 and next_mean >= 2*(mean-1)
            return {'vertices':len(deg),'edges':len(part),
                    'min_degree':min(deg.values()),'max_degree':max(deg.values()),
                    'mean_degree':str(mean),'next_mean_degree':str(next_mean)}
    return None


def canonical(edges):
    edges = normalize(edges)
    n = len({v for e in edges for v in e})
    return min(tuple(sorted(tuple(sorted((p[a],p[b]))) for a,b in edges))
               for p in permutations(range(n)))


def classify(edges):
    edges = normalize(edges)
    seen = set()
    for step in range(12):
        cert = certificate(edges)
        if cert: return 'growing',step,cert
        if not edges: return 'extinct',step,None
        key = canonical(edges)
        if key in seen: return 'repeating',step,None
        seen.add(key)
        edges = line(edges)
    raise AssertionError('Unclassified seed; cannot infer absence of growth from a cutoff')


# All graphs on up to four vertices, including disconnected ones and isolates.
# Three edges need at most six incident vertices; eight labels more than suffice.
# Enumerating all <=3-edge graphs on eight labels covers every smaller-edge seed,
# regardless of additional isolated records (which cannot affect later growth).
small_vertex = []
for n in range(1,5):
    universe = list(combinations(range(n),2))
    counts = Counter()
    growing = []
    for mask in range(1 << len(universe)):
        edges = frozenset(e for i,e in enumerate(universe) if mask & (1 << i))
        kind,step,cert = classify(edges)
        counts[kind] += 1
        if kind == 'growing': growing.append((edges,step,cert))
    small_vertex.append({'vertices':n,'tested':1 << len(universe),'outcomes':dict(counts)})
    if n < 4: assert not growing
    else: four_vertex_growing = growing

by_edges = []
all_pairs = list(combinations(range(8),2))
for m in range(4):
    counts = Counter()
    for chosen in combinations(all_pairs,m):
        kind,_,_ = classify(frozenset(chosen))
        counts[kind] += 1
    assert counts['growing'] == 0
    by_edges.append({'edges':m,'tested':sum(counts.values()),'outcomes':dict(counts)})

minimal = [(es,step,cert) for es,step,cert in four_vertex_growing if len(es)==4]
classes = {canonical(es) for es,_,_ in minimal}
assert len(minimal) == 12 and len(classes) == 1
paw = frozenset({(0,1),(1,2),(0,2),(0,3)})
assert canonical(paw) in classes
kind,step,cert = classify(paw)
assert kind == 'growing' and step == 1
trace = []
edges = paw
for k in range(5):
    degrees = Counter(v for e in edges for v in e)
    trace.append({'promotion':k,'records':len(degrees),'relationships':len(edges),
                  'directed_packets':2*len(edges), 'degrees':sorted(degrees.values())})
    if k < 4: edges = line(edges)
assert [(r['records'],r['relationships']) for r in trace] == [(4,4),(4,5),(5,8),(8,18),(18,64)]

result = {'status':'passed',
    'scope':'simple undirected graphs; reciprocal directed-packet realization',
    'vertex_exhaustion':small_vertex,'edge_exhaustion':by_edges,
    'minimal_growing_seed':{'name':'paw (triangle with one pendant edge)',
                           'edges':sorted(paw),'vertices':4,'relationships':4,
                           'directed_packets':8,'classes_at_minimum_vertex_and_edge_counts':1,
                           'certificate_after_promotions':step,'certificate':cert},
    'trace':trace,
    'proof':'At a connected min-degree>=2 non-cycle, mean degree exceeds2. Line promotion preserves min-degree>=2, connectedness, and mean d_next>=2d-2. Thus mean degree diverges and vertex count is unbounded.',
    'minimality':'No graph with <=3 vertices or <=3 edges grows; all such edge-supported seeds enumerated. A four-vertex four-edge paw has a growth certificate after one promotion.'}
path = Path(__file__).resolve().parents[1]/'results/minimal-line-graph-growth.json'
path.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
