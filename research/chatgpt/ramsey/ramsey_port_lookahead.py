"""Enumerate attachments incl. shrinking maximal supports, then deduplicate unrooted output cores for the NEXT step."""
from ramsey_port_deletion_chain import search,D,json,independent,Counter
from ramsey_port_chain_from_17 import read_seed
from collections import defaultdict
import networkx as nx

def completions(H,k,d):
    n=len(H);todo=[];seen=set();search(H,k,d,lambda s,g:todo.append(tuple(sorted(s))))
    while todo:
        s=todo.pop()
        if s in seen:continue
        seen.add(s);G=H[:]+[0]*(d+1)
        for a,m in enumerate(s,n):
            G[a]=m|(1<<(n+d));G[-1]|=1<<a
            for i in range(n):
                if m>>i&1:G[i]|=1<<a
        if independent(G,(1<<len(G))-1,k):continue
        yield s,G
        for i,m in enumerate(s):
            while m:
                b=m&-m;m-=b;t=list(s);t[i]^=b;todo.append(tuple(sorted(t)))

def nxgraph(A):
    G=nx.empty_graph(len(A));G.add_edges_from((v,w) for v,r in enumerate(A) for w in range(v) if r>>w&1);return G

def layer(inputs,k):
    buckets=defaultdict(list);rows=[];total=0
    for idx,H in enumerate(inputs):
        for s,A in completions(H,k,4):
            total+=1;G=nxgraph(A);key=tuple(sorted(dict(G.degree()).values()));group=buckets[key]
            if any(nx.is_isomorphic(G,J) for J in group):continue
            group.append(G);rows.append({'source':idx,'supports':s,'graph':A})
    print(k,'valid multisets',total,'isotypes',len(rows),flush=True);return rows
if __name__=='__main__':
    seeds=[read_seed(l) for l in (D/'pauli-realization-catalogues/r36_17.g6').read_bytes().splitlines()];L=layer(seeds,7);M=layer([r['graph'] for r in L],8);out={'22s':L,'27s':M,'lookahead':[]}
    for idx,r in enumerate(M):
        H=r['graph']
        for d in (7,6,5,4):
            a=search(H,9,d)
            if 'graph' in a:break
        out['lookahead'].append({'idx':idx,'largest_tried_success':d if 'graph'in a else None,'certificate':a});print('capacity at 27',idx,d,'success', 'graph' in a,flush=True)
    (D/'ramsey_port_lookahead.json').write_text(json.dumps(out)+'\n')
