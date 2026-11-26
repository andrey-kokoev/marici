"""Combinatorial replay: if |Q|>|union labels| then at least one pair in Q must be red. Shared labels forbid edges; red two-paths forbid others. Propagate single options in batches and save witnesses. No SAT, degree constraints, or assumptions on completion symmetry."""
import json,itertools,collections
from pathlib import Path
P=Path(__file__).resolve().parents[1]/'results';R=json.loads((P/'ramsey_incidence_distinct35.json').read_text());out=[]
for z in R['cases']:
 m=z['masks'];pairs=lambda q:list(itertools.combinations(q,2));clauses=set()
 for t in range(256):
  if t.bit_count()>5:continue
  for q in itertools.combinations([i for i,s in enumerate(m) if not s&~t],t.bit_count()+1):clauses.add(q)
 red=[0]*26;log=[]
 while True:
  grow={};fail=None
  for q in sorted(clauses,key=lambda q:(len(q),q)):
   pp=pairs(q)
   if any(red[i]>>j&1 for i,j in pp):continue
   avail=[e for e in pp if not m[e[0]]&m[e[1]] and not red[e[0]]&red[e[1]]];
   if not avail:fail=q;break
   if len(avail)==1:grow.setdefault(avail[0],q)
  if fail:break
  assert grow
  for i,j in grow:red[i]|=1<<j;red[j]|=1<<i
  log.append([dict(edge=e,demand=q) for e,q in grow.items()]);
 out.append(dict(masks=m,stages=log,contradiction=fail));print([len(v) for v in log],fail)
(P/'ramsey_incidence_unit35.json').write_text(json.dumps(out)+'\n')
