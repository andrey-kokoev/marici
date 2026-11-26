"""Uniform controls conditional on intersection size with the very same center clique. For each potential cut of <=8 hitting every fixed clique, record missed candidates. An omission succeeds iff it contains one such missed set."""
import json,random,math
from pathlib import Path
from collections import Counter
from pysat.solvers import Solver
from pysat.card import CardEnc
P=Path(__file__).resolve().parents[1]/'results';F={v for row in json.loads((P/'ramsey_square_edge_families.json').read_text()) for v in row[3]};r=next(r for r in json.loads((P/'ramsey_wedge_join_reversal.json').read_text()) if r['reversals']);q=sum(1<<int(i) for i in r['rotation']);pool={k:sorted(z for z in F if (q&z).bit_count()==k) for k in (3,5)};c=pool[3]+pool[5];fixed=F-set(c);n3=len(pool[3]);n5=len(pool[5]);idx=lambda v:sum(1<<i for i,z in enumerate(c) if not z&v);miss=set();num=0;clauses=[[i+1 for i in range(35) if z>>i&1] for z in fixed];
with Solver(name='g4',bootstrap_with=clauses+CardEnc.atmost(list(range(1,36)),8).clauses) as sl:
 while sl.solve():
  v=[i for i in sl.get_model() if 1<=i<=35];assert len(v)==8 # checked, not assumed
  m=idx(sum(1<<(i-1) for i in v));assert m;miss.add(m);num+=1;sl.add_clause([-i for i in v]);
minimal=[]
for m in sorted(miss,key=int.bit_count):
 if not any(t&m==t for t in minimal):minimal.append(m)
N=10000;rng=random.Random(391856);cnt=0
for _ in range(N):
 d=sum(1<<i for i in rng.sample(range(n3),18)+rng.sample(range(n3,n3+n5),6));cnt+=any(m&d==m for m in minimal)
out=dict(pool3=n3,pool5=n5,fixed=len(fixed),eligible_cuts=num,minimal_miss_patterns=len(minimal),miss_size_hist=dict(Counter(m.bit_count() for m in minimal)),samples=N,seed=391856,controls_reaching_eight=cnt);assert n5==6
# Removing all six size-five overlaps is mandatory. Maximize the size-three removals that still block every eight-cut.
blocks=[[-(i+1) for i in range(n3) if m>>i&1] for m in minimal];lo,hi=0,n3+1
while hi-lo>1:
 k=(lo+hi)//2
 with Solver(name='g4',bootstrap_with=blocks+CardEnc.atleast(list(range(1,n3+1)),k).clauses) as sl:
  if sl.solve():lo=k;example=[i-1 for i in sl.get_model() if 1<=i<=n3]
  else:hi=k
out.update(max_triple_removals_preserving_nine=lo,example=[pool[3][i] for i in example]);print(out);(P/'ramsey_reversal_cut_control.json').write_text(json.dumps(out,indent=1)+'\n')
