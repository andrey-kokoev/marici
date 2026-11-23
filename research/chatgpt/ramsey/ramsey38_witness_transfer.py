"""Exhaustive catalogue screen of frozen source roles. Stage counts and reproducible example per eligible novel address size profile. No fitted target labels."""
from pathlib import Path
import gzip,json,collections,itertools
D=Path(__file__).parent;src=D/'pauli-realization-catalogues/r38_27.g6.gz';cnt=collections.Counter();profiles=collections.Counter();examples={};parents=set();passed=[]
for rec,line in enumerate(gzip.open(src,'rb'),1):
 s=line.strip();assert s[0]==90;h=[0]*27;b=0
 for j in range(1,27):
  for i in range(j):
   if ((s[1+b//6]-63)>>(5-b%6))&1:h[i]|=1<<j;h[j]|=1<<i
   b+=1
 cnt['parents']+=1
 for t,N in enumerate(h):
  cnt['roots']+=1
  if N.bit_count()!=7:continue
  cnt['degree7']+=1;A=[N&v for i,v in enumerate(h) if i!=t and not (N>>i&1)];qs=[v for v in A if v.bit_count()==4];
  if len(qs)!=1:continue
  cnt['one_Q']+=1;q=qs[0];n=[1<<i for i in range(27) if N>>i&1];ps={v for v in A if v.bit_count()==2};zs=[z for z in n if all(z|v in ps for v in n if v!=z)]
  if len(zs)!=1:continue
  cnt['one_z']+=1;z=zs[0];B=N&~(z|q)
  if z&q or B in ps:continue
  cnt['eligible']+=1;parents.add(rec);missing=[a|b for a,b in itertools.combinations(n,2) if a|b not in ps];old=len(ps)==18 and len(missing)==3 and sum(missing)==(N^z) and all(not x&y for x,y in itertools.combinations(missing,2));k=('original' if old else 'novel')+':'+','.join(map(str,sorted(a.bit_count() for a in A)));profiles[k]+=1;examples.setdefault(k,[rec,t]);passed.append((rec,t,old))
o=dict(counts=cnt,eligible_parents=len(parents),profiles=profiles,first_examples=examples,novel_eligible=sum(not old for _,_,old in passed));print(o);(D/'ramsey38_witness_transfer.json').write_text(json.dumps(o,indent=2)+'\n')
