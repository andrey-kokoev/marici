"""Read triples online. For equality of two marked occurrences, store their path-local site-position stamps; no complete trace, seen-arrow table or per-arrow counters required. Test oracle: independently joined archived trace. Not a first-ever-visit classifier."""
import json,itertools
from pathlib import Path
D=Path(__file__).resolve().parents[1];paths=json.loads((D/'results/pne_selected_path_balance.json').read_text())['rows'];stats=dict(paths=len(paths),window_leg_pairs=0,identical_directed_occurrence=0,same_directed_arrow_different_occurrence=0);demo={}
for row in paths:
 prev=None;base=0;reads=[] # reads collected by audit only, not by the online reader
 for w in row['windows']:
  if prev is not None:
   k=max(i for i in [1,2,3] if prev[-i:]==w[:i]);base+=3-k
  reads.append([(tuple(w[j:j+2]),(base+j,base+j+1)) for j in (0,1)]);prev=w
 # Independent offsets from archived join lengths and word, not reader state
 starts=[0];
 for k in row['overlap']:starts.append(starts[-1]+3-k)
 marked=[(e,t,(starts[i]+j,starts[i]+j+1)) for i,r in enumerate(reads) for j,(e,t) in enumerate(r)];assert all(tuple(row['word'][n] for n in ref)==e and t==ref for e,t,ref in marked)
 for (a,u,r),(b,v,s) in itertools.combinations(marked,2):
  stats['window_leg_pairs']+=1;assert (u==v)==(r==s);stats['identical_directed_occurrence']+=u==v;stats['same_directed_arrow_different_occurrence']+=a==b and u!=v
 if row['seq']==['PN','NE']:
  p,n,e=reads
  for name,((a,i),(b,j)) in zip(['PN1','N1N2','N2N1','N2E'],[(p[1],n[0]),(n[0],n[1]),(n[1],n[0]),(n[1],e[0])]):demo[name]=dict(stamps=[i,j],shared_sites=len(set(a)&set(b)),shared_occurrences=len(set(i)&set(j)))
o=dict(stats=stats,minimal_path=demo);print(o);(D/'results/pne_occurrence_stamps.json').write_text(json.dumps(o,indent=2)+'\n')
