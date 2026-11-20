"""Exhaust linear strip rank signs via subset DP, allowing *any* order of ten sites. Reverse-path sign is covered by reversing the chosen order; also allow an independently selected reversal at each pole. Compare to a completely unrestricted directed endpoint lookup. No frame used as input to a prediction within a pole."""
import json
from collections import defaultdict,Counter
from pathlib import Path
D=Path(__file__).resolve().parents[1]/'results';rows=json.loads((D/'ramsey_37_ordered_star_sign.json').read_text());V=sorted({r['slot'] for r in rows});n=len(V)
def test(rs,rev):
    wants=defaultdict(Counter);w=[[0]*n for _ in V]
    for r in rs:
        u,v=V.index(r['slot']),V.index(r['continuation']);s=r['change']*(-1 if rev and r['pole']=='pole6' else 1);wants[u,v][s]+=1
        if s<0:u,v=v,u
        w[u][v]+=1
    dp=[0]*(1<<n);last={}
    for m in range(1,1<<n):
        dp[m],last[m]=max((dp[m^(1<<j)]+sum(w[i][j] for i in range(n) if m>>i&1),j) for j in range(n) if m>>j&1)
    order=[];m=(1<<n)-1
    while m:j=last[m];order.append(V[j]);m^=1<<j
    return dict(samples=len(rs),best_rank=dp[-1],best_order=order[::-1],best_endpoint_lookup=sum(max(c.values()) for c in wants.values()),conflicts=[[V[u],V[v]] for (u,v),c in wants.items() if len(c)>1])
out={}
for red in (True,False):
    for pole in ('pole0','pole6','both'):
        rs=[r for r in rows if (not red or r['red']) and (pole=='both' or r['pole']==pole)]
        for rev in ([False,True] if pole=='both' else [False]):out[f'{pole},red_only={red},reverse_pole6={rev}']=test(rs,rev)
print([(k,v['best_rank'],v['best_endpoint_lookup'],v['samples']) for k,v in out.items()]);(D/'ramsey_37_strip_order_sign.json').write_text(json.dumps(out,indent=2)+'\n')
