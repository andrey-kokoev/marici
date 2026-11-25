"""No refit. Extend each certified pair table to every observed address by monotone step interpolation (left, right, nearest). Verify global unimodality, then independently evaluate all 39 graphs. Triple counts deduplicated across certificates."""
import ast,bisect,gzip,itertools,json,sys
from collections import Counter
from pathlib import Path
import numpy as np
from scipy.sparse import csr_matrix
root=Path(__file__).resolve().parents[2];p=root/'chatgpt/ramsey';sys.path.insert(0,str(p));from ramsey_r37_recursive_proof_verify import graph6,independent_fives
D=root/'voevodsky/results';pairs=json.loads((D/'ramsey_37_unimodal_pairs.json').read_text());assert len(pairs)==741
R=[];starts=[];G=[];addresses={}
for rec,line in enumerate(gzip.open(p/'r36_16.g6.gz','rb'),1):
 A=graph6(line)
 if sum(v.bit_count() for v in A)!=66:continue
 F=independent_fives(A);dd=[[j for j,b in enumerate(F) if not a&b] for a in F];k=[(len(d),sum(len(dd[j]) for j in d)) for d in dd];C=Counter(k);addresses[rec]=set(k);starts.append(len(R));G.append(rec);seen=set()
 for d in dd:
  h=Counter(k[j] for j in d);row=tuple(sorted((v,6*h[v]-n) for v,n in C.items()));
  if row not in seen:R.append(dict(row));seen.add(row)
K=sorted(set.union(*addresses.values()));M=csr_matrix(np.array([[r.get(k,0) for k in K] for r in R],dtype=np.int64));norm=int(np.max(abs(M).sum(axis=1)));triples=set();best=[];transfers=[];hist=Counter()
for v in pairs:
 a,b=v['records'];known=sorted(addresses[a]|addresses[b]);w={ast.literal_eval(k):x for k,x in v['weights'].items()};assert norm*max(w.values())<2**63
 by={d:[s for _,s in g] for d,g in itertools.groupby(known,lambda k:k[0])}
 for mode in ('left','right','nearest'):
  vals=[]
  for d,s in K:
   t=by.get(d);u=0
   if t:
    idx=bisect.bisect_left(t,s);right=t[min(idx,len(t)-1)];left=t[max(0,idx-1)];h=s if s==right else left if mode=='left' or mode=='nearest' and s-left<=right-s else right;u=w.get((d,h),0)
   vals.append(u)
  for _,g in itertools.groupby(zip(K,vals),lambda x:x[0][0]):
   y=[v for k,v in g];j=y.index(max(y));assert y[:j+1]==sorted(y[:j+1]) and y[j:]==sorted(y[j:],reverse=True)
  margins=np.minimum.reduceat(M@np.array(vals,dtype=np.int64),starts);ok=[g for g,m in zip(G,margins) if m>0];assert a in ok and b in ok;hist[len(ok)]+=1;triples.update(itertools.combinations(ok,3));
  if len(ok)>len(best):best=ok
  if len(ok)>2:transfers.append(dict(pair=[a,b],mode=mode,verifiedOn=ok))
out=dict(allTriples=len(list(itertools.combinations(G,3))),certifiedTriples=len(triples),largest=best,groupSizes=hist,transfers=transfers);print({k:v for k,v in out.items() if k!='transfers'});(D/'ramsey_37_unimodal_transfer.json').write_text(json.dumps(out,indent=2)+'\n')
