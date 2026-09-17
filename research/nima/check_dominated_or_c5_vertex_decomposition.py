#!/usr/bin/env python3
"""Test a graph-theoretic decomposition: dominated shedding vertices plus C5 atoms."""
exec(compile(open(__file__.replace('check_dominated_or_c5_vertex_decomposition.py','check_common_tree_vertex_decomposability.py'),encoding='utf-8').read().split('rows=[]')[0], 'vd-prefix', 'exec'))
import itertools,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];cache={};stats={'dominated':0,'type_a_atom':0};terminal=[]
def graph(fs):
 V=set().union(*fs);co={frozenset((a,b)) for F in fs for a,b in itertools.combinations(F,2)}
 N={v:{w for w in V-{v} if frozenset((v,w)) not in co} for v in V}
 return V,N
def is_type_a_atom(fs,V):
 r=len(next(iter(fs)));catalan=__import__('math').comb(2*(r+1),r+1)//(r+2)
 return len(V)==r*(r+3)//2 and len(fs)==catalan
def shedding_data(fs,v):
 d=len(next(iter(fs)));deletion=maximal(frozenset(f for f in fs if v not in f));link=maximal(frozenset(frozenset(f-{v}) for f in fs if v in f))
 ok=(deletion and {len(f) for f in deletion}=={d} and link and {len(f) for f in link}=={d-1} and all(any(q<=g for g in deletion) for q in link))
 return ok,deletion,link
def dec(fs):
 fs=maximal(fs);k=statekey(fs)
 if k in cache:return cache[k]
 if len(fs)<=1:cache[k]=True;return True
 V,N=graph(fs);ordered=sorted(V,key=lambda q:(len(q),tuple(sorted(q))));cands=[]
 for v in ordered:
  witness=next((u for u in N[v] if N[u]|{u} <= N[v]|{v}),None)
  atom=is_type_a_atom(fs,V)
  if witness is None and not atom:continue
  ok,d,l=shedding_data(fs,v)
  if ok:cands.append((v,d,l,'type_a_atom' if atom and witness is None else 'dominated'))
 if not cands:
  terminal.append({'facets':len(fs),'vertices':len(V),'degrees':sorted(len(N[v]) for v in V)});cache[k]=False;return False
 v,d,l,kind=cands[0];stats[kind]+=1;ok=dec(d) and dec(l);cache[k]=ok;return ok
rows=[];fails=[]
for n in range(4,9):
 A=trees(tuple(range(1,n+1)));total=empty=good=0
 for tail in itertools.permutations(range(2,n+1)):
  beta=(1,)+tail;rev=(1,)+tuple(reversed(tail))
  if beta>rev:continue
  total+=1;F=A&trees(beta)
  if not F:empty+=1
  elif dec(F):good+=1
  else:fails.append({'n':n,'beta':list(beta),'facets':len(F)})
 rows.append({'n':n,'nonempty':total-empty,'decomposed':good,'failures':total-empty-good})
out={'schema':'marici.nima.dominated-or-type-a-atom-vertex-decomposition.v1','range':[4,8],'results':rows,'selection_counts':stats,'states':len(cache),'failures':fails[:20],'terminal_obstructions':terminal[:20],'passed':not fails}
p=ROOT/'research/nima/results/dominated-or-c5-vertex-decomposition.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':out['passed'],'results':rows,'stats':stats,'first_terminal':terminal[:1]},indent=2));raise SystemExit(0 if out['passed'] else 1)
