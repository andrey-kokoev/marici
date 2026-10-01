"""Continue the paw seed through18 promotions: exact prefix, certified bounds.

Materialize only through promotion7. Weighted degree-profile counting obtains
later exact totals without storing their graphs. Beyond the exact prefix use
mean-degree and maximum-degree inequalities, never guessed point estimates.
"""
from collections import Counter, defaultdict
from itertools import combinations
from fractions import Fraction
from math import ceil, floor
from pathlib import Path
import json


def degree_hist(edges):
    return Counter(Counter(v for edge in edges for v in edge).values())


def totals(hist):
    n = sum(hist.values())
    twice_e = sum(d*c for d,c in hist.items())
    assert twice_e % 2 == 0
    return n, twice_e//2


def promote(edges):
    incident = defaultdict(list)
    for i,(a,b) in enumerate(sorted(edges)):
        incident[a].append(i); incident[b].append(i)
    return {tuple(sorted(pair)) for ids in incident.values() for pair in combinations(ids,2)}


def pair_hist(profile):
    # For two incident edges of degrees p,q in the preceding line graph,
    # their new shared-endpoint edge becomes a vertex of degree p+q-2.
    result = Counter()
    items = sorted(profile.items())
    for i,(p,c) in enumerate(items):
        if c >= 2: result[2*p-2] += c*(c-1)//2
        for q,d in items[i+1:]: result[p+q-2] += c*d
    return result


def aggregate_pairs(profiles):
    result = Counter()
    for entries, multiplicity in profiles.items():
        for degree, count in pair_hist(dict(entries)).items():
            result[degree] += count*multiplicity
    return result


edges = {(0,1),(0,2),(1,2),(0,3)}
histories = {}
for k in range(8):
    histories[k] = degree_hist(edges)
    if k < 7: edges = promote(edges)
# Stored graph G7; its edges are G8 vertices.
old_edges = sorted(edges)
degree7 = Counter(v for edge in old_edges for v in edge)
degree8 = [degree7[a]+degree7[b]-2 for a,b in old_edges]
histories[8] = Counter(degree8)
# A G7 endpoint gathers incident G8 vertices by their degrees.
incident_degree8 = defaultdict(Counter)
for (a,b),d in zip(old_edges,degree8):
    incident_degree8[a][d] += 1; incident_degree8[b][d] += 1
profiles7 = Counter(tuple(sorted(p.items())) for p in incident_degree8.values())
histories[9] = aggregate_pairs(profiles7)
# Around G8 vertex e=(a,b), neighbors are other edges at a or b.
# Thus its G9 incident edge degrees are computable from those two profiles.
profiles8 = Counter()
for (a,b),d in zip(old_edges,degree8):
    neighbor_degrees = incident_degree8[a] + incident_degree8[b]
    neighbor_degrees[d] -= 2
    profile = Counter({d+q-2: count for q,count in neighbor_degrees.items() if count})
    assert sum(profile.values()) == d
    profiles8[tuple(sorted(profile.items()))] += 1
histories[10] = aggregate_pairs(profiles8)

rows = []
for k,hist in sorted(histories.items()):
    n,e = totals(hist)
    rows.append({'cycle':k,'records_min':n,'records_max':n,
                 'relationships_min':e,'relationships_max':e,'status':'exact',
                 'min_degree':min(hist),'max_degree':max(hist)})
    if k:
        prev = histories[k-1]
        assert n == totals(prev)[1]
        assert e == sum(c*d*(d-1)//2 for d,c in prev.items())
# G11 vertices and edges follow from the complete G10 degree histogram.
h = histories[10]
n11 = totals(h)[1]
e11 = sum(c*d*(d-1)//2 for d,c in h.items())
rows.append({'cycle':11,'records_min':n11,'records_max':n11,
             'relationships_min':e11,'relationships_max':e11,'status':'exact'})

# Connected simple graphs here have no isolates. At each later iteration:
# V_next=E; mean_degree_next >=2*mean_degree-2;
# maximum_degree_next <=2*maximum_degree-2.
mean_lower = Fraction(2*e11,n11)
max_upper = 2*max(h)-2
lo_n = hi_n = n11
lo_e = hi_e = e11
for k in range(12,19):
    lo_n,hi_n = lo_e,hi_e
    mean_lower = 2*mean_lower-2
    max_upper = 2*max_upper-2
    lo_e = ceil(Fraction(lo_n)*mean_lower/2)
    hi_e = floor(Fraction(hi_n)*max_upper/2)
    assert 0 < lo_n <= hi_n and 0 < lo_e <= hi_e
    rows.append({'cycle':k,'records_min':lo_n,'records_max':hi_n,
                 'relationships_min':lo_e,'relationships_max':hi_e,
                 'status':'certified bounds','mean_degree_lower':str(mean_lower),
                 'max_degree_upper':max_upper})

result = {'status':'passed','seed':'paw: AB,AC,BC,AD (8 reciprocal directed packets)',
          'rule':'retained line-graph promotion by shared endpoints',
          'materialized_through_cycle':7,'degree_histograms_exact_through_cycle':10,
          'totals_exact_through_cycle':11,'cycles':rows,
          'bound_justification':'V_next=E; mean_degree_next>=2*mean_degree-2 by Cauchy-Schwarz; max_degree_next<=2*max_degree-2.',
          'scope':'18 promotion indices; exact finite prefix followed by rigorous count intervals, not18 fully instantiated graphs.'}
path = Path(__file__).resolve().parents[1]/'results/line-graph-eighteen-cycles.json'
path.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
for r in rows:
    def cell(a,b): return str(a) if a==b else f'[{a}, {b}]'
    print(r['cycle'],cell(r['records_min'],r['records_max']),cell(r['relationships_min'],r['relationships_max']),r['status'],sep=' | ')
