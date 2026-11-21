"""Bounded search for nontrivial comparison return through backbone-changing operations. Moves: four-edge Hall-chart exchanges, rebase at other Hall center, full cooperative center transfer. All inverse moves preserve comparison information on their admitted domains."""
from pathlib import Path
from collections import deque,Counter
from itertools import combinations
import json,argparse
from ramsey_hall_center_conjecture import decode,root_profile
from ramsey_regular_two_switch import iso,relation
from ramsey_hall_center_four_exchange import P,T,matchings
D=Path(__file__).parent;catalogue=json.loads((D/'ramsey_hall_center_conjecture.json').read_text());C=decode(catalogue['regular'][-1]['graph6'].encode());example=json.loads((D/'ramsey_closed_repair_size5.json').read_text())[1]['first_valid_example'];MS=list(matchings())
def lift(G,c,R):
 U=[u for u in range(22) if G[c]>>u&1];assert {R[u] for u in U}==set(U);lookup={frozenset(u for u in U if G[w]>>u&1):w for w in range(22) if w!=c and w not in U};out=list(range(22))
 for u in U:out[u]=R[u]
 for s,w in lookup.items():out[w]=lookup[frozenset(R[u] for u in s)]
 return tuple(out)
def four(G,c):
 U=[u for u in range(22) if G[c]>>u&1];W=[w for w in range(22) if w!=c and w not in U];labels={tuple(k for k,u in enumerate(U) if G[w]>>u&1):w for w in W};E={e for e in combinations(range(22),2) if G[e[0]]>>e[1]&1};fixed={e for e in E if e[0] not in W or e[1] not in W};base={tuple(sorted((labels[P[i]],labels[P[j]]))) for i,j in combinations(range(15),2) if not set(P[i])&set(P[j])}
 for m in MS:
  removed={tuple(sorted(labels[P[k]] for k in T[j] if k!=i)) for i,j in m};F=fixed|(base-removed)
  if len(E-F)!=4:continue
  B=[0]*22
  for i,j in F:B[i]|=1<<j;B[j]|=1<<i
  yield tuple(B)
def neighbors(G,c,R):
 for B in four(G,c):
  removed=[(i,j) for i,j in combinations(range(22),2) if G[i]>>j&1 and not B[i]>>j&1];added=[(i,j) for i,j in combinations(range(22),2) if B[i]>>j&1 and not G[i]>>j&1]
  yield B,c,R,{'move':'four-edge','center':c,'removed':removed,'added':added}
 centers=[v for v in range(22) if root_profile(G,v)['hall_center']]
 for v in centers:
  if v!=c and R[v]==v and {R[u] for u in range(22) if G[v]>>u&1}=={u for u in range(22) if G[v]>>u&1}:yield G,v,lift(G,v,R),{'move':'rebase','from':c,'to':v}
 if len(centers)==1:
  f=iso(G,C,relation(G),relation(C));assert f is not None;back={v:k for k,v in f.items()};v=back[1]
  if R[v]!=v:return
  B=list(G)
  for s in example['switches']:
   for i,j in s['removed']+s['added']:
    a,b=back[i],back[j];B[a]^=1<<b;B[b]^=1<<a
  if {R[u] for u in range(22) if B[v]>>u&1}=={u for u in range(22) if B[v]>>u&1}:yield tuple(B),v,lift(B,v,R),{'move':'full-orbit-transfer','from':c,'to':v}
if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--nodes',type=int,default=1000);parser.add_argument('--depth',type=int,default=6);args=parser.parse_args();f={int(k):v for k,v in json.loads((D/'ramsey_center_transfer_seed_binding.json').read_text())['affine_to_catalogue'].items()};back={v:k for k,v in f.items()};r=(1,0,2,3,5,4);R0=[0]+[1+r[i] for i in range(6)]+[7+P.index(tuple(sorted(r[x] for x in d))) for d in P];R=tuple(f[R0[back[i]]] for i in range(22));start=(tuple(C),0,R);queue=deque([(start,[])]);seen={start};at={(tuple(C),0):(R,[])};expanded=0;collision=None;move_counts=Counter();depth_counts=Counter();reencounters=0
 fixed=[i for i in range(22) if R[i]==i];squares=[q for q in combinations(fixed,4) if all(sum(C[i]>>j&1 for j in q)==2 for i in q)];assert len(squares)==1;Q=set(squares[0]);center_counts=Counter()
 while queue and expanded<args.nodes:
  (G,c,R),path=queue.popleft()
  if len(path)>=args.depth:continue
  expanded+=1;depth_counts[len(path)]+=1;center_counts[c]+=1
  assert c in Q and all(R[i]==i for i in Q) and all(sum(G[i]>>j&1 for j in Q)==2 for i in Q)
  for B,v,S,move in neighbors(G,c,R):
   move_counts[move['move']]+=1
   nextpath=path+[move];state=(B,v,S);key=(B,v)
   if key in at:reencounters+=1
   if key in at and at[key][0]!=S:
    old,oldpath=at[key];collision={'graph':B,'center':v,'comparison_1':old,'comparison_2':S,'path_1':oldpath,'path_2':nextpath};break
   at.setdefault(key,(S,nextpath))
   if state not in seen:seen.add(state);queue.append((state,nextpath))
  if collision:break
 result={'conserved_fixed_square':sorted(Q),'centers_expanded':dict(center_counts),'moves_examined':dict(move_counts),'expanded_by_depth':dict(depth_counts),'graph_center_reencounters':reencounters,'expanded':expanded,'states_seen':len(seen),'queued':len(queue),'max_depth':args.depth,'node_budget':args.nodes,'collision':collision};(D/'ramsey_frame_loop_search.json').write_text(json.dumps(result,indent=2)+'\n');print(result)
