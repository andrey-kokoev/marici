"""Small exhaustive check: fix root 0, test all labeled edge colorings through order 6. Compare root-fiber conditions with direct forbidden-clique tests. Check pullback of the core under single-vertex deletions."""
from itertools import combinations
from ramsey_retention_slice import check,has

def split(a,p):return p&~(a[0]|1),p&a[0]
def fiber(a,p,k):
 c,d=split(a,p);blue=[~v for v in a];
 if not check(a,c,3,k) or has(a,d,2):return False
 js=[j for j in range(len(a)) if d>>j&1];ss=[a[j]&c for j in js]
 if any(has(a,s,2) for s in ss):return False
 q=c
 while True:
  if not has(a,q,2) and sum(not(s&q) for s in ss)+q.bit_count()>k:return False
  if not q:return True
  q=(q-1)&c
if __name__=='__main__':
 count=0
 for n in range(1,7):
  pairs=list(combinations(range(n),2));p=(1<<n)-1
  for mask in range(1<<len(pairs)):
   a=[0]*n
   for v,(i,j) in enumerate(pairs):
    if mask>>v&1:a[i]|=1<<j;a[j]|=1<<i
   for j in range(1,n):
    u=p^(1<<j);assert split(a,u)==tuple(v&u for v in split(a,p))
   for k in (2,3,4,5):assert fiber(a,p,k)==check(a,p,3,k+1);count+=1
 print('rooted threshold cases:',count)
