"""Degree-free test: can the retained 20 and a single additional small cell satisfy the local <=4-label demands without a red triangle? Extract deletion-minimal sets of coverage and triangle clauses for a representative of each label orbit. The full 26-vertex graph and other five cells play no role in a local UNSAT."""
from ramsey_unsaturated_free_six_gate import fixed,P,pairs,Solver,json,itertools,partial
cap=(0,1,3,5,8,12,16,19,26);S=[s for s in range(1,256) if all(1+sum(not x&~t for x in fixed)<=cap[t.bit_count()] for t in range(256) if not s&~t)];G=[]
for p in itertools.permutations(range(8)):
 img=lambda s:sum(1<<p[i] for i in range(8) if s>>i&1)
 if {img(s) for s in fixed}==set(fixed):G.append([img(s) for s in range(256)])
rows=[]
for s in S:
 orb={g[s] for g in G}
 if s!=min(orb):continue
 m=fixed+(s,);E={p:i+1 for i,p in enumerate(p for p in pairs(range(21),2) if not m[p[0]]&m[p[1]])};C={}
 for t in range(256):
  if t.bit_count()>4:continue
  for q in pairs([i for i,x in enumerate(m) if not x&~t],t.bit_count()+1):C[tuple(E[p] for p in pairs(q,2) if p in E)]=('cover',t,*q)
 for q in pairs(range(21),3):
  es=list(pairs(q,2));
  if all(p in E for p in es):C[tuple(-E[p] for p in es)]=('triangle',*q)
 cs=list(C);v=len(E)+1;rec=dict(s=s,n=len(orb),partial=partial((s,)))
 with Solver(name='cadical195',bootstrap_with=[[-v-j,*c] for j,c in enumerate(cs)]) as sl:
  a=list(range(v,v+len(cs)));rec['without_degrees']=sl.solve(assumptions=a)
  if not rec['without_degrees']:
   core=sl.get_core();
   for j in core[:]:
    if j in core and not sl.solve(assumptions=[i for i in core if i!=j]):core=sl.get_core()
   rec['reason']=[C[cs[i-v]] for i in core]
 rows.append(rec)
print([(z['s'],z['n'],z['partial'],z['without_degrees'],len(z.get('reason',[]))) for z in rows]);(P/'ramsey_unsaturated_one_cell_obstruction.json').write_text(json.dumps(rows)+'\n')
