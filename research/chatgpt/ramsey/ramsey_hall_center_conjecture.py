"""Falsification test of Hall-center necessity for 6-regular (3,7;22) graphs. Independently validate catalogue records; record input digest and root obstructions."""
from pathlib import Path
from itertools import combinations
from collections import Counter
import hashlib,json

def decode(line):
 assert line[0]==85
 values=[b-63 for b in line[1:]];assert all(0<=b<64 for b in values);A=[0]*22;k=0
 for j in range(1,22):
  for i in range(j):
   if values[k//6]>>(5-k%6)&1:A[i]|=1<<j;A[j]|=1<<i
   k+=1
 return A

def independent(A,mask,k):
 if not k:return True
 while mask.bit_count()>=k:
  bit=mask&-mask;mask^=bit
  if independent(A,mask&~A[bit.bit_length()-1],k-1):return True
 return False

def root_profile(A,v):
 outside=[u for u in range(22) if u!=v and not A[v]>>u&1];pairs=[A[u]&A[v] for u in outside]
 return {'vertex':v,'intersection_sizes':dict(sorted(Counter(s.bit_count() for s in pairs).items())),'distinct_pairs':len(set(pairs)),'hall_center':all(s.bit_count()==2 for s in pairs) and len(set(pairs))==15}

if __name__=='__main__':
 path=Path(__file__).with_name('pauli-realization-catalogues')/'r37_22.g6';raw=path.read_bytes();rows=raw.splitlines();regular=[]
 for index,line in enumerate(rows,1):
  A=decode(line);assert all(not(A[i]&A[j]) for i,j in combinations(range(22),2) if A[i]>>j&1);assert not independent(A,(1<<22)-1,7)
  if all(a.bit_count()==6 for a in A):
   profiles=[root_profile(A,v) for v in range(22)];centers=[p['vertex'] for p in profiles if p['hall_center']];regular.append({'record':index,'centers':centers,'root_profiles':profiles,'graph6':line.decode()})
 report={'input':str(path),'sha256':hashlib.sha256(raw).hexdigest(),'records_validated':len(rows),'regular_records':len(regular),'center_count_histogram':dict(sorted(Counter(len(r['centers']) for r in regular).items())),'counterexamples':[r['record'] for r in regular if not r['centers']],'regular':regular}
 out=Path(__file__).with_suffix('.json');out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:v for k,v in report.items() if k!='regular'},indent=2))
