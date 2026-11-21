"""Test shared 26-core hypothesis by full adjacency isomorphism, not degree matching."""
from ramsey_port_lookahead import nxgraph,nx
from ramsey_port_clique_transfer import inputs,induce,D,json
A,_=inputs(9);B,_=inputs(10);found=[]
for v,r in enumerate(B):
    V=[i for i in range(len(B)) if i!=v and not r>>i&1]
    if len(V)!=26:continue
    gm=nx.isomorphism.GraphMatcher(nxgraph(A),nxgraph(induce(B,V)))
    if not gm.is_isomorphic():continue
    m=[V[gm.mapping[i]] for i in range(26)];assert all((A[i]>>j&1)==(B[m[i]]>>m[j]&1) for i in range(26) for j in range(26));P=[i for i in range(34) if r>>i&1];s=[sum(1<<i for i,j in enumerate(m) if B[p]>>j&1) for p in P];found.append({'root':v,'embedding':m,'supports':s});print('embedding root',v,'sizes',list(map(int.bit_count,s)))
(D/'ramsey_common_port_core.json').write_text(json.dumps(found)+'\n')
