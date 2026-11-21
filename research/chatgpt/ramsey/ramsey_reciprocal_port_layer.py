"""Enumerate reciprocal-root four-port completions. Prescribe no supports or output degrees. An involution swaps the new root with a port and pairs its three other neighbors on each side."""
from itertools import combinations,combinations_with_replacement
from collections import Counter
import networkx as nx
from ramsey_slack_ladder_replay import D,json,read_seed,induce,attach,verify,independent
from ramsey_port_lookahead import nxgraph

def reciprocal(H,k=7):
    n=len(H);d=4;J=nxgraph(H);seen=set()
    for S in combinations(range(n),d-1):
        sm=sum(1<<v for v in S)
        if any(H[v]&sm for v in S):continue
        V=set(range(n))-set(S);K=J.subgraph(V)
        for p in nx.isomorphism.GraphMatcher(K,K).isomorphisms_iter():
            if any(p[p[i]]!=i for i in V) or sum(i==p[i] for i in V)!=1:continue
            outside=[sum(1<<p[x] for x in V if H[v]>>x&1) for v in S]
            cells=list(combinations_with_replacement(range(d-1),2))
            for bits in range(1<<len(cells)):
                T=outside[:]
                for b,(i,j) in enumerate(cells):
                    if bits>>b&1:T[i]|=1<<S[j];T[j]|=1<<S[i]
                if any(m.bit_count()>=k-1 or any(H[j]&m for j in range(n) if m>>j&1) for m in T):continue
                ports=tuple(sorted([sm]+T));
                if ports in seen:continue
                seen.add(ports);G=attach(H,ports)
                if not independent(G,(1<<len(G))-1,k):yield ports,G

def calibrated_seed():
    A=read_seed((D/'pauli-realization-catalogues/r36_17.g6').read_bytes().splitlines()[4]);
    for i in [12,16]:A[2]^=1<<i;A[i]^=1<<2
    return induce(A,[i for i in range(17) if i!=5])
if __name__=='__main__':
    import subprocess,sys
    from ramsey_hall_anchor_ports import anchor_lift
    H=calibrated_seed();verify(H,6);stats=Counter();rows=[];pr=set()
    for S,K in reciprocal(H):
        stats['21s']+=1
        p=subprocess.run([sys.argv[1],*map(str,K)],capture_output=True,text=True,check=True)
        for l in p.stdout.splitlines():
            T=list(map(int,l.split()));B=attach(K,T);stats['26s']+=1;res=anchor_lift(B,9)
            if res and 'graph' in res:verify(res['graph'],9);rows.append({'to21':S,'to26':T,'to35':res});pr.add(S)
    print(stats,'successful 21s',len(pr),'schedules',len(rows));(D/'ramsey_reciprocal_ladder.json').write_text(json.dumps({'counts':dict(stats),'winning21s':len(pr),'solutions':rows})+'\n')
