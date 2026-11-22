"""Run the adjacent frozen star-comparison pilot protocol. Labels are 1-based slots, 0 is root."""
from pathlib import Path
from itertools import combinations
import csv,json
import networkx as nx
D=Path(__file__).parent

def independent(h):
    I=[0]
    for i,n in enumerate(h):I.extend([s|1<<i for s in I if not s&n])
    return I

def load(p):
    m=[[int(x) for x in row] for row in csv.reader(p.open())];assert len(m)==22 and all(len(r)==22 for r in m)
    order=[0]+sorted(range(1,21),key=lambda v:(-m[0][v],v))+[21];h=[sum(m[i][j]<<k for k,j in enumerate(order)) for i in order];assert all(m[i][i]==0 for i in order) and all(m[i][j]==m[j][i] for i,j in combinations(order,2));assert all(not h[i]&h[j] for i,j in combinations(range(22),2) if h[i]>>j&1);assert max(s.bit_count() for s in independent(h))==6
    h=[n%2**21 for n in h[:21]];I=independent(h);six=[s for s in I if s.bit_count()==6];B=[s for s in I if all(s&t for t in six)];assert B;g=nx.Graph();g.add_nodes_from(range(21));g.add_edges_from((i,j) for i,j in combinations(range(21),2) if h[i]>>j&1);return p.name,h,B,g
cores=[load(p) for p in sorted(D.glob('ramsey_3_7_*22.csv'))];hits=[]
for a,h,B,g in cores:
    for b,k,C,f in cores:
        if a==b or h[0]!=k[0]:continue
        for i,j in combinations(range(1,21),2):
            mask=(1<<i)|(1<<j);s=next((s for s in B if s&mask==mask),None)
            if s is None or not k[i]>>j&1:continue
            assert not any(t&mask==mask for t in C);hits.append(dict(yes=a,no=b,pair=[i,j],red_slots=[v for v in range(21) if s>>v&1],root_red=[v for v in range(21) if h[0]>>v&1],borders=[len(B),len(C)],isomorphic=nx.is_isomorphic(g,f)));break
print([(a,h[0].bit_count(),len(B)) for a,h,B,g in cores]);print(hits[:2]);D.joinpath('ramsey_37_graph_merge.json').write_text(json.dumps(hits,indent=2)+'\n')
