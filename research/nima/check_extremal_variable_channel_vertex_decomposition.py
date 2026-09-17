#!/usr/bin/env python3
"""Test the canonical extremal-variable-channel vertex decomposition through n=8."""
exec(compile(open(__file__.replace('check_extremal_variable_channel_vertex_decomposition.py','check_common_tree_vertex_decomposability.py'),encoding='utf-8').read().split('rows=[]')[0], 'vd-prefix', 'exec'))
import itertools,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];cache={};hist={};reasons={};terminal_failures=[]
def decompose(fs):
 fs=maximal(fs);k=statekey(fs)
 if k in cache:return cache[k]
 sizes={len(f) for f in fs}
 if len(sizes)!=1:cache[k]=False;return False
 if len(fs)<=1:cache[k]=True;return True
 d=next(iter(sizes));V=set().union(*fs);forced=set.intersection(*(set(T) for T in fs));variable=V-forced
 mins=sorted((v for v in variable if (not any(set(w)<set(v) for w in variable if w!=v)) or (not any(set(v)<set(w) for w in variable if w!=v))),key=lambda q:(len(q),tuple(sorted(q))))
 if not mins:cache[k]=False;reasons[k]='no minimal variable channel';return False
 candidates=[]
 for v in mins:
  deletion=maximal(frozenset(f for f in fs if v not in f));link=maximal(frozenset(frozenset(f-{v}) for f in fs if v in f))
  shed=(deletion and {len(f) for f in deletion}=={d} and link and {len(f) for f in link}=={d-1} and all(any(q<=g for g in deletion) for q in link))
  if shed:candidates.append((v,deletion,link))
 if not candidates:
  cache[k]=False;reasons[k]={'extremal_channels':[sorted(v) for v in mins],'reason':'no extremal channel is shedding'}
  terminal_failures.append({'facet_count':len(fs),'facets':[[sorted(q) for q in sorted(T,key=lambda q:(len(q),tuple(sorted(q))))] for T in fs],'extremal_channels':[sorted(v) for v in mins]})
  return False
 v,deletion,link=candidates[0]
 hist[len(v)]=hist.get(len(v),0)+1;ok=decompose(deletion) and decompose(link);cache[k]=ok
 if not ok:reasons[k]={'channel':sorted(v),'reason':'descendant failed'}
 return ok
rows=[];fails=[]
for n in range(4,9):
 A=trees(tuple(range(1,n+1)));total=empty=good=0
 for tail in itertools.permutations(range(2,n+1)):
  beta=(1,)+tail;rev=(1,)+tuple(reversed(tail))
  if beta>rev:continue
  total+=1;F=A&trees(beta)
  if not F:empty+=1
  elif decompose(F):good+=1
  else:fails.append({'n':n,'beta':list(beta),'facets':len(F),'reason':reasons.get(statekey(maximal(F)))})
 rows.append({'n':n,'nonempty':total-empty,'canonical_decompositions':good,'failures':total-empty-good})
out={'schema':'marici.nima.extremal-variable-channel-vertex-decomposition.v1','range':[4,8],'rule':'Discard forced channels; among inclusion-minimal or inclusion-maximal variable channels choose the lexicographically first shedding channel, without recursive backtracking.','results':rows,'recursive_states':len(cache),'selected_size_histogram':hist,'failures':fails[:20],'terminal_failures':terminal_failures[:10],'passed':not fails}
p=ROOT/'research/nima/results/extremal-variable-channel-vertex-decomposition.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':out['passed'],'results':rows,'states':len(cache),'sizes':hist,'first_failure':fails[:1]},indent=2));raise SystemExit(0 if out['passed'] else 1)
