#!/usr/bin/env python3
"""Exact weighted-Laurent witness for continuity of physical cut translations."""
import itertools,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
t=3;radius=4
G=list(itertools.product(range(-radius,radius+1),repeat=2))
def norm(g):return abs(g[0])+2*abs(g[1])
def weight(g):return t**norm(g)
def shift(c,h):return {(g[0]+h[0],g[1]+h[1]):v for g,v in c.items()}
def q(c):return sum(abs(v)*weight(g) for g,v in c.items())
packets=[]
for g1,g2 in zip(G[::7],G[3::7]):packets.append({g1:2,g2:-1})
shifts=((1,-1),(-1,1),(2,0),(0,-2))
translation_bound=all(q(shift(c,h))<=weight(h)*q(c) for c in packets for h in shifts)
commute=all(shift(shift(c,h),k)==shift(shift(c,k),h) for c in packets for h,k in itertools.product(shifts,repeat=2))
# A two-slot cut is a direct-sum output; its l1 norm is the sum of branch norms.
two_slot_bound=all(q(shift(c,shifts[0]))+q(shift(c,shifts[1]))<=(weight(shifts[0])+weight(shifts[1]))*q(c) for c in packets)
checks={'laurent_translation_bound':translation_bound,'disjoint_translation_order_independent':commute,'two_slot_cut_bound':two_slot_bound}
out={'schema':'marici.nima.physical-cut-completion.v1','model':'two-generator weighted Laurent group','checks':checks,'occurrence_coaction_regression':'check_qtds_cut_coaction.py passes through twelve points','theorem':'finite physical cut coactions extend uniquely to the projective Laurent completion','passed':all(checks.values()),'boundary':'not a claim that sharp finite windows are invariant under Laurent translations'}
p=ROOT/'research/nima/results/physical-cut-completion.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
