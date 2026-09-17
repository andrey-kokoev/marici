#!/usr/bin/env python3
"""Test whether common-tree restrictions inherit the standard type-A subword word."""
import itertools,json
from functools import lru_cache
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def compose(p,i):
 p=list(p);p[i-1],p[i]=p[i],p[i-1];return tuple(p)
def inv(p):return sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
def product(word,r):
 p=tuple(range(r+1))
 for s in word:p=compose(p,s)
 return p
def cluster_word(m,c=None):
 r=m-3;c=tuple(range(1,r+1)) if c is None else tuple(c);p=tuple(range(r+1));sorting=[]
 while inv(p)<r*(r+1)//2:
  for s in c:
   q=compose(p,s)
   if inv(q)>inv(p):p=q;sorting.append(s)
 return c+tuple(sorting)
def position_diagonals(m,c=None):
 r=m-3;c=tuple(range(1,r+1)) if c is None else tuple(c);q=cluster_word(m,c);pos={s:i for i,s in enumerate(c)};seen={};out=[]
 for s in q:
  seen[s]=seen.get(s,0)+1;rot=seen[s]-1
  asc=sum(pos[j]<pos[j+1] for j in range(1,s));desc=sum(pos[j]>pos[j+1] for j in range(1,s))
  a=(asc+rot)%m;b=(-2-desc+rot)%m;out.append(frozenset((a,b)))
 return out
def crosses(d,e,order):
 a,b=d;c,x=e
 if len(d&e):return False
 pos={v:i for i,v in enumerate(order)}
 a,b=sorted((pos[a],pos[b]));c,x=sorted((pos[c],pos[x]))
 return (a<c<b<x) or (c<a<x<b)
def planar(d,order):return not any(crosses(d,e,order) for e in []) # diagonal itself is always planar
def beta_allowed(d,beta):
 # A channel diagonal is beta-planar iff the alpha interval on either side is beta-contiguous.
 m=len(beta);a,b=sorted(d);S=set(range(a+1,b+1));bits=[x in S for x in beta]
 return sum(bits[i]!=bits[(i+1)%m] for i in range(m))==2
def facets_on(positions,diags,r):
 return {frozenset(c) for c in itertools.combinations(positions,r) if all(not crosses(diags[i],diags[j],tuple(range(r+3))) for i,j in itertools.combinations(c,2))}
def represented_for_c(m,beta,c):
 r=m-3;q=cluster_word(m,c);ds=position_diagonals(m,c);allowed=tuple(i for i,d in enumerate(ds) if beta_allowed(d,beta));F=facets_on(allowed,ds,r)
 if not F:return True,None,0
 L=len(allowed)-r;targets={product(tuple(q[i] for i in allowed if i not in f),r) for f in F}
 if len(targets)!=1:return False,None,len(F)
 w=next(iter(targets))
 if inv(w)!=L:return False,None,len(F)
 allF=set()
 for comp in itertools.combinations(allowed,L):
  if product(tuple(q[i] for i in comp),r)==w:allF.add(frozenset(set(allowed)-set(comp)))
 return allF==F,w,len(F)
def represented(m,beta):
 first_nf=0
 for c in itertools.permutations(range(1,m-2)):
  good,w,nf=represented_for_c(m,beta,c);first_nf=nf
  if good:return True,(list(c),w),nf
 return False,None,first_nf
rows=[];fails=[]
for m in range(4,8):
 ok=empty=total=0
 for tail in itertools.permutations(range(1,m)):
  beta=(0,)+tail;rev=(0,)+tuple(reversed(tail))
  if beta>rev:continue
  total+=1;good,w,nf=represented(m,beta)
  if nf==0:empty+=1
  if good:ok+=1
  else:fails.append({'n':m,'beta':list(beta),'facets':nf})
 rows.append({'n':m,'orbits':total,'empty':empty,'represented_by_some_coxeter_cluster_word':ok,'failures':total-ok})
checks={'nontrivial':sum(x['orbits'] for x in rows)>0}
out={'schema':'marici.nima.common-tree-standard-subword-representation-test.v1','range':[4,7],'results':rows,'failure_count':len(fails),'first_failures':fails[:20],'checks':checks,'passed':not fails,'interpretation':'Retain beta-planar positions in c w0(c), testing every Coxeter-element ordering c, and ask whether all common facets are complements of reduced expressions of one target.'}
p=ROOT/'research/nima/results/common-tree-standard-subword-representation-test.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':out['passed'],'results':rows,'first_failure':fails[:1]},indent=2))
