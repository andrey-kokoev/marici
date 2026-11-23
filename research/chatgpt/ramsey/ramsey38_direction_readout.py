"""Replay compact fork reading. Only static input red adjacency is accessed by predict. Compare labels with previously archived output continuation tests afterwards."""
from ramsey38_direction_motifs import D,C,J,E,S,P,r,images,json
rule=json.loads((D/'ramsey38_direction_motif_freeze.json').read_text());star,=[s for s in S if s.bit_count()==4];pairs={s for s in S if s.bit_count()==2};z,=[i for i in range(7) if all((1<<i|1<<j) in pairs for j in range(7) if i!=j)];ab=[i for i in range(7) if i!=z and not star>>i&1];W=sorted(r['wirings'])
def forks(c):
 O=set()
 for a,b in (ab,ab[::-1]):
  v=S.index(1<<b|1<<z)
  for x in range(7):
   if star>>x&1 and x<c[x]:O.add(tuple(sorted(E.index(tuple(sorted((v,S.index(1<<a|1<<j))))) for j in [x,c[x]])))
 assert O==images(c,rule['motif_edge_indices']);return O
def predict(w,c):return sum(all(w>>e&1 for e in row) for row in forks(c))
scores=[[predict(w,c) for c in (C,J)] for w in W];known=json.loads((D/'ramsey38_relative_query.json').read_text())['per_input'];assert all({*s}=={0,2} and all((a==2)==(b==46) for a,b in zip(s,t)) for s,t in zip(scores,known));assert all({tuple(sorted(g[e] for e in row)) for row in forks(c)}==forks(next(k for k in (C,J) if all(p[c[i]]==k[p[i]] for i in range(7)))) for p,g in P.items() for c in (C,J));o=dict(input_forks=scores,continuation_scores=known,calibration_inputs=1,other_starts=7,covariant_relabelings=len(P));print(o);(D/'ramsey38_direction_readout.json').write_text(json.dumps(o,indent=2)+'\n')
