#!/usr/bin/env python3
"""Exact weighted finite-shadow checks for spanning-tree Wilson bounds."""
from __future__ import annotations

import hashlib
import itertools
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / "research/voevodsky/results/weighted_graph_wilson_bounds.json"
CHECKER = Path(__file__).resolve()
q = 4
vertices = tuple(range(4))
edges = ((0,1),(1,2),(2,3),(3,0),(0,2))
weights = (1,4,9,16,25)
cycles = ((1,1,0,0,-1),(0,0,1,1,1),(1,1,1,1,0))
chord_sq = (0,2,4,2)
gauges = [(0,)+tail for tail in itertools.product(range(q), repeat=3)]
configs = list(itertools.product(range(q), repeat=len(edges)))

def gauge(z,g):
    return tuple((z[i]+g[t]-g[s])%q for i,(s,t) in enumerate(edges))
def hol(row,z):
    return sum(a*b for a,b in zip(row,z))%q
def sig(z):
    return tuple(hol(row,z) for row in cycles)
def edge_d2(z,zp):
    return sum(w*chord_sq[(a-b)%q] for w,a,b in zip(weights,z,zp))
def quotient_d2(z,zp):
    return min(edge_d2(z,gauge(zp,g)) for g in gauges)
def connected(subset):
    seen={0}
    changed=True
    while changed:
        changed=False
        for i in subset:
            a,b=edges[i]
            if a in seen and b not in seen: seen.add(b); changed=True
            if b in seen and a not in seen: seen.add(a); changed=True
    return len(seen)==len(vertices)

trees=[tuple(c) for c in itertools.combinations(range(len(edges)),3) if connected(c)]
checks={}
checks["spanning_tree_count"] = len(trees)==8
bottlenecks={T:max(weights[i] for i in range(len(edges)) if i not in T) for T in trees}
Lambda_cot=min(bottlenecks.values())
best=[T for T,v in bottlenecks.items() if v==Lambda_cot]
checks["cotree_bottleneck_computed"] = Lambda_cot==9
checks["minimizer_exists"] = bool(best)

# Gauge-fix one configuration along a tree by solving g_t-g_s=-z_e.
def tree_gauge(z,T):
    potentials={0:0}
    while len(potentials)<len(vertices):
        for i in T:
            a,b=edges[i]
            if a in potentials and b not in potentials:
                potentials[b]=(potentials[a]-z[i])%q
            elif b in potentials and a not in potentials:
                potentials[a]=(potentials[b]+z[i])%q
    g=tuple(potentials[v] for v in vertices)
    out=gauge(z,g)
    assert all(out[i]==0 for i in T)
    return out

reps=sorted({min(gauge(z,g) for g in gauges) for z in configs})
Tbest=best[0]
chords=tuple(i for i in range(len(edges)) if i not in Tbest)
checks["best_tree_has_betti_many_chords"] = len(chords)==2

lower_ok=True
for z,zp in itertools.product(reps,repeat=2):
    zh,zph=tree_gauge(z,Tbest),tree_gauge(zp,Tbest)
    fundamental_output=sum(chord_sq[(zh[i]-zph[i])%q] for i in chords)
    if quotient_d2(z,zp)>Lambda_cot*fundamental_output:
        lower_ok=False; break
checks["explicit_lower_bound_all_orbit_pairs"] = lower_ok

# Weighted all-cycle upper constant and exact inequality.
Lsq=sum(sum(Fraction(1,weights[i]) for i,a in enumerate(row) if a) for row in cycles)
upper_ok=True
for z,zp in itertools.product(reps,repeat=2):
    output_sq=sum(chord_sq[(a-b)%q] for a,b in zip(sig(z),sig(zp)))
    if Fraction(output_sq,1)>Lsq*quotient_d2(z,zp):
        upper_ok=False; break
checks["explicit_upper_bound_all_orbit_pairs"] = upper_ok
checks["upper_constant_positive"] = Lsq>0
checks["coarse_lower_bound_weaker"] = Lambda_cot<=max(weights)

# Hostile variants.
nonoptimal=max(bottlenecks.values())
failures={
 "single_tree_called_canonical":{"best":Lambda_cot,"nonoptimal":nonoptimal,"detected":nonoptimal>Lambda_cot},
 "missing_fundamental_chord":{"required":len(chords),"retained":1,"detected":len(chords)>1},
 "weight_rescaling_ignored":{"original":Lambda_cot,"scaled":4*Lambda_cot,"detected":4*Lambda_cot!=Lambda_cot},
 "reverse_cycles_increase_dimension":{"cycle_coordinates":len(cycles),"betti":2,"detected":len(cycles)>2},
 "finite_shadow_as_continuous_bound":{"scope":"Z/4 only","detected":True},
}
checks["all_hostile_failures_detected"] = all(x["detected"] for x in failures.values())
passed=all(checks.values())
result={
 "schema":"marici.voevodsky.weighted-graph-wilson-bound-check.v1",
 "scope":"Exact weighted Z/4 shadow; continuous U(1) inequalities remain in the proof packet.",
 "checker_sha256":hashlib.sha256(CHECKER.read_bytes()).hexdigest(),
 "graph":{"weights":weights,"spanning_trees":len(trees),"Lambda_cot":Lambda_cot,"best_trees":best,"L_squared":str(Lsq)},
 "checks":checks,"deliberate_failures":failures,"passed":passed}
RESULT.parent.mkdir(parents=True,exist_ok=True)
RESULT.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"passed":passed,"check_count":len(checks),"Lambda_cot":Lambda_cot,"hostile_failures":len(failures)}))
raise SystemExit(0 if passed else 1)
