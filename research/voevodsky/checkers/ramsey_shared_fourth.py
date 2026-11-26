"""Select demands from triples of supports, before looking at a fourth support. Each selected blue triple witnesses a violation by three mutually four-clique-compatible supports. Greedily cover distinct bad support triples, not frequencies of completed assignments. Validate using exact completions and a minimum hitting-set oracle solely for comparison."""
import json,itertools
from pathlib import Path
P=Path(__file__).resolve().parents[1]/'results';gs=[r['core'] for r in json.loads((P/'ramsey_frontier_transfer.json').read_text()) if r['n']==11 and r['d']==4];out=[]
for i in (80,97):
 a=gs[i];I=[0]
 for j,v in enumerate(a):I.extend([s|1<<j for s in I if not s&v])
 S=[s for s in I if all(s&(v|1<<j) for j,v in enumerate(a))];Q=[q for q in I if q.bit_count()==4];T=[q for q in I if q.bit_count()==3];assert all(any(t&q==t for q in Q) for t in T);M=[sum(1<<j for j,q in enumerate(Q) if not q&s) for s in S]
 def legal(z):return all(not M[u]&M[v] for u,v in itertools.combinations(z,2))
 R={t:set() for t in T};atoms=[]
 for z in itertools.combinations_with_replacement(range(len(S)),3):
  if not legal(z):continue
  bad=[t for t in T if not any(S[u]&t for u in z)]
  if bad:
   for t in bad:R[t].add(len(atoms))
   atoms.append(z)
 alive=set(range(len(atoms)));panel=[]
 while alive:
  t=max(T,key=lambda t:(len(alive&R[t]),-t));assert alive&R[t];panel.append(t);alive-=R[t]
 rows=[z for z in itertools.combinations_with_replacement(range(len(S)),4) if legal(z)];bad=[{t for t in T if sum(bool(S[u]&t) for u in z)<2} for z in rows];curve=[sum(not x.intersection(panel[:j]) for x in bad) for j in range(len(panel)+1)];assert curve[-1]==0
 # Branch on smallest still-unhit witness to prove optimum, allowing overlap across branches.
 best=panel[:curve.index(0)]
 def opt(chosen,left):
  global best
  if not left:best=chosen;return
  if len(chosen)+1>=len(best):return
  for t in sorted(min(left,key=len)):
   nex=[x for x in left if t not in x];opt(chosen+[t],nex)
 opt([],bad)
 tie_lengths=set()
 def ties(left,p):
  if all(x.intersection(p) for x in bad):tie_lengths.add(len(p));return
  gain=max(len(left&R[t]) for t in T);assert gain
  for t in T:
   if len(left&R[t])==gain:ties(left-R[t],p+[t])
 ties(set(range(len(atoms))),[]);print('greedy closure across ties',sorted(tie_lengths));out.append(dict(row=i,atoms=len(atoms),panel=panel,curve=curve,optimum=best,tie_lengths=sorted(tie_lengths)));print(i,len(atoms),len(panel),curve,best,panel[:curve.index(0)])
(P/'ramsey_shared_fourth.json').write_text(json.dumps(out)+'\n')
