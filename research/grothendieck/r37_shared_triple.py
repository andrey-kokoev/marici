"""Triple-only baseline, joint feasibility, fixed rarity rank, leave-one-core-out risk."""
from r37_feature_obstructions import *
from math import lcm

def data(a):
 R=sorted(sum(1<<i for i in t) for t in combinations(range(16),5) if all(not a[i]>>j&1 for i,j in combinations(t,2)));T={r:list(combinations([i for i in range(16) if r>>i&1],3)) for r in R};cnt=Counter(t for v in T.values() for t in v);K=[tuple(sorted(cnt[t] for t in T[r])) for r in R];V={r:sum(1<<(3*i) for i in range(16) if r>>i&1) for r in R};target=sum((6-d.bit_count())<<(3*i) for i,d in enumerate(a));M={r:sum(1<<j for j,q in enumerate(R) if not r&q) for r in R};buckets=defaultdict(list)
 for t in combinations(R,3):buckets[sum(V[r] for r in t)].append(t)
 hits=Counter();n=0
 for k,L in buckets.items():
  for x in L:
   for y in buckets.get(target-k,[]):
    if x[-1]>=y[0]:continue
    n+=1;one=two=0
    for r in x+y:two|=one&M[r];one|=M[r]
    while two:b=two&-two;two^=b;hits[K[b.bit_length()-1]]+=1
 risk={k:F(hits[k],n*v) for k,v in Counter(K).items()} if n else {};return R,K,risk

def margin(R,w):return min((6*sum(x for q,x in zip(R,w) if not q&r)-sum(w),r) for r in R)
if __name__=='__main__':
 ds=[data(c['core']) for c in cores];eligible=[];cnt=Counter();first={};ids={k:i for i,k in enumerate(sorted({k for R,K,z in ds for k in K}))};blocks={}
 for i,(R,K,risk) in enumerate(ds):
  ok,_,_=certify(R,K);assert ok is not None
  if not ok:continue
  eligible.append(i);G=defaultdict(list)
  for q,k in zip(R,K):G[k].append(q)
  A=np.zeros((len(R),len(ids)),dtype=int)
  for k,L in G.items():A[:,ids[k]]=[6*sum(not s&q for q in L)-len(L) for s in R]
  blocks[i]=A;scores=[sum(F(1,t) for t in k) for k in K];rank=[F(sum(x<=s for x in scores),len(R)) for s in scores];rules={'rank':rank}
  if risk:
   def avg(k):
    xs=[z[k] for j,(_,_,z) in enumerate(ds) if j!=i and k in z];return sum(xs,F(0))/len(xs) if xs else F(0)
   rules['risk']=[avg(k) for k in K]
  for name,w in rules.items():
   m,r=margin(R,w);cnt[name,m>0]+=1
   if m<=0:first.setdefault(name,(i,r,str(m),sum(v==0 for v in w)))
 def joint(I):
  A=np.vstack([blocks[i] for i in I]);return linprog(np.ones(len(ids)),A_ub=-A,b_ub=-np.ones(len(A)),method='highs')
 print('eligible',eligible,'rules',cnt,'first',first,flush=True);I=eligible.copy();res=joint(I)
 if not res.success:
  for i in eligible:
   J=[j for j in I if j!=i];s=joint(J);assert s.status in (0,2)
   if s.status==2:I=J
  A=np.vstack([blocks[i] for i in I]);dual=linprog(np.zeros(len(A)),A_ub=A.T,b_ub=np.zeros(len(ids)),A_eq=[np.ones(len(A))],b_eq=[1]);assert dual.success
  for den in [10000,10**8]:
   y=[F(float(t)).limit_denominator(den) for t in dual.x];nz=[(j,t) for j,t in enumerate(y) if t];assert nz
   if all(sum(int(A[j,k])*t for j,t in nz)<=0 for k in range(len(ids))):break
  else:raise AssertionError('inexact dual')
  print('verified conflicting cores',I,'dual support',len(nz))
 else:
  A=np.vstack(list(blocks.values()));x=np.rint(res.x*1e7).astype('int64');assert min(x)>=0 and min(A@x)>0;print('verified shared function',len(x),'positive weights',sum(x>0))
