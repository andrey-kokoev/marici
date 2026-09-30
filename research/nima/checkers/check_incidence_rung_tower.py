"""Uniform shared-incidence promotion at each three-rung boundary.

Undirected simple supports; reciprocal arrows are display orientations and
identity loops are units excluded from structural edge counts. No path history.
"""
from itertools import combinations
from pathlib import Path
import json


def edge(a,b): return tuple(sorted((a,b)))
def directed(edges): return {p for a,b in edges for p in ((a,b),(b,a))}

def groups(arrows,vertices,field):
    return {v:sorted(p for p in arrows if p[field]==v) for v in vertices}

def promote(vertices,edges,level):
    # New vertex addresses denote old undirected edges, not duplicated histories.
    old=sorted(edges)
    names=[f'L{level}:{i}' for i in range(len(old))]
    new_edges={edge(names[i],names[j]) for i,j in combinations(range(len(old)),2)
               if set(old[i]) & set(old[j])}
    degrees={v:sum(v in e for e in edges) for v in vertices}
    assert len(new_edges)==sum(d*(d-1)//2 for d in degrees.values())
    assert len(new_edges)==len(set(new_edges))
    return tuple(names),new_edges


def run(name,seed):
    vertices=tuple('ABCD');edges=set(seed);rows=[]
    expected={'two_triangles':[(4,5),(5,8),(8,18),(18,64),(64,396)],
              'completed_tetrahedron':[(4,6),(6,12),(12,36),(36,180),(180,1620)]}[name]
    first_edge_pairs=None
    for level in range(5):
        assert (len(vertices),len(edges))==expected[level]
        arrows=directed(edges)
        assert len(arrows)==2*len(edges) and all(a!=b for a,b in arrows)
        source=groups(arrows,vertices,0);target=groups(arrows,vertices,1)
        assert {p for family in source.values() for p in family}==arrows
        assert {p for family in target.values() for p in family}==arrows
        r=12-3*level
        for offset,form in ((0,'flat arrows'),(1,'source-indexed'),(2,'target-indexed')):
            if r-offset<0: continue
            rows.append({'rung':r-offset,'promotion_level':level,'form':form,
                         'vertices':len(vertices),'undirected_edges':len(edges),
                         'directed_2_packets':len(arrows),'unit_identities':len(vertices)})
        if level==0:
            old=sorted(edges)
            first_edge_pairs=[[''.join(a),''.join(b)] for a,b in combinations(old,2) if set(a)&set(b)]
        if level<4: vertices,edges=promote(vertices,edges,level+1)
    return {'seed_edges':[''.join(e) for e in sorted(seed)],'rows':rows,
            'first_promotion_relationships':first_edge_pairs}


def main():
    original=('AB','BC','CA','BA','AD','DB')
    diamond={edge(*p) for p in original}
    tetra={edge(a,b) for a,b in combinations('ABCD',2)}
    assert len(diamond)==5 and tetra-diamond=={('C','D')}
    results={name:run(name,seed) for name,seed in
             (('two_triangles',diamond),('completed_tetrahedron',tetra))}
    # Octahedral identification: three opposite pairs of disjoint tetrahedral edges.
    opposites=[[''.join(a),''.join(b)] for a,b in combinations(sorted(tetra),2) if not set(a)&set(b)]
    assert len(opposites)==3
    report={'status':'passed','rule':'line graph: old edges are new vertices; share an old endpoint to relate',
            'rung_schedule':'flat -> source-indexed -> target-indexed -> promote; rung0 is next block rung12',
            'orientation':'undirected supports; both directed views available',
            'identities':'units, omitted from structural adjacency','results':results,'octahedral_opposites':opposites,
            'scope':'Four finite incidence promotions; changes the earlier Cartesian multiplication and closure-at-grouping schedules explicitly.'}
    dest=Path(__file__).resolve().parents[1]/'results'/'incidence-rung-tower.json'
    dest.write_text(json.dumps(report,indent=2)+'\n')
    print('PASS: uniform rung rule, both seeds, exact regrouping, four promotions, octahedral identification. Rung0 wraps without a second promotion.')

if __name__=='__main__': main()
