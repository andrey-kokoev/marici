"""Check whether successful 26/34 cores can themselves grow one vertex at previous k; certify deletion equivalence for generated 35."""
from ramsey_port_clique_transfer import inputs,D,json,graph
import networkx as nx

def asgraph(A):
    G=nx.empty_graph(len(A));G.add_edges_from((u,v) for v,row in enumerate(A) for u in range(v) if row>>u&1);return G
A=json.loads((D/'ramsey_port_clique_k9.json').read_text())['graph'];C=graph((1,7,11,16));gm=nx.isomorphism.GraphMatcher(asgraph(A),asgraph(C));assert gm.is_isomorphic();p=[gm.mapping[i] for i in range(35)];assert all(((A[i]>>j)&1)==(C[p[i]]>>p[j]&1) for i in range(35) for j in range(35));print('cyclic chart',p)
result={'generated35_to_cyclic':p,'previous_level_extensions':{}}
for k in (9,10):
    H,d=inputs(k);I=[0]
    for i,row in enumerate(H):I += [x|1<<i for x in I if not row&x]
    top=[x for x in I if x.bit_count()==k-2];hits=[x for x in I if all(x&t for t in top)];result['previous_level_extensions'][k]=hits;print('k',k,'core',len(H),'top',len(top),'independent hitting neighborhoods',len(hits))
(D/'ramsey_core_extendibility_calibration.json').write_text(json.dumps(result)+'\n')
