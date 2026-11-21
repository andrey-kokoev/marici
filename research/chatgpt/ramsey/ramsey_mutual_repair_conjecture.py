"""Exhaust mutual repair conjecture for vertex-disjoint triangle-free two-edge switches from both Hall graph types. Search genuinely joint independent sevens."""
from pathlib import Path
from itertools import combinations
from collections import Counter
import json
from ramsey_hall_center_conjecture import decode

def sevens(A,mask=None,k=7,chosen=0):
 if mask is None:mask=(1<<len(A))-1
 if k==0:yield chosen;return
 while mask.bit_count()>=k:
  bit=mask&-mask;mask^=bit
  yield from sevens(A,mask&~A[bit.bit_length()-1],k-1,chosen|bit)

def apply(A,removed,added):
 B=A[:]
 for i,j in (*removed,*added):B[i]^=1<<j;B[j]^=1<<i
 return B

def switches(A):
 E=[e for e in combinations(range(len(A)),2) if A[e[0]]>>e[1]&1]
 for removed in combinations(E,2):
  (a,b),(c,d)=removed
  if len({a,b,c,d})!=4:continue
  for added in [((a,c),(b,d)),((a,d),(b,c))]:
   if any(A[i]>>j&1 for i,j in added):continue
   B=apply(A,removed,added)
   if any(B[i]&B[j] for i,j in added):continue
   bad=list(sevens(B))
   if not bad:continue  # Only individually invalid switches enter repair tests.
   yield {'removed':removed,'added':added,'support':sum(1<<v for v in (a,b,c,d)),'bad':bad}

def repairs(s,t):
 return all(any((mask>>i&1) and (mask>>j&1) for i,j in t['added']) for mask in s['bad'])

if __name__=='__main__':
 data=json.loads(Path(__file__).with_name('ramsey_hall_center_conjecture.json').read_text());results=[]
 for record in data['regular']:
  if record['record'] not in (190,191):continue
  A=decode(record['graph6'].encode());moves=list(switches(A));stats=Counter();examples={};hist=Counter()
  for s,t in combinations(moves,2):
   if s['support']&t['support']:continue
   stats['disjoint_pairs']+=1;mutual=repairs(s,t) and repairs(t,s);bad=list(sevens(apply(apply(A,s['removed'],s['added']),t['removed'],t['added'])));emergent=set(bad)-set(s['bad'])-set(t['bad']);hist[mutual,bool(bad),bool(emergent)]+=1
   if mutual:stats['mutual_repair_pairs']+=1
   if mutual and bad:stats['counterexamples']+=1
   key=str((mutual,bool(bad),bool(emergent)))
   examples.setdefault(key,{'A':s,'B':t,'combined_bad':bad,'emergent':sorted(emergent)})
  result={'source':record['record'],'triangle_free_single_switches':len(moves),'stats':dict(stats),'histogram':{str(k):v for k,v in hist.items()},'examples':examples};results.append(result);print({k:v for k,v in result.items() if k!='examples'})
 Path(__file__).with_suffix('.json').write_text(json.dumps(results,indent=2)+'\n')
