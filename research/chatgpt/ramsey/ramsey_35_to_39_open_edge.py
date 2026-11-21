"""Construct 39 vertices from cyclic 35: delete 0, test every legal one-edge deletion, glue four ports."""
from ramsey_ports_saturated_core import graph,induce,combinations,independent,four,D,json
H=induce(graph((1,7,11,16)),range(1,35));F=(1<<34)-1;rows=[]
for i,j in combinations(range(34),2):
    if not H[i]>>j&1:continue
    # Any newly independent nine must use both endpoints and seven common nonneighbors.
    if independent(H,F&~(H[i]|H[j]),7):continue
    B=H[:];B[i]^=1<<j;B[j]^=1<<i;r=four(B);r['removed']=(1+i,1+j);rows.append(r);print(r,flush=True)
(D/'ramsey_ports_one_edge_open.json').write_text(json.dumps(rows)+'\n')
