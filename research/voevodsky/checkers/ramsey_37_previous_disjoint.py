"""Decode opposite pole by its disjoint counterpart and compare to a history readout on the native PN-entry and NE-arrival pair orbits. Reference direction from pole0_successor, no permutation search."""
import json,itertools
from pathlib import Path
D=Path(__file__).resolve().parents[1]/'results';load=lambda n:json.loads((D/(n+'.json')).read_text());r=load('ramsey_37_dual_stars');S,T=[[set(s) for s in f] for f in r['stars']];T=[next(t for t in T if not t&s) for s in S];succ=load('ramsey_37_star_addresses')['pole0_successor'];V=sorted(set.union(*S));edges={tuple(sorted(e)) for e in r['red_edges']};A={v:frozenset(i for i,s in enumerate(S) if v in s) for v in V};B={v:frozenset(i for i,s in enumerate(T) if v in s) for v in V}
def prev(p,step):
 q=p
 for k in range(1,6):
  q=frozenset(step[x] for x in q)
  if not q&p:return k,q
 raise AssertionError
inv=[succ.index(i) for i in range(5)];assert all(prev(A[v],inv)[1]==B[v] for v in V)
# An observed orbit order fixes the position map up to its starting star; cyclic recuts give the same predicates.
natives=load('pne_all_exit_opportunities');out=[]
for n in natives:
 if n['mode']!='arrival-only':continue
 # recover the coefficient cycle from consecutive observed entry pairs (the shared endpoint advances)
 P,E=n['entry'],n['exit'];P0=[set(p) for p in P];ring=[next(iter(P0[i-1]&P0[i])) for i in range(5)];idx=dict(zip(ring,range(5)));names={k:frozenset(idx[x] for x in k) for k in P+E};back=[(i-1)%5 for i in range(5)];opp={k:prev(v,back)[1] for k,v in names.items()};oracle={k:next(v for v in V if A[v]==a) for k,a in names.items()};assert all(opp[k]==B[v] for k,v in oracle.items());pred={(a,b) for a,b in itertools.combinations(names,2) if not names[a]&names[b] and not opp[a]&opp[b]};truth={(a,b) for a,b in itertools.combinations(names,2) if tuple(sorted((oracle[a],oracle[b]))) in edges};assert pred==truth and len(pred)==10;out.append(dict(advance=n['advance'],perm=n['perm'],ring=ring,lags=[prev(names[p],back)[0] for p in P+E],predicted=sorted(pred)))
(D/'ramsey_37_previous_disjoint.json').write_text(json.dumps(out,indent=2)+'\n');print(len(V),len(out),out[0]['lags'])
