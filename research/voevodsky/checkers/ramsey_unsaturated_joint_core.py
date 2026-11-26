"""Test whether the best archived unsaturated incidence can escape by rebuilding every core edge. Find a deletion-minimal conflicting set of five-label demands on top of all four-label demands."""
from ramsey_incidence_first35 import P,CardEnc,Solver,itertools,json
r=json.loads((P/'ramsey_unanchored_saturation.json').read_text());i=r['archive_control']['node'];m=json.loads((P/'ramsey_incidence_joint_beam.json').read_text())['nodes'][i]['m'];pairs=itertools.combinations;E={p:k+1 for k,p in enumerate(p for p in pairs(range(26),2) if not m[p[0]]&m[p[1]])};n=len(E);cs=[]
for i,s in enumerate(m):
 b=CardEnc.equals([w for e,w in E.items() if i in e],8-s.bit_count(),top_id=n);n=max(n,b.nv);cs+=b.clauses
for xs in pairs(range(26),3):
 es=list(pairs(xs,2));
 if all(p in E for p in es):cs.append([-E[p] for p in es])
tags={}
for t in range(256):
 k=t.bit_count()
 if k>5:continue
 guard=[]
 if k==5:n+=1;tags[n]=t;guard=[-n]
 for xs in pairs([i for i,s in enumerate(m) if not s&~t],k+1):cs.append(guard+[E[p] for p in pairs(xs,2) if p in E])
with Solver(name='cadical195',bootstrap_with=cs) as sl:
 assert sl.solve() and not sl.solve(assumptions=list(tags));core=sl.get_core();
 for x in core[:]:
  test=[y for y in core if y!=x]
  if not sl.solve(assumptions=test):core=test
 assert not sl.solve(assumptions=core) and all(sl.solve(assumptions=[y for y in core if y!=x]) for x in core)
out=dict(node=r['archive_control']['node'],five_masks=[tags[x] for x in core]);print(out);(P/'ramsey_unsaturated_joint_core.json').write_text(json.dumps(out)+'\n')
