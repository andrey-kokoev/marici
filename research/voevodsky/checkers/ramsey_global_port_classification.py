"""Try all three marked counterexamples at every root of the classified (3,9;35) graph. Theorem 3 is an external classification, not reproved here."""
import json
from itertools import combinations
from collections import Counter
from pathlib import Path

def run():
    n=35;steps=(1,7,11,16);N=[{(r+s*d)%n for d in steps for s in (1,-1)} for r in range(n)];a=[sum(1<<v for v in row) for row in N];I=[0]
    for i,v in enumerate(a):I.extend([s|1<<i for s in I if not s&v]);
    assert max(map(int.bit_count,I))==8 and all(not N[i]&N[j] for i in range(n) for j in N[i]);fails=Counter();tot=Counter();certificate=None
    for root,ports in enumerate(N):
        R={i:N[i]-ports-{root} for i in ports};assert all(len(s)==7 for s in R.values());pairs=list(combinations(sorted(ports),2));over={p:len(R[p[0]]&R[p[1]]) for p in pairs};zero=[p for p,k in over.items() if k==0];two=[p for p,k in over.items() if k==2];three=[p for p,k in over.items() if k==3];bad=[i for i in ports if sum(i in p for p in zero)!=1];color={};ok=True
        for v in sorted(ports):
            if v in color:continue
            color[v]=0;stack=[v]
            while stack:
                i=stack.pop()
                for j in ports:
                    if tuple(sorted((i,j))) not in three:continue
                    if j not in color:color[j]=1-color[i];stack.append(j)
                    elif color[i]==color[j]:ok=False
        fails.update(dict(nonunique_port=len(bad),two_site_pairs=len(two),nonbipartite_roots=int(not ok)));tot.update(dict(roots=1,marked_ports=len(ports),marked_pairs=len(pairs)));assert all(over[(i,j)]+1==len(N[i]&N[j]) for i,j in pairs)
        if root==0:certificate=dict(ports=sorted(ports),opposites=zero,overlap_hist=Counter(over.values()),parts=[sorted(i for i in ports if color[i]==k) for k in (0,1)],three_site_edges=three)
    assert not any(fails.values());out=dict(source='Goedgebeur and Radziszowski, EJC 20(1), P30 (2013), Theorem 3, p. 12',doi='10.37236/2824',inspected_pdf_sha256='d2abf9b7c2c184869d6d1caa080e47e27cd75d918d8bd541698b2c311572b2cb',cyclic_distances=steps,coverage=tot,counterexamples=fails,root_zero=certificate);print(out);(Path(__file__).resolve().parents[1]/'results/ramsey_global_port_classification.json').write_text(json.dumps(out,indent=1)+'\n')
if __name__=='__main__':run()
