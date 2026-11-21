"""Backward calibration only: discover two port schedules from the cyclic 35; replay is separate."""
from ramsey_27_to_35_embedding import embedding,inputs,induce,D,json,combinations
from ramsey_port_chain_from_17 import read_seed
H=inputs(9)[0];r=5;U=[i for i in range(26) if i!=r and not H[r]>>i&1];K=induce(H,U);v=10;V=[i for i in range(21) if i!=v and not K[v]>>i&1];C=induce(K,V)
seed=read_seed((D/'pauli-realization-catalogues/r36_17.g6').read_bytes().splitlines()[4]);p=embedding(C,seed);missing=(set(range(17))-set(p.values())).pop();keep=sorted(p.values());inv={a:i for i,a in p.items()};base=[inv[a] for a in keep]
opened=[(a,b) for a,b in combinations(keep,2) if seed[a]>>b&1 and not C[inv[a]]>>inv[b]&1]
def recover(G,root,base):
    P=[i for i in range(len(G)) if G[root]>>i&1];assert set(base+P+[root])==set(range(len(G)))
    return [sum(1<<j for j,i in enumerate(base) if G[a]>>i&1) for a in P],base+P+[root]
s1,order=recover(K,v,[V[i] for i in base]);s2,_=recover(H,r,[U[i] for i in order]);schedule={'seed_index':5,'delete_vertex':missing,'delete_edges':opened,'to21':s1,'to26':s2};print(schedule);(D/'ramsey_slack_ladder_schedule.json').write_text(json.dumps(schedule)+'\n')
