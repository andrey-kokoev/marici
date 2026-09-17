#!/usr/bin/env python3
"""Exact counterexample: free-ridge peeling need not reverse to a shelling."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
# Facets encoded by channel splits for alpha=(1,2,3,4,5,6), beta=(1,2,3,4,6,5).
def F(*splits):return frozenset(frozenset(q) for q in splits)
A=F((3,4),(5,6),(1,5,6));B=F((2,3),(5,6),(1,5,6));C=F((1,2),(5,6),(1,2,3));D=F((1,2),(3,4),(5,6));E=F((2,3),(5,6),(1,2,3))
order=[A,B,C,D,E]
def admissible(facet,prior):
 intersections=[facet&q for q in prior];ridges=[q for q in intersections if len(q)==len(facet)-1]
 return bool(ridges) and all(any(q<=r for r in ridges) for q in intersections)
# The forward deletion E,D,C,B leaves A. Every deleted facet has a free ridge at deletion time.
def free_at_deletion(deletion):
 remaining=set(order)
 for facet in deletion:
  ridges=[frozenset(q) for q in __import__('itertools').combinations(facet,len(facet)-1)]
  if not any(sum(r<=g for g in remaining)==1 for r in ridges):return False
  remaining.remove(facet)
 return True
delete=[E,D,C,B];admissibility=[True]+[admissible(order[i],order[:i]) for i in range(1,len(order))]
checks={'all_deletions_use_free_ridge':free_at_deletion(delete),'reverse_order_fails_shelling_at_third_facet':admissibility==[True,True,False,True,True]}
out={'schema':'marici.nima.free-ridge-reverse-shelling-counterexample.v1','alpha':[1,2,3,4,5,6],'beta':[1,2,3,4,6,5],'facet_count':5,'reverse_order_admissibility':admissibility,'first_bad_index':2,'checks':checks,'passed':all(checks.values()),'consequence':'The free-ridge lemma is true, but arbitrary free-ridge peeling does not imply reverse shellability. A stronger selection invariant is necessary.'}
p=ROOT/'research/nima/results/free-ridge-reverse-shelling-counterexample.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
