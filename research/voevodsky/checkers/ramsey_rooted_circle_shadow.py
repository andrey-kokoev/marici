"""Test exact induced embedding (no switching, both signs preserved), modulo host translations."""
import json
from pathlib import Path
H=Path(__file__).resolve().parents[1]/'results'
def embed(n,E):
    host=[sum(1<<((i+d)%35) for d in (1,-1,7,-7,11,-11,16,-16)) for i in range(35)];adj=[set() for _ in range(n)]
    for i,j in E:adj[i].add(j);adj[j].add(i)
    root=max(range(n),key=lambda i:len(adj[i]));U=(1<<35)-1;steps=0
    def dfs(D,m):
        nonlocal steps;steps+=1
        if not D:return m
        v=min(D,key=lambda v:(D[v].bit_count(),-len(adj[v])));a=D[v]
        while a:
            b=a&-a;a-=b;j=b.bit_length()-1
            dd={w:t&~b&(host[j] if w in adj[v] else ~host[j]) for w,t in D.items() if w!=v}
            if all(dd.values()):
                z=dfs(dd,{**m,v:j})
                if z is not None:return z
    D={v:1 if v==root else U for v in range(n)};m=dfs(D,{})
    if m is not None:assert len(set(m.values()))==n and all(bool((host[m[i]]>>m[j])&1)==(j in adj[i]) for i in range(n) for j in range(i))
    return dict(vertices=n,root_fixed_to_zero=root,search_nodes=steps,image=m)
if __name__=='__main__':
    E=json.loads((H/'ramsey_37_root_glue.json').read_text())['witness']['plus_edges'];F=json.loads((H/'ramsey_38_root_glue.json').read_text())['witness']['plus_edges'];out=[embed(17,[(i-5,j-5) for i,j in E if i>=5]),embed(22,E),embed(27,F)];print(out);(H/'ramsey_rooted_circle_shadow.json').write_text(json.dumps(out,indent=2)+'\n')
