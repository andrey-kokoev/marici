#!/usr/bin/env python3
"""Test a uniform lexicographic channel deletion/link recursion through n=8."""
exec(compile(open(__file__.replace('check_common_tree_lex_vertex_decomposition.py','check_common_tree_vertex_decomposability.py'),encoding='utf-8').read().split('rows=[]')[0], 'vd-prefix', 'exec'))
gcache={};fail_reason={};chosen_size_hist={};chosen_vertices={}
def greedy(fs):
 fs=maximal(fs);k=statekey(fs)
 if k in gcache:return gcache[k]
 sizes={len(f) for f in fs}
 if len(sizes)!=1:gcache[k]=False;return False
 if len(fs)<=1:gcache[k]=True;return True
 d=next(iter(sizes));verts=sorted(set().union(*fs),key=lambda q:(len(q),tuple(sorted(q))))
 # Uniform rule: take the first vertex whose deletion/link have the required purity;
 # unlike vd(), do not backtrack if its descendants later fail.
 candidates=[]
 for v in verts:
  deletion=maximal(frozenset(f for f in fs if v not in f));link=maximal(frozenset(frozenset(f-{v}) for f in fs if v in f))
  if (deletion and {len(f) for f in deletion}=={d} and link and {len(f) for f in link}=={d-1}
      and all(any(q<=g for g in deletion) for q in link)):
   candidates.append((v,deletion,link))
 if not candidates:gcache[k]=False;fail_reason[k]='no pure shedding candidate';return False
 v,deletion,link=candidates[0];chosen_vertices[k]=v;chosen_size_hist[len(v)]=chosen_size_hist.get(len(v),0)+1
 ok=greedy(deletion) and greedy(link);gcache[k]=ok
 if not ok:fail_reason[k]={'chosen':sorted(v),'pure_candidate_count':len(candidates)}
 return ok
import itertools,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];rows=[];fails=[]
for n in range(4,9):
 alpha=tuple(range(1,n+1));A=trees(alpha);total=empty=good=0
 for tail in itertools.permutations(range(2,n+1)):
  beta=(1,)+tail;rev=(1,)+tuple(reversed(tail))
  if beta>rev:continue
  total+=1;F=A&trees(beta)
  if not F:empty+=1
  elif greedy(F):good+=1
  else:fails.append({'n':n,'beta':list(beta),'facets':len(F),'reason':fail_reason.get(statekey(maximal(F)))})
 rows.append({'n':n,'nonempty':total-empty,'lex_recursive_success':good,'failures':total-empty-good})
out={'schema':'marici.nima.common-tree-lex-vertex-decomposition.v1','range':[4,8],'rule':'At each state choose the lexicographically first channel whose deletion and link have the required pure dimensions; never backtrack.','results':rows,'memoized_states':len(gcache),'chosen_channel_size_histogram':chosen_size_hist,'all_choices_are_two_label_ears':set(chosen_size_hist)<={2},'failure_count':len(fails),'first_failures':fails[:20],'passed':not fails}
p=ROOT/'research/nima/results/common-tree-lex-vertex-decomposition.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':out['passed'],'results':rows,'states':len(gcache),'chosen_sizes':chosen_size_hist,'first_failure':fails[:1]},indent=2));raise SystemExit(0 if out['passed'] else 1)
