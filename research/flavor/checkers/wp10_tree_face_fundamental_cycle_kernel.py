"""Fundamental-cycle incidence kernel between tree-face smoothing normals."""
from collections import defaultdict, deque
import itertools, json
from pathlib import Path

from wp10_exact_tree_face_spanning_groupoid import (
    ATLAS, INC, PERMS, graph_cc, slots, transport, witness)

OUT=Path("research/flavor/results/wp10_tree_face_fundamental_cycle_kernel.json")
a=json.loads(ATLAS.read_text()); inc=json.loads(INC.read_text())
vertices={v["id"]:v for v in inc["vertices"]}
vc={v:i for i,c in enumerate(inc["components"]) for v in c["vertices"]}

def reduced(vertex,x):
    mu,md=vertex["member"]; bit=1<<(3*x["row"]+x["column"])
    return (mu&~bit,md) if x["sector"]=="u" else (mu,md&~bit)
def mapped_normal(x,p):
    q,u,d=p; return (x["sector"],q[x["row"]],(u if x["sector"]=="u" else d)[x["column"]])
def act(n,g):
    s,i,j=n;q,u,d=g;return(s,q[i],(u if s=="u" else d)[j])
def autos(pair):
    return [g for g in itertools.product(PERMS,repeat=3)
            if transport(pair[0],g[0],g[1])==pair[0]
            and transport(pair[1],g[0],g[2])==pair[1]]
def endpoints(edge):
    s,i,j=edge; return i,(3 if s=="u" else 6)+j
def face_edges(pair):
    return [("u",i,j) for i,j in slots(pair[0])]+[("d",i,j) for i,j in slots(pair[1])]
def cycle(pair,normal):
    adjacency=defaultdict(list)
    for edge in face_edges(pair):
        x,y=endpoints(edge); adjacency[x].append((y,edge)); adjacency[y].append((x,edge))
    start,end=endpoints(normal); queue=deque([end]); previous={end:None}
    while queue:
        x=queue.popleft()
        if x==start:break
        for y,e in adjacency[x]:
            if y not in previous: previous[y]=(x,e); queue.append(y)
    assert start in previous
    # Orient every labelled edge Q -> column. The normal coefficient is +1;
    # the tree path runs from its column endpoint back to its Q endpoint.
    vector={normal:1}; x=start
    while x!=end:
        px,e=previous[x]; q,col=endpoints(e)
        vector[e]=1 if (x,px)==(q,col) else -1
        x=px
    return vector
def dot(v,w): return sum(v.get(e,0)*w.get(e,0) for e in set(v)|set(w))

occ=defaultdict(lambda:defaultdict(list))
for vs,faces in a["vertex_faces"].items():
    vid=int(vs); vertex=vertices[vid]
    for x in faces:
        canonical=tuple(map(int,x["canonical_face"].split(":")))
        if graph_cc(canonical)!=(1,8):continue
        p=witness(reduced(vertex,x),canonical)
        occ[x["canonical_face"]][vc[vid]].append(
            {"vertex":vid,"deletion":x,"normal":mapped_normal(x,p)})

compatible={}
overlaps=defaultdict(int)
for face,by in occ.items():
    canonical=tuple(map(int,face.split(":"))); aa=autos(canonical)
    for ca,cb in itertools.combinations(sorted(by),2):
        hit=None
        for left in by[ca]:
            for right in by[cb]:
                va=cycle(canonical,left["normal"])
                for g in aa:
                    nb=act(right["normal"],g); value=dot(va,cycle(canonical,nb))
                    if value:
                        hit={"left":left,"right":right,"signed_cycle_overlap":value};break
                if hit:break
            if hit:break
        if hit:
            compatible.setdefault((ca,cb),{"faces":[]})["faces"].append(
                {"canonical_face":face,"witness":hit})
            overlaps[abs(hit["signed_cycle_overlap"])]+=1

parent=list(range(len(inc["components"])))
def find(x):
    while parent[x]!=x:parent[x]=parent[parent[x]];x=parent[x]
    return x
spanning=[]
for edge,data in sorted(compatible.items()):
    x,y=map(find,edge)
    if x==y:continue
    parent[y]=x;spanning.append({"components":list(edge),**data["faces"][0]})
groups=defaultdict(list)
for i in range(len(parent)):groups[find(i)].append(i)
out={"schema":"marici.flavor.tree_face_fundamental_cycle_kernel.v1",
 "compatible_component_pair_count":len(compatible),"absolute_overlap_histogram":dict(sorted(overlaps.items())),
 "component_count":len(groups),"component_sizes":sorted((len(x) for x in groups.values()),reverse=True),
 "spanning_edge_count":len(spanning),
 "criterion":"Nonzero signed edge-incidence pairing of the two fundamental cycles, allowing canonical-tree automorphisms.",
 "scope":"This certifies a labelled occurrence-module kernel, not yet physical weak-basis descent.",
 "spanning_edges":spanning}
OUT.write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps({k:v for k,v in out.items() if k!="spanning_edges"},indent=2))
