#!/usr/bin/env python3
"""Test a uniform lexicographic shelling rule for all common-tree complexes through n=9."""
import itertools,json,math
from functools import lru_cache
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def edge(a,b):return tuple(sorted((a,b)))
@lru_cache(None)
def tri(n):
 @lru_cache(None)
 def rec(v):
  if len(v)<=3:return (frozenset(),)
  out=set();a,z=v[0],v[-1]
  for k in range(1,len(v)-1):
   b=v[k];L=rec(v[:k+1]) if k+1>=3 else (frozenset(),);R=rec(v[k:]) if len(v)-k>=3 else (frozenset(),);add=set()
   if k>1:add.add(edge(a,b))
   if k<len(v)-2:add.add(edge(b,z))
   for l in L:
    for r in R:out.add(frozenset(set(l)|set(r)|add))
  return tuple(out)
 return rec(tuple(range(n)))
def canon(S,U):
 S=frozenset(S);C=frozenset(U-S);return min((S,C),key=lambda q:(len(q),tuple(sorted(q))))
def fkey(F):return tuple(sorted((len(q),tuple(sorted(q))) for q in F))
def admissible(F,prior):
 ints=[F&G for G in prior];ridges=[q for q in ints if len(q)==len(F)-1]
 return bool(ridges) and all(any(q<=r for r in ridges) for q in ints)
def interval(S,beta):
 n=len(beta);bits=[x in S for x in beta];return sum(bits[i]!=bits[(i+1)%n] for i in range(n))==2
rows=[];fails=[];total=0
for n in range(4,10):
 alpha=tuple(range(1,n+1));U=set(alpha);A=[frozenset(canon(set(alpha[i:j]),U) for i,j in t) for t in tri(n)]
 empty=nonempty=lex_ok=0
 for tail in itertools.permutations(range(2,n+1)):
  beta=(1,)+tail;rev=(1,)+tuple(reversed(tail))
  if beta>rev:continue
  total+=1;F=sorted((t for t in A if all(interval(s,beta) for s in t)),key=fkey)
  if not F:empty+=1;continue
  nonempty+=1;bad=next((i for i in range(1,len(F)) if not admissible(F[i],F[:i])),None)
  if bad is None:lex_ok+=1
  else:fails.append({'n':n,'beta':list(beta),'facets':len(F),'first_bad_index':bad})
 rows.append({'n':n,'empty':empty,'nonempty':nonempty,'lexicographically_shellable':lex_ok,'failures':nonempty-lex_ok})
checks={'all_orbits_through_nine':total==sum(math.factorial(n-1)//2 for n in range(4,10)),'uniform_lexicographic_rule_succeeds':not fails}
out={'schema':'marici.nima.double-partial-lexicographic-shelling.v1','channel_order':'canonical split key (smaller side cardinality, then sorted labels); facets sorted lexicographically by their sorted channel keys','range':[4,9],'results':rows,'failure_count':len(fails),'first_failures':fails[:20],'checks':checks,'passed':all(checks.values())}
p=ROOT/'research/nima/results/double-partial-lexicographic-shelling.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':out['passed'],'results':rows,'failure_count':len(fails),'first_failure':fails[:1]},indent=2));raise SystemExit(0 if out['passed'] else 1)
