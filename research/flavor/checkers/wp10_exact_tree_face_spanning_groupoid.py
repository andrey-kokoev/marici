"""Exact spanning presentation using connected eight-link boundary faces."""
from collections import defaultdict
import itertools, json
from pathlib import Path

ATLAS=Path("research/flavor/results/wp10_sparse_fiber_face_atlas.json")
INC=Path("research/flavor/results/wp10_sparse_fiber_incidence_graph.json")
OUT=Path("research/flavor/results/wp10_exact_tree_face_spanning_groupoid.json")
PERMS=list(itertools.permutations(range(3)))

def slots(m): return [(i,j) for i in range(3) for j in range(3) if m&(1<<(3*i+j))]
def mask(es): return sum(1<<(3*i+j) for i,j in es)
def transport(m,q,c): return mask((q[i],c[j]) for i,j in slots(m))
def witness(pair,canon):
    for q,u,d in itertools.product(PERMS,repeat=3):
        if (transport(pair[0],q,u),transport(pair[1],q,d))==canon:
            return [list(q),list(u),list(d)]
    raise AssertionError((pair,canon))
def graph_cc(pair):
    edges=[(i,3+j) for i,j in slots(pair[0])]+[(i,6+j) for i,j in slots(pair[1])]
    p=list(range(9))
    def f(x):
        while p[x]!=x: p[x]=p[p[x]]; x=p[x]
        return x
    for x,y in edges:
        x,y=f(x),f(y); p[y]=x
    return len({f(i) for i in range(9)}),len(edges)

a=json.loads(ATLAS.read_text()); inc=json.loads(INC.read_text())
vc={v:i for i,c in enumerate(inc["components"]) for v in c["vertices"]}
vertices={v["id"]:v for v in inc["vertices"]}
occ=defaultdict(list)
for vs,faces in a["vertex_faces"].items():
    v=int(vs); mu,md=vertices[v]["member"]
    for x in faces:
        pair=(mu & ~(1<<(3*x["row"]+x["column"])) ,md) if x["sector"]=="u" else (mu,md & ~(1<<(3*x["row"]+x["column"])))
        occ[x["canonical_face"]].append((vc[v],v,x,pair))
tree_faces={f["canonical_face"]:f for f in a["faces"] if graph_cc(f["canonical_masks"])==(1,8)}
candidates=[]
for face in tree_faces:
    items=occ[face]
    by=defaultdict(list)
    for z in items: by[z[0]].append(z)
    for x,y in itertools.combinations(sorted(by),2): candidates.append((face,x,y,by[x][0],by[y][0]))
candidates.sort()
p=list(range(len(inc["components"])))
def find(x):
    while p[x]!=x:p[x]=p[p[x]];x=p[x]
    return x
chosen=[]
for face,x,y,l,r in candidates:
    fx,fy=find(x),find(y)
    if fx==fy: continue
    p[fy]=fx
    canon=tuple(tree_faces[face]["canonical_masks"])
    chosen.append({"components":[x,y],"canonical_face":face,
      "left":{"vertex":l[1],"deletion":l[2],"permutation_to_canonical":witness(l[3],canon)},
      "right":{"vertex":r[1],"deletion":r[2],"permutation_to_canonical":witness(r[3],canon)}})
assert len(chosen)==len(inc["components"])-1
assert len({find(i) for i in range(len(inc["components"]))})==1
out={"schema":"marici.flavor.exact_tree_face_spanning_groupoid.v1",
 "input_component_count":len(inc["components"]),"connected_tree_face_type_count":len(tree_faces),
 "eligible_tree_face_component_edge_count":len({tuple(sorted((x,y))) for _,x,y,_,_ in candidates}),
 "exact_spanning_edge_count":len(chosen),"exact_component_count":1,
 "reason":"Each selected face is a connected graph with 9 vertices and 8 links, hence a tree. It has no phase holonomy; support permutations and vertex rephasings give an exact weak-basis boundary arrow.",
 "spanning_edges":chosen}
OUT.write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps({k:v for k,v in out.items() if k!="spanning_edges"},indent=2))
