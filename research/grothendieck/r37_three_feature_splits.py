from r37_feature_obstructions import certify,weights,cores,Counter,combinations
from statistics import median
out=Counter();sizes=[[] for _ in range(4)];remaining=[]
for idx,rec in enumerate(cores):
 a=rec['core'];R=sorted(sum(1<<i for i in t) for t in combinations(range(16),5) if all(not a[i]>>j&1 for i,j in combinations(t,2)));W=weights(set(R));moves={r:{3<<i for i in range(15) if ((r>>i)&3) in (1,2) and (r^(3<<i)) in W[0]} for r in R}
 def profile(k):
    rows={r:[sum(1<<i for i in t) for t in combinations([i for i in range(16) if r>>i&1],k)] for r in R};ct=Counter(t for v in rows.values() for t in v);return {r:tuple(sorted(ct[t] for t in v)) for r,v in rows.items()}
 four,three=profile(4),profile(3);key={r:(W[0][r],four[r],W[2][r]) for r in R};refinements=[[tuple(sorted(key[r^m] for m in moves[r])) for r in R],[three[r] for r in R],[tuple(sorted(len(moves[r^m^h]) for m,h in combinations(moves[r],2) if not m&h and r^m^h in moves)) for r in R]];flags=[]
 for j,K in enumerate([list(key.values()),*[list(zip(key.values(),v)) for v in refinements]]):
    ok,n,_=certify(R,K);flags.append(ok);sizes[j].append(n);out[j,ok]+=1
 if all(v is False for v in flags):remaining.append(idx)
print(out,'median classes',list(map(median,sizes)),'all fail',remaining)
