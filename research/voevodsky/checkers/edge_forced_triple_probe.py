"""Minimum worst-case column probes to name one particular BBB interval. Allow deductions from the exact count, and stop if an interval is shared by every completion."""
from functools import lru_cache
from itertools import combinations

def solve(k):
 n=k+3; words=[sum(1<<j for j in s) for s in combinations(range(n),3)]
 full=(1<<len(words))-1; cols=[sum(1<<h for h,w in enumerate(words) if w>>j&1) for j in range(n)]
 covers=[full&~(cols[j]|cols[j+1]|cols[j+2]) for j in range(n-2)]
 @lru_cache(None)
 def win(pool,budget):
  if any(pool&~c==0 for c in covers):return True
  if not budget:return False
  for c in cols:
   r=pool&c;b=pool^r
   if r and b and win(b,budget-1) and win(r,budget-1):return True
  return False
 d=next(t for t in range(n+1) if win(full,t));starts=[j+1 for j,c in enumerate(cols) if win(c,d-1) and win(full^c,d-1)]
 seq=[i for pair in zip(range(n),reversed(range(n))) for i in pair][:n];hist={}
 for i in range(len(words)):
  pool=full
  for t,j in enumerate(seq,1):
   pool &= cols[j] if cols[j]>>i&1 else full^cols[j]
   if any(pool&~c==0 for c in covers):hist[t]=hist.get(t,0)+1;break
 print(k,len(words),d,starts,sorted(hist.items()))
for k in (9,10):solve(k)
