"""Separate source-graph, rooted partial-chart, unrooted completion, and signed Hamming readout symmetries. uv run --with networkx python ramsey_exoo_chart22_symmetry.py"""
from ramsey_exoo_root_readout import edges,Path,json
from itertools import permutations,product
from collections import Counter,defaultdict
import networkx as nx
D=Path(__file__).parent;E=edges();G=nx.Graph();G.add_nodes_from(range(39));G.add_edges_from(E);anchors={22,*G[22]};chart=G.copy();chart.remove_edges_from([(u,v) for u,v in E if not anchors.intersection((u,v))]);nx.set_node_attributes(chart,{i:2 if i==22 else int(i in anchors) for i in chart},'role');
def maps(g,roles=False):return nx.isomorphism.GraphMatcher(g,g,node_match=(lambda a,b:a['role']==b['role']) if roles else None).isomorphisms_iter()
def moved(p):return {i:j for i,j in p.items() if i!=j}
d=json.loads((D/'ramsey_exoo_chart22_words.json').read_text());vs=d['probes'];words=set(d['words']);M=len(words);fr=[sum(s[i]=='1' for s in words) for i in range(len(vs))];cells=defaultdict(list)
for i,n in enumerate(fr):cells[min(n,M-n)].append(i)
signed=[]
for ps in product(*(permutations(c) for c in cells.values())):
    p=dict(zip(sum(cells.values(),[]),sum(map(list,ps),[])));flip=[i for i,j in p.items() if fr[i]!=fr[j]];assert all(2*n!=M for n in fr)
    if all(''.join(str(int(s[p[i]])^(i in flip)) for i in range(len(vs))) in words for s in words):signed.append(dict(permutation=moved(p),flip=flip))
# Exact unrooted comparisons only within equal WL hashes; a hash match is never taken as an isomorphism proof.
classes=defaultdict(list);aut=Counter()
for w in sorted(words):
    H=G.copy()
    for v,x in zip(vs,w):
        if x=='1':H.add_edge(v,35)
        elif H.has_edge(v,35):H.remove_edge(v,35)
    aut[sum(1 for _ in maps(H))]+=1;k=nx.weisfeiler_lehman_graph_hash(H,iterations=5);lst=classes[k]
    for rep,ws in lst:
        if nx.is_isomorphic(rep,H):ws.append(w);break
    else:lst.append((H,[w]))
r=dict(source=[moved(p) for p in maps(G)],chart=[moved(p) for p in maps(chart,True)],signed_code=signed,completion_aut_orders=aut,unrooted_classes=[ws for lst in classes.values() for _,ws in lst]);print({k:(len(v) if k=='unrooted_classes' else v) for k,v in r.items()});(D/'ramsey_exoo_chart22_symmetry.json').write_text(json.dumps(r)+'\n')
