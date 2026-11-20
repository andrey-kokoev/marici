"""All root sequences, grouped by the unordered minus clique of roots. The remaining core is their common minus neighborhood. No choice of root ordering can change it. Also compare all seven catalogued extremal (3,6) graphs."""
from pathlib import Path
from collections import Counter
import json
H=Path(__file__).resolve().parents[1];D=H/'results'
def profile(n,k,E):
    U=(1<<n)-1;B=[U^(1<<i) for i in range(n)]
    for a,b in E:B[a]&=~(1<<b);B[b]&=~(1<<a)
    hist=[Counter() for _ in range(k)];w=[None]*k
    def visit(roots,c,after):
        t=roots.bit_count();assert t<k;sz=c.bit_count();hist[t][sz]+=1
        if w[t] is None or sz>w[t][0]:w[t]=(sz,roots,c)
        a=c&after
        while a:
            b=a&-a;a-=b;i=b.bit_length()-1;visit(roots|b,c&B[i],~(2*b-1))
    visit(0,U,U);out=[]
    for t,(size,r,c) in enumerate(w):
        verts=lambda m:[i for i in range(n) if m>>i&1];R=verts(r);assert verts(c)==[j for j in range(n) if all(B[i]>>j&1 for i in R)]
        out.append(dict(depth=t,target=k-t,max_core=size,attaining_sets=hist[t][size],hist=dict(sorted(hist[t].items())),root_witness=R,core_witness=verts(c)))
    def chain(c,t):
        if t==k-2:return []
        a=c
        while a:
            b=a&-a;a-=b;i=b.bit_length()-1;q=c&B[i]
            if q.bit_count()!=out[t+1]['max_core']:continue
            rest=chain(q,t+1)
            if rest is not None:return [i]+rest
        return None
    out[0]['jointly_maximizing_root_order_through_target_2']=chain(U,0)
    return out

def main():
    graphs=[(27,8,json.loads((D/'ramsey_38_root_glue.json').read_text())['witness']['plus_edges']),(35,9,json.loads((D/'ramsey_39_glue_vs_circle.json').read_text())['plus_edges'])];profiles={str(n):profile(n,k,E) for n,k,E in graphs};degrees=[]
    for g in (H.parent/'chatgpt/ramsey/pauli-realization-catalogues/r36_17.g6').read_text().splitlines():
        assert ord(g[0])-63==17;bits=''.join(f'{ord(c)-63:06b}' for c in g[1:]);edges=[(a,b) for b in range(17) for a in range(b) if bits[b*(b-1)//2+a]=='1'];degrees.append(min(sum(v in e for e in edges) for v in range(17)))
    out=dict(profiles=profiles,minimum_plus_degrees_catalogue_17=degrees);print({n:[(r['target'],r['max_core'],r['attaining_sets']) for r in p] for n,p in profiles.items()},degrees);(D/'ramsey_root_chain_envelopes.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()
