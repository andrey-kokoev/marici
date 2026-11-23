"""Replay known 22-state gate columns as two partial readings. Delete the candidate column by identifying crossing partners, then re-expand the tagged halves. Retrospective control, not a blind prediction."""
from pathlib import Path
import json,itertools
import networkx as nx
D=Path(__file__).parent; B=json.loads((D/'ramsey_long_circuit_2.json').read_text())['component'];G=nx.Graph();G.add_nodes_from(B);G.add_edges_from((x,y) for x,y in itertools.combinations(B,2) if (x^y).bit_count()==1);d=dict(nx.all_pairs_shortest_path_length(G));code=lambda x:0 if x>>2&1 else 3 if x>>17&1 else 1 if x>>4&1 else 2
out=[]
for bit in [1,2]:
 tag=lambda x:int(bool(code(x)&bit));cross=[(x,y) if not tag(x) else (y,x) for x,y in G.edges if tag(x)!=tag(y)];addr={x:x for x in B};assert len(set(itertools.chain.from_iterable(cross)))==2*len(cross)
 for x,y in cross:addr[y]=x
 halves=[{addr[x] for x in B if tag(x)==i} for i in [0,1]];edges=[{tuple(sorted([addr[x],addr[y]])) for x,y in G.edges if tag(x)==tag(y)==i} for i in [0,1]];I=halves[0]&halves[1];restr=[{e for e in E if set(e)<=I} for E in edges];assert restr[0]==restr[1];assert all(all((d[w][y]<d[w][x])==bool(tag(w)) for w in B) for x,y in cross);K=nx.Graph();K.add_nodes_from(I);K.add_edges_from(restr[0]);out.append(dict(bit=bit,half_sizes=list(map(len,halves)),addresses=len(set(addr.values())),interface=len(I),interface_edges=len(restr[0]),interface_components=sorted(map(len,nx.connected_components(K))),bridges=len(cross),within_edges=list(map(len,edges)),target_agreement=True))
print(out);(D/'ramsey_interface_replay.json').write_text(json.dumps(out,indent=2)+'\n')
