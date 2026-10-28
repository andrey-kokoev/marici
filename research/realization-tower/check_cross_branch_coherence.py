"""Exact geometric comparison/fillers between retained shortest-path branches.

Elementary move: change one intermediate vertex across two lattice triangles.
Higher comparison: the difference between two face fillers bounds a chain of
actual tetrahedral/octahedral volume cells. No phase/reader law is inferred.
"""
from itertools import product, combinations
from collections import defaultdict, deque
from pathlib import Path
import json
from check_extended_cell_closure import sub, dot, cross

HOME=Path(__file__).parent


def plus(*chains):
    out=defaultdict(int)
    for chain,scale in chains:
        for cell,n in chain.items():out[cell]+=scale*n
    return {c:n for c,n in out.items() if n}


def oriented(vertices):
    ordered=tuple(sorted(vertices));indices=[ordered.index(v) for v in vertices]
    return ordered,(-1)**sum(indices[i]>indices[j] for i in range(len(indices)) for j in range(i+1,len(indices)))


def route(path):
    result={}
    for a,b in zip(path,path[1:]):
        edge,sign=oriented((a,b));result[edge]=result.get(edge,0)+sign
    return {e:n for e,n in result.items() if n}


def boundary2(chain):
    result={}
    for (a,b,c),n in chain.items():
        result=plus((result,1),({(a,b):1,(b,c):1,(a,c):-1},n))
    return result


def geometry(points):
    cells=[]
    bounds=[range(min(p[i] for p in points)-1,max(p[i] for p in points)+1) for i in range(3)]
    for c in product(*bounds):
        tet=tuple(sorted(p for d in product((0,1),repeat=3) if sum(p:=tuple(x+y for x,y in zip(c,d)))%2==0))
        if set(tet)<=points:cells.append(tet)
        if sum(c)%2:
            octa=tuple(sorted(tuple(c[i]+(s if i==axis else 0) for i in range(3)) for axis in range(3) for s in (-1,1)))
            if set(octa)<=points:cells.append(octa)
    facets=[];incidence=defaultdict(list)
    for index,cell in enumerate(cells):
        boundary={}
        for f in combinations(cell,3):
            a,b,c=f;n=cross(sub(b,a),sub(c,a));signs=[dot(n,sub(p,a)) for p in cell if p not in f]
            if all(s>0 for s in signs):boundary[f]=-1
            elif all(s<0 for s in signs):boundary[f]=1
        assert len(boundary)==(4 if len(cell)==4 else 8)
        assert not boundary2(boundary)
        for f,s in boundary.items():incidence[f].append((index,s))
        facets.append(boundary)
    assert all(len(v)<=2 for v in incidence.values())
    assert all(len(v)==1 or v[0][1]==-v[1][1] for v in incidence.values())
    return cells,facets,incidence


def fill_volume(cycle,facets,incidence):
    assert not boundary2(cycle)
    assert set(cycle)<=incidence.keys()
    # Solve d3*x=cycle over the dual cell graph, anchoring exterior coefficient 0.
    dual=defaultdict(list)
    for f,terms in incidence.items():
        (a,sa),(b,sb)=terms if len(terms)==2 else [terms[0],(-1,-terms[0][1])]
        dual[a].append((b,f,sa,sb));dual[b].append((a,f,sb,sa))
    values={-1:0};queue=deque([-1])
    while queue:
        a=queue.popleft()
        for b,f,sa,sb in dual[a]:
            value=(cycle.get(f,0)-sa*values[a])*sb  # sb is +/-1
            if b in values:assert values[b]==value,'inconsistent volume filler'
            else:values[b]=value;queue.append(b)
    assert len(values)==len(facets)+1
    result={i:n for i,n in values.items() if i!=-1 and n}
    recovered={}
    for i,n in result.items():recovered=plus((recovered,1),(facets[i],n))
    assert recovered==cycle
    return result


def audit(experiment):
    paths=[tuple(tuple(p) for p in c['path']) for c in experiment['cases']]
    records=[c['final_record'] for c in experiment['cases']]
    assert len(set(paths))==len(paths) and len(set(records))==len(records)
    points=set().union(*(set(p) for p in paths));cells,facets,incidence=geometry(points)
    groups=defaultdict(list)
    for i,path in enumerate(paths):
        for k in range(1,len(path)-1):groups[(k,path[:k]+path[k+1:])].append(i)
    edges=[];adj=defaultdict(list)
    for (k,_),group in groups.items():
        for i,j in combinations(group,2):
            p,q=paths[i],paths[j]
            if dot(sub(p[k],q[k]),sub(p[k],q[k]))!=2:continue
            a,b=p[k-1],p[k+1];chain={}
            for triangle in [(a,q[k],p[k]),(q[k],b,p[k])]:
                f,s=oriented(triangle);assert f in incidence
                chain=plus((chain,1),({f:s},1))
            assert boundary2(chain)==plus((route(q),1),(route(p),-1))
            e=len(edges);edges.append((i,j,chain));adj[i].append((j,e,1));adj[j].append((i,e,-1))
    # Root normalizations retain the actual chain; they do not identify archives.
    normal={0:{}};queue=deque([0]);tree=set()
    while queue:
        i=queue.popleft()
        for j,e,sign in adj[i]:
            if j not in normal:
                normal[j]=plus((normal[i],1),(edges[e][2],sign));tree.add(e);queue.append(j)
    assert len(normal)==len(paths),'disconnected branch comparison graph'
    for i,filler in normal.items():assert boundary2(filler)==plus((route(paths[i]),1),(route(paths[0]),-1))
    higher=[];nonzero=0
    for e,(i,j,local) in enumerate(edges):
        residual=plus((normal[i],1),(local,1),(normal[j],-1))
        filling=fill_volume(residual,facets,incidence)
        if filling:nonzero+=1
        higher.append({'edge':e,'volume_coefficients':filling})
    def encode(chain):return [{'vertices':list(cell),'coefficient':n} for cell,n in sorted(chain.items())]
    return {'initial_separation':experiment['original_separation'],'branches':len(paths),'comparison_edges':len(edges),
            'independent_graph_cycles':len(edges)-len(paths)+1,'connected':True,'volume_cells':len(cells),
            'nonzero_volume_fillers':nonzero,'retained_terminal_ids':records,
            'root_face_fillers':{str(i):encode(f) for i,f in normal.items()},
            'local_comparisons':[{'from':i,'to':j,'face_filler':encode(f)} for i,j,f in edges],
            'volume_cell_vertices':cells,'higher_comparisons':higher}


def main():
    source=json.loads((HOME/'results/recursive-branch-descent-v1.json').read_text())
    reports=[audit(experiment) for experiment in source['experiments']]
    # A single nonzero face is not a closed cycle and must not be filled as one.
    f=next(iter(reports[0]['root_face_fillers']['1']))['vertices'] if reports[0]['root_face_fillers']['1'] else None
    assert f is not None and boundary2({tuple(tuple(p) for p in f):1})
    output={'status':'pass','scope':'Oriented integral cellular-chain coherence for branch comparisons, not native coefficient/phase/reader coherence.',
            'reports':reports,'history_policy':'Every terminal branch record remains distinct; fillers compare their recovered geometric routes.',
            'no_particle_assignment':True}
    (HOME/'results/cross-branch-coherence-v1.json').write_text(json.dumps(output,indent=2)+'\n',encoding='utf-8')
    keys=['initial_separation','branches','comparison_edges','independent_graph_cycles','connected','volume_cells','nonzero_volume_fillers']
    print(json.dumps({'status':'pass','reports':[{k:r[k] for k in keys} for r in reports]}))


if __name__=='__main__':main()
