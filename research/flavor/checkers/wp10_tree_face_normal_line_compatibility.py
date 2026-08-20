"""Normal-line compatibility over the exact connected tree-face carrier atlas."""
from collections import defaultdict
import itertools, json
from pathlib import Path

from wp10_exact_tree_face_spanning_groupoid import (
    ATLAS, INC, PERMS, graph_cc, transport, witness)

OUT=Path("research/flavor/results/wp10_tree_face_normal_line_compatibility.json")
a=json.loads(ATLAS.read_text()); inc=json.loads(INC.read_text())
vertices={v["id"]:v for v in inc["vertices"]}
vc={v:i for i,c in enumerate(inc["components"]) for v in c["vertices"]}

def reduced(vertex,deletion):
    mu,md=vertex["member"]; bit=1<<(3*deletion["row"]+deletion["column"])
    return (mu & ~bit,md) if deletion["sector"]=="u" else (mu,md & ~bit)
def mapped_normal(deletion,perms):
    q,u,d=perms; cols=u if deletion["sector"]=="u" else d
    return (deletion["sector"],q[deletion["row"]],cols[deletion["column"]])
def act(n,g):
    s,i,j=n; q,u,d=g
    return (s,q[i],(u if s=="u" else d)[j])
def automorphisms(pair):
    return [g for g in itertools.product(PERMS,repeat=3)
            if transport(pair[0],g[0],g[1])==pair[0]
            and transport(pair[1],g[0],g[2])==pair[1]]

occ=defaultdict(lambda:defaultdict(list))
for vs,faces in a["vertex_faces"].items():
    vid=int(vs); vertex=vertices[vid]
    for deletion in faces:
        face=deletion["canonical_face"]
        canonical=tuple(map(int,face.split(":")))
        if graph_cc(canonical)!=(1,8): continue
        perms=witness(reduced(vertex,deletion),canonical)
        occ[face][vc[vid]].append({
            "vertex":vid,"deletion":deletion,
            "canonical_normal":mapped_normal(deletion,perms)})

compatible={}
for face,by_component in occ.items():
    canonical=tuple(map(int,face.split(":"))); autos=automorphisms(canonical)
    for ca,cb in itertools.combinations(sorted(by_component),2):
        hits=[]
        for left in by_component[ca]:
            for right in by_component[cb]:
                if any(act(left["canonical_normal"],g)==right["canonical_normal"]
                       for g in autos):
                    hits.append({"left":left,"right":right})
        if hits:
            compatible.setdefault((ca,cb),{"faces":[]})["faces"].append(
                {"canonical_face":face,"witness":hits[0]})

parent=list(range(len(inc["components"])))
def find(x):
    while parent[x]!=x: parent[x]=parent[parent[x]]; x=parent[x]
    return x
spanning=[]
for edge,data in sorted(compatible.items()):
    x,y=map(find,edge)
    if x==y: continue
    parent[y]=x; spanning.append({"components":list(edge),**data["faces"][0]})
groups=defaultdict(list)
for i in range(len(parent)):groups[find(i)].append(i)
out={"schema":"marici.flavor.tree_face_normal_line_compatibility.v1",
 "compatible_component_pair_count":len(compatible),
 "component_count":len(groups),
 "component_sizes":sorted((len(x) for x in groups.values()),reverse=True),
 "spanning_edge_count":len(spanning),
 "criterion":"The two deleted normals lie in the same automorphism orbit of a common canonical boundary tree.",
 "spanning_edges":spanning}
OUT.write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps({k:v for k,v in out.items() if k!="spanning_edges"},indent=2))
