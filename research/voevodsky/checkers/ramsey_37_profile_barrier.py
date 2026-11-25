"""Dual countercertificates to any nonnegative rule constant on test classes. For a multiset of attachments of size q, each class must miss on average at most q/6 of them. This forbids strict 1/6 for any weights on these classes. Search equal mixtures of one or two attachments; no hit is inconclusive."""
import sys,gzip,json,itertools,collections
from pathlib import Path
root=Path(__file__).resolve().parents[2];p=root/'chatgpt/ramsey';sys.path.insert(0,str(p));from ramsey_r37_recursive_proof_verify import graph6,independent_fives
out=[]
for num,line in enumerate(gzip.open(p/'r36_16.g6.gz','rb'),1):
 A=graph6(line)
 if sum(x.bit_count() for x in A)!=66:continue
 F=independent_fives(A);ds=[[j for j,b in enumerate(F) if not a&b] for a in F];row={}
 for kind,keys in [('missCount',list(map(len,ds))),('degreeSum',[sum(A[i].bit_count() for i in range(16) if t>>i&1) for t in F]),('degreeSequence',[tuple(sorted(A[i].bit_count() for i in range(16) if t>>i&1)) for t in F])]:
  size=collections.Counter(keys);profiles=[collections.Counter(keys[j] for j in d) for d in ds];hit=None
  for q in (1,2):
   for ts in itertools.combinations(range(len(F)),q):
    if all(6*sum(profiles[i][k] for i in ts)<=q*v for k,v in size.items()):hit=dict(sets=[F[i] for i in ts],classes=[(k,v,sum(profiles[i][k] for i in ts)) for k,v in sorted(size.items())]);break
   if hit:break
  row[kind]=hit
 out.append(dict(record=num,**row))
for k in row:print(k,sum(x[k] is not None for x in out),next((x for x in out if x[k]),{}).get(k));(root/'voevodsky/results/ramsey_37_profile_barrier.json').write_text(json.dumps(out,indent=2)+'\n')
