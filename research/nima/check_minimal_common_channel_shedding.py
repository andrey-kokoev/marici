#!/usr/bin/env python3
"""Test whether inclusion-minimal common channels supply shedding vertices."""
exec(compile(open(__file__.replace('check_minimal_common_channel_shedding.py','check_common_tree_vertex_decomposability.py'),encoding='utf-8').read().split('rows=[]')[0], 'vd-prefix', 'exec'))
import itertools,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def shedding(F,v):
 avoiding=[T for T in F if v not in T]
 if not avoiding:return False
 return all(any((T-{v})<=G for G in avoiding) for T in F if v in T)
def split_refines(a,b,U):
 # Channels use the canonical smaller side; test strict interval containment.
 return set(a)<set(b)
rows=[];fails=[];lexfails=[]
for n in range(4,9):
 U=set(range(1,n+1));alpha=tuple(range(1,n+1));A=trees(alpha);total=empty=has=lexok=0
 for tail in itertools.permutations(range(2,n+1)):
  beta=(1,)+tail;rev=(1,)+tuple(reversed(tail))
  if beta>rev:continue
  total+=1;F=A&trees(beta)
  if not F:empty+=1;continue
  V=set().union(*F)
  if len(F)==1:has+=1;lexok+=1;continue
  forced=set.intersection(*(set(T) for T in F));variable=V-forced
  mins=sorted((v for v in variable if not any(split_refines(w,v,U) for w in variable if w!=v)),key=lambda q:(len(q),tuple(sorted(q))))
  good=[v for v in mins if shedding(F,v)]
  if good:has+=1
  else:fails.append({'n':n,'beta':list(beta),'facets':len(F),'minimal_channels':[sorted(v) for v in mins]})
  if mins and shedding(F,mins[0]):lexok+=1
  else:lexfails.append({'n':n,'beta':list(beta),'facets':len(F),'lex_minimal':sorted(mins[0]) if mins else None})
 rows.append({'n':n,'nonempty':total-empty,'some_minimal_channel_shedding':has,'lex_first_minimal_shedding':lexok,'existence_failures':total-empty-has,'lex_failures':total-empty-lexok})
checks={'every_nonsimplex_has_minimal_shedding_channel':not fails}
out={'schema':'marici.nima.minimal-common-channel-shedding.v1','range':[4,8],'minimality':'First discard channels forced in every facet. A variable channel is minimal when its canonical smaller side contains no canonical smaller side of another variable channel.','results':rows,'existence_failure_count':len(fails),'first_existence_failures':fails[:20],'lex_failure_count':len(lexfails),'first_lex_failures':lexfails[:20],'checks':checks,'passed':all(checks.values())}
p=ROOT/'research/nima/results/minimal-common-channel-shedding.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':out['passed'],'results':rows,'first_failure':fails[:1],'first_lex_failure':lexfails[:1]},indent=2));raise SystemExit(0 if out['passed'] else 1)
