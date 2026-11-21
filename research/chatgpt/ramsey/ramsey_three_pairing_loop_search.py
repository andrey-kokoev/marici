"""Transport all three off-square pairings simultaneously. Detect holonomy invisible to the original comparison."""
from collections import deque,Counter
from itertools import combinations
import json,argparse
from ramsey_frame_loop_search import D,C,P,lift,neighbors

if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--nodes',type=int,default=5000);parser.add_argument('--depth',type=int,default=9);args=parser.parse_args();f={int(k):v for k,v in json.loads((D/'ramsey_center_transfer_seed_binding.json').read_text())['affine_to_catalogue'].items()};back={v:k for k,v in f.items()};r=(1,0,2,3,5,4);R0=[0]+[1+r[i] for i in range(6)]+[7+P.index(tuple(sorted(r[x] for x in d))) for d in P];R=tuple(f[R0[back[i]]] for i in range(22));fixed=[i for i in range(22) if R[i]==i];squares=[q for q in combinations(fixed,4) if all(sum(C[i]>>j&1 for j in q)==2 for i in q)];assert len(squares)==1;Q=set(squares[0]);ports=[u for u in range(22) if C[0]>>u&1 and u not in Q];a,b,c,d=ports;alternatives=[]
 for pairs in [((a,b),(c,d)),((a,c),(b,d)),((a,d),(b,c))]:
  action=list(range(22))
  for i,j in pairs:action[i]=j;action[j]=i
  alternatives.append(lift(C,0,action))
 assert R in alternatives;Rs=(R,)+tuple(S for S in alternatives if S!=R);start=(tuple(C),0,Rs);queue=deque([(start,[])]);seen={start};at={(tuple(C),0):(Rs,[])};expanded=0;collision=None;depths=Counter();moves=Counter();reencounters=0
 while queue and expanded<args.nodes:
  (G,c,Rs),path=queue.popleft()
  if len(path)>=args.depth:continue
  expanded+=1;depths[len(path)]+=1
  for B,v,S,move in neighbors(G,c,Rs[0]):
   Ss=Rs if move['move']=='four-edge' else tuple(lift(B,v,Ri) for Ri in Rs);assert Ss[0]==S and len(set(Ss))==3;assert all(all(Ri[q]==q for q in Q) for Ri in Ss);moves[move['move']]+=1;key=(B,v);nextpath=path+[move]
   if key in at:
    reencounters+=1;old,oldpath=at[key];assert set(old)==set(Ss)
    if old!=Ss:
     collision={'graph':B,'center':v,'permutation_of_pairings':[old.index(Si) for Si in Ss],'old_comparisons':old,'new_comparisons':Ss,'path_1':oldpath,'path_2':nextpath};break
   at.setdefault(key,(Ss,nextpath));state=(B,v,Ss)
   if state not in seen:seen.add(state);queue.append((state,nextpath))
  if collision:break
 result={'conserved_square':sorted(Q),'initial_ports':ports,'initial_comparisons':start[2],'expanded':expanded,'states_seen':len(seen),'queued':len(queue),'expanded_by_depth':dict(depths),'moves_examined':dict(moves),'reencounters':reencounters,'node_budget':args.nodes,'depth_ceiling':args.depth,'collision':collision};(D/'ramsey_three_pairing_loop_search.json').write_text(json.dumps(result,indent=2)+'\n');print({k:v for k,v in result.items() if k not in ('initial_comparisons','collision')});print('collision',collision)
