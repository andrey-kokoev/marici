"""Rank blue triples by number of individual maximal supports hitting them; ties kept, not broken by labels. Compute scores before enumerating quadruples. Test if one selected constraint eliminates every four-clique survivor. Discovery core 69 separated from five transfer cores."""
import json,itertools,collections
from pathlib import Path
P=Path(__file__).resolve().parents[1]/'results';gs=[r['core'] for r in json.loads((P/'ramsey_frontier_transfer.json').read_text()) if r['n']==11 and r['d']==4];ids=[r['row'] for r in json.loads((P/'ramsey_integer_bound11.json').read_text())];out=[]
for i in ids:
 a=gs[i];I=[0]
 for j,v in enumerate(a):I.extend([s|1<<j for s in I if not s&v])
 S=[s for s in I if all(s&(v|1<<j) for j,v in enumerate(a))];T=[q for q in I if q.bit_count()==3];Q=[q for q in I if q.bit_count()==4];scores={t:sum(bool(t&s) for s in S) for t in T};panel=[t for t in T if scores[t]==min(scores.values())];miss=[sum(1<<j for j,q in enumerate(Q) if not q&s) for s in S];terminal=[t for t in T if t in S];terminal_pass=0;reject=collections.Counter();hist=collections.Counter();n=0
 for z in itertools.combinations_with_replacement(range(len(S)),4):
  if any(miss[u]&miss[v] for u,v in itertools.combinations(z,2)):continue
  n+=1;bad=[t for t in T if sum(bool(t&S[j]) for j in z)<2];terminal_pass+=not set(bad).intersection(terminal);reject.update(bad);hist[sum(t in panel for t in bad)]+=1
 exact=[t for t in T if reject[t]==n];print(i,len(T),min(scores.values()),panel,n,[reject[t] for t in panel],exact,flush=True);print('maximal triples',terminal,'assignments left',terminal_pass);out.append(dict(row=i,maximal_triples=terminal,passing_maximal_triples=terminal_pass,triples=len(T),supports=len(S),score=scores,selected=panel,assignments=n,rejected=dict(reject),exact=exact,missed_by_panel=hist[0]))
(P/'ramsey_blind_triple11.json').write_text(json.dumps(out)+'\n')
