"""Recover root-stabilizing symmetries before examining repair pairs; test unique C5 orbit pairing and relative-phase predictions."""
from pathlib import Path
from itertools import permutations,combinations
import json
from ramsey_hall_center_conjecture import decode
from ramsey_mutual_repair_conjecture import switches,repairs

def key(s):return tuple(sorted(tuple(sorted(e)) for e in s['removed'])),tuple(sorted(tuple(sorted(e)) for e in s['added']))
def transport(k,p):return tuple(tuple(sorted(tuple(sorted((p[a],p[b]))) for a,b in side)) for side in k)
def compose(a,b):return tuple(a[b[i]] for i in range(22))
def cyclic_group(p):
 identity=tuple(range(22));g=identity;out=[]
 while g not in out:out.append(g);g=compose(p,g)
 assert g==identity;return frozenset(out)
def root_auts(A):
 U=[i for i in range(22) if A[0]>>i&1];W=[i for i in range(1,22) if i not in U];labels={tuple(u for u in U if A[w]>>u&1):w for w in W};assert len(labels)==15
 for image in permutations(U):
  p={0:0,**dict(zip(U,image))}
  for S,w in labels.items():p[w]=labels[tuple(sorted(p[u] for u in S))]
  if all(((A[i]>>j)&1)==((A[p[i]]>>p[j])&1) for i,j in combinations(range(22),2)):yield tuple(p[i] for i in range(22))

if __name__=='__main__':
 data=json.loads(Path(__file__).with_name('ramsey_hall_center_conjecture.json').read_text());report=[]
 for r in data['regular']:
  if r['record'] not in (190,191):continue
  A=decode(r['graph6'].encode());auts=list(root_auts(A));groups={cyclic_group(p) for p in auts if len(cyclic_group(p))==5};assert len(groups)==1;G=next(iter(groups));p=min(g for g in G if g!=tuple(range(22)));moves={key(s):s for s in switches(A)};todo=set(moves);orbits=[]
  while todo:
   k=min(todo);orbit=[];q=k
   while q not in orbit:orbit.append(q);q=transport(q,p)
   assert len(orbit)==5 and set(orbit)<=set(moves);todo-=set(orbit);orbits.append(orbit)
  successful=[(s,t) for s,t in combinations(moves,2) if not moves[s]['support']&moves[t]['support'] and repairs(moves[s],moves[t]) and repairs(moves[t],moves[s])];participants={s for pair in successful for s in pair};participating=[i for i,o in enumerate(orbits) if set(o)&participants];phases=[]
  if successful:
   assert len(participating)==2 and participants==set().union(*(set(orbits[i]) for i in participating));a,b=successful[0];paired=[]
   for _ in range(5):paired.append(frozenset((a,b)));a=transport(a,p);b=transport(b,p)
   assert set(paired)=={frozenset(z) for z in successful};a,b=successful[0]
   for phase in range(5):
    s,t=moves[a],moves[b];phases.append({'relative_phase':phase,'disjoint':not bool(s['support']&t['support']),'A_repairs_B':repairs(t,s),'B_repairs_A':repairs(s,t),'A_bad_count':len(s['bad']),'B_bad_count':len(t['bad']),'B_bad_containing_root':sum(bool(mask&1) for mask in t['bad']),'A_repairs_B_root_obstructions':all(any(mask>>i&1 and mask>>j&1 for i,j in s['added']) for mask in t['bad'] if mask&1)});b=transport(b,p)
  result={'source':r['record'],'root_automorphisms':len(auts),'unique_C5_generator':p,'switch_orbits':len(orbits),'participating_orbits':participating,'successful_pairs':len(successful),'phase_table':phases};report.append(result);print(result)
 Path(__file__).with_suffix('.json').write_text(json.dumps(report,indent=2)+'\n')
