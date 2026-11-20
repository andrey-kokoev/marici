"""Effect of a single pole bit on red-walk transport. Check equitable partition and exact walk counts; all-length identity follows by telescoping powers, with every middle vertex seeing the same number of length-i walks to either pole (separate pole seeds, five-cycle orbit quotient)."""
from pathlib import Path
import json
D=Path(__file__).resolve().parents[1]/'results';g=json.loads((D/'ramsey_37_dual_stars.json').read_text());M=sorted(g['rows'][1]+g['rows'][2]);orb=[[0],[6],g['rows'][0],g['rows'][3],M];E=set(map(tuple,g['red_edges']));tables=[];walks=[]
for bit in (0,1):
    edges=E if bit else E-{(0,6)};N=[{j for j in range(22) if tuple(sorted((u,j))) in edges} for u in range(22)];Q=[[len(N[o[0]]&set(t)) for t in orb] for o in orb];assert all([len(N[v]&set(t)) for t in orb]==row for o,row in zip(orb,Q) for v in o);tables.append(Q);w=[[int(i==j) for j in range(22)] for i in range(22)];seq=[]
    for k in range(10):
        seq.append([[w[i][j] for j in M] for i in M]);w=[[sum(w[v][j] for v in N[i]) for j in range(22)] for i in range(22)]
    walks.append(seq)
deltas=[]
for a,b in zip(*walks):
    ds={v-u for x,y in zip(a,b) for u,v in zip(x,y)};assert len(ds)==1;deltas.append(ds.pop())
assert deltas[:6]==[0,0,0,0,0,8];out=dict(middle=M,parts=orb,blue_and_red_quotients=tables,common_red_minus_blue_walk_delta_by_length=deltas);print(deltas);(D/'ramsey_37_pole_walk_transfer.json').write_text(json.dumps(out,indent=2)+'\n')
