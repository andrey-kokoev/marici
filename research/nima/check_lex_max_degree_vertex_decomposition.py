#!/usr/bin/env python3
"""Test maximum-overlap-degree shedding recursion through n=8."""
exec(compile(open(__file__.replace('check_lex_max_degree_vertex_decomposition.py','check_common_tree_vertex_decomposability.py'),encoding='utf-8').read().split('rows=[]')[0], 'vd-prefix', 'exec'))
import itertools,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];cache={};terminal=[]
def graph(fs):
 V=set().union(*fs);co={frozenset((a,b)) for F in fs for a,b in itertools.combinations(F,2)}
 return V,{v:{w for w in V-{v} if frozenset((v,w)) not in co} for v in V}
def data(fs,v):
 d=len(next(iter(fs)));de=maximal(frozenset(f for f in fs if v not in f));li=maximal(frozenset(frozenset(f-{v}) for f in fs if v in f))
 return (de and {len(f) for f in de}=={d} and li and {len(f) for f in li}=={d-1} and all(any(q<=g for g in de) for q in li)),de,li
def dec(fs):
 fs=maximal(fs);k=statekey(fs)
 if k in cache:return cache[k]
 if len(fs)<=1:cache[k]=True;return True
 V,N=graph(fs);mx=max(map(lambda v:len(N[v]),V));vs=sorted((v for v in V if len(N[v])==mx),key=lambda q:(len(q),tuple(sorted(q))));v=vs[0];ok,de,li=data(fs,v)
 if not ok:terminal.append({'facets':len(fs),'vertices':len(V),'max_degree':mx,'chosen':[sorted(x) for x in v],'degree_sequence':sorted(len(N[x]) for x in V)});cache[k]=False;return False;cache[k]=dec(de) and dec(li);return cache[k]
rows=[];fails=[]
for n in range(4,9):
 A=trees(tuple(range(1,n+1)));total=empty=good=0
 for tail in itertools.permutations(range(2,n+1)):
  b=(1,)+tail;r=(1,)+tuple(reversed(tail))
  if b>r:continue
  total+=1;F=A&trees(b)
  if not F:empty+=1
  elif dec(F):good+=1
  else:fails.append({'n':n,'beta':list(b),'facets':len(F)})
 rows.append({'n':n,'nonempty':total-empty,'decomposed':good,'failures':total-empty-good})
out={'schema':'marici.nima.lex-max-degree-vertex-decomposition.v1','range':[4,8],'results':rows,'states':len(cache),'terminal_obstructions':terminal[:20],'failures':fails[:20],'passed':not fails}
p=ROOT/'research/nima/results/lex-max-degree-vertex-decomposition.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':out['passed'],'results':rows,'states':len(cache),'first_terminal':terminal[:1]},indent=2));raise SystemExit(0 if out['passed'] else 1)
